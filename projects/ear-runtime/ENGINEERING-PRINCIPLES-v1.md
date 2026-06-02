# EAR Runtime Engineering Principles v1

**Type:** Operational principles for runtime engineering  
**Date:** 2026-06-02  
**Charter:** [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md)  
**MARS discipline:** [AGENTS.md](../../AGENTS.md) — SAFE UNKNOWN, status honesty

---

## Purpose

Principles govern **all** EAR Runtime engineering work — planning, implementation, and pilot execution. They apply before code is written and remain binding after.

---

## Core principles

### 1. Human operated

Every acquisition session, validation step, and publish action is **initiated and approved by a human operator**. Runtime helpers assist; they do not replace HITL gates defined in architecture.

### 2. Read-only first

v1 scope is **Mode 2 Connected Read-Only**. Connectors must not write, delete, or mutate remote resources. Write connectors and Mode 3 require architecture amendment and separate charter.

### 3. SAFE UNKNOWN

If evidence is missing, incomplete, or unverifiable, runtime outputs must **honestly mark** gaps — not fill them with assumptions. Aligns with MARS status honesty and architecture snapshot quality mapping.

### 4. Snapshot before analysis

Consumers receive **published snapshots** — not raw connector output. Runtime must preserve the evidence → validate → snapshot → publish pipeline; consumers must not bypass it.

### 5. Evidence before claims

No quality level, completeness claim, or consumer-ready assertion without corresponding evidence in the Evidence Package. Candidate snapshots document exclusions and gaps per spec.

### 6. No hidden writes

Runtime helpers must not perform undeclared filesystem, network, or remote mutations. All side effects are explicit, logged, and within chartered scope.

### 7. No autonomous actions

No unattended acquisition, auto-publish, auto-validate, or scheduled production runs without separate ops charter and explicit human authorization. Fail closed on ambiguity.

---

## Additional principles

### 8. Architecture conformance

Runtime implements architecture contracts — it does not redefine them. Normative changes require **Architecture Amendment Charter**, not runtime PRs or README drift.

### 9. Credential boundary

Runtime uses `credential_ref` only. Raw passwords, private keys, and session secrets **never** enter git-bound artefacts. Credential resolution is operator-bound and external to repository.

### 10. Fail closed

On connector failure, validation failure, or gate ambiguity — **stop and log**. Do not proceed to publish or claim success. Per [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md).

### 11. Separation of layers

Acquisition mechanics stay in runtime. Consumer analysis (OCPilot diffs, Factory deployment) stays in consumer programs. No cross-layer logic leakage.

### 12. Status honesty

Backlog existence, charter approval, and planning completion **do not** imply implementation exists. [EAR-RUNTIME-STATE.md](EAR-RUNTIME-STATE.md) is the authoritative honesty record.

### 13. Pilot discipline

Pilot execution requires **Execution Authorization** separate from engineering charter. Architecture pilot packages define governance; runtime `pilots/` holds execution artefacts only when authorized.

### 14. Minimal scope per change

Each engineering change addresses one chartered backlog item or explicit sub-task. Avoid scope creep via "small additions" that bypass charter or architecture gates.

### 15. Inspectability

All runtime outputs (evidence, candidate snapshots, validate reports, publish logs) must be **human-inspectable** without proprietary tooling. Prefer plain formats (JSON, text logs, directory trees).

---

## Principle application matrix

| Stage | Primary principles |
|-------|-------------------|
| Planning | Architecture conformance, status honesty, minimal scope |
| R1 connector | Read-only first, credential boundary, fail closed, no hidden writes |
| R2 evidence | Evidence before claims, SAFE UNKNOWN, inspectability |
| R3 snapshot | Evidence before claims, SAFE UNKNOWN, snapshot before analysis |
| R5 validate | Human operated, fail closed, no autonomous actions |
| R4 publish | Human operated, fail closed, snapshot before analysis |
| Pilot execution | Pilot discipline, human operated, all principles |

---

## Truth statement

Principles are binding from engineering charter approval. **No** principle is enforced by automated tooling at this stage — human discipline and future implementation design must embody them.
