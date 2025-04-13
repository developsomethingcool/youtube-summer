# Streamlit app

import streamlit as st
from utils import get_video_id, get_transcript, get_video_title, format_transcript, detect_language
from summarizer import summarizer

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
            with st.spinner("Fetching video title..."):
                title = get_video_title(url)
                
            with st.spinner("Extracting video ID..."):
                video_id = get_video_id(url)

            with st.spinner("Retrieving transcript..."):
                transcript = get_transcript(video_id)

            if not transcript:
                st.warning("Transcript not available for this video.")
            else:
                with st.spinner("Generating summary..."):
                    summary = summarizer(transcript)

                st.markdown(f"## 🎬 *{title}*")

                st.markdown("### ✨ Summary")
                st.markdown(summary)

                lang_code, flag = detect_language(transcript)

                st.markdown(f"### Transcript Language Detected: {flag} ({lang_code})")

                with st.expander("📝 See full transcript"):
                    st.text_area("Transcript", format_transcript(transcript), height=300)


                st.download_button(
                    label="⬇️ Download Summary as .txt",
                    data=summary,
                    file_name=f"{title}.txt",
                    mime="text/plain"
                )



        except ValueError as e:
            st.error(f"Error: {e}")

        except Exception as e:
            st.error(f"Something went wrong: {type(e).__name__} - {e}")

