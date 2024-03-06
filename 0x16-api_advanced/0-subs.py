#!/usr/bin/python3
"""function that queries the Reddit API and
    returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and
    returns the number of subscribers
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Provide a custom User-Agent header
    headers = {"User-Agent": "custom_user_1.0"}

    response = requests.get(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0

    data = response.json()
    return data["data"]["subscribers"]
