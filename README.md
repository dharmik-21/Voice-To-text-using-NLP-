
# 🎤 Voice-to-Text Insight Generator

An AI-powered Streamlit application that converts speech into text using Whisper, auto-summarizes content, detects emotions, extracts key points, and generates actionable tasks—all from your voice.



## 🚀 Features

* 🎙️ **Browser-based voice recording** (no external software needed)
* 🤖 **Whisper AI transcription** with high accuracy
* 📝 **Automatic text summarization**
* 😊 **Emotion detection** from speech content
* 📌 **Key point extraction**
* 🧭 **Task & action item detection**
* ⚡ Simple, fast, and interactive Streamlit UI



## 🛠️ Technologies Used

* Python
* OpenAI Whisper
* HuggingFace Transformers
* Streamlit
* NLTK
* PyTorch



 📂 Project Structure


📁 Voice-To-Text-Insight
│── app.py               # Main Streamlit application
│── voice.wav            # Temporary audio file
│── requirements.txt     # Dependencies
└── README.md




 ▶️ How to Run

 1. Install dependencies

bash
pip install -r requirements.txt


### 2. Run Streamlit app

bash
streamlit run app.py


 3. Speak into your mic

Record → Transcribe → Summaries → Insights 🎉



## 📦 requirements.txt (example)


streamlit
whisper
transformers
torch
nltk


## 🧠 How It Works

1. User records audio in the browser
2. Whisper converts speech → text
3. NLP pipelines generate

   * Summary
   * Emotion
   * Key points
   * Action items
     
4. Results displayed in a clean UI
   
   * shared Output.png


## ⭐ Future Enhancements

* Live real-time transcription
* Speaker diarization
* Multi-language emotion detection
* ChatGPT-like chat history
* Export results to PDF

---

## 👨‍💻 Author

**Dharmik Barot**

