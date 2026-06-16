# News Briefing Agent

Fetches recent news on a set of topics from the Superhighway `/news` endpoint,
deduplicates articles by URL, summarizes each topic with GPT-4o-mini, and writes
a formatted Markdown briefing to `briefing.md`.

## Run

```bash
pip install -r requirements.txt
cp .env.example .env   # add your SUPERHIGHWAY_API_KEY and OPENAI_API_KEY
python briefing.py
```

Edit the `TOPICS` list in `briefing.py` to customize what gets covered.

## Schedule daily (cron)

```bash
0 7 * * * cd /path/to/news_briefing && /usr/bin/python3 briefing.py
```

Full walkthrough: [superhighway.walls.sh/guides/news-briefing-agent](https://superhighway.walls.sh/guides/news-briefing-agent)
