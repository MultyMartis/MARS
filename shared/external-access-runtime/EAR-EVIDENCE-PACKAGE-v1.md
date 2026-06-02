# EAR Evidence Package v1

**Purpose:** Define the **Evidence Package** — temporary acquisition artifact between connector output and EAR validation / snapshot assembly.  
**Status:** architecture specification only — **no** schemas, storage layout, or code.  
**Phase:** 2D

---

## Position in the pipeline

```
Channel
    ↓
Connector
    ↓
Evidence Package    ← this document
    ↓
EAR Validation
    ↓
Snapshot Sections / Snapshot Package
```

The Evidence Package is **not** consumer input. It is **not** durable archive by default. It is **acquisition-internal** until validation promotes content into a governed snapshot.

---

## Definition

An **Evidence Package** is a bounded collection of **raw and semi-structured acquisition artifacts** plus **provenance metadata**, produced by one connector session (or merged by Hybrid Coordinator), consumed exclusively by **EAR Validation** during the **Acquire → Validate** boundary.

| Property | Meaning |
|----------|---------|
| **Temporary** | May be deleted or archived separately after successful publish; retention policy **SAFE UNKNOWN** until storage charter |
| **Pre-contract** | Not required to satisfy full snapshot section completeness |
| **Honest** | Carries connector warnings, partial flags, and scope echo |
| **May hold bulk** | Large files live in external quarantine; package holds refs |

---

## Evidence Package purpose

| Goal | Detail |
|------|--------|
| **Decouple acquisition from publication** | Connectors do not write snapshot shape directly |
| **Enable validation gate** | EAR checks contract, quality, redaction before Publish |
| **Preserve provenance** | Know which connector produced which artifact |
| **Support partial acquisition** | Failed legs do not silently become complete snapshots |
| **Quarantine risk** | Raw exports inspected before consumer visibility |

---

## Conceptual contents

| Category | Examples | Notes |
|----------|----------|-------|
| **Identity** | `acquisition_id`, `site_ref`, `connector_class` | Required |
| **Provenance** | `channel`, `started_at`, `completed_at`, `operator_approval_ref` | Required |
| **Scope echo** | Approved vs attempted paths/tables | Required |
| **Artifact index** | Logical list: manifest file, export sql, screenshots | Required |
| **Bulk references** | External paths to downloads, zip extract roots | Optional |
| **Connector status** | success / partial / failed | Required |
| **Errors and warnings** | Per [EAR-CONNECTOR-CONTRACT-v1.md](EAR-CONNECTOR-CONTRACT-v1.md) | Required when applicable |
| **Raw protocol artifacts** | Listings, hashes, export files | Channel-dependent |

**Forbidden at evidence stage (target policy):** Publishing to consumer bulk without validation pass.

---

## Evidence Package vs Snapshot Package

| Dimension | Evidence Package | Snapshot Package |
|-----------|------------------|------------------|
| **Audience** | EAR Validation (+ operator review) | Consumers (OCPilot, etc.) |
| **Lifecycle** | Acquire → Validate (then retire) | Store → Publish → Consume → Archive |
| **Shape** | Connector-oriented blobs + index | Contracted sections per Phase 2A |
| **Completeness** | May be partial | Must declare gaps in `safe-unknown` at publish |
| **Secrets** | May exist pre-redaction in quarantine | Must not contain secrets at publish |
| **Quality level** | Not certified | `package_quality_level` at publish |
| **Immutability** | Working artifact | Published snapshot treated as point-in-time evidence |

Validation **transforms** evidence into snapshot sections; it does not rename Evidence Package as Snapshot.

---

## Evidence Package vs Consumer Output

| Dimension | Evidence Package | Consumer Output |
|-----------|------------------|-----------------|
| **Producer** | Connector (+ Hybrid merge) | Consumer (e.g. OCPilot audit report) |
| **Consumer** | EAR Validation | Humans, tickets, knowledge base |
| **Content** | Raw/semi-raw site evidence | Findings, diffs, risk ratings |
| **EAR role** | Assembles snapshot from evidence | None — downstream of Publish |
| **Git** | External bulk only | Consumer repo rules |

Consumer output **must not** be confused with acquisition evidence — consumers do not feed back into Evidence Package except via a **new** acquisition cycle (operator-delivered files Mode 0).

---

## Hybrid merge semantics (conceptual)

When Hybrid Coordinator runs multiple connectors:

| Approach | Description |
|----------|-------------|
| **Single merged package** | One index with `leg_ref` per connector class |
| **Ordered package set** | Multiple evidence packages under one `acquisition_id` |

EAR Validation resolves contradictions per [EAR-CONNECTOR-FAILURES-v1.md](EAR-CONNECTOR-FAILURES-v1.md) — prefer corroborated file evidence over screenshot-only admin claims unless charter says otherwise.

---

## Storage placement (conceptual)

| Artifact | Typical location |
|----------|------------------|
| Evidence bulk | External quarantine / processing area — not git |
| Evidence index | Sidecar logical record — may live in processing store |
| Post-validation snapshot | Consumer registry bulk per [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) |

Exact folder names — **SAFE UNKNOWN** until Phase 3 storage charter.

---

## Workflow alignment

| Workflow stage | Evidence Package |
|----------------|------------------|
| Request | Not created |
| Acquire | Created / updated by connector |
| Validate | Read; mapped to sections; redaction enforced |
| Store | Snapshot stored; evidence may move to archive or delete per policy |
| Publish | Evidence not published to consumers |
| Consume | Consumers see snapshot only |
| Archive | Evidence retention **SAFE UNKNOWN** |

---

## SAFE UNKNOWN

- Retention period for evidence after successful publish.
- Whether evidence checksum registry is required before validation.
- Virus scan on ZIP evidence — policy not fixed.

---

## Non-goals

- Defining ZIP layout, database dump format, or manifest file format.
- Automated evidence lifecycle product.
