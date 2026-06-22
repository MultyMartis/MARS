# Triumph-ORCA Evidence Inventory v1

**Method:** Repository-only — existence ≠ usage  
**Generated:** 2026-06-22  
**Machine-readable:** [`triumph-orca-evidence-inventory-v1.json`](triumph-orca-evidence-inventory-v1.json)

---

## Summary counts

| Domain | Artifact count (representative) | Operational use proven |
|--------|--------------------------------|------------------------|
| Triumph Manipulator production | 28+ canonical | **High** — battle freeze |
| Triumph-derived laws / contract | 8 | **Partial** — documented; Corvonero clean-room did not enforce |
| Corvonero v1–v7.1 historical | 40+ | **Diagnostic only** — forbidden as semantic source |
| Corvonero clean-room v2 | 25+ | **CONFIRMED USED** — pipeline executed; failed gate |
| ORCA Semantic Intelligence P0-A–C | 80+ | **Documented** — not runtime |
| ORCA Semantic Intelligence P0-D | 35+ | **PROPOSED** — uncommitted |
| MIG Corvonero session | 15+ | **CONFIRMED USED** — Wordstat Pass A ingested |
| MIG Triumph pilot | 6+ | **REFERENCED** — keyword_pass off |

---

## A. Triumph Manipulator — production core

| Path | Title | Date/ver | Owner | Type | Authority | Usage | Evidence of use | Consumers | Relevance |
|------|-------|----------|-------|------|-----------|-------|-----------------|-----------|-----------|
| `projects/orca/freeze/battle-pilot-triumph-search-v1/TRIUMPH-SEARCH-RK-STABLE-STATE-v1.md` | Battle stable state | 2026-05-30 | ORCA/Triumph | Freeze milestone | Partial — import PASS, not launch | **CONFIRMED USED** | Commander import PASS documented | Contract derivation, audits | **High** |
| `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | PPC JSON instance (meaning SoT) | v1 | ORCA Triumph | Schema instance | Draft fixture — not semantic lock | **CONFIRMED USED** | validation-cli + exporter inputs | Exporter, validation | **High** |
| `projects/orca/ppc/triumph-manipulator/doctrine/generation-logic-v0.md` | ORCA generation doctrine | v0 frozen | ORCA | Doctrine | Documented architecture | **CONFIRMED USED** | Referenced in process freeze, validation rules | All Triumph PPC | **High** |
| `projects/orca/ppc/triumph-manipulator/research/intent-groups-v1.md` | Intent tiers S/A/X | v1 frozen | ORCA | Research | Documented | **CONFIRMED USED** | JSON `intent_tier` fields; SE rules | Group architecture | **High** |
| `projects/orca/ppc/triumph-manipulator/validation/semantic-validation-rules-v1.md` | SE-* semantic rules | v1 | ORCA validator | Validation contract | Frozen | **CONFIRMED USED** | validation-cli registry | Pre-export gate | **High** |
| `projects/orca/ppc/triumph-manipulator/validation/commercial-validation-rules-v1.md` | CM-* commercial rules | v1 | ORCA | Validation | Frozen | **CONFIRMED USED** | validation-cli | Ad/landing QA | **High** |
| `projects/orca/ppc/triumph-manipulator/validation/landing-continuity-rules-v1.md` | LM-* landing rules | v1 | ORCA | Validation | Frozen | **CONFIRMED USED** | validation-cli | Ad↔landing | **High** |
| `projects/orca/ppc/triumph-manipulator/tools/validation-cli/` | Validator CLI (345 rules) | battle-stable | Cursor/ORCA tools | Tool | Human-triggered | **CONFIRMED USED** | Stable state reproduction steps | Export gate | **High** |
| `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/` | Commander exporter v1.4 | battle-stable | ORCA tools | Tool | Human-triggered | **CONFIRMED USED** | Battle export path | Commander XLSX | **High** |
| `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/cross-negative-matrix-v1.4.js` | Cross-negative builder | v1.4 | ORCA tools | Script | Mandatory pre-export | **CONFIRMED USED** | Export pipeline docs | Group negatives | **High** |
| `projects/orca/freeze/route-family-freeze-v1/ORCA-ROUTE-FAMILY-FREEZE-v1.md` | 12-route family freeze | 2026-05-28 | ORCA freeze | Scope lock | Frozen pre-keywords | **CONFIRMED USED** | JSON groups map 1:1 | Semantic architecture | **High** |
| `projects/orca/freeze/ppc-exporter-production-baseline-v1/` | Export baseline rules | v1 | ORCA freeze | Policy pack | Frozen | **CONFIRMED USED** | Exporter README, hygiene | Transport | **High** |
| `projects/orca/freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md` | Post-battle lessons | 2026-05-30 | Human review | Lessons | Documented | **REFERENCED** | LRL derivation, contract | LRL, SI migration | **High** |
| `projects/orca/freeze/commander-url-sync-v1/` | URL sync gate | v1 | ORCA freeze | Gate evidence | Human PASS | **CONFIRMED USED** | 164 URL replacements | Landing alignment | **High** |
| `projects/orca/content-packs/examples/triumph-manipulyator-*-pack-v1/` | Semantic content packs | v1 | ORCA packs | Content | Per-pack status | **REFERENCED** | Route freeze table | Factory handoff | **Medium** |
| `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json` | Landing URL registry | project | Triumph project | Registry | Partial | **CONFIRMED USED** | URL sync freeze | PPC JSON URLs | **Medium** |
| `workspaces/triumph-manipulator-landing-v6/` | Frontend delivery | v6 | Website Factory | Implementation | Deploy checklist | **REFERENCED** | Calibration loop docs | Landing continuity | **Medium** |
| `projects/orca/ppc/triumph-manipulator/TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md` | Triumph ↔ Intelligence v0 | v0 | ORCA docs | Relationship | Documented | **REFERENCED** | Intelligence foundation | Migration policy | **Medium** |

---

## B. Triumph-derived ORCA laws and contract (post-battle formalization)

| Path | Title | Date | Owner | Type | Authority | Usage | Evidence | Consumers | Relevance |
|------|-------|------|-------|------|-----------|-------|----------|-----------|-----------|
| `projects/orca/knowledge/triumph-derived-orca-laws-v1.md` | 15 ORCA laws | 2026-06-22 | ORCA knowledge | Law registry | Documented | **REFERENCED** | Cited in clean-room manifest AUTH-04 | Contract, clean-room | **High** |
| `projects/orca/knowledge/triumph-manipulator-production-process-v1.md` | Reconstructed process | 2026-06-22 | ORCA knowledge | Process doc | Evidence-based | **REFERENCED** | Prior audit task | Contract derivation | **High** |
| `projects/orca/knowledge/triumph-manipulator-production-evidence-inventory.md` | Evidence inventory | 2026-06-22 | ORCA knowledge | Inventory | Documented | **REFERENCED** | This audit extends | Contract | **High** |
| `projects/orca/knowledge/triumph-manipulator-production-decisions-v1.json` | Production decisions | 2026-06-22 | ORCA knowledge | JSON registry | Documented | **AVAILABLE BUT USAGE UNPROVEN** | No pipeline auto-load found | Future integration | **High** |
| `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` | Campaign production contract | v1 uncommitted | ORCA contracts | Contract | Canonical (declared) | **REFERENCED** | Clean-room manifest AUTH-03; **not consumed by pipeline script** | Validator tool only | **Critical** |
| `projects/orca/contracts/orca-campaign-production-invariants-v1.json` | Invariants | v1 | ORCA | Machine contract | Documented | **REFERENCED** | `validate-campaign-production-contract.mjs` | Corvonero v7 audit | **High** |
| `projects/orca/architecture/orca-production-contract-integration-plan-v1.md` | Integration plan | 2026-06-22 | ORCA architecture | Plan | **Planned not wired** | **NOT USED** | Explicitly "not delivered: full pipeline refactor" | Future enforcement | **Critical** |
| `projects/orca/tools/validate-campaign-production-contract.mjs` | Contract validator | v1 | ORCA tools | Validator | Read-only gate | **CONFIRMED USED** | v7 audit reports; tests pass | Corvonero v7 only | **High** |

---

## C. Corvonero historical (v1–v7.1) — anti-pattern evidence

| Path | Title | Owner | Type | Authority | Usage | Relevance |
|------|-------|-------|------|-----------|-------|-----------|
| `projects/orca/projects/corvonero-yandex-direct/production/` | v1–v7 production datasets | Corvonero | Production | **HISTORICAL ONLY** | **CONFIRMED USED** (past runs) | Failure pattern source |
| `projects/orca/projects/corvonero-yandex-direct/artifacts/REPORT-orca-evidence-audit-and-commander-v5.md` | v5 evidence audit | ORCA | Report | Diagnostic | **REFERENCED** | Template classifier overreach |
| `projects/orca/projects/corvonero-yandex-direct/artifacts/REPORT-triumph-experience-and-v7-contract-audit.md` | Triumph recovery + v7 audit | ORCA | Report | 2026-06-22 | **REFERENCED** | Contract gate PASS v7 |
| `projects/orca/projects/corvonero-yandex-direct/production/triumph-production-pattern-audit-v1.md` | Triumph reuse map | ORCA | Audit | Factual | **REFERENCED** | Stage 2A adaptation |
| `projects/orca/tools/fixtures/campaign-contract/corvonero-v6-failure-patterns-v1.json` | v6 failure fixtures | ORCA tools | Fixture | Test evidence | **CONFIRMED USED** | Contract validator tests | **High** |

---

## D. Corvonero clean-room v2

| Path | Title | Owner | Type | Authority | Usage | Evidence | Relevance |
|------|-------|-------|------|-----------|-------|----------|-----------|
| `projects/orca/projects/corvonero-direct-v2-clean-room/PROJECT.md` | Project status | Corvonero v2 | Project | DIAGNOSTIC FAILED | **CONFIRMED USED** | Operator D2/D7 | **Critical** |
| `projects/orca/projects/corvonero-direct-v2-clean-room/tools/run-clean-room-semantic-pipeline-v1.mjs` | Semantic pipeline | ORCA tools | Script | Executed | **CONFIRMED USED** | `pipeline-run-summary-v1.json` | **Critical** |
| `projects/orca/projects/corvonero-direct-v2-clean-room/semantic-core/corvonero-commercial-eligibility-v1.json` | Eligibility decisions | Pipeline output | Semantic | **DO NOT PROMOTE** | **CONFIRMED USED** | 1892 accepts | **Critical** |
| `projects/orca/projects/corvonero-direct-v2-clean-room/authority/CORVONERO-DIRECT-V2-SOURCE-AUTHORITY-MANIFEST-v1.md` | Source manifest | Corvonero v2 | Authority | ACTIVE | **REFERENCED** | Lists contract as AUTH-03 | **High** |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/` | MIG session | MIG | External intake | Operator approved | **CONFIRMED USED** | Wordstat 2399 rows | **High** |

---

## E. ORCA Semantic Intelligence (P0)

| Path | Title | Status | Usage | Relevance |
|------|-------|--------|-------|-----------|
| `projects/orca/architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md` | P0-A ADR | APPROVED `f17c270` | **DOCUMENTATION ONLY** | Architecture target |
| `projects/orca/semantic-intelligence/taxonomy/`, `schemas/` | P0-B | APPROVED `3151953` | **DOCUMENTATION ONLY** | Schema spec |
| `projects/orca/semantic-intelligence/annotation/` | P0-C | APPROVED `78b0557` | **DOCUMENTATION ONLY** | Annotation handbook |
| `projects/orca/semantic-intelligence/benchmark/` | P0-D | PROPOSED uncommitted | **NOT USED** operationally | On hold |

---

## F. MIG / demand evidence

| Path | Title | Usage | Notes |
|------|-------|-------|-------|
| `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` | Triumph MIG pilot | **REFERENCED** | `keyword_pass: false` — no Wordstat in MIG for Triumph |
| `incoming/mig/completed/triumph-gruzotaxi-krasnodar-v1.canonical.json` | Triumph MIG outcome | **AVAILABLE BUT USAGE UNPROVEN** for keyword surface | Business intake pattern |
| `incoming/mig/pilots/corvonero/session-mig-20260622-corv01/evidence/wordstat/` | Corvonero Wordstat Pass A | **CONFIRMED USED** | 18 XLSX → 2399 rows |
| `C:\AI MARS STORAGE\mig\corvonero\wordstat-2026-06\` | Raw Wordstat Excel | **REFERENCED** | External storage — not in git |

---

## G. Landing Readiness Layer

| Path | Title | Usage | Notes |
|------|-------|-------|-------|
| `projects/orca/intelligence/landing-readiness-layer-v1.md` | LRL v1 (live path) | **REFERENCED** | Listed in OPERATIONAL-INDEX |
| `archive/orca-lrl-foundation-v1/intelligence/landing-readiness-layer-v1.md` | LRL archive copy | **AVAILABLE BUT USAGE UNPROVEN** | Triumph battle source |

---

## H. SAFE UNKNOWN (not in repository)

| Item | Status |
|------|--------|
| Web-GPT chat transcripts for Triumph campaign build | **Not in repo** |
| Operator Wordstat exports for Triumph (if any) | **Not found in repo** |
| Triumph launch XLSX (gitignored) | By design |
| Operator-signed Triumph launch approval | **Not found** |
| Live campaign performance data | **Not in repo** |
