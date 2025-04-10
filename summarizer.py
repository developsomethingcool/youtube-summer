# LLM logic

from youtube_transcript_api import YouTubeTranscriptApi
from ollama import chat
from ollama import ChatResponse
from utils import get_video_id, get_transcript

def summarizer(transcript):
    prompt = f"""Summarize the following YouTube video transcript into:
    -Main idea
    -Bullet point key takeaways
    -TL;DR summary

    Transcript:
    {transcript}
    """

    response = chat(model='llama3.1', messages=[
      {
        'role': 'user',
        'content': prompt
      }
    ])

    return response['message']['content']

print("\nSummary:")

