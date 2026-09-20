#!/usr/bin/env python3
"""Regenerate the published HTML from the Markdown sources.

    privacy.md -> index.html          (https://kyralee22.github.io/bside-legal/)
    support.md -> support/index.html  (https://kyralee22.github.io/bside-legal/support/)

Run after editing either source, then commit everything it writes:

    pip3 install --user markdown
    python3 build.py && git commit -am "Update legal pages" && git push
"""
import re, html, pathlib
import markdown

HERE = pathlib.Path(__file__).parent

PAGES = [
    {
        "src": "privacy.md",
        "out": "index.html",
        "title": "Privacy Policy",
        "heading": "Privacy Policy",
        "description": "How the BSIDE concert-logging app collects, uses, and shares your information.",
    },
    {
        "src": "support.md",
        "out": "support/index.html",
        "title": "Support",
        "heading": "Support",
        "description": "Help, contact, and answers to common questions about the BSIDE concert-logging app.",
    },
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} — BSIDE</title>
<meta name="description" content="{description}">
<style>
  :root {{
    --bg: #faf9f7; --surface: #ffffff; --ink: #1a1a1a; --muted: #5c5c5c;
    --line: #e2e0dc; --accent: #2b4cd6; --code-bg: #f1efec;
  }}
  @media (prefers-color-scheme: dark) {{
    :root:not([data-theme="light"]) {{
      --bg: #121110; --surface: #1a1918; --ink: #ece9e4; --muted: #a09b94;
      --line: #2e2c29; --accent: #8fa4ff; --code-bg: #232120;
    }}
  }}
  :root[data-theme="dark"] {{
    --bg: #121110; --surface: #1a1918; --ink: #ece9e4; --muted: #a09b94;
    --line: #2e2c29; --accent: #8fa4ff; --code-bg: #232120;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0; background: var(--bg); color: var(--ink);
    font: 16px/1.65 -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    -webkit-text-size-adjust: 100%;
  }}
  .wrap {{ max-width: 46rem; margin: 0 auto; padding: 0 16px 6rem; }}
  header {{ padding: 3.5rem 0 2rem; border-bottom: 1px solid var(--line); margin-bottom: 2.5rem; }}
  .brand {{ font-size: .75rem; letter-spacing: .22em; text-transform: uppercase; color: var(--muted); margin: 0 0 .75rem; }}
  h1 {{ font-size: 2.1rem; line-height: 1.15; margin: 0 0 .6rem; letter-spacing: -.015em; }}
  .updated {{ color: var(--muted); font-size: .9rem; margin: 0; }}
  h2 {{ font-size: 1.3rem; margin: 2.75rem 0 .85rem; letter-spacing: -.01em; padding-top: 1.25rem; border-top: 1px solid var(--line); }}
  h2:first-of-type {{ border-top: 0; padding-top: 0; margin-top: 0; }}
  ul {{ padding-left: 1.25rem; }}
  li {{ margin: .4rem 0; }}
  a {{ color: var(--accent); text-decoration-thickness: 1px; text-underline-offset: 2px; }}
  strong {{ font-weight: 650; }}
  hr {{ border: 0; border-top: 1px solid var(--line); margin: 2rem 0; }}
  code {{ background: var(--code-bg); padding: .12em .4em; border-radius: 3px; font-size: .88em; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }}
  .table-scroll {{ overflow-x: auto; margin: 1.25rem 0; -webkit-overflow-scrolling: touch; }}
  table {{ border-collapse: collapse; width: 100%; min-width: 34rem; font-size: .93rem; }}
  th, td {{ text-align: left; padding: .7rem .8rem; border-bottom: 1px solid var(--line); vertical-align: top; }}
  th {{ font-size: .72rem; letter-spacing: .1em; text-transform: uppercase; color: var(--muted); font-weight: 600; background: var(--surface); }}
  footer {{ margin-top: 4rem; padding-top: 1.5rem; border-top: 1px solid var(--line); color: var(--muted); font-size: .875rem; }}
</style>
</head>
<body>
<div class="wrap">
  <header>
    <p class="brand">BSIDE</p>
    <h1>{heading}</h1>
{subtitle}
  </header>
  <main>
{body}
  </main>
  <footer>
    <p>BSIDE — a place to log the shows you go to. Questions: <a href="mailto:bsideworkapp@gmail.com">bsideworkapp@gmail.com</a></p>
  </footer>
</div>
</body>
</html>
"""

for spec in PAGES:
    src = (HERE / spec["src"]).read_text()

    body = markdown.markdown(src, extensions=["tables", "sane_lists"])
    body = re.sub(r"^<h1>.*?</h1>\s*", "", body, count=1, flags=re.S)
    body = re.sub(r"^<p><strong>Last updated:.*?</strong></p>\s*", "", body, count=1, flags=re.S)

    # Only the policy carries a date; everything else gets no subtitle line.
    stamp = re.search(r"\*\*Last updated: (.+?)\*\*", src)
    subtitle = (
        f'    <p class="updated">Last updated: {html.escape(stamp.group(1))}</p>'
        if stamp else ""
    )

    page = TEMPLATE.format(
        title=html.escape(spec["title"]),
        heading=html.escape(spec["heading"]),
        description=html.escape(spec["description"]),
        subtitle=subtitle,
        body=body,
    )
    page = page.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")

    out = HERE / spec["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(page)
    print(f"{spec['out']} regenerated ({len(page)} bytes)")
