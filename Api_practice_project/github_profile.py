import requests

BASE_URL = "https://api.github.com"
HTTPBIN_URL = "https://httpbin.org"
YOUR_GITHUB_USERNAME = "singhkuljit107"  # <-- CHANGE THIS


# =============================================================
# TASK 1: Fetch your GitHub profile
# -----------------------------------------------------------
# Use requests.get() to call:
#   https://api.github.com/users/YOUR_GITHUB_USERNAME
#
# Then print:
#   - Your name
#   - Your public repos count
#   - Your location
#   - Your GitHub profile URL
#
# HINT: Use r.json() to parse response, then access keys like
#       data['name'], data['public_repos'], etc.
#
# Try it in browser first to see all available fields:
#   https://api.github.com/users/your_username_here
# =============================================================
r = requests.get(f'{BASE_URL}/users/{YOUR_GITHUB_USERNAME}')
data = r.json()
name = data["name"]
repo_count = data["public_repos"]
location = data["location"] or "Not Set"
profile_url = data['html_url']
final_data = f"My name is: {name}\nMy repo count is: {repo_count}\nlocation: {location} \nProfile URL: {profile_url}"
print(final_data)
