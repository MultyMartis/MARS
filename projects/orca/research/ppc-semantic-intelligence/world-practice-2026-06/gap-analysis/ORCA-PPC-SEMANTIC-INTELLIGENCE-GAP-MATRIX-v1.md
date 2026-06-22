# ORCA PPC Semantic Intelligence — Gap Matrix v1

**Matrix ID:** `orca-ppc-semantic-intelligence-gap-matrix`  
**Version:** v1  
**Date:** 2026-06-22

Maturity scale: `ABSENT` | `DOCUMENTED` | `PARTIAL` | `PILOT` | `VALIDATED`

**Implementation status** in this matrix refers to **documented/planned ORCA capability** — not claimed runtime unless evidence exists.

---

## Layer 1 — Operator Authority

| Field | Value |
|-------|-------|
| Research recommendation | Versioned operator brief, scope freeze, threshold governance, sign-off before campaign production |
| Current MARS/ORCA evidence | Business intake contracts; Corvonero clean-room intake v1; operator decisions D1–D7 |
| Artifact paths | `projects/orca/projects/corvonero-direct-v2-clean-room/intake/`; `decisions/ORCA-PPC-SEMANTIC-INTELLIGENCE-OPERATOR-DECISIONS-v1.md` |
| Maturity | PARTIAL |
| Confirmed capability | Operator intake and D1–D7 recorded for semantic intelligence program |
| Missing capability | Semantic Intelligence-specific operator sign-off contract (P0-H) |
| Risk | Scope drift without Semantic Core authority contract |
| Required promotion artifact | P0-H Semantic Core Authority Contract |
| Dependencies | P0-A Architecture ADR |
| Corvonero blocking impact | HIGH — no production restart without operator sign-off chain |
| Implementation status | DOCUMENTED governance only |

---

## Layer 2 — Market Evidence

| Field | Value |
|-------|-------|
| Research recommendation | Wordstat, keyword tools, search terms, competitor evidence packs with source log |
| Current MARS/ORCA evidence | MIG Wordstat Pass A for Corvonero; ORCA research layer v0; evidence classification v0 |
| Artifact paths | `projects/orca/projects/corvonero-direct-v2-clean-room/mig-source/`; `projects/orca/research/orca-research-layer-v0.md` |
| Maturity | PARTIAL |
| Confirmed capability | Corvonero MIG corpus ingested with ledger |
| Missing capability | Benchmark-stratified market evidence for intent classes |
| Risk | Corpus alone insufficient for commercial admission |
| Required promotion artifact | P0-D Benchmark Charter |
| Dependencies | P0-C Annotation Guideline |
| Corvonero blocking impact | MEDIUM — raw evidence preserved; not blocking reuse of corpus |
| Implementation status | PILOT evidence for Corvonero only |

---

## Layer 3 — Source Corpus

| Field | Value |
|-------|-------|
| Research recommendation | Raw corpus snapshot; provenance; no premature intent labels |
| Current MARS/ORCA evidence | Corvonero normalized + canonical phrase registry; MIG source ledger |
| Artifact paths | `semantic-core/CORVONERO-NORMALIZED-CORPUS-v1.md`; `semantic-core/CORVONERO-CANONICAL-PHRASE-REGISTRY-v1.md` |
| Maturity | PILOT |
| Confirmed capability | 2370 unique raw phrases; deduplicated canonical registry |
| Missing capability | Universal ORCA corpus program beyond Corvonero |
| Risk | Re-running admission without frozen corpus versioning |
| Required promotion artifact | Corpus snapshot versioning in P0-A ADR |
| Dependencies | None for Corvonero reuse |
| Corvonero blocking impact | LOW for preserved layers — reusable |
| Implementation status | PILOT — clean-room v1 |

---

## Layer 4 — Normalization

| Field | Value |
|-------|-------|
| Research recommendation | Lemmatization, dedupe, operator-aware parsing (`!`, `+`, `[]`) |
| Current MARS/ORCA evidence | `tools/normalize-mig-corpus.mjs`; normalized corpus v1 |
| Artifact paths | `projects/orca/projects/corvonero-direct-v2-clean-room/tools/normalize-mig-corpus.mjs` |
| Maturity | PARTIAL |
| Confirmed capability | Basic normalization and dedupe for MIG Wordstat |
| Missing capability | Yandex operator semantics test suite; versioned normalizer contract |
| Risk | Operator scope loss (research failure mode) |
| Required promotion artifact | P0-A normalizer requirements |
| Dependencies | P0-B schema for normalized fields |
| Corvonero blocking impact | MEDIUM — must not contaminate new run with old semantic labels |
| Implementation status | PARTIAL script — not validated runtime product |

---

## Layer 5 — Query Understanding

| Field | Value |
|-------|-------|
| Research recommendation | Entity/action/object/modifiers feature object |
| Current MARS/ORCA evidence | Research recommends; clean-room pipeline uses keyword heuristics only |
| Artifact paths | Research normalized companion § reference architecture |
| Maturity | ABSENT |
| Confirmed capability | None as structured feature layer |
| Missing capability | Query understanding schema and extractors |
| Risk | Admission without literal task decomposition |
| Required promotion artifact | P0-B Semantic Taxonomy and Record Schema |
| Dependencies | P0-A ADR |
| Corvonero blocking impact | HIGH |
| Implementation status | NOT STARTED |

---

## Layer 6 — Intent Screening

| Field | Value |
|-------|-------|
| Research recommendation | Hard exclusions; query-type classification; protected strata |
| Current MARS/ORCA evidence | `CORVONERO-INTENT-SCREENING-v1.md` — **DIAGNOSTIC EVIDENCE ONLY** |
| Artifact paths | `semantic-core/CORVONERO-INTENT-SCREENING-v1.md` |
| Maturity | PARTIAL |
| Confirmed capability | Diagnostic pass existed — failed protected-strata control |
| Missing capability | Benchmark-gated intent screening with abstention |
| Risk | Career/educational/DIY leakage to commercial path |
| Required promotion artifact | P0-C Guideline + P0-F baselines |
| Dependencies | P0-D/E benchmarks |
| Corvonero blocking impact | CRITICAL — invalid for reuse |
| Implementation status | DIAGNOSTIC FAILED |

---

## Layer 7 — Commercial Eligibility

| Field | Value |
|-------|-------|
| Research recommendation | accept/reject/abstain; cost-sensitive thresholds; no topical-only admit |
| Current MARS/ORCA evidence | `CORVONERO-COMMERCIAL-ELIGIBILITY-v1.md` — **DIAGNOSTIC EVIDENCE ONLY** |
| Artifact paths | `semantic-core/CORVONERO-COMMERCIAL-ELIGIBILITY-v1.md` |
| Maturity | PARTIAL |
| Confirmed capability | Diagnostic eligibility pass — 1892 accepts (over-admission signal) |
| Missing capability | D3 thresholds; D4 abstention; calibrated classifier |
| Risk | Paid search FP cost; platform semantic expansion |
| Required promotion artifact | P0-G Evaluation and Threshold Gate |
| Dependencies | P0-C, P0-D, P0-F |
| Corvonero blocking impact | CRITICAL |
| Implementation status | DIAGNOSTIC FAILED |

---

## Layer 8 — Semantic Adjudication

| Field | Value |
|-------|-------|
| Research recommendation | Per-phrase record: literal interpretation, goals, signals, rationale, abstain |
| Current MARS/ORCA evidence | Research table of fields; no ORCA adjudication product |
| Artifact paths | Research § «Стандарт semantic adjudication» |
| Maturity | DOCUMENTED |
| Confirmed capability | Field model described in research (recommendation) |
| Missing capability | Approved schema, tooling, human adjudication workflow |
| Risk | Invented commercial interpretations |
| Required promotion artifact | P0-B + P0-C |
| Dependencies | P0-A |
| Corvonero blocking impact | HIGH |
| Implementation status | NOT STARTED |

---

## Layer 9 — Service Mapping

| Field | Value |
|-------|-------|
| Research recommendation | Service ownership with confidence; conflict → review |
| Current MARS/ORCA evidence | `CORVONERO-PHRASE-TO-SERVICE-MAP-v1.md` — **DIAGNOSTIC EVIDENCE ONLY** |
| Artifact paths | `intake/CORVONERO-DIRECT-V2-SERVICE-SCOPE-v1.md`; phrase map v1 |
| Maturity | PARTIAL |
| Confirmed capability | 34 service IDs defined; diagnostic mapping produced |
| Missing capability | Mapping precision gate ≥ 0.97 on accepted commercial |
| Risk | Wrong ownership → wrong clusters/negatives |
| Required promotion artifact | P0-G metrics |
| Dependencies | P0-B, P0-C |
| Corvonero blocking impact | HIGH — invalid for reuse |
| Implementation status | DIAGNOSTIC FAILED |

---

## Layer 10 — Cluster Discovery

| Field | Value |
|-------|-------|
| Research recommendation | Task-based clusters; landing compatibility; operator approval |
| Current MARS/ORCA evidence | `CORVONERO-COMMERCIAL-CLUSTER-CANDIDATES-v1.md` — **DIAGNOSTIC EVIDENCE ONLY** |
| Artifact paths | `semantic-core/CORVONERO-COMMERCIAL-CLUSTER-CANDIDATES-v1.md` |
| Maturity | PARTIAL |
| Confirmed capability | Diagnostic cluster candidates generated |
| Missing capability | Cluster spec approval on approved core only |
| Risk | Lexical clusters mix intents |
| Required promotion artifact | P0-A stage separation rules |
| Dependencies | P0-H approved core |
| Corvonero blocking impact | HIGH — invalid for reuse |
| Implementation status | DIAGNOSTIC FAILED |

---

## Layer 11 — Negative Intelligence

| Field | Value |
|-------|-------|
| Research recommendation | Negatives after ownership; collision tests; no early aggressive minus |
| Current MARS/ORCA evidence | `CORVONERO-NEGATIVE-CANDIDATE-REGISTRY-v1.md` — **DIAGNOSTIC EVIDENCE ONLY**; Triumph cross-negative rules freeze |
| Artifact paths | `semantic-core/CORVONERO-NEGATIVE-CANDIDATE-REGISTRY-v1.md`; `freeze/ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md` |
| Maturity | PARTIAL |
| Confirmed capability | Triumph export-time cross-negative doctrine (separate project) |
| Missing capability | ORCA semantic negative intelligence on approved ownership |
| Risk | Destructive negatives; false commercial suppression |
| Required promotion artifact | P0-A + P0-H |
| Dependencies | Approved service map |
| Corvonero blocking impact | CRITICAL — D7 prohibits final negatives |
| Implementation status | DIAGNOSTIC candidates only |

---

## Layer 12 — Human Review

| Field | Value |
|-------|-------|
| Research recommendation | Double annotation; adjudication; stratified reviewer queues |
| Current MARS/ORCA evidence | Review workbook generated; approval gates contract v0 |
| Artifact paths | `artifacts/` review workbook; `artifacts/approval-gates-contract-v0.md` |
| Maturity | PARTIAL |
| Confirmed capability | HITL gate vocabulary documented; workbook exists for v1 diagnostic |
| Missing capability | Annotation guideline; double annotation on gold set |
| Risk | Self-validating pipeline |
| Required promotion artifact | P0-C, P0-D, P0-E |
| Dependencies | Benchmark charters |
| Corvonero blocking impact | HIGH — v1 workbook decisions not promotable |
| Implementation status | PARTIAL — diagnostic workbook only |

---

## Layer 13 — Semantic Core Authority

| Field | Value |
|-------|-------|
| Research recommendation | Freeze `Approved Semantic Core` before any campaign work |
| Current MARS/ORCA evidence | `CORVONERO-DIRECT-SEMANTIC-CORE-CANDIDATE-v1.md` — **NOT APPROVED**; campaign production contract v1 |
| Artifact paths | `semantic-core/CORVONERO-DIRECT-SEMANTIC-CORE-CANDIDATE-v1.md`; `contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` |
| Maturity | PARTIAL |
| Confirmed capability | Production contract documents authority chain concept |
| Missing capability | Approved Semantic Core artifact; P0-H contract |
| Risk | Pipeline contamination |
| Required promotion artifact | P0-H |
| Dependencies | P0-G threshold pass |
| Corvonero blocking impact | CRITICAL |
| Implementation status | CANDIDATE v1 INVALID |

---

## Layer 14 — Campaign Architecture

| Field | Value |
|-------|-------|
| Research recommendation | Campaign blueprint only after approved core |
| Current MARS/ORCA evidence | Campaign mode architecture v0; Corvonero PROJECT blocks production |
| Artifact paths | `campaign-modes/orca-campaign-mode-architecture-v0.md`; Corvonero `PROJECT.md` |
| Maturity | DOCUMENTED |
| Confirmed capability | Documentation-level separation; D7 prohibition |
| Missing capability | Corvonero campaign architecture for v2 line |
| Risk | Premature group design |
| Required promotion artifact | P0-H sign-off |
| Dependencies | Approved semantic core |
| Corvonero blocking impact | BLOCKED per D7 |
| Implementation status | NOT STARTED for Corvonero v2 |

---

## Layer 15 — Ad and Landing Alignment

| Field | Value |
|-------|-------|
| Research recommendation | Honest landing fit per cluster; alignment QA |
| Current MARS/ORCA evidence | Landing readiness layer v1; landing-match reviews |
| Artifact paths | `intelligence/landing-readiness-layer-v1.md`; `landing-match/` |
| Maturity | DOCUMENTED |
| Confirmed capability | Landing QA layer documented (Triumph-derived) |
| Missing capability | Corvonero landing routes for approved clusters |
| Risk | Ads compensate for bad core |
| Required promotion artifact | Campaign phase — post P0-H |
| Dependencies | Approved clusters |
| Corvonero blocking impact | BLOCKED per D7 |
| Implementation status | NOT STARTED for Corvonero |

---

## Layer 16 — Match Type and Bid Layer

| Field | Value |
|-------|-------|
| Research recommendation | Match/bid plan after blueprint; policy versioning |
| Current MARS/ORCA evidence | Triumph bid rules freeze; Commander baseline |
| Artifact paths | `freeze/ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md` |
| Maturity | DOCUMENTED |
| Confirmed capability | Triumph Search bid doctrine frozen |
| Missing capability | Corvonero match-type production plan |
| Risk | Match strategy rewriting core |
| Required promotion artifact | Post semantic-core gate |
| Dependencies | P0-H |
| Corvonero blocking impact | BLOCKED per D7 |
| Implementation status | NOT STARTED for Corvonero |

---

## Layer 17 — Production Dataset

| Field | Value |
|-------|-------|
| Research recommendation | Export tables/JSON with schema validation |
| Current MARS/ORCA evidence | Triumph schema/instances; exporter CLI |
| Artifact paths | `ppc/triumph-manipulator/schema/` |
| Maturity | VALIDATED |
| Confirmed capability | Triumph production dataset path battle-tested |
| Missing capability | Corvonero production dataset from approved core |
| Risk | Semantic decisions mutated at export |
| Required promotion artifact | P0-H + export QA |
| Dependencies | Approved core |
| Corvonero blocking impact | BLOCKED per D7 |
| Implementation status | Triumph only — not Corvonero |

---

## Layer 18 — Platform Export

| Field | Value |
|-------|-------|
| Research recommendation | Commander/XLSX export with pre-export QA |
| Current MARS/ORCA evidence | PPC exporter production baseline v1; Commander template SoT |
| Artifact paths | `freeze/ppc-exporter-production-baseline-v1/` |
| Maturity | VALIDATED |
| Confirmed capability | Triumph Commander export baseline frozen |
| Missing capability | Corvonero Commander export |
| Risk | Export mutates semantics |
| Required promotion artifact | External artefact QA layer |
| Dependencies | P0-H |
| Corvonero blocking impact | BLOCKED per D7 |
| Implementation status | NOT STARTED for Corvonero |

---

## Layer 19 — External Artifact QA

| Field | Value |
|-------|-------|
| Research recommendation | JSON/XLSX/API parity; checksum; mandatory human check |
| Current MARS/ORCA evidence | Commander hygiene audit; validation CLI (Triumph) |
| Artifact paths | `freeze/ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md` |
| Maturity | VALIDATED |
| Confirmed capability | Triumph hygiene checklist and battle findings |
| Missing capability | Corvonero export QA |
| Risk | Silent mutations |
| Required promotion artifact | Reuse Triumph QA patterns in Corvonero charter |
| Dependencies | Production dataset |
| Corvonero blocking impact | BLOCKED per D7 |
| Implementation status | Triumph only |

---

## Layer 20 — Post-Launch Search-Term Learning

| Field | Value |
|-------|-------|
| Research recommendation | Feedback loop after launch; not pre-launch core excuse |
| Current MARS/ORCA evidence | Search terms review assembly; Google/Yandex reports cited in research |
| Artifact paths | `search-terms-review/`; research source ledger platform entries |
| Maturity | DOCUMENTED |
| Confirmed capability | Human-operated search-term review docs |
| Missing capability | Corvonero post-launch loop (no launch yet) |
| Risk | «Fix in search terms» rationalizing bad core |
| Required promotion artifact | P0-A policy on post-launch vs pre-launch authority |
| Dependencies | Launch (prohibited until gates) |
| Corvonero blocking impact | N/A until launch authorized |
| Implementation status | NOT STARTED for Corvonero |

---

## Summary

| Maturity | Layer count |
|----------|-------------|
| ABSENT | 1 |
| DOCUMENTED | 6 |
| PARTIAL | 10 |
| PILOT | 2 |
| VALIDATED | 3 (Triumph export path — not Semantic Intelligence admission) |

**Critical Corvonero blockers:** Layers 6–11, 13 — diagnostic outputs invalid; Layers 14–19 blocked by D7.
