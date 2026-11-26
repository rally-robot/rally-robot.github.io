#!/usr/bin/env python3
"""Build index.html from src/page.html.

src/page.html holds the page without the document skeleton (it is also published as-is for previews).
Everything above the "<!-- end head -->" marker goes into <head>. Run after editing src/page.html:
    python3 build.py
"""
from pathlib import Path

SITE = "https://rally-robot.github.io/"  # used only for the absolute link-preview image URL
TITLE = "Structuring Robotic Harnesses Through Adversarial and Collaborative Play"
DESC = ("RALLY: Alice reads a robot's code policy and proposes scenes that break it or related tasks that "
        "extend it; Bob refines the policy on each one.")

D = Path(__file__).resolve().parent
head, body = (D / "src" / "page.html").read_text().split("<!-- end head -->", 1)
meta = f"""<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta property="og:type" content="website">
<meta property="og:title" content="RALLY: {TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{SITE}static/images/teaser.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="static/images/favicon.svg" type="image/svg+xml">"""
html = (f'<!doctype html>\n<html lang="en">\n<head>\n{meta}\n{head.strip()}\n</head>\n<body>\n'
        f"{body.strip()}\n</body>\n</html>\n")
(D / "index.html").write_text(html)
print("wrote index.html", len(html), "bytes")
