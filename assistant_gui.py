import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import pyttsx3
import openai
import threading

# API KEY من OpenAI
openai.api_key = "هناال api"

# الصوت
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("تحدث الآن...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="ar-SA")
    except:
        return "لم أفهم، حاول مرة أخرى."

def ask_gpt(text):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": text}]
        )
        return res['choices'][0]['message']['content']
    except:
        return "حدث خطأ في الاتصال بـ GPT."

# الدالة اللي تتعامل مع الضغط على الزر (بخيط منفصل)
def handle_click():
    threading.Thread(target=process_interaction).start()

def process_interaction():
    user_input = listen()
    chat_box.insert(tk.END, "🧑‍💬 أنت: " + user_input + "\n")
    response = ask_gpt(user_input)
    chat_box.insert(tk.END, "🤖 GPT: " + response + "\n\n")
    speak(response)

# الواجهة
root = tk.Tk()
root.title("🎤 مساعد صوتي ذكي")
root.geometry("500x500")
root.config(bg="#f0f0f0")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

mic_button = tk.Button(root, text="🎤 اضغط للتحدث", font=("Arial", 14), bg="#4CAF50", fg="white", command=handle_click)
mic_button.pack(pady=10)

# أول صوت ترحيبي (بخيط حتى ما يعلق)
threading.Thread(target=lambda: speak("مرحباً بك، اضغط على الزر وابدأ بالتحدث.")).start()

root.mainloop()
