from youtube_transcript_api import YouTubeTranscriptApi
from ollama import chat
from ollama import ChatResponse

def get_video_id(url_link):
  return url_link.split("watch?v=")[-1]

video_id = get_video_id("https://www.youtube.com/watch?v=QTABGw29W5M&list=LL&index=1")

transcript = YouTubeTranscriptApi.get_transcript(video_id)

#print(transcript)
transcript_joined = " ".join([line['text'] for line in transcript])
print(f'joined transcript {transcript_joined}')

response = chat(model='llama3.1', messages=[
  {
    'role': 'user',
    'content': f"Summarize this lesson:\n\n{transcript_joined}"
  }
])

print("\nSummary:")
print(response['message']['content'])
