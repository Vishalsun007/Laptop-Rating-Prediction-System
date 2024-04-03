<<<<<<< Updated upstream
# main.py
from tensorflow.keras.models import load_model
import cv2
import matplotlib.pyplot as plt
import numpy as np

model = load_model('linear_regression_model.joblib')

def predict_disease(image_file):
    img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
    img = cv2.resize(img, (28, 28))
    result = model.predict(img.reshape(1, 28, 28, 3))
    max_prob = max(result[0])
    class_ind = list(result[0]).index(max_prob)
    class_name = classes[class_ind]

    return class_name
=======
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Load your data
@st.cache
def load_data():
    df_encoded = pd.read_csv('your_data.csv')
    return df_encoded

df_encoded = load_data()

# Create a sidebar for user input
st.sidebar.header('User Input Parameters')

def user_input_features():
    row_index = st.sidebar.slider('Row Index', 0, df_encoded.shape[0]-1, 835)
    return row_index

row_index = user_input_features()

# Select the row from df_encoded
selected_row = df_encoded.loc[[row_index], :]
print(selected_row)
# Separate the features and the target
X_selected = selected_row.drop('Rating', axis=1)
y_selected = selected_row['Rating']

# Define your model
reg = RandomForestRegressor()

# Train your model
reg.fit(X_selected, y_selected)

# Predict the target using the reg model
y_pred = reg.predict(X_selected)
print(y_pred)
>>>>>>> Stashed changes
