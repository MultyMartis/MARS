# WPilot Write Operation Lifecycle v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** lifecycle contract for first installable plugin MVP write-like operations.

This document defines how a scoped replacement must move from request to response. The MVP prefers safe refusal over dangerous modification.

## Covered Operation

**CORE / PLANNED:** one text-only replacement on one approved WordPress page/post content field, using WordPress APIs, after plugin-created backup and validation.

Out of scope:

- Arbitrary SQL.
- Filesystem writes.
- Plugin/theme/core updates.
- Multi-page replacement.
- Background autonomous mutation.
- Browser/admin automation.

## Lifecycle Overview

1. Request received.
2. Auth validation.
3. Operation validation.
4. Dry validation.
5. Page backup.
6. Checksum generation.
7. WPBakery structure validation.
8. Scoped replacement.
9. Post-write validation.
10. Audit log write.
11. Success/failure response.
12. Rollback path.

## 1. Request Received

The REST controller receives `POST /page/{id}/replace-text`.

Minimum request fields:

- Target page/post ID.
- Expected before text.
- Replacement text.
- Match mode: exact single occurrence only for MVP.
- Dry-run flag or explicit execute flag.
- Human approval reference for execution.
- Optional expected pre-write checksum.

Abort if:

- Route is not registered in the allowlist.
- Bridge is disabled.
- Request body is missing or malformed.
- Target ID is missing, non-numeric, or unsupported.
- Operation is not a known MVP operation.

## 2. Auth Validation

The request must pass per-site token validation and operation-level permission checks.

Abort if:

- Token is absent.
- Token is invalid.
- Token is revoked.
- Token is submitted through an unsupported channel.
- User/capability context is insufficient where WordPress user context is required.
- Authentication failure cannot be logged safely.

## 3. Operation Validation

Validate operation shape before reading or mutating content.

Abort if:

- Target post type is not allowed for MVP.
- Target status is not allowed by operator policy.
- Replacement text is empty when empty replacement is disallowed.
- Before text and replacement text are identical.
- Request asks for regex, wildcard, HTML restructuring, shortcode editing, or mass replacement.
- Request references filesystem, SQL, plugin, theme, core, upload, or `wp-config.php` targets.
- Approval reference is missing for execute mode.

## 4. Dry Validation

Read current content through WordPress APIs and compute a dry-run plan.

Dry validation must determine:

- Target exists.
- Target is readable.
- Target content can be loaded.
- Before text appears exactly once in an allowed edit zone.
- Replacement would not modify shortcode boundaries.
- Expected checksum matches if provided.

Abort if:

- Target cannot be read.
- Content is empty and expected content is not empty.
- Before text appears zero times.
- Before text appears more than once.
- Match crosses shortcode boundary.
- Match is inside a forbidden edit zone.
- Parser cannot produce a stable enough map for the requested edit.
- Expected checksum does not match current content.

## 5. Page Backup

Before execution, create a plugin-owned backup snapshot of the current page content and metadata needed for rollback.

Backup must include:

- Target ID.
- Target type.
- Current content.
- Current content checksum.
- Timestamp.
- Operation reference.
- Actor class or user ID where safely available.

Abort if:

- Backup table/storage is unavailable.
- Backup write fails.
- Backup checksum cannot be generated.
- Backup cannot be linked to the operation.
- Audit preflight indicates write-like events cannot be logged.

## 6. Checksum Generation

Generate current pre-write checksum after backup and before mutation.

Abort if:

- Checksum generation fails.
- Current checksum differs from backup checksum.
- Current checksum differs from request expected checksum, when provided.
- Content changed between dry validation and backup.

## 7. WPBakery Structure Validation

Build a shortcode-aware map and validate that the replacement is text-only and structure-preserving.

Abort if:

- Shortcode parsing reports malformed boundaries.
- The target is inside shortcode names or attributes.
- The target crosses opening/closing shortcode boundaries.
- The target is inside raw HTML or encoded content that the MVP cannot safely classify.
- Replacement would introduce unmatched `[` or `]` shortcode-like syntax.
- Replacement would alter shortcode nesting.

## 8. Scoped Replacement

Perform one replacement in memory, then write via WordPress APIs.

Required behavior:

- Replace exactly one approved occurrence.
- Preserve all other content byte-for-byte where feasible.
- Use `wp_update_post` or equivalent WordPress content API.
- Do not issue arbitrary SQL.

Abort before write if:

- Replacement plan no longer matches current content.
- Replacement count is not exactly one.
- WordPress API write target differs from approved target.

Treat as failure if:

- WordPress API returns error.
- WordPress API reports an unexpected target.
- Write result cannot be verified.

## 9. Post-Write Validation

Read content after write and compare expected result.

Validate:

- New text is present exactly as expected.
- Old target text is absent for the approved occurrence.
- Replacement count is exactly one.
- Shortcode structure map remains valid enough for MVP.
- Post-write checksum is generated.

Failure if:

- Post-write read fails.
- New text is absent.
- Old target text remains in the same approved location.
- More than one occurrence changed.
- Shortcode map becomes malformed.
- Checksum cannot be generated.

## 10. Audit Log Write

Write an operation outcome event.

Minimum outcomes:

- `accepted`
- `rejected`
- `failed`
- `succeeded`
- `rollback_requested`
- `rolled_back`

Abort before mutation if:

- Audit logger cannot write the planned write-start event.

After mutation:

- If final audit write fails, return a failure response and instruct manual review.
- Do not attempt hidden repair.
- Preserve rollback reference in response if available.

## 11. Success Or Failure Response

Success response includes:

- Operation ID.
- Target ID.
- Backup ID.
- Before checksum.
- After checksum.
- Replacement count.
- Audit event ID.
- Manual verification reminder.

Failure/refusal response includes:

- Operation ID where available.
- Safe error code.
- Abort stage.
- Whether mutation occurred.
- Backup ID where available.
- Rollback availability.
- Manual review instruction.

Responses must not include secrets, token values, raw stack traces, database dumps, or unrelated content.

## 12. Rollback Path

Rollback uses `POST /page/{id}/rollback` with an approved plugin-created backup ID.

Rollback must:

- Authenticate request.
- Validate bridge is enabled.
- Validate backup belongs to target.
- Validate backup was created by this plugin.
- Create a rollback-start audit event.
- Restore content through WordPress APIs.
- Generate post-rollback checksum.
- Log rollback outcome.

Abort rollback if:

- Backup ID is missing or unknown.
- Backup target does not match request target.
- Backup content is unavailable.
- Current page cannot be read.
- WordPress API write fails.
- Rollback audit preflight fails.

## Global Must-Abort Conditions

The operation must abort if any of these are true:

- Bridge disabled.
- DEV/test status not manually confirmed in plugin settings.
- Invalid or revoked token.
- Missing administrator capability for configuration or write approval.
- Missing human approval reference for execution.
- Backup cannot be created.
- Audit preflight for write cannot be created.
- Target match is zero, multiple, ambiguous, or outside allowed zones.
- Parser reports malformed shortcode structure.
- Expected checksum mismatch.
- Request asks for arbitrary SQL, filesystem access, code execution, mass replacement, or software updates.
- WordPress API returns an error.
- Mutation outcome cannot be verified.

## Failure Philosophy

Failures are first-class outcomes. A rejected operation is a successful safety result when it prevents an unsafe mutation.

The MVP must not:

- Retry with broader permissions.
- Fall back to SQL.
- Fall back to filesystem edits.
- Attempt automatic repair.
- Continue after failed backup.
- Continue after failed validation.

