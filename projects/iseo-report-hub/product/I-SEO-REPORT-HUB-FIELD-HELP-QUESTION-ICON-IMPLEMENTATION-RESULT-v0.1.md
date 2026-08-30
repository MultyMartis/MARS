# I-SEO Report Hub — Field Help Question Icon Implementation Result v0.1

**Status:** implementation complete  
**Date:** 2026-08-21  
**Wave:** `I-SEO Report Hub — Field Help Question Icon Implementation 01`  
**Verdict:** `FIELD HELP QUESTION ICON PASS`  
**Scope:** UI/render only — no DB mutation, no demo seed, no PDF/export/share

---

## 1. Architecture

| Piece | Role |
|-------|------|
| `app/Support/FieldHelp.php` | Static Russian copy map + `get()` / `render()` / aliases |
| `app/Views/partials/field-help.php` | Reusable `?` `<details>` control + panel |
| `field_help($key)` helper | Thin wrapper in `helpers.php` |
| `public/assets/css/app.css` | `.field-help*` styles |
| `public/assets/js/app.js` | stopPropagation in labels; one-open; Esc close |

No DB table. No external packages. Client preview/print **excluded**.

---

## 2. Help copy keys implemented

### Work entry
`work_entry.category`, `catalog_item`, `title`, `description`, `status`, `period_role`, `client_visibility`, `client_summary`, `internal_note`, `evidence_note`, `sort_order`

### Report block
`report_block.block_key`, `block_type`, `title`, `summary`, `body`, `status`, `sort_order`, `data_json`, `source_metric_refs`

### Monthly / report sections
`report_section.executive_summary`, `results_summary`, `work_completed`, `key_findings`, `risks_and_blockers`, `next_month_plan`, `client_notes`, `internal_notes`, `title`, `status`

### Assembly (optional)
`assembly.future_block_text`, `assembly.apply_block`

Aliases from Copy Pack (`work_entry.category_id`, `monthly.*`, …) resolve to the same entries.

---

## 3. Screens updated

- Work entry create/edit form — 11 help icons
- Report block create/edit form — block fields + advanced JSON cautions
- Monthly report content form — title/status + all section textareas
- Monthly report detail (`show`) — compact help on content status rows
- Assembly preview — «Будущий текст блока» + apply-block help
- Client preview — **no** help icons (regression checked)

---

## 4. Runtime sync (exact)

To `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`:

- `app/Support/FieldHelp.php`
- `app/bootstrap.php`
- `app/Support/helpers.php`
- `app/Views/partials/field-help.php`
- `app/Views/pages/monthly-report-work-entries/form.php`
- `app/Views/pages/report-blocks/form.php`
- `app/Views/pages/monthly-reports/form.php`
- `app/Views/pages/monthly-reports/show.php`
- `app/Views/pages/monthly-reports/assembly-preview.php`
- `public/assets/css/app.css`
- `public/assets/js/app.js`

No `.env` / storage / export / PDF / vendor / DB / WordPress / OVERSEO sync.

---

## 5. Validation

- PHP lint: OK (changed PHP files)
- HTTP GET 200: health, login, work create/edit, monthly 1/5, assembly-preview, preview 1/5
- UI: help icons present; panel opens; form names unchanged; Save present
- Client preview: no `field-help`
- DB/export/share/PDF unchanged (export 4 size `117055`, checksum prefix `a8c4d61c6216`)

---

## 6. Evidence

`X:\AI MARS STORAGE\incoming\iseo-report-hub\field-help-question-icon-implementation-01\20260821-130037\`

Screenshots not committed to git.

---

## 7. Remaining queue

1. Demo User and Scenario Seed Charter 01  
2. Demo User and Scenario Seed Implementation 01  
3. Browser Filled Demo Report Pass 01  
4. Pre-hosting Deployment Readiness Charter 01  

---

## 8. Commit

Primary message: `feat(iseo-report-hub): add field help question icons`  
Push: **no**
