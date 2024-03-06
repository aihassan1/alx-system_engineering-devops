#!/usr/bin/python3
""" a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """a recursive function that queries the Reddit API and returns a list
    containing the titles of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"user-agent": "testuser_1.0"}
    params = {"limit": 100}
    if after:
        params["after"] = after

    response = requests.get(
        url=url, headers=headers, allow_redirects=False, params=params
    )

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]
        for post in children:
            hot_list.append(post["data"]["title"])

        after = data["data"].get("after")
        if after:
            recurse(subreddit, hot_list, after)

    return hot_list
