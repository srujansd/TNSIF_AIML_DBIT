# ⚙️ Equipment Output Predictor

A Streamlit web app that predicts **Parts Per Hour** for manufacturing equipment using process and machine parameters.  
Built using **Linear Regression**, it helps visualize and estimate production efficiency based on user input.

---

## 🧠 Features

- Predicts parts per hour using process parameters
- Clean and responsive Streamlit UI
- Sidebar controls for all model input features
- Real-time results with confidence visualization
- Easy to deploy via Docker or locally

---

## 🧩 Tech Stack

- **Python 3.11**
- **Streamlit**
- **Scikit-learn (Linear Regression)**
- **Pandas / NumPy**
- **Docker (for deployment)**

---


## Running On Docker

### 1️⃣ Build the image
```bash
docker build -t equipment-output-predictor .
```

### 2️⃣ Run the container
```bash
docker run -p 8501:8501 equipment-output-predictor
```