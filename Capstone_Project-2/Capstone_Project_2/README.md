# ❤️ Heart Disease Prediction (ML+Flask + Streamlit + Docker)

## 🧩 Overview
This project predicts the likelihood of heart disease using a trained ML model, deployed through:
- **Flask API** for backend inference
- **Streamlit UI** for frontend interaction
- **Docker** for easy containerized deployment

---

## 🏗️ Setup

### Run It On Docker

### 1. Build Docker Image
```bash
docker build -t heart-predictor .
```

### 2. Run the Container 
```commandline
docker run -p 5000:5000 -p 8501:8501 heart-predictor
```