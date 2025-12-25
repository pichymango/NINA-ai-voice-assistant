import os
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import subprocess


 



def speak(text):
    print("🗣️ NINA:", text)
    subprocess.run([
        "osascript",
        "-e",
        f'say "{text}"'
    ])



def listen():
    print("🎤 Listening... Speak now")

    samplerate = 16000
    duration = 5

    audio_data = sd.rec(
        int(duration * samplerate),
        samplerate=samplerate,
        channels=1,
        dtype="int16"
    )
    sd.wait()

    audio = sr.AudioData(audio_data.tobytes(), samplerate, 2)
    recognizer = sr.Recognizer()

    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        print("🧑 You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("❌ Didn't catch that")
        return ""
    except sr.RequestError:
        print("❌ Network issue")
        return ""
