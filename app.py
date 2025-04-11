# Streamlit app

import streamlit as st
from utils import get_video_id, get_transcript
from summarizer import summarizer
import re

st.title("🎥 YouTube Video Summarizer")

url = st.text_input("Paste YouTube video link:")
file_name = st.text_input("Paste the file name")

if st.button("Summarize Video"):
    if not url:
        st.error("Please provide Youtube URL.")
    else:
        with st.spinner("Fetching and summarizing video..."):
            try:
                video_id = get_video_id(url)
                transcript = get_transcript(video_id=video_id)

                if not transcript:
                    st.warning("Transcript not available for this video")
                else:
                    summary = summarizer(transcript)
                    st.write(summary)

                    # removed non allowed signs from the name
                    safe_file_name = re.sub(r'[\\/*?:"<>|]', "_", file_name or "summary.txt")

                    if not safe_file_name.endswith(".txt"):
                        safe_file_name += ".txt"

                    st.download_button(
                        label="Download Summary",
                        data=summary,
                        file_name=safe_file_name,
                        mime="text/plain"
                    )
            except Exception as e:
                st.error(f"An error occured: {e}")
    


