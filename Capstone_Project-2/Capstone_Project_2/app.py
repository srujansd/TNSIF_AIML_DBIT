# app_flask.py
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load("heart_disease_model.joblib")

@app.route('/')
def home():
    return jsonify({"message": "Heart Disease Prediction Flask API is running!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        prediction = model.predict(df)[0]
        probability = (
            model.predict_proba(df)[0][1] if hasattr(model, "predict_proba") else None
        )

        return jsonify({
            "heart_disease_prediction": int(prediction),
            "probability": float(probability) if probability is not None else None
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
