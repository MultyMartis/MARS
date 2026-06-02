# EAR Offline Acquisition v1

**Purpose:** Define **Offline Acquisition** (Model A) — archive-first, operator-delivered evidence — as a **permanent** EAR capability.  
**Status:** architecture specification — **no** implementation.  
**Phase:** 2E  
**Parent:** [EAR-ACQUISITION-TRACKS-v1.md](EAR-ACQUISITION-TRACKS-v1.md)

---

## Mission

Produce a governed **Snapshot Package** from **operator-supplied archives and exports** without requiring live read-only connectors. Offline acquisition exists for engagements where connection is impossible, undesirable, or unnecessary for the chartered outcome.

**Archive First philosophy:** The delivered archive (ZIP, tarball, panel export, DB dump) is the **primary evidence artifact**. EAR does not imply live site truth. Staleness, incomplete trees, and missing sections are recorded honestly in `safe-unknown` and quality level — never inflated.

**Permanent capability:** Offline is **not** a temporary bridge until Connected exists. Air-gapped audits, client packages, and legacy archives remain in scope for the full EAR lifecycle.

---

## Inputs

| Input class | Examples | Operator responsibility |
|-------------|----------|-------------------------|
| **Site archive** | Full or partial ZIP of web root; hosting panel backup export | Integrity, scope, extraction if needed |
| **Database archive** | SQL dump (structure-only preferred), `.sql.gz`, table-list export | Redaction policy; no full row dumps in git-bound paths unless chartered |
| **Supplementary drops** | Admin screenshots, extension list exports, manifest text files | Label provenance and date |
| **Metadata** | `site_id`, environment class, baseline reference, acquisition date | Accurate declaration |
| **Charter** | Read-only scope, target snapshot level, platform spec reference | Human approval at Request |

**EAR modes:** Primarily **Mode 0** (Manual Evidence) and **Mode 1** (Guided Evidence) per [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md).

**Credentials:** Typically **none** flow through EAR for Acquire — operator obtained archives out-of-band.

---

## Outputs

| Output | Description |
|--------|-------------|
| **Candidate snapshot** | Assembled per platform spec (e.g. [EAR-OPENCART-SNAPSHOT-SPEC-v1.md](EAR-OPENCART-SNAPSHOT-SPEC-v1.md)) after Validate |
| **Published snapshot** | After operator Publish approval per [EAR-SNAPSHOT-PUBLISHING-v1.md](EAR-SNAPSHOT-PUBLISHING-v1.md) |
| **`acquisition-log` / `access-log`** | Records offline channels used (ZIP, panel export, operator drop IDs) — not live connector sessions |
| **`safe-unknown`** | Mandatory entries for gaps (missing DB, partial tree, unstated backup date) |

---

## Expected snapshot levels

Honest levels depend on **what was delivered**, not on operator intent.

| Typical delivery | Achievable level (honest) | Notes |
|------------------|---------------------------|-------|
| Declaration + browser only | **0** | Path L0-* |
| ZIP only (site tree) | **1** | DB/theme gaps → `safe-unknown` |
| ZIP + DB structure export | **1** (strong) | Path L1-A, L1-E offline variant |
| ZIP + admin corroboration drops | **2** | Path L2-A, L2-D |
| Comprehensive archives + structured inventories | **2–3** | Level 3 rare without machine-readable full manifest policy |

Canonical path recipes: [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md). OpenCart channel alignment: [EAR-OPENCART-SNAPSHOT-PATHS-v1.md](EAR-OPENCART-SNAPSHOT-PATHS-v1.md) (offline-capable paths).

---

## Strengths

| Strength | Benefit |
|----------|---------|
| **No live access required** | Audits under NDA, legal hold, or client-only packages |
| **Low credential surface** | Secrets often never enter EAR tooling |
| **Predictable evidence boundary** | Fixed byte set — easier legal review |
| **Works before Mode 2 runtime** | SITE-001 Run 5 resume via Mode 0/1 today |
| **Permanent fit for legacy** | Archived ocStore/WP sites without hosting |

---

## Weaknesses

| Weakness | Mitigation (process) |
|----------|----------------------|
| **Staleness** | Record backup/export date in `acquisition-log`; `safe-unknown` if unknown |
| **Operator burden** | Mode 1 guided checklist |
| **Inconsistent layout** | Validate against spec; reject publish on critical gaps |
| **Quality ceiling** | May not reach Level 3 without comprehensive archives |
| **Repeat cost** | Each refresh requires new operator export — no automatic delta |

---

## Typical use cases

| Use case | Why offline |
|----------|-------------|
| Legacy ocStore site — hosting dead | Only backup ZIP exists |
| Client audit package | Third party delivered archives |
| Pre-migration inventory | One-time snapshot before cutover |
| Run 5 resume with Beget backup | [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md) |
| Air-gapped compliance review | No outbound connection |
| Hybrid baseline | First snapshot before Connected charter |

---

## Archive First (normative)

1. **Treat archives as point-in-time truth** for the snapshot — not as “cache of live site.”
2. **Never infer completeness** from archive size alone — Validate manifest coverage.
3. **Prefer structure-only DB exports** for `database-metadata`; row data is out of v1 consumer contract unless explicitly chartered.
4. **Document provenance** — who provided archive, when, from which backup job (if known).
5. **Re-acquisition** = new `snapshot_id` (new archive drop or refreshed export), not silent overwrite.

---

## Workflow alignment

Offline uses the same lifecycle as all acquisition: **Request → Acquire → Validate → Publish → Archive** per [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md). Acquire = operator delivery + EAR intake (manual assembly), not connector session.

---

## Relation to Connected track

| Question | Answer |
|----------|--------|
| Is Offline replaced by Connected for SITE-001? | **No** — SITE-001 may use Connected when chartered; Offline remains valid for backup-first path |
| Can same site use both? | **Yes** — Hybrid pattern; separate snapshots |
| Do consumers care which track? | Consumers care about **published quality level** and `safe-unknown`; track informs expectations, not analysis algorithms |

---

## SAFE UNKNOWN

- Standard ZIP layout validator tool — not specified Phase 2E.
- Maximum archive size for external bulk storage — operator / storage policy.
- Automated virus scan on intake — not EAR v1 scope.

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md) | Canonical offline paths |
| [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) | When to choose offline |
| [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md) | Where bulk archives live |
