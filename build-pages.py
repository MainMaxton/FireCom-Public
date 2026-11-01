#!/usr/bin/env python3
"""Builds operating-firecom.html and incident-map-manual.html from their .md files.
Run: python3 build-pages.py   (needs the 'markdown' package)"""
import re, markdown

PAGES = {'operating-firecom': 'Operating FireCom', 'incident-map-manual': 'FireCom Incident Map Manual'}
UPDATED = '1 November 2026'

for name, title in PAGES.items():
    src = open(f'{name}.md', encoding='utf-8').read()
    # first heading and the subtitle line become the page header
    lines = src.split('\n')
    h1 = lines[0].lstrip('# ').strip()
    sub = lines[2].strip()
    body = markdown.markdown('\n'.join(lines[3:]), extensions=['sane_lists'])
    html = (
        '<!DOCTYPE html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">\n'
        f'<title>{title}</title><link rel="stylesheet" href="style.css"></head>\n<body>\n'
        '<p><a href="index.html">&larr; Back</a></p>\n'
        f'<h1>{h1}</h1>\n<p class="muted">{sub}</p>\n{body}\n\n'
        f'<footer>Last updated {UPDATED}.</footer>\n</body></html>\n'
    )
    open(f'{name}.html', 'w', encoding='utf-8').write(html)
    print('wrote', name + '.html')
