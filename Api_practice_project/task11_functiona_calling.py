import requests
from dotenv import load_dotenv
import os
import json

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
url = "https://api.openai.com/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Step 1: Define your actual Python function


def get_weather(city):
    # In real life this would call a weather API
    # For now we return fake data
    weather_data = {
        "New York": {"temperature": "72°F", "condition": "Sunny"},
        "London": {"temperature": "58°F", "condition": "Cloudy"},
        "Toronto": {"temperature": "65°F", "condition": "Partly Cloudy"},
    }
    return weather_data.get(city, {"temperature": "Unknown", "condition": "Unknown"})


# Step 2: Describe your function to OpenAI
functions = [
    {
        "name": "get_weather",
        "description": "Get the current weather for a given city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "The name of the city"
                }
            },
            "required": ["city"]
        }
    }
]

# Step 3: Send message with function definitions
messages = [
    {"role": "system", "content": "You are a helpful weather assistant"},
    {"role": "user", "content": "What is the weather in New York?"}
]

payload = {
    "model": "gpt-3.5-turbo",
    "messages": messages,
    "functions": functions,
    "function_call": "auto"  # AI decides when to call a function
}

r = requests.post(url, headers=headers, json=payload)
r.raise_for_status()

response = r.json()
message = response['choices'][0]['message']

# Step 4: Check if AI wants to call a function
if message.get('function_call'):
    function_name = message['function_call']['name']
    arguments = json.loads(message['function_call']['arguments'])

    print(f"AI wants to call: {function_name}")
    print(f"With arguments: {arguments}")

    # Step 5: Actually run the function
    result = get_weather(arguments['city'])
    print(f"Function returned: {result}")

    # Step 6: Send result back to AI for final response
    messages.append(message)
    messages.append({
        "role": "function",
        "name": function_name,
        "content": json.dumps(result)
    })

    final_payload = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }

    final_r = requests.post(url, headers=headers, json=final_payload)
    final_r.raise_for_status()

    final_reply = final_r.json()['choices'][0]['message']['content']
    print(f"\nFinal AI Response: {final_reply}")

else:
    print(response['choices'][0]['message']['content'])
