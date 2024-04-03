from joblib import load

# Load the model from the file
model = load('model.joblib')

# Use the loaded model to make predictions

def make_prediction(data):
    predictions = model.predict(data)
    return predictions
