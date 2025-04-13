# Streamlit app

import streamlit as st
from utils import get_video_id, get_transcript, get_video_title
from summarizer import summarizer
import re
import os

st.set_page_config(page_title="YouTube Video Summarizer", page_icon="🎥", layout="centered")
st.title("🎥 YouTube Video Summarizer")

st.markdown("""
Welcome! This tool helps you quickly summarize any YouTube video using AI.

Paste a YouTube link below and get:
- A clean, human-readable summary
- Key bullet points with main ideas
- Ability to download your summary
- Ask custom questions about the video content

Great for learning faster, note-taking, or saving time!
""")

st.markdown("---")

url = st.text_input("Paste YouTube video link here:", placeholder="https://www.youtube.com/watch?v=abcd1234")

if st.button("Summarize Video"):
    if url.strip() == "":
        st.error("Please provide YouTube URL.")
    else:
        try:
            with st.spinner("Generating summary..."):
                title = get_video_title(url)
                video_id = get_video_id(url)
                transcript = get_transcript(video_id)
                summary = summarizer(transcript)
            
            st.success("Summary generated!")

            st.markdown("### Video Title")
            st.write(title)

            st.markdown("### Summary")
            st.write(summary)

            st.download_button(
                label="Download Summary as .txt",
                data=summary,
                file_name=f"{title}.txt",
                mime="text/plain"
            )
        except ValueError as e:
            st.error(f"Error: {e}")

        except Exception as e:
            st.error(f"Something went wrong: {type(e).__name__} - {e}")

