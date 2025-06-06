from reddit_client import RedditClient
from summarizer import Summarizer

class RedditInsightAgent:
    def __init__(self, subreddit: str, limit: int = 5):
        self.subreddit = subreddit
        self.limit = limit
        self.reddit_client = RedditClient()
        self.summarizer = Summarizer()

    def run(self) -> str:
        posts = self.reddit_client.fetch_posts(self.subreddit, self.limit)
        formatted_input = self._format_for_summary(posts)
        summary = self.summarizer.summarize(formatted_input)
        return summary

    def _format_for_summary(self, posts: list[dict]) -> str:
        lines = []
        for i, post in enumerate(posts, start=1):
            lines.append(f"Post {i}: {post['title']}\n{post['content']}\n")
        return "\n\n".join(lines)
