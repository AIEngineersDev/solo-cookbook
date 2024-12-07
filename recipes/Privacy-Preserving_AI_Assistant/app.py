import streamlit as st
import requests

st.title("Privacy-Preserving AI Assistant")
st.subheader("Provide private, offline assistant capabilities.")

user_query = st.text_area("Enter a query for the assistant:")

if st.button("Get Response"):
    if user_query:
        response = requests.post(
            "http://localhost:8000/llm-llama32",
            json={"query": user_query}
        )
        if response.ok:
            st.subheader("Response")
            st.success(response.json().get("response", "No response returned"))
        else:
            st.error(f"Error: {response.status_code}")
