"""
Challenge on DataQuest to work with reddit API to:
1. Retrieve a list of trending posts on a particular subreddit
2. Explore the comments on a single article
3. Post my own comment on an article
"""
import requests

# uses OAuth to authenticate
headers = {"Authorization": "bearer  13426216-4U1ckno9J5AiK72VRbpEeBaMSKk",
           "User-Agent": "Dataquest/1.0"}
parameters = {"t": "day"}

# retrieve the /r/python subreddit's top posts for the past day using the
# /r/python/top endpoint. t=day shows time is one day
response = requests.get("https://oauth.reddit.com/r/python/top",
                        headers=headers, params=parameters)
python_top = response.json()
# python_top is a dictionary containing information about all of the individual
#  posts that users submitted during the past day.

# Explore the python_top dictionary. Extract the list containing all of
# the posts, and assign it to python_top_articles
python_top_articles = python_top["data"]["children"]
print(type(python_top_articles))
print("----------------------------")
print("----------------------------")


# getting the most upvoted post inside the python_top_articles
most_upvoted = ""
upvotes = 0
for article in python_top_articles:
    if article["data"]["ups"] >= upvotes:
        most_upvoted = article["data"]["id"]
        upvotes = article["data"]["ups"]

# retrieve the comments on the most upvoted post it using the
#  /r/{subreddit}/comments/{article} endpoint. The items that have brackets
# around them are replaced with the appropriate values: {subreddit}
# - The name of the subreddit the post appears in
# (omit the leading /r, because it already exists).
# Use python for the python subreddit, for example. {article} -
# The ID for the post whose comments we want to retrieve.
response_comments = requests.get(
    "https://oauth.reddit.com/r/python/comments/4b7w9u", headers=headers)
comments = response_comments.json()
# getting the most upvoted comment
most_upvoted_com = ""
upvotes_com = 0
comments_list = comments[1]["data"]["children"]
for com in comments_list:
    if com["data"]["ups"] >= upvotes_com:
        most_upvoted_com = com["data"]["id"]
        upvotes_com = com["data"]["ups"]

print(most_upvoted_com)

# upvoting a comment with the /api/vote endpoint
# parameters: dir - Vote direction: 1, 0, or -1. 1 is an upvote,
# and -1 is a downvote.
# id - The ID for the post or comment to upvote.
payload = {"dir": 1, "id": "d16y4ry"}
response_upvote = requests.post("https://oauth.reddit.com/api/vote",
                                json=payload, headers=headers)
status = response_upvote.status_code
print(status)
