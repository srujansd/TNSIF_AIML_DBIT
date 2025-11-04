# app.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd
import os

app = Flask(__name__)

# Load model
MODEL_PATH = "equipment_output_model_best.joblib"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Equipment Output Prediction API"})

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])

    # Compute engineered features (if applicable)
    try:
        if "Temperature_Pressure_Ratio" in model.named_steps["preprocessor"].transformers_[0][2]:
            df["Temperature_Pressure_Ratio"] = df["Injection_Temperature"] / df["Injection_Pressure"]
        if "Total_Cycle_Time" in model.named_steps["preprocessor"].transformers_[0][2]:
            df["Total_Cycle_Time"] = df["Cycle_Time"] + df["Cooling_Time"]
    except Exception:
        pass  # skip if model doesn't need these

    pred = model.predict(df)
    return jsonify({"Predicted_Parts_Per_Hour": float(pred[0])})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
