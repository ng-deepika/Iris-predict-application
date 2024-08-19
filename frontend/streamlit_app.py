import streamlit as st
import requests
import os

# Set the title of the Streamlit app
st.title("Iris Species Prediction")

# Input fields for the Iris dataset features
sepal_length = st.number_input("Sepal Length (cm)", min_value=0.0, max_value=10.0, value=5.1)
sepal_width = st.number_input("Sepal Width (cm)", min_value=0.0, max_value=10.0, value=3.5)
petal_length = st.number_input("Petal Length (cm)", min_value=0.0, max_value=10.0, value=1.4)
petal_width = st.number_input("Petal Width (cm)", min_value=0.0, max_value=10.0, value=0.2)

# Define the Flask API URL
flask_api_url = "http://flask:5000/predict"

# When the user clicks "Predict", make a POST request to the Flask API
if st.button("Predict"):
    # Prepare the data for the POST request
    features = [sepal_length, sepal_width, petal_length, petal_width]
    data = {
        "features": features
    }

    try:
        # Make the POST request to the Flask API
        response = requests.post(flask_api_url, json=data)
        response.raise_for_status()  # Raise an error for bad responses

        # Check the response from the Flask API
        if response.status_code == 200:
            prediction = response.json().get("prediction", "Unknown")
            st.write(f"Predicted Iris species: {prediction}")
        else:
            st.error(f"Error: {response.json().get('error')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Connection error: {e}")

# Instructions on how to use the app
st.write("""
### Instructions:
1. Enter the features of the Iris flower (sepal length, sepal width, petal length, petal width).
2. Click "Predict" to see the predicted species.
""")
