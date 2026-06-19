# REPORT — WPilot UX-01

**Sprint:** Admin UI Alignment + Localization  
**Scope:** Admin UI only — no runtime, REST, schema, auth, or deploy changes  
**Date:** 2026-06-19  
**Plugin target:** `metacode-wpilot` v0.3.0 (state freeze checkpoint `8c67478`)

---

## 1. Changed files

| File | Action |
|------|--------|
| `projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-page.php` | Modified — new panels, text alignment, i18n for admin messages |
| `projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-ui-model.php` | **Created** — display-only UI data model |
| `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-constants.php` | Modified — UI constants (maturity, milestone, endpoint counts) |
| `projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-plugin.php` | Modified — `load_plugin_textdomain()` |
| `projects/wpilot/plugin/metacode-wpilot/metacode-wpilot.php` | Modified — `Domain Path`, require UI model |
| `projects/wpilot/plugin/metacode-wpilot/languages/metacode-wpilot.pot` | **Created** — translation template |
| `projects/wpilot/plugin/metacode-wpilot/languages/metacode-wpilot-ru_RU.po` | **Created** — Russian catalog |
| `projects/wpilot/reports/wpilot-ux-01-report.md` | **Created** — this report |

**Not changed (per hard constraints):** REST controller, backup/rollback/scoped-replace services, schema, auth, audit, checksums, route registration.

---

## 2. Replaced texts

| Location | Old (v0.1/v0.2 drift) | New (v0.3.0 aligned) |
|----------|------------------------|----------------------|
| Warning notice body | «read endpoints and dry-run… does not implement content mutation, rollback execution…» | «WPilot v0.3.0 provides a proven DEV runtime with… scoped content mutation, backup, validation, rollback, and audit trail» |
| Write enabled (Current State) | `enabled for dry-run readiness only` | `enabled (dry-run analysis and proven write endpoints)` |
| Bridge checkbox | `Enable authenticated read-only bridge` | `Enable authenticated REST bridge` |
| Write checkbox | `Enable dry-run write readiness. This does not enable content mutation endpoints.` | `Enable write readiness for dry-run analysis and proven content mutation endpoints.` |
| Section title | `Read-only Endpoints` | `REST Endpoints` (with Read / Analysis / Proven Write subsections) |
| Section title | `Dry-run Endpoint` | `Analysis Endpoint` + `Proven Write Endpoints` |
| Dry-run description | «without mutating content, creating backups, writing audit logs, or executing rollback» | «Pre-apply dry-run… without mutating content. Proven write endpoints create backups, audit records, and support rollback.» |
| Admin POST messages | Hardcoded English strings | Wrapped in `__()` with textdomain `metacode-wpilot` |
| State table labels | Hardcoded `enabled` / `disabled` / `confirmed` etc. | Localized via `WPilot_Admin_UI_Model` helpers |

**Removed outdated claims:** read-only-only bridge, dry-run-only write path, no content mutation, no rollback execution (from admin UI copy).

**Not used in new copy:** production ready, autonomous, AI admin, fully automated.

---

## 3. Added UI blocks

| Block | Position | Data source |
|-------|----------|-------------|
| **Runtime Status** | Top (after warning notice) | `WPilot_Constants::VERSION`, `SCHEMA_VERSION`, `RUNTIME_STATUS`, `ENVIRONMENT`, `RUNTIME_MATURITY` |
| **Proven Operations** | Below Runtime Status | Static list from state freeze / proven capabilities register |
| **Runtime Surface** | Below Proven Operations | `READ_ENDPOINT_COUNT` (8), `WRITE_ENDPOINT_COUNT` (4), `REST_NAMESPACE` |
| **Safety Features** | Below Runtime Surface | Static informational checklist |
| **Milestone 001** | Below Safety Features | `MILESTONE_001_*` constants + translatable title |
| **REST Endpoints** (expanded) | Bottom (replaces old read-only + dry-run sections) | `WPilot_Admin_UI_Model::endpoint_inventory()` — 8 read + 1 analysis + 3 proven write |

### Runtime Status example (from constants)

```
Version: 0.3.0
Schema Version: 0.2.0
Status: ACTIVE
Environment: DEV
Runtime Maturity: proven_content_writes
```

### Proven Operations (informational)

✓ Inspect · ✓ Backup · ✓ Apply Content Change · ✓ Validate · ✓ Rollback · ✓ Audit Trail · ✓ Checksum Validation

### Safety Features (informational)

✓ Backup Before Apply · ✓ Checksum Validation · ✓ Audit Trail · ✓ Rollback Available · ✓ Human Approval Required

---

## 4. Translated strings (ru_RU)

Russian translations provided in `languages/metacode-wpilot-ru_RU.po` for **all 78 admin UI msgids**, including:

- Page title and warning notices
- All five new panel headings and table labels
- Bridge / token / emergency control copy
- REST endpoint section headings and descriptions
- Proven operations and safety feature labels (operation names kept in English where they match proven capability IDs)
- Admin action feedback messages
- Current State status labels

**Language selection:** WordPress locale (`ru_RU` → Russian, `en_US` → English source strings). No custom language switcher.

---

## 5. Strings prepared for i18n

All user-visible admin strings use WordPress i18n:

- `__()` — return translated string
- `esc_html__()` — escape + translate for output
- `esc_html_e()` — not required where `esc_html( __() )` pattern used
- Textdomain: `metacode-wpilot` (`WPilot_Constants::TEXT_DOMAIN`)
- Bootstrap: `load_plugin_textdomain()` in `WPilot_Plugin::init()`
- `Domain Path: /languages` in plugin header

**No custom `if ($lang === 'ru')` logic.**

Constants displayed as code values (`ACTIVE`, `proven_content_writes`, endpoint counts) are **not** translated — they are machine/status identifiers from state freeze docs.

---

## 6. Screenshot section list (UI order, top → bottom)

For operator visual verification after deploy to DEV:

1. **Page header** — `MetaCODE WPilot` (H1)
2. **Warning notice** (yellow) — DEV/test prohibition + v0.3.0 capability summary
3. **Runtime Status** — 5-row table (Version, Schema, Status, Environment, Runtime Maturity)
4. **Proven Operations** — 7-item checklist with ✓
5. **Runtime Surface** — Read/Write counts + Namespace + footnote
6. **Safety Features** — 5-item checklist with ✓
7. **Milestone 001** — Title, Date, Status, Milestone ID table
8. **Admin notices** (conditional) — bridge save, token, emergency messages
9. **Token success notice** (conditional) — one-time plaintext display
10. **Current State** — operational flags table (updated labels)
11. **Production prohibition** — inline warning
12. **Bridge Control** — 3 checkboxes + save (updated labels)
13. **Token Control** — generate/revoke buttons
14. **Emergency Control** — emergency disable / clear
15. **REST Endpoints** — Read (8 routes) · Analysis (1) · Proven Write (3)

Path: **Settings → MetaCODE WPilot**

---

## 7. Git status

```
 M projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-page.php
 M projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-constants.php
 M projects/wpilot/plugin/metacode-wpilot/includes/class-wpilot-plugin.php
 M projects/wpilot/plugin/metacode-wpilot/metacode-wpilot.php
?? projects/wpilot/plugin/metacode-wpilot/admin/class-wpilot-admin-ui-model.php
?? projects/wpilot/plugin/metacode-wpilot/languages/
?? projects/wpilot/reports/wpilot-ux-01-report.md
```

No commit performed (default policy).

---

## 8. SAFE UNKNOWN

| Item | Status |
|------|--------|
| **`.mo` binary for `ru_RU`** | `msgfmt` not available in current environment. `.po` is present; WordPress loads `.mo` at runtime. Operator must compile `metacode-wpilot-ru_RU.mo` before Russian translations appear on DEV (e.g. `msgfmt -o metacode-wpilot-ru_RU.mo metacode-wpilot-ru_RU.po` or WP-CLI `i18n make-mo`). |
| **Live admin screenshot** | Not captured in this sprint — UI exists in source only until FTP/deploy. |
| **`Environment: DEV` on non-DEV WordPress** | Constant reflects proven deployment target from state freeze, not auto-detection of `WP_ENV` or site URL. Operator may install plugin on any host; label is informational. |
| **`Status: ACTIVE`** | UI constant — not derived from bridge enabled/disabled state. Operational gating remains in existing settings/emergency flags. |

---

## 9. SECURITY RISK

| Risk | Assessment |
|------|------------|
| **New attack surface** | None — display-only UI; no new endpoints, no auth changes. |
| **Token plaintext notice** | Unchanged behavior — one-time display after generation (existing pattern). |
| **Information disclosure** | Admin page still documents REST routes and DEV warnings — same class of disclosure as before, now includes proven write routes (accurate, not expanded beyond registered inventory). |
| **i18n files** | `.po`/`.pot` contain no secrets. |

**Deploy note:** Not performed automatically per task instructions. Upload changed plugin files + compile `.mo` to activate Russian UI on `ru_RU` sites.

---

## Summary

WPilot admin UI now reflects **v0.3.0 proven runtime** (inspect, backup, apply, validate, rollback, audit, checksum) with five new informational panels, expanded REST inventory, WordPress-standard i18n foundation, and Russian translation catalog. Runtime, REST contracts, and database schema were not modified.
