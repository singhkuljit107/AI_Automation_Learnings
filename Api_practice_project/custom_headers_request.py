
# =============================================================
# TASK 3: Send custom headers with a request
# -----------------------------------------------------------
# Repeat Task 1 BUT this time add a custom header:
#   'User-Agent': 'MyGitHubExplorer/1.0'
#
# GitHub API actually requires a User-Agent header in
# production — good practice to include it
#
# After the request, print:
#   - The User-Agent you SENT (from r.request.headers)
#   - The Content-Type you RECEIVED (from r.headers)
#
# HINT:
#   r.request.headers  → headers you sent
#   r.headers          → headers server sent back
# =============================================================
import requests

BASE_URL = "https://api.github.com"
HTTPBIN_URL = "https://httpbin.org"
YOUR_GITHUB_USERNAME = "singhkuljit107"

headers = {'User-Agent': 'MyGitHubExplorer/1.0'}
r = requests.get(f'{BASE_URL}/users/{YOUR_GITHUB_USERNAME}', headers=headers)
# data = r.json()
print(r.headers['Content-Type'])
print(r.request.headers['User-Agent'])
