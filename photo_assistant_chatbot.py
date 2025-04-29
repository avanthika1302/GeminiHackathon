import streamlit as st
import time, io
import helper
import toml
import google.generativeai as genai
from google.generativeai import GenerativeModel
from PIL import Image

# Access the keys
GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
SERPER_API_KEY = st.secrets["SERPER_API_KEY"]

# Load your API key from Streamlit secrets
genai.configure(api_key=GOOGLE_API_KEY)


# --- Session state init ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_info" not in st.session_state:
    st.session_state.user_info = {}
if "user_history" not in st.session_state:
    st.session_state.user_history = []
if "last_image" not in st.session_state:
    st.session_state.last_image = None
if "last_ModelOP" not in st.session_state:
    st.session_state.last_ModelOP = None
if "last_DBinsert" not in st.session_state:
    st.session_state.last_DBinsert = ""

# Sidebar user session management
st.sidebar.title("User Session")

if st.sidebar.button("Reset Session"):
    st.session_state.clear()
    st.rerun()


# Get user info
if not st.session_state.user_info:
    st.title("📸 Smart Photography Assistant")
    st.subheader("Tell us about you to get started")

    name = st.text_input("Your Name", key="name_input")
    email = st.text_input("Your Email", key="email_input")
    location = st.text_input("Location of interest", key="loc_input")

    if st.button("Start Session"):
        if name and email and location:
            st.session_state.user_info = {
                "name": name,
                "email": email,
                "location": location
            }
            st.rerun()
        else:
            st.warning("Please fill in all fields.")
    st.stop()

# --- Main Chat UI ---
# Display chat history

st.title("📸 Smart Photography Assistant")
st.subheader("Welcome " + st.session_state.user_info["name"]+"!")
st.markdown("Hi! I'm your Photo Assistant 🤖. Here's what I can do:")
st.markdown("""
                - 📝 Describe an uploaded photo
                - 📸 Social media captions and tags
                - 🌤️ Ideal weather for similar pictures
                - 🖼️ Photo elements for this picture and type of photography
                - 📍 Suggest nearby photo spots
                - ⬆️ Upload a new pic
                - 🔄 Clear all and start over
                Just type your option and I'll help!
                """)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

uploaded_file = st.file_uploader("Upload a photo to proceed", type=["jpg", "jpeg", "png"], key="file_uploader")

# Handle file upload
if st.button("Browse, Select & Upload"):
    try:
        st.session_state.last_image = uploaded_file.read()
        st.info("Uploading your photo...")

        image = Image.open(io.BytesIO(st.session_state.last_image))
        with st.chat_message("assistant"):
                st.markdown("Here is the image uploaded")
                st.image(image, caption="Your uploaded image", use_column_width=True)
        st.info("Analyzing using the Model...")

        with st.chat_message("assistant"):
            st.markdown("Thanks for uploading!")

        with st.spinner("Working on Photo Analysis..."):
            #time.sleep(10)
            try:
                ModelOP = helper.generate_description(st.session_state.last_image, st.session_state.user_info["location"])
                insights = helper.clean_json(ModelOP.text)
                DBinsert = helper.insert_image_metadata(st.session_state.user_info["name"],st.session_state.user_info["email"],st.session_state.user_info["location"],st.session_state.user_info["location"],insights)

            except Exception as e:
                insights = ""
                st.error("error performing analysis")

        st.session_state.last_ModelOP = insights
        st.session_state.last_DBinsert = DBinsert

        st.info("Ready, lets discuss about the image...")
        st.session_state.show_upload = False

    except Exception as e:
        st.error('Upload a file..')


user_input = st.chat_input("What would you like to do?", key="chat_box")

if user_input is not None and st.session_state.last_ModelOP is not None:
    with st.spinner("Model responding..."):
        # simulate delay or processing
        time.sleep(5)

    st.session_state.messages.append({"role": "user", "content": user_input})

    # Handle commands
    cmd = user_input.lower()
    response = ""

    if "start" in cmd or "reset" in cmd:
        st.session_state.clear()
        st.rerun()

    elif "upload" in cmd:
        response = "Upload a pic..."
        st.session_state.show_upload = True

    else:
        OPModel2 = helper.answer_question_from_json(st.session_state.last_ModelOP,cmd)
        response = OPModel2

    st.session_state.messages.append({"role": "assistant", "content": response})

    st.rerun()  # Only needed once at the end to reflect both messages
