# Corvonero — Actual Semantic Pipeline v1

**Scope:** `corvonero-direct-v2-clean-room` (canonical failed admission run) + historical v1–v7.1 context  
**Machine-readable:** [`corvonero-actual-semantic-pipeline-v1.json`](corvonero-actual-semantic-pipeline-v1.json)  
**Status:** DIAGNOSTIC FAILED — FROZEN

---

## Clean-room v2 pipeline (executed 2026-06-22)

| # | Stage | Input | Rules/scripts | Authority read | Authority NOT read | Output | Execution evidence | Defects |
|---|-------|-------|---------------|----------------|-------------------|--------|-------------------|---------|
| 1 | Business intake | Operator markdown + JSON | Manual authoring | `intake/CORVONERO-DIRECT-V2-BUSINESS-INTAKE-v1.md` | Old v7 production | intake JSON | Report §6 | None at intake |
| 2 | Service scope | Operator charter | `write-service-scope-v1.mjs`, `service-scope-data.mjs` | 34 service IDs | Operator phrase-level seeds for admission | scope JSON | Report §7 | Priority not assigned (documented) |
| 3 | MIG corpus ingest | Wordstat Pass A normalized | Read `wordstat-pass-a-normalized.json` | MIG session; ledger | Triumph workflow; operator per-phrase review | 2399 raw rows | Report §8 | National Wordstat ≠ regional volume (documented) |
| 4 | Normalization | Raw phrases | `normalizePhrase()` in pipeline | — | P0-B semantic record schema | normalized corpus | Report §9 | Technical only — OK |
| 5 | Deduplication | Normalized | dedup key | — | — | 2368 canonical | Report §10 | OK |
| 6 | Intent screening | Canonical phrases | `classifyIntent()` regex arrays (CAREER, EDU, DIY, etc.) | Service scope patterns indirectly | **Campaign Production Contract**; **P0-C annotation**; **operator seeds protection** | intent screening JSON | `corvonero-intent-screening-v1.json` | Regex gaps; `COMMERCIAL SERVICE` with medium confidence |
| 7 | Commercial eligibility | Intent + service map | `commercialEligibility()` + `mapService()` | Service scope regex | **ACCEPT requires commercial evidence (SI)**; **ABSTAIN policy** | eligibility JSON | 1892 ELIGIBLE COMMERCIAL | **Topic≈intent failure** |
| 8 | Service mapping | Phrases | `SERVICE_PATTERNS` | scope registry | Triumph ownership-before-negatives | phrase-to-service map | mapping JSON | Multi-service ambiguous phrases accepted |
| 9 | Cluster discovery | Eligible phrases | `clusterKey()` heuristics | — | Operator group architecture freeze | cluster candidates | clusters JSON | Clusters after broken admission |
| 10 | Negative candidates | Classes + eligibility | `discoverNegatives()` | Excluded class phrases | Cross-group ownership review | negative registry | negatives JSON | Negatives derived from bad accepts |
| 11 | Review workbook | All above | ExcelJS sheets in pipeline | Display only | Contract validator | XLSX workbook | artifacts/ | Operator review too late in chain |
| 12 | Semantic core candidate | Eligible set | Aggregation | — | Independent gold labels | candidate JSON/MD | 1892 eligible | **FAILED gate** |
| 13 | Production/export | — | **BLOCKED** | D7 | — | Not created | PROJECT.md | Correctly blocked |

**Script:** `projects/orca/projects/corvonero-direct-v2-clean-room/tools/run-clean-room-semantic-pipeline-v1.mjs`

---

## Historical Corvonero v1–v7.1 (summary — forbidden as semantic source)

| Stage | Tool pattern | Known defect |
|-------|--------------|--------------|
| Semantic classifier | `semantic-human-review-v*.mjs` | Template identical reasons; advisory treated as authority |
| Group viability | min-count / HOLD heuristics | 41 seed loss v6 |
| Repair package | auto scope mutation | Operator scope narrowed |
| Pipeline validators | structural checks | PASS without commercial validity |
| v7 recovery | operator recovery package + contract audit | Contract PASS at export level — **after** v6 failure |

Evidence: `orca-production-contract-integration-plan-v1.md`, `corvonero-v6-failure-patterns-v1.json`, v7 audit report.

---

## Why career / education / DIY phrases appeared

| Mechanism | Explanation | Evidence |
|-----------|-------------|----------|
| **Bulk Wordstat corpus** | National semantic discovery includes career, edu, DIY queries | MIG Pass A 2370 unique phrases |
| **Weak admission logic** | `COMMERCIAL SERVICE` class assigned when `/(1с|маркиров)/` matches even without hire verbs; eligibility accepts with `services.length` | Lines 92–133 in pipeline script |
| **Service scope regex too broad** | `mapService()` matches configuration names → treats product queries as service demand | `service-scope-data.mjs` |
| **No ABSTAIN terminal** | Ambiguous → ELIGIBLE NARROW or NEEDS OPERATOR but bulk auto-promoted | No P0-C runtime |
| **No operator seed gate** | Unlike Triumph `is_primary` protection | Triumph JSON pattern not consumed |
| **Contract not loaded** | AUTH-03 listed but script has no `require`/read of contract or invariants | Authority manifest vs script |
| **Negatives after broken ownership** | Exclusion registry lists career/edu but thousands already accepted | Negative stage cannot undo admission |

---

## Pipeline stages that did NOT read Triumph-derived contracts

- `run-clean-room-semantic-pipeline-v1.mjs` — **no import** of contract, laws, or triumph laws JSON  
- No call to `validate-campaign-production-contract.mjs` at semantic admission stage  
- P0-A–C SI documents — **not consumed** (implementation not started)
