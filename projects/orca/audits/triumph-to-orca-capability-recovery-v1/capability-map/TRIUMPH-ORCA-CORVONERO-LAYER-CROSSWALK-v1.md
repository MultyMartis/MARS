# Triumph — ORCA — Corvonero Layer Crosswalk v1

**Machine-readable:** [`triumph-orca-corvonero-layer-crosswalk-v1.json`](triumph-orca-corvonero-layer-crosswalk-v1.json)

| Functional capability | Triumph actual | Pre-SI ORCA | SI P0 (SI-01–17) | Corvonero clean-room | Gap / duplication |
|----------------------|----------------|-------------|------------------|---------------------|-------------------|
| Business scope lock | Route freeze 12/12 | Route freeze docs; Intelligence v0 | SI-01 Business Context | Intake + 34 services | **Corvonero: scope exists but admission ignores** |
| Market evidence | **Not in repo pipeline**; MIG keyword off | Research layer v0; MIG optional | SI-02 Market Evidence | Wordstat Pass A 2399 rows | **Triumph: scenario-first; Corvonero: corpus-first** |
| Demand proof for ACCEPT | Operator curation (64 phrases) | Doctrine intent-first | SI-03 + P0-C commercial evidence | Regex + service regex | **SI documents fix; not integrated** |
| Architecture freeze before semantics | **CONFIRMED** | Freeze milestones | SI-04 Architecture Freeze | Groups **not** frozen before admission | **Missing in Corvonero** |
| Phrase normalization | N/A (small set) | — | SI-05 Normalization | **CONFIRMED** | Reusable |
| Intent screening | SE rules in validation | semantic-validation-rules | SI-06 Screening | Regex classifyIntent | **Weak rules vs P0-C** |
| Commercial eligibility | Operator + SE-03 | CM rules | SI-07 Admission | commercialEligibility bulk | **FAILED — 1892 accepts** |
| ABSTAIN | Manual operator HOLD | approval gates | SI-07 + P0-C | HOLD bucket only — no block | **NEW in P0 — needed** |
| Service mapping | Group = route owner | landing routing | SI-08 Mapping | mapService regex | **Too permissive** |
| Clustering | 12 groups by design | intent groups doc | SI-09 Clustering | Post-hoc clusterKey | **Order inverted** |
| Negatives | Cross-matrix pre-export | CROSS-NEGATIVE-RULES | SI-11 Negatives | After bad accepts | **Ownership violated** |
| Semantic freeze | JSON SoT | content-packs | SI-12 Freeze | Candidate v1 failed | **Not reached** |
| Export validation | 345 rules | validation-cli | SI-16 QA | BLOCKED | Triumph pattern not reused |
| Campaign contract gate | Informal | 2026-06 contract | Planned in SI | **NOT CONSUMED** | **Integration gap** |
| Benchmark / gold labels | None | None | P0-D proposed | None | **NEW — on hold** |
| Landing Readiness | URL sync battle | LRL v1 docs | SI-14 Landing alignment | Not in semantic pipeline | **Documented only** |

## Renaming vs genuine improvement

| Old label (Triumph) | New label (SI/P0) | Genuinely new? |
|--------------------|-------------------|----------------|
| Intent purity / one group one intent | Primary intent taxonomy + invariants | **Formalization** — enforcement still needed |
| Operator phrase judgment | ACCEPT/REJECT/ABSTAIN annotation | **Strengthening** — ABSTAIN explicit |
| 345 export validation rules | Universal benchmark 1200–2000 phrases | **Different product** — admission eval vs export QA |
| JSON SoT | Semantic record schema v1 | **Formalization** for interchange |
| Battle lessons | SI architecture risks R-01–R-18 | **Consolidation** |

## Enforcement improvement assessment

**P0 SI design would improve enforcement IF integrated before Corvonero rerun.** As documentation-only, it **duplicates** Triumph tacit practice without closing the Corvonero gap.
