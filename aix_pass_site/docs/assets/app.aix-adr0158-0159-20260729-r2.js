
const KNOWLEDGE_ID = "knowledge-export";
const state = { category: "すべて", query: "", currentId: "", artifact: "format" };
const $ = (id) => document.getElementById(id);
const categories = ["すべて", ...Object.keys(window.OSKB_CATEGORIES)];
const artifacts = {
  format: {
    kind: "KNOWLEDGEMGR FORMAT STANZA",
    filename: "aix73_tech_format_definition.txt",
    text: window.OSKB_KNOWLEDGE.format,
    href: "downloads/aix73_tech_format_definition.txt"
  },
  bundle: {
    kind: "CONCATENATED KNOWLEDGE STANZAS",
    filename: "aix73_tech_knowledge_bundle.txt",
    text: window.OSKB_KNOWLEDGE.bundle,
    href: "downloads/aix73_tech_knowledge_bundle.txt"
  },
  spec: {
    kind: "STANZA SPECIFICATION",
    filename: "KNOWLEDGE_MGR_STANZA_SPEC.md",
    text: window.OSKB_KNOWLEDGE.spec,
    href: "downloads/KNOWLEDGE_MGR_STANZA_SPEC.md"
  },
  splitter: {
    kind: "VALIDATING PYTHON SPLITTER",
    filename: "split_knowledge_mgr_bundle.py",
    text: window.OSKB_KNOWLEDGE.splitter,
    href: "downloads/split_knowledge_mgr_bundle.py"
  },
  command: {
    kind: "COPY AND RUN",
    filename: "PowerShell",
    text: window.OSKB_KNOWLEDGE.command,
    href: ""
  }
};
async function copyText(value) {
  if (navigator.clipboard && window.isSecureContext) {
    await navigator.clipboard.writeText(value);
    return;
  }
  const area = document.createElement("textarea");
  area.value = value;
  area.style.position = "fixed";
  area.style.opacity = "0";
  document.body.appendChild(area);
  area.select();
  document.execCommand("copy");
  area.remove();
}
function showCopied(button, message = "全文をコピーしました。") {
  const original = button.innerHTML;
  button.innerHTML = '<i data-lucide="check"></i>';
  $("copy-status").textContent = message;
  lucide.createIcons();
  window.setTimeout(() => {
    button.innerHTML = original;
    lucide.createIcons();
  }, 1400);
}
function filtered() {
  const q = state.query.trim().toLowerCase();
  return window.OSKB_ITEMS.filter((item) =>
    (state.category === "すべて" || item.category === state.category) &&
    (!q || item.search.toLowerCase().includes(q))
  );
}
function renderCategories() {
  $("category-nav").innerHTML = categories.map((category) => {
    const count = category === "すべて" ? window.OSKB_ITEMS.length :
      window.OSKB_CATEGORIES[category];
    return `<button class="category-button ${category === state.category ? "active" : ""}"
      data-category="${category}"><span>${category}</span><span>${count}</span></button>`;
  }).join("");
  document.querySelectorAll(".category-button").forEach((button) =>
    button.addEventListener("click", () => {
      state.category = button.dataset.category;
      renderCategories();
      const matching = filtered();
      if (matching.length) openItem(matching[0].id); else renderList();
    })
  );
}
function renderList() {
  const items = filtered();
  $("result-count").textContent = items.length;
  $("list-count").textContent = items.length;
  $("list-label").textContent = state.category === "すべて" ? "すべての記事" : state.category;
  $("article-list").innerHTML = items.map((item) =>
    `<button class="list-item ${item.id === state.currentId ? "active" : ""}"
      data-id="${item.id}"><strong>${item.title}</strong><span>${item.form} / ${item.difficulty}</span></button>`
  ).join("") || '<p class="empty-list">一致する記事はありません。</p>';
  document.querySelectorAll(".list-item").forEach((button) =>
    button.addEventListener("click", () => openItem(button.dataset.id))
  );
  $("knowledge-button").classList.toggle("active", state.currentId === KNOWLEDGE_ID);
}
async function openItem(id, updateHash = true) {
  const item = window.OSKB_ITEMS.find((value) => value.id === id) || window.OSKB_ITEMS[0];
  $("knowledge-view").hidden = true;
  $("article-view").hidden = false;
  state.currentId = item.id;
  const index = window.OSKB_ITEMS.indexOf(item);
  $("article-title").textContent = item.title;
  $("article-category").textContent = item.category;
  $("article-difficulty").textContent = item.difficulty; $("article-form").textContent = item.form;
  $("article-position").textContent = `${index + 1} / ${window.OSKB_ITEMS.length}`;
  $("article-body").innerHTML = "<p class=\"article-loading\">IBM公式本文を読み込み中です。</p>";
  try {
    const response = await fetch(item.bodyPath, {cache: "no-store"});
    if (!response.ok) throw new Error(`HTTP ${response.status}`);
    const body = await response.text();
    if (state.currentId === item.id) { $("article-body").innerHTML = body; lucide.createIcons(); }
  } catch (error) {
    if (state.currentId === item.id) $("article-body").innerHTML = "<p class=\"article-error\">IBM公式本文を表示できません。IBM Docsリンクから確認してください。</p>";
  }
  $("source-link").textContent = item.source.label;
  $("source-link").href = item.source.url;
  const previous = window.OSKB_ITEMS[index - 1];
  const next = window.OSKB_ITEMS[index + 1];
  $("previous-button").disabled = !previous;
  $("next-button").disabled = !next;
  $("previous-title").textContent = previous?.title || "";
  $("next-title").textContent = next?.title || "";
  $("previous-button").onclick = () => previous && openItem(previous.id);
  $("next-button").onclick = () => next && openItem(next.id);
  document.querySelectorAll(".copy-code").forEach((button) =>
    button.addEventListener("click", async () => {
      await copyText(button.closest(".code-shell").querySelector("code").textContent);
      showCopied(button, "コマンドをコピーしました。");
    })
  );
  if (updateHash) history.replaceState(null, "", `#${item.id}`);
  document.body.classList.remove("menu-open");
  renderList(); lucide.createIcons();
  window.scrollTo({ top: 0, behavior: "smooth" });
}
function renderArtifact() {
  const artifact = artifacts[state.artifact];
  $("artifact-kind").textContent = artifact.kind;
  $("artifact-filename").textContent = artifact.filename;
  $("artifact-code").textContent = artifact.text;
  $("copy-status").textContent = "";
  $("artifact-download").hidden = !artifact.href;
  $("artifact-download").href = artifact.href || "";
  document.querySelectorAll("[data-artifact]").forEach((button) =>
    button.classList.toggle("active", button.dataset.artifact === state.artifact)
  );
}
function renderKnowledgeDefinition() {
  const definition = window.OSKB_KNOWLEDGE.definition;
  $("definition-format-id").textContent = definition.format_id;
  $("definition-format-name").textContent = definition.format_name;
  $("definition-format-path").textContent = definition.format_path;
  $("definition-knowledge-path").textContent = definition.knowledge_path;
  $("definition-encoding").textContent =
    `${definition.encoding} / ${definition.line_endings}`;
  $("definition-table-body").innerHTML = definition.fields.map((field) =>
    `<tr><td><code>${field.name}</code></td><td>${field.type}</td>` +
    `<td>${field.required ? "必須" : "任意"}</td>` +
    `<td>${field.search ? "対象" : "対象外"}</td><td>${field.purpose}</td></tr>`
  ).join("");
}
function openKnowledge(updateHash = true) {
  state.currentId = KNOWLEDGE_ID;
  $("article-view").hidden = true;
  $("knowledge-view").hidden = false;
  renderKnowledgeDefinition();
  renderArtifact();
  renderList();
  if (updateHash) history.replaceState(null, "", `#${KNOWLEDGE_ID}`);
  document.body.classList.remove("menu-open");
  lucide.createIcons();
  window.scrollTo({ top: 0, behavior: "smooth" });
}
$("search-input").addEventListener("input", (event) => {
  state.query = event.target.value; renderList();
});
$("knowledge-button").onclick = () => openKnowledge();
$("copy-artifact").onclick = async () => {
  await copyText(artifacts[state.artifact].text);
  showCopied($("copy-artifact"));
};
document.querySelectorAll("[data-artifact]").forEach((button) =>
  button.addEventListener("click", () => {
    state.artifact = button.dataset.artifact;
    renderArtifact();
  })
);
$("menu-button").onclick = () => document.body.classList.add("menu-open");
$("close-button").onclick = $("scrim").onclick =
  () => document.body.classList.remove("menu-open");
renderCategories();
if (location.hash.slice(1) === KNOWLEDGE_ID) {
  openKnowledge(false);
} else {
  openItem(location.hash.slice(1) || window.OSKB_ITEMS[0].id, false);
}
