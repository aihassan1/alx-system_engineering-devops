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
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}
    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
