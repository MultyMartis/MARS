# I-SEO Report Hub — Demo Visual Page Mapping v0.1

**Status:** MAPPING / DOCS ONLY  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-31  
**Wave:** Demo Visual Alignment Charter 01

**Demo root:** `workspaces/website-factory-operations/iseo-report-hub-prototype/`  
**Live SoT:** `projects/iseo-report-hub/app-source/`  
**Live URL base:** `http://iseo-report-hub.test/`

---

## 1. Mapping legend

| Class | Meaning |
|-------|---------|
| **NOW** | In scope for Demo Visual Shell Alignment Implementation 02 (shell/tokens/layout) |
| **LATER** | Future product/UI wave after shell alignment |
| **OUT OF SCOPE** | Not a live page target soon; keep as demo reference only |

---

## 2. Demo → live mapping table

| Demo page | Demo purpose | Live target(s) | Mapping class | Notes |
|-----------|--------------|----------------|---------------|-------|
| `index.html` | Обзор проектов / lifecycle dashboard | `/` (dashboard); secondary: `/reporting-periods` | **NOW** (shell + light dashboard restyle); lifecycle cards **LATER** | Live has manager quick actions, not multi-project cards |
| `specialist-workspace.html` | SEO working panel (blocks, checklist, stages) | Future report editor / monthly blocks panel | **LATER** | Live monthly/blocks CRUD exists but not this UX |
| `project.html` | Project + reporting cycle overview | Period detail / monthly show (partial) | **LATER** (detail IA); shell **NOW** if page already uses layout | Live period show exists; not full lifecycle matrix |
| `weekly.html` | Structured weekly checkpoint view | Weekly checkpoint CRUD pages | **LATER** | Functional CRUD exists; visual not demo-like |
| `monthly.html` | Structured monthly / type block matrix | Monthly report + blocks + preview | **LATER**; export list surfaces **NOW** for shell only | Export pages are handoff, not editor |
| `client-report.html` | Client-facing report document | Future HTML/PDF export template | **OUT OF SCOPE** for Impl 02 → separate charter | Existing PDF artifact immutable this track |
| `review.html` | Review / approval queue | Future review workflow | **LATER** / mostly **OUT OF SCOPE** for near MVP | No complete live equivalent |

---

## 3. Live pages → demo visual target (Implementation 02)

| Live page | Route | Demo visual target | Impl 02 |
|-----------|-------|--------------------|---------|
| Login | `/login` | Light surface form card (demo form-card tokens) | **NOW** — shell/tokens; keep form logic |
| Dashboard / Главная | `/` | `index.html` shell + simplified content (no fake 3-project matrix required) | **NOW** |
| Reporting periods | `/reporting-periods` | Demo card + `data-table` rhythm | **NOW** |
| Exports / Файлы отчета | `/report-snapshots/{id}/exports` | Demo card/table + primary CTA | **NOW** |
| Export detail / Файл отчета | `/report-exports/{id}` | Demo card + alert strips | **NOW** |
| Shares / Ссылки для клиента | `/report-exports/{id}/shares` | Demo card/table + badges | **NOW** |
| Health / Состояние системы | `/health` | Same shell; admin density OK | **NOW** if easy |
| Monthly / weekly / blocks / snapshot / preview / finalization | various | Demo monthly/weekly/workspace | **LATER** (English-heavy; out of shell-minimum if timeboxed) |
| Public share / PDF download artifact | artifact / share URL | `client-report.html` | **OUT OF SCOPE** (separate charter) |

---

## 4. Demo inventory (per page)

### 4.1 `index.html` — overview / projects / lifecycle

| Aspect | Detail |
|--------|--------|
| Purpose | Project overview + staged lifecycle (Final / W3 / W1) |
| Layout | `admin-shell` → sidebar + `admin-main` → `iseo-header` + `page-content` |
| Sidebar | Full product nav; brand INTLSEO; footer «Демо-данные · Без сервера · v0.4» |
| Header | Brand mark + title + prototype badge + CTA to workspace |
| Patterns | Section numbers `01`/`02`; `project-cards`; lifecycle matrix; alerts; platform note |
| Map | **NOW** shell inspiration for `/`; project/lifecycle content **LATER** |

### 4.2 `specialist-workspace.html` — SEO specialist panel

| Aspect | Detail |
|--------|--------|
| Purpose | Daily fill: project/stage select, mandatory blocks, checklists, confirmations |
| Layout | Same shell; two-column `specialist-grid` (work panel + readiness) |
| Patterns | Service cards, stage selector, form-cards, section numbers, KPI inputs |
| Map | **LATER** — no full live equivalent |

### 4.3 `project.html` — project and cycle

| Aspect | Detail |
|--------|--------|
| Purpose | Per-project cycle dashboard (KPI, lifecycle, type blocks, next action) |
| Patterns | Project tabs, badges by type, KPI grid, cards, CTA button group |
| Map | **LATER** toward period/monthly detail |

### 4.4 `weekly.html`

| Aspect | Detail |
|--------|--------|
| Purpose | Structured weekly checkpoint (read/structured editor view) |
| Patterns | Project select, week indicator, report-blocks, workspace note |
| Map | **LATER** → live weekly CRUD |

### 4.5 `monthly.html`

| Aspect | Detail |
|--------|--------|
| Purpose | Monthly structured view + type block matrix + publish gates |
| Patterns | Project tabs, badges, report-blocks, missing-block alerts |
| Map | **LATER** → live monthly/blocks/preview |

### 4.6 `client-report.html`

| Aspect | Detail |
|--------|--------|
| Purpose | Client-facing document (no admin sidebar) |
| Layout | `article.client-report` — white document, numbered sections 1–10 |
| Patterns | Meta bar, KPI grid, section titles, evidence appendix |
| Map | **OUT OF SCOPE** for Impl 02 — separate Client Report Template charter |

### 4.7 `review.html`

| Aspect | Detail |
|--------|--------|
| Purpose | Review queue table + detail/actions |
| Patterns | `data-table`, badges, cards, right-side review context |
| Map | **LATER** — workflow not complete in live |

---

## 5. Demo CSS / JS inventory

### `assets/css/styles.css` — shell primitives to port (token-level)

| Primitive | Classes / tokens | Impl 02 |
|-----------|------------------|---------|
| Tokens | `--color-bg`, `--color-surface`, `--color-accent: #c8102e`, sidebar width 240px | **NOW** |
| Shell | `.admin-shell`, `.sidebar*`, `.admin-main`, `.page-content` | **NOW** |
| Header | `.iseo-header`, `.topbar` / CTA | **NOW** (adapt) |
| Cards | `.card`, `.kpi-card`, `.form-card` | **NOW** (map to live `.panel`) |
| Badges | `.badge`, status/type variants | **NOW** |
| Buttons | `.btn`, `.btn--primary/secondary`, `.brand-cta` | **NOW** |
| Alerts | `.alert`, `.prototype-banner` (do not keep prototype banners) | **NOW** alerts only |
| Tables | `.data-table` | **NOW** |
| Section numbers | `.section-heading`, `.section-number` | Optional **NOW** / **MINOR** |
| Lifecycle | `.lifecycle-*`, `.project-card*` | **LATER** |
| Client report | `.client-report*` | Separate charter |
| Specialist | `.specialist-grid`, `.work-panel`, `.stage-btn` | **LATER** |

### `assets/js/demo.js`

| Item | Guidance |
|------|----------|
| Role | Demo fixtures, project tabs, workspace fill, client report fields |
| Reuse | **Do not** port demo.js into live |
| Live JS | `app.js` only if sidebar collapse / mobile nav needed |

---

## 6. Recommended nav mapping (live sidebar for Impl 02)

Map current top-nav items into demo-like sidebar sections:

| Sidebar section | Live links |
|-----------------|------------|
| Главное | Главная `/` |
| Отчёты | Отчетные периоды `/reporting-periods` |
| Клиент / handoff | Context links when on export/share (or quick links from dashboard only) |
| Система | Состояние системы `/health` |
| Session | User label + Выйти / Вход |

Do **not** invent live routes for «Рабочая панель SEO», «Очередь проверки», «Клиентский отчёт» in Impl 02 — those remain LATER / separate.

---

## 7. SAFE UNKNOWN

| Item | Note |
|------|------|
| Exact pixel tolerances for Visual QA | Operator must define pass bar beyond «shell resembles demo» |
| Whether period detail should be restyled in Impl 02 | Prefer yes if low-cost (same layout partials); otherwise LATER |
| Whether smoke tests assert old CSS class names | Check before Impl 02 merge |
