# process_audio.py
from openai import OpenAI

client = OpenAI()

def transcribe_audio(audio_file):
    # This function will send the audio file to Whisper ASR API and return the transcription
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    return transcription

def process_audio(file_path):
    transcription = transcribe_audio(file_path)

    return transcription
