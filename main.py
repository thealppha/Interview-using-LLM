import streamlit as st
from utils import *

st.title("Mock")

topic = st.text_input("Interview Domain")

if not topic:
    st.stop()

if "button_clicked" not in st.session_state:
    st.session_state.button_clicked = False

def button_callback():
    st.session_state.button_clicked = True
    
if st.button("Create question", key="create_question", on_click=button_callback) or st.session_state.button_clicked:
    question = run_question_bot(topic)
    st.write(question)

    if st.button("Record Answer", key="record_answer"):
        recording()
        audio_file = open('recording.wav', 'rb')
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format='audio/wav')