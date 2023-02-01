# ADVANCED API

File | Description
---- | -----------
[0-subs.py](./0-subs.py) | Function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.
[1-top_ten.py](./1-top_ten.py) | Function that queries the Reddit API and prints the titles of the first ten hot posts listed for a given subreddit
[2-recurse.py](./2-recurse.py) | A recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit the function returns None
[100-count.py](./100-count.py) | A recursive function that queries the Reddit API , parses the title of all hot articles, and prints a sorted count of given keywords(case-insensitive, delimited by spaces. Javascript counts as javascript, but not java
