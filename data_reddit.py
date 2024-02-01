import praw
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

reddit = praw.Reddit(
    client_id= os.getenv('CLIENT_ID'),
    client_secret= os.getenv('CLIENT_SECRET'),
    user_agent= os.getenv('USER_AGENT')
)

""" subs = reddit.subreddit('health').hot(limit=10)

for submission in subs:
    print(submission.title) """
    
""" subreddit = reddit.subreddit('COVID19')

# Obtener los últimos 100 posts del subreddit
for post in subreddit.new(limit=100):
    print(post.title, post.selftext) """

subreddit = reddit.subreddit('COVID19')
posts = []

for post in subreddit.new(limit=100):
    posts.append({
        "title": post.title,
        "text": post.selftext,
        
    })

df = pd.DataFrame(posts)
print(df.head())