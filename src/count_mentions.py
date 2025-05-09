import json, re, pathlib

DATA = pathlib.Path("data")
latest = sorted(DATA.glob("rss_*.json"))[-1]
items  = json.load(open(latest))

sports  = ["cricket","football","hockey","swimming","athletics"]
pattern = {s: re.compile(rf"\b{s}\b", re.I) for s in sports}
counts  = dict.fromkeys(sports, 0)

for it in items:
    text = it["title"] + " " + it["summary"]
    for s, p in pattern.items():
        if p.search(text):
            counts[s] += 1

out = DATA / "counts.json"
out.write_text(json.dumps(counts, indent=2))
print("Counts:", counts)
