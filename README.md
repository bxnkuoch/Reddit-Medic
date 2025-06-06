# Reddit Medic

## Overview

Reddit Medic is a mini AI-powered tool that fetches top posts and comments from a specified subreddit and summarizes key healthcare-related discussion themes using OpenAI's GPT models. This project combines Reddit data extraction with AI summarization to deliver actionable insights in the healthcare domain.

## Features

- Fetches posts and top comments from a subreddit using the Reddit API (PRAW)
- Summarizes discussions with OpenAI's GPT-3.5-turbo model
- Customizable via command-line arguments for subreddit and post limits
- Modular design for easy extension and improvements

### Example Usage

- python3 main.py --subreddit=SUBREDDIT_NAME --limit=NUM_OF_POSTS --time_filter=POSTS_TIME_PERIOD


### Requirements

- Python
- Reddit API credentials (client ID and client secret)  
- OpenAI API key  

### Your .env file should look like this:
REDDIT_CLIENT_ID=YOUR_REDDIT_CLIENT_ID <br>
REDDIT_CLIENT_SECRET=YOUR_REDDIT_SECRET_ID <br>
OPENAI_API_KEY=YOUR_OPENAI_KEY <br>

