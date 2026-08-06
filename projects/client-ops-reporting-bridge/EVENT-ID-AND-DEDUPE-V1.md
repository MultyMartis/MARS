# Event ID and Deduplication v1

**Status:** DESIGN ONLY / PHASE 0B  
**Implementation:** NOT STARTED

---

## 1. Purpose

Define deterministic `event_id` generation and consumer-side deduplication so that:

- the same normalized source observation yields the same `event_id`;
- publication/delivery retries do not create a new site event;
- materially changed normalized facts yield a new `event_id`;
- Telegram and future AI retries reuse `event_id`;
- `event_id` contains no secrets and does not depend on absolute paths, Telegram destination, or delivery timestamp.

---

## 2. Comparison of approaches

| Approach | Deterministic? | Stable across retries? | Collision / ops notes | Verdict |
|----------|----------------|------------------------|------------------------|---------|
| UUID v4 | No | No (new each run) | Easy but breaks dedupe | **Reject** for site events |
| run_id-only | Partial | Yes per run folder | Collides if re-export with changed normalization; ignores status/metrics | **Reject** as sole identity |
| SHA-256 hex of canonical doc | Yes | Yes | Opaque 64-char; not UUID-shaped | Acceptable alternate |
| UUID v5 from canonical identity | Yes | Yes | Fits envelope “uuid” examples; standard | **Recommend** |

---

## 3. Recommended method

**UUID v5** over a fixed MARS Client Ops namespace UUID, where the UUID v5 **name** is the **SHA-256 hex** (lowercase) of the **canonical identity document** bytes.

```text
event_id = UUID_v5(
  namespace = MARS_CLIENT_OPS_REPORT_NAMESPACE_UUID,  # fixed constant, non-secret
  name    = hex_sha256(canonical_identity_json_utf8)
)
```

**DESIGN ONLY:** The namespace UUID must be a fixed randomly chosen UUID documented at implementation charter time (not derived from secrets). Phase 0B does not invent a “live” namespace resource beyond this rule.

Why this hybrid:

- Deterministic like SHA-256.
- Envelope remains UUID-shaped for validators expecting UUID strings.
- Canonical document hashing keeps UUID v5 name length bounded and encoding-safe.

---

## 4. Canonical identity document

Include exactly these logical fields (names stable):

| Field | Source |
|-------|--------|
| `schema_major` | major of `schema_version` (e.g. `1`) |
| `site_id` | `site.site_id` |
| `event_type` | `event_type` |
| `run_id` | `run.run_id` |
| `observed_at` | normalized UTC `Z` form |
| `normalized_status` | `run.normalized_status` |
| `summary_code` | `run.summary_code` |
| `metrics` | baseline/current/added/removed/onboarding integers |
| `reason_codes` | sorted ascending |
| `action_code` | `action.code` |

**Exclude:** `generated_at`, delivery fields, Telegram destinations, absolute paths, producer hostname, profile mode, AI fields.

### Material change rule

Any change to the included identity fields → new `event_id`.  
Retry with identical normalized facts → same `event_id`.

---

## 5. Canonicalization rules

| Rule | Requirement |
|------|-------------|
| Encoding | UTF-8 |
| Key ordering | Stable sorted keys at every object level |
| Whitespace | No insignificant whitespace (compact JSON) |
| reason_codes | Sorted ascending lexicographically |
| Nulls | Explicit `null` only if field included; prefer omit unused optional identity fields — MVP identity has no nulls |
| Integers | Preserve integer types (no `1.0`) |
| Timestamps | UTC with `Z` suffix in identity doc |
| Booleans | `true`/`false` lowercase JSON |

Pseudocode:

```text
identity = {
  action_code,
  event_type,
  metrics: { added_urls, baseline_count, current_count, onboarding_needed_count, removed_urls },
  normalized_status,
  observed_at,          # UTC Z
  reason_codes: sorted(reason_codes),
  run_id,
  schema_major,
  site_id,
  summary_code
}
bytes = utf8(json_compact_sorted(identity))
name  = sha256_hex(bytes)
event_id = uuid_v5(NAMESPACE, name)
```

---

## 6. Security constraints on `event_id`

- Must not embed secrets, tokens, chat IDs, URLs with credentials.
- Must not embed absolute Windows/UNC paths.
- Must not depend on Telegram destination.
- Must not depend on delivery timestamp.

---

## 7. n8n dedupe state options

| Option | Pros | Cons | MetaBOT signal |
|--------|------|------|----------------|
| Workflow static data | Simple | Known drift / export pollution risk in MetaBOT intake history | Use cautiously |
| n8n Data Store | Durable within n8n; portable across profiles | Host-specific; backup needed | Prefer over staticData for authority |
| External state file (promoted `state/`) | Auditable on Storage | PROFILE A natural; PROFILE B needs exporter host sync | Good audit mirror |
| Database | Strong | Out of MVP scope unless already present | Not assumed |
| Promoted state manifest | Human-auditable | Concurrency needs locks | Good secondary |

### MVP recommendation

**Primary dedupe store:** **n8n Data Store** keyed by `event_id` → delivery record.

**Optional mirror (PROFILE A):** append-only or replace-safe record under promoted `state/` for operator audit.

**Do not** treat workflow `staticData` as sole long-term authority (MetaBOT lessons: staticData snapshots drift vs operational SoT).

Phase 0B implements **neither**.

---

## 8. Duplicate handling statuses

| Status | Meaning | Telegram send? |
|--------|---------|----------------|
| `NEW` | No prior successful/terminal record | Yes (per send policy) |
| `DUPLICATE_ALREADY_SENT` | Prior confirmed SENT for same `event_id` | **No** |
| `DUPLICATE_PREVIOUSLY_FAILED` | Prior delivery FAILED / uncertain | See retry rules |
| `RETRY_ALLOWED` | Prior attempt failed or uncertain; retry permitted | Yes (retry) |
| `CONFLICTING_EVENT_ID` | Same `event_id` seen with **different** payload hash | **No** — manual review |

### Payload conflict

If `event_id` matches but envelope SHA-256 differs → `CONFLICTING_EVENT_ID` (should be rare if algorithm correct). Fail closed; do not send.

---

## 9. Retry identity rules

| Retry type | event_id |
|------------|----------|
| Re-publish same normalized observation | Same |
| Telegram delivery retry | Same |
| AI retry (future) | Same |
| New monitor run / changed normalized facts | New |

---

## 10. Delivery record shape (design)

```json
{
  "event_id": "uuid",
  "envelope_sha256": "hex",
  "delivery_status": "SENT|FAILED|RETRYING|NOT_ATTEMPTED",
  "last_attempt_at": "ISO-8601-UTC",
  "attempt_count": 1
}
```

No chat IDs or tokens in records destined for Git.
