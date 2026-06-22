# MARS Search PPC — Cross-System Integration Map v1

**Parent:** [MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md)  
**Lifecycle status:** `APPROVED — IMPLEMENTATION AUTHORIZED` (W1-D1, 2026-06-22)  
**Wave 1 enforcement locus:** `runtime/` (manifest, transition engine, validator CLI)

---

## Artifact flow

```text
ATLAS → Business/Project Authority (SPPC-01)

MIG → Source Registry (02)
    → Full Corpus binding (03)
    → Wordstat / collection metadata
    → Paid SERP business hours (10)
    → Competitor Evidence (11)

ORCA → Canonical Semantic Registry (04)
     → Admission (05)
     → Tiers T1–T5 (06)
     → Ownership (07)
     → Clusters (08)
     → Negatives (09)

Cross-system → Dated Analytical Pack (12)

AI PPC Strategist → Strategy record (13)

Campaign Production → Architecture (14)
                    → Keyword/negative distribution (15)
                    → Ads (16)
                    → Bidding/budget (18)

QA → Landing alignment (17)
   → Campaign QA (19)

Commander Export → Transport artifact (20) — no semantic mutation

Operator → Dry-run approval (21)

Platform → Launch evidence (22)

Post-Launch Learning → Governed proposals (23)
```

---

## Boundary table

| Boundary | Producer | Consumer | Contract | Validation | On failure |
|----------|----------|----------|----------|------------|------------|
| Business authority | ATLAS / Operator | MIG, ORCA, Strategist | SPPC-01 | Lifecycle validator | BLOCKED |
| Source registry | MIG | ORCA normalization | SPPC-02 | Source ID + date required | BLOCKED |
| Canonical corpus | ORCA | Admission | SPPC-04 | Phrase ID stability | BLOCKED |
| Admission | ORCA SI | Tiers, ownership | SPPC-05 | ACCEPT/REJECT/ABSTAIN | BLOCKED |
| Market evidence | MIG | Analytical pack, Strategist | SPPC-10–11 | Time passport | BLOCKED or DEGRADED |
| Analytical pack | Cross-system | AI PPC Strategist | SPPC-12 | Completeness gate | BLOCKED |
| Strategy | Strategist | Campaign Production | SPPC-13 | No Commander jump | BLOCKED |
| Campaign SoT | Campaign Production | QA, Commander | SPPC-14–19 | ORCA campaign contract + lifecycle | BLOCKED |
| Commander export | Commander Export | Operator import | SPPC-20 | Parity check | BLOCKED |
| Launch | Platform | Post-launch | SPPC-22 | Goals/UTM/landing | BLOCKED |

---

## Consumer obligations (no drift)

Subsystem docs link here; they do **not** duplicate full lifecycle text.

- ORCA: [projects/orca/OPERATIONAL-INDEX.md](../../orca/OPERATIONAL-INDEX.md)  
- MIG: [projects/mig/contracts/](../../mig/contracts/)  
- ATLAS: [projects/atlas/foundation/](../../atlas/foundation/)
