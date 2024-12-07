import streamlit as st
import requests

st.title("Multilingual Voice Assistant")
st.subheader("Generate multilingual text-to-speech outputs.")

text_input = st.text_area("Enter text for speech synthesis:")
language_code = st.text_input("Enter language code (e.g., en, fr, es):")

if st.button("Generate Speech"):
    if text_input and language_code:
        response = requests.post(
            "http://localhost:8000/speech-parler-tts",
            json={"text": text_input, "language_code": language_code}
        )
        if response.ok:
            st.audio(response.content, format="audio/mp3")
        else:
            st.error(f"Error: {response.status_code}")
