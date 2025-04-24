# Photo Assistant Chatbot
# AI-Powered Photo Assistant Chatbot

An interactive Streamlit chatbot that helps you understand your photo's style, find similar inspirational images online, and even discover nearby places to recreate those vibes — all with a conversational interface!

---
## Flow

🧠 Smart Photography Assistant – High-Level Flow

This chatbot offers an engaging, image-aware chat experience tailored for photography enthusiasts. Below is a high-level flow description for the assistant:

🌟 1. User Session Initialization

        Collects user details (Name, Email, Location).

        Initializes a personalized session.

🖼️ 2. Photo Upload & Analysis

        User uploads a photo (jpg, jpeg, png).

        Gemini Vision Model analyzes the photo to extract:

            📜 Description of the scene
    
            🏷️ Tags/keywords
    
            🌦️ Ideal weather conditions
    
            🎨 Visual elements and style
    
            🧭 Suggested use cases (e.g., portrait, travel)
    
            📝 Social media caption ideas
    
            📍 Nearby similar photography spots (based on location)

💬 3. Conversational Commands

        Users interact through a chat interface and can:

            "describe" → Get a natural description of the uploaded photo.
    
            "tags" / "caption" → Receive curated hashtags and captions to add to your social media.
    
            "weather" → Understand ideal photo conditions.
    
            "similar" → See or find visually similar content.
    
            "spot" → Discover nearby photo-worthy spots.
    
            "upload" → Upload a new image.
    
            "start" / "reset" → Clear session and start fresh.

        Any other query → Handled via Gemini Pro model for a natural, intelligent reply.

🔄 4. Continuous Engagement

        All interactions are stored in session state.

        Users can continue chatting, upload new photos, or reset the experience at any time.

        This flow ensures a seamless and intelligent chat journey powered by LLM and vision models, helping users creatively engage with           their images and explore the world around them through a lens.

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
## Folder Structure
```text
photo-assistant-chatbot/
├── photo_assistant_chatbot.py     # Main Streamlit app
├── requirements.txt
├── helper.py
└── .streamlit/
    └── secrets.toml               # Contains SERPER_API_KEY and GEMINI KEY
```

---
## Installation

```bash
git clone https://github.com/avanthika1302/photo-assistant-chatbot.git
cd photo-assistant-chatbot
pip install -r requirements.txt
```
---
## Future developments

1. Search if there are images from the SQLite DB based on tags i.e. previous uploads
2. Integrate function calling to perform the above using search using natural language
3. View past chat and then based on specific users past chat

