# app_streamlit.py
import streamlit as st
import requests
import pandas as pd
import json

st.set_page_config(page_title="Heart Disease Predictor", page_icon="❤️", layout="centered")
st.title("❤️ Heart Disease Prediction App")

st.sidebar.header("Enter Patient Information")

# Collect user input
input_data = {
    "age": st.sidebar.number_input("Age", 1, 120, 45),
    "sex": st.sidebar.selectbox("Sex (1=Male, 0=Female)", [0, 1]),
    "chest_pain_type": st.sidebar.selectbox("Chest Pain Type", [0, 1, 2, 3]),
    "resting_blood_pressure": st.sidebar.number_input("Resting Blood Pressure (mm Hg)", 50, 200, 120),
    "cholesterol": st.sidebar.number_input("Cholesterol (mg/dl)", 100, 600, 200),
    "fasting_blood_sugar": st.sidebar.selectbox("Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)", [0, 1]),
    "resting_ecg": st.sidebar.selectbox("Resting ECG", [0, 1, 2]),
    "max_heart_rate": st.sidebar.number_input("Max Heart Rate", 60, 220, 150),
    "exercise_induced_angina": st.sidebar.selectbox("Exercise Induced Angina (1=Yes, 0=No)", [0, 1]),
    "st_depression": st.sidebar.number_input("ST Depression", 0.0, 10.0, 1.0),
    "st_slope": st.sidebar.selectbox("ST Slope", [0, 1, 2]),
    "num_major_vessels": st.sidebar.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3]),
    "thalassemia": st.sidebar.selectbox("Thalassemia (0–3)", [0, 1, 2, 3]),
}

if st.button("Predict"):
    api_url = "http://localhost:5000/predict"
    response = requests.post(api_url, json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {'Heart Disease Detected' if result['heart_disease_prediction'] == 1 else 'No Heart Disease'}")
        st.metric(label="Probability", value=f"{result['probability']*100:.2f}%")
    else:
        st.error("Error: Unable to connect to API or invalid response.")
