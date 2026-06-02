# EAR Connected Acquisition v1

**Purpose:** Define **Connected Acquisition** (Model B) — read-only acquisition from **approved live channels** on actively managed projects.  
**Status:** architecture specification — **no** implementation, runtime, or connectors.  
**Phase:** 2E  
**Parent:** [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md)  
**Connector layer:** [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md) (Phase 2D)

---

## Mission

Produce a governed **Snapshot Package** by acquiring read-only evidence from **chartered external systems** (SFTP, SSH, phpMyAdmin metadata, OpenCart Admin read paths, future WordPress channels) under operator HITL, using the Phase 2D connector model: **Connector → Evidence Package → EAR Validation → Snapshot**.

**Managed Project philosophy:** Connected acquisition targets **long-lived operational projects** — recurring snapshots, stable `site_id`, maintained credentials outside git, and repeatable channel scope. Examples: **SITE-001**, **BZPM**, future dealership and support engagements.

---

## Inputs

| Input class | Examples | Operator responsibility |
|-------------|----------|-------------------------|
| **Channel charter** | Approved channels, paths, exclusions | HITL at Request |
| **Target scope** | Site root, extension dirs, DB metadata-only | Document in Request |
| **`credential_ref`** | External secret store pointer | Per [EAR-CREDENTIAL-BOUNDARY-v1.md](EAR-CREDENTIAL-BOUNDARY-v1.md) |
| **Connector plan** | Single or Hybrid (SFTP + PMA + Admin) | Align [EAR-SNAPSHOT-MAPPING-v1.md](EAR-SNAPSHOT-MAPPING-v1.md) |
| **Platform spec** | OpenCart snapshot spec, future WP spec | Validate mapping |

**EAR mode:** **Mode 2** (Connected Read Only) per [EAR-MODES-v1.md](EAR-MODES-v1.md).

**Implementation status:** Mode 2 connectors are **specified, not implemented** at Phase 2E freeze. Connected acquisition **architecture** is complete; **runtime** requires Phase 3 assessment + explicit pilot charter.

---

## Outputs

| Output | Description |
|--------|-------------|
| **Evidence Package** | Transient acquisition artifact per [EAR-EVIDENCE-PACKAGE-v1.md](EAR-EVIDENCE-PACKAGE-v1.md) |
| **Candidate snapshot** | After EAR Validation maps evidence → sections |
| **Published snapshot** | Operator-approved Publish |
| **`acquisition-log`** | Channel entries, scope, `acquisition_id`, partial/failed legs |
| **Connector status** | `success` | `partial` | `failed` per [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md) |

---

## Expected snapshot levels

Connected paths are designed for **repeatable** Level 2–3 when channels and scope are confirmed. Nothing is guaranteed — Validate and honesty rules apply.

| Typical connector plan | Achievable level (honest) | Reference |
|------------------------|---------------------------|-----------|
| SFTP narrow (version + root list) | **1** | Connected L1-B |
| SFTP + PMA metadata | **1–2** | Connected L1-E, L2-B |
| SFTP + PMA + Admin (hybrid coordinator) | **2–3** | Connected L3-B |
| SSH comprehensive | **2–3** | Connected L3-A |

Canonical paths: [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md). OpenCart detail: [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md), [EAR-MODE-2-OPENCART-REFERENCE-v1.md](EAR-MODE-2-OPENCART-REFERENCE-v1.md).

---

## Strengths

| Strength | Benefit |
|----------|---------|
| **Repeatability** | Same scope policy → comparable snapshots |
| **Structured provenance** | `acquisition-log` with channel and timestamps |
| **Lower operator toil** (when runtime exists) | Recurring audits without re-export |
| **Path to Level 3** | Hybrid coordinator for OpenCart comprehensive manifest |
| **Aligns with SITE-001 reality** | Multiple channels available per project brief |

---

## Weaknesses

| Weakness | Mitigation (process) |
|----------|----------------------|
| **Credential dependency** | `credential_ref` required; fail closed without secrets |
| **Runtime not yet available** | Mode 0/1 Offline fallback until pilot |
| **Host variability** | Partial acquisition + `safe-unknown` per DD-2D-07 |
| **Over-collection risk** | Scope limits in charter; Validate rejects policy violations |
| **False “live truth”** | Snapshot remains point-in-time; consumers must not silent re-fetch |

---

## Typical use cases

| Use case | Why connected |
|----------|---------------|
| SITE-001 OCPilot Run 5 (chartered) | Active test site; channels in access brief |
| BZPM / dealership support | Ongoing maintenance; recurring snapshots |
| Extension inventory refresh | Scoped Connected re-acquisition after Level 1 |
| Level 3 comprehensive audit | SFTP + PMA + Admin hybrid |
| Future WPilot WordPress sites | Same track; platform connectors TBD |

---

## Managed Project (normative)

1. **Register `site_id`** in consumer registry before first Connected Request.
2. **Maintain channel charter** — which connectors allowed; review on hosting change.
3. **Rotate credentials outside git** — never embed in snapshot or reports.
4. **Plan recurring snapshots** — new `snapshot_id` per cycle; consumer compares explicitly.
5. **HITL on every Acquire session** — no autonomous scheduled acquisition in EAR v1 architecture.

---

## Connector alignment (Phase 2D)

Connected acquisition **must** use connector classes from [EAR-CONNECTOR-TYPES-v1.md](EAR-CONNECTOR-TYPES-v1.md). Consumers **must not** invoke connectors directly (DD-2D-01, DD-2E-04).

```
Operator HITL
  → Connector(s) read-only
  → Evidence Package
  → EAR Validate
  → Publish
  → Consumer
```

---

## When Connected is inappropriate

| Situation | Prefer |
|-----------|--------|
| No credentials and no charter | Offline |
| One-time archive-only audit | Offline |
| Write/deploy/migration | Non-EAR change process |
| Connector runtime not approved | Offline Mode 0/1 until charter |

See [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md).

---

## SAFE UNKNOWN

- First production connector class (SFTP vs ZIP Intake) — Phase 3 Connected Acquisition Pilot Charter.
- Scheduled recurring acquisition without operator present — **forbidden** in v1 architecture unless future charter explicitly allows supervised automation.
- WordPress connected channel catalog — WPilot Phase TBD.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md) | Canonical connected paths |
| [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md) | Failure taxonomy |
| [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | SITE-001 theoretical options |
