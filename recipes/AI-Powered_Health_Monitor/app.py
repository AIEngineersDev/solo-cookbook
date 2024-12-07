import streamlit as st
import requests

st.title("AI-Powered Health Monitor")
st.subheader("Monitor patient exercises and assess progress.")

uploaded_file = st.file_uploader("Upload an image or video:", type=["jpg", "png", "mp4"])

if uploaded_file:
    st.write("Processing your file...")
    response = requests.post("http://localhost:8000/vision-pose-estimate", files={"file": uploaded_file.read()})
    if response.ok:
        st.success("Processed successfully!")
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")
