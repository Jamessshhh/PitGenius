import streamlit as st
import pandas as pd
import fastf1
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

# ----------------------------
# ⚙️ Streamlit Configuration
# ----------------------------
st.set_page_config(
    page_title="🏁 F1 Pit Stop Intelligence Center",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: white;
    }
    div.block-container {padding-top: 1rem;}
    h1, h2, h3 { color: #00ADB5 !important; }
    .signature {
        color: #00ADB5;
        font-weight: bold;
        text-shadow: 0px 0px 10px #00ADB5;
        font-size: 17px;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# 🚀 Load Cached Data
# ----------------------------
@st.cache_data
def load_data():
    fastf1.Cache.enable_cache('data/cache')
    seasons = [2023, 2024]
    all_data = []

    for year in seasons:
        schedule = fastf1.get_event_schedule(year)
        for _, event in schedule.iterrows():
            try:
                session = fastf1.get_session(year, event['EventName'], 'R')
                session.load(laps=True, telemetry=False)
                laps = session.laps
                laps['Year'] = year
                laps['Event'] = event['EventName']
                all_data.append(laps)
            except:
                continue

    return pd.concat(all_data, ignore_index=True)

st.sidebar.header("🏎️ Control Panel")
st.sidebar.write("Filter data to customize your analytics")

all_laps = load_data()

# ----------------------------
# 🎛️ Sidebar Filters
# ----------------------------
years = st.sidebar.multiselect("Select Season(s)", sorted(all_laps['Year'].unique()), default=[2023, 2024])
events = st.sidebar.multiselect("Select Races", sorted(all_laps['Event'].unique()), default=None)
drivers = st.sidebar.multiselect("Select Drivers", sorted(all_laps['Driver'].unique()), default=['VER', 'HAM'])

filtered = all_laps[all_laps['Year'].isin(years)]
if events:
    filtered = filtered[filtered['Event'].isin(events)]
if drivers:
    filtered = filtered[filtered['Driver'].isin(drivers)]

# ----------------------------
# 🏁 TITLE & SIGNATURE
# ----------------------------
st.title("🏁 Formula 1 Pit Stop & Race Intelligence Dashboard")
st.caption("Visual analysis of pit stop patterns, tyre usage, and race intelligence (OPI, SES, RII) for 2023–2024 F1 seasons.")
st.markdown("<p class='signature'>⚡ Crafted by Ritesh Mahara — Turning Data into Drive 🏎️</p>", unsafe_allow_html=True)

# ----------------------------
# 🧭 TABS
# ----------------------------
tab1, tab2, tab3 = st.tabs(["🏎️ Pit Stop Analytics", "🧤 Tyre & Degradation", "🧠 Race Intelligence Metrics"])

# ----------------------------
# TAB 1: PIT STOP ANALYTICS
# ----------------------------
with tab1:
    st.subheader("🔧 Total Pit Stops per Driver")
    pit_data = filtered.dropna(subset=['PitInTime', 'PitOutTime'])
    pit_summary = (
        pit_data.groupby(['Year', 'Driver'])
        .size()
        .reset_index(name='TotalPitStops')
    )
    fig1 = px.bar(
        pit_summary, x='Driver', y='TotalPitStops', color='Year',
        title="Total Pit Stops per Driver", height=500, template='plotly_dark'
    )
    st.plotly_chart(fig1, use_container_width=True)

    if 'Team' in filtered.columns:
        st.subheader("🔩 Average Pit Stops per Team per Season")
        team_summary = (
            pit_data.groupby(['Year', 'Team'])
            .size()
            .reset_index(name='TotalPitStops')
        )
        fig2 = px.bar(
            team_summary, x='Team', y='TotalPitStops', color='Year',
            title="Average Pit Stops per Team", template='plotly_dark'
        )
        st.plotly_chart(fig2, use_container_width=True)

# ----------------------------
# TAB 2: TYRE & DEGRADATION
# ----------------------------
with tab2:
    st.subheader("🧤 Tyre Compound Usage Across Seasons")
    tyre_usage = (
        filtered[['Year', 'Compound']]
        .dropna()
        .groupby(['Year', 'Compound'])
        .size()
        .reset_index(name='Count')
    )
    fig3 = px.bar(
        tyre_usage, x='Compound', y='Count', color='Year',
        barmode='group', title="Tyre Compound Usage", template='plotly_dark'
    )
    st.plotly_chart(fig3, use_container_width=True)

    st.subheader("📉 Lap Time Degradation Over Laps")
    if not filtered.empty and 'LapTime' in filtered:
        filtered = filtered.copy()
        filtered['LapTimeSeconds'] = filtered['LapTime'].dt.total_seconds()
        fig4 = px.line(
            filtered, x='LapNumber', y='LapTimeSeconds', color='Driver',
            title="Lap Time Degradation", template='plotly_dark'
        )
        st.plotly_chart(fig4, use_container_width=True)

# ----------------------------
# TAB 3: RACE INTELLIGENCE METRICS
# ----------------------------
with tab3:
    st.subheader("🧠 Performance Intelligence Index")

    # Prepare data
    perf_data = (
        filtered.groupby(['Year', 'Driver'])
        .agg({'LapTime': 'mean', 'LapNumber': 'count'})
        .reset_index()
        .rename(columns={'LapTime': 'AvgLapTime', 'LapNumber': 'TotalLaps'})
    )
    perf_data['AvgLapTime'] = perf_data['AvgLapTime'].dt.total_seconds()

    # Create synthetic intelligence metrics
    perf_data['ConsistencyIndex'] = 100 - (perf_data['AvgLapTime'] / perf_data['AvgLapTime'].max() * 100)
    scaler = MinMaxScaler()
    perf_data[['NormAvgLapTime', 'NormConsistency']] = scaler.fit_transform(
        perf_data[['AvgLapTime', 'ConsistencyIndex']]
    )

    perf_data['OPI'] = (1 - perf_data['NormAvgLapTime']) * 100
    perf_data['SES'] = perf_data['NormConsistency'] * 100
    perf_data['RaceIntelligenceIndex'] = (perf_data['OPI'] + perf_data['SES']) / 2

    st.dataframe(perf_data[['Year', 'Driver', 'AvgLapTime', 'TotalLaps', 'OPI', 'SES', 'RaceIntelligenceIndex']], use_container_width=True)

    st.subheader("📊 OPI vs SES Scatter Visualization")
    fig5 = px.scatter(
        perf_data, x='OPI', y='SES', color='Driver',
        size='RaceIntelligenceIndex', hover_data=['Year'],
        title="Performance vs Strategy Efficiency (OPI vs SES)", template='plotly_dark'
    )
    st.plotly_chart(fig5, use_container_width=True)

    st.subheader("🏆 Top 10 Drivers by Race Intelligence Index")
    top_drivers = perf_data.sort_values('RaceIntelligenceIndex', ascending=False).head(10)
    fig6 = px.bar(
        top_drivers, x='Driver', y='RaceIntelligenceIndex', color='Year',
        title="Top 10 Drivers by Race Intelligence Index", template='plotly_dark'
    )
    st.plotly_chart(fig6, use_container_width=True)

# ----------------------------
# 🏁 FOOTER
# ----------------------------
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #999; font-size: 15px;'>
        💡 Built with ❤️ using <b>Streamlit</b>, <b>FastF1</b> & <b>Plotly</b><br>
        Data Source: Formula 1 Telemetry (2023–2024)
        <br><br>
        <span style='font-size:17px; color:#00ADB5; text-shadow: 0px 0px 10px #00ADB5;'>
            ⚡ Crafted by <b>Ritesh Mahara</b> — "Turning Data into Drive."
        </span>
    </div>
""", unsafe_allow_html=True)
