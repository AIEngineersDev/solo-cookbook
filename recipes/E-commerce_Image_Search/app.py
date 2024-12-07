import streamlit as st
import requests

st.title("E-commerce Image Search")
st.subheader("Search for products using an image.")

uploaded_image = st.file_uploader("Upload a product image:", type=["jpg", "png"])

if uploaded_image:
    st.write("Processing your image...")
    response = requests.post(
        "http://localhost:8000/multimodal-clip",
        files={"file": uploaded_image.read()}
    )
    if response.ok:
        st.subheader("Search Results")
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")
