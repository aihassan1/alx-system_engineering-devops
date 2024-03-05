#!/usr/bin/python3
"""function that queries the Reddit API and
    returns the number of subscribers
"""

import json
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and
    returns the number of subscribers
    """
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    # Provide a custom User-Agent header
    headers = {"User-Agent": "custom_user/1.0"}

    response = requests.get(url=url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
