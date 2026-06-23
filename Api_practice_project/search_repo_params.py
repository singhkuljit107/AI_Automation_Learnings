# =============================================================
# TASK 2: Search GitHub repositories with params
# -----------------------------------------------------------
# Use requests.get() with params= to search GitHub repos
# API endpoint: https://api.github.com/search/repositories
#
# Send these params:
#   q      = "python automation"   (search keyword)
#   sort   = "stars"               (sort by stars)
#   per_page = 3                   (only get 3 results)
#
# Then print the name and star count of each repo found
#
# HINT: response structure is:
#   data['items'] → list of repos
#   each repo has 'full_name' and 'stargazers_count'
# =============================================================
import requests
BASE_URL = "https://api.github.com"
HTTPBIN_URL = "https://httpbin.org"
YOUR_GITHUB_USERNAME = "singhkuljit107"

payload = {'q': 'python automation', 'sort': 'stars', 'per_page': 3}

r = requests.get(f'{BASE_URL}/search/repositories', params=payload)

data = r.json()

for repo in data['items']:
    print(repo['full_name'], repo['stargazers_count'])
