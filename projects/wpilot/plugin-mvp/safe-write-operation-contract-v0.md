# WPilot Safe Write Operation Contract v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** controlled mutation lifecycle for WPilot Phase 2 before any write endpoint is implemented.

This contract defines the only acceptable path toward content mutation. It does not implement write endpoints, execute rollback, create backups, or mutate WordPress content.

## Safety Principle

The Phase 2 write model is refusal-first, backup-first, deterministic, observable, and human-supervised.

**EXCLUDED:**

- AI rewriting.
- Smart editing.
- Broad or mass replacement.
- Browser automation.
- Autonomous repair.
- Arbitrary SQL, filesystem, code execution, plugin/theme/core updates.
- Mutation outside approved WordPress content APIs.

## Covered Mutation

**CORE / PLANNED / DEV-ONLY:** one exact deterministic text replacement on one approved DEV page content field after dry-run, backup, checksum, WPBakery-safe-zone validation, and operator sign-off.

No other mutation type is covered by this contract.

## Required Lifecycle

### 1. Request

The request must describe one target, one exact source string, one replacement string, dry-run or execute intent, and an operator approval reference for execute intent.

Abort if:

- Request body is missing or malformed.
- Target ID is missing, non-numeric, or unsupported.
- Operation is not the approved exact replacement operation.
- Request asks for regex, fuzzy match, translation, summarization, HTML rewrite, shortcode rewrite, mass replacement, SQL, filesystem, browser automation, or AI rewrite.

### 2. Auth

The request must pass the existing per-site token authentication model.

Abort if:

- Token is missing, invalid, revoked, or supplied through an unsupported channel.
- Auth result cannot be represented without exposing secrets.
- Permission context is insufficient for the requested operation.

### 3. Bridge State Validation

The bridge must be enabled and operational before any target content is read for a write-like operation.

Abort if:

- Bridge is disabled.
- Emergency disable is active.
- Plugin state is invalid.
- Required storage or options cannot be read safely.

### 4. DEV-only Validation

The operation must remain explicitly DEV-only.

Abort if:

- DEV/test confirmation is absent.
- Environment cannot be classified as allowed for DEV mutation.
- Operator tries to use the bridge as production automation.
- The plugin cannot prove that DEV-only safeguards are active.

### 5. Write-enabled Validation

Write capability must require a separate explicit toggle beyond read-only bridge access.

Abort if:

- `write_enabled` is false.
- Write toggle state is missing or inconsistent.
- Write settings do not match the allowed MVP operation.
- Human approval reference is absent for execute intent.

### 6. Dry-run Precheck

Every execute request must be preceded by a matching dry-run result.

Abort if:

- Dry-run was not performed.
- Dry-run input differs from execute input.
- Dry-run result is expired, rejected, or SAFE UNKNOWN.
- Dry-run did not confirm exactly one allowed occurrence.

### 7. Page Existence Validation

Target content must be read through WordPress APIs.

Abort if:

- Page does not exist.
- Post type is outside the MVP allowlist.
- Target status is not allowed by operator policy.
- Content cannot be read safely.
- Content type is unsupported.

### 8. Exact Occurrence Validation

The source string must appear exactly once in the current content.

Abort if:

- Source string appears zero times.
- Source string appears more than once.
- Match position differs from the approved dry-run.
- Replacement would affect more than one span.
- Source and replacement are identical when no-op writes are disallowed.

### 9. WPBakery-safe Zone Validation

The match must be in a plain text zone that does not cross or modify builder structure.

Abort if:

- Match is inside shortcode name, shortcode attribute, shortcode boundary, `vc_raw_html`, encoded content, script, style, HTML tag syntax, or unsupported builder area.
- Match crosses structural boundaries.
- Replacement introduces shortcode-like syntax or unsafe markup.
- Structure map is malformed, unstable, or SAFE UNKNOWN.

### 10. Backup Creation

A plugin-owned backup must be created after validation and before mutation.

Abort if:

- Backup storage is unavailable.
- Backup write fails.
- Backup cannot be linked to operation ID, target ID, content checksum, and timestamp.
- Backup source cannot be marked as plugin-created.

### 11. Checksum Snapshot

The plugin must compute a pre-write checksum after backup and immediately before replacement.

Abort if:

- Checksum generation fails.
- Current checksum differs from backup checksum.
- Current checksum differs from the dry-run or request expected checksum.
- Content changed between dry-run, backup, and execute.

### 12. Replacement Execution

Execute exactly one in-memory replacement and write through WordPress content APIs only.

Abort before write if:

- Replacement plan no longer matches current content.
- Replacement count is not exactly one.
- Target ID or content field differs from the approved plan.

Treat as failure if:

- WordPress API write fails.
- API result targets an unexpected record.
- Write result cannot be read back.

### 13. Post-write Verification

Read the target after write and verify deterministic result.

Failure if:

- Replacement text is absent from the approved span.
- Source text remains in the approved span.
- More than one occurrence changed.
- Post-write checksum cannot be generated.
- WPBakery boundary summary differs unexpectedly.
- Structure-read validation fails or is SAFE UNKNOWN after mutation.

### 14. Rollback Trigger Conditions

Rollback must be considered when mutation may have occurred and verification fails.

Trigger rollback path when:

- Write API reports success but post-write verification fails.
- Checksum after write is inconsistent with expected output.
- Structure validation reports corruption risk.
- Audit cannot record a completed write outcome after mutation.
- Operator explicitly requests rollback for a plugin-created backup.

Rollback must not run automatically when the plugin cannot safely identify the correct plugin-created backup.

### 15. Audit Log Write

Audit events must be written before and after mutation where storage is available.

Abort before mutation if:

- Write-start audit event cannot be written.
- Audit storage is unavailable and policy requires observable mutation.

After mutation:

- Failure to write final audit is a serious failure requiring manual review.
- Do not hide audit failure behind a success response.
- Do not log tokens, auth headers, cookies, raw stack traces, or unrelated personal data.

### 16. Deterministic Response

Every outcome must return compact JSON.

Success response includes:

- `ok: true`
- operation ID
- target ID
- backup ID
- before checksum
- after checksum
- replacement count
- post-write verification status
- warnings, if any

Refusal/failure response includes:

- `ok: false`
- stable error code
- stage
- `mutation_performed`
- `rollback_available`
- operator-readable message

No response may include plaintext token values, auth headers, credentials, SQL, stack traces, full filesystem paths, or hidden debug payloads.

## Mutation MUST Abort

Mutation MUST abort at any stage that cannot prove safety. SAFE UNKNOWN is a refusal state, not a degraded execution mode.

Mandatory abort classes:

- Auth, state, DEV-only, or write-enabled failure.
- Missing valid dry-run.
- Page, content, checksum, or storage ambiguity.
- Zero or multiple matches.
- WPBakery unsafe zone.
- Backup failure.
- Checksum mismatch.
- Unsupported content.
- Audit preflight failure when audit is required.
- Any request for excluded behavior.

