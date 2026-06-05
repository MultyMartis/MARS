# MIG Keyword Pass Manifest Contract v1

**Status:** **normative** — manifest discipline only (Phase 2g / G-05)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2g — Provider Infrastructure Contracts  
**Gate closed:** **G-05** — `keyword_pass` manifest flag path and review gate  
**Prior artifacts:** [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md) · [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) · [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md)  
**Related (reference):** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) · [request-triumph-gruzotaxi-krasnodar-v1-fields.md](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/request-triumph-gruzotaxi-krasnodar-v1-fields.md)

**This document delivers:** `keyword_pass` states, allowed transitions, required artifacts, review gate integration, SAFE UNKNOWN behavior — aligned with existing session manifest discipline.

**This document does not deliver:** runtime changes to `resolve-capture-profile.js`, manifest writer code, or automated pass execution.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This contract defines **how the session manifest records keyword pass truth**. It does **not** authorize runtime to execute Wordstat ingest.

---

## Manifest fields (keyword pass surface)

### Primary flag: `capture_profile.keyword_pass`

| Value | Meaning | MVP evidence |
|-------|---------|--------------|
| **`false`** | Keyword / demand provider pass **not** executed or **not** reviewed | All Phase 1 manifests — freeze default |
| **`true`** | Keyword pass **completed** and Human Review Gate **passed** | **Not yet observed** in repo — future pilot target |

**Normative:** Boolean only in v1 contract. Enum expansion (`surface_only`, `surface_and_wordstat`) from Keyword Intelligence v1 remains **reference** — manual pilot uses boolean `true`/`false` until enum charter amends manifest contract.

### Supplementary fields (logical — may be added to manifest on keyword pass)

| Field | Required when | Meaning |
|-------|---------------|---------|
| **keyword_pass_status** | `keyword_pass: true` or partial attempt | `completed` \| `partial` \| `skipped` \| `review_pending` |
| **keyword_pass_started_at** | Pass attempted | ISO-8601 UTC |
| **keyword_pass_completed_at** | `keyword_pass: true` | ISO-8601 UTC — after review gate |
| **keyword_pass_operator_id** | Pass attempted | Operator who ran export + review |
| **keyword_provider_path** | Pass attempted | e.g. `manual_wordstat_export` |
| **keyword_artifacts** | Pass attempted | Logical pointers — see §Required artifacts |
| **keyword_pass_safe_unknown[]** | Always when pass section present | Pass-level gaps |

**Location:** `session_manifest.json` — same level as existing `capture_profile`, `artifacts`, `scope` (mqgt01 pattern).

---

## keyword_pass state model

States describe **manifest truth**, not registry lifecycle (`KR-LC-*`).

| State id | `keyword_pass` | **keyword_pass_status** | Meaning |
|----------|------------------|-------------------------|---------|
| **KP-OFF** | `false` | absent or `skipped` | Default — no demand provider work |
| **KP-PENDING** | `false` | `review_pending` | Snapshot attached; registry or review incomplete |
| **KP-PARTIAL** | `false` | `partial` | Attempt made; review failed or coverage incomplete |
| **KP-COMPLETE** | **`true`** | `completed` | Ingest + Human Review Gate passed |
| **KP-SKIPPED** | `false` | `skipped` | Operator explicitly skipped Wordstat — SAFE UNKNOWN required |

```text
KP-OFF ──attempt──► KP-PENDING ──review pass──► KP-COMPLETE (keyword_pass: true)
   │                      │
   │                      └──review fail / partial coverage──► KP-PARTIAL
   │
   └──explicit skip──► KP-SKIPPED
```

---

## Allowed transitions

| From | To | Trigger | Guard |
|------|-----|---------|-------|
| **KP-OFF** | **KP-PENDING** | Operator attaches raw export or snapshot stub | Raw file ref recorded |
| **KP-PENDING** | **KP-COMPLETE** | Human Review Gate HR-01..HR-05 passed | Registry frozen or reviewed; `keyword_pass: true` |
| **KP-PENDING** | **KP-PARTIAL** | Review failed or partial phrase coverage undeclared | `keyword_pass` stays `false` |
| **KP-PENDING** | **KP-OFF** | Operator abort before any snapshot | Remove pending artifacts or mark skipped |
| **KP-OFF** | **KP-SKIPPED** | Operator documents skip | Session SAFE UNKNOWN: demand not captured |
| **KP-PARTIAL** | **KP-PENDING** | Operator fixes gaps, re-submits for review | New registry revision allowed |
| **KP-COMPLETE** | **KP-PENDING** | Re-capture chartered | New revision — **must not** silently revert `true` without operator action |
| **KP-COMPLETE** | **KP-OFF** | **Forbidden** without new session or explicit amendment | Audit trail integrity |

**Normative (PCR-12):** `keyword_pass: true` **only** when provider ingest completed **and** Human Review Gate passed — not at file drop.

---

## Required artifacts (by state)

| State | Required artifacts | Authority |
|-------|-------------------|-----------|
| **KP-OFF** | None | — |
| **KP-PENDING** | Raw provider file ref; Keyword Snapshot (logical or on disk); `keyword_artifacts.snapshot_ref` | Snapshot = upstream SoT |
| **KP-PARTIAL** | Above + documented gaps in **keyword_pass_safe_unknown[]** | Honest partial |
| **KP-COMPLETE** | Raw file; Keyword Snapshot; Keyword Registry revision (logical `keyword_registry.json`); review checklist record | Registry = demand SoT |
| **KP-SKIPPED** | Session SAFE UNKNOWN only | No false completeness |

### `keyword_artifacts` stub (manifest section)

| Key | When required | Points to |
|-----|---------------|-----------|
| **snapshot_ref** | KP-PENDING+ | `wordstat_snapshot.{capture_id}.json` or path |
| **source_file_ref** | Manual export | Original CSV/XLSX |
| **registry_ref** | KP-COMPLETE | `keyword_registry.json` (revision noted) |
| **review_record_ref** | KP-COMPLETE | Operator checklist file or manifest inline notes |

**Integration with existing `artifacts` block:** Keyword artifacts **may** extend `session_manifest.artifacts` or live in parallel `keyword_artifacts` — pilot **must** record at least one stable pointer. Do not replace SERP artifact keys (`serp_index`, etc.).

---

## Review gate integration

Human Review Gate from [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) binds to manifest as follows:

| Gate check | Manifest effect |
|------------|-----------------|
| **HR-01** Raw snapshot present | `keyword_artifacts.source_file_ref` populated |
| **HR-02** Region match | Pass-level or per-object SAFE UNKNOWN documented in **keyword_pass_safe_unknown[]** |
| **HR-03** Phrase coverage | **keyword_pass_safe_unknown[]** lists missing q-codes |
| **HR-04** Conflicts surfaced | Registry conflict count noted; `keyword_pass_status` = `partial` if unresolved conflicts acknowledged |
| **HR-05** No strategy bleed | Blocks transition to KP-COMPLETE |

**Transition to KP-COMPLETE requires:**

1. HR-01..HR-05 satisfied (HR-04 allows acknowledged unresolved conflicts with `partial` semantics only if operator accepts — default: resolve or document before `true`).
2. Registry writer **freeze** invoked OR operator sign-off on open registry with documented waiver.
3. `keyword_pass_completed_at` and `keyword_pass_operator_id` set.

---

## SAFE UNKNOWN behavior

### Manifest-level (`keyword_pass_safe_unknown[]`)

| Situation | Declaration |
|-----------|-------------|
| Pass not run | «Keyword demand pass not executed — frequency evidence unknown» (default KP-OFF) |
| Explicit skip | «Wordstat export skipped by operator — demand frequency unknown» |
| Partial query coverage | «Provider rows missing for queries: q05, q06, q07» |
| Region mismatch rows | «N rows with export region ≠ session scope.region» |
| Snapshot without registry | «Provider snapshot attached — keyword registry not populated» |
| Review pending | «Keyword pass review pending — registry not authoritative» |
| Re-capture without diff | «Registry revision 2 — diff against revision 1 not computed» |

### Relationship to registry `session_safe_unknown[]`

| Layer | Scope |
|-------|-------|
| **keyword_pass_safe_unknown[]** | Manifest audit — what operator declares about the pass |
| **registry.session_safe_unknown[]** | Registry SoT — what registry writer aggregates |

**Normative:** Manifest **must not** claim `keyword_pass: true` while registry session SAFE UNKNOWN contains «registry not populated».

### MVP runtime note (honest)

Phase 1 runtime ([resolve-capture-profile.js](../../../projects/mig/lib/runtime/resolve-capture-profile.js)) **forces** `keyword_pass: false` regardless of request. First manual pilot may update manifest **by operator edit** after pass — runtime automation of this contract is **not** authorized here.

---

## Alignment with existing manifest discipline

| Existing pattern | Keyword pass alignment |
|------------------|------------------------|
| `capture_profile.serp_pass` | Boolean pass flag — same pattern |
| `capture_profile.website_pass` / `landing_pass` | Independent toggles — keyword pass additive |
| `artifacts.*` pointers | Keyword artifacts follow pointer discipline |
| `status: draft` | Keyword pass does not auto-approve pack |
| `queries_executed[]` | Cross-check phrase coverage — not substitute for Wordstat |
| `scope.region` | HR-02 alignment anchor |

**Phase 1 freeze compatibility:** Setting `keyword_pass: true` on a **new** keyword-only session or additive pass **does not** invalidate Phase 1 SERP/landing evidence (Readiness Charter §Reality Review).

---

## Contradiction guards

| Failure mode | Prevention |
|--------------|------------|
| `keyword_pass: true` without snapshot | Forbidden — KP-COMPLETE guards |
| Snapshot on disk, `keyword_pass: false`, no KP-PENDING | **Manifest lie** — use KP-PENDING + review_pending |
| `keyword_pass: true` without review | Violates PCR-12 |
| SERP inference documented as Wordstat | HR-05 + forbidden numeric source |
| Request `keyword_pass: true` while runtime forces false | Document operator post-pass manifest update until runtime gate |

---

## Architecture decisions (pass manifest contract)

| ID | Decision | Rationale |
|----|----------|-----------|
| **KP-MC-01** | Boolean `keyword_pass` for v1 pilot | Matches existing mqgt01 manifests |
| **KP-MC-02** | Five manifest states KP-* | Clearer than boolean alone |
| **KP-MC-03** | `true` only after Human Review Gate | PCR-12 |
| **KP-MC-04** | Supplementary fields optional until pass attempted | Minimal Phase 1 manifest unchanged |
| **KP-MC-05** | Runtime force-off documented as known gap | Reality-first |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) | HR-01..HR-05 |
| [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) | Freeze before KP-COMPLETE |
| [MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md](MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md) | Umbrella + verdict |
| [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md) | `keyword_pass: false` baseline |

---

*MIG Keyword Pass Manifest Contract v1 · 2026-06-06 · manifest discipline only · G-05 closed · no runtime*
