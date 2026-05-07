# SmartGrid AI ⚡ FINAL VERSION

## 🚀 Overview
AI-powered EV Charging Optimization & Infrastructure Planning System.

## 🔥 Features
- LSTM Demand Prediction
- Smart Charging Optimization (Peak Reduction)
- Explainable AI Recommendations
- Hotspot Detection
- Map-based Station Recommendation
- Dashboard + API
- Before vs After Impact Visualization

## ⚙️ Setup Instructions

### 1. Install Dependencies
pip install -r requirements.txt

### 2. Generate Data
python utils/data_generator.py

### 3. Run Backend
uvicorn api.main:app --reload

### 4. Run Dashboard
streamlit run dashboard/app.py

---

## 🌍 Deployment

### Backend (Render)
- Build: pip install -r requirements.txt
- Start: uvicorn api.main:app --host 0.0.0.0 --port 10000

### Dashboard (Streamlit Cloud)
- Upload repo → select dashboard/app.py → deploy

---

## 🎤 Pitch
We predict EV demand, optimize charging schedules, and recommend infrastructure locations, reducing peak load by ~30%.

