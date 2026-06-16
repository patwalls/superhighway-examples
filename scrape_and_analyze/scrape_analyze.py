"""Scrape-and-analyze agent for the Superhighway API.

Scrapes any URL to clean Markdown via the Superhighway /scrape endpoint, then
answers a question about the page with an LLM.

Run it:

    python scrape_analyze.py https://superhighway.walls.sh "What does this service offer?"

Guide: https://superhighway.walls.sh/guides/web-scraping
"""

import os
import sys

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SUPERHIGHWAY_KEY = os.getenv("SUPERHIGHWAY_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def scrape_and_analyze(
    url: str, question: str = "What is the main content of this page?"
) -> str:
    r = requests.get(
        "https://superhighway.walls.sh/scrape",
        params={"url": url},
        headers={"Authorization": f"Bearer {SUPERHIGHWAY_KEY}"},
    )
    r.raise_for_status()
    data = r.json()
    markdown = data.get("markdown", "")[:4000]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Answer the question based on the page content.",
            },
            {
                "role": "user",
                "content": (
                    f"Page: {url}\n\nContent:\n{markdown}\n\nQuestion: {question}"
                ),
            },
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else "https://superhighway.walls.sh"
    question = sys.argv[2] if len(sys.argv) > 2 else "What does this service offer?"
    print(scrape_and_analyze(url, question))
