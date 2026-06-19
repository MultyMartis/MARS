# REPORT — WPilot Runtime Prototype Sprint 1

**Date:** 2026-06-19  
**Scope:** Backup → Rollback recovery path on DEV (`target_type=page`, field `post_content` only).  
**Sprint adjustment:** Schema → Backup → **Rollback** (no `apply_replace` in this sprint).  
**Plugin version:** `0.2.0` / schema `0.2.0`

---

## 1. Files Changed

### Created

| File | Purpose |
|------|---------|
| `plugin/metacode-wpilot/includes/class-wpilot-checksum.php` | Shared `sha256:` checksum + UTF-8 normalization |
| `plugin/metacode-wpilot/includes/class-wpilot-operation-id.php` | `op_<uuid>` generator |
| `plugin/metacode-wpilot/includes/class-wpilot-schema.php` | dbDelta migration for plugin tables |
| `plugin/metacode-wpilot/includes/class-wpilot-audit-service.php` | `wpilot_audit_log` writer |
| `plugin/metacode-wpilot/includes/class-wpilot-backup-service.php` | Backup CRUD service |
| `plugin/metacode-wpilot/includes/class-wpilot-rollback-service.php` | Rollback validate + execute |
| `reports/wpilot-runtime-prototype-sprint-1-report.md` | This report |

### Modified

| File | Change |
|------|--------|
| `plugin/metacode-wpilot/metacode-wpilot.php` | v0.2.0, require new classes |
| `plugin/metacode-wpilot/includes/class-wpilot-constants.php` | Version/schema bump |
| `plugin/metacode-wpilot/includes/class-wpilot-settings.php` | Schema install on activation |
| `plugin/metacode-wpilot/includes/class-wpilot-plugin.php` | Schema upgrade on init |
| `plugin/metacode-wpilot/includes/class-wpilot-response.php` | `operation_id` in envelope |
| `plugin/metacode-wpilot/includes/class-wpilot-auth.php` | `require_backup_access`, `require_rollback_access` |
| `plugin/metacode-wpilot/includes/class-wpilot-rest-controller.php` | Backup + rollback endpoints |

---

## 2. Database Changes

Migration via `WPilot_Schema::install_or_upgrade()` (dbDelta), triggered on activation and `plugins_loaded` upgrade check.

### `{prefix}wpilot_backups`

| Column | Notes |
|--------|-------|
| `id` | PK → `backup_id` in API |
| `operation_id` | `op_<uuid>` of backup run |
| `changeset_ref` | Optional MARS changeset |
| `target_type` | MVP: `page` |
| `target_id` | WP page ID |
| `post_type`, `post_status` | Restore metadata |
| `content_before` | LONGTEXT — raw `post_content` snapshot |
| `content_checksum` | `sha256:<hex>` |
| `created_by_user_id`, `created_at` | Audit |
| `source` | Always `plugin` |
| `rollback_used_at` | Set after successful rollback |

### `{prefix}wpilot_audit_log`

Lifecycle events per `operation_id`: `backup_requested`, `backup_created`, `backup_refused`, `rollback_requested`, `rollback_verified`, `rollback_refused`, `rollback_failed`.

### Upgrade path

- Fresh install: tables created on activation.
- Upgrade from v0.1.0: `WPilot_Schema::maybe_upgrade()` on init when `schema_version < 0.2.0` or tables missing.
- Failure: `wpilot_schema_valid=0`, `last_safety_error=INVALID_CONFIG`, write/recovery routes refuse with `INVALID_CONFIG`.

---

## 3. New Services

### `WPilot_Backup_Service`

| Method | Description |
|--------|-------------|
| `create_backup( $page_id, $operation_id, $context )` | Snapshot `post_content` → DB row |
| `get_backup( $backup_id )` | Fetch full backup row |
| `list_backups_for_target( $target_type, $target_id, $limit )` | Newest-first list (content omitted) |
| `mark_backup_used( $backup_id, $rollback_operation_id )` | Sets `rollback_used_at` |

### `WPilot_Rollback_Service`

| Method | Description |
|--------|-------------|
| `validate_rollback( $page_id, $backup_id, $expected_current_checksum )` | Pre-flight without mutation |
| `rollback_backup( $page_id, $backup_id, $operation_id, $context )` | Restore via `wp_update_post`, verify checksum |

### Supporting

- `WPilot_Audit_Service::log_event()`
- `WPilot_Checksum::hash()` / `verify()` / `normalize_content()`
- `WPilot_Operation_Id::generate()` → `op_<uuid>`

---

## 4. New Endpoints

### `POST /wp-json/wpilot/v1/pages/{id}/backups`

**Auth:** token + bridge + DEV confirmed + valid schema  
**Body (optional):** `{ "reason", "approval_ref", "changeset_ref" }`

**Success:**

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "backup_id": 1,
    "target_id": 69,
    "content_checksum": "sha256:...",
    "operation_id": "op_..."
  }
}
```

### `POST /wp-json/wpilot/v1/pages/{id}/rollback`

**Auth:** backup auth + `write_enabled`  
**Body (required):** `backup_id`, `approval_ref`  
**Body (optional):** `expected_current_checksum`

**Success:**

```json
{
  "ok": true,
  "operation_id": "op_...",
  "data": {
    "target_id": 69,
    "backup_id": 1,
    "restored_checksum": "sha256:...",
    "mutation_performed": true,
    "operation_id": "op_..."
  }
}
```

**Not implemented this sprint:** `POST /pages/{id}/scoped-replace` execute.

---

## 5. Audit Integration

Every `create_backup` and `rollback_backup` REST call:

1. Generates `operation_id` at request start.
2. Logs pre-action event (`backup_requested` / `rollback_requested`).
3. On success: `backup_created` / `rollback_verified` with checksums + `backup_id`.
4. On refusal/failure: `backup_refused` / `rollback_refused` / `rollback_failed` with `reason_code`.

`operation_id` appears in:

- Response envelope (top-level)
- `wpilot_backups.operation_id`
- All related `wpilot_audit_log` rows

No tokens, content dumps, or stack traces in audit rows.

---

## 6. Backup Flow

```
REST POST /pages/{id}/backups
  → require_backup_access (bridge, DEV, token, schema)
  → operation_id = op_<uuid>
  → audit: backup_requested
  → get_post(page) → normalize UTF-8 content
  → checksum = sha256(content)
  → INSERT wpilot_backups
  → re-read + verify stored checksum
  → audit: backup_created
  → JSON response with backup_id + content_checksum
```

---

## 7. Rollback Flow

```
REST POST /pages/{id}/rollback
  → require_rollback_access (+ write_enabled)
  → operation_id = op_<uuid>
  → audit: rollback_requested
  → validate_rollback:
      backup exists, source=plugin, target match,
      not already used, backup checksum OK,
      optional expected_current_checksum match
  → wp_update_post(ID, post_content=wp_slash(backup content))
  → re-read post → verify restored_checksum == backup checksum
  → mark_backup_used(rollback_used_at)
  → audit: rollback_verified (outcome=rolled_back)
  → JSON response
```

Write path uses **WordPress APIs only** (`wp_update_post`), not direct SQL on `wp_posts`.

---

## 8. DEV Proof Procedure

**Prerequisites:** Plugin v0.2.0 on DEV site; bridge + DEV confirmed; token generated; **write_enabled** ON for rollback step.

### Steps

| # | Action | Expected |
|---|--------|----------|
| 1 | `GET /pages/{id}` — inspect_page | `content_checksum` = baseline `C0` |
| 2 | `POST /pages/{id}/backups` | `backup_id`, `content_checksum` = `C0`, audit rows |
| 3 | Edit `post_content` manually in WP Admin | Live content changes; new checksum `C1` |
| 4 | `GET /pages/{id}` | `content_checksum` = `C1` ≠ `C0` |
| 5 | `POST /pages/{id}/rollback` with `backup_id`, `approval_ref`, `expected_current_checksum: C1` | `restored_checksum` = `C0`, `mutation_performed: true` |
| 6 | `GET /pages/{id}` — validate | `content_checksum` = `C0` (match backup) |
| 7 | Compare checksums | `C0` after rollback == backup `content_checksum` |

### Example curl (replace host, id, token)

```bash
# 1. Inspect
curl -s -H "X-WPilot-Token: $TOKEN" \
  "https://dev.example/wp-json/wpilot/v1/pages/69"

# 2. Backup
curl -s -X POST -H "X-WPilot-Token: $TOKEN" -H "Content-Type: application/json" \
  -d '{"reason":"sprint1_proof","approval_ref":"proof-001"}' \
  "https://dev.example/wp-json/wpilot/v1/pages/69/backups"

# 3. Manual WP Admin edit (human step)

# 4. Inspect changed checksum C1

# 5. Rollback
curl -s -X POST -H "X-WPilot-Token: $TOKEN" -H "Content-Type: application/json" \
  -d '{"backup_id":1,"approval_ref":"proof-001","expected_current_checksum":"sha256:..."}' \
  "https://dev.example/wp-json/wpilot/v1/pages/69/rollback"

# 6. Validate checksum match
```

**Evidence to archive (MARS):** request/response JSON, audit log query, before/after checksums.

**SAFE UNKNOWN:** Live DEV proof not executed from this repository — requires deployed plugin on target host.

---

## 9. Risks

| Risk | Assessment | Mitigation |
|------|------------|------------|
| **WPBakery pages** | Low for full-field restore | Store/restore exact `post_content` string; no shortcode parsing on rollback; byte-identical restore preserves VC structure |
| **Shortcode content** | Low | No partial replace; whole `post_content` swapped via WP API |
| **UTF-8 content** | Medium if mishandled | `wp_check_invalid_utf8` on read; no `sanitize_text_field` on content; checksum on normalized bytes |
| **Serialized fragments** | Low in `post_content` | WPBakery uses shortcodes in post_content, not PHP serialized meta; rollback does not touch `postmeta` |
| **wp_slash / stripslashes** | Medium | `wp_slash()` before `wp_update_post`; read via `get_post` (unslashed); checksum pipeline uses same read path as inspect |
| **Human edits after backup** | Expected | `expected_current_checksum` guard; operator must confirm drift before rollback |
| **Single-use backup** | Policy enforced | `rollback_used_at` blocks reuse (`BACKUP_ALREADY_USED`) |
| **Cache/CDN** | SAFE UNKNOWN | Post-rollback frontend may lag; manual HTML check still required |
| **Plugin backup ≠ site backup** | High if misunderstood | Labels, docs, operator training — rollback only restores one page field |

---

## 10. Next Sprint Recommendation

After successful DEV proof of **inspect → backup → manual drift → rollback → checksum match**:

1. Implement `POST /pages/{id}/scoped-replace` execute (`apply_replace`).
2. Chain: dry-run → backup → scoped-replace → validate_page (checksum).
3. Reuse existing backup/audit/operation_id infrastructure.
4. Update Proven Capabilities register with REST-backed rollback proof.
5. Retire temporary PHP helpers for the same operation class on DEV.

**Do not start:** production, CSS/menu/widget endpoints, ChangeSet REST CRUD, multisite.

---

## Git status note

Implementation is in-repo under `projects/wpilot/plugin/metacode-wpilot/`. No commit performed (default policy).
