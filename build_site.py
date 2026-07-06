#!/usr/bin/env python3
"""Generate docs/index.html (a searchable visual gallery) from README.md.

Parses the numbered list in README.md and emits a self-contained static page
styled as a clean, light directory/gallery (saaspo-style): category sidebar +
a responsive grid of cards, each with a live website screenshot thumbnail.
Run this whenever the README list changes:

    python3 build_site.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
README = ROOT / "README.md"
OUT = ROOT / "docs" / "index.html"
REPO = "Moh4696/300-free-resource-websites"
PAGES = "https://moh4696.github.io/300-free-resource-websites/"

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


HTML = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<meta name="description" content="Browse and search __COUNT__ genuinely useful free tools across __NCATS__ categories.">
<link rel="preconnect" href="https://s0.wp.com">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #f6f6f7; --panel: #ffffff; --border: #ececef; --border-strong: #e0e0e4;
    --text: #17171a; --muted: #6b6b73; --faint: #9a9aa2;
    --accent: #6366f1; --accent-soft: #eef0ff; --grey: #b45309; --grey-soft: #fef3c7;
    --shadow: 0 1px 2px rgba(20,20,30,.05), 0 8px 24px rgba(20,20,30,.06);
    --shadow-hover: 0 6px 16px rgba(20,20,30,.10), 0 18px 40px rgba(20,20,30,.12);
    --radius: 14px; --sidebar: 260px;
  }
  * { box-sizing: border-box; }
  html { scroll-behavior: smooth; }
  body {
    margin: 0; background: var(--bg); color: var(--text);
    font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    -webkit-font-smoothing: antialiased;
  }
  a { color: inherit; text-decoration: none; }

  .layout { display: grid; grid-template-columns: var(--sidebar) 1fr; min-height: 100vh; }

  /* ---- Sidebar ---- */
  aside {
    border-right: 1px solid var(--border); background: var(--panel);
    position: sticky; top: 0; height: 100vh; overflow-y: auto; padding: 22px 14px;
  }
  .brand { font-weight: 800; font-size: 1.05rem; letter-spacing: -.02em; padding: 4px 10px 2px; }
  .brand span { color: var(--accent); }
  .brand small { display: block; font-weight: 500; font-size: .74rem; color: var(--faint); margin-top: 2px; letter-spacing: 0; }
  .navlabel { font-size: .68rem; text-transform: uppercase; letter-spacing: .08em; color: var(--faint);
    padding: 18px 10px 8px; font-weight: 600; }
  .catlist { list-style: none; margin: 0; padding: 0; }
  .catlist li {
    display: flex; justify-content: space-between; align-items: center; gap: 8px;
    padding: 8px 10px; border-radius: 9px; cursor: pointer; font-size: .875rem; color: var(--muted);
    font-weight: 500; line-height: 1.25;
  }
  .catlist li:hover { background: var(--bg); color: var(--text); }
  .catlist li.active { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
  .catlist li .cnt { font-size: .72rem; color: var(--faint); background: var(--bg); border-radius: 999px;
    padding: 1px 8px; min-width: 26px; text-align: center; }
  .catlist li.active .cnt { background: #fff; color: var(--accent); }

  /* ---- Main ---- */
  main { padding: 0; }
  .topbar {
    position: sticky; top: 0; z-index: 20; background: rgba(246,246,247,.85);
    backdrop-filter: saturate(180%) blur(12px); border-bottom: 1px solid var(--border);
    padding: 18px 32px;
  }
  .searchrow { display: flex; align-items: center; gap: 14px; max-width: 1400px; margin: 0 auto; }
  .searchbox { position: relative; flex: 1; }
  .searchbox svg { position: absolute; left: 15px; top: 50%; transform: translateY(-50%); color: var(--faint); }
  #q {
    width: 100%; padding: 13px 16px 13px 44px; font-size: 1rem; border-radius: 12px;
    border: 1px solid var(--border-strong); background: var(--panel); color: var(--text);
    font-family: inherit; transition: border-color .15s, box-shadow .15s;
  }
  #q:focus { outline: none; border-color: var(--accent); box-shadow: 0 0 0 4px var(--accent-soft); }
  .count { color: var(--muted); font-size: .85rem; white-space: nowrap; }

  .content { max-width: 1400px; margin: 0 auto; padding: 26px 32px 80px; }
  .cat-head { font-size: 1.05rem; font-weight: 700; letter-spacing: -.01em; margin: 30px 2px 14px;
    display: flex; align-items: baseline; gap: 10px; }
  .cat-head:first-child { margin-top: 6px; }
  .cat-head .n { font-size: .78rem; font-weight: 500; color: var(--faint); }

  .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)); gap: 20px; }
  .card {
    background: var(--panel); border: 1px solid var(--border); border-radius: var(--radius);
    overflow: hidden; box-shadow: var(--shadow); transition: transform .18s ease, box-shadow .18s ease, border-color .18s;
    display: flex; flex-direction: column;
  }
  .card:hover { transform: translateY(-4px); box-shadow: var(--shadow-hover); border-color: var(--border-strong); }
  .thumb { position: relative; aspect-ratio: 16 / 10; background: linear-gradient(135deg,#f0f0f3,#e7e7ec); overflow: hidden; }
  .thumb img { width: 100%; height: 100%; object-fit: cover; object-position: top center; display: block;
    opacity: 0; transition: opacity .4s; }
  .thumb img.loaded { opacity: 1; }
  .thumb .fallback { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center;
    font-weight: 800; font-size: 2rem; color: #fff; letter-spacing: -.02em; }
  .flag { position: absolute; top: 10px; right: 10px; z-index: 2; font-size: .68rem; font-weight: 600;
    color: var(--grey); background: var(--grey-soft); border-radius: 6px; padding: 2px 7px; }
  .body { padding: 13px 15px 15px; display: flex; flex-direction: column; gap: 6px; flex: 1; }
  .titlerow { display: flex; align-items: center; gap: 9px; }
  .titlerow img { width: 18px; height: 18px; border-radius: 4px; flex: none; }
  .titlerow .name { font-weight: 600; font-size: .96rem; letter-spacing: -.01em; overflow: hidden;
    text-overflow: ellipsis; white-space: nowrap; }
  .card:hover .name { color: var(--accent); }
  .review { color: var(--muted); font-size: .84rem; line-height: 1.45; margin: 0;
    display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
  .cattag { margin-top: auto; padding-top: 4px; font-size: .72rem; color: var(--faint); font-weight: 500; }

  .empty { text-align: center; color: var(--muted); padding: 80px 0; grid-column: 1/-1; }
  mark { background: #fde68a; color: inherit; border-radius: 3px; padding: 0 1px; }

  /* ---- Mobile ---- */
  .menutoggle { display: none; }
  @media (max-width: 900px) {
    .layout { grid-template-columns: 1fr; }
    aside { position: static; height: auto; border-right: none; border-bottom: 1px solid var(--border); }
    .catlist { display: flex; flex-wrap: wrap; gap: 8px; }
    .catlist li { border: 1px solid var(--border-strong); border-radius: 999px; padding: 6px 12px; }
    .catlist li .cnt { display: none; }
    .navlabel { display: none; }
    .topbar { padding: 14px 18px; }
    .content { padding: 20px 18px 60px; }
    .searchrow .count { display: none; }
  }
</style>
</head>
<body>
<div class="layout">
  <aside>
    <div class="brand">__NDISPLAY__ <span>free tools</span><small>curated · every link verified</small></div>
    <div class="navlabel">Categories</div>
    <ul class="catlist" id="cats"></ul>
  </aside>
  <main>
    <div class="topbar">
      <div class="searchrow">
        <div class="searchbox">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <input id="q" type="search" placeholder="Search a tool, task or category — e.g. pdf, background remover, icons&hellip;" autocomplete="off" autofocus>
        </div>
        <span class="count" id="count"></span>
      </div>
    </div>
    <div class="content" id="results"></div>
  </main>
</div>
<script>
const DATA = __DATA__;
const q = document.getElementById('q');
const results = document.getElementById('results');
const countEl = document.getElementById('count');
const catsEl = document.getElementById('cats');
let activeCat = null;

const cats = [...new Set(DATA.map(d => d.category))];
const GRAD = ['#6366f1','#ec4899','#f59e0b','#10b981','#3b82f6','#8b5cf6','#ef4444','#14b8a6','#f97316','#0ea5e9'];
function host(url){ return url.replace(/^https?:\/\//,'').replace(/\/.*$/,''); }
function shot(url){ return 'https://image.thum.io/get/width/600/crop/420/noanimate/' + url; }
function favicon(url){ return 'https://www.google.com/s2/favicons?domain=' + encodeURIComponent(host(url)) + '&sz=64'; }
function gradFor(name){ let h=0; for(const c of name) h=(h*31+c.charCodeAt(0))>>>0; return GRAD[h%GRAD.length]; }

function esc(s){ return s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }
function highlight(text, terms){
  let out = esc(text);
  terms.filter(Boolean).forEach(t => {
    const re = new RegExp('(' + t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&') + ')', 'ig');
    out = out.replace(re, '<mark>$1</mark>');
  });
  return out;
}

function buildCats(){
  catsEl.innerHTML = '';
  const mk = (label, cat, count) => {
    const li = document.createElement('li');
    if (cat === activeCat) li.className = 'active';
    li.innerHTML = '<span>' + esc(label) + '</span><span class="cnt">' + count + '</span>';
    li.onclick = () => { activeCat = (activeCat === cat) ? null : cat; window.scrollTo({top:0,behavior:'smooth'}); render(); };
    return li;
  };
  catsEl.appendChild(mk('All tools', null, DATA.length));
  cats.forEach(c => catsEl.appendChild(mk(c, c, DATA.filter(d=>d.category===c).length)));
}

function card(d, terms){
  const el = document.createElement('a');
  el.className = 'card';
  el.href = d.url; el.target = '_blank'; el.rel = 'noopener';
  const initial = esc(d.name[0].toUpperCase());
  el.innerHTML =
    '<div class="thumb">' +
      (d.grey ? '<span class="flag">grey</span>' : '') +
      '<div class="fallback" style="background:linear-gradient(135deg,' + gradFor(d.name) + ',' + gradFor(d.category) + ')">' + initial + '</div>' +
      '<img loading="lazy" alt="" src="' + shot(d.url) + '">' +
    '</div>' +
    '<div class="body">' +
      '<div class="titlerow"><img loading="lazy" alt="" src="' + favicon(d.url) + '" onerror="this.style.display=\'none\'">' +
        '<span class="name">' + highlight(d.name, terms) + '</span></div>' +
      '<p class="review">' + highlight(d.review, terms) + '</p>' +
      '<div class="cattag">' + esc(d.category) + '</div>' +
    '</div>';
  const img = el.querySelector('.thumb img');
  img.addEventListener('load', () => { if (img.naturalWidth > 1) img.classList.add('loaded'); });
  img.addEventListener('error', () => { img.remove(); });
  return el;
}

function render(){
  const raw = q.value.trim();
  const terms = raw.toLowerCase().split(/\s+/).filter(Boolean);
  let items = DATA.filter(d => !activeCat || d.category === activeCat);
  items = items.filter(d => {
    const hay = (d.name + ' ' + d.url + ' ' + d.review + ' ' + d.category).toLowerCase();
    return terms.every(t => hay.includes(t));
  });
  buildCats();
  countEl.textContent = items.length + ' result' + (items.length===1?'':'s');
  results.innerHTML = '';
  if (!items.length){ results.innerHTML = '<p class="empty">No tools match. Try a different word.</p>'; return; }

  let currentCat = null, grid = null;
  items.forEach(d => {
    if (d.category !== currentCat){
      currentCat = d.category;
      const h = document.createElement('div');
      h.className = 'cat-head';
      const inCat = items.filter(x=>x.category===currentCat).length;
      h.innerHTML = esc(currentCat) + ' <span class="n">' + inCat + '</span>';
      results.appendChild(h);
      grid = document.createElement('div'); grid.className = 'grid'; results.appendChild(grid);
    }
    grid.appendChild(card(d, terms));
  });
}

q.addEventListener('input', render);
render();
</script>
</body>
</html>
"""


def main():
    entries = parse(README.read_text(encoding="utf-8"))
    ncats = len({e["category"] for e in entries})
    n = len(entries)
    title = f"{n} Free Resource Websites"
    html = (HTML
            .replace("__DATA__", json.dumps(entries, ensure_ascii=False))
            .replace("__TITLE__", title)
            .replace("__NDISPLAY__", str(n))
            .replace("__COUNT__", str(n))
            .replace("__NCATS__", str(ncats))
            .replace("__REPO__", REPO)
            .replace("__PAGES__", PAGES))
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    print(f"Wrote {OUT} — {n} entries, {ncats} categories.")


if __name__ == "__main__":
    main()
