import streamlit as st
import requests

st.title("Creative Writing Assistant")
st.subheader("Generate creative writing ideas and drafts.")

prompt = st.text_area("Provide a writing prompt:")

if st.button("Generate"):
    if prompt:
        response = requests.post(
            "http://localhost:8000/nlp-gpt-neo",
            json={"prompt": prompt}
        )
        if response.ok:
            st.subheader("Generated Text")
            st.success(response.json().get("text", "No text generated"))
        else:
            st.error(f"Error: {response.status_code}")
