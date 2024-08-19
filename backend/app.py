from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Define the mapping of numerical predictions to species names
species_names = ['setosa', 'versicolor', 'virginica']

# Load the model from file
def load_model():
    model_filename = 'iris_model.pkl'  # Change this if needed
    if os.path.exists(model_filename):
        with open(model_filename, 'rb') as f:
            model = pickle.load(f)
        return model
    else:
        raise FileNotFoundError(f"Model file {model_filename} not found")

@app.route('/predict', methods=['POST'])
def predict():
    model = load_model()  # Load the model from file

    data = request.json
    features = data.get('features')

    if not features:
        return jsonify({'error': 'Features are required'}), 400

    # Make a prediction using the loaded model
    prediction = model.predict([features])[0]
    species = species_names[prediction]  # Map prediction to species name
    return jsonify({'prediction': species})

