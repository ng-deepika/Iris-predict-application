# Iris Species Prediction Project
 This project is a web-based application designed to predict the species of the Iris flower using the famous Iris dataset. The project is built using Flask for the backend, Streamlit for the frontend, and is containerized using Docker.

# Prerequisites
  To run this project locally, ensure you have the following dependencies installed:
  Flask==3.0.3
  Gunicorn==23.0.0
  Scikit-learn==1.5.1
  Docker (for containerization)
  Docker Compose (for managing multiple services)
  
## Project Structure

  Flask Application:
  The backend of the application is built using Flask. It serves as the API for predicting the species based on the input features.
  Flask is exposed on port 5000.
  
  Streamlit Frontend:
  The frontend of the application is built using Streamlit. It provides a user-friendly interface to input the Iris features and visualize the predictions.
  Streamlit is exposed on port 8501.
  
# Iris Dataset:
 The model is trained on the Iris dataset, which is a classic dataset in machine learning for classification tasks. The trained model is integrated into the Flask app.
