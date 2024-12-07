import streamlit as st
import requests

st.title("Personalized Marketing Tool")
st.subheader("Analyze customer reviews for insights.")

review_text = st.text_area("Enter customer review text:")

if st.button("Analyze"):
    if review_text:
        response = requests.post(
            "http://localhost:8000/nlp-text-embedding",
            json={"text": review_text}
        )
        if response.ok:
            st.subheader("Insights")
            st.json(response.json())
        else:
            st.error(f"Error: {response.status_code}")
