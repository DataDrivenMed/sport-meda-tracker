import glob, markdown, pathlib, datetime as dt

md_file = sorted(glob.glob("digests/weekly_*.md"))[-1]
body    = markdown.markdown(open(md_file).read(), extensions=["tables"])
stamp   = dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
  <title>Indian Sports Mentions</title>
  <link rel="stylesheet" href="https://cdn.simplecss.org/simple.min.css">
</head><body>
  <h1>Indian Sports Media Mentions</h1>
  <p><em>Generated {stamp}</em></p>
  {body}
</body></html>"""

out = pathlib.Path("docs/index.html")
out.parent.mkdir(exist_ok=True)
out.write_text(html)
print("Wrote", out)
