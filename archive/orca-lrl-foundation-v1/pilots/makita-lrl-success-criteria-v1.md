# Makita LRL Pilot — Success Criteria v1

## Status

**PREPARATION ONLY** — evaluation rubric for the first Landing Readiness Layer pilot (2026-05-30).

**Not** launch approval. **Not** automated scoring. **Not** PPC export authorization.

## Purpose

Determine whether **LRL v1** succeeds or fails when validated with:

- **Project:** Makita
- **`landing_source`:** `existing_client_website`
- **Architectural claim:** ORCA operates without Website Factory

Human operators apply this rubric at Phase 5 of [makita-lrl-pilot-v1.md](makita-lrl-pilot-v1.md).

---

## Evaluation Scope

| In scope | Out of scope |
|----------|--------------|
| One route through FWCP → LRC → PPC gate review | Multi-route batch readiness |
| Operator usability of v1 docs | Exporter / validation-cli behavior |
| Source-agnostic contract shape | Triumph migration |
| Evidence and SAFE UNKNOWN discipline | Campaign performance |

---

## What Validates Architecture

Architecture is **validated** when the pilot demonstrates all of the following with evidence:

| # | Validation item | Evidence expected |
|---|-----------------|-------------------|
| A1 | **Factory-independent path** | FWCP captured from live client site; no Factory handoff steps in session log |
| A2 | **Mandatory chain operable** | Semantic pack (if any) → FWCP (approved) → LRC (approved) completed by human operator |
| A3 | **Deployed copy SoT** | LRC Section 3 cites FWCP; hero/copy fields match live page verification |
| A4 | **URL truth in LRL** | LRC Section 2 records verified `landing_url`; not exporter-only URL edits |
| A5 | **PPC gate separation** | Operator documents that LRC `approved` ≠ Launch READY; export READY semantics understood |
| A6 | **Provenance recorded** | LRC Section 7: `landing_source = existing_client_website` with human description |
| A7 | **Contract shape source-agnostic** | Same LRC sections 1–7 usable without Factory-specific required fields |

**Minimum for architectural PASS:** A1, A2, A3, A4, A6, A7 satisfied. A5 strongly recommended.

---

## What Indicates Missing Fields

Signals that v1 contracts or operator guidance lack required field clarity:

| Signal | Where it appears | Severity |
|--------|------------------|----------|
| Operator could not determine whether a field is required vs recommended | Session log / observation log | High |
| Required LRC section left blank with no SAFE UNKNOWN policy path | LRC draft | High |
| FWCP minimum sections ambiguous — operator invented structure | COPY-PACK.md variance | Medium |
| Identity fields (`route_id`, `intent_group`, `campaign_modes`) undefined for Makita | Phase 1 intake | Medium |
| PPC alignment section fields set without knowing acceptable values | LRC Section 5 | Medium |
| Evidence storage path unclear — evidence skipped | Missing `evidence/<route_id>/` | Low–Medium |
| PACK-STATUS gates vs artifact-system statuses confused | PACK-STATUS.md | Medium |

**Interpretation:** Multiple High signals → **PARTIAL** or **FAIL** on documentation usability; log specific field gaps for post-pilot charter.

---

## What Indicates Excessive Complexity

Signals that LRL v1 imposes operator load beyond intended human-operated scope:

| Signal | Example | Threshold |
|--------|---------|-----------|
| Phase overrun without scope change | Single route exceeds one focused session | >1 full operator day for one route |
| Duplicate capture | Same copy transcribed in FWCP and LRC without clear division of labor | Same hero typed 3+ times |
| Document spiral | Operator opens >5 ORCA docs beyond the three LRL foundation docs | OPERATIONAL-INDEX anti-fatigue violated |
| Alignment section paralysis | Section 5 blocked because ads do not exist yet | Expected — should not block LRC structure test |
| Status ladder confusion | Unclear difference between FWCP `production-ready` and LRC `approved` | Blocks promotion |
| Drift notes over-engineering | Extensive semantic diff when no semantic pack exists | Unnecessary work |
| Evidence grading overhead | evidence-classification-system invoked for every screenshot | Friction without decision value |

**Interpretation:** Complexity alone does not fail architecture if chain completes — but **≥3 Medium+ complexity signals** warrants **PARTIAL** and lessons for simplification.

---

## What Indicates Missing Gates

Signals that approval or readiness gates are implicit, skipped, or contradictory:

| Signal | Meaning |
|--------|---------|
| LRC reached `approved` without FWCP at `approved` / `production-ready` | FWCP gate bypass — **FAIL** |
| PPC review treated semantic pack as landing SoT | Pre-LRL failure mode reproduced — **FAIL** |
| `approved` set with Section 5 alignment = `fail` | Contract rule violated — **FAIL** |
| `partial` alignment combined with `approved` without operator variance note | Gate rule violated — **FAIL** |
| URL changed after LRC approval without contract update | Drift gate missing in operator habit — **PARTIAL** |
| No human named on `status_updated_by` / sign-off fields | HITL gate missing — **FAIL** |
| PACK-STATUS promoted without live page re-check | Capture gate weak — **PARTIAL** |
| Export or ad work started before LRC `approved` | PPC gate bypass — out of scope / **FAIL** if occurred |

---

## What Indicates Source-Specific Assumptions

Signals that v1 docs or operator behavior still assume Website Factory or Triumph patterns:

| Signal | Indicator |
|--------|-----------|
| Factory handoff docs opened as required path | Factory treated as universal dependency |
| Semantic lock or MODE 1 steps applied | Factory-only contract invoked |
| Operator waits for Factory dist before FWCP | Wrong source workflow |
| LRC fields like `factory_handoff_ref` marked required | Source-specific shape leak |
| Triumph URL registry workflow assumed mandatory | Triumph-scale pattern forced on Makita |
| Exporter URL replacement habit used instead of LRC URL section | Pre-LRL battle pattern |
| `copy_pack_export` method assumed available | Factory-specific capture assumed default |
| WPilot or other future source vocabulary used without charter | Premature source expansion |

**Interpretation:** Any **confirmed** Factory-required assumption for Makita route → architectural validation **FAIL** for A1.

---

## Success Conditions

Pilot outcome **PASS** when **all** apply:

1. **Chain complete:** Phases 1–4 executed for one Makita route (Phase 5 evaluation done).
2. **Architecture validated:** Minimum items A1, A2, A3, A4, A6, A7 (see above) satisfied with evidence.
3. **Artifacts exist:**
   - Approved FWCP at `artifacts/landing-readiness/copy-pack-<route_id>-v1/`
   - LRC at `approved` at `artifacts/landing-readiness/lrc-<route_id>-v1.md`
4. **No gate bypass:** No FAIL signals in [Missing Gates](#what-indicates-missing-gates).
5. **No Factory dependency:** No source-specific Factory assumption signals confirmed.
6. **Observations captured:** ≥3 observation log entries (any severity) documenting friction or confirmation.
7. **Human sign-off:** Named operator attests evaluation in Phase 5 session log.

**PARTIAL PASS** allowed when:

- Chain complete but **≤2** Medium complexity or missing-field signals remain documented, AND
- No FAIL gate bypass, AND
- Architecture items A1 and A2 satisfied.

---

## Failure Conditions

Pilot outcome **FAIL** when **any** apply:

| Code | Condition |
|------|-----------|
| F1 | FWCP or LRC not produced for pilot route |
| F2 | LRC `approved` without approved FWCP |
| F3 | Landing truth taken from semantic pack alone (live verification skipped) |
| F4 | `landing_source` not `existing_client_website` or Factory path required to proceed |
| F5 | Required LRC gate violated (`approved` with alignment fail, anonymous approval, etc.) |
| F6 | PPC export / ad / keyword work performed under guise of readiness review |
| F7 | Operator cannot complete contract without undeclared v1 doc changes (critical defect — document separately) |
| F8 | Phase aborted with no recoverable artifacts and no documented blocker resolution path |

**FAIL does not invalidate LRL v1 architecture by default** — it may indicate pilot execution error, missing operator prep, or documentation defect. Classify in lessons.

---

## Outcome Matrix

| Outcome | Meaning | Typical next step |
|---------|---------|-------------------|
| **PASS** | LRL v1 viable for `existing_client_website`; evidence supports limited post-pilot expansion | Charter PPC `lrc_ref` field naming; optional second route |
| **PARTIAL** | Chain works but friction / ambiguity documented | Targeted doc clarification charter (not redesign); second pilot route |
| **FAIL** | Gate bypass, Factory dependency, or incomplete chain | Root-cause review; fix execution or document critical defect; re-pilot |

---

## Lessons-Captured Section

*(Populate during Phase 5 — do not pre-fill.)*

### Pilot metadata

| Field | Value |
|-------|-------|
| `pilot_id` | makita-lrl-pilot-v1 |
| `evaluation_date` | |
| `evaluator` | |
| `route_id` | |
| `project_id` | |
| `outcome` | PASS / PARTIAL / FAIL |

### What worked

1.
2.
3.

### Friction and ambiguity

1.
2.
3.

### SAFE UNKNOWN discovered

1.
2.

### Recommended post-pilot actions (human decision)

| Priority | Action | Architecture change? |
|----------|--------|----------------------|
| | | no — charter only |
| | | |

### Deferred per LRL v1 (do not expand without evidence)

- Formal `landing_source` taxonomy doc
- Dedicated LRL approval-gates checklist
- Machine-readable LRC schema
- Capture helper scripts
- Triumph route migration to explicit LRCs

---

## Related Documents

- [makita-lrl-pilot-v1.md](makita-lrl-pilot-v1.md) — execution plan
- [makita-lrl-observation-log-v1.md](makita-lrl-observation-log-v1.md) — live friction log
- [makita-lrl-preflight-review-v1.md](makita-lrl-preflight-review-v1.md) — pre-pilot risk review
- [landing-readiness-layer-v1.md](../intelligence/landing-readiness-layer-v1.md)

## Boundary

Evaluation rubric only. **No** scoring automation. **No** modification of LRL foundation docs from this file.
