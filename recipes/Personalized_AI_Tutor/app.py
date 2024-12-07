import streamlit as st
import requests

st.title("Personalized AI Tutor")
st.subheader("Summarize educational material into key points.")

educational_text = st.text_area("Enter the educational text:")

if st.button("Summarize"):
    if educational_text:
        response = requests.post(
            "http://localhost:8000/nlp-text-summarizer",
            json={"text": educational_text}
        )
        if response.ok:
            st.subheader("Summary")
            st.success(response.json().get("summary", "No summary returned"))
        else:
            st.error(f"Error: {response.status_code}")
