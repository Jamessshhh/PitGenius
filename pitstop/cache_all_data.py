import fastf1
from fastf1 import plotting
import os

# Enable cache directory
fastf1.Cache.enable_cache('data/cache')

# Define years and sessions you want
years = [2023, 2024]
sessions = ['R', 'Q']  # Race and Qualifying

for year in years:
    print(f"\n🏁 Starting data fetch for {year} season...")
    schedule = fastf1.get_event_schedule(year)
    
    for event in schedule.iterrows():
        gp_name = event[1]['EventName']
        round_num = event[1]['RoundNumber']

        for session_type in sessions:
            try:
                print(f"➡️  Fetching {year} {gp_name} - {session_type}")
                session = fastf1.get_session(year, round_num, session_type)
                session.load(laps=True, telemetry=False)
                print(f"✅ Cached {gp_name} ({session_type}) successfully!\n")
            except Exception as e:
                print(f"⚠️ Skipped {gp_name} ({session_type}) due to error: {e}\n")
