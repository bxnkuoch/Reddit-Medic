import os
import openai

class Summarizer:
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def summarize(self, text: str) -> str:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes Reddit healthcare discussions."},
                {"role": "user", "content": f"Summarize the key concerns and themes from these Reddit posts:\n\n{text}"}
            ],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
