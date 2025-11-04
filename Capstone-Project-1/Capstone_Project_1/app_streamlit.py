# app_streamlit.py
import streamlit as st
import pandas as pd
import joblib

# ------------------------------
# ⚙️ App Configuration
# ------------------------------
st.set_page_config(
    page_title="Equipment Output Predictor",
    page_icon="⚙️",
    layout="centered",
)

# ------------------------------
# 🏭 App Header
# ------------------------------
st.markdown(
    """
    <div style="text-align:center; padding:10px; background:linear-gradient(90deg, #0072ff, #00c6ff); border-radius:12px;">
        <h1 style="color:white;">⚙️ Equipment Output Predictor</h1>
        <p style="color:white; font-size:16px;">Predict the parts produced per hour using machine and process parameters.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# 📦 Load Trained Model
# ------------------------------
MODEL_PATH = "equipment_output_model_best.joblib"
model = joblib.load(MODEL_PATH)

st.sidebar.header("📊 Enter Input Features")

# ------------------------------
# 🧠 Input Fields
# ------------------------------
Injection_Temperature = st.sidebar.number_input("Injection Temperature (°C)", 100, 300, 200)
Injection_Pressure = st.sidebar.number_input("Injection Pressure (bar)", 20, 100, 50)
Cycle_Time = st.sidebar.number_input("Cycle Time (s)", 10, 100, 30)
Cooling_Time = st.sidebar.number_input("Cooling Time (s)", 5, 50, 10)
Material_Viscosity = st.sidebar.number_input("Material Viscosity", 0.1, 10.0, 1.0)
Ambient_Temperature = st.sidebar.number_input("Ambient Temperature (°C)", 10, 50, 25)
Machine_Age = st.sidebar.number_input("Machine Age (years)", 0, 15, 5)
Operator_Experience = st.sidebar.number_input("Operator Experience (years)", 0, 20, 3)
Maintenance_Hours = st.sidebar.number_input("Maintenance Hours", 0, 100, 10)
Temperature_Pressure_Ratio = st.sidebar.number_input("Temperature Pressure Ratio", 0.1, 10.0, 4.0)
Total_Cycle_Time = st.sidebar.number_input("Total Cycle Time (s)", 10, 200, 40)
Efficiency_Score = st.sidebar.slider("Efficiency Score", 0.0, 1.0, 0.9)
Machine_Utilization = st.sidebar.slider("Machine Utilization (%)", 0, 100, 85)

Shift = st.sidebar.selectbox("Shift", ["Morning", "Evening", "Night"])
Machine_Type = st.sidebar.selectbox("Machine Type", ["TypeA", "TypeB", "TypeC"])
Material_Grade = st.sidebar.selectbox("Material Grade", ["A", "B", "C"])
Day_of_Week = st.sidebar.selectbox("Day of Week", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])

# ------------------------------
# 📘 Prepare DataFrame for Model
# ------------------------------
input_data = pd.DataFrame([{
    "Injection_Temperature": Injection_Temperature,
    "Injection_Pressure": Injection_Pressure,
    "Cycle_Time": Cycle_Time,
    "Cooling_Time": Cooling_Time,
    "Material_Viscosity": Material_Viscosity,
    "Ambient_Temperature": Ambient_Temperature,
    "Machine_Age": Machine_Age,
    "Operator_Experience": Operator_Experience,
    "Maintenance_Hours": Maintenance_Hours,
    "Shift": Shift,
    "Machine_Type": Machine_Type,
    "Material_Grade": Material_Grade,
    "Day_of_Week": Day_of_Week,
    "Temperature_Pressure_Ratio": Temperature_Pressure_Ratio,
    "Total_Cycle_Time": Total_Cycle_Time,
    "Efficiency_Score": Efficiency_Score,
    "Machine_Utilization": Machine_Utilization
}])

# ------------------------------
# 🔮 Prediction
# ------------------------------
st.markdown("### 🧾 Prediction Result")

if st.button("🚀 Predict Output"):
    prediction = model.predict(input_data)
    st.success(f"🔹 **Predicted Parts Per Hour:** {prediction[0]:.2f}")
    st.balloons()

# ------------------------------
# 📄 Footer
# ------------------------------
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:gray;">
        Built with ❤️ using <b>Streamlit</b> + <b>Linear Regression</b> Model.
    </p>
    """,
    unsafe_allow_html=True
)
