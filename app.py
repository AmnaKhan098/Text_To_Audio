import streamlit as st
from gtts import gTTS
import os

# Function to convert text to audio
def text_to_audio(text):
    tts = gTTS(text=text, lang='en')
    audio_file = 'output.mp3'
    tts.save(audio_file)
    return audio_file

# Streamlit UI
st.set_page_config(page_title="🎵 Text to Audio Converter", layout="wide")
st.markdown(
    """
    <style>
    .title {
        color: #4CAF50;
        font-size: 48px;
        text-align: center;
        font-weight: bold;
    }
    .text-area {
        background-color: #f0f8ff;
        border: 2px solid #4CAF50;
        border-radius: 5px;
        padding: 10px;
    }
    .button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">🗣️ Text to Audio Converter</div>', unsafe_allow_html=True)

# Text input box for user text
user_text = st.text_area("Enter your text here:", height=200, key="user_text", help="Type or paste your text here.", 
                          css_class="text-area")

# Button to convert text to audio
if st.button("Convert to Audio", key="convert_button"):
    if user_text:
        st.write("Converting text to audio...")
        audio_file_path = text_to_audio(user_text)

        # Provide an audio player for the user
        st.audio(audio_file_path, format='audio/mp3')
        st.success("Audio conversion complete!")
    else:
        st.warning("Please enter some text before converting.")

# Optional: Clean up the audio file after use (uncomment if needed)
# if os.path.exists('output.mp3'):
#     os.remove('output.mp3')
