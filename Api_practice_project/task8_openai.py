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

payload = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {"role": "user", "content": "Explain what a REST API is in 2 sentences"}
    ]
}

r = requests.post(url, headers=headers, json=payload)
r.raise_for_status()

data = r.json()
response_text = data['choices'][0]['message']['content']
print(response_text)
