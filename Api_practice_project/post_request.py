# =============================================================
# TASK 4: POST request to httpbin
# -----------------------------------------------------------
# Send a POST request to https://httpbin.org/post
# with the following data (use json= not data=):
#   {
#     "name": "your name",
#     "learning": "python requests",
#     "day": 1
#   }
#
# Then print:
#   - The json field from the response (what you sent)
#   - The Content-Type header from the response
#
# HINT: When you use json=, your data shows under
#       r.json()['json'] in httpbin's response
# =============================================================
import requests
url = "https://httpbin.org/post"
payload = {
    "name": "Kuljit Singh",
    "learning": "python requests",
    "day": 2
}
r = requests.post(url, json=payload)
print(r.json()['json'])
print(r.headers['Content-Type'])
