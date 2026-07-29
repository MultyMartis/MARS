# I-SEO Report Hub — Russian UX HTML Demo Inventory v0.1

**Status:** INVENTORY / READ-ONLY SEARCH — no file mutation of demos or runtime  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Wave:** Russian UX and HTML Demo Alignment Charter 01

---

## 1. Search result summary

| Result | Detail |
|--------|--------|
| **HTML demo / prototype** | **FOUND** |
| Primary candidate | `X:\AI MARS\workspaces\website-factory-operations\iseo-report-hub-prototype\` |
| Likelihood this is the operator “HTML-демка отчётника” | **High** — OPERATIONAL-INDEX documents v0.1–v0.4 reviews; v0.4 accepted as UX reference |
| Live PHP UI | Separate — `app-source` + Laragon runtime `iseo-report-hub.test` |
| STORAGE HTML product demo | **Not found** as a second full UI demo (incoming holds corpus + QA evidence) |

---

## 2. Primary HTML demo (accepted UX reference)

**Path:** `X:\AI MARS\workspaces\website-factory-operations\iseo-report-hub-prototype\`

| File | Role |
|------|------|
| `README.md` | Static demo v0.4 notes (RU); not production |
| `index.html` | Обзор проектов / dashboard |
| `specialist-workspace.html` | Рабочая панель SEO |
| `project.html` | Проект и цикл |
| `weekly.html` | Недельный чекпоинт |
| `monthly.html` | Месячный отчёт |
| `client-report.html` | Клиентский отчёт (RU sections) |
| `review.html` | Очередь проверки |
| `assets/css/styles.css` | Light INTLSEO-inspired shell (sidebar, red accent `#c8102e`) |
| `assets/js/demo.js` | Demo-only JS |

**What it is:** Self-contained static HTML/CSS/JS prototype; Russian UI chrome; project lifecycle matrix; client report structure; **no** PHP/MySQL.

**What it is not:** Live runtime; share/PDF engine; production SoT.

**Operator history (from OPERATIONAL-INDEX):** v0.1–v0.4 reviews; v0.4 accepted as raw UX reference; polishing deferred to v0.5 backlog; SEO specialist feedback deferred.

---

## 3. Other candidates

| Path | Appears to be | Demo? |
|------|---------------|-------|
| `X:\AI MARS\projects\iseo-report-hub\app-source\` | Versioned PHP source SoT | No — live app mirror |
| `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\` | Laragon runtime | No — live MVP |
| `X:\AI MARS STORAGE\incoming\iseo-report-hub\` | Corpus (Denis/Ilya/Nikita) + QA evidence folders | Not a product HTML demo |
| `projects/iseo-report-hub/product/*DEMO*` / reports `*website-factory*` / `*static-demo*` | Documentation of demo waves | Docs only |
| `product/I-SEO-REPORT-HUB-V0.5-DEMO-CORRECTIONS-BACKLOG-v0.1.md` | Backlog for demo polish | Docs only |

---

## 4. Demo vs live PHP comparison

| Dimension | Static demo v0.4 | Live PHP MVP |
|-----------|------------------|--------------|
| Language | Russian chrome (`lang="ru"`, RU nav labels) | `lang="ru"` on shell, **English** user-facing copy |
| Layout | Sidebar admin shell + light main | Top header + narrow container |
| Colors | Light `#f7f7f8` / white; accent `#c8102e`; dark sidebar | Dark `#0f1c24` / teal accent |
| Typography | Compact 14px system UI | Segoe/Arial utility |
| Manager flow | Project overview → workspace → monthly → client report | Periods → monthly → snapshot → exports → shares |
| Client report | Structured RU sections (резюме, KPI, риски, план…) | Export template English-leaning + block keys/meta |
| Shares / PDF handoff | Conceptual / gate in demo | Implemented (EN chrome; RU copy pack templates exist) |
| Footer | «Демо-данные · Без сервера · v0.4» | Stale Phase 1A skeleton claim |

### Reusable from demo (future implementation)

| Asset / pattern | Reuse guidance |
|-----------------|----------------|
| Russian navigation labels & section naming | Copy dictionary + IA |
| Sidebar / shell information architecture | Optional visual alignment phase |
| Client report section titles / hierarchy | PDF/client template target (adapt to charter section list) |
| Light surface + brand accent | Visual token inspiration (do not blindly copy demo demo-data) |
| CSS components wholesale | Possible reference; prefer porting tokens/patterns into `app.css`, not embedding demo JS |

### Not reusable as-is

- Demo JS / static project fixtures  
- Fake lifecycle percentages / staged demo projects  
- Absence of export/share/checksum backend concepts (must exist, but hidden)

---

## 5. Current live UI inventory

Inspected read-only under `projects/iseo-report-hub/app-source/app/Views/` (+ `public/assets/css/app.css`).

| Page | Current language | Purpose | Target Russian name | Intended user | Visible (manager) | Technical / hide |
|------|------------------|---------|---------------------|---------------|-------------------|------------------|
| Login | EN | Auth | Вход | SEO manager / admin | Email, пароль, Войти | Auth-implementation notes |
| Dashboard | EN | Status cards + quick links | Главная | SEO manager | Вход выполнен, быстрые кнопки | Role dumps; CRUD status cards as-is → simplify |
| Reporting periods | EN | Period list/CRUD | Отчетные периоды | SEO manager | Список периодов, статус | Internal IDs unless needed |
| Monthly report | EN | Monthly content | Месячный отчет / Отчет за {месяц} | SEO manager | Клиент, проект, период, статус, блоки | Machine block keys |
| Snapshot show | EN | Snapshot metadata | Снимок отчета | Admin / advanced | Link to files | Snapshot key, checksums |
| Snapshot exports | EN | Export list/create | Файлы отчета | SEO manager | Рекомендуемый PDF | Wide technical table; legacy rows |
| Export detail | EN | Artifact + handoff | Файл отчета | SEO manager | Статус, Скачать PDF, готовность | Render engine/target, checksums, storage disk |
| Shares | EN chrome / RU copy templates | Create link + copy pack | Ссылки для клиента | SEO manager | Создать ссылку, copy buttons | Token hash, revoked dump as primary |
| Health | EN | Ops diagnostics | Состояние системы | Admin / developer | Overall OK (optional) | Extensions, migration internals |
| Preview/print | Mixed | Internal preview | Предпросмотр | SEO manager / reviewer | Content blocks | Template internals |
| PDF/HTML export template | EN-leaning + fixture markers | Client artifact | SEO-отчет за {месяц} | Client (via PDF) | Russian sections | `LOCAL_FIXTURE_ONLY`, file paths, block keys |

### Why it feels technical (term dump)

Dashboard, Reporting periods, Report exports, Snapshot, Export detail, Shareable, Render target, Render engine, Source HTML, Checksum, Storage disk, Revoked rows, Public share links, Client handoff readiness, Internal only, PDF/HTML artifact, `iseo_default_v1`, Phase 1A skeleton footer.

---

## 6. SAFE UNKNOWN

| Item | Note |
|------|------|
| Exact operator mental model of “the” demo | High confidence = v0.4 prototype; if operator meant a different Figma/PDF mock, **SAFE UNKNOWN** until pointed |
| Whether STORAGE evidence HTML dumps include a separate UI prototype | Not identified as a second product demo in this wave |
| Pixel-perfect parity requirement vs “inspired by” | Operator must choose in Implementation 01 / Visual QA |
| Live HTTP screenshot capture this wave | Optional; inventory based on source + prior operator screenshots / feedback |
