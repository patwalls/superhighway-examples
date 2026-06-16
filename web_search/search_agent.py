"""Simple search-and-summarize agent for the Superhighway API.

Queries the Superhighway /search endpoint and summarizes the top results with
an LLM.

Run it:

    python search_agent.py AI agent frameworks 2025

Guide: https://superhighway.walls.sh/guides/web-search-openai-function-calling
"""

import os
import sys

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SUPERHIGHWAY_KEY = os.getenv("SUPERHIGHWAY_API_KEY")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def search_and_summarize(query: str) -> str:
    # Fetch results
    r = requests.get(
        "https://superhighway.walls.sh/search",
        params={"q": query},
        headers={"Authorization": f"Bearer {SUPERHIGHWAY_KEY}"},
    )
    r.raise_for_status()
    results = r.json()["results"]

    # Build context
    context = "\n".join(
        f"{x['title']}: {x['url']}\n{x.get('content', '')}"
        for x in results[:5]
    )

    # Summarize
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Summarize the key findings from these search results.",
            },
            {
                "role": "user",
                "content": f"Query: {query}\n\nResults:\n{context}",
            },
        ],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    query = " ".join(sys.argv[1:]) or "AI agent frameworks 2025"
    print(search_and_summarize(query))
