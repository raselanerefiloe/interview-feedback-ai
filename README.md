# 🎙️ Interview Feedback AI

An AI-powered tool that analyzes job interview audio and provides structured, unbiased feedback on clarity, confidence, communication, and technical accuracy—helping candidates improve without human reviewers.

## 🚀 Features

- 🎧 Upload audio recordings of interviews
- 🤖 Automatic transcription using Whisper
- 🧠 AI-generated structured feedback with GPT-4o (via Puter.js)
- ✅ Focused on skill-based, unbiased assessment
- 🌐 Simple, interactive web interface (HTML + Tailwind CSS + Flask backend)
- 🎨 Smooth animations with Framer Motion

## 🧠 AI Feedback Criteria

The AI evaluates the interview based on:

1. **Clarity of Answers**
2. **Confidence and Tone** (without bias)
3. **Communication Skills**
4. **Technical or Content Accuracy**
5. **Overall Impression & Suggestions for Improvement**


## 💡 How It Works

1. User uploads an interview audio file via the frontend.
2. Flask backend saves the file and transcribes it using Whisper.
3. Transcription is returned to the frontend.
4. Frontend sends the transcript to GPT-4o using **Puter.js** (no API key needed).
5. AI returns unbiased, structured feedback.

## 🌐 Demo UI Screenshot

> _Include a screenshot here if available_

## 📦 Requirements

- Python 3.9.9
- Flask
- whisper
- HTML/JS frontend with Tailwind & Puter.js

Install dependencies:

```bash
pip install flask openai-whisper

git clone https://github.com/yourusername/interview-feedback-ai.git
cd interview-feedback-ai
python app.py

Then open http://localhost:5000 in your browser.