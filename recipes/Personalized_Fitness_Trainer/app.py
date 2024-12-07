import streamlit as st
import requests

st.title("Personalized Fitness Trainer")
st.subheader("Monitor and provide feedback on exercise form.")

uploaded_exercise_video = st.file_uploader("Upload a video of the exercise:", type=["mp4", "mov", "avi"])

if uploaded_exercise_video:
    st.write("Analyzing your exercise form...")
    response = requests.post(
        "http://localhost:8000/vision-pose-estimate",
        files={"file": uploaded_exercise_video.read()}
    )
    if response.ok:
        st.subheader("Feedback")
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")
