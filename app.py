# Streamlit app

import streamlit as st
from utils import get_video_id, get_transcript
from summarizer import summarizer

st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Paste YouTube video link:")
file_name = st.text_input("Paste the file name")

if st.button("Summarize Video"):
    video_id = get_video_id(url)
    transcript = get_transcript(video_id=video_id)
    summary = summarizer(transcript)

    st.markdown("### Summary")
    st.write()

    st.download_button("Download Summary", summary, file_name=file_name)
