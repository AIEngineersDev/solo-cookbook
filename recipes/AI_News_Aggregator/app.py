import streamlit as st
import requests

st.title("AI News Aggregator")
st.subheader("Summarize news articles into concise summaries.")

text_input = st.text_area("Enter the news article text:")

if st.button("Summarize"):
    if text_input:
        response = requests.post(
            "http://localhost:8000/nlp-text-summarizer",
            json={"text": text_input}
        )
        if response.ok:
            st.subheader("Summary")
            st.success(response.json().get("summary", "No summary returned"))
        else:
            st.error(f"Error: {response.status_code}")
