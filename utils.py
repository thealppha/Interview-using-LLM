import openai

from dotenv import dotenv_values
from transformers import pipeline
from completion import Completion
from record_voice import Record

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

def run_question_bot(topic):
    prompt = f"""
            Write a {topic} interview question, don't use Q: ...
            """
        
    completion = Completion("text-davinci-003", prompt, max_tokens=50)
    response = completion.create_completion()["choices"][0]["text"].strip()

    return response

def recording():
    duration = 5

    record = Record(duration)
    record.record_voice()

def audio_2_text():
    audio_file= open("recording.wav", "rb")
    transcript = openai.Audio.translate("whisper-1", audio_file)

    return transcript

def rate_the_answer(question, answer):
    prompt = f"""
            Classify the answer according to the question as valid or invalid
            Desired:
            Q: {question}
            A: {answer}
            Result:
            Valid 
            """
        
    completion = Completion("text-davinci-003", prompt, max_tokens=50)
    response = completion.create_completion()["choices"][0]["text"].strip()

    return response
