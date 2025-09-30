# Dockerfile

# Use an official lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the saved model and the application code
COPY linear_regression_pipeline.pkl .
COPY api_app.py .

# Expose the port where the FastAPI application will listen
EXPOSE 8000

# Command to run the application using Uvicorn
# --host 0.0.0.0 makes the app accessible externally from the container
CMD ["uvicorn", "api_app:app", "--host", "0.0.0.0", "--port", "8000"]