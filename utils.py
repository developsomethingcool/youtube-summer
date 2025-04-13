# Helper functions
import requests
from googleapiclient.discovery import build_from_document


from youtube_transcript_api import YouTubeTranscriptApi
from pytube import YouTube
import re

def get_video_id(url_link):
  return url_link.split("watch?v=")[-1]

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([t['text'] for t in transcript])

def get_video_title(url):
    import yt_dlp
    
    try:
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'skip_download': True,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', None)
            
            if not title:
                raise ValueError("No title found")
                
            safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "_", "-", "(", ")")).rstrip()
            return safe_title
            
    except Exception as e:
        raise ValueError(f"Could not retrieve video title with yt-dlp: {str(e)}")

