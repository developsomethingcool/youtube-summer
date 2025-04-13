# Summarizer

from ollama import chat

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

    if not response or 'message' not in response:
        raise ValueError("Failed to generate summary from LLM.")

    return response['message']['content']



