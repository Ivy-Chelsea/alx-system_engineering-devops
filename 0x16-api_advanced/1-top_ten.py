#!/usr/bin/python3
"""gets top 10 post on subredit"""
import json
import requests


def top_ten(subreddit):
    """gets the top 10 post of a subreddit"""
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    data = requests.get("https://www.reddit.com/r/{}/hot/.json"
                        .format(subreddit),
                        headers=user_agent,
                        allow_redirects=False)
    if data.status_code != 200:
        print("None")
        return
    json_data = data.json().get("data").get("children", [])
    if len(json_data) == 0:
        print("None")
        return
    for post in json_data[0:10]:
        print(post.get("data").get("title"))
