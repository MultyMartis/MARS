# I-SEO Report Hub — Russian UX and HTML Demo Alignment Charter v0.1

**Status:** CHARTER / DOCS ONLY — no app-source, runtime, DB, or artifact mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-30  
**Wave:** I-SEO Report Hub — Russian UX and HTML Demo Alignment Charter 01  
**Authority:** Operator charter (docs / product-UX planning)

**Related:**
- [I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-INVENTORY-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-INVENTORY-v0.1.md)
- [I-SEO-REPORT-HUB-RUSSIAN-UX-COPY-DICTIONARY-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-COPY-DICTIONARY-v0.1.md)
- [I-SEO-REPORT-HUB-RUSSIAN-UX-MANAGER-FLOW-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-MANAGER-FLOW-v0.1.md)
- [I-SEO-REPORT-HUB-RUSSIAN-UX-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-IMPLEMENTATION-PLAN-v0.1.md)
- [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md)

---

## 1. Purpose

Подготовить alignment package: привести живой PHP+SQL MVP к понятному **русскому** интерфейсу для SEO-специалистов и менеджеров i-SEO и к ранее принятой **HTML-демке** отчётника (static demo v0.4), **без** implementation в этой волне.

---

## 2. Problem statement

| Observation | Evidence |
|-------------|----------|
| PHP+SQL мотор живой | Login, dashboard, exports, export detail, shares — 200; DB active |
| UI выглядит как технический скелет | English labels; Phase 1A footer; checksum / render engine / storage disk на primary surface |
| Не похож на HTML-демку | Demo = light INTLSEO shell + sidebar RU; Live = dark skeleton EN |
| Сложно тестировать менеджерам | Internal terms (Snapshot, Render target, Revoked rows) |
| Клиентский PDF не client-ready | `LOCAL_FIXTURE_ONLY`, local `file:///` footer paths допустимы для fixture, не для реальных отчётов |

**Вывод:** живой мотор ≠ продуктовый UX. Следующий слой — Russian UX + demo alignment **перед** production.

---

## 3. Non-goals (this wave)

- No app-source / runtime / DB / SQL / migration edits  
- No share create/revoke; no export/PDF regeneration  
- No production deploy / DNS / HTTPS / server ops  
- No source→runtime sync; no secrets printed  
- No Git push / fetch / pull / reset / clean / stash; no broad `git add`

---

## 4. Decisions (product)

| Decision | Value |
|----------|-------|
| Target language | **Русский** (primary for managers/SEO specialists) |
| Engine | **Retain** current PHP+SQL app-source / runtime |
| Visual reference | Static demo **v0.4** at `workspaces/website-factory-operations/iseo-report-hub-prototype/` |
| Technical fields | Hidden by default → «Технические детали» |
| Manager-first flow | Открыть отчёт → статус → PDF → ссылка → копировать сообщение |
| Production | **No production** until Russian UX accepted by operator |
| Production environment Decision 01 | May continue later; product UX cleanup has priority for day-to-day usability |

---

## 5. Why current UI looks like a skeleton

1. **Phase 1A scaffolding leftovers** — footer still claims «no DB · runtime not synced» while DB/runtime are active.  
2. **Developer-facing English** — nav, badges, table headers, health page all English.  
3. **Internal domain model on the surface** — snapshot keys, checksums, render engine/target, storage disk shown as primary facts.  
4. **Dark skeleton CSS** (`app.css`) — teal-on-dark utility panels; not the light INTLSEO admin shell from demo.  
5. **Feature accretion without UX pass** — handoff/share UX added in English technical phrasing; copy pack templates are RU, but chrome around them is EN.  
6. **Demo never ported** — static HTML accepted as UX reference; PHP MVP built for CRUD/export correctness first.

---

## 6. Alignment scope for future implementation

1. Russian copy dictionary across manager screens.  
2. Footer / phase-label cleanup (truthful local status, no stale skeleton claim).  
3. Dashboard + exports + export detail + shares simplification.  
4. Collapsible technical details.  
5. Client-facing Russian PDF/report template (real reports; fixtures may keep test labels).  
6. Optional visual alignment toward demo shell (sidebar / light surface) — **after** copy+flow, not instead of it.  
7. Visual QA + manual click-through with operator.

---

## 7. Success criteria (future Implementation 01)

- Manager can complete handoff flow in Russian without decoding internal terms.  
- Primary surfaces hide checksum / render / storage / snapshot keys.  
- Recommended PDF is obvious; legacy HTML/PDF demoted.  
- Footer no longer contradicts live DB/runtime.  
- Operator Visual QA PASS on Russian UX.  
- Still no production claim until production gates + UX acceptance.

---

## 8. Recommended next wave

**I-SEO Report Hub — Russian UX and Demo Alignment Implementation 01**

See [I-SEO-REPORT-HUB-RUSSIAN-UX-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-RUSSIAN-UX-IMPLEMENTATION-PLAN-v0.1.md).
