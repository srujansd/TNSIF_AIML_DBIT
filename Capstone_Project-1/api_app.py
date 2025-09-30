# api_app.py

import pandas as pd
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

# --- Configuration ---
MODEL_FILENAME = 'linear_regression_pipeline.pkl'

# --- 1. Load Model ---
# Load the full pipeline (preprocessor + model) saved from the Jupyter Notebook
try:
    pipeline = joblib.load(MODEL_FILENAME)
    print("Model pipeline loaded successfully.")
except FileNotFoundError:
    print(f"ERROR: Model file {MODEL_FILENAME} not found. Ensure the notebook was run and the file is present.")
    pipeline = None

# --- 2. FastAPI Application Setup ---
app = FastAPI(
    title="Manufacturing Output Predictor",
    description="Predicts Parts_Per_Hour based on machine settings."
)

# --- 3. Define Input Schema (Pydantic Model for Data Validation) ---
# This ensures that any incoming request has the exact 17 features in the correct type.
class MachineParameters(BaseModel):
    Injection_Temperature: float
    Injection_Pressure: float
    Cycle_Time: float
    Cooling_Time: float
    Material_Viscosity: float
    Ambient_Temperature: float
    Machine_Age: float
    Operator_Experience: float
    Maintenance_Hours: float
    Shift: Literal['Day', 'Night', 'Evening']
    Machine_Type: Literal['Type_A', 'Type_B', 'Type_C'] # Assuming Type_C exists based on dataset snippet
    Material_Grade: Literal['Economy', 'Standard', 'Premium']
    Day_of_Week: Literal['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    Temperature_Pressure_Ratio: float
    Total_Cycle_Time: float
    Efficiency_Score: float
    Machine_Utilization: float

# --- 4. API Endpoints ---

@app.get("/")
def health_check():
    """Simple check to confirm the API is running."""
    return {"status": "OK", "model_loaded": pipeline is not None}

@app.post("/predict")
def predict_output(data: MachineParameters):
    """
    Accepts machine operating parameters and returns the predicted Parts_Per_Hour.
    """
    if pipeline is None:
        return {"error": "Model not loaded. Check server logs."}
        
    try:
        # Convert the Pydantic data into a Pandas DataFrame for the pipeline
        input_data = data.model_dump()
        input_df = pd.DataFrame([input_data])

        # Define the exact order of features as used during training
        feature_order = [
            'Injection_Temperature', 'Injection_Pressure', 'Cycle_Time', 'Cooling_Time',
            'Material_Viscosity', 'Ambient_Temperature', 'Machine_Age', 'Operator_Experience',
            'Maintenance_Hours', 'Shift', 'Machine_Type', 'Material_Grade', 'Day_of_Week',
            'Temperature_Pressure_Ratio', 'Total_Cycle_Time', 'Efficiency_Score', 'Machine_Utilization'
        ]
        input_df = input_df[feature_order]

        # Make the prediction
        prediction = pipeline.predict(input_df)[0]
        
        # Ensure output is non-negative, as production cannot be negative
        predicted_output = max(0, prediction)

        return {
            "predicted_parts_per_hour": round(predicted_output, 2),
            "model_used": "Linear Regression"
        }

    except Exception as e:
        return {"error": f"An unexpected error occurred: {e}"}