# Laptop-Rating-Prediction-System
app deployment : https://laptop-rating-prediction-system-57ftwedd56qsydttfml4m4.streamlit.app/

**Laptop Rating Prediction System**

## Overview

This project aims to develop a system that predicts the rating of laptops based on their specifications. By leveraging machine learning techniques, we can provide users with insights into the expected performance and quality of a laptop given its hardware and other attributes.

## Features

- **Prediction Model**: Utilizes machine learning algorithms to predict the rating of a laptop based on its specifications such as CPU, GPU, RAM, storage, display, etc.
  
- **User Interface**: Includes a user-friendly interface to input laptop specifications and obtain predicted ratings.

## How It Works

1. **Data Collection**: We gather data on various laptop models along with their specifications and corresponding ratings.

2. **Data Preprocessing**: The collected data is preprocessed to handle missing values, normalize features, and prepare it for training.

3. **Model Training**: Using machine learning techniques, we train a prediction model on the preprocessed data.

4. **Prediction**: Once trained, the model can accept input regarding a laptop's specifications and provide an estimated rating based on its learned patterns from the training data.

## File Structure

- **DataSet.xlsx**: Contains the dataset used for training and evaluation.
  
- **README.md**: Provides an overview of the project, its features, and how it works.
  
- **app.py**: Code for the Streamlit web application.
  
- **builder.ipynb**: Jupyter notebook containing the code for building the Streamlit app.
  
- **demo.py**: Code for demonstrating the application.
  
- **main.py**: Main script for running the Streamlit app.
  
- **model.joblib**: Pre-trained model stored using joblib.
  
- **model.pkl**: Pre-trained model stored using pickle.
  
- **requirements.txt**: Lists all dependencies required to run the project.

## How to Use

1. Clone the repository to your local machine.
   
2. Install the required dependencies listed in `requirements.txt`.
   
3. Run `main.py` to start the Streamlit app.
   
4. Input the specifications of the laptop you want to predict the rating for.
   
5. Get the predicted rating based on the provided specifications.

## Contributors
- Vishalsun007 - https://github.com/Vishalsun007
- Rajkumar-Gunasekaran - https://github.com/Rajkumar-Gunasekaran 





---

Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue. We appreciate your feedback!
