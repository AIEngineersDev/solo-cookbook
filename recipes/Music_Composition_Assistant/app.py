import streamlit as st
import requests

st.title("Music Composition Assistant")
st.subheader("Generate music tracks based on input.")

music_theme = st.text_area("Provide a theme or genre for your music:")

if st.button("Generate Music"):
    if music_theme:
        response = requests.post(
            "http://localhost:8000/audio-audiocraft",
            json={"theme": music_theme}
        )
        if response.ok:
            st.audio(response.content, format="audio/mp3")
        else:
            st.error(f"Error: {response.status_code}")
