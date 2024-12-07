import streamlit as st
import requests

st.title("Food Recognition for Restaurants")
st.subheader("Detect food items from images for inventory tracking.")

uploaded_food_image = st.file_uploader("Upload a food image:", type=["jpg", "png"])

if uploaded_food_image:
    st.write("Analyzing your image...")
    response = requests.post(
        "http://localhost:8000/vision-object-detect",
        files={"file": uploaded_food_image.read()}
    )
    if response.ok:
        st.subheader("Detected Items")
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")
