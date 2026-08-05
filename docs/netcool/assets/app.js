const $ = (id) => document.getElementById(id);
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
