# 🌫️ AQI Prediction System

A Machine Learning–based Air Quality Index (AQI) Prediction System that predicts the numerical AQI value from pollutant concentrations and classifies air quality into standard AQI categories. The project also includes an interactive Streamlit web application for real-time AQI prediction.

---

## 📌 Problem Statement
Air pollution has a significant impact on human health and the environment. Predicting the Air Quality Index (AQI) based on pollutant concentrations helps assess pollution levels and enables early preventive measures. This project aims to build a predictive system that estimates AQI using machine learning techniques.

---

## 🎯 Objectives
- Analyze air quality data containing major pollutants
- Predict the AQI value using machine learning regression models
- Classify AQI into standard air quality categories
- Build an interactive Streamlit-based web application
- Visualize and interpret air quality predictions

---

## 🧠 Dataset
- **Name:** Air Quality Prediction Dataset  
- **Source:** Kaggle  
- **Dataset Link:** https://www.kaggle.com/datasets/sahideseker/air-quality-prediction-dataset  

### Features Used:
- PM2.5
- PM10
- NO2
- SO2
- CO
- O3

### Target Variable:
- `AQI` (Numerical AQI value)

AQI categories are derived from the predicted AQI value using standard AQI classification ranges.

---

## 🏗️ Project Structure
AQI-PREDICTION-SYSTEM/
│
├── venv/
├── 16_air_quality_prediction.csv
├── app.py
├── aqi_models.pkl
├── scaler.pkl
├── main.ipynb
├── ReadMe.md


---

## 🚀 Getting Started (After Cloning)

Follow these steps to run the project locally.

---

### 1. Clone the Repository

```bash
git clone <repository-url>
cd AQI-PREDICTION-SYSTEM

### 2. Create and activate venv

python -m venv venv
venv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run streamlit application

streamlit run app.py
