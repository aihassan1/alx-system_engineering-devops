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
    headers = {'User-Agent': 'Reddit API Client'}

    response = requests.post(url=url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
