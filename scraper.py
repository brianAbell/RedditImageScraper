import os
import praw
import requests

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

def download_images(posts):
    """
    Downloads images from a list of Reddit posts.

    Args:
    - posts (list): A list of Reddit post objects fetched using PRAW.

    Notes:
    - Only downloads images with 'jpg', 'jpeg', or 'png' extensions.
    - Uses the post's URL to download the image.
    - Saves the image with its original name in the current directory.
    """

    # Loop through each post object in the list
    for post in posts:
        
        # Extract the direct URL to the image from the post
        image_url = post.url
        
        # Extract the image's filename from its URL.
        # This is done by splitting the URL at each "/" and taking the last segment.
        image_name = image_url.split("/")[-1]
        
        # Open (or create) an image file in binary write mode
        with open(image_name, 'wb') as f:
            
            # Send a GET request to the image URL to fetch the raw image content
            image = requests.get(image_url).content
            
            # Write the raw image content to the file
            f.write(image)
