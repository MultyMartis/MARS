# EAR OpenCart Readiness Checklist v1

**Purpose:** Human-operated checklist **before** acquisition (Request stage completion / Acquire gate).  
**Status:** design only — items are **not** auto-verified; operator and EAR document outcomes.  
**Phase:** 2C

**Usage:** Copy or reference per acquisition cycle. Do **not** assume completion without explicit operator attestation.

---

## Checklist

| # | Item | Owner | Pass criteria | If fail |
|---|------|-------|---------------|---------|
| 1 | **Scope approved** | Operator | Charter or Run reference authorizes SITE, read-only, consumer | Stop — no Acquire |
| 2 | **Mode selected** | Operator | EAR Mode 0, 1, or 2 documented; Mode 3 **not** selected | Stop |
| 3 | **Target snapshot level selected** | Operator | Quality target 0–3 recorded in Request | Stop |
| 4 | **Acquisition path selected** | Operator + EAR | Path ID from [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) or hybrid plan documented | Revise Request |
| 5 | **Channels identified** | Operator | Channel list matches path; connection types noted | Stop if channel unavailable |
| 6 | **Environment class confirmed** | Operator | TEST / PRODUCTION / STAGING recorded; matches charter | Stop if PRODUCTION without charter |
| 7 | **Consumer identified** | Operator | e.g. `ocpilot`, Run id, baseline ref | Stop |
| 8 | **Credentials available** | Operator | External secrets location; **not** in git | Defer Acquire or change path |
| 9 | **Read-only discipline acknowledged** | Operator | No write/install/SQL mutation; client read-only | Stop |
| 10 | **Backup status known** | Operator | Backup date/location recorded or SAFE UNKNOWN explicit | Document in metadata |
| 11 | **Storage available** | Operator | External bulk path for manifests/archives agreed | Stop if nowhere to place bulk |
| 12 | **Publish path defined** | Operator + EAR | Where published snapshot reference will live (consumer registry) | Stop before Publish |
| 13 | **Risk accepted** | Operator | Reviewed [EAR-OPENCART-RISK-MODEL-v1.md](EAR-OPENCART-RISK-MODEL-v1.md) for chosen channels | Stop or reduce scope |
| 14 | **SAFE UNKNOWN documented** | EAR | Expected gaps listed in Request (e.g. ocMod deferred) | Update plan |
| 15 | **HITL reference** | Operator | Approver id, charter link, forbidden actions | Stop |
| 16 | **Exclusions policy** | Operator + EAR | cache/logs/sessions/image bulk policy for manifest | Document in scope |
| 17 | **Secret redaction plan** | Operator | `config.php` and dumps handling | Stop if no plan |
| 18 | **Hybrid time window** (if hybrid) | Operator | Single acquisition window or stale-data note planned | Document in acquisition-log |
| 19 | **Prior snapshot** (if re-entry) | EAR | `prior snapshot reference` and scoped delta defined | Full re-Request |
| 20 | **Validate owner identified** | Operator | Who signs Validate / Publish | Stop |

---

## Gate alignment

| Checklist block | [EAR-READINESS-GATES-v1.md](EAR-READINESS-GATES-v1.md) |
|-----------------|--------------------------------------------------------|
| Items 1–7, 15 | G0 Request |
| Items 8–9, 16–18 | G1 Acquire readiness |
| Items 11–12 | G3 Store / G4 Publish prep |

---

## Minimal checklist (Level 0 only)

For emergency registration only:

- [ ] Scope approved (identity only)
- [ ] Mode selected
- [ ] Target level **0**
- [ ] Consumer identified
- [ ] SAFE UNKNOWN lists all non-acquired sections
- [ ] Publish path defined

---

## Post-checklist (not part of readiness — reminder)

| Stage | Document |
|-------|----------|
| Acquire | [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) |
| Validate | [EAR-OPENCART-QUALITY-MAPPING-v1.md](EAR-OPENCART-QUALITY-MAPPING-v1.md) |
| Publish | [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) |

---

## SAFE UNKNOWN

- Checklist tracking tool (issue template, JSON) — not standardized in-repo at Phase 2C.
- Whether all 20 items required for Mode 0 — operator may waive with charter note except items 1, 2, 3, 7, 14.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OPENCART-ACQUISITION-DESIGN-v1.md](EAR-OPENCART-ACQUISITION-DESIGN-v1.md) | Channel capabilities |
| [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | Example site |
