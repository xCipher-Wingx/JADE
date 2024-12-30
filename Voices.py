#checking for different voices on the system
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice {i}:")
    print(f" - Name: {voice.name}")
    print(f" - ID: {voice.id}")
    print(f" - Gender: {'Male' if 'male' in voice.name.lower() else 'Female'}")
