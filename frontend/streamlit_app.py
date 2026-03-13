import streamlit as st

import json
import requests

from pathlib import Path

st.set_page_config(
    page_title="Car Price Predictor",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Car Resale Price Prediction")
st.write("Provide the vehicle details below to estimate the resale price.")

cw_folder = Path().resolve() / "frontend" / "brand_mapping.json"

with open(cw_folder) as f:
    brand_to_car_dct = json.load(f)

st.sidebar.header("Vehicle Basics")

brand = st.sidebar.selectbox(
    "Select Car Brand",
    sorted(brand_to_car_dct.keys())
)

car_name = st.sidebar.selectbox(
    "Car Model",
    sorted(brand_to_car_dct[brand])
)

seller_type = st.sidebar.radio(
    "Seller Type",
    ['Dealer', 'Individual', 'Trustmark Dealer']
)

fuel_type = st.sidebar.radio(
    "Fuel Type",
    ['Petrol', 'Diesel', 'CNG', 'Hybrid', 'LPG']
)

transmission_type = st.sidebar.selectbox(
    "Transmission Type",
    ['Automatic', 'Manual']
)

st.divider()

st.subheader("Vehicle Usage")

col1, col2, col3 = st.columns(3)

with col1:
    vehicle_age = st.slider(
        "Vehicle Age (Years)",
        1, 15
    )

with col2:
    km_driven = st.number_input(
        "Kilometers Driven",
        min_value=100,
        max_value=500000,
        step=1
    )

with col3:
    seats = st.slider(
        "Number of Seats",
        1, 9
    )

st.subheader("Engine & Performance")

col4, col5, col6 = st.columns(3)

with col4:
    engine = st.number_input(
        "Engine Capacity (cc)",
        min_value=793,
        max_value=6592,
        step=1
    )

with col5:
    mileage = st.number_input(
        "Mileage (km/l)"
    )

with col6:
    max_power = st.number_input(
        "Max Power (bhp)"
    )

st.divider()

if st.button("Predict Car Price 🚀"):
    
    payload = {
        "car_name": car_name,
        "brand": brand,
        "vehicle_age": vehicle_age,
        "km_driven": km_driven,
        "seller_type": seller_type,
        "fuel_type": fuel_type,
        "transmission_type": transmission_type,
        "mileage": mileage,
        "engine": engine,
        "max_power": max_power,
        "seats": seats
    }

    response = requests.post(
        "http://localhost:8000/predict",
        json=payload
    )

    result = response.json()
    price = result["prediction"]

    st.success(f"The predicted price for the car is {price} lakhs.")