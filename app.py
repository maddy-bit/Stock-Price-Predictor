import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("Stock Price Predictor")

st.write("Enter stock details")

open_price = st.number_input("Open Price")
high_price = st.number_input("High Price")
low_price = st.number_input("Low Price")
close_price = st.number_input("Close Price")
volume = st.number_input("Volume")

if st.button("Predict"):

    data = np.array([
        [
            open_price,
            high_price,
            low_price,
            close_price,
            volume
        ]
    ])

    prediction = model.predict(data)

    st.success(
        f"Predicted Next Day Price: ${prediction[0]:.2f}"
    )