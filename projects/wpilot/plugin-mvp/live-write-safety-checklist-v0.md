# WPilot Live Write Safety Checklist v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** operator checklist before any future live DEV mutation attempt.

This checklist is for supervised DEV validation only. It does not authorize production mutation, autonomous editing, AI rewriting, broad replacement, browser automation, SQL writes, or filesystem writes.

## Precondition

Use this checklist only after write endpoints are implemented and reviewed. Until then, WPilot remains a safe read-only DEV bridge.

## Checklist

### DEV-only Confirmation

- [ ] Target site is confirmed DEV/test, not production.
- [ ] Operator understands mutation may alter WordPress content.
- [ ] Bridge state confirms DEV-only mode.
- [ ] No production automation or scheduled/background operation is involved.

### Write-enabled Toggle Confirmation

- [ ] Read-only bridge is enabled.
- [ ] Separate write-enabled toggle is explicitly enabled.
- [ ] Emergency disable is not active.
- [ ] Plugin state is not `invalid-config` or `safe-unknown`.

### Token Handling Rules

- [ ] Token is supplied locally only.
- [ ] Token is not printed, committed, screenshotted, or logged.
- [ ] Invalid-token refusal was tested recently.
- [ ] Token rotation/revocation path is known before mutation.

### Target Confirmation

- [ ] Target page ID is confirmed through read endpoint.
- [ ] Target content checksum is captured.
- [ ] Target post type/status is allowed for MVP.
- [ ] Operator has a manual recovery path outside WPilot if needed.

### Exact Occurrence Confirmation

- [ ] Source string is exact current stored content.
- [ ] Source string appears exactly once.
- [ ] Replacement string is exact intended text.
- [ ] Source and replacement do not require normalization, regex, fuzzy match, translation, or AI rewrite.

### Dry-run Preview Confirmation

- [ ] Dry-run returned `ok: true`.
- [ ] Dry-run reported `match_count: 1`.
- [ ] Dry-run reported a before checksum.
- [ ] Dry-run reported an expected after checksum.
- [ ] Dry-run classified the target as an allowed safe zone.
- [ ] Dry-run result was reviewed by a human operator.

### WPBakery Safety Confirmation

- [ ] Match is not inside shortcode name.
- [ ] Match is not inside shortcode attributes.
- [ ] Match does not cross shortcode boundaries.
- [ ] Match is not inside `vc_raw_html`.
- [ ] Match is not inside encoded content.
- [ ] Match is not inside script/style or HTML tag syntax.
- [ ] Structure summary remains stable in dry-run.

### Backup Validation

- [ ] Plugin-owned backup creation is available.
- [ ] Backup storage health is confirmed.
- [ ] Backup schema/version is compatible.
- [ ] Backup checksum can be generated and verified.
- [ ] Backup will be linked to operation ID and target ID.

### Rollback Availability

- [ ] Rollback route/operation exists and is reviewed.
- [ ] Rollback is limited to plugin-created backups.
- [ ] Rollback refusal conditions are understood.
- [ ] Operator knows how to verify rollback result.
- [ ] Hosting/database backup responsibility remains external and human-owned.

### Operator Sign-off Requirement

- [ ] Human operator approves the exact target, source, replacement, and dry-run result.
- [ ] Approval reference is recorded in the request or audit metadata.
- [ ] Operator is present to inspect result immediately after execution.
- [ ] No autonomous retry or repair is enabled.

### Execution Readiness

- [ ] Write-start audit can be recorded.
- [ ] Content checksum still matches dry-run.
- [ ] Current occurrence count is still exactly one.
- [ ] Backup has not failed.
- [ ] No SAFE UNKNOWN condition is present.

### Post-write Verification

- [ ] Target content is read back after write.
- [ ] Replacement occurred exactly once.
- [ ] Before text is absent from the approved span.
- [ ] After checksum matches expected checksum.
- [ ] Response is deterministic JSON.
- [ ] No HTML fatal page or stack trace is returned.

### Structure-read Validation After Mutation

- [ ] `GET /pages/{id}/structure` returns JSON.
- [ ] WPBakery shortcode counts remain expected.
- [ ] Basic integrity remains acceptable.
- [ ] Warnings are reviewed.
- [ ] Frontend visual/manual check is completed where relevant.

### Emergency Disable Readiness

- [ ] Operator can disable bridge immediately.
- [ ] Operator can disable write mode immediately.
- [ ] Token can be revoked immediately.
- [ ] Backup and audit records are preserved.
- [ ] Manual rollback/recovery path is known.

## Stop Conditions

Stop and refuse mutation if any item above is false, unknown, or not reviewed.

Mandatory stop labels:

- **SAFE UNKNOWN:** evidence missing or ambiguous.
- **EXCLUDED:** requested behavior outside MVP.
- **PARTIALLY OPERATIONAL:** dependency exists but has not been validated for this target.

## Completion Record

After a future mutation attempt, record only sanitized facts:

- Operation ID.
- Target ID.
- Backup ID.
- Before checksum.
- After checksum.
- Refusal or success code.
- Post-write verification result.
- Rollback status if applicable.

Do not record tokens, auth headers, cookies, credentials, raw stack traces, or unrelated content dumps.

