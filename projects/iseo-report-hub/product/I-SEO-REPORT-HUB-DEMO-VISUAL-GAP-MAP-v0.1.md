# I-SEO Report Hub — Demo Visual Gap Map v0.1

**Status:** GAP MAP / DOCS ONLY  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-31  
**Wave:** Demo Visual Alignment Charter 01

**Baseline live:** after Russian UX Implementation 01 (`RUSSIAN UX IMPLEMENTATION PASS`)  
**Baseline demo:** static v0.4 `iseo-report-hub-prototype/`

**Severity:** `BLOCKER` · `MAJOR` · `MINOR` · `ACCEPTED_FOR_NOW`

---

## 1. Live UI inventory (post–Russian UX)

| Page | Purpose | Current layout | Demo-like | Not demo-like | Visual blockers | Must not break |
|------|---------|----------------|-----------|---------------|-----------------|----------------|
| Login `/login` | Auth | Dark page + `.panel` form | RU labels | Dark theme; no sidebar; teal btn | Theme/shell | CSRF, POST login, session |
| Dashboard `/` | Manager home | Top header + narrow `.container` + dark panels | RU copy; quick actions | No sidebar; dark; no project cards/lifecycle; role codes visible | Shell | Quick action URLs; auth gate |
| Periods `/reporting-periods` | Period list | Dark panel + table | RU headers | Dark table chrome; narrow | Shell/table | CRUD links; create gate |
| Exports `/report-snapshots/1/exports` | Файлы отчета | Primary PDF card + table + tech `<details>` | Manager-first hierarchy | Dark cards; teal accents | Shell/components | Recommended PDF; no regen |
| Export detail `/report-exports/4` | Файл отчета | Manager facts + download + handoff + tech details | RU handoff | Dark panels | Shell/components | Download; eligibility; no artifact rewrite |
| Shares `/report-exports/4/shares` | Ссылки для клиента | Create/copy/revoke + checklist | RU copy pack | Dark; not card/table rhythm of demo | Shell/components | Share crypto; no accidental create in smoke |
| Health `/health` | Ops status | Multi-panel diagnostics | Some RU chrome | Dark; dense tech OK | Shell only | Read-only health semantics |

**Live style summary:** `--bg: #0f1c24`, teal `--accent: #2bb3a3`, top `site-header` + `site-nav`, content `width: min(960px, …)`, `.panel` cards.

**Live constraints (do not break):** auth session; reporting/export/share services; existing PDF checksum; DB row counts; collapsed technical details; Russian manager copy; truthful footer.

---

## 2. Shell gaps

| ID | Gap | Severity | Recommended wave |
|----|-----|----------|------------------|
| S1 | No left sidebar; top horizontal nav only | **BLOCKER** | Implementation 02 |
| S2 | Dark central theme vs demo light shell | **BLOCKER** | Implementation 02 |
| S3 | Narrow content column (~960px) vs demo wide `page-content` | **MAJOR** | Implementation 02 |
| S4 | Missing red INTLSEO accent `#c8102e` (uses teal) | **MAJOR** | Implementation 02 |
| S5 | No sticky topbar / `iseo-header` pattern | **MAJOR** | Implementation 02 |
| S6 | Header brand is uppercase teal micro-label, not demo mark + title hierarchy | **MINOR** | Implementation 02 |
| S7 | Footer is OK (truthful RU) but not demo sidebar footer placement | **ACCEPTED_FOR_NOW** | Optional Impl 02 tweak |

---

## 3. Component gaps

| ID | Gap | Severity | Recommended wave |
|----|-----|----------|------------------|
| C1 | `.panel` dark cards ≠ demo `.card` white + border `#e5e5e7` | **MAJOR** | Implementation 02 |
| C2 | Buttons teal solid ≠ demo red primary / outline secondary | **MAJOR** | Implementation 02 |
| C3 | Badges / pills not demo status/type system | **MAJOR** | Implementation 02 |
| C4 | Tables present but not light `data-table` styling | **MAJOR** | Implementation 02 |
| C5 | Alerts / handoff warnings not demo alert strips | **MINOR** | Implementation 02 |
| C6 | No section numbering (`01`, `02`) | **MINOR** | Optional Impl 02 |
| C7 | No KPI cards on dashboard | **ACCEPTED_FOR_NOW** | LATER (needs data UX) |
| C8 | Collapsible tech details — pattern OK functionally | **ACCEPTED_FOR_NOW** | Restyle only in Impl 02 |

---

## 4. Flow / IA gaps

| ID | Gap | Severity | Recommended wave |
|----|-----|----------|------------------|
| F1 | Live dashboard = quick actions; demo = multi-project cards + lifecycle matrix | **MAJOR** (content) / **ACCEPTED_FOR_NOW** for Impl 02 | Shell NOW; matrix LATER |
| F2 | Live single fixture project vs demo three staged scenarios | **ACCEPTED_FOR_NOW** | Product/data wave |
| F3 | Handoff flow exists but visually not demo client/review path | **MINOR** for shell | Impl 02 restyle; review LATER |
| F4 | No live specialist workspace equivalent | **ACCEPTED_FOR_NOW** | LATER |
| F5 | No live review queue equivalent | **ACCEPTED_FOR_NOW** | LATER |
| F6 | Remaining English on non–A–D CRUD pages | **MINOR** for visual wave | Parallel / later RU pass |

---

## 5. Report / PDF gaps

| ID | Gap | Severity | Recommended wave |
|----|-----|----------|------------------|
| R1 | Export admin pages ≠ `client-report.html` document look | **MAJOR** (product) | **Separate** Client Report Template charter — **not** Impl 02 |
| R2 | Existing PDF artifact not regenerated / not client-report styled | **MAJOR** (product) | Separate charter + regen wave |
| R3 | Fixture markers / LOCAL_FIXTURE_ONLY in artifacts | **ACCEPTED_FOR_NOW** for local MVP | Client template wave |

---

## 6. Language / content gaps

| ID | Gap | Severity | Recommended wave |
|----|-----|----------|------------------|
| L1 | INTLSEO brand | **ACCEPTED_FOR_NOW** — keep | — |
| L2 | Demo Client / Demo SEO Project fixture names | **ACCEPTED_FOR_NOW** | Fixture refresh later |
| L3 | Role codes (`admin_owner`) still visible on dashboard | **MINOR** | Impl 02 or small UX polish |
| L4 | Technical keys hidden — good | **ACCEPTED_FOR_NOW** | Keep |

---

## 7. Severity rollup for Implementation 02

**Must address (shell blockers/majors):** S1–S5, C1–C4.

**May address lightly:** C5–C6, S6, L3, F3 (visual only).

**Explicitly exclude:** R1–R2, F4–F5 (full), F1 content matrix, demo.js fixtures.

---

## 8. Evidence notes (read-only)

| Check | Result |
|-------|--------|
| Demo CSS tokens | `--color-bg: #f7f7f8`; `--color-accent: #c8102e`; sidebar `#1e293b` |
| Live CSS tokens | `--bg: #0f1c24`; `--accent: #2bb3a3`; no sidebar rules |
| Live layout | `layout.php` → `header.php` + `<main class="container">` |
| HTTP GET | `/health` 200; `/login` 200; has `site-header`; **no** sidebar markup |
| Authenticated GET this wave | Not required for charter; prior Implementation 01 attested A–D Russian |

---

## 9. SAFE UNKNOWN

| Item | Note |
|------|------|
| Operator Visual QA screenshots vs demo side-by-side | Not captured in this docs wave |
| Whether authenticated pages still 200 without session in this session | Login page confirmed; A–D assume prior session / Impl 01 evidence |
| Exact smoke-test class assertions | Verify in Impl 02 preflight |
