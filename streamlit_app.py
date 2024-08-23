import streamlit as st
import pandas as pd
import pickle
from pathlib import Path

# Set the background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as f:
        image = f.read()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{image_file}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to add a background image
add_bg_from_local('C:\Users\youss\OneDrive\Desktop\portfolio\background.jpg')

# Set the title with custom font and style
st.markdown("<h1 style='text-align: center; color: white;'>Car CO2 Emission Predictor</h1>", unsafe_allow_html=True)

# Create a container for input fields
input_container = st.container()
with input_container:
    st.markdown("<h3 style='color: white;'>Enter the car details:</h3>", unsafe_allow_html=True)
    engine_size = st.number_input('Engine Size', min_value=0.0, max_value=10.0, value=1.0)
    cylinder = st.number_input('Cylinders', min_value=0, max_value=10, value=1)
    fuelconsumption = st.number_input('Fuel Consumption (City)', min_value=0.0, max_value=10.0, value=1.0)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Make predictions
output = model.predict([[engine_size, cylinder, fuelconsumption]])

# Display the prediction with custom style
st.markdown(f"<h2 style='text-align: center; color: white;'>CO2 Emission: {output[0][0]} g/km</h2>", unsafe_allow_html=True)
