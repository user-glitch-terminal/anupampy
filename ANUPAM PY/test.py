# === Jarvis Voice Assistant ===
# Requirements: pip install openai speechrecognition pyttsx3 pyaudio

import openai
import speech_recognition as sr
import pyttsx3
import os

# ---------- CONFIG ----------
openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace with your API key
MODEL = "gpt-4o-mini"  # You can use gpt-4o, gpt-4-turbo, etc.

# ---------- SETUP ----------
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # [0]=US male, [1]=UK female (usually)
engine.setProperty('rate', 180)

r = sr.Recognizer()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("🗣️ You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn’t catch that.")
        return None
    except sr.RequestError:
        speak("Speech service is unavailable.")
        return None

def ask_jarvis(prompt):
    try:
        response = openai.ChatCompletion.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "You are Jarvis, a smart, witty, and helpful AI assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    speak("Jarvis online. How can I assist you today?")
    while True:
        command = listen()
        if command:
            if any(exit_word in command.lower() for exit_word in ["exit", "quit", "stop", "goodbye"]):
                speak("Goodbye, sir.")
                break
            reply = ask_jarvis(command)
            speak(reply)

if __name__ == "__main__":
    main()
