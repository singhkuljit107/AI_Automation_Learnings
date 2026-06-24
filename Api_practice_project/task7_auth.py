import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://api.github.com"

token = os.getenv("GITHUB_TOKEN")

headers = {
    "Authorization": f"Bearer {token}",
    "User-Agent": "MyGitHubExplorer/1.0"
}

r = requests.get(f'{BASE_URL}/user', headers=headers)
data = r.json()

print(f"Logged in as: {data['login']}")
print(f"Name: {data['name']}")
print(f"Private repos: {data['total_private_repos']}")
print(f"Email: {data['email']}")
