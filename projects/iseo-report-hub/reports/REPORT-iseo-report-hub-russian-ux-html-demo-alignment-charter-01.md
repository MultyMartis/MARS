# REPORT — I-SEO REPORT HUB RUSSIAN UX AND HTML DEMO ALIGNMENT CHARTER 01

**Wave:** docs / product-UX planning only  
**Date:** 2026-07-30  
**project_id:** `iseo-report-hub`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive / volume | `X:` / **AI WS** |
| Branch (main worktree) | `mars/canonical-post-recovery` |
| HEAD before | `7f9fd29fa037939a7f6f13bdb02cb18801bc7fbd` |
| Git state | Foreign WIP present (client-ops staged/unstaged); **i-SEO scope clean** before start |
| Clean worktree used | **Yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-hub-russian-ux-html-demo-alignment-charter-01\repo` (branch `docs/iseo-report-hub-russian-ux-html-demo-alignment-charter-01`) |
| i-SEO WIP clean | **Yes** (preflight) |
| Foreign WIP preserved | **Yes** — main index not disturbed |

Note: Charter text mentioned tip `929cda7b…`; live HEAD before this wave was newer (`7f9fd29f…`, includes subsequent client-ops commit on canonical).

---

## 2. Operator Feedback Captured

- Current UI works (login, dashboard, exports, export detail, shares).  
- MVP is live, but interface is too technical and English-heavy.  
- Expected alignment with earlier HTML demo of the report hub.  
- Russian UX required before production for Russian-speaking SEO specialists and managers.  
- Footer still claims Phase 1A skeleton / no DB though runtime+DB are active.  
- PDF fixture markers (`LOCAL_FIXTURE_ONLY`, local paths) acceptable for test, not client-ready.

---

## 3. HTML Demo Search Result

| Result | **FOUND** |
|--------|-----------|
| Primary path | `X:\AI MARS\workspaces\website-factory-operations\iseo-report-hub-prototype\` |
| Version | Static demo **v0.4** (INTLSEO-inspired; Russian chrome; sidebar shell) |
| Pages | `index.html`, `specialist-workspace.html`, `project.html`, `weekly.html`, `monthly.html`, `client-report.html`, `review.html` + `assets/css/styles.css`, `assets/js/demo.js` |
| Likelihood | **High** — documented in OPERATIONAL-INDEX as accepted UX reference |
| Other | Runtime `X:\MARS-Localhost\sites\php\projects\iseo-report-hub` = live PHP (not demo); STORAGE `incoming\iseo-report-hub` = corpus/QA evidence (not second UI demo) |
| SAFE UNKNOWN | If operator meant a different unpublished Figma/PDF mock beyond v0.4 — not identified this wave |

---

## 4. Current UI Inventory

Pages inventoried (app-source views): Login, Dashboard, Reporting periods, Monthly report, Snapshot, Exports, Export detail, Shares, Health, Preview/print, export HTML/PDF template path.

**Issues:** English primary chrome; technical terms on surface (Snapshot, Render engine/target, Checksum, Storage disk, Revoked rows, Client handoff readiness, etc.); dark skeleton CSS vs demo light shell; stale footer; manager flow buried under domain-model steps.

---

## 5. Russian UX Decision

- Target language: **Russian**.  
- Technical details: **hidden by default**.  
- Manager-first flow: Главная → периоды → отчет → файлы → PDF → ссылка → копировать сообщение → отправить вручную.  
- Current PHP+SQL engine: **retained**.  
- Visual demo alignment: reuse IA/labels/client-report structure; optional CSS shell later.

---

## 6. PDF / Report Decision

- Client title target: `SEO-отчет за июль 2026` (pattern).  
- Sections: Краткий вывод; Что сделали; Результаты; Что изменилось; Проблемы и риски; План на следующий месяц; Комментарий специалиста.  
- Remove from **real** client PDF: `LOCAL_FIXTURE_ONLY`, `file:///` footers, snapshot keys, checksums, block machine keys, render/template internals.  
- Fixtures may keep obvious test labels.

---

## 7. Docs Created

| Path |
|------|
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-ALIGNMENT-CHARTER-v0.1.md` |
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-RUSSIAN-UX-HTML-DEMO-INVENTORY-v0.1.md` |
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-RUSSIAN-UX-COPY-DICTIONARY-v0.1.md` |
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-RUSSIAN-UX-MANAGER-FLOW-v0.1.md` |
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-RUSSIAN-UX-IMPLEMENTATION-PLAN-v0.1.md` |
| `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-russian-ux-html-demo-alignment-charter-01.md` |
| `projects/iseo-report-hub/OPERATIONAL-INDEX.md` (updated) |

---

## 8. Recommended Next Path

**I-SEO Report Hub — Russian UX and Demo Alignment Implementation 01**

---

## 9. Restrictions Confirmed

- no code edits; no runtime edits; no DB mutation; no share token creation; no export/report mutation; no PDF regeneration; no production; no Git push/fetch/pull/reset/clean/stash; no broad git add.

---

## 10. Commit

| Field | Value |
|-------|-------|
| Message 1 | `docs(iseo-report-hub): add russian ux demo alignment charter` |
| Hash 1 | `38b829cb4428f9655d5bed84419567abe8609f2c` |
| Message 2 (hash record) | `docs(iseo-report-hub): record russian ux demo alignment charter commit hash` |
| Hash 2 | `a97accd953b53dac0faa4a9ebaec1232f5643b3e` |
| Push | **None** |

---

## 11. SAFE UNKNOWN

- Whether operator’s mental “HTML demo” is exclusively v0.4 or includes another unpublished artifact.  
- Pixel-perfect vs inspired-by visual parity requirement for Implementation 01.  
- Exact footer replacement string (Implementation TBD; must be truthful, non-production-claiming).  
- Whether smoke suite asserts English strings that will need updates in Implementation 01.

---

## 12. Files Changed

Same allowlist as §7 (docs only).

---

## 13. Git Actions

- Clean temp worktree created for selective docs commit.  
- Exact-path stage + commit(s) on docs branch; fast-forward into `mars/canonical-post-recovery` without disturbing foreign WIP.  
- **No push.**
