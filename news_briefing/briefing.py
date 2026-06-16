"""News briefing agent for the Superhighway API.

Fetches recent news on a set of topics, deduplicates by URL, summarizes each
topic with an LLM, and writes a formatted Markdown briefing.

Run it directly:

    python briefing.py

Or schedule it daily with cron:

    0 7 * * * cd /path/to/news_briefing && /usr/bin/python3 briefing.py

Guide: https://superhighway.walls.sh/guides/news-briefing-agent
"""

import os
from datetime import datetime

import requests
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

SUPERHIGHWAY_KEY = os.getenv("SUPERHIGHWAY_API_KEY")
llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TOPICS = [
    "AI agents and autonomous systems",
    "large language model releases",
    "AI regulation and policy",
]


def fetch_news(topic: str, max_articles: int = 5) -> list[dict]:
    """Fetch recent news articles on a topic from the Superhighway API."""
    r = requests.get(
        "https://superhighway.walls.sh/news",
        params={"q": topic, "count": max_articles},
        headers={"Authorization": f"Bearer {SUPERHIGHWAY_KEY}"},
    )
    r.raise_for_status()
    return r.json().get("articles", [])


def deduplicate(articles: list[dict]) -> list[dict]:
    """Remove duplicate articles by URL, preserving order."""
    seen_urls = set()
    unique = []
    for a in articles:
        url = a.get("url")
        if url and url not in seen_urls:
            seen_urls.add(url)
            unique.append(a)
    return unique


def write_briefing(topic: str, articles: list[dict]) -> str:
    """Summarize a topic's articles into a short briefing with an LLM."""
    article_text = "\n".join(
        f"- {a.get('title', 'Untitled')} ({a.get('source', 'unknown')}): "
        f"{a.get('description', '')}"
        for a in articles[:5]
    )
    response = llm.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a news editor writing concise briefings.",
            },
            {
                "role": "user",
                "content": (
                    f'Write a 2-3 sentence briefing on "{topic}" based on these '
                    f"articles:\n\n{article_text}\n\nBe factual and concise."
                ),
            },
        ],
    )
    return response.choices[0].message.content


def generate_briefing(topics: list[str]) -> str:
    """Run the full pipeline for every topic and return Markdown."""
    today = datetime.now().strftime("%B %d, %Y")
    sections = [f"# AI News Briefing — {today}\n"]

    for topic in topics:
        articles = fetch_news(topic)
        unique = deduplicate(articles)
        if not unique:
            continue
        briefing = write_briefing(topic, unique)
        sections.append(f"## {topic.title()}\n\n{briefing}\n")
        sections.append("**Sources:**")
        for a in unique[:3]:
            sections.append(f"- [{a.get('title', 'Untitled')}]({a['url']})")
        sections.append("")

    return "\n".join(sections)


if __name__ == "__main__":
    briefing = generate_briefing(TOPICS)
    print(briefing)
    with open("briefing.md", "w") as f:
        f.write(briefing)
    print("\nSaved to briefing.md")
