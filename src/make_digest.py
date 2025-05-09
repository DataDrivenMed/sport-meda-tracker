import json, datetime as dt, pathlib

pathlib.Path("digests").mkdir(exist_ok=True)
counts = json.load(open("data/counts.json"))
week   = dt.date.today().isoformat()

lines = [f"# Indian Sports Media Mentions — Week of {week}", ""]
for sport, val in counts.items():
    lines.append(f"* **{sport.capitalize()}**: {val}")

out = pathlib.Path(f"digests/weekly_{week}.md")
out.write_text("\n".join(lines))
print("Wrote", out)
