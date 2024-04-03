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