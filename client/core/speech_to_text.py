import speech_recognition as sr
import whisper
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile


model = whisper.load_model("small")


def transcribe_audio_whisper():
    threshold = 100               
    silence_duration = 1.0        
    max_duration = 10             
    sample_rate = 48000
    frame_duration = 0.1          
    frame_samples = int(sample_rate * frame_duration)

    print("Parla quando vuoi...")

    buffer = []
    silence_counter = 0

    stream = sd.InputStream(samplerate=sample_rate, channels=1, dtype='int16')
    stream.start()

    try:
        while True:
            audio_chunk, _ = stream.read(frame_samples)
            audio_chunk = np.squeeze(audio_chunk)

            buffer.append(audio_chunk)

            volume = np.abs(audio_chunk).mean()
            if volume < threshold:
                silence_counter += frame_duration
            else:
                silence_counter = 0

            if silence_counter >= silence_duration:
                break

            if len(buffer) * frame_duration >= max_duration:
                print("Durata massima raggiunta.")
                break
    finally:
        stream.stop()
        stream.close()

    audio_data = np.concatenate(buffer)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, sample_rate, audio_data)
        result = model.transcribe(f.name, language="it")
        return result["text"].strip().rstrip('.')
