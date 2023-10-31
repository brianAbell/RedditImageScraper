# RedditImageScraper
Description

This project serves as a utility tool tailored for avid Reddit enthusiasts and data collectors. It's designed to efficiently scrape and download image posts from specified subreddits.

The underlying code leverages the capabilities of praw, the Python Reddit API Wrapper, ensuring reliable and consistent interaction with Reddit's platform. This is combined with other libraries such as requests and os to seamlessly manage image downloads.

Key features:
  * Subreddit Specificity: Users can target specific subreddits for image scraping.
  * Image Type Filtering: The scraper only fetches posts linking to 'jpg', 'jpeg', or 'png' images, ensuring quality and relevance.
  * Seamless Download: Images are saved automatically to an 'output' directory for easy access and organization.

Getting Started

Dependencies

makefile

* praw==7.4.0
* requests==2.26.0
* python-dotenv==0.19.1

Installing

Clone the repository:
```
git clone [your-repo-link]
```
Navigate to the directory:
```
cd [your-repo-name]
```

Create a virtual environment (Optional but recommended):
```
python -m venv venv
```
Activate the virtual environment:

  On Windows:
  ```
  venv\Scripts\activate
  ```
  
  On MacOS and Linux:
  ```
  source venv/bin/activate
  ```

Install the dependencies:
```
pip install -r requirements.txt
```

Executing program

Simply run:
```
python reddit_image_scraper.py
```
And follow the prompt to enter the desired subreddit name.

Help

  * Ensure your .env file contains the correct Reddit API credentials.
  * Ensure all dependencies are installed: pip install -r requirements.txt.
  * Ensure your virtual environment is activated.
  * Check the logs for any specific error messages and consult praw documentation or search for them online.

For more assistance or to report bugs, please open an issue on this repository.

Authors

Brian Bell
[@BrianBe11](https://www.linkedin.com/in/brianbe11/)

Version History

  * 1.0
        * Initial release with image scraping and downloading functionality.
        * Added .env support for secure credential storage.
        * See commit change or See release history.
