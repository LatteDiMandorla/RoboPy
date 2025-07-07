import speech_recognition as sr

# Initialize the recognizer = sr.Recognizer()

def transcribe_audio():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300
    recognizer.pause_threshold = 1.0
    with sr.Microphone() as source:
        print("In ascolto...")
        recognizer.adjust_for_ambient_noise(source, duration=1.0)  
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
