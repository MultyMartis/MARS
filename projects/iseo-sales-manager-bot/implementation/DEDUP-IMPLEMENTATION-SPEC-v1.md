# DEDUP IMPLEMENTATION SPEC v1

**Product:** i-SEO Sales Manager Bot  
**Phase:** 3A  
**Principle:** bounded lookup via `DEDUP_INDEX` — **never** full CLEAN sheet read per lead

---

## 1. Index schema

| Field | Purpose |
|-------|---------|
| `dedup_key` | Compact unique lookup (`{key_type}:{normalized_value}`) |
| `key_type` | `gmail_message_id` \| `phone` \| `email` \| `messenger` \| `site` |
| `lead_id` | Owning CLEAN lead |
| `gmail_message_id` | Source message when known |
| `normalized_value` | Canonical form used in key |
| `created_at` | First index write |
| `last_seen_at` | Last match/update |
| `active` | Soft disable without delete |

Optional future (not required): `is_primary_contact_key` from Phase 2 model — can be derived from `key_type ∈ {phone,email,messenger}`.

---

## 2. Normalization rules

| Type | Normalize |
|------|-----------|
| `gmail_message_id` | trim; reject empty |
| `phone` | digits only (+ keep leading + as metadata separately); **valid length** typically 10–15 digits after country normalization; reject `44`, short stubs, `#ERROR!` |
| `email` | lower trim; must contain `@` and domain dot |
| `messenger` | lower trim; require handle-like token (`@name` or `t.me/...`); reject generic labels `telegram`, `whatsapp`, `viber`, `телефон` alone |
| `site` | registrable domain lower; strip protocol/path/query; reject empty / `localhost` |

**Never** index: `#ERROR!`, formula errors, whitespace-only, placeholder phones, generic messenger words.

---

## 3. Lookup strategy (per lead)

1. Build candidate keys from current normalized contacts + `gmail_message_id`.  
2. Query DEDUP_INDEX **by exact `dedup_key`** (one query per candidate key, or batch OR if Sheets node allows).  
3. Collect active matches within `dedupe_contact_window_days` (CONFIG; default 365) for contact/site keys. Message-id match ignores window.  
4. Classify (§4).  
5. On successful CLEAN write, upsert keys (`last_seen_at`, `lead_id`).

**Forbidden:** read entire `lead_clean_v2` or historical `lead-base-processed` for every lead.

---

## 4. Classification rules

| Condition | `duplicate_status` | `duplicate_match_type` | Business meaning |
|-----------|--------------------|------------------------|------------------|
| Same `gmail_message_id` | `reprocessed` | `same_message` | Retry / reprocess — **not** business repeat |
| Same phone **or** email **or** messenger (valid) | `repeat` | `phone` / `email` / `messenger` | Repeat client |
| ≥2 strong contact keys → same prior `lead_id` | `repeat` | `multi_evidence` | Exact repeat |
| Same site only | `possible` | `site_only` | Informational — **do not** suppress lead |
| No match | `new` | `none` | New |

### Hard rules

- `same_message` **never** becomes `repeat`.  
- Site-only match **must not** suppress Telegram / CLEAN write.  
- Prefer strongest match; among ties pick most recent `last_seen_at` excluding current lead.  
- Fill `duplicate_lead_id`, `previous_*` from CLEAN row of matched lead (bounded get by `lead_id`).

---

## 5. Reprocess behavior

When `gmail_message_id` already indexed:

1. Map to existing `lead_id`.  
2. Update CLEAN row (do not append duplicate CLEAN).  
3. Telegram header = повторная обработка.  
4. Preserve lifecycle status if already set (do not force `new` unless empty).  
5. Gmail labels follow success/fail policy (incoming preserved until TG success).

---

## 6. Writer / reader

| Workflow | Role |
|----------|------|
| Operational | Lookup + upsert |
| Admin | Read-only diagnostics optional; `/test_lead` may write sandbox index rows |

---

## 7. Failure mode

If DEDUP_INDEX unavailable: classify `new` with warning in `processing_error` / LEAD_EVENTS; **do not** invent matches; log `dedup_read` error.

---

## 8. SAFE UNKNOWN

Sheets lookup API limits for multi-key OR; whether document uses filter views — confirm in sandbox.

---

*Related: LEAD-DATA-MODEL-v1 §5 · OPERATIONAL-WORKFLOW-PATCH-SPEC-v1.*
