import streamlit as st
import requests

st.title("Intelligent Customer Support")
st.subheader("Provide context-aware customer support chat.")

customer_query = st.text_area("Enter customer query:")

if st.button("Get Response"):
    if customer_query:
        response = requests.post(
            "http://localhost:8000/llm-chat-gpt3",
            json={"query": customer_query}
        )
        if response.ok:
            st.subheader("Response")
            st.success(response.json().get("response", "No response generated"))
        else:
            st.error(f"Error: {response.status_code}")
