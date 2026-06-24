# =============================================================
# TASK 5: Error handling with raise_for_status()
# -----------------------------------------------------------
# Make a GET request to this URL (it intentionally returns 404):
#   https://api.github.com/users/this_user_does_not_exist_xyz123
#
# Handle it properly:
#   - Wrap in try/except
#   - If successful: print "User found!"
#   - If HTTPError: print the status code and "User not found!"
#   - If ConnectionError: print "No internet connection"
#   - If Timeout: print "Request timed out"
#
# HINT: Use requests.exceptions.HTTPError,
#       requests.exceptions.ConnectionError,
#       requests.exceptions.Timeout
# =============================================================
import requests

BASE_URL = "https://api.github.com"
HTTPBIN_URL = "https://httpbin.org"
YOUR_GITHUB_USERNAME = "singhkuljit107"

try:
    url = 'https://api.github.com/users/this_user_does_not_exist_xyz123'
    r = requests.get(url)
    r.raise_for_status()
    print("User Found")


except requests.exceptions.HTTPError as e:
    print(f"HTTP Error: {r.status_code} - User not found!")

except requests.exceptions.ConnectionError:
    print("No internet connection")

except requests.exceptions.Timeout:
    print("Request timed out")
