import argparse
from dotenv import load_dotenv
from agent import RedditInsightAgent

def main():
    load_dotenv()  # Load environment variables from .env

    parser = argparse.ArgumentParser(description="Reddit Insight Agent")
    parser.add_argument("--subreddit", type=str, default="AskDocs", help="Subreddit to analyze")
    parser.add_argument("--limit", type=int, default=5, help="Number of posts to analyze")
    parser.add_argument("--time_filter", type=str, default="day", help="Time filter for posts (e.g., day, week, month, year, all)")
    args = parser.parse_args()

    agent = RedditInsightAgent(subreddit=args.subreddit, limit=args.limit, time_filter=args.time_filter)
    summary = agent.run()
    print("\n===== Summary =====\n")
    print(summary)

if __name__ == "__main__":
    main()
