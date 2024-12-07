import streamlit as st
import requests

st.title("Language Learning Buddy")
st.subheader("Detect the language of spoken text.")

uploaded_audio = st.file_uploader("Upload an audio file:", type=["wav", "mp3", "ogg"])

if uploaded_audio:
    st.write("Processing your audio...")
    response = requests.post(
        "http://localhost:8000/speech-lang-id",
        files={"file": uploaded_audio.read()}
    )
    if response.ok:
        st.subheader("Detected Language")
        st.success(response.json().get("language", "No language detected"))
    else:
        st.error(f"Error: {response.status_code}")
