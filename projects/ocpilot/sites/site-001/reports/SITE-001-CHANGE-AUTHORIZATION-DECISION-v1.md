# SITE-001 Change Authorization Decision v1

**Type:** Operator decision record — Phase 1 Brand Replacement  
**Date:** 2026-06-07  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST** only  
**Review:** [SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md)

---

## Decision

| Field | Value |
|-------|-------|
| **Question** | Is SITE-001 (TEST) authorized to begin Phase 1 — **Hmelnickiy → SIBKAR Brand Replacement** — first real modification cycle? |
| **Outcome** | **NOT AUTHORIZED** |
| **Scope of denial** | All write operations: files, database, admin changes, logo upload, theme edits, cache/modification refresh on live TEST |
| **Scope still allowed** | Read-only discovery (W0); checklist preparation; documentation; operator-supervised evidence collection per [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) *if separately sessioned* |
| **Re-decision trigger** | Pre-execution checklist **C-01..C-11** in review §6 — all **PASS** → eligible for **AUTHORIZED WITH NOTES** (decision v1.1) |

---

## Rationale

1. **Write gates closed** — [project-access-brief.md](../project-access-brief.md) explicitly forbids file edits, DB edits, theme edits, and admin changes. [AUDIT-CHARTER.md](../AUDIT-CHARTER.md) authorizes **read-only** work only.

2. **No pre-change evidence** — Run 5 initialization found no site snapshot, file manifest, or brand inventory ([RUN-5-FIRST-FINDINGS.md](RUN-5-FIRST-FINDINGS.md); blockers B-EV-01..04). First write without grep baseline creates high leftover-brand risk.

3. **Incomplete target pack** — SIBCAR legal entity is attested (LE-0005 / EV-W1C-CC-01), but **phones and messengers are SAFE UNKNOWN**; logo assets are not staged; old-brand on-site variants are not documented in repo.

4. **Backup insufficient for write** — Operator-claimed Beget backup dated **2026-05-31** is planning input only; restorability not verified; fresh backup required immediately before W1.

5. **No change control artefacts** — Change Request and Rollback Plan instances do not exist.

6. **EAR dry run does not apply** — EAR Dry Run **PASS WITH NOTES** (2026-06-07) covers mock acquisition pipeline only; it does **not** authorize CMS content modification.

**NOT AUTHORIZED** (not **AUTHORIZED WITH NOTES**): multiple **P0** blockers remain; incremental execution is viable **after** checklist, but starting modification now would violate OCPilot safety boundaries.

---

## Conditions not satisfied

| ID | Condition | Status |
|----|-----------|--------|
| C-DEC-01 | Write permission on TEST — access brief | **NOT SATISFIED** |
| C-DEC-02 | Brand Replacement Pack v1 approved | **NOT SATISFIED** |
| C-DEC-03 | Old-brand search baseline | **NOT SATISFIED** |
| C-DEC-04 | Logo assets staged | **NOT SATISFIED** |
| C-DEC-05 | Complete contact set (phone, messengers) | **NOT SATISFIED** |
| C-DEC-06 | Fresh backup + restore acknowledgment | **NOT SATISFIED** |
| C-DEC-07 | Change Request + Rollback Plan | **NOT SATISFIED** |
| C-DEC-08 | Pre-change evidence (screenshots, settings export) | **NOT SATISFIED** |
| C-DEC-09 | Theme / extension inventory (W0) | **NOT SATISFIED** |

---

## Conditions satisfied (planning only)

| ID | Condition | Status |
|----|-----------|--------|
| C-DEC-OK-01 | SITE-001 identified; TEST URL documented | **SATISFIED** |
| C-DEC-OK-02 | Baseline `ocstore-3038-rs2` approved | **SATISFIED** |
| C-DEC-OK-03 | Intake closed | **SATISFIED** |
| C-DEC-OK-04 | Legal entity source (Atlas E1 CC) for drafting | **SATISFIED** |
| C-DEC-OK-05 | External storage root exists | **SATISFIED** |
| C-DEC-OK-06 | Incremental wave plan documented | **SATISFIED** — review §Q7 |

---

## Gate record

| Gate | Before | After |
|------|--------|-------|
| Phase 1 Brand Replacement — execution on TEST | **NOT STARTED** | **NOT AUTHORIZED** |
| Phase 1 — pre-execution checklist | **NOT STARTED** | **IN PROGRESS** (operator) |
| Run 5 read-only audit | **paused** | **unchanged** |
| OCPilot write charter (site) | **NO** | **NO** |

---

## Authorized next steps

| Action | Authorized? |
|--------|-------------|
| Operator completes checklist C-01..C-11 (review §6) | **YES** |
| Read-only W0 discovery on TEST (supervised) | **YES** |
| Draft Brand Replacement Pack from CC + operator input | **YES** (docs/materials only) |
| Create Change Request + Rollback Plan drafts | **YES** (not execution) |
| First write on TEST (any wave W1+) | **NO** |
| FTP/DB/admin modification without updated brief | **NO** |
| Treat EAR dry run as write authorization | **NO** |

---

## Path to AUTHORIZED WITH NOTES (v1.1)

When **all** items below are true, program owner may sign **SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.1** as **AUTHORIZED WITH NOTES**:

1. Checklist C-01..C-10 **PASS** (evidence paths recorded externally).
2. Access brief updated: write on TEST **YES**; backup + rollback confirmed; named approver.
3. First modification session limited to **W1** (store settings only) unless operator expands charter in Change Request.
4. Supervised HITL session — no autonomous agent writes.
5. `# REPORT — SITE-001 Phase 1 W1 — Brand Replacement` required after first write session.

**Notes expected at authorization:** live version unverified; extension/ocMod surface may expand scope; SEO URL slug changes may remain as known leftovers unless explicitly in Change Request.

---

## Required questions (explicit answers)

| Question | Answer |
|----------|--------|
| **Can Phase 1 begin safely now?** | **NO** |
| **Can preparation begin now?** | **YES** — checklist and W0 read-only discovery |
| **Does this decision authorize FTP or deployment?** | **NO** |
| **Does this decision supersede AUDIT-CHARTER for writes?** | **NO** — write charter still required |
| **What must operator do first?** | Complete checklist §6 in review; then request decision v1.1 |

---

## Sign-off

| Role | Signature | Date |
|------|-----------|------|
| Program owner (Phase 1 decision) | _Pending_ | _Pending_ |
| Operator (acknowledgment) | _Pending_ | _Pending_ |
| Review author | `cursor-agent` | 2026-06-07 |

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-07 | **CREATED** — Phase 1 decision **NOT AUTHORIZED**; checklist path to v1.1 documented |

*SITE-001 Change Authorization Decision v1 — decision record only; no site modification performed.*
