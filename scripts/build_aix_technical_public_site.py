#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import shutil
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "aix_pass_site" / "docs"
OUTPUT_ROOT = REPO_ROOT / "docs" / "aix"
SOURCE_DATA = SOURCE_ROOT / "assets" / "data.aix-adr0158-0159-20260729-r2.js"
SOURCE_ARTICLES = SOURCE_ROOT / "articles"
SOURCE_GAPS = SOURCE_ROOT / "source-gaps.json"
SOURCE_MANIFEST = SOURCE_ROOT / "release-manifest.json"

RELEASE_ID = "aix73-technical-items-20260802-r1"


INDEX_TEMPLATE = """<!doctype html>
<html lang="ja" data-release="{release_id}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>AIX 7.3 Technical Item Library</title>
  <link rel="stylesheet" href="assets/site.css?{release_id}">
</head>
<body>
  <header>
    <div class="mark">AIX</div>
    <div>
      <strong>AIX 7.3</strong>
      <small>TECHNICAL ITEM LIBRARY / IBM DOCS LINKED</small>
    </div>
    <label>
      <input id="search" type="search" placeholder="Search by title, category, difficulty, or keyword">
    </label>
    <div class="count">
      <b>{article_count}</b>
      <small>TECHNICAL ITEMS</small>
    </div>
  </header>

  <div class="layout">
    <aside>
      <p class="eyebrow">TECHNICAL ITEM VIEW</p>
      <h1>Category Collection</h1>
      <button class="category active" data-category="">
        All items <b>{article_count}</b>
      </button>
      <div id="categories"></div>
      <p class="note">
        This public route keeps the technical-item perspective. Items are grouped by category and opened
        with the existing AIX technical-item body. Each page keeps the IBM Docs source link. Source gaps: {source_gap_count}.
      </p>
    </aside>

    <main>
      <section class="list">
        <div class="listhead">
          <span id="listlabel">All technical items</span>
          <b id="listcount">{article_count}</b>
        </div>
        <div id="items"></div>
      </section>

      <article id="reader">
        <div class="empty">Select a technical item from the list.</div>
      </article>
    </main>
  </div>

  <script src="assets/data.js?{release_id}"></script>
  <script src="assets/app.js?{release_id}"></script>
</body>
</html>
"""


APP = r"""const $ = (id) => document.getElementById(id);
const items = window.OSKB_ITEMS || [];
const categoryCounts = window.OSKB_CATEGORIES || {};
let categoryName = "";
let query = "";
let selected = "";

function esc(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#39;",
  }[char]));
}

function filtered() {
  const q = query.trim().toLowerCase();
  return items.filter((item) => {
    if (categoryName && item.category !== categoryName) return false;
    if (!q) return true;
    const haystack = `${item.title} ${item.category} ${item.difficulty} ${item.form} ${item.search || ""}`.toLowerCase();
    return haystack.includes(q);
  });
}

function renderCategories() {
  const host = $("categories");
  const entries = Object.entries(categoryCounts).sort((left, right) => left[0].localeCompare(right[0], "ja"));
  host.innerHTML = entries.map(([name, count]) =>
    `<button class="category ${name === categoryName ? "active" : ""}" data-category="${esc(name)}">${esc(name)} <b>${count}</b></button>`
  ).join("");

  document.querySelectorAll(".category").forEach((button) => {
    button.onclick = () => {
      categoryName = button.dataset.category;
      const rows = filtered();
      selected = rows.some((item) => item.id === selected) ? selected : (rows[0]?.id || "");
      renderCategories();
      renderList();
      if (selected) {
        openItem(selected);
      } else {
        $("reader").innerHTML = '<div class="empty">No technical items matched the current filter.</div>';
      }
    };
  });
}

function renderList() {
  const rows = filtered();
  $("listlabel").textContent = categoryName || "All technical items";
  $("listcount").textContent = rows.length;
  $("items").innerHTML = rows.map((item) =>
    `<button class="item ${item.id === selected ? "current" : ""}" data-id="${item.id}">` +
    `<strong>${esc(item.title)}</strong>` +
    `<small>${esc(item.category)} / ${esc(item.difficulty)} / ${esc(item.form)}</small>` +
    `</button>`
  ).join("") || '<div class="empty list-empty">No technical items matched the current filter.</div>';

  document.querySelectorAll(".item").forEach((button) => {
    button.onclick = () => openItem(button.dataset.id);
  });
}

async function openItem(id) {
  const item = items.find((value) => value.id === id);
  if (!item) return;

  selected = item.id;
  renderCategories();
  renderList();
  $("reader").innerHTML = '<div class="loading">Loading the technical-item body...</div>';

  try {
    const response = await fetch(item.bodyPath, { cache: "no-store" });
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const text = await response.text();
    const doc = new DOMParser().parseFromString(text, "text/html");
    const body = doc.querySelector(".official-dom")?.outerHTML || doc.body.innerHTML;
    const sourceLink = item.source?.url
      ? `<a href="${item.source.url}" target="_blank" rel="noreferrer">${esc(item.source.label || "IBM Docs")}</a>`
      : "";

    $("reader").innerHTML =
      `<header class="articlehead">` +
      `<p class="eyebrow">IBM DOCS / TECHNICAL ITEM</p>` +
      `<h2>${esc(item.title)}</h2>` +
      `<p class="articlemeta">${esc(item.category)} / ${esc(item.difficulty)} / ${esc(item.form)}</p>` +
      sourceLink +
      `</header>` +
      body;

    history.replaceState(null, "", `#${item.id}`);
    $("reader").scrollTop = 0;
    window.scrollTo({ top: 0, behavior: "smooth" });
  } catch (error) {
    $("reader").innerHTML = '<div class="empty">The technical-item body could not be loaded.</div>';
  }
}

$("search").oninput = (event) => {
  query = event.target.value;
  const rows = filtered();
  selected = rows.some((item) => item.id === selected) ? selected : (rows[0]?.id || "");
  renderCategories();
  renderList();
  if (selected) {
    openItem(selected);
  } else {
    $("reader").innerHTML = '<div class="empty">No technical items matched the current filter.</div>';
  }
};

const requested = location.hash.slice(1);
if (requested) {
  const match = items.find((item) => item.id === requested);
  if (match) {
    categoryName = match.category;
    selected = match.id;
  }
}

if (!selected && items.length) {
  selected = items[0].id;
}

renderCategories();
renderList();

if (selected) {
  openItem(selected);
}
"""


CSS = """*{box-sizing:border-box}
body{margin:0;color:#171717;background:#fff;font-family:Arial,'Yu Gothic UI',sans-serif}
header{height:76px;border-bottom:1px solid #222;display:flex;align-items:center;gap:16px;padding:0 24px}
.mark{height:52px;width:78px;background:#171717;color:#fff;display:grid;place-items:center;font-size:22px;font-weight:700}
header strong{display:block;font-size:22px}
small,.eyebrow{display:block;color:#7d6557;font-family:Consolas,monospace;font-size:11px}
header label{margin-left:auto;border:1px solid #bdbdbd;height:38px;display:flex;align-items:center;padding:0 10px;min-width:360px}
input{border:0;outline:0;font-size:14px;width:100%}
.count{text-align:right}
.count b{display:block;font-size:20px}
.layout{display:grid;grid-template-columns:290px 1fr;min-height:calc(100vh - 76px)}
aside{border-right:1px solid #ddd;padding:28px 14px;overflow:auto;max-height:calc(100vh - 76px);position:sticky;top:0}
h1{font-size:22px;margin:6px 8px 18px}
.category{background:#fff;border:0;border-left:3px solid transparent;width:100%;text-align:left;padding:10px 9px;font-size:14px;display:flex;justify-content:space-between;gap:10px;cursor:pointer}
.category:hover,.category.active{border-left-color:#e04646;background:#f7f7f7}
.note{font-size:12px;line-height:1.6;color:#555;border-top:1px solid #ddd;padding:16px 8px;margin-top:18px}
main{display:grid;grid-template-columns:380px minmax(0,1fr)}
.list{border-right:1px solid #ddd;overflow:auto;max-height:calc(100vh - 76px);position:sticky;top:0}
.listhead{padding:18px;border-bottom:1px solid #ddd;display:flex;justify-content:space-between;font-size:14px}
.item{display:block;border:0;border-bottom:1px solid #eee;background:#fff;width:100%;padding:13px 18px;text-align:left;cursor:pointer}
.item:hover,.item.current{background:#f7f7f7;border-left:3px solid #e04646;padding-left:15px}
.item strong{display:block;font-size:14px;line-height:1.4}
.item small{margin-top:4px;color:#73615a}
#reader{min-width:0;padding:44px 52px;overflow:auto}
.articlehead{border-bottom:2px solid #171717;padding-bottom:22px;margin-bottom:28px}
.articlehead h2{font-size:27px;margin:6px 0 10px;overflow-wrap:anywhere}
.articlemeta{color:#555}
.articlehead a{display:inline-block;margin-top:10px;color:#075d95;font-size:14px}
.empty,.loading,.list-empty{padding:60px;color:#555}
.official-dom{color:#171717}
.official-dom section{margin:0 0 28px}
.official-dom h2{margin:0 0 12px;font-size:21px;line-height:1.35}
.official-dom h3{margin:18px 0 8px;font-size:16px}
.official-dom p,.official-dom li,.official-dom dd{line-height:1.8}
.official-dom ul,.official-dom ol{padding-left:22px}
.official-dom code{padding:1px 4px;border-radius:3px;background:#edf0f1;font-family:Consolas,'Cascadia Mono',monospace;overflow-wrap:anywhere}
.official-dom pre{margin:14px 0;padding:14px;overflow:auto;white-space:pre;background:#f4f6f7;border:1px solid #cfd6d8;font:14px/1.55 Consolas,'Cascadia Mono',monospace}
.official-dom pre code{padding:0;background:transparent}
.official-dom table{width:100%;border-collapse:collapse;margin:12px 0 18px}
.official-dom th,.official-dom td{border:1px solid #ddd;padding:10px 12px;text-align:left;vertical-align:top}
.official-dom th{background:#f7f7f7}
.official-dom blockquote{margin:14px 0;padding:12px 16px;border-left:4px solid #e04646;background:#faf7f7;color:#444}
.official-dom a{color:#075d95}
@media(max-width:900px){
header{padding:0 12px}
.mark{width:54px;font-size:16px}
header label{min-width:0;width:35%}
.layout{grid-template-columns:190px 1fr}
main{grid-template-columns:1fr}
.list{display:none}
#reader{padding:28px 22px}
header strong{font-size:17px}
}
"""


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build() -> None:
    manifest = json.loads(SOURCE_MANIFEST.read_text(encoding="utf-8"))
    article_count = int(manifest["article_count"])
    source_gap_count = int(manifest["source_gap_count"])

    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)

    shutil.copytree(SOURCE_ARTICLES, OUTPUT_ROOT / "articles")
    shutil.copy2(SOURCE_GAPS, OUTPUT_ROOT / "source-gaps.json")
    (OUTPUT_ROOT / "assets").mkdir(parents=True, exist_ok=True)
    shutil.copy2(SOURCE_DATA, OUTPUT_ROOT / "assets" / "data.js")

    write_text(
        OUTPUT_ROOT / "index.html",
        INDEX_TEMPLATE.format(
            release_id=RELEASE_ID,
            article_count=article_count,
            source_gap_count=source_gap_count,
        ),
    )
    write_text(OUTPUT_ROOT / "assets" / "app.js", APP)
    write_text(OUTPUT_ROOT / "assets" / "site.css", CSS)

    release_manifest = {
        "release_id": RELEASE_ID,
        "source_release_id": manifest["release_id"],
        "article_count": article_count,
        "source_gap_count": source_gap_count,
        "assets": {
            "index.html": sha256(OUTPUT_ROOT / "index.html"),
            "assets/site.css": sha256(OUTPUT_ROOT / "assets" / "site.css"),
            "assets/app.js": sha256(OUTPUT_ROOT / "assets" / "app.js"),
            "assets/data.js": sha256(OUTPUT_ROOT / "assets" / "data.js"),
            "source-gaps.json": sha256(OUTPUT_ROOT / "source-gaps.json"),
        },
    }
    write_text(
        OUTPUT_ROOT / "release-manifest.json",
        json.dumps(release_manifest, ensure_ascii=False, indent=2) + "\n",
    )


if __name__ == "__main__":
    build()
