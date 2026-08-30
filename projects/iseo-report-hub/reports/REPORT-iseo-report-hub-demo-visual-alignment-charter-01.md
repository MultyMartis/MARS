# REPORT — I-SEO REPORT HUB DEMO VISUAL ALIGNMENT CHARTER 01

**Wave:** docs / visual specification — Demo Visual Alignment Charter 01  
**Date:** 2026-07-31  
**project_id:** `iseo-report-hub`

---

## 1. Verdict

`DEMO VISUAL ALIGNMENT CHARTER COMPLETE`

---

## 2. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive / volume | `X:` / **AI WS** |
| Branch (main worktree) | `mars/canonical-post-recovery` |
| HEAD before | `2145935c879534b3585c0fb5d5600ed6c6118316` (later than charter expected `4ab1be35…`; expected is ancestor — OK) |
| Clean worktree used | **Yes** — `X:\AI MARS STORAGE\git-sync-iseo-report-hub-demo-visual-alignment-charter-01\repo` (branch `feat/iseo-report-hub-demo-visual-alignment-charter-01`) |
| i-SEO WIP clean before | **Yes** |
| Foreign WIP / staged | **Preserved** — main index has foreign `client-ops-reporting-bridge` staged paths; not touched |
| App-source / runtime / DB / demo HTML | **No changes** |
| Optional HTTP | GET `/health` 200; GET `/login` 200 (RU «Вход»; `site-header`; no sidebar) |

---

## 3. Operator Feedback Captured

- Russian UX base accepted as normal for local MVP.
- Live interface still visually unlike demo v0.4.
- Full visual pull onto demo v0.4 had **not** been tasked before.
- Goal now: local live PHP UI → demo visual direction without breaking the working engine.
- Laragon local context confirmed.

---

## 4. Demo Inventory

| Item | Detail |
|------|--------|
| Path | `X:\AI MARS\workspaces\website-factory-operations\iseo-report-hub-prototype\` |
| Pages | `index.html`, `specialist-workspace.html`, `project.html`, `weekly.html`, `monthly.html`, `client-report.html`, `review.html` |
| Assets | `assets/css/styles.css`, `assets/js/demo.js` |
| Shell primitives | Dark left sidebar; light main; red `#c8102e`; section numbers; cards/KPI/badges/buttons/alerts; lifecycle matrix; client-report document body; specialist work panel |

Full page inventory: [I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md](../product/I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md)

---

## 5. Live UI Inventory

| Item | Detail |
|------|--------|
| Pages | login, dashboard `/`, reporting periods, exports, export detail, shares, health |
| Style | Dark `#0f1c24`, teal accent, top `site-header` nav, narrow `.container` (~960px), `.panel` cards |
| Demo-like | Russian A–D copy; manager quick actions; collapsed tech details; truthful footer |
| Not demo-like | No sidebar; dark theme; narrow column; teal not red; no project/lifecycle dashboard chrome |
| Constraints | Auth/export/share engine; no PDF regen; fixture data; DB counts |

---

## 6. Page Mapping

| Demo | Live | Class |
|------|------|-------|
| `index.html` | `/` (+ periods list secondary) | NOW shell; lifecycle content LATER |
| `specialist-workspace.html` | Future editor/workspace | LATER |
| `project.html` | Period/monthly detail (partial) | LATER |
| `weekly.html` / `monthly.html` | Weekly/monthly CRUD (+ exports shell NOW) | LATER / shell NOW on export surfaces |
| `client-report.html` | Future PDF/HTML template | OUT OF SCOPE for Impl 02 |
| `review.html` | Future review queue | LATER |

---

## 7. Visual Gap Map

| Category | Key gaps | Severity |
|----------|----------|----------|
| Shell | No sidebar; top nav; dark theme; narrow width; missing red accent | BLOCKER / MAJOR |
| Components | Cards, buttons, badges, tables not demo-like | MAJOR |
| Flow | Simple dashboard vs project/lifecycle demo | ACCEPTED_FOR_NOW for Impl 02 content |
| Report | Admin export ≠ client-report; PDF not regen | Separate charter |
| Language | Fixture/brand OK; role codes minor | ACCEPTED / MINOR |

Detail: [I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md](../product/I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md)

---

## 8. Target Standard

| Level | Meaning |
|-------|---------|
| **Implementation 02** | Close visual shell alignment — light shell + dark sidebar + red accent; keep routes/data/RU/manager flow; no new workflows; no PDF regen |
| **Later** | Lifecycle dashboard, specialist workspace, monthly editor visual, review queue, client report template/PDF |
| Pixel-perfect | **Not required** unless operator later mandates |

Acceptance for Impl 02: sidebar present; A–D + related pages share shell; top nav reduced; content wider/lighter; dark skeleton removed; RU retained; flows work; tech details collapsed; DB stable.

---

## 9. Implementation Strategy

**Next wave:** `I-SEO Report Hub — Demo Visual Shell Alignment Implementation 02`

**Likely files:** `layout.php`, `header.php`, `footer.php`, new `sidebar.php`, dashboard/periods/exports/shares/health/login views, `app.css`, optional `app.js`.

**Runtime sync:** exact allowlist source → Laragon after source OK; no `.env`/storage/exports/DB.

**Validation:** PHP lint; GET smoke; visual screenshots; checksum/DB unchanged; smoke-test class assertions checked.

Plan: [I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md](../product/I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md)

---

## 10. Client Report Separation

Full `client-report.html` / PDF template alignment is **excluded** from Implementation 02.

**Proposed future:** `I-SEO Report Hub — Client Report Template Visual Alignment Charter 01`

**Why:** artifact integrity, checksum changes on regen, separate client-facing QA.

---

## 11. Docs Created

- `product/I-SEO-REPORT-HUB-DEMO-VISUAL-ALIGNMENT-CHARTER-v0.1.md`
- `product/I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md`
- `product/I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md`
- `product/I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md`
- `reports/REPORT-iseo-report-hub-demo-visual-alignment-charter-01.md`
- `OPERATIONAL-INDEX.md` (updated)

---

## 12. Restrictions Confirmed

- No code / runtime / DB / share / PDF / `.env` edits  
- No demo prototype edits  
- No production / DNS / HTTPS / package install  
- No push; no broad git add; foreign WIP preserved  
- No secrets printed  

---

## 13. Commit

| Item | Value |
|------|-------|
| Primary | `1f329571df24780107ee4d9d85c718f35329c499` |
| Hash-record | `40c460a59cec7fd0bea3e6d79bcf64fb12e575b2` |
| Tip HEAD (feat branch / after canonical FF) | `6b5debc2dd75be1dcaed2eed2fa02510e0375e08` |
| Push | **no** |

---

## 14. SAFE UNKNOWN

- Operator side-by-side Visual QA screenshots not captured this wave.
- Exact pixel tolerance for “close shell alignment” — operator judgment at Impl 02 Visual QA.
- Whether existing automated smoke asserts old dark-theme class names — verify in Impl 02.
- Authenticated A–D GET in this session not re-run (prior Impl 01 + login/health GET sufficient for charter).

---

## 15. Recommended Next Action

`I-SEO Report Hub — Demo Visual Shell Alignment Implementation 02`

---

## 16. Files Changed

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEMO-VISUAL-ALIGNMENT-CHARTER-v0.1.md` (created)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md` (created)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md` (created)
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEMO-VISUAL-IMPLEMENTATION-PLAN-v0.1.md` (created)
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-demo-visual-alignment-charter-01.md` (created)
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md` (updated)

---

## 17. Git Actions

- Clean temp worktree used for docs write + exact-path commit.
- Main worktree index not disturbed.
- No push.
- Commit message primary: `docs(iseo-report-hub): add demo visual alignment charter`
- Optional hash-record: `docs(iseo-report-hub): record demo visual alignment charter commit hash`
