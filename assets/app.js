
(() => {
  "use strict";
  const data = window.AIX_SITE_DATA;
  const byId = new Map(data.items.map((item) => [item.id, item]));
  const categories = data.categories;
  const state = { query: "", category: "すべて", filtered: data.items.slice(), selected: null };

  const el = {
    search: document.getElementById("search-input"),
    mobileSearch: document.getElementById("mobile-search-input"),
    resultCount: document.getElementById("result-count"),
    listCount: document.getElementById("list-count"),
    listLabel: document.getElementById("list-label"),
    categoryNav: document.getElementById("category-nav"),
    list: document.getElementById("article-list"),
    title: document.getElementById("article-title"),
    category: document.getElementById("article-category"),
    difficulty: document.getElementById("article-difficulty"),
    form: document.getElementById("article-form"),
    body: document.getElementById("article-body"),
    position: document.getElementById("article-position"),
    sourceLink: document.getElementById("source-link"),
    sourceLabel: document.getElementById("source-label"),
    previousButton: document.getElementById("previous-button"),
    previousTitle: document.getElementById("previous-title"),
    nextButton: document.getElementById("next-button"),
    nextTitle: document.getElementById("next-title"),
    menuButton: document.getElementById("menu-button"),
    closeButton: document.getElementById("close-button"),
    scrim: document.getElementById("scrim"),
  };

  function refreshIcons() {
    if (window.lucide) window.lucide.createIcons({ attrs: { "stroke-width": 1.8 } });
  }

  function renderCategories() {
    const entries = [["すべて", data.items.length], ...categories.map((item) => [item.name, item.count])];
    el.categoryNav.innerHTML = entries.map(([name, count]) => `
      <button class="category-button${name === state.category ? " active" : ""}"
              type="button" data-category="${escapeAttribute(name)}">
        <span>${escapeHtml(name)}</span><span>${count}</span>
      </button>`).join("");
    el.categoryNav.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => {
        state.category = button.dataset.category;
        applyFilter();
      });
    });
  }

  function applyFilter() {
    const query = state.query.trim().toLocaleLowerCase("ja");
    state.filtered = data.items.filter((item) => {
      const categoryMatch = state.category === "すべて" || item.category === state.category;
      const searchMatch = !query || item.search.toLocaleLowerCase("ja").includes(query);
      return categoryMatch && searchMatch;
    });
    el.resultCount.textContent = String(state.filtered.length);
    el.listCount.textContent = String(state.filtered.length);
    el.listLabel.textContent = state.category === "すべて" ? "すべての記事" : state.category;
    renderCategories();
    renderList();
    if (state.filtered.length && (!state.selected || !state.filtered.some((item) => item.id === state.selected.id))) {
      selectArticle(state.filtered[0].id, false);
    }
  }

  function renderList() {
    if (!state.filtered.length) {
      el.list.innerHTML = '<p class="empty-list">該当する記事はありません。</p>';
      return;
    }
    el.list.innerHTML = state.filtered.map((item) => `
      <button class="list-item${state.selected?.id === item.id ? " active" : ""}"
              type="button" data-id="${item.id}">
        <strong>${escapeHtml(item.title)}</strong>
        <span>${escapeHtml(item.category)} / ${item.form}</span>
      </button>`).join("");
    el.list.querySelectorAll("button").forEach((button) => {
      button.addEventListener("click", () => selectArticle(button.dataset.id, true));
    });
  }

  function selectArticle(id, updateHash) {
    const item = byId.get(id);
    if (!item) return;
    state.selected = item;
    const index = data.items.findIndex((candidate) => candidate.id === id);
    el.title.textContent = item.title;
    el.category.textContent = item.category;
    el.difficulty.textContent = `難易度: ${item.difficulty}`;
    el.form.textContent = item.form === "E" ? "公式実例あり" : "汎化形式";
    el.body.innerHTML = item.body;
    el.position.textContent = `${index + 1} / ${data.items.length}`;
    if (item.source.url) {
      el.sourceLink.hidden = false;
      el.sourceLink.href = item.source.url;
      el.sourceLink.textContent = item.source.label;
      el.sourceLabel.hidden = true;
    } else {
      el.sourceLink.hidden = true;
      el.sourceLabel.hidden = false;
      el.sourceLabel.textContent = item.source.label;
    }
    setPager(index);
    bindCodeCopy();
    renderList();
    refreshIcons();
    const active = el.list.querySelector(`[data-id="${id}"]`);
    if (active) active.scrollIntoView({ block: "nearest" });
    if (updateHash && location.hash !== `#${id}`) history.pushState(null, "", `#${id}`);
    if (window.innerWidth <= 780) document.body.classList.remove("menu-open");
    document.title = `${item.title} | AIX 7.3`;
    window.scrollTo({ top: 0, behavior: "auto" });
  }

  function setPager(index) {
    const previous = data.items[index - 1];
    const next = data.items[index + 1];
    el.previousButton.disabled = !previous;
    el.previousTitle.textContent = previous?.title || "";
    el.previousButton.onclick = previous ? () => selectArticle(previous.id, true) : null;
    el.nextButton.disabled = !next;
    el.nextTitle.textContent = next?.title || "";
    el.nextButton.onclick = next ? () => selectArticle(next.id, true) : null;
  }

  function bindCodeCopy() {
    el.body.querySelectorAll(".copy-code").forEach((button) => {
      button.addEventListener("click", async () => {
        const code = button.closest(".code-shell").querySelector("pre code").textContent;
        await navigator.clipboard.writeText(code);
        button.innerHTML = '<i data-lucide="check"></i>';
        button.title = "コピーしました";
        refreshIcons();
        window.setTimeout(() => {
          button.innerHTML = '<i data-lucide="copy"></i>';
          button.title = "コマンドをコピー";
          refreshIcons();
        }, 1200);
      });
    });
  }

  function syncSearch(source, target) {
    state.query = source.value;
    target.value = source.value;
    applyFilter();
  }

  function escapeHtml(value) {
    const node = document.createElement("div");
    node.textContent = value;
    return node.innerHTML;
  }
  function escapeAttribute(value) {
    return escapeHtml(value).replaceAll('"', "&quot;");
  }

  el.search.addEventListener("input", () => syncSearch(el.search, el.mobileSearch));
  el.mobileSearch.addEventListener("input", () => syncSearch(el.mobileSearch, el.search));
  el.menuButton.addEventListener("click", () => document.body.classList.add("menu-open"));
  el.closeButton.addEventListener("click", () => document.body.classList.remove("menu-open"));
  el.scrim.addEventListener("click", () => document.body.classList.remove("menu-open"));
  window.addEventListener("hashchange", () => {
    const id = location.hash.slice(1);
    if (byId.has(id)) selectArticle(id, false);
  });

  renderCategories();
  const initialId = byId.has(location.hash.slice(1)) ? location.hash.slice(1) : data.items[0].id;
  selectArticle(initialId, false);
  refreshIcons();
})();
