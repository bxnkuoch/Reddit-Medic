import os
import praw

class RedditClient:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=os.getenv("REDDIT_CLIENT_ID"),
            client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
            user_agent="RedditInsightAgent/0.1"
        )

    def fetch_posts(self, subreddit_name: str, limit: int, time_filter: str = "day") -> list[dict]:
        subreddit = self.reddit.subreddit(subreddit_name)
        posts_data = []

        # Use subreddit.top() to respect time_filter
        for post in subreddit.top(limit=limit, time_filter=time_filter):
            post.comments.replace_more(limit=0)
            top_comments = "\n".join([c.body for c in post.comments[:5]])
            posts_data.append({
                "title": post.title,
                "content": post.selftext + "\nTop comments:\n" + top_comments
            })

        return posts_data
