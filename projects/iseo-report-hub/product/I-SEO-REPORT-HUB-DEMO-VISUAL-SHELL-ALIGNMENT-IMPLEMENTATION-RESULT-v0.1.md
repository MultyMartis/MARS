# I-SEO Report Hub — Demo Visual Shell Alignment Implementation Result v0.1

**Status:** COMPLETE — DEMO VISUAL SHELL ALIGNMENT PASS  
**project_id:** `iseo-report-hub`  
**Wave:** Demo Visual Shell Alignment Implementation 02  
**Date:** 2026-07-31  
**Target level:** Close visual shell alignment to static demo v0.4 — **not** pixel-perfect

---

## 1. What changed visually

| Area | Change |
|------|--------|
| Shell | Dark left sidebar + light main column (`app-shell` / `admin-shell`) |
| Sidebar | INTLSEO brand, `i-SEO Report Hub`, subtitle `локальная тестовая среда`; sections Главное / Отчеты / Проверка и клиент; active red left border |
| Topbar | White sticky page title + compact user/logout |
| Content | Neutral `#f5f6f8` background; wide container ~1440px; white cards |
| Accent | INTLSEO red `#c8102e` for primary buttons, active nav, section numbers |
| Components | Cards, badges, tables, buttons, alerts, section numbers restyled to demo-like tokens |
| Login | Centered clean `login-shell` card (no cluttered dark header) |
| Footer | Unchanged truthful local line in main column |

## 2. Demo primitives reused

From `workspaces/website-factory-operations/iseo-report-hub-prototype/assets/css/styles.css` (v0.4):

- Palette tokens (bg/surface/border/text/accent/success/warn/danger)
- Sidebar fixed width + dark `#1f2a3a` / `#1e293b` family
- Topbar height / sticky header rhythm
- Section number + heading pattern
- Card / KPI / badge / button / table / alert patterns

**Not reused:** `demo.js`, multi-project dashboard cards, lifecycle matrix, specialist workspace, review queue, client-report document chrome.

## 3. Pages aligned

| Page | Alignment |
|------|-----------|
| Dashboard `/` | Sections 01–03; working contour card; quick actions; collapsed module status |
| Reporting periods | Section heading + light table/card |
| Exports | PDF primary card + all-files table + collapsed tech details |
| Export detail `#4` | Status/checklist/actions in card shell |
| Shares `#4` | Readiness + form + active/revoked tables |
| Health | Status cards in shell |
| Login | Centered demo-like card |

Russian UX copy from Implementation 01 retained on manager surfaces.

## 4. Out of scope (unchanged)

- Client report / PDF HTML template visual alignment
- PDF regeneration / export artifact edits
- Share create/revoke / token mutation
- DB schema / migrations
- Specialist workspace / review queue / lifecycle matrix as features
- Pixel-perfect parity
- Production deploy

## 5. Client report / PDF

| Item | Status |
|------|--------|
| Client-report template changed | **No** |
| PDF regenerated | **No** |
| Artifact `monthly-1-v2.pdf` checksum | Unchanged `a8c4d61c…56b6b` |
| Future wave | **I-SEO Report Hub — Client Report Template Visual Alignment Charter 01** |

## 6. Validation (summary)

- PHP lint: all changed PHP files — no syntax errors
- HTTP: `/health`, `/login`, `/`, exports, export 4, shares — 200 (auth via session injection)
- Visual markers: sidebar, light shell, red accent CSS present; old teal tokens absent
- DB: exports **4**, shares **6**, active **0**, revoked **6**
- No share token created; no report/export/share row mutation
- Evidence: `X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-visual-shell-alignment-implementation-02\`

## 7. Remaining visual debt

- Non A–D CRUD pages use shell but still EN-heavy titles in places
- Not pixel-perfect vs demo screens
- No multi-project lifecycle dashboard
- Client PDF/document chrome still old template
- Mobile sidebar toggle is minimal
- Operator manual click-through still recommended

## 8. Runtime sync

Exact allowlist source → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`  
No `.env` / storage / exports / vendor / DB sync.
