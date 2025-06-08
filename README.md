# Reddit Medic

Reddit Medic is a lightweight AI agent that fetches posts from healthcare-related subreddits and summarizes key concerns and discussion themes using OpenAI's GPT model. This tool helps surface meaningful insights from patient and provider conversations happening on Reddit, streamlining community-driven healthcare discourse.

---

## Features
- Fetches top Reddit posts from a given subreddit (e.g., `r/AskDocs`)
- Extracts post titles, content, and top comments
- Summarizes posts using GPT-3.5/4 via OpenAI API
- Supports configurable post limits and time filters (e.g., day, week, month)

---

## Design Choices, Tech Stack, and Algorithms

### Design
- **Simplicity**: A script-based interface that runs efficiently.
- **Clarity**: Explicit summaries of user-generated health questions and advice.
- **Flexibility**: Command-line options to customize subreddit, post count, and time window.

### Tech Stack
- **Python 3.9+**: General-purpose scripting and API interaction
- **PRAW**: Python Reddit API Wrapper for fetching Reddit posts and comments
- **OpenAI API**: GPT-3.5-turbo for text summarization
- **dotenv**: Securely loads API keys from a `.env` file

### Core Components
- `reddit_client.py`: Uses PRAW to fetch Reddit posts and top-level comments
- `summarizer.py`: Sends data to OpenAI Chat API and extracts the response summary
- `agent.py`: Orchestrates Reddit fetching and summarization into a pipeline
- `main.py`: CLI interface with support for arguments like `--subreddit`, `--limit`, `--time_filter`

### Summarization Algorithm
- Concatenates post title, selftext, and up to 5 top comments
- Sends this context to GPT as a `user` message with system prompt guidance
- Requests a summary of themes and concerns in healthcare discussions

### Environment Setup
Create a `.env` file with the following variables:
```env
REDDIT_CLIENT_ID=your_id
REDDIT_CLIENT_SECRET=your_secret
OPENAI_API_KEY=your_openai_key
```

### Run the agent
```bash
python main.py
```
This uses defaults:
- `--subreddit AskDocs`
- `--limit 5`
- `--time_filter day`

To customize:
```bash
python main.py --subreddit Health --limit 10 --time_filter month
```

---

## What I Can Improve With More Time
- Add a web UI for easier interaction
- Caching + retries to avoid hitting API rate limits
- Support for multiple subreddits or keyword filtering
- Visualization of topic clusters
- Deploy as a Flask/Streamlit web service for broader access
