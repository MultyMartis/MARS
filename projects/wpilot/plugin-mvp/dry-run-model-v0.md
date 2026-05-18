# WPilot Dry-run Model v0

**Status:** CORE / PLANNED / DEV-ONLY.
**Scope:** no-mutation preview model for WPilot Phase 2 safe write planning.

Dry-run is the required gate before any future execute mutation. It must never mutate WordPress content, create live content changes, trigger rollback execution, or perform hidden repair.

## Philosophy

Dry-run answers one question: can this exact replacement be safely executed later under the current content, state, and WPBakery constraints?

Dry-run is:

- Deterministic.
- Read-only.
- Refusal-first.
- Human-reviewable.
- Bound to one target and one exact replacement plan.

Dry-run is not:

- A content editor.
- A suggestion engine.
- AI rewriting.
- HTML cleanup.
- Shortcode repair.
- Backup execution.
- A guarantee that future content will remain unchanged.

## Request Shape

**CORE / PLANNED:** a dry-run request should include:

- Target page ID.
- Exact source string.
- Exact replacement string.
- Optional expected current checksum.
- Optional operator note.
- Explicit dry-run intent.

Abort preview if:

- Request is malformed.
- Target is unsupported.
- Operation is not exact deterministic replacement.
- Source or replacement violates safety constraints.

## No-mutation Behavior

Dry-run may read content and compute previews. It must not:

- Call WordPress update APIs.
- Change `post_content`, metadata, options, files, database schema, plugin settings, or external services.
- Create rollback records that imply mutation occurred.
- Run browser automation.
- Attempt automatic repair.

Audit of dry-run itself may be allowed if it stores only sanitized metadata and no content dump.

## Exact Occurrence Preview

Dry-run must count exact source-string occurrences in the current content.

Accepted preview requires:

- Count is exactly one.
- Match byte/character span is deterministic.
- Match does not move through normalization.
- Match is inside an allowed content zone.

Refuse preview if:

- Count is zero.
- Count is greater than one.
- Match cannot be located without fuzzy logic.
- Match appears in more than one structural zone.

## Replacement Preview

Dry-run may compute an in-memory candidate result for validation only.

Preview must report:

- Target ID.
- Source length.
- Replacement length.
- Match count.
- Approved span summary.
- Before checksum.
- Expected after checksum.
- Structural summary before and after.
- Whether backup would be required for execution.

Preview must not return full page content unless a future implementation explicitly adds a safe, bounded, redacted preview field. Default MVP output should prefer field presence, checksums, counts, and short context-free summaries.

## Refusal Preview

Dry-run refusal should use the same deterministic refusal model as execute.

Refusal response includes:

- `ok: false`
- error code
- stage
- operator meaning
- `mutation_performed: false`
- `rollback_available: false`

Dry-run refusal must not suggest bypassing checks. It may suggest manual inspection or a narrower exact string.

## Checksum Preview

Dry-run must compute a checksum of current content when content is readable.

Rules:

- Checksum identifies the pre-write content snapshot used for preview.
- Execute must provide or reference the same checksum.
- If content changes after dry-run, execute must refuse with checksum mismatch.
- Checksum failure is refusal, not permission to continue.

## WPBakery-safe Zone Preview

Dry-run must classify the match zone before execution is allowed.

Allowed preview result:

- Plain text content zone.
- Not inside shortcode name or attribute.
- Not crossing shortcode boundaries.
- Not inside `vc_raw_html`.
- Not inside encoded, script, style, or HTML tag syntax.
- Shortcode boundary summary remains stable in candidate content.

Refusal preview result:

- Unsafe zone.
- Unsupported builder zone.
- Malformed shortcode structure.
- Replacement introduces shortcode-like syntax or unsafe markup.
- SAFE UNKNOWN classification.

## Dry-run Token

**PLANNED:** execute may require a dry-run reference generated from:

- Operation ID.
- Target ID.
- Source string hash.
- Replacement string hash.
- Before checksum.
- Match span.
- Created timestamp.

The dry-run reference must not contain plaintext token values or full content. Expiry duration is **SAFE UNKNOWN** until implementation.

## Deterministic Response

Success envelope:

```json
{
  "ok": true,
  "data": {
    "mode": "dry-run",
    "target_id": 954,
    "match_count": 1,
    "before_checksum": "sha256:...",
    "expected_after_checksum": "sha256:...",
    "wpbakery_zone": "plain_text",
    "execution_allowed": true
  },
  "meta": {}
}
```

Refusal envelope:

```json
{
  "ok": false,
  "error": {
    "code": "MULTIPLE_MATCHES",
    "message": "Source text appears more than once.",
    "stage": "dry_run",
    "mutation_performed": false,
    "rollback_available": false
  },
  "meta": {}
}
```

## SAFE UNKNOWN

- Exact dry-run reference format.
- Preview context length, if any.
- Dry-run expiry window.
- Whether dry-run audit is mandatory or optional.

