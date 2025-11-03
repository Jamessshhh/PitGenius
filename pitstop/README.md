# 🏎️ Formula 1 Pit Stop Strategy Optimization Using Python

**A comprehensive data-driven analysis of Formula 1 race strategies, pit stop timing, and tyre degradation patterns**

---

## 👨‍🎓 Author Information

**Ritesh Mahara**  
SRM Institute of Science and Technology, Kattankulathur  
Academic Year: 2025

---

## 🧠 Project Overview

This project analyzes and models Formula 1 race strategies — focusing on **pit stop timing, tyre degradation, and driver consistency** — using real race data from the **2023 and 2024 F1 seasons**.

By leveraging **FastF1**, **Pandas**, **Seaborn**, **Scikit-learn**, and **Plotly**, the project aims to discover **optimal pit windows**, **tyre performance patterns**, and **strategic intelligence indices (OPI & SES)** that influence race outcomes.

---

## ⚙️ Key Objectives

1. 📊 Collect and process Formula 1 race data (2023–2024 seasons)
2. 🛠️ Analyze pit stop frequency, duration, and tyre compound choices
3. 🔥 Model tyre degradation across stints for all drivers and teams
4. 🤖 Build performance indicators:
   - **Optimal Performance Index (OPI)** – measures driver consistency & pace
   - **Strategy Execution Score (SES)** – measures strategic pit timing efficiency
5. 🧩 Develop visual insights and an optional Streamlit dashboard
6. 📈 Identify the most efficient teams and drivers in race management

---

## 🚀 Setup Instructions

### 1️⃣ Create and activate environment
```bash
conda create -n pitstop python=3.10
conda activate pitstop
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Enable FastF1 cache
```python
import fastf1
fastf1.Cache.enable_cache('data/cache')
```

### 4️⃣ Run the notebooks
```bash
jupyter notebook
```

### 5️⃣ (Optional) Run Streamlit dashboard
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
PITSTOP-STRATEGY/
│
├── data/
│   └── cache/                     # FastF1 cached race data
│       ├── 2023/                  # 2023 season data
│       ├── 2024/                  # 2024 season data
│       └── fastf1_http_cache.sqlite
│
├── models/                        # Trained models and artifacts
│
├── notebooks/
│   ├── .ipynb_checkpoints/
│   ├── 1_data_exploration.ipynb   # Data collection and exploration
│   ├── all_laps.csv              # Processed lap data
│   └── race_intelligence.csv      # Strategic analysis data
│
├── src/                          # Source code modules
│
├── app.py                        # Streamlit dashboard application
├── cache_all_data.py             # Script to cache F1 data
├── main.py                       # Main execution script
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies
```

---

## 🧮 Methodology Summary

| Step | Focus                | Description                                              |
| ---- | -------------------- | -------------------------------------------------------- |
| 1️⃣  | Data Loading         | Load 2023–2024 race data via FastF1                      |
| 2️⃣  | Cleaning             | Select relevant variables (lap time, stint, compound)    |
| 3️⃣  | Pit Stop Analysis    | Analyze average pit stops per driver and team            |
| 4️⃣  | Tyre Stint Study     | Visualize tyre performance trends                        |
| 5️⃣  | Degradation Modeling | Fit regression models on lap time vs stint               |
| 6️⃣  | Performance Metrics  | Derive OPI and SES indices                               |
| 7️⃣  | Dashboard            | Create interactive data visualization (Plotly/Streamlit) |

---

## 📊 Key Insights

- **Soft tyres** degrade quickly but provide faster initial pace
- **Medium tyres** offer balanced performance across most tracks
- **Red Bull and Ferrari** show higher SES scores due to better strategy timing
- Drivers with steady lap pacing achieve higher **OPI (Optimal Performance Index)**
- Multiple-pit strategies can outperform single-stop plans in high-temperature races

---

## 🧠 Performance Metrics

### Optimal Performance Index (OPI)
Measures driver consistency and pace management across race stints.

**Components:**
- Average lap time percentile (40%)
- Lap time standard deviation (30%)
- Stint management score (30%)

### Strategy Execution Score (SES)
Evaluates pit stop timing efficiency and strategic decision quality.

**Components:**
- Pit window optimality (50%)
- Compound choice efficiency (30%)
- Undercut/overcut success (20%)

---

## 🏁 Outcome

This project demonstrates how data analytics can optimize pit stop timing and tyre strategy in Formula 1. It bridges sports analytics, machine learning, and strategic modeling, proving how AI-driven insights can improve on-track decisions.

---

## 🔮 Future Enhancements

- Integrate real-time weather API (OpenWeather)
- Add predictive race simulation using machine learning
- Use deep learning for dynamic tyre wear forecasting
- Expand dashboard for real-time telemetry comparisons

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙏 Acknowledgments

- **FastF1** - The excellent Python library for F1 timing data
- **Formula 1** - For publicly available timing and telemetry data
- **SRM Institute of Science and Technology** - Academic support and resources

---

**⭐ Star this repository if you find it helpful!**

Made with ❤️ by Ritesh Mahara