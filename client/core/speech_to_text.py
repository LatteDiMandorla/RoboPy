import speech_recognition as sr
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile


model = whisper.load_model("small")
# Initialize the recognizer = sr.Recognizer()


def transcribe_audio_whisper():
    duration = 4
    sample_rate = 48000 

    print("Speak now")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, sample_rate, recording)
        result = model.transcribe(f.name, language="it")
        return result["text"].strip().rstrip('.')
