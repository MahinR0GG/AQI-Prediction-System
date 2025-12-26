import streamlit as st
import pandas as pd
import numpy as np
import pickle

# --------------------
# Load model & scaler
# --------------------
with open("aqi_models.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

# --------------------
# App UI
# --------------------
st.set_page_config(page_title="AQI Predictor", layout="centered")

st.title("🌫️ AQI Prediction App")
st.write("Predict Air Quality Index based on pollution levels.")

# --------------------
# User Inputs
# --------------------
pm25 = st.number_input("PM2.5", min_value=0.0, step=0.1)
pm10 = st.number_input("PM10", min_value=0.0, step=0.1)
temperature = st.number_input("Temperature (°C)", step=0.1)

month = st.selectbox("Month", list(range(1, 13)))
weekday = st.selectbox(
    "Weekday",
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)

location = st.selectbox(
    "Location",
    ["Ankara", "Bursa", "Istanbul", "Izmir"]
)

# --------------------
# Encode inputs
# --------------------
weekday_map = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6
}

weekday_val = weekday_map[weekday]

# one-hot encoding (match training!)
location_bursa = 1 if location == "Bursa" else 0
location_istanbul = 1 if location == "Istanbul" else 0
location_izmir = 1 if location == "Izmir" else 0
# Ankara is the reference city (all zeros)

# --------------------
# Create input DataFrame
# --------------------
input_data = pd.DataFrame([[
    pm25,
    pm10,
    temperature,
    month,
    weekday_val,
    location_bursa,
    location_istanbul,
    location_izmir
]], columns=[
    "pm2.5",
    "pm10",
    "temperature",
    "month",
    "weekday",
    "location_Bursa",
    "location_Istanbul",
    "location_Izmir"
])

# --------------------
# Prediction
# --------------------
if st.button("Predict AQI"):
    scaled_input = scaler.transform(input_data)
    prediction = model.predict(scaled_input)

    st.success(f"✅ Predicted AQI: {prediction[0]:.2f}")
