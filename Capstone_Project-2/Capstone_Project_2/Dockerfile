# Dockerfile

# Base image
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 5000
EXPOSE 8501

# Run both Flask (backend) and Streamlit (frontend)
CMD ["bash", "-c", "python app.py & streamlit run app_streamlit.py --server.port=8501 --server.address=0.0.0.0"]
