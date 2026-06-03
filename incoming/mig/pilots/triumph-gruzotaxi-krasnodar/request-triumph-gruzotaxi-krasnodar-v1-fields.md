# Research Request field documentation — triumph-gruzotaxi-krasnodar-v1

Canonical object per [mig-research-request-contract-v0.md](../../../../projects/mig/contracts/mig-research-request-contract-v0.md).

---

## Required fields

| Field | Value (pilot) | Meaning |
|-------|---------------|---------|
| `schema_version` | `"0"` | Contract major version |
| `request_id` | `triumph-gruzotaxi-krasnodar-v1` | Stable intake id; must match inbox filename `request-<request_id>.json` |
| `request_type` | `groundtruth_run` | Full groundtruth pipeline: SERP → competitors → optional website/landing → draft pack. **Accepted** by Task File Adapter v0.1 (OR-10) — do not substitute `serp_capture`. |
| `scope.niche` | `Грузотакси` | Market vertical |
| `scope.region` | `Краснодар` | Geographic scope |
| `scope.business_type` | `local_service` | Local service business model |
| `scope.search_engine` | `yandex` | Target SERP engine (lowercase) |
| `scope.device` | `mobile` | SERP device context (lowercase) |
| `queries.seed_queries` | 12 strings | Seed set — **Runtime MVP uses first element only** as `query_used` |
| `operator_id` | `human-supervised` | Owning operator / supervision mode |
| `created_at` | ISO-8601 UTC | Request creation timestamp |
| `source.adapter` | `task_file` | Task File Adapter |
| `source.adapter_version` | `0.1` | Adapter semver |
| `source.transport_ref` | inbox path | Opaque handle to dropped file (no secrets) |

---

## Optional fields (set on this pilot)

| Field | Value | Meaning |
|-------|-------|---------|
| `scope.city` | `Краснодар` | City-level localization for local pack |
| `capture_profile` | see below | Explicit pass toggles |
| `priority` | `normal` | Queue hint (ignored in v0.1) |
| `strict` | `false` | Warnings do not fail validation |
| `downstream_context` | object | Operator notes — **not** ORCA semantics |

### `capture_profile` (pilot)

| Key | Value | Charter alias | Runtime behavior |
|-----|-------|---------------|------------------|
| `multi_query` | `false` | — | Single-query MVP execution |
| `website_pass` | `true` | — | P3: HTTP fetch top competitor URLs |
| `landing_pass` | `true` | — | P4: landing block / CTA / trust extraction |
| `keyword_pass` | `false` | **keyword_runtime off** | No Wordstat / keyword surface pass |
| `deep_research_pass` | `false` | **deep_research off** | No LLM deep-research memo |

Runtime MVP **forces** `keyword_pass` and `deep_research_pass` off regardless of request ([resolve-capture-profile.js](../../../../projects/mig/lib/runtime/resolve-capture-profile.js)).

---

## Fields absent until execution

| Field | When added | Operator action |
|-------|------------|-----------------|
| `manual_serp` | Before adapter run | Paste captured SERP JSON per [pilot-serp-capture-checklist.md](pilot-serp-capture-checklist.md) |
| `session_id` | After adapter binds session | **Do not** set before drop — adapter/runtime assigns |
| `status` | Adapter/runtime | Lifecycle state |

---

## Fields intentionally omitted

| Field | Reason |
|-------|--------|
| `provider_response` | No SERP API configured for pilot MVP — manual path only |
| `fixture_map` | Production run — live HTTP fetch, not test fixtures |
| `expectations` | Test-fixture only — not part of production intake |
| `resume_from_session` | New session, not resume |

---

## `manual_serp` shape (reference — fill at execution)

When operator completes SERP capture, `manual_serp` must follow the discipline in [test-payload-manual-serp-v0.1.json](../../../../projects/mig/test/test-payload-manual-serp-v0.1.json):

- `query`, `search_engine`, `region`, `city`, `device`, `localization`, `timestamp`
- `serp_type`, `ads_blocks`, `maps_local_pack`, `aggregators`, `marketplaces`
- `organic_results[]` with `position`, `title`, `url` (+ optional `snippet`)
- `safe_unknown[]` for gaps — **never fabricate**
