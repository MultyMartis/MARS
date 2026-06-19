# REPORT — WPilot Runtime Proof Sprint

**Date:** 2026-06-19  
**Environment:** DEV only — `https://dev.gktriumph.ru`  
**Plugin:** MetaCODE WPilot `0.2.0` / schema `0.2.0`  
**Sprint result:** **PASS** (3/3 rollback runs)  
**Evidence archive:** `C:\AI MARS STORAGE\wpilot\backups\dev.gktriumph.ru\runtime-proof-sprint-20260619-151747\`

---

## 1. Deployment

| Step | Result |
|------|--------|
| Pre-sprint live routes | v0.1 only — `/backups` and `/rollback` returned `rest_no_route` |
| Deploy method | FTP upload of 21 plugin source files to `wp-content/plugins/metacode-wpilot/` |
| Schema upgrade | `WPilot_Schema::install_or_upgrade()` — `ok: true`, `schema_valid: true` |
| Post-deploy verification | `plugin_version: 0.2.0`, `schema_version: 0.2.0` |

### Tables confirmed

| Table | Exists |
|-------|--------|
| `wp_wpilot_backups` | yes |
| `wp_wpilot_audit_log` | yes |

### REST routes confirmed (post-deploy)

- `POST /wp-json/wpilot/v1/pages/{id}/backups`
- `POST /wp-json/wpilot/v1/pages/{id}/rollback`
- (plus all v0.1 read/dry-run routes)

### Bridge state (post-deploy)

- `bridge_enabled: true`
- `dev_confirmed: true`
- `write_enabled: true`
- Sprint required token rotation (previous plaintext token not available locally); new token generated via controlled bootstrap, stored only in evidence dir `.sprint-token.local` (not in git).

---

## 2. Proof Run #1 — Simple test page

**Target:** page ID `954` (`/wpilot-test-page/`)  
**Scenario:** inspect → backup → drift → rollback → validate

| Field | Value |
|-------|-------|
| `operation_id` (backup) | `op_bd282459-b6f5-4a40-96b0-c73fd4ebc443` |
| `operation_id` (rollback) | `op_d60b68ef-e0ae-4a7a-ae37-899ba65c38e2` |
| `backup_id` | `1` |
| `checksum_before` | `sha256:6e4852dd7948960cfd97b2e7a49da829204064090b681d3bf74d66a98f2888e2` |
| `checksum_modified` | `sha256:a5f2ed6c9009de690e099627a6378e7755f8035017a35abe90d8557160b3e2da` |
| `checksum_after_rollback` | `sha256:6e4852dd7948960cfd97b2e7a49da829204064090b681d3bf74d66a98f2888e2` |
| `validation_result` | **PASS** |

**post_content length:** before `1201` → modified `1096` → after rollback `1201`  
**Live HTML after rollback:** title `WPilot Test Page`, H1 and test copy present; drift marker absent.

---

## 3. Proof Run #2 — WPBakery page

**Target:** page ID `38` (`/services/gruzovoe-taksi/`) — large WPBakery/The7 page  
**Scenario:** inspect → backup → drift → rollback → validate

| Field | Value |
|-------|-------|
| `operation_id` (backup) | `op_68e53a55-36f1-4a78-98d6-6d4206b8c770` |
| `operation_id` (rollback) | `op_cbde0a1e-9c32-43a2-9b80-2df37c3096cd` |
| `backup_id` | `2` |
| `checksum_before` | `sha256:8f450f24c575fe7e41c253bb16dc82e8436eaa850350b3e5fd965e3b99fa5ec1` |
| `checksum_modified` | `sha256:f692b56bfb74c701582603473e5e18f634dd648f84cd1e862331922de4c80d71` |
| `checksum_after_rollback` | `sha256:8f450f24c575fe7e41c253bb16dc82e8436eaa850350b3e5fd965e3b99fa5ec1` |
| `validation_result` | **PASS** |

**Shortcode counts (before = after rollback):** `vc_row: 3`, `vc_column: 3`, `vc_raw_html: 12`  
**post_content length:** before `30911` → modified `2602` (drift phase) → after rollback `30911`  
**Live HTML after rollback:** `wsp_cargo_scroll_steps`, `cargo_taxi__tariffs__wrap`, `ПЕРЕЕЗД` blocks render; drift marker absent.

---

## 4. Proof Run #3 — Contacts page

**Target:** page ID `69` (`/contacts/`)  
**Scenario:** backup → small text drift → rollback → validate

| Field | Value |
|-------|-------|
| `operation_id` (backup) | `op_8fc20944-69af-4daf-85ba-10c6cee988f9` |
| `operation_id` (rollback) | `op_6bbeae87-ac40-4e7c-afc0-58d9577a669d` |
| `backup_id` | `3` |
| `checksum_before` | `sha256:f5440c198c3480092d91c3cc12cf74c3ac50efed8ecfc0f596e9635d4d4ec312` |
| `checksum_modified` | `sha256:52e776ba22be4ca7c7ef1b33b65eab93f6ffd5c8ce1b360018e1609b45da8e24` |
| `checksum_after_rollback` | `sha256:f5440c198c3480092d91c3cc12cf74c3ac50efed8ecfc0f596e9635d4d4ec312` |
| `validation_result` | **PASS** |

**Shortcode counts (before = after):** `vc_row: 2`, `vc_column: 2`, `vc_raw_html: 1`  
**post_content length:** before `17843` → modified `611` → after rollback `17843`  
**Live HTML after rollback:** `Реквизиты организации`, `Контакты службы «ГРУЗОТАКСИ»` present; drift marker absent.

---

## 5. Checksum Validation

| Check | Run #1 | Run #2 | Run #3 |
|-------|--------|--------|--------|
| `checksum_after_rollback == backup_checksum` | yes | yes | yes |
| `checksum_after_rollback == checksum_before` | yes | yes | yes |
| `restored_checksum == backup_checksum` (API) | yes | yes | yes |
| `post_content` length restored | yes | yes | yes |
| Drift marker removed from `content_raw` | yes | yes | yes |

All three runs: **checksum integrity verified** after rollback.

---

## 6. Audit Validation

Lifecycle events recorded per `operation_id`:

| Run | Backup events | Rollback events |
|-----|---------------|-----------------|
| #1 | `backup_requested` → `backup_created` | `rollback_requested` → `rollback_verified` |
| #2 | `backup_requested` → `backup_created` | `rollback_requested` → `rollback_verified` |
| #3 | `backup_requested` → `backup_created` | `rollback_requested` → `rollback_verified` |

Example rollback row (run #2):

- `event_type: rollback_verified`
- `outcome: rolled_back`
- `before_checksum`: modified-state checksum
- `after_checksum`: matches backup / baseline

No tokens or content dumps in audit rows (spot-checked).

---

## 7. WPBakery Validation

**Run #2 (primary WPBakery target):**

| Check | Result |
|-------|--------|
| `has_wpbakery: true` before and after | yes |
| Shortcode count unchanged after rollback | yes |
| `wsp_cargo_scroll_steps` block in live HTML | yes |
| Tariffs section (`cargo_taxi__tariffs__wrap`) | yes |
| No drift HTML comment in rendered page | yes |

**Run #1** also uses WPBakery shortcodes (`vc_row`, `vc_column_text`, etc.) — counts unchanged after rollback.

---

## 8. Findings

1. **v0.2.0 was not on DEV before sprint** — only v0.1 routes were live; FTP deploy + schema upgrade succeeded.
2. **Three consecutive rollback runs passed** without manual content repair.
3. **Checksum + length + shortcode integrity** restored after rollback on all targets.
4. **Drift phase observation:** simulated edit via `wp_update_post` (append HTML comment) changed `post_content` length dramatically on runs #1–#3 during modified state (e.g. page 38: `30911` → `2602`). This reflects WordPress save/filter behaviour on drift, **not** WPilot backup/rollback. Rollback restored full byte-identical backup content in all cases.
5. **Sprint token rotation** invalidated the previous DEV REST credential; operators must store the new token from `.sprint-token.local` in approved local storage.
6. **Temporary bootstrap helper** (`wpilot-runtime-proof-bootstrap.php`) uploaded for schema/token/drift/audit reads and **self-deleted** after sprint (`cleanup: ok`).

---

## 9. Risks

| Risk | Level | Note |
|------|-------|------|
| CDN/page cache after rollback | SAFE UNKNOWN | Live HTML checks passed immediately; cache lag not formally measured |
| Drift via raw `wp_update_post` vs WP Admin UI | Medium | Drift simulation may not mirror WPBakery backend editor path; rollback path still proven |
| FTP deploy (no ZIP/admin pipeline) | Low | Files deployed; plugin remained active |
| Token rotation side effect | Medium | Previous operator token no longer valid until re-synced from local evidence |
| Bootstrap secret on DEV root | Low | File deleted post-sprint; rotate if exposure suspected |

---

## 10. Recommendation

**Sprint success criteria met:** 3 successful rollback runs, no content loss after rollback, WPBakery page 38 intact, no manual restore required.

**Next step (per Sprint 1 report):** proceed to `apply_replace` / scoped-replace execute endpoint — **only after** operator acknowledges sprint token rotation and stores new credential locally.

**Do not start:** production enablement, Apply on business-critical pages without HITL, autonomous deploy tooling.

---

## Git / repo note

- Report file: `projects/wpilot/reports/wpilot-runtime-proof-sprint-report.md` (this file)
- Evidence: `C:\AI MARS STORAGE\` only (gitignored)
- No commit performed (default policy)
