#Use Python 3.10.11
"""
TODO: 1. Work on naturalness of the speech output.
        2. Add more features to the speech recognition.
        3. Add more features to the speech output.
        
"""
import speech_recognition as sr
import pyttsx3

def speak_text(text):
    """Use text-to-speech to speak the given text."""
    engine = pyttsx3.init()
    # Change voice (e.g., male or female)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # Set to female voice
    
    # You can also adjust other properties
    engine.setProperty('rate', 150)  # Speech rate (default: 200)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    
    engine.say(text)
    engine.runAndWait()

def record_and_repeat():
    """Recognize user speech and repeat it back."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise. Please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Ready to receive your input. Start speaking...")
        
        try:
            # Listen to user's input
            audio_data = recognizer.listen(source, timeout=10)
            print("Recognizing speech...")
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio_data)
            print("You said:", text)
            # Speak back the text
            speak_text(text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            speak_text("Sorry, I could not understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak_text("There was an issue with the speech recognition service.")
        except Exception as ex:
            print(f"An error occurred: {ex}")
            speak_text("An unexpected error occurred.")

if __name__ == "__main__":
    record_and_repeat()
