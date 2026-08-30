# I-SEO Report Hub — Demo Visual Implementation Plan v0.1

**Status:** FUTURE IMPLEMENTATION PLAN — **do not implement in this charter wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-31  
**Recommended next wave:** **I-SEO Report Hub — Demo Visual Shell Alignment Implementation 02**

**Inputs:**
- [I-SEO-REPORT-HUB-DEMO-VISUAL-ALIGNMENT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-DEMO-VISUAL-ALIGNMENT-CHARTER-v0.1.md)
- [I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md](I-SEO-REPORT-HUB-DEMO-VISUAL-GAP-MAP-v0.1.md)
- [I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md](I-SEO-REPORT-HUB-DEMO-VISUAL-PAGE-MAPPING-v0.1.md)
- Demo v0.4: `workspaces/website-factory-operations/iseo-report-hub-prototype/`
- Prior: Russian UX Implementation 01 result

---

## 1. Principle

Keep the **PHP+SQL engine**, Russian manager copy, routes, and handoff flow.  
Change **visual shell and tokens** toward demo v0.4: light content + dark sidebar + red accent.

**Target level:** *Close visual shell alignment, not pixel-perfect.*

**No** client PDF regeneration. **No** new workflows (specialist workspace, review queue, lifecycle matrix as product features).

---

## 2. Implementation 02 scope

### In scope

| Area | Work |
|------|------|
| CSS tokens | Port demo palette into `app.css` (bg, surface, border, text, accent `#c8102e`, success/warn/danger) |
| Layout shell | `layout.php` → admin-shell structure (sidebar + main) |
| Sidebar | New partial; move primary nav from top header |
| Header / topbar | Compact page title / user meta; reduce duplicate brand block |
| Pages | Dashboard, periods list, exports, export detail, shares, health, login |
| Components | Restyle panels→cards, buttons, badges, tables, alerts |
| Footer | Keep truthful local line; place in main column footer |
| JS | Only if sidebar mobile toggle required |

### Out of scope

- DB / schema / migrations  
- Share create/revoke / token smoke that mutates state (unless operator explicitly requests controlled smoke)  
- PDF / export artifact regeneration  
- `client-report.html` template parity  
- Porting `demo.js` or demo fixture projects  
- Building specialist-workspace / review queue / full lifecycle dashboard  
- Production deploy / DNS / HTTPS  
- Pixel-perfect matching every demo section

---

## 3. Likely files (app-source)

| Zone | Paths |
|------|-------|
| Layout | `app/Views/layout.php` |
| Partials | `app/Views/partials/header.php`, `footer.php`; **new** `partials/sidebar.php` (optional `page-header.php`) |
| Pages | `pages/dashboard.php`, `login.php`, `health.php`, `reporting-periods/index.php`, `report-exports/index.php`, `report-exports/show.php`, `report-export-shares/index.php` |
| CSS | `public/assets/css/app.css` |
| JS | `public/assets/js/app.js` only if needed |

Optional lightweight reusable markup helpers (avoid overengineering):
- sidebar include  
- status badge class helpers (CSS only preferred)  
- keep existing PHP structures; restyle classes rather than rewrite business markup

**Do not edit:** demo prototype files; `.env*`; storage/export artifacts; vendor.

---

## 4. Runtime sync strategy

1. Edit **app-source** only under exact allowlist.  
2. After validation, explicit **source → runtime** sync of the same allowlist to  
   `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`  
3. **Never** sync `.env.local`, storage, exports, logs, DB, vendor.  
4. No package install.

---

## 5. Validation strategy (Impl 02)

| Gate | Check |
|------|-------|
| Preflight | X: / AI WS / branch / clean i-SEO / foreign WIP preserved |
| PHP lint | Changed PHP files |
| HTTP GET | `/health`, `/login`, `/`, exports, export detail, shares (auth as needed) |
| Visual | Screenshots vs demo shell (sidebar present; light content; red accent) |
| Functional | Manager flow still reachable; download PDF still works; tech details collapsed |
| DB | Export/share counts unchanged if no mutating smoke |
| Artifacts | Existing PDF checksum unchanged |
| Smoke tests | Update expectations if they assert old dark-theme class names |
| Restrictions | No production; no push unless operator asks |

---

## 6. Acceptance criteria (Impl 02)

1. Live `/` uses demo-like shell (dark left sidebar + light main).  
2. Exports / export detail / shares use same shell, typography, buttons, card/table style.  
3. Top horizontal nav reduced or relocated into sidebar/topbar.  
4. Content area wider and lighter; dark skeleton tokens removed from primary chrome.  
5. Russian copy retained; manager flow works.  
6. Technical details remain collapsed by default.  
7. Auth/export/share still work; no PDF regen; DB counts stable.  
8. Pixel-perfect **not** required.

---

## 7. Later targets (after Impl 02)

| Target | Proposed wave |
|--------|---------------|
| Full project lifecycle dashboard (demo `index` cards/matrix) | Product UI wave after multi-project data readiness |
| Specialist workspace | Dedicated UX + feature wave |
| Monthly editor visual | After RU + shell on CRUD pages |
| Review queue | Workflow feature wave |
| Client report template / PDF visual | **I-SEO Report Hub — Client Report Template Visual Alignment Charter 01** then regen wave |

---

## 8. Client report separation (mandatory)

**Do not** include full `client-report.html` / PDF template alignment in Implementation 02.

**Why:**
- Export artifact integrity / checksums  
- Regeneration changes stored files and client-facing output  
- Client document requires its own QA checklist  
- Admin shell alignment is independent of document chrome

**Proposed future:**  
`I-SEO Report Hub — Client Report Template Visual Alignment Charter 01`

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| CSS regressions across many pages | Shared layout/CSS tokens; Visual QA on A–D + login/health |
| Smoke tests fail on old selectors | Grep smoke for class/color assertions before merge |
| Over-porting demo IA | Stick to shell; no fake project cards |
| Accidental PDF/share mutation | Forbid regen/create in charter; GET-only smoke default |
| Mobile nav | Minimal toggle; hide sidebar ≤768 like demo |

---

## 10. Suggested implementation prompt basis (for next agent)

```
Wave: I-SEO Report Hub — Demo Visual Shell Alignment Implementation 02
Authority docs: DEMO-VISUAL-ALIGNMENT-CHARTER / GAP-MAP / PAGE-MAPPING / IMPLEMENTATION-PLAN v0.1
Target: close visual shell alignment to demo v0.4 — not pixel-perfect
Do: layout shell, CSS tokens, sidebar, restyle A–D + login + health
Do not: PDF regen, share mutation, DB/schema, demo.js port, client-report template,
        specialist/review workflows, production, push
Russian UX copy: retain
Sync: exact allowlist source → Laragon runtime after source OK
```

---

## 11. Ordering vs other tracks

| Track | Status |
|-------|--------|
| Russian UX Implementation 01 | Complete — baseline for copy/flow |
| This charter | Complete — visual plan |
| Demo Visual Shell Implementation 02 | **Recommended next product UX wave** |
| Operator click-through | Can run after Impl 02 (or parallel visual QA) |
| Production Environment Decision 01 | Parallel / deferred until UX accepted |
| Client Report Template charter | After or parallel to shell, **not** inside Impl 02 |
