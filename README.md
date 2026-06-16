# Superhighway Examples

Runnable examples for the [Superhighway](https://superhighway.walls.sh) web search API — a search, news, images, scrape, and research API for AI agents.

## Get an API Key

Free at [superhighway.walls.sh/pricing](https://superhighway.walls.sh/pricing) — no credit card required.

Or: pay per call with USDC via [x402](https://superhighway.walls.sh/guides/x402-pay-per-call) — no signup, no API key.

## Examples

| Example | Description | Guide |
|---------|-------------|-------|
| [news_briefing/](news_briefing/) | Fetch news on custom topics, deduplicate, summarize with GPT, schedule via cron | [Guide →](https://superhighway.walls.sh/guides/news-briefing-agent) |
| [web_search/](web_search/) | Simple search agent: query → results → LLM summary | [Guide →](https://superhighway.walls.sh/guides/web-search-openai-function-calling) |
| [scrape_and_analyze/](scrape_and_analyze/) | Scrape any URL, extract clean Markdown, analyze with LLM | [Guide →](https://superhighway.walls.sh/guides/web-scraping) |

## Setup

Each example has its own `requirements.txt`. General setup:

```bash
git clone https://github.com/patwalls/superhighway-examples
cd superhighway-examples/<example>
pip install -r requirements.txt
cp .env.example .env   # fill in your keys
python <script>.py
```

## API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /search` | Web search with results + content |
| `GET /news` | Recent news articles |
| `GET /images` | Image search |
| `GET /scrape` | Convert any URL to clean Markdown |
| `GET /research` | Multi-source research with synthesis |

Full docs at [superhighway.walls.sh](https://superhighway.walls.sh).
