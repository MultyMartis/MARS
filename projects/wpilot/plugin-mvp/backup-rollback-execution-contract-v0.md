# WPilot Backup Rollback Execution Contract v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** backup and rollback contract for future WPilot safe write execution.

This document defines rollback safety before write endpoints exist. It does not create backups, perform rollback, or mutate content.

## Principle

Rollback is a narrow recovery path for plugin-created backups only. It is not a site backup system, deployment system, database restore tool, or general WordPress repair mechanism.

## Backup Timing

Backup must be created after all pre-write validation passes and before any mutation is attempted.

Required order:

1. Auth, state, DEV-only, and write-enabled validation.
2. Dry-run reference validation.
3. Page existence and content read.
4. Exact occurrence validation.
5. WPBakery-safe zone validation.
6. Backup creation.
7. Backup checksum verification.
8. Final pre-write checksum check.
9. Replacement execution.

Abort before mutation if backup cannot be created, linked, checksummed, or audited.

## Backup Schema

**CORE / PLANNED:** a plugin-owned backup record should include:

| Field | Purpose |
|---|---|
| `backup_id` | Stable backup identifier. |
| `operation_id` | Links backup to one write operation. |
| `source` | Must be `plugin`. |
| `target_type` | Expected `page` for MVP. |
| `target_id` | WordPress page ID. |
| `post_type` | Original post type. |
| `post_status` | Original post status. |
| `content_before` | Exact pre-write content snapshot. |
| `content_checksum` | Checksum of `content_before`. |
| `dry_run_reference` | Link to accepted dry-run, if implemented. |
| `created_at` | Backup timestamp. |
| `created_by` | Safe actor identifier when available. |
| `rollback_used_at` | Nullable timestamp. |
| `rollback_operation_id` | Nullable rollback operation link. |

Backup must not include tokens, auth headers, cookies, credentials, full database dumps, filesystem snapshots, or unrelated personal data.

## Checksum Linkage

Backup checksum is the authority for rollback content integrity.

Rules:

- Backup checksum must be generated from the stored `content_before`.
- Pre-write checksum must match backup checksum immediately before mutation.
- Rollback must verify stored content still matches backup checksum before writing it.
- A checksum mismatch refuses rollback unless a human performs manual recovery outside WPilot.

## Rollback Eligibility

Rollback is eligible only when all conditions are true:

- Backup was created by WPilot.
- Backup belongs to the requested target.
- Backup has not already been used if single-use policy is selected.
- Backup content is readable from plugin-owned storage.
- Backup checksum validates.
- Current target still exists and is a supported content type.
- Operator explicitly requests rollback.
- Bridge, DEV-only, auth, and rollback permission checks pass.

Rollback may be offered after a failed or unverified mutation when the plugin can safely identify the exact backup.

## Rollback Refusal Conditions

Rollback must refuse if:

- Backup is missing.
- Backup source is not `plugin`.
- Target ID or post type does not match backup.
- Backup checksum fails.
- Backup content is unavailable or oversized beyond configured limits.
- Current target cannot be read.
- Current target is no longer a supported page/content type.
- Emergency disabled state blocks operational writes.
- Rollback would require SQL/filesystem/browser automation.
- Plugin cannot safely determine whether rollback would overwrite unrelated human edits.
- SAFE UNKNOWN applies.

## Rollback Execution

**PLANNED:** rollback writes the backed-up content to the same target through WordPress content APIs only.

Rollback execution must:

- Create a rollback operation ID.
- Record rollback-start audit before mutation where audit is required.
- Verify backup checksum before write.
- Write only the backed-up content field for the original target.
- Read back content after write.
- Verify post-rollback checksum equals backup checksum.
- Mark backup as used if policy requires.
- Return deterministic JSON.

Rollback must not:

- Restore whole database tables.
- Modify plugin/theme/core files.
- Change settings unrelated to target content.
- Delete audit records.
- Repair shortcode structure beyond restoring the exact backup content.

## Rollback Audit Behavior

Audit events should include:

- rollback requested
- rollback refused
- rollback started
- rollback write failed
- rollback verified
- rollback verification failed

Audit records may include operation ID, backup ID, target ID, checksums, outcome, and refusal code. They must not include tokens, auth headers, cookies, stack traces, or full content dumps.

## Failed Rollback Handling

If rollback fails after mutation attempt:

- Return `ok: false`.
- Use rollback-specific stage and code where possible.
- Report whether mutation may have occurred.
- Preserve backup record.
- Preserve audit trail.
- Instruct manual review.
- Do not attempt repeated hidden rollback loops.
- Do not broaden permissions or fall back to SQL/filesystem.

## Retention Assumptions

**PLANNED / SAFE UNKNOWN:** retention is intentionally narrow for DEV.

Assumptions:

- Backups are small in number.
- Retention may be manual clear, limited count per target, or limited days.
- No backup should be deleted during an active write or rollback operation.
- Uninstall behavior must be explicit in a later storage implementation contract.

Retention is not proof of disaster recovery. Hosting-level and database-level backups remain external human responsibilities.

## Deterministic Response

Rollback success should include:

- `ok: true`
- rollback operation ID
- backup ID
- target ID
- restored checksum
- verification status

Rollback refusal/failure should include:

- `ok: false`
- refusal code
- stage
- `mutation_performed`
- `rollback_available`
- operator-readable message

