import streamlit as st
import main

# Define parameters
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

# Display message
st.write("Please select values for the following parameters:")

# Create Streamlit dropdowns
selected_parameters = {}
for key, values in parameters.items():
    values.insert(0, "Select")
    selected_parameters[key] = st.selectbox(f"Select {key}", values, index=0 if key != 'num_cores' else None)

# Numeric input for price (compulsory)
price = st.number_input("Enter the price", min_value=0.0, value=0.0, step=1.0, format="%.2f", key="price")

# Submit button
# Define the mapping dictionary
mapping_dict = {
    'brand': {'acer': 0, 'apple': 1, 'asus': 2, 'avita': 3, 'axl': 4, 'chuwi': 5, 'dell': 6, 'fujitsu': 7, 'gigabyte': 8, 'honor': 9, 'hp': 10, 'iball': 11, 'infinix': 12, 'jio': 13, 'lenovo': 14, 'lg': 15, 'microsoft': 16, 'msi': 17, 'primebook': 18, 'realme': 19, 'samsung': 20, 'tecno': 21, 'ultimus': 22, 'walker': 23, 'wings': 24, 'zebronics': 25},
    'processor_brand': {'apple': 0, 'amd': 1, 'intel': 2, 'other': 3},
    'processor_tier': {'other': 0, 'celeron': 1, 'core i3': 2, 'core i5': 3, 'core i7': 4, 'core i9': 5, 'core ultra 7': 6, 'm1': 7, 'm2': 8, 'm3': 9, 'other': 10, 'pentium': 11, 'ryzen 3': 12, 'ryzen 7': 13, 'ryzen 9': 14},
    'primary_storage_type': {'HDD': 0, 'SSD': 1},
    'gpu_brand': {'amd': 0, 'arm': 1, 'intel': 2, 'nvidia': 3},
    'gpu_type': {'dedicated': 0, 'integrated': 1, 'other': 2},
    'OS': {'android': 0, 'chrome': 1, 'dos': 2, 'mac': 3, 'other': 4, 'ubuntu': 5, 'windows': 6}
}

if st.button("Submit"):
    # Check if any parameter is not selected
    if any(value == "Select" or value is None for value in selected_parameters.values()) or price == 0.0:
        st.warning("Please fill in all the compulsory fields.")
    else:
        # Convert selected parameters to list format
        parameter_list = [[
            mapping_dict['brand'][selected_parameters['brand']],
            price,
            mapping_dict['processor_brand'][selected_parameters['processor_brand']],
            mapping_dict['processor_tier'][selected_parameters['processor_tier']],
            selected_parameters['num_cores'],
            selected_parameters['num_threads'],
            selected_parameters['ram_memory'],
            mapping_dict['primary_storage_type'][selected_parameters['primary_storage_type']],
            selected_parameters['primary_storage_capacity'],
            selected_parameters['secondary_storage_capacity'],
            mapping_dict['gpu_brand'][selected_parameters['gpu_brand']],
            mapping_dict['gpu_type'][selected_parameters['gpu_type']],
            selected_parameters['is_touch_screen'],
            selected_parameters['display_size'],
            selected_parameters['resolution_width'],
            selected_parameters['resolution_height'],
            mapping_dict['OS'][selected_parameters['OS']],
            selected_parameters['year_of_warranty']
        ]]
        # Import main.py

        # Use the predict function from main.py
        prediction = main.make_prediction(parameter_list)

        # Display the prediction
        st.write("The predicted laptop rating is:", prediction)
        # Print the list
        st.write("Data in list format:", parameter_list)
        