# 🧠 Smart Voice Assistant using ChatGPT 🎙️

A Python project that acts as a voice assistant in **Arabic**, powered by ChatGPT.  
It listens to your voice, sends the text to GPT, and responds with both **spoken voice** and a clean **graphical interface** built with Tkinter.

---

## ✅ Features:

- 🎤 Recognizes Arabic speech using Google Speech Recognition.
- 💬 Sends your question to ChatGPT (GPT-3.5-Turbo).
- 🔊 Converts GPT response to speech using `pyttsx3`.
- 🪟 User-friendly GUI built with Tkinter.
- 🧵 Threaded execution to keep the app responsive (no freezing).

---

## 🧰 Requirements:

Install the necessary Python packages:

```
pip install openai pyttsx3 SpeechRecognition pyaudio

⚠️ On Windows, if you face issues installing pyaudio, run:

pip install pipwin
pipwin install pyaudio
```
---
## 🔐 Set Up Your OpenAI API Key:

1. Go to [OpenAI API Keys](https://platform.openai.com/account/api-keys)
2. Click **"Create new secret key"**
3. Copy your API key
4. Open the `assistant_gui.py` file and add your key like this:

```
openai.api_key = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
---
## 🚀 How to Run:
After installing all requirements and setting the API key, run the assistant:
```
python assistant_gui.py
```
---
## 📁 Project Files:

| File               | Description                            |
|-------------------|----------------------------------------|
| `assistant_gui.py` | Main Python script for the assistant   |
| `README.md`        | Project documentation and instructions |
