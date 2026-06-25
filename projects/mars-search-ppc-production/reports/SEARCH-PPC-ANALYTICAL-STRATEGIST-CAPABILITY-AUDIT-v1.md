# Search PPC Analytical and Strategist Capability Audit v1

**Date:** 2026-06-23  
**Scope:** ORCA, MIG, Search PPC lifecycle, Corvonero, Triumph, Commander, landing/bidding docs

## Summary

| Classification | Count |
|----------------|-------|
| OPERATIONAL | 14 |
| REUSABLE | 11 |
| PARTIALLY IMPLEMENTED | 6 |
| DOCUMENTED ONLY | 8 |
| DIAGNOSTIC ONLY | 5 |
| PROJECT-SPECIFIC | 7 |
| MISSING (pre-Wave 4) | 4 |
| UNSAFE (bypass risk) | 2 |

## 1. Strategy schemas

| Asset | Status |
|-------|--------|
| Lifecycle contract SPPC-12/13 artifact types | OPERATIONAL |
| `strategy/schemas/dated-analytical-pack-v1.schema.json` | OPERATIONAL (Wave 4) |
| `strategy/schemas/search-ppc-strategy-v1.schema.json` | OPERATIONAL (Wave 4) |
| Corvonero `strategy/*.md` charters | PROJECT-SPECIFIC — not lifecycle JSON |

## 2. Analytical packs

| Asset | Status |
|-------|--------|
| `stages/SPPC-12-dated-analytical-pack.md` | DOCUMENTED ONLY → **PARTIALLY IMPLEMENTED** (Wave 4 builder) |
| MIG `evidence-manifest.mjs` SPPC-12 contribution | REUSABLE |
| Synthetic placeholder `state/fixtures/evidence/analytical-pack.json` | DIAGNOSTIC ONLY |

## 3. Competitor reports

| Asset | Status |
|-------|--------|
| MIG competitor audit fixtures | REUSABLE |
| `competitor_advertising_audit` in lifecycle contract | OPERATIONAL |
| Corvonero competitor packs | MISSING / FROZEN |

## 4. Campaign architecture generators

| Asset | Status |
|-------|--------|
| Triumph `triumph-s-tier-draft-v1.json` | PROJECT-SPECIFIC |
| ORCA `ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1` | REUSABLE contract |
| Wave 4 `campaign-architecture.mjs` | OPERATIONAL (strategy-level, not Commander) |
| Corvonero production v2–v7 scripts | PROJECT-SPECIFIC — must not become universal authority |

## 5. Bidding/budget logic

| Asset | Status |
|-------|--------|
| Triumph validation rules | PROJECT-SPECIFIC |
| Wave 4 `bidding-framework.mjs`, `budget-framework.mjs` | OPERATIONAL |
| SPPC-18 stage docs | DOCUMENTED ONLY |

## 6. Landing alignment

| Asset | Status |
|-------|--------|
| SPPC-17 stage docs | DOCUMENTED ONLY |
| Wave 4 `landing-offer-alignment.mjs` | OPERATIONAL |
| Website-factory landing QA | REUSABLE patterns only |

## 7. Must NOT become universal authority

- `corvonero-yandex-direct/tools/run-full-production-v*.mjs`
- Corvonero clean-room diagnostic semantic outputs
- Triumph Commander export scripts without lifecycle gate
- Chat-based strategy without pack (UNSAFE bypass — now gated)

## 8. Components to reuse

- `runtime/src/lifecycle-gate.mjs` / `validate-lifecycle.mjs`
- ORCA semantic production packs (SPPC-05–09)
- MIG evidence CLI and paid-SERP contracts
- OpenRouter secret loader (strategist uses separate prompt)
- Triumph-derived ORCA laws (reference only)

JSON counterpart: `SEARCH-PPC-ANALYTICAL-STRATEGIST-CAPABILITY-AUDIT-v1.json`
