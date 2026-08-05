#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
import shutil
from html import unescape
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOT = REPO_ROOT / "netcool_pass_site" / "docs" / "categories" / "c23"
SOURCE_INDEX = SOURCE_ROOT / "index.md"
SOURCE_PART = SOURCE_ROOT / "part-01.md"
OUTPUT_ROOT = REPO_ROOT / "docs" / "netcool"

RELEASE_ID = "netcool-omnibus-v81-technical-items-20260805-r1"
SOURCE_RELEASE_ID = "netcool-c23-20260716-r1"


INDEX_TEMPLATE = """<!doctype html>
<html lang="ja" data-release="{release_id}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Netcool/OMNIbus V8.1 Technical Item Library</title>
  <link rel="stylesheet" href="assets/site.css?{release_id}">
</head>
<body>
  <header>
    <div class="mark">NETCOOL</div>
    <div>
      <strong>Netcool/OMNIbus V8.1</strong>
      <small>TECHNICAL ITEM LIBRARY / PROCEDURE-LINKED</small>
    </div>
    <label>
      <input id="search" type="search" placeholder="Search by title, category, difficulty, or source">
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
        This public route keeps the technical-item perspective. Items are grouped by Netcool functional area
        and opened with the existing Netcool technical-item body. Each page keeps the source document names.
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
    const sourceHtml = item.source?.url
      ? `<a href="${item.source.url}" target="_blank" rel="noreferrer">${esc(item.source.label || "Source")}</a>`
      : item.source?.label
        ? `<p class="sourceline">${esc(item.source.label)}</p>`
        : "";

    $("reader").innerHTML =
      `<header class="articlehead">` +
      `<p class="eyebrow">NETCOOL / TECHNICAL ITEM</p>` +
      `<h2>${esc(item.title)}</h2>` +
      `<p class="articlemeta">${esc(item.category)} / ${esc(item.difficulty)} / ${esc(item.form)}</p>` +
      sourceHtml +
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
.mark{height:52px;width:92px;background:#145d52;color:#fff;display:grid;place-items:center;font-size:16px;font-weight:700;letter-spacing:.08em}
header strong{display:block;font-size:22px}
small,.eyebrow{display:block;color:#5d7066;font-family:Consolas,monospace;font-size:11px}
header label{margin-left:auto;border:1px solid #bdbdbd;height:38px;display:flex;align-items:center;padding:0 10px;min-width:360px}
input{border:0;outline:0;font-size:14px;width:100%}
.count{text-align:right}
.count b{display:block;font-size:20px}
.layout{display:grid;grid-template-columns:290px 1fr;min-height:calc(100vh - 76px)}
aside{border-right:1px solid #ddd;padding:28px 14px;overflow:auto;max-height:calc(100vh - 76px);position:sticky;top:0}
h1{font-size:22px;margin:6px 8px 18px}
.category{background:#fff;border:0;border-left:3px solid transparent;width:100%;text-align:left;padding:10px 9px;font-size:14px;display:flex;justify-content:space-between;gap:10px;cursor:pointer}
.category:hover,.category.active{border-left-color:#145d52;background:#f4f8f7}
.note{font-size:12px;line-height:1.6;color:#555;border-top:1px solid #ddd;padding:16px 8px;margin-top:18px}
main{display:grid;grid-template-columns:380px minmax(0,1fr)}
.list{border-right:1px solid #ddd;overflow:auto;max-height:calc(100vh - 76px);position:sticky;top:0}
.listhead{padding:18px;border-bottom:1px solid #ddd;display:flex;justify-content:space-between;font-size:14px}
.item{display:block;border:0;border-bottom:1px solid #eee;background:#fff;width:100%;padding:13px 18px;text-align:left;cursor:pointer}
.item:hover,.item.current{background:#f4f8f7;border-left:3px solid #145d52;padding-left:15px}
.item strong{display:block;font-size:14px;line-height:1.4}
.item small{margin-top:4px;color:#5b6c63}
#reader{min-width:0;padding:44px 52px;overflow:auto}
.articlehead{border-bottom:2px solid #171717;padding-bottom:22px;margin-bottom:28px}
.articlehead h2{font-size:27px;margin:6px 0 10px;overflow-wrap:anywhere}
.articlemeta{color:#555}
.articlehead a,.articlehead .sourceline{display:block;margin-top:10px;color:#145d52;font-size:14px;line-height:1.6}
.empty,.loading,.list-empty{padding:60px;color:#555}
.official-dom{color:#171717}
.official-dom p,.official-dom li,.official-dom dd{line-height:1.8}
.official-dom ul,.official-dom ol{padding-left:22px}
.official-dom code{padding:1px 4px;border-radius:3px;background:#edf0f1;font-family:Consolas,'Cascadia Mono',monospace;overflow-wrap:anywhere}
.official-dom pre,.official-dom .kb-code{margin:14px 0;padding:14px;overflow:auto;white-space:pre-wrap;background:#f4f6f7;border:1px solid #cfd6d8;font:14px/1.55 Consolas,'Cascadia Mono',monospace}
.official-dom pre code{padding:0;background:transparent}
.official-dom table{width:100%;border-collapse:collapse;margin:12px 0 18px}
.official-dom th,.official-dom td{border:1px solid #ddd;padding:10px 12px;text-align:left;vertical-align:top}
.official-dom th{background:#f7f7f7}
.official-dom blockquote{margin:14px 0;padding:12px 16px;border-left:4px solid #145d52;background:#f4f8f7;color:#444}
.official-dom a{color:#145d52}
.official-dom .kb-src,.official-dom .kb-meta,.official-dom .kb-pname{color:#555}
.official-dom .kb-block{display:block;margin-top:18px;border:1px solid #d5dfdc;border-radius:6px;padding:14px 16px;background:#fbfcfc}
.official-dom .kb-block > summary{cursor:pointer;font-weight:700;color:#145d52}
@media(max-width:900px){
header{padding:0 12px}
.mark{width:66px;font-size:12px}
header label{min-width:0;width:35%}
.layout{grid-template-columns:190px 1fr}
main{grid-template-columns:1fr}
.list{display:none}
#reader{padding:28px 22px}
header strong{font-size:17px}
}
"""


SECTION_PATTERN = re.compile(r'(<section class="kb-item" id="([^"]+)">.*?</section>)', re.S)


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def strip_tags(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value).strip()


def extract(pattern: str, text: str) -> str:
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else ""


def parse_meta(meta_text: str) -> tuple[str, str]:
    category = ""
    difficulty = ""
    for part in meta_text.split("・"):
        chunk = part.strip()
        if chunk.startswith("分類:"):
            category = chunk.split(":", 1)[1].strip()
        if chunk.startswith("難易度:"):
            difficulty = chunk.split(":", 1)[1].strip()
    return category, difficulty


def build_body(section_html: str) -> str:
    inner = re.sub(r'^<section class="kb-item" id="[^"]+">', "", section_html, count=1)
    inner = re.sub(r"</section>$", "", inner, count=1)
    inner = re.sub(r"<h3>.*?</h3>", "", inner, count=1, flags=re.S)
    inner = re.sub(r'<p class="kb-meta">.*?</p>', "", inner, count=1, flags=re.S)
    inner = re.sub(r'<p class="kb-src"><strong>出典:</strong>.*?</p>', "", inner, count=1, flags=re.S)
    return "<!doctype html><html lang=\"ja\"><body><div class=\"official-dom\">{}</div></body></html>\n".format(inner.strip())


def parse_items() -> tuple[list[dict[str, object]], dict[str, int]]:
    raw = SOURCE_PART.read_text(encoding="utf-8")
    items: list[dict[str, object]] = []
    category_counts: dict[str, int] = {}

    blocks = re.split(r"^##\s+", raw, flags=re.M)
    for block in blocks[1:]:
        lines = block.splitlines()
        if not lines:
            continue
        heading = lines[0].strip()
        content = "\n".join(lines[1:])
        matches = SECTION_PATTERN.findall(content)
        if not matches:
            continue

        for section_html, raw_id in matches:
            title = strip_tags(extract(r"<h3>(.*?)</h3>", section_html))
            meta_text = strip_tags(extract(r'<p class="kb-meta">(.*?)</p>', section_html))
            source_text = strip_tags(extract(r'<p class="kb-src"><strong>出典:</strong>(.*?)</p>', section_html))
            category, difficulty = parse_meta(meta_text)
            category = category or heading
            difficulty = difficulty or "未分類"
            body_path = OUTPUT_ROOT / "articles" / f"{raw_id}.html"
            write_text(body_path, build_body(section_html))

            items.append(
                {
                    "id": raw_id,
                    "title": unescape(title),
                    "category": category,
                    "difficulty": difficulty,
                    "form": "手順",
                    "bodyPath": f"articles/{raw_id}.html",
                    "source": {"label": source_text} if source_text else None,
                    "search": " ".join(filter(None, [title, category, difficulty, source_text])),
                }
            )
            category_counts[category] = category_counts.get(category, 0) + 1

    return items, category_counts


def build() -> None:
    if not SOURCE_INDEX.exists() or not SOURCE_PART.exists():
        raise FileNotFoundError("Netcool source files were not found under netcool_pass_site/docs/categories/c23")

    if OUTPUT_ROOT.exists():
        shutil.rmtree(OUTPUT_ROOT)

    items, category_counts = parse_items()
    article_count = len(items)

    write_text(
        OUTPUT_ROOT / "index.html",
        INDEX_TEMPLATE.format(release_id=RELEASE_ID, article_count=article_count),
    )
    write_text(OUTPUT_ROOT / "assets" / "app.js", APP)
    write_text(OUTPUT_ROOT / "assets" / "site.css", CSS)
    write_text(
        OUTPUT_ROOT / "assets" / "data.js",
        "window.OSKB_ITEMS = "
        + json.dumps(items, ensure_ascii=False, separators=(",", ":"))
        + ";\nwindow.OSKB_CATEGORIES = "
        + json.dumps(category_counts, ensure_ascii=False, separators=(",", ":"))
        + ";\n",
    )

    release_manifest = {
        "release_id": RELEASE_ID,
        "source_release_id": SOURCE_RELEASE_ID,
        "article_count": article_count,
        "source_gap_count": 0,
        "assets": {
            "index.html": sha256(OUTPUT_ROOT / "index.html"),
            "assets/site.css": sha256(OUTPUT_ROOT / "assets" / "site.css"),
            "assets/app.js": sha256(OUTPUT_ROOT / "assets" / "app.js"),
            "assets/data.js": sha256(OUTPUT_ROOT / "assets" / "data.js"),
        },
    }
    write_text(
        OUTPUT_ROOT / "release-manifest.json",
        json.dumps(release_manifest, ensure_ascii=False, indent=2) + "\n",
    )


if __name__ == "__main__":
    build()
