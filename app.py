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
st.set_page_config(page_title="Text to Audio Converter", layout="wide")
st.title("🗣️ Text to Audio Converter")

# Text input box for user text
user_text = st.text_area("Enter your text here:", height=200)

# Button to convert text to audio
if st.button("Convert to Audio"):
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

