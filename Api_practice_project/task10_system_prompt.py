import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}


def ask_assistant(system_prompt, question):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 150
    }

    r = requests.post(url, headers=headers, json=payload)
    r.raise_for_status()

    return r.json()['choices'][0]['message']['content']


# same question, three different assistants
question = "What is Python?"

print("ASSISTANT 1 - Simple Teacher:")
print(ask_assistant(
    "You are a teacher explaining to a 10 year old. Use very simple words.", question))

print("\nASSISTANT 2 - Senior Engineer:")
print(ask_assistant(
    "You are a senior software engineer. Be technical and precise.", question))

print("\nASSISTANT 3 - Funny Explainer:")
print(ask_assistant(
    "You are a comedian who explains tech concepts using jokes and humor.", question))
