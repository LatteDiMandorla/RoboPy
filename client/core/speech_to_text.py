import speech_recognition as sr

# Initialize the recognizer = sr.Recognizer()
recognizer = sr.Recognizer()
def transcribe_audio():
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="it-IT")
            return text
        except sr.UnknownValueError:
            return

