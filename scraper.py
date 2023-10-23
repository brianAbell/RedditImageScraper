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