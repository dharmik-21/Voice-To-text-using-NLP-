import streamlit as st
import whisper
import torch
from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
nltk.download("punkt_tab")

# Whisper model
model = whisper.load_model("base")

# Summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Emotion classifier
emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base"
)

# Extract key points
def extract_key_points(text):
    sentences = sent_tokenize(text)
    return sentences[:3]

# Extract tasks
def extract_tasks(text):
    tasks = []
    for s in text.split("."):
        if any(x in s.lower() for x in ["should", "need to", "must", "plan", "schedule"]):
            tasks.append(s.strip())
    return tasks


# Streamlit UI
st.set_page_config(page_title="Voice-to-Text Insight Generator", layout="wide")
st.title("🎤 Voice to Text Insight Generator")

st.write("Click the recorder below and speak.")

audio_file = st.audio_input("Record your voice")

if audio_file is not None:
    st.audio(audio_file)

    # Save audio
    with open("voice.wav", "wb") as f:
        f.write(audio_file.getvalue())

    # Transcribe
    st.subheader("📝 converted Text")
    text = model.transcribe("voice.wav")["text"]
    st.write(text)

    # Summary
    st.subheader("📄 Summary")
    summary = summarizer(text, max_length=60, min_length=20, do_sample=False)[0]['summary_text']
    st.write(summary)

    # Emotion
    st.subheader("😊 Emotion Detected")
    emo = emotion_model(text)[0]
    st.write(f"{emo['label']} ({round(emo['score']*100,2)}%)")

    # Key points
    st.subheader("📌 Key Points")
    for s in extract_key_points(text):
        st.write("- " + s)

    # Action items
    st.subheader("🧭 Action Items")
    for t in extract_tasks(text):
        st.write("➡ " + t)
