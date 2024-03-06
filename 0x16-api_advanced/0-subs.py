#!/usr/bin/python3
"""function that queries the Reddit API and
    returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and
    returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Provide a custom User-Agent header
    headers = {"User-Agent": "custom_user_1.0"}

    response = requests.get(url=url, headers=headers, allow_redirects=False)
    """
    if response.status_code == 200:
        data = response.json()
        return data.get("data").get("subscribers")
    else:
        return 0
    """
    if response.status_code == 404:
        return 0

    results = response.json().get("data")
    return results.get("subscribers")
