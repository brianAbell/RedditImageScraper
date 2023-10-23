import os
import praw

# Load secrets from .env file
client_id = os.getenv('REDDIT_CLIENT_ID')
client_secret = os.getenv('REDDIT_CLIENT_SECRET')
username = os.getenv('REDDIT_USERNAME')
password = os.getenv('REDDIT_PASSWORD')

reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent='reddit_image_scraper',
                     username=username,
                     password=password)

# Fetch posts from subreddit
def get_image_posts(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    # for each post in 'hot' category, add valid image to list
    for post in subreddit.hot(limit=limit):
        if post.url.endswith(('jpg', 'jpeg', 'png')):
            posts.append(post)
    
    return posts