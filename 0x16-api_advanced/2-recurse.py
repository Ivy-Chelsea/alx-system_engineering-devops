#!/usr/bin/python3
import json
import requests


def recurse(subreddit, hot_list=[], after=None, ugly_flag=0):
    user_agent = {"User-Agent": "unix:0-subs.py:v1.0"}
    if after is None:
        if ugly_flag == 1:
            return hot_list
        data = requests.get("https://www.reddit.com/r/{}/hot/.json"
                            .format(subreddit),
                            headers=user_agent,
                            allow_redirects=False)
        if data.status_code != 200:
            return None
        else:
            json_data = data.json().get("data").get("children", [])
            for post in json_data:
                hot_list.append(post.get("data").get("title"))
            ugly_flag = 1
            after = data.json().get("data").get("after")
            return recurse(subreddit, hot_list, after, ugly_flag)
    else:
        data = requests.get("https://www.reddit.com/r/{}/hot/.json?after={}"
                            .format(subreddit, after),
                            headers=user_agent,
                            allow_redirects=False)
        json_data = data.json().get("data").get("children", [])
        for post in json_data:
                hot_list.append(post.get("data").get("title"))
        after = data.json().get("data").get("after")
        return recurse(subreddit, hot_list, after, ugly_flag)
