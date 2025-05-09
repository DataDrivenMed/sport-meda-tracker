import feedparser, json, datetime as dt, pathlib

DATA = pathlib.Path("data"); DATA.mkdir(exist_ok=True)
feeds = open("src/feeds.txt").read().splitlines()
items = []
for url in feeds:
    d = feedparser.parse(url)
    for e in d.entries:
        items.append({
            "feed": url,
            "title": e.get("title",""),
            "summary": e.get("summary",""),
            "link": e.get("link",""),
            "published": e.get("published", "")
        })
out = DATA / f"rss_{dt.date.today()}.json"
out.write_text(json.dumps(items, indent=2))
print("Saved", len(items), "items to", out)
