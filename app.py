import streamlit as st
import joblib
import pandas as pd

# Load the linear regression model
model = joblib.load("linear_regression_model.joblib")

# Define the dropdown parameters
parameters = {
    "brand": ['acer', 'apple', 'asus', 'avita', 'axl', 'chuwi', 'dell', 'fujitsu', 'gigabyte', 'hp',
              'honor', 'iball', 'infinix', 'jio', 'lenovo', 'lg', 'microsoft', 'msi', 'primebook', 'realme',
              'samsung', 'tecno', 'ultimus', 'walker', 'wings', 'zebronics'],
    "processor_brand": ['amd', 'apple', 'intel', 'other'],
    "processor_tier": ['celeron', 'core i3', 'core i5', 'core i7', 'core i9', 'core ultra 7', 'm1', 'm2',
                       'm3', 'other', 'pentium', 'ryzen 3', 'ryzen 7', 'ryzen 9'],
    "num_cores": [2, 4, 5, 6, 8, 10, 11, 12, 14, 16, 20, 24],
    "num_threads": [0, 2, 4, 5, 6, 8, 11, 12, 14, 16, 20, 22, 24, 28, 32],
    "ram_memory": [2, 4, 8, 12, 16, 32, 36],
    "primary_storage_type": ['HDD', 'SSD'],
    "primary_storage_capacity": [32, 64, 128, 256, 512, 1024, 2048],
    "secondary_storage_capacity": [0, 128, 256, 512],
    "gpu_brand": ['amd', 'arm', 'intel', 'nvidia'],
    "gpu_type": ['dedicated', 'integrated', 'other'],
    "is_touch_screen": [False, True],
    "display_size": [10.1, 11.6, 12.4, 13.0, 13.3, 13.4, 13.5, 13.6, 14.0, 14.1, 14.2,
                     14.5, 15.0, 15.3, 15.6, 16.0, 16.1, 16.2, 17.3, 18.0],
    "resolution_width": [1280, 1365, 1422, 1440, 1536, 1600, 1920, 2048, 2160, 2240,
                         2256, 2560, 2844, 2880, 2951, 2958, 3000, 3024, 3072, 3200, 
                         3413, 3456, 3840],
    "resolution_height": [800, 900, 1024, 1080, 1400, 1440, 1504, 1536, 1600, 1620, 1660,
                          1664, 1800, 1864, 1920, 1964, 2000, 2160, 2234, 2400],
    "OS": ['android', 'chrome', 'dos', 'mac', 'other', 'ubuntu', 'windows'],
    "year_of_warranty": [1, 2, 3]
}

# Arrange values in ascending order
for key, values in parameters.items():
    if isinstance(values[0], str):
        parameters[key] = sorted(values)

# Display message
st.write("Please select values for the following parameters:")

# Create Streamlit dropdowns
selected_parameters = {}
for key, values in parameters.items():
    values.insert(0, "Select")
    selected_parameters[key] = st.selectbox(f"Select {key}", values, index=0 if key != 'num_cores' else None)

# Numeric input for price
price = st.number_input("Enter the price", min_value=0)

# Submit button
if st.button("Submit"):
    # Remove 'Select' from selected_parameters
    for key, value in selected_parameters.items():
        if value == "Select":
            selected_parameters[key] = None
    
    # Add price to selected_parameters
    selected_parameters["price"] = price
    
    # Create a DataFrame from selected parameters
    input_data = pd.DataFrame(selected_parameters, index=[0])
    
    # Send data to main.py for prediction
    prediction = model.predict(input_data)
    
    # Display prediction
    st.write("Predicted Rating:", prediction[0])
