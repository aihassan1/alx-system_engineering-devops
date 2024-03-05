#!/usr/bin/python3
"""function that queries the Reddit API and prints
    the titles of the first 10 hot posts
    listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    headers = {"user-agent": "testuser_1.0"}

    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
