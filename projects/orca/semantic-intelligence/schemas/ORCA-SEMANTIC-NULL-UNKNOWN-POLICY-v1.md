# ORCA Semantic Null and Unknown Policy v1

**Policy ID:** `orca-semantic-null-unknown-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Distinguish **meaningful absence** from **epistemic unknown** and forbid placeholder sentinels that corrupt audit and operator review.

---

## Semantic distinctions

| Term | Meaning | JSON representation | Example field |
|------|---------|----------------------|---------------|
| **unknown** | Assessor could not determine value; epistemic limit | `UNKNOWN` enum or intent/goal id `UNKNOWN` | `provenance_status: UNKNOWN`, `primary_intent: UNKNOWN` |
| **not assessed** | Stage not run yet; not same as unknown | omit optional field or explicit stage flag in audit | signals not populated pre-SI-05 |
| **not applicable** | Field irrelevant for this phrase | `null` where schema allows | `geography: null` for global SaaS doc query |
| **absent** | Expected optional content missing after assessment | `[]` empty array or `null` per schema | `secondary_intents: []` |
| **empty** | Zero-length input | `raw_query` invalid if empty (minLength 1) | rejected at ingest |
| **unresolved** | Competing hypotheses remain | `ambiguity.unresolved_questions` non-empty | ABSTAIN records |
| **no evidence** | No signal support | `strength: NONE` or signal omitted | no PROVIDER_HIRE evidence |

**Do not conflate:** `unknown` (we tried, failed) vs `not assessed` (we did not try) vs `null` (N/A).

---

## Forbidden sentinels

The following **must not** appear in narrative or categorical fields:

| Forbidden | Reason |
|-----------|--------|
| `1234` | Legacy error-code placeholder |
| `2464` | Legacy numeric sentinel |
| `970` | Legacy numeric sentinel |
| `272` | Legacy numeric sentinel |
| Empty string `""` for required narrative | Indistinguishable from missing rationale |
| `[object Object]` | Serialization failure artifact |

**Invariant 14:** Narrative fields (`literal_interpretation`, `phrase_explanation`, `review_notes`, competing_interpretations entries) must contain human-readable text or valid taxonomy tokens — never raw numeric sentinels.

---

## Field-specific guidance

| Field | When null | When UNKNOWN token |
|-------|-----------|-------------------|
| `geography` | No geo in phrase and not required | Do not use UNKNOWN string; use null |
| `product_or_module` | Not mentioned | null |
| `provenance_status` | — | MISSING or UNKNOWN enum only |
| `primary_intent` | — | UNKNOWN intent_id when assessed but inconclusive |
| `likely_user_goal` | — | UNKNOWN goal_id |
| `confidence` | — | Use numeric 0.0–1.0, not sentinel integers |

---

## Arrays

- Prefer `[]` for «assessed, none found»
- Omit only if schema allows and stage truly not assessed
- Never `[null]` or `[""]`

---

## Related documents

- [`ORCA-SEMANTIC-RECORD-SCHEMA-v1.md`](ORCA-SEMANTIC-RECORD-SCHEMA-v1.md)
- [`../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md)
