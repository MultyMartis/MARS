# ORCA Semantic Intelligence — Migration Boundary v1

**Boundary ID:** `orca-semantic-intelligence-migration-boundary`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Principle

New ORCA Semantic Intelligence v1 starts from **preserved evidence and operator scope** — not from defective semantic decisions. Diagnostic layers inform failure-mode analysis only.

---

## Reusable assets

| Asset | Locus | Use in v1 |
|-------|-------|-----------|
| Corvonero operator intake | `corvonero-direct-v2-clean-room/intake/` | SI-01 business scope |
| Service scope registry | `intake/CORVONERO-DIRECT-V2-SERVICE-SCOPE-v1.md` | SI-01, SI-10 |
| MIG raw ledger | `mig-source/MIG-WORDSTAT-SOURCE-LEDGER-v1.md` | SI-02, SI-03 provenance |
| Source corpus | MIG binding + raw ledger | SI-03 |
| Normalized corpus | `semantic-core/CORVONERO-NORMALIZED-CORPUS-v1.md` | SI-04 input |
| Canonical deduplicated phrase registry | `semantic-core/CORVONERO-CANONICAL-PHRASE-REGISTRY-v1.md` | SI-04/SI-05 input |
| Provenance / authority manifest | `authority/`, `artifacts/pipeline-run-summary-v1.json` | Audit trail |
| Universal Campaign Production Contract | `contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` | SI-15 where compatible |
| Research package | `research/ppc-semantic-intelligence/world-practice-2026-06/` | Analytical source |
| Triumph-derived laws | `knowledge/triumph-derived-orca-laws-v1.md` | Architecture evidence |
| Architecture ADR v1 (post-approval) | `architecture/semantic-intelligence/` | Target model |

---

## Diagnostic only — DO NOT PROMOTE

| Asset | Marker | Reason |
|-------|--------|--------|
| Clean-room v1 intent classifications | `DIAGNOSTIC EVIDENCE ONLY` | Protected-strata failure |
| Eligibility decisions (~1892 accepts) | `DIAGNOSTIC EVIDENCE ONLY` | Over-admission |
| Service mappings | `DIAGNOSTIC EVIDENCE ONLY` | Built on bad eligibility |
| Cluster candidates | `DIAGNOSTIC EVIDENCE ONLY` | Built on bad ownership |
| Negative candidates | `DIAGNOSTIC EVIDENCE ONLY` | Cannot rescue base |
| Semantic Core Candidate v1 | `DIAGNOSTIC EVIDENCE ONLY` | Not approved authority |
| Operator review workbook decisions | `DIAGNOSTIC EVIDENCE ONLY` | Contaminated pipeline |
| Corvonero v1–v7.1 production | `HISTORICAL DIAGNOSTIC` | Pre-clean-room failures |

**Rule:** No semantic decision migration from diagnostic layers.

---

## Must be created later

| Artifact | Backlog | Layer impact |
|----------|---------|--------------|
| New intent taxonomy | P0-B | SI-07 |
| Per-phrase semantic record schema | P0-B | All layers |
| Annotation guideline | P0-C | SI-09, SI-13 |
| Universal benchmark charter | P0-D | Quality gates |
| Corvonero pilot charter | P0-E | Pilot evaluation |
| Gold labels | P0-D/E | Authority rank 5 |
| Pilot corpus annotation | P0-E | Corvonero rerun input |
| Baseline classifiers | P0-F | SI-07, SI-08 |
| Evaluation harness | P0-F/G | Threshold gate |
| Approved Semantic Core | P0-H | SI-14 |

---

## Corvonero restart path

```text
Preserved corpus (SI-03/04)
  → New taxonomy + guideline + benchmark (P0-B/C/D/E)
  → Baselines + threshold gate (P0-F/G)
  → New admission run CONSERVATIVE mode
  → Human review + Semantic Core (SI-13/14)
  → Operator sign-off (P0-H)
  → Campaign production (SI-15) — still blocked until then
```

Diagnostic v1 outputs remain in repository as failure evidence — never merged into new core.

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-migration-boundary-v1.json` |
| Corvonero PROJECT.md | `projects/corvonero-direct-v2-clean-room/PROJECT.md` |
