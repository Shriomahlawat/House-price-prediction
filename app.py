import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("house_price_model.pkl")

st.title("House Price Prediction")

st.write(
    "Enter the details of your house "
    "to estimate its price."
)

# User inputs
area = st.number_input(
    "Area (sq ft)",
    min_value=100,
    max_value=10000,
    value=2500
)

bedrooms = st.selectbox(
    "Bedrooms",
    [1, 2, 3, 4, 5]
)

bathrooms = st.selectbox(
    "Bathrooms",
    [1, 2, 3, 4]
)

floors = st.selectbox(
    "Floors",
    [1, 2, 3]
)

year = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=2010
)

location = st.selectbox(
    "Location",
    ["Downtown", "Rural", "Urban", "Suburban"]
)

condition = st.selectbox(
    "Condition",
    ["Excellent", "Good", "Fair", "Poor"]
)

garage = st.selectbox(
    "Garage",
    ["Yes", "No"]
)

# Prediction button
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        "Area": [area],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Floors": [floors],
        "YearBuilt": [year],
        "Location": [location],
        "Condition": [condition],
        "Garage": [garage]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Estimated Price: {prediction[0]:,.2f}"
    )

    st.warning(
        "Educational estimate only. "
        "Model performance must be validated."
    )
