# ORCA Enforcement Gap Matrix v1

**Machine-readable:** [`orca-enforcement-gap-matrix-v1.json`](orca-enforcement-gap-matrix-v1.json)

| Rule | Source | Intended consumer | Actual consumer | Enforcement | Bypass route | Observed failure | Required fix | Priority | New implementation? |
|------|--------|-------------------|-----------------|-------------|--------------|------------------|--------------|----------|---------------------|
| topic ≠ intent | P0-C; SI admission | SI-07 admission | Regex classifier | DOCUMENTATION ONLY | `COMMERCIAL SERVICE` on topic match | 1892 accepts | Integrate commercial evidence check | **P0** | **INTEGRATE** existing P0-C |
| service scope ≠ demand proof | ORCA-LAW-01; contract A | Semantic admission | Scope file only | MANUAL EXPECTATION | mapService regex | Product queries accepted | Scope cannot imply ACCEPT | **P0** | **ENFORCE** contract |
| ACCEPT requires commercial evidence | P0-C COMMERCIAL-EVIDENCE | Annotator / classifier | None | NOT CONSUMED | Auto ELIGIBLE | career/edu/DIY blur | Wire evidence fields | **P0** | **INTEGRATE** |
| ABSTAIN under ambiguity | P0-C ABSTAIN | Admission | HOLD label only | SOFT WARNING | Promote to ELIGIBLE | False precision | Default ABSTAIN not ELIGIBLE | **P0** | **INTEGRATE** |
| Service mapping after eligibility | SI flow; LAW-08 | SI-08 after SI-07 | Mapping same pass | NOT CONSUMED | Order shortcut | Wrong ownership | Reorder pipeline | **P1** | **INTEGRATE** |
| Clustering after ownership | Triumph; SI-09 | Post-admission | clusterKey early | NOT CONSUMED | Cluster before accept | Clusters on bad set | Freeze architecture first | **P1** | **INTEGRATE** |
| Negatives after ownership | LAW-08; CROSS-NEGATIVE | Post-ownership | After bulk accept | NOT CONSUMED | discoverNegatives on bad set | Cosmetic negatives | Triumph order | **P1** | **REUSE** Triumph pattern |
| Semantic freeze | Triumph JSON SoT | Pre-export | Not reached | NOT CONSUMED | — | No freeze artifact | Block export without freeze | **P1** | **EXTEND** |
| Export cannot mutate semantics | Contract I | Exporter | N/A blocked | HARD BLOCK | — | — | Maintain block | **P2** | No |
| Operator sign-off | approval-gates | Launch | D7 production block | HARD BLOCK production | Semantic stage | Late workbook | Sign-off before bulk accept | **P0** | **ENFORCE** gate |
| Provenance | P0-B schema | Semantic records | MIG ledger only | PARTIAL | — | Ledger OK | Full decision trace | **P1** | **INTEGRATE** schema |
| Versioning | Freeze discipline | All stages | Partial | MANUAL EXPECTATION | — | v1 diagnostic frozen OK | Version contracts | **P2** | **EXTEND** |
| Independent validation | LAW-14; P0-D | Benchmark + export | Triumph export only | PARTIAL | — | No admission benchmark | B0 after integration | **P1** | **NEW** benchmark rows later |
