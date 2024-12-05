# VidChat: Chat with YouTube Videos 🤖

VidChat is a cutting-edge application designed to revolutionize how users interact with video content. By combining advanced AI technologies such as **Google Generative AI (Gemini)**, **OpenAI APIs**, **LangChain**, and **Retrieval-Augmented Generation (RAG)**, VidChat delivers a seamless experience where users can search, analyze, and engage with YouTube videos in entirely new ways.

With **RAG**, VidChat intelligently combines video transcripts with contextually relevant data to provide accurate and meaningful responses to user queries. Whether you want to explore a video’s content, uncover insights, or interactively search for related videos, VidChat simplifies the process with intuitive design and powerful functionality. 

---

## 🚀 Features

### 1. **Video Content Analysis**
   - Analyze YouTube videos by providing a URL or by searching with keywords.
   - Extract insights from video content using AI-driven models.

### 2. **Context-Based Question Answering**
   - Uses OpenAI Whisper to transcribe video audio into text.
   - Answers user queries strictly based on the transcript and retrieved content.

### 3. **Keyword-Based Video Search**
   - Search for YouTube videos by keywords, sorted by relevance, upload date, view count, or rating.
   - Explore related videos directly within the app.

### 4. **Interactive Chat Interface**
   - Engage in seamless conversations with video content.
   - Reference specific video segments to answer user questions effectively.

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python, LangChain
- **AI Models:**  
  - Google Gemini (Generative AI)  
  - OpenAI Whisper (Audio Transcription)  
- **YouTube Integration:** YouTube Data API, Scrapetube
- **Database:** FAISS (for vectorized document retrieval)

---

## 📋 Prerequisites

1. **Python Version**  
   Ensure you have Python 3.9 or higher installed.  

2. **Install Required Libraries**  
   Use the following command to install the dependencies:  
   ```bash
   pip install -r requirements.txt
3. **API KEYS**  
   Create a .env file in the root directory with the following keys:
   ```bash
   OPENAI_API_KEY=your_openai_api_key
   GEMINI_API_KEY=your_google_gemini_api_key

## 💻 Usage
### 1. **Launch the Application**
Start the Streamlit server using the command:
  ```bash
   streamlit run app.py
  ```
### 2. **Features Overview**

**Chat with a YouTube Video by URL**
<ul>
  <li>Paste the YouTube video URL in the "URL" tab.</li>
  <li>Ask questions about the video; responses are generated using its transcript.</li>
</ul>

**Search and Analyze YouTube Videos**
<ul>
  <li>Use the "YouTube Search" tab to find videos by entering keywords.</li>
  <li>Filter results by relevance, view count, upload date, or rating.</li>
  <li>Select a video and ask questions based on its content.</li>
</ul>

**Explore Related Videos**
<ul>
  <li>View a curated list of related videos directly within the app.</li>
</ul>

## 📂 Project Structure
  ```bash
.
├── app.py                      # Main application file
├── videohelper.py              # Handles video processing and transcription
├── raghelper.py                # Retrieval-Augmented Generation (RAG) functions
├── .env                        # Environment variables for API keys
├── requirements.txt            # Python dependencies
└── imgs/
    └── app_banner.png          # Banner image for the app
```

