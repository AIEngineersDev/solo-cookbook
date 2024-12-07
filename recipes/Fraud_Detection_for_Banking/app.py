import streamlit as st
import requests

st.title("Fraud Detection for Banking")
st.subheader("Predict fraudulent transactions.")

transaction_data = st.text_area("Enter transaction data (JSON format):")

if st.button("Predict"):
    if transaction_data:
        response = requests.post(
            "http://localhost:8000/ml-logistic-reg",
            json={"data": transaction_data}
        )
        if response.ok:
            st.subheader("Prediction")
            st.json(response.json())
        else:
            st.error(f"Error: {response.status_code}")
