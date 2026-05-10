import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model/house_price_model.pkl")

# Page configuration
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 House Price Prediction App")

st.write(
    "Predict house prices using Machine Learning."
)

st.divider()

# User Inputs
overall_qual = st.slider(
    "Overall Quality",
    1,
    10,
    5
)

gr_liv_area = st.number_input(
    "Ground Living Area (sq ft)",
    min_value=300,
    max_value=10000,
    value=1500
)

garage_cars = st.slider(
    "Garage Capacity (cars)",
    0,
    5,
    2
)

garage_area = st.number_input(
    "Garage Area",
    min_value=0,
    max_value=2000,
    value=500
)

total_bsmt_sf = st.number_input(
    "Basement Area",
    min_value=0,
    max_value=5000,
    value=800
)

full_bath = st.slider(
    "Full Bathrooms",
    0,
    5,
    2
)

year_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2025,
    value=2000
)

# Prediction Button
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "OverallQual": [overall_qual],
        "GrLivArea": [gr_liv_area],
        "GarageCars": [garage_cars],
        "GarageArea": [garage_area],
        "TotalBsmtSF": [total_bsmt_sf],
        "FullBath": [full_bath],
        "YearBuilt": [year_built]
    })

    prediction = model.predict(input_data)[0]

    st.success(
        f"Estimated House Price: ${prediction:,.2f}"
    )