import whisper
import sounddevice as sd
import numpy as np
import wavio

# Function to record audio
def record_audio(filename, duration=5, fs=44100):
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype=np.float32)
    sd.wait()  # Wait until recording is finished
    print("Recording complete.")
    wavio.write(filename, audio, fs, sampwidth=2)

# Use Whisper to transcribe
def transcribe_audio(filename):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    print("Transcription:", result["text"])

if __name__ == "__main__":
    # Record and transcribe
    audio_file = "recorded_audio.wav"
    record_audio(audio_file, duration=10)
    transcribe_audio(audio_file)
