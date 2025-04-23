{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOKeAwtHlOMZg+T9wAGiBiu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/avanthika1302/GeminiHackathon/blob/main/helper.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "YoinueqV-UkR"
      },
      "outputs": [],
      "source": [
        "import sqlite3, re, json, requests\n",
        "from google.colab import userdata\n",
        "from google.generativeai import GenerativeModel\n",
        "import google.generativeai as genai\n",
        "\n",
        "# Initialize Gemini model\n",
        "model = GenerativeModel(\"gemini-2.0-flash\")\n",
        "\n",
        "# Function to generate insights from image and location\n",
        "def generate_description(imagefile, location):\n",
        "    prompt = \"\"\"\n",
        "    You are a professional photography assistant.\n",
        "    Analyze this photo and describe:\n",
        "    1. The scene and type of location.\n",
        "    2. The optimal time of day and weather for this type of photo.\n",
        "    3. Key photographic elements.\n",
        "    4. Ideal use case for the photo (e.g., family shoots, fashion, travel).\n",
        "    5. Add in an apt social media captions with tags to the picture as a bonus.\n",
        "    6. Suggest nearby or similar locations for taking such photos based on the user's location.\n",
        "    Return the response in JSON format with keys:\n",
        "    - desc\n",
        "    - tags\n",
        "    - OptWeather\n",
        "    - Elements\n",
        "    - UseCase\n",
        "    - SMCaption\n",
        "    - NearbySpots\n",
        "    \"\"\"\n",
        "    client = genai.Client(api_key=userdata.get('GOOGLE_API_KEY'))\n",
        "    response = client.models.generate_content(\n",
        "        model=\"gemini-2.0-flash\",\n",
        "        contents=[imagefile.read(), prompt])\n",
        "    #response = model.generate_content([imagefile.read(), prompt])\n",
        "    return response.text\n",
        "\n",
        "# Parse JSON safely\n",
        "def clean_json(text):\n",
        "    try:\n",
        "        json_match = re.search(r\"\\{.*\\}\", text, re.DOTALL)\n",
        "        return json.loads(json_match.group()) if json_match else {}\n",
        "    except Exception as e:\n",
        "        #st.error(\"Failed to parse JSON: \" + str(e))\n",
        "        return {\"Failed to parse JSON: \" + str(e)}\n",
        "\n",
        "# Save metadata to SQLite\n",
        "def init_db(db_path):\n",
        "    conn = sqlite3.connect(db_path)\n",
        "    cursor = conn.cursor()\n",
        "    cursor.execute(\"\"\"\n",
        "        CREATE TABLE IF NOT EXISTS photos (\n",
        "            id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
        "            name TEXT,\n",
        "            email TEXT,\n",
        "            location TEXT,\n",
        "            image_name TEXT,\n",
        "            metadata TEXT\n",
        "        )\n",
        "    \"\"\")\n",
        "    conn.commit()\n",
        "    conn.close()\n",
        "\n",
        "def insert_image_metadata(name, email, image_path, location, metadata):\n",
        "    try:\n",
        "        conn = sqlite3.connect(\"userimages.db\")\n",
        "        cursor = conn.cursor()\n",
        "        cursor.execute(\"INSERT INTO photos (name, email, location, image_name, metadata) VALUES (?, ?, ?, ?, ?)\",\n",
        "                        (name, email, location, image_path, json.dumps(metadata)))\n",
        "        conn.commit()\n",
        "        conn.close()\n",
        "        return \"success\"\n",
        "    except Exception as e:\n",
        "        return str(e)\n",
        "\n",
        "def search_similar_places(tags, location):\n",
        "    query = f\"photography spots with {', '.join(tags)} in {location}\"\n",
        "    headers = {\n",
        "        \"X-API-KEY\": userdata.get('SERPER_API_KEY'),\n",
        "        \"Content-Type\": \"application/json\"\n",
        "    }\n",
        "    payload = {\"q\": query, \"type\": \"images\"}\n",
        "    response = requests.post(\"https://google.serper.dev/search\", headers=headers, json=payload)\n",
        "    if response.status_code == 200:\n",
        "        results = response.json()\n",
        "        return results.get(\"images\", [])[:3]\n",
        "    else:\n",
        "        #st.error(\"Error from Serper API\")\n",
        "        return []"
      ]
    }
  ]
}