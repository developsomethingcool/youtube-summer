from youtube_transcript_api import YouTubeTranscriptApi
from ollama import chat
from ollama import ChatResponse

def get_video_id(url_link):
  return url_link.split("watch?v=")[-1]

video_link = "https://www.youtube.com/watch?v=wjZofJX0v4M"
video_id = get_video_id(video_link)


transcript = YouTubeTranscriptApi.get_transcript(video_id)

#print(transcript)
transcript_joined = " ".join([line['text'] for line in transcript])
print(f'joined transcript {transcript_joined}')

response = chat(model='phi4:latest', messages=[
  {
    'role': 'user',
    'content': f"Summarize this lesson:\n\n{transcript_joined}"
  }
])

print("\nSummary:")
print(response['message']['content'])
