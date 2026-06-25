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

# conversation history — starts with system message
messages = [
    {"role": "system", "content": "You are a helpful assistant who explains programming concepts simply"}
]

print("Chatbot ready! Type 'quit' to exit\n")

while True:
    # get user input
    user_input = input("You: ")

    # exit if user types quit
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    # add user message to history
    messages.append({"role": "user", "content": user_input})

    # send full conversation to OpenAI
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages,
        "temperature": 0.7,
        "max_tokens": 150
    }

    r = requests.post(url, headers=headers, json=payload)
    r.raise_for_status()

    # extract reply
    reply = r.json()['choices'][0]['message']['content']

    # add assistant reply to history
    messages.append({"role": "assistant", "content": reply})

    print(f"\nAssistant: {reply}\n")
