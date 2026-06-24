# =============================================================
# TASK 6 (BONUS): Build a reusable function
# -----------------------------------------------------------
# Write a function called get_github_user(username) that:
#   - Takes a GitHub username as a parameter
#   - Makes a GET request to the GitHub API
#   - Returns a dictionary with just these fields:
#       { 'name', 'username', 'repos', 'followers' }
#   - Returns None if the user is not found (404)
#
# Then call it with 3 different usernames and print results
#
# This is how you'll structure real-world API wrapper
# functions in your AI automation projects
# =============================================================

import requests

BASE_URL = "https://api.github.com"
HTTPBIN_URL = "https://httpbin.org"
YOUR_GITHUB_USERNAME = "singhkuljit107"


def get_github_user(username):
    try:
        r = requests.get(f'{BASE_URL}/users/{username}')
        r.raise_for_status()
        data = r.json()
        return {
            'name': data['name'],
            'username': data['login'],
            'repos': data['public_repos'],
            'followers': data['followers']
        }
    except requests.HTTPError:
        print('An HTTP error occurred.')


usernames = ['singhkuljit107', 'torvalds', 'fake_user_xyz']

for username in usernames:
    result = get_github_user(username)
    if result:
        print(result)
    else:
        print(f"'{username}' not found")
