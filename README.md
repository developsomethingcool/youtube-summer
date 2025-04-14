# 🎥 YouTube Video Summarizer

A Streamlit-based web application that uses AI to summarize YouTube videos and answer questions about their content.

## 📋 Overview

YouTube Video Summarizer helps you quickly extract the key information from any YouTube video with available captions. The tool:

- Extracts video transcripts in multiple languages
- Generates concise summaries with key takeaways
- Allows you to ask specific questions about the video content
- Provides downloadable summaries
- Shows the full transcript for reference

## 🛠️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/developsomethingcool/youtube-summer.git
   cd youtube-summer
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Install Ollama (required for the AI functionality):
   - Visit [ollama.ai](https://ollama.ai/) to download and install
   - Pull the Llama3.1 model: `ollama pull llama3.1`

## 🚀 Usage

1. Start the application:
   ```
   streamlit run app.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (typically http://localhost:8501)

3. Paste a YouTube URL into the text field and click "Summarize Video"

4. Once the summary is generated, you can:
   - Read the AI-generated summary
   - Ask questions about the video content
   - View the full transcript
   - Download the summary as a text file

## 📁 Project Structure

- `app.py` - Main Streamlit application
- `utils.py` - Helper functions for YouTube transcript retrieval and processing
- `summarizer.py` - AI-powered transcript summarization
- `qa.py` - Question answering functionality

## ⚙️ Requirements

- Python 3.8+
- Streamlit
- YouTube Transcript API
- PyTube
- yt-dlp
- langdetect
- Ollama with llama3.1 model

## 🔍 Features

- **Language Detection**: Automatically identifies the language of the transcript
- **Multi-Language Support**: Can extract transcripts in various languages
- **Interactive UI**: Clean, user-friendly Streamlit interface
- **Q&A System**: Ask specific questions about the video content
- **Downloadable Summaries**: Save summaries for later reference

## ⚠️ Limitations

- Works only with YouTube videos that have captions/transcripts available
- Summary quality depends on transcript quality and AI model capabilities
- Currently uses a local Ollama instance for AI processing


## 📜 License

This project is [MIT](LICENSE) licensed.