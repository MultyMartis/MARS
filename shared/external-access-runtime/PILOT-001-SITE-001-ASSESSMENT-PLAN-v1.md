# PILOT-001 — Assessment Plan v1

**Pilot ID:** `PILOT-001`  
**Target:** `SITE-001` — SFTP Read-Only — Connected Acquisition  
**Type:** Assessment plan only — **no execution**, **no access**, **no connector code**  
**Date:** 2026-06-01  
**Prerequisite:** [pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md)

---

## 1. Purpose

Define **what evidence** would be collected at Assessment, **what success and failure look like**, and **what remains SAFE UNKNOWN** before any Execution is chartered — so assessors and operators share the same bar without performing acquisition in this phase.

---

## 2. Assessment scope

| In scope | Out of scope |
|----------|--------------|
| Judgment vs [SUCCESS-CRITERIA-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/SUCCESS-CRITERIA-v1.md) | Live SFTP in Phase 4 |
| Architecture traceability (Charter-stage criteria) | Level 2/3 publish |
| Future execution evidence checklist | OCPilot full Run 5 audit completion |
| Honesty of `safe-unknown` usage | Production environment |
| Stop condition review | Implementation without sub-charter |

**Assessment stage entry:** Requires **Execution** completed under Implementation Sub-Charter — **not** available at Phase 4.

---

## 3. Expected evidence (if Execution were authorized)

### 3.1 Documentation evidence (Charter-stage — available now)

| Evidence ID | Artifact | Proves |
|-------------|----------|--------|
| E-DOC-01 | PILOT-CHARTER-v1 | Scope, G0, CON-L1-A path |
| E-DOC-02 | SUCCESS-CRITERIA + STOP-CONDITIONS | Bar for pass/halt |
| E-DOC-03 | RISK-REGISTER | Mitigations considered |
| E-DOC-04 | EAR-SNAPSHOT-MAPPING SFTP rows | Section mapping feasible |
| E-DOC-05 | EAR-OPENCART-QUALITY-MAPPING Level 1 | Minimum sections known |

### 3.2 Execution evidence (future — not collected in Phase 4)

| Evidence ID | Artifact | Proves |
|-------------|----------|--------|
| E-EX-01 | Operator preflight record | TEST host, SFTP channel confirmed |
| E-EX-02 | `credential_ref` audit | No secrets in git |
| E-EX-03 | Evidence Package tree | SFTP acquisition output |
| E-EX-04 | `acquisition-log` | Channel, scope, timestamps, partial legs |
| E-EX-05 | Connector status record | `success` / `partial` / `failed` |
| E-EX-06 | Candidate snapshot (pre-publish) | Level 1 sections + `safe-unknown` |
| E-EX-07 | Validate checklist signed | Human Validate per gates |
| E-EX-08 | Publish record (if publish occurs) | Operator HITL |
| E-EX-09 | Redaction review | No secrets in consumer package |
| E-EX-10 | Consumer handoff note | OCPilot intake path documented |

---

## 4. What success would look like

### 4.1 Charter-stage success (Phase 4 — current)

| Criterion | Success signal |
|-----------|----------------|
| Pilot package complete | All pilot folder artifacts present |
| Governance linked | PILOT-GOVERNANCE + OPERATIONAL-INDEX Phase 4 DONE |
| Architecture traceability | CON-L1-A → Level 1 mapping documented without contradiction |
| No false claims | No runtime, execution, or Run 5 completion stated |

**Phase 4 assessment verdict:** **CHARTER COMPLETE** (documentation) — distinct from Execution assessment.

### 4.2 Execution-stage success (future)

| Criterion | Success signal |
|-----------|----------------|
| SC-01–SC-18 | Met per [SUCCESS-CRITERIA-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/SUCCESS-CRITERIA-v1.md) |
| Level 1 honest | Version proof + file-manifest substantiated or explicit `safe-unknown` |
| Read-only | No stop conditions triggered |
| Consumer-ready path | Published snapshot (if publish approved) matches OCPilot Level 1 intake |

**Overall verdict options:** PASS | CONDITIONAL PASS | FAIL | NOT ASSESSED

**Theoretical success (minimal SFTP-only):** Level 1 with `database-metadata`, `theme-info`, or `seo-structure` in `safe-unknown` — **valid** if documented and consumer gates respected.

---

## 5. What failure would look like

| Failure mode | Observable signal | Verdict |
|--------------|-------------------|---------|
| **Architectural contradiction** | SFTP path cannot map to required sections even with `safe-unknown` honesty | FAIL (Charter review) |
| **Stop triggered** | Any ST-* in [STOP-CONDITIONS-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/STOP-CONDITIONS-v1.md) | FAIL / HALTED |
| **Inflated level** | Level 2+ claimed from SFTP-only | FAIL |
| **Secret leak** | Credentials in git or snapshot | FAIL + security escalation |
| **Channel unavailable** | SFTP blocked; no honest Offline fallback chartered | FAIL or track change |
| **Incomplete manifest** | No version proof path; publish attempted at L1 | FAIL |
| **False readiness** | Stakeholders told “runtime shipped” | FAIL (governance) |
| **Execution without sub-charter** | Live access occurred | FAIL (process) |

**CONDITIONAL PASS example:** SFTP works; Level 1 with DB deferred via `safe-unknown`; follow-up PMA leg **not** in PILOT-001 scope — document for OCPilot.

---

## 6. Assessment procedure (future)

```
1. Confirm pilot at Execution complete (STATUS)
2. Collect evidence E-EX-01 … E-EX-10
3. Score each SC-* (pass / fail / n/a)
4. Review stop condition log
5. Review risk register residuals
6. Draft verdict + rationale
7. Human assessor sign-off (HITL)
8. Update LESSONS-LEARNED.md
9. Report: # REPORT — PILOT-001 Assessment
```

**Assessor:** Human operator — not autonomous agent sign-off for publish or security.

---

## 7. SAFE UNKNOWN (assessment-relevant)

| Unknown | Why it matters | Would verify at |
|---------|----------------|-----------------|
| SFTP host, port, path root for SITE-001 TEST | Cannot pre-score Execution | Preflight |
| SFTP vs FTP only on Beget account | Channel selection | Operator hosting check |
| Read-only account availability | ST-13 risk | Provider policy |
| Backup ZIP usability vs live SFTP | Offline alternative | Separate charter |
| Quarantine/bulk absolute paths | Storage hygiene | Implementation Sub-Charter |
| Virus scan policy for downloads | Evidence handling | Sub-charter / ops |
| Automated validator availability | Validate consistency | Phase 5 |
| OCPilot Run 5 resume date | Project schedule | OCPilot lane |
| Machine-readable snapshot schema | Tooling | Phase 5+ |

**Phase 4 rule:** Unknowns are **listed**, not **filled** with assumptions.

---

## 8. Deliverables from Assessment (future)

| Deliverable | Location |
|-------------|----------|
| Assessment report | Operator REPORT in chat or `projects/` per MARS discipline |
| Verdict | [STATUS.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) |
| Lessons | [LESSONS-LEARNED.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/LESSONS-LEARNED.md) |
| EAR doc updates | Only if architecture gap found — governed edit |

---

## 9. Current status

| Field | Value |
|-------|-------|
| Assessment executed | **No** |
| Phase 4 assessment | **CHARTER COMPLETE** (documentation only) |
| Execution evidence | **None expected** |

---

## 10. Cross-references

| Document | Use |
|----------|-----|
| [PILOT-CHARTER-v1.md](pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) | Scope |
| [PILOT-GOVERNANCE-v1.md](PILOT-GOVERNANCE-v1.md) | Boundaries |
| [EAR-RUNTIME-READINESS-ASSESSMENT-v1.md](EAR-RUNTIME-READINESS-ASSESSMENT-v1.md) | Phase 3 baseline |
