import joblib

# Load the model
model = joblib.load('linear_regression_model.joblib')

# Make a prediction
prediction = model.predict([[1, 2, 3]])

# Print the prediction
print(prediction)