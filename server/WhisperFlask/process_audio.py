# process_audio.py
from openai import OpenAI
from time import sleep

client = OpenAI()

def summarize_transcription(transcript):
    # Define a prompt for the GPT-3 model
    prompt = f"I need a concise summary of the following transcript:\n\n{transcript}"

    # Use the GPT-3 model to generate a summary
    summary = chatgpt3(prompt)

    return summary

def write_notes(summary):
    # Define a prompt for the GPT-3 model
    prompt = f"I need important notes from the following summary:\n\n{summary}"

    # Use the GPT-3 model to generate notes
    notes = chatgpt3(prompt)

    return notes

def generate_synopsis(notes):
    # Define a prompt for the GPT-3 model
    prompt = f"I need a synopsis based on the following notes:\n\n{notes}"

    # Use the GPT-3 model to generate a synopsis
    synopsis = chatgpt3(prompt)

    return synopsis

def chatgpt3(userinput, temperature=0.6, frequency_penalty=0, presence_penalty=0):
    max_retry = 6
    retry = 0
    messagein = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": userinput },]
    while True:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                temperature=temperature,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
                messages=messagein
            )
            text = response.choices[0].message.content
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return "GPT3 error: %s" % oops
            print('Error communicating with OpenAI:', oops)
            sleep(5)


def transcribe_audio(audio_file_path):
    """Transcribe the given audio file using OpenAI Whisper ASR.

    Returns a dictionary with a single key "raw" containing the raw
    transcription text so that callers can safely access
    ``transcript["raw"]``.
    """
    with open(audio_file_path, 'rb') as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return {'raw': transcription.text}

