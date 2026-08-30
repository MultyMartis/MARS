# REPORT — I-SEO REPORT HUB SCREENSHOT QA FIX CHARTER 01

**Date:** 2026-08-21  
**project_id:** `iseo-report-hub`  
**Wave:** Screenshot QA Fix Charter 01  
**Verdict:** `SCREENSHOT QA FIX CHARTER COMPLETE`

Docs / QA triage / safety charter only. No app-source, runtime, DB, export, share, or PDF mutation. No push.

Primary commit: `a5f43443524b692a7cf46d9cfd6dbc8dbebb56a5`  
Hash-record / tip: `c52936b54dbe889c41ea27000a37f8672caee311`

---

## 1. Verdict

`SCREENSHOT QA FIX CHARTER COMPLETE`

---

## 2. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `X:` / `AI WS` |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `1deadfeb7d04c986e1f10f0103b6c2bf4f29d2e4` |
| Clean worktree used | **Yes** — `feat/iseo-report-hub-screenshot-qa-fix-charter-01` at `X:\AI MARS STORAGE\git-sync-iseo-report-hub-screenshot-qa-fix-charter-01\repo` |
| Foreign WIP preserved | **Yes** (website-factory / wpilot / metabot / etc. untouched) |
| i-SEO WIP before start | **None** |
| Staged i-SEO | **None** |
| App-source / runtime / DB | **Unchanged** |

---

## 3. Evidence Used

| Field | Value |
|-------|-------|
| Folder | `X:\AI MARS STORAGE\incoming\iseo-report-hub\automated-screenshot-capture-01\20260821-010501` |
| Index | `SCREENSHOT-INDEX.md`, `SCREENSHOT-INDEX.json` |
| URL map | `URL-MAP-FOR-OPERATOR.md` |
| Screenshots reviewed | **16** (`01_login.png` … `16_404.png`) |

---

## 4. P0 Findings

1. **Fixture markers** (`LOCAL_FIXTURE_ONLY` etc.) visible in normal UI (periods, monthly detail, work-entry headers).
2. **Bad demo content** (`Updated body`, `Risks body`, numeric junk on report 5 preview).
3. **Empty yellow action buttons** on reporting periods — label present in HTML; CSS yellow-on-yellow hides it.
4. **Technical English 404** (`not-found.php`: Phase 1A / Dashboard).

---

## 5. P1/P2 Queue

- **P1:** monthly detail too technical; report 5 draft path; client preview content show-readiness after P0.
- **P2 / parked:** exports/shares polish; PDF/export deferred; mobile deferred; metrics model deferred.

---

## 6. P0 Fix Strategy

1. Render-layer sanitizer (no DB write).
2. Render-layer junk/empty fallbacks for client bodies.
3. CSS/view fix for readable action labels (GET only).
4. Friendly Russian 404 view only.

Detail: `product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-STRATEGY-v0.1.md`

---

## 7. Next Implementation Scope

**Wave:** `I-SEO Report Hub — Screenshot QA P0 Fix Implementation 01`

Allowed: views/helpers/CSS; optional Model A sync of changed files.  
Forbidden: DB/export/share/PDF mutation.

Validation: re-check P0 pages; no fixture markers / junk in normal view; buttons labeled; RU 404; DB/export unchanged.

---

## 8. Safety / Acceptance

Documented in `product/I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md` — no DB/export/share/PDF; export 4 frozen; no token print; Capture 01 = before baseline.

---

## 9. Docs Created

Full absolute paths:

- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-SCREENSHOT-QA-FINDINGS-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-FIX-STRATEGY-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-IMPLEMENTATION-SCOPE-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-SCREENSHOT-QA-P0-SAFETY-ACCEPTANCE-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-SCREENSHOT-QA-TRIAGE-RESULT-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\reports\REPORT-iseo-report-hub-screenshot-qa-fix-charter-01.md`
- `X:\AI MARS\projects\iseo-report-hub\OPERATIONAL-INDEX.md` (updated)

---

## 10. Restrictions Confirmed

- no app-source code edits
- no runtime edits / sync
- no DB mutation
- no share/export/PDF mutation
- no production
- no push
- no secrets/token printing

---

## 11. Commit

- primary: `a5f43443524b692a7cf46d9cfd6dbc8dbebb56a5`
- hash-record: `c52936b54dbe889c41ea27000a37f8672caee311`
- tip HEAD: `c52936b54dbe889c41ea27000a37f8672caee311`
- push: **no**

---

## 12. SAFE UNKNOWN

- Whether intentional RU badges «Локальная демо-среда» should remain on client document after P0 (distinct from `LOCAL_FIXTURE_ONLY`); strategy keeps environment honesty on manager shell; client-doc badge policy may need operator confirm during implementation.
- Exact post-impl screenshot folder name — created in Implementation 01.
- Live MySQL counts not re-probed this docs-only wave (baseline assumed from prior local work).

---

## 13. Files Changed

Same as §9 (7 paths under `projects/iseo-report-hub/`).

---

## 14. Git Actions

- Clean worktree on `feat/iseo-report-hub-screenshot-qa-fix-charter-01`
- Exact-path docs commit(s) cherry-picked onto `mars/canonical-post-recovery`
- Foreign WIP preserved on main working tree
- **No push**
