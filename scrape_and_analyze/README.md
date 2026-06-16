# Scrape and Analyze

Scrapes any URL into clean Markdown via the Superhighway `/scrape` endpoint,
then answers a question about the page with GPT-4o-mini.

## Run

```bash
pip install -r requirements.txt
cp .env.example .env   # add your SUPERHIGHWAY_API_KEY and OPENAI_API_KEY
python scrape_analyze.py https://superhighway.walls.sh "What does this service offer?"
```

Both arguments are optional — they default to the Superhighway homepage and a
generic question.

Full walkthrough: [superhighway.walls.sh/guides/web-scraping](https://superhighway.walls.sh/guides/web-scraping)
