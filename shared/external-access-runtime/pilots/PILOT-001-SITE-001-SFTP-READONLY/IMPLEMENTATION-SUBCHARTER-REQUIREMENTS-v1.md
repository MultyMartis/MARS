# PILOT-001 — Implementation Sub-Charter Requirements v1

**Type:** Requirements checklist only — **not** an Implementation Sub-Charter, **not** implementation, **not** execution  
**Phase:** 5 — Implementation Readiness Review (CONDITIONAL GO output)  
**Date:** 2026-06-01  
**Pilot ID:** `PILOT-001`  
**Prerequisite decision:** [IMPLEMENTATION-READINESS-REVIEW-v1.md](IMPLEMENTATION-READINESS-REVIEW-v1.md) — **CONDITIONAL GO**

**Purpose:** Document exactly what must exist **before** a human operator may **authorize** an Implementation Sub-Charter for PILOT-001. Satisfying this list is necessary for sub-charter approval; it does **not** authorize writing connector code or performing live access until the sub-charter itself is approved and Execution is separately chartered.

---

## 1. Governance prerequisites

| # | Requirement | Source | Status at Phase 5 close |
|---|-------------|--------|-------------------------|
| G-01 | Pilot charter package complete (charter, success, stop, risk, status) | Phase 4 | **Met** |
| G-02 | Phase 5 Implementation Readiness Review = GO or CONDITIONAL GO | [PHASE-5-DECISION-v1.md](PHASE-5-DECISION-v1.md) | **Met** (CONDITIONAL GO) |
| G-03 | **Human Approval** recorded in [STATUS.md](STATUS.md) with approver id and date | [PILOT-GOVERNANCE-v1.md](../../PILOT-GOVERNANCE-v1.md) §5.1 | **Not met** — required before sub-charter authorization |
| G-04 | No stop conditions triggered | [STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md) | **Met** |
| G-05 | Explicit statement in sub-charter: charter ≠ implementation ≠ execution | Governance §2 | **Required in sub-charter text** |

---

## 2. Scope requirements (sub-charter must define)

| # | Requirement | Must include |
|---|-------------|--------------|
| S-01 | Connector class | **SFTP Read-Only** only — no scope creep to SSH, Hybrid, or Level 2+ |
| S-02 | Reference path | **CON-L1-A** per [EAR-CONNECTED-PATHS-v1.md](../../EAR-CONNECTED-PATHS-v1.md) |
| S-03 | Environment | **TEST** only — `site_id` SITE-001 |
| S-04 | Quality cap | Snapshot Level **1** honest maximum |
| S-05 | Implementation deliverables | Enumerate allowed artifacts (e.g. connector module location, helper scripts policy) — **human decision**; repo vs external tooling **SAFE UNKNOWN** until stated |
| S-06 | Non-deliverables | Restate charter §4 exclusions (no Mode 3, no prod, no OCPilot Run 5 completion claim) |

---

## 3. Credential requirements

| # | Requirement | Must include |
|---|-------------|--------------|
| C-01 | `credential_ref` | Operator-named external path or ref id — **no values** in git |
| C-02 | Store location | Align with [EAR-CREDENTIAL-BOUNDARY-v1.md](../../EAR-CREDENTIAL-BOUNDARY-v1.md) (e.g. operator `secrets/`) |
| C-03 | Read-only account plan | Dedicated read-only SFTP user **or** procedural read-only discipline + stop ST-13 if write-capable |
| C-04 | Rotation / exposure | Procedure if ST-10/11 triggered — outside MARS repo |
| C-05 | `operator_approver` | Named human id for Execution-stage HITL (may resolve charter G0 pending field) |

---

## 4. Storage and path requirements

| # | Requirement | Must include |
|---|-------------|--------------|
| P-01 | Evidence quarantine root | Absolute or operator-relative path for pre-redaction Evidence Package |
| P-02 | Bulk payload root | External bulk storage for large downloads per [EAR-STORAGE-MODEL-v1.md](../../EAR-STORAGE-MODEL-v1.md) |
| P-03 | Candidate snapshot workspace | Where Validate assembles pre-publish package |
| P-04 | Published snapshot reference | Consumer-visible location policy (OCPilot intake) |
| P-05 | Git exclusion | Confirm no secrets, dumps, or unredacted bulk in MARS git |

---

## 5. SFTP scope requirements (CON-L1-A)

| # | Requirement | Must include |
|---|-------------|--------------|
| F-01 | Remote root path | TEST site document root — operator-confirmed |
| F-02 | Approved path list / globs | Version proof files (`index.php`, `admin/index.php`, etc.) |
| F-03 | Exclusions | `cache/`, `logs/`, `sessions/`, large `image/` policy per charter risk R-11 |
| F-04 | Byte / file count limits | Prevent ST-24 bulk exfiltration |
| F-05 | Partial acquisition semantics | Connector `partial` + `safe-unknown` per [EAR-CONNECTOR-CONTRACT-v1.md](../../EAR-CONNECTOR-CONTRACT-v1.md) |
| F-06 | Channel preflight | Operator attestation: SFTP available (or documented fail → stop ST-21) |

---

## 6. Validation and evidence requirements

| # | Requirement | Must include |
|---|-------------|--------------|
| V-01 | Validate owner | Human who signs G1–G4 manual Validate |
| V-02 | Level 1 checklist | From [EAR-OPENCART-QUALITY-MAPPING-v1.md](../../EAR-OPENCART-QUALITY-MAPPING-v1.md) + [SUCCESS-CRITERIA-v1.md](SUCCESS-CRITERIA-v1.md) |
| V-03 | Evidence vs snapshot | Per [EAR-EVIDENCE-PACKAGE-v1.md](../../EAR-EVIDENCE-PACKAGE-v1.md) |
| V-04 | Redaction plan | `config.php` and sensitive paths — item 17 of [EAR-OPENCART-READINESS-CHECKLIST-v1.md](../../EAR-OPENCART-READINESS-CHECKLIST-v1.md) |
| V-05 | Waived risks register | Copy or reference pilot R-12 and any sub-charter-specific waivers |

---

## 7. Safety and stop-condition requirements

| # | Requirement | Must include |
|---|-------------|--------------|
| X-01 | Incorporate [STOP-CONDITIONS-v1.md](STOP-CONDITIONS-v1.md) by reference | ST-01–ST-24 |
| X-02 | Fail-closed publish | No publish on ST trigger or inflated level |
| X-03 | Implementation boundary | ST-17 — no live access without Execution authorization |
| X-04 | Acquisition log fields | Channel, scope, `acquisition_id`, timestamps (SC-17) |

---

## 8. Consumer handoff requirements

| # | Requirement | Must include |
|---|-------------|--------------|
| H-01 | Consumer | OCPilot — Level 1 intake per [EAR-OPENCART-CONSUMER-GUIDE-v1.md](../../EAR-OPENCART-CONSUMER-GUIDE-v1.md) |
| H-02 | Run 5 honesty | Resume prerequisites stated; **no** claim Run 5 complete |
| H-03 | Metadata | `environment: TEST`, `site_id: SITE-001`, baseline `ocstore-3038-rs2` |

---

## 9. Authorization block (sub-charter document tail)

The Implementation Sub-Charter artifact (future) must end with explicit human sign-off table:

| Role | Authorizes | Does not authorize |
|------|------------|-------------------|
| Human charter authority | Implementation scope (code/access **plan**) | Execution, live SFTP, publish |
| Operator technical lead | Path/credential/storage bindings | Production, Mode 3 |

**Execution** requires: approved sub-charter + separate Execution authorization + preflight per checklist.

---

## 10. Checklist summary (operator use)

Before signing Implementation Sub-Charter authorization:

- [ ] G-03 Approval recorded in STATUS
- [ ] G-01–G-05 governance items satisfied
- [ ] S-01–S-06 scope bound to CON-L1-A / L1 / TEST
- [ ] C-01–C-05 credential refs named (no secrets in git)
- [ ] P-01–P-05 storage paths named
- [ ] F-01–F-06 SFTP scope documented
- [ ] V-01–V-05 validation ownership clear
- [ ] X-01–X-04 stop conditions incorporated
- [ ] H-01–H-03 consumer handoff honest

---

## 11. Truth statement

| Claim | Accurate? |
|-------|-----------|
| This file is an Implementation Sub-Charter | **No** — requirements only |
| Implementation authorized by this file | **No** |
| All requirements met today | **No** — G-03 and operator paths pending |
