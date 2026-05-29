# ORCA LRL Pilot — Observation Log Template v1

## Status

**REUSABLE TEMPLATE** — structured observation log for Landing Readiness Layer pilots (2026-05-30).

First instance: Makita LRL pilot (`makita-lrl-pilot-v1`). Copy structure for future pilots; replace pilot metadata per session.

**Not** automated telemetry. **Not** incident registry. **Not** governance audit.

## Purpose

Capture **structured operational observations** during LRL pilot execution — friction, gaps, ambiguities, and confirmed patterns — without redesigning architecture mid-flight.

---

## Pilot Metadata (update per pilot)

| Field | Makita instance | Future pilot |
|-------|-----------------|--------------|
| `pilot_id` | makita-lrl-pilot-v1 | `<pilot-id>` |
| `project_id` | *(confirm at intake)* | |
| `landing_source` | `existing_client_website` | |
| `operator` | | |
| `session_dates` | | |
| `execution_plan_ref` | [makita-lrl-pilot-v1.md](makita-lrl-pilot-v1.md) | link to plan |

---

## How To Use

1. Append one **Observation Entry** per notable event (confusion, blocker, confirmation, workaround).
2. Log during execution — not only at end of session.
3. One observation per entry; split compound issues.
4. Link to phase in execution plan when applicable.
5. Do **not** fix architecture in this log — record **Suggested change** for post-pilot charter.
6. Severity guides evaluation; does not auto-trigger halt unless operator decides.

### Severity Guide

| Level | Meaning |
|-------|---------|
| **S1 — Blocker** | Cannot proceed without resolution or explicit SAFE UNKNOWN acceptance |
| **S2 — Major** | Proceed with workaround; likely affects PASS/PARTIAL outcome |
| **S3 — Minor** | Friction only; document for lessons |
| **S4 — Info** | Positive confirmation or neutral note |

---

## Observation Entry Template

Copy block below for each entry.

---

### Entry `<NNN>`

| Field | Value |
|-------|-------|
| **Date / time** | |
| **Phase** | 1 Intake · 2 FWCP · 3 LRC · 4 PPC review · 5 Evaluation |
| **Observer** | |

#### Observation

*(What happened? Factual, specific — artifact path, field name, doc section.)*

#### Problem

*(What went wrong or what was unclear? Use "none" for S4 confirmations.)*

#### Impact

*(What decision, gate, or artifact was affected?)*

#### Severity

S1 · S2 · S3 · S4

#### Suggested change

*(Post-pilot charter only — doc clarification, checklist, helper, training note. Not an in-session redesign.)*

#### Architecture affected

*(Check all that apply; add note.)*

- [ ] LRL layer ([landing-readiness-layer-v1.md](../intelligence/landing-readiness-layer-v1.md))
- [ ] FWCP artifact ([final-website-copy-pack-v1.md](../intelligence/final-website-copy-pack-v1.md))
- [ ] LRC contract ([landing-ready-contract-v1.md](../intelligence/landing-ready-contract-v1.md))
- [ ] Project structure ([project-structure-contract-v0.md](../projects/project-structure-contract-v0.md))
- [ ] PPC layer / export gates (consumer — no change in pilot)
- [ ] Website Factory bridge (should **not** apply for `existing_client_website`)
- [ ] Operator procedure / execution plan only
- [ ] None — informational
- [ ] Other: |

#### Evidence refs (optional)

*(Path to screenshot, session log line, artifact snippet.)*

---

## Makita Pilot — Live Entries

*(Append below during pilot execution.)*

---

### Entry `001`

| Field | Value |
|-------|-------|
| **Date / time** | *(pilot day)* |
| **Phase** | — |
| **Observer** | |

#### Observation

Preflight preparation complete. Makita LRL pilot execution plan, success criteria, and observation template created. No Makita site analysis performed.

#### Problem

none

#### Impact

Pilot can start tomorrow with defined phases and evaluation rubric.

#### Severity

S4

#### Suggested change

Confirm `project_id` slug at Phase 1 intake before creating artifact folders.

#### Architecture affected

- [x] Operator procedure / execution plan only

#### Evidence refs (optional)

- [makita-lrl-pilot-v1.md](makita-lrl-pilot-v1.md)
- [makita-lrl-success-criteria-v1.md](makita-lrl-success-criteria-v1.md)
- [makita-lrl-preflight-review-v1.md](makita-lrl-preflight-review-v1.md)

---

## Session Summary Block (end of pilot)

*(Complete in Phase 5.)*

| Metric | Count |
|--------|-------|
| Total entries | |
| S1 blockers | |
| S2 major | |
| S3 minor | |
| S4 info | |
| Factory-assumption signals | |
| Gate bypass signals | |

**Top 3 themes:**

1.
2.
3.

**Cross-reference:** [makita-lrl-success-criteria-v1.md](makita-lrl-success-criteria-v1.md) Lessons-captured section.

---

## Reuse Notes (future pilots)

When starting a new LRL pilot:

1. Duplicate this file or create `<project>-lrl-observation-log-v1.md` using the same entry template.
2. Update Pilot Metadata table.
3. Clear Live Entries section (keep Entry 001 preflight pattern optional).
4. Keep **Observation / Problem / Impact / Severity / Suggested change / Architecture affected** fields unchanged for cross-pilot comparison.

## Boundary

Observation log only. **No** architecture edits. **No** defect fixes in foundation docs from this file.
