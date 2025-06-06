import argparse
from dotenv import load_dotenv

load_dotenv()

from agent import RedditInsightAgent


def main():
    parser = argparse.ArgumentParser(description="Reddit Insight Agent")
    parser.add_argument("--subreddit", type=str, default="AskDocs", help="Subreddit to analyze")
    parser.add_argument("--limit", type=int, default=5, help="Number of posts to analyze")
    args = parser.parse_args()

    agent = RedditInsightAgent(subreddit=args.subreddit, limit=args.limit)
    summary = agent.run()
    print("\n===== Summary =====\n")
    print(summary)


if __name__ == "__main__":
    main()
