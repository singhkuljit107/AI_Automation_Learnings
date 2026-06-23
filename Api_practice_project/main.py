"""
=============================================================
  MINI PROJECT: GitHub Profile & Repo Explorer
  Topic: Python requests — GET, POST, headers, params,
         status codes, error handling
=============================================================

INSTRUCTIONS:
  - Read each TASK carefully before writing code
  - Do NOT copy-paste — type everything yourself
  - Run the file after completing each task to test it
  - Replace YOUR_GITHUB_USERNAME with your actual username

Run with:  python api_practice_project.py
=============================================================
"""

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

def task1_get_github_profile():
    print("\n" + "="*50)
    print("TASK 1: My GitHub Profile")
    print("="*50)

    # YOUR CODE HERE
    pass


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

def task2_search_repos():
    print("\n" + "="*50)
    print("TASK 2: Search GitHub Repos")
    print("="*50)

    # YOUR CODE HERE
    pass


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

def task3_custom_headers():
    print("\n" + "="*50)
    print("TASK 3: Custom Headers")
    print("="*50)

    # YOUR CODE HERE
    pass


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

def task4_post_request():
    print("\n" + "="*50)
    print("TASK 4: POST Request")
    print("="*50)

    # YOUR CODE HERE
    pass


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

def task5_error_handling():
    print("\n" + "="*50)
    print("TASK 5: Error Handling")
    print("="*50)

    # YOUR CODE HERE
    pass


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

def get_github_user(username):
    # YOUR CODE HERE
    pass


def task6_bonus_reusable_function():
    print("\n" + "="*50)
    print("TASK 6 (BONUS): Reusable Function")
    print("="*50)

    usernames = [YOUR_GITHUB_USERNAME, "torvalds", "this_fake_user_xyz"]

    for username in usernames:
        result = get_github_user(username)
        if result:
            print(f"\nFound: {result}")
        else:
            print(f"\n'{username}' not found")


# =============================================================
# MAIN — runs all tasks in order
# Complete each task one at a time, not all at once
# Comment out tasks you haven't reached yet
# =============================================================

if __name__ == "__main__":
    task1_get_github_profile()
    task2_search_repos()
    task3_custom_headers()
    task4_post_request()
    task5_error_handling()
    task6_bonus_reusable_function()

    print("\n" + "="*50)
    print("All tasks complete!")
    print("="*50)
