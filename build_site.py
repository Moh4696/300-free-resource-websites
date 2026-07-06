#!/usr/bin/env python3
"""Generate docs/index.html (a searchable page) from README.md.

Parses the numbered list in README.md and emits a self-contained static page
with a live search/filter box. Run this whenever the README list changes:

    python3 build_site.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"
OUT = ROOT / "docs" / "index.html"

CATEGORY_RE = re.compile(r"^## (.+?)\s*$")
ENTRY_RE = re.compile(r"^(\d+)\.\s+\*\*\[([^\]]+)\]\(([^)]+)\)\*\*\s+—\s+(.*)$")


def parse(readme_text):
    entries = []
    category = None
    for line in readme_text.splitlines():
        cat = CATEGORY_RE.match(line)
        if cat:
            category = cat.group(1).strip()
            continue
        m = ENTRY_RE.match(line.strip())
        if m and category:
            num, name, url, review = m.groups()
            grey = "⚠️" in review or "grey" in review.lower()
            entries.append({
                "n": int(num),
                "name": name,
                "url": url,
                "review": review.strip(),
                "category": category,
                "grey": grey,
            })
    return entries


HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="Search __COUNT__ genuinely useful free tools across __NCATS__ categories.">
<style>
  :root {
    --bg: #0d1117; --card: #161b22; --border: #30363d; --text: #e6edf3;
    --muted: #8b949e; --accent: #58a6ff; --grey: #d29922;
  }
  * { box-sizing: border-box; }
  body {
    margin: 0; background: var(--bg); color: var(--text);
    font: 16px/1.55 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }
  header { padding: 32px 20px 12px; max-width: 960px; margin: 0 auto; }
  h1 { margin: 0 0 6px; font-size: 1.7rem; }
  .sub { color: var(--muted); margin: 0 0 20px; }
  .searchwrap { position: sticky; top: 0; z-index: 10; background: var(--bg);
    padding: 12px 20px; max-width: 960px; margin: 0 auto; }
  #q {
    width: 100%; padding: 14px 16px; font-size: 1.05rem; border-radius: 10px;
    border: 1px solid var(--border); background: var(--card); color: var(--text);
  }
  #q:focus { outline: none; border-color: var(--accent); }
  .chips { display: flex; flex-wrap: wrap; gap: 8px; margin: 12px 0 4px; }
  .chip {
    font-size: .82rem; padding: 5px 11px; border-radius: 999px; cursor: pointer;
    border: 1px solid var(--border); background: var(--card); color: var(--muted);
    white-space: nowrap;
  }
  .chip.active { background: var(--accent); color: #0d1117; border-color: var(--accent); font-weight: 600; }
  .count { color: var(--muted); font-size: .85rem; margin: 8px 20px; max-width: 960px;
    margin-left: auto; margin-right: auto; }
  main { max-width: 960px; margin: 0 auto; padding: 0 20px 60px; }
  .cat-head { font-size: .8rem; text-transform: uppercase; letter-spacing: .06em;
    color: var(--muted); margin: 26px 0 10px; border-bottom: 1px solid var(--border); padding-bottom: 6px; }
  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 12px; }
  .card { background: var(--card); border: 1px solid var(--border); border-radius: 10px;
    padding: 14px 16px; transition: border-color .15s; }
  .card:hover { border-color: var(--accent); }
  .card a { color: var(--accent); font-weight: 600; text-decoration: none; font-size: 1.02rem; }
  .card a:hover { text-decoration: underline; }
  .card p { margin: 6px 0 0; color: var(--muted); font-size: .9rem; }
  .flag { display: inline-block; font-size: .7rem; color: var(--grey); border: 1px solid var(--grey);
    border-radius: 5px; padding: 0 5px; margin-left: 6px; vertical-align: middle; }
  .empty { color: var(--muted); text-align: center; padding: 50px 0; }
  footer { max-width: 960px; margin: 0 auto; padding: 20px; color: var(--muted); font-size: .82rem; }
  footer a { color: var(--accent); }
  mark { background: #bb800955; color: inherit; border-radius: 3px; }
</style>
</head>
<body>
<header>
  <h1>__TITLE__</h1>
  <p class="sub">__COUNT__ genuinely useful free tools across __NCATS__ categories. Freemium and legally grey sites are flagged.</p>
</header>
<div class="searchwrap">
  <input id="q" type="search" placeholder="Search a tool, task or category — e.g. &quot;pdf&quot;, &quot;background remover&quot;, &quot;icons&quot;&hellip;" autofocus autocomplete="off">
  <div class="chips" id="chips"></div>
</div>
<div class="count" id="count"></div>
<main id="results"></main>
<footer>
  Generated from <a href="https://github.com/__REPO__/blob/master/README.md">README.md</a> &middot;
  <a href="https://github.com/__REPO__">source repository</a>. Type to filter instantly.
</footer>
<script>
const DATA = __DATA__;
const q = document.getElementById('q');
const results = document.getElementById('results');
const countEl = document.getElementById('count');
const chipsEl = document.getElementById('chips');
let activeCat = null;

const cats = [...new Set(DATA.map(d => d.category))];
function makeChip(label, cat) {
  const c = document.createElement('span');
  c.className = 'chip' + (cat === activeCat ? ' active' : '');
  c.textContent = label;
  c.onclick = () => { activeCat = (activeCat === cat) ? null : cat; render(); };
  return c;
}
function buildChips() {
  chipsEl.innerHTML = '';
  chipsEl.appendChild(makeChip('All', null));
  cats.forEach(cat => chipsEl.appendChild(makeChip(cat, cat)));
}

function esc(s){ return s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function highlight(text, terms){
  let out = esc(text);
  terms.filter(Boolean).forEach(t => {
    const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\\]\\\\]/g,'\\\\$&') + ')', 'ig');
    out = out.replace(re, '<mark>$1</mark>');
  });
  return out;
}

function render() {
  const raw = q.value.trim().toLowerCase();
  const terms = raw.split(/\\s+/).filter(Boolean);
  let items = DATA.filter(d => !activeCat || d.category === activeCat);
  items = items.filter(d => {
    const hay = (d.name + ' ' + d.url + ' ' + d.review + ' ' + d.category).toLowerCase();
    return terms.every(t => hay.includes(t));
  });
  buildChips();
  countEl.textContent = items.length + ' result' + (items.length === 1 ? '' : 's') +
    (activeCat ? ' in ' + activeCat : '') + (raw ? ' for "' + q.value.trim() + '"' : '');
  results.innerHTML = '';
  if (!items.length) { results.innerHTML = '<p class="empty">No tools match. Try a different word.</p>'; return; }
  let currentCat = null;
  items.forEach(d => {
    if (d.category !== currentCat) {
      currentCat = d.category;
      const h = document.createElement('div');
      h.className = 'cat-head';
      h.textContent = currentCat;
      results.appendChild(h);
      const grid = document.createElement('div');
      grid.className = 'grid';
      grid.dataset.cat = currentCat;
      results.appendChild(grid);
    }
    const grid = results.querySelector('.grid[data-cat="' + cssEscape(currentCat) + '"]');
    const card = document.createElement('div');
    card.className = 'card';
    const host = d.url.replace(/^https?:\\/\\//,'').replace(/\\/$/,'');
    card.innerHTML = '<a href="' + esc(d.url) + '" target="_blank" rel="noopener">' +
      highlight(d.name, terms) + '</a>' + (d.grey ? '<span class="flag">grey</span>' : '') +
      '<p>' + highlight(d.review, terms) + '</p>';
    grid.appendChild(card);
  });
}
function cssEscape(s){ return s.replace(/"/g,'\\\\"'); }

q.addEventListener('input', render);
render();
</script>
</body>
</html>
"""


def main():
    entries = parse(README.read_text(encoding="utf-8"))
    ncats = len({e["category"] for e in entries})
    title = f"{len(entries)} Free Resource Websites"
    html = (HTML
            .replace("__DATA__", json.dumps(entries, ensure_ascii=False))
            .replace("__TITLE__", title)
            .replace("__COUNT__", str(len(entries)))
            .replace("__NCATS__", str(ncats))
            .replace("__REPO__", "Moh4696/300-free-resource-websites"))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} — {len(entries)} entries, {ncats} categories.")


if __name__ == "__main__":
    main()
