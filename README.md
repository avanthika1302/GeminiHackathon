# GeminiHackathon
# AI-Powered Photo Assistant Chatbot

An interactive Streamlit chatbot that helps you understand your photo's style, find similar inspirational images online, and even discover nearby places to recreate those vibes — all with a conversational interface!

## Demo

> Live Demo: [Streamlit Cloud App](https://your-app-url.streamlit.app)

---

## Features

- **Conversational Chatbot UI**: Start with your name and email and upload an image to get personalized results.
- **AI-Generated Image Descriptions**: Automatically extract image context and tags (mocked using a placeholder for Gemini Vision).
- **Serper.dev Integration**: Searches Google to recommend nearby photography spots based on image aesthetics and user location.
- **SQLite Integration**: Stores image descriptions, tags, location, and suggestions for future reference.
- **Search Your History**: Use keywords like "tulips", "beach", or "sunset" to find past inspirations.

---

## Technologies Used

- **Streamlit**: Web interface and chatbot flow
- **SQLite**: Persistent storage for image metadata
- **Serper.dev API**: Google Search alternative for photo location recommendations
- **Pillow**: Image processing

---
photo-assistant-chatbot/
├── photo_assistant_chatbot.py     # Main Streamlit app
├── requirements.txt
├── helper.py
└── .streamlit/
    └── secrets.toml               # Contains SERPER_API_KEY and GEMINI KEY

## Installation

```bash
git clone https://github.com/avanthika1302/photo-assistant-chatbot.git
cd photo-assistant-chatbot
pip install -r requirements.txt
