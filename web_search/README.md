# Web Search Agent

A minimal search agent: takes a query, fetches results from the Superhighway
`/search` endpoint, and summarizes the top 5 with GPT-4o-mini.

## Run

```bash
pip install -r requirements.txt
cp .env.example .env   # add your SUPERHIGHWAY_API_KEY and OPENAI_API_KEY
python search_agent.py AI agent frameworks 2025
```

If no query is passed on the command line it defaults to
`AI agent frameworks 2025`.

Full walkthrough: [superhighway.walls.sh/guides/web-search-openai-function-calling](https://superhighway.walls.sh/guides/web-search-openai-function-calling)
