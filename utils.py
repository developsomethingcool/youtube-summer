# Helper functions

from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url_link):
  return url_link.split("watch?v=")[-1]

def get_transcript(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([t['text'] for t in transcript])