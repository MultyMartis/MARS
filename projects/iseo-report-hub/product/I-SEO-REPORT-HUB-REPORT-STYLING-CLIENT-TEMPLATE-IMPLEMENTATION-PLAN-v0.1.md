# I-SEO Report Hub — Report Styling / Client Template Implementation Plan v0.1

**Status:** PLANNING ONLY — not an implementation charter execution  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Styling / Client Template Charter 01  
**Parent:** [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-CHARTER-v0.1.md)  
**Design:** [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-DESIGN-v0.1.md)  
**Validation:** [I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-STYLING-CLIENT-TEMPLATE-VALIDATION-PLAN-v0.1.md)

---

## 1. Recommended next wave

**Name:** `I-SEO Report Hub — Report Styling Default Template Implementation 01`

**Goal:** Implement code-first template `iseo_default_v1` version `1` for **future** HTML (and thus PDF) generation without silently mutating historical exports id **1** / **2**.

**Preferred before:** any DB-09 template metadata migration.

---

## 2. Preflight (for that future wave)

1. Repo `X:\AI MARS`; volume `AI WS`; branch `mars/canonical-post-recovery`.
2. Guardrails session header for filesystem/git risk.
3. Confirm i-SEO WIP empty; foreign WIP preserved; use clean worktree if main index non-empty foreign-only.
4. Read-only DB: `iseo_report_hub_dev` @ `127.0.0.1`; migrations **7**; tables **15**; `report_exports` **2**.
5. Read-only artifacts: HTML/PDF checksums match baseline.
6. Confirm PDF Hardening still in tip lineage.
7. No package install; Edge path remains allowlisted.

---

## 3. Allowed source areas (future implementation)

Likely allowlist (exact list owned by implementation charter):

| Area | Intent |
|------|--------|
| `app-source/app/Services/ReportExportService.php` | Template constants; `buildHtml` / `embeddedCss`; optional template helper methods |
| Optional new small PHP helper under `app-source/app/` (e.g. `ReportTemplate.php`) | Only if keeps service thinner — not required |
| `app-source/app/Views/pages/...` preview/print | Only if sharing safe token subset; must not rewrite exports |
| `app-source/public/assets/css/app.css` | Internal UI hints only; not export SoT |
| `app-source/README.md` + product result docs | Status / next stage |

**Not allowed unless separately chartered:** migrations; DB-09; runtime `.env`; public share routes; demo workspace; registry.

---

## 4. Template constants / config

Introduce in code (names illustrative):

```text
TEMPLATE_ID = iseo_default_v1
TEMPLATE_VERSION = 1
```

Optional later (still no DB): Git JSON/YAML under `app-source/config/` for tokens — only if implementation charter prefers config over PHP constants.

Do **not** invent admin UI for templates in Implementation 01.

---

## 5. HTML artifact builder changes

1. Replace/upgrade `embeddedCss()` to `iseo_default_v1` tokens (typography, spacing, print `@page` A4, section/block rules).
2. Add template id/version to HTML head (meta/comment) and footer.
3. Keep escape + snapshot-only content rules.
4. No JS; no external URLs.
5. Preserve storage path layout under `storage/exports/reports/...`.

### No old artifact overwrite

Default policy for Implementation 01:

- **Do not** rewrite files for export id **1** / **2**.
- Idempotent HTML/PDF create continues to return existing ready rows.
- If a new styled artifact is required for smoke:
  - either use a **new** export version/key path explicitly allowed by that charter;
  - or generate into a **temporary non-registered path** for visual smoke only (preferred for pure visual check);
  - or operator-approved repair/regeneration charter.

Silent checksum change of existing ready exports = **STOP**.

---

## 6. PDF generation compatibility

- PDF remains Edge headless from HTML file:// path.
- Styled HTML must remain valid input for current `generatePdfFromHtml`.
- Re-validate: `%PDF` magic; size > 0; hardening `validateReadyArtifact`.
- Do not change engine install policy.

If Implementation 01 does not create a new PDF row, still prove print CSS via:

- temporary HTML fixture rendered by Edge offline; **or**
- operator-approved new export version.

---

## 7. UI / preview / print implications

| Surface | Guidance |
|---------|----------|
| Export list/detail | Optional display of template id when metadata exists; no fake fields in DB yet |
| Snapshot show | No forced re-export; keep Download for historical artifacts |
| Internal monthly preview | May adopt subset of tokens for visual consistency — only if safe and scoped; must not mutate finalized content |
| Browser print route | May align print CSS later; not required day-one if export path is primary |

---

## 8. Optional DB-09 later

Separate charter only if product needs durable queryable metadata:

- columns on `report_exports`: `template_id`, `template_version`, `render_engine`, `render_options_json`;
- **or** `report_templates` registry + assignment.

**Not** part of Default Template Implementation 01 unless blocked without schema (unlikely: HTML comments suffice for MVP).

---

## 9. Smoke plan (summary)

See validation plan. Minimum for Implementation 01:

1. PHP lint on changed files.
2. Baseline exports id 1/2 unchanged (checksum + mtime or hash_equals).
3. New styled HTML (temp or new version) contains `iseo_default_v1` / version `1`.
4. No `<script>`; no external asset URLs.
5. Edge PDF from styled HTML succeeds when exercised.
6. Hardening regression subset PASS.
7. No public routes; auth still required.
8. Cyrillic readable spot-check.
9. A4/@page present in CSS.

---

## 10. STOP conditions (future implementation)

STOP if:

- would overwrite existing ready HTML/PDF silently;
- requires package install;
- requires DB migration without DB-09 charter;
- introduces CDN/remote assets/JS in export;
- public share / client portal scope creeps in;
- foreign WIP would be staged;
- HEAD/branch/volume identity unsafe;
- cannot prove old artifacts unchanged.

---

## 11. Delivery shape

Typical commits (illustrative):

1. `feat(iseo-report-hub): add default report styling template` (source + docs result)
2. docs hash-record closeout as needed

Push: **no** unless operator charter says otherwise.
