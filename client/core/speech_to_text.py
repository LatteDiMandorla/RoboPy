import speech_recognition as sr
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile


model = whisper.load_model("small")
# Initialize the recognizer = sr.Recognizer()

def transcribe_audio():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 0.5
    with sr.Microphone() as source:
        print("In ascolto...")
        recognizer.adjust_for_ambient_noise(source, duration=3.0)  
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language="it-IT")
        return text
    except sr.UnknownValueError:
        print("Non ho capito cosa hai detto.")
        return None
    except sr.RequestError as e:
        print(f"Errore nel servizio Google Speech: {e}")
        return None





def transcribe_audio_whisper():
    duration = 4
    sample_rate = 16000

    print("🎙️ Parla ora...")
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, sample_rate, recording)
        result = model.transcribe(f.name, language="it")
        return result["text"].strip().rstrip('.')
