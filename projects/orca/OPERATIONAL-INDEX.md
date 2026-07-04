# ORCA Operational Index

## Live-First Start

Use this index when an operator needs a fast PPC review session, not a full architecture pass.

## FAST PATH

Default to `fast-path/README.md`.

Recommended default path:

1. Define one PPC object.
2. Open one primary review.
3. Add one support signal only if the decision is blocked.
4. Capture top 3 findings.
5. Make one PPC decision or mark SAFE UNKNOWN.
6. STOP NOW.

Document gravity warning: the main overload risk is opening "just one more document." More ORCA reading is usually not more PPC clarity.

## Minimal Session Path

1. Define one PPC object: query, ad, landing page, or search-term set.
2. Pick one primary review from Starter Core.
3. Add at most one support signal if it changes the decision.
4. Record top 3 findings in `reports/orca-live-session-report-template-v1.md`.
5. Stop.

## Recommended Max Review Depth

- One primary checklist.
- One support signal checklist.
- Top 3 findings.
- One PPC decision or one SAFE UNKNOWN.
- Normal target: 10-20 minutes per PPC object.

## Starter Core

- `fast-review/mobile-serp-review-v1.md` - quick mobile SERP scan.
- `fast-review/landing-mismatch-review-v1.md` - query/ad/landing mismatch check.
- `fast-review/cta-pattern-review-v1.md` - CTA clarity and pressure review.
- `fast-review/mobile-friction-review-v1.md` - mobile conversion friction review.
- `essential-signals/trust-patterns-v1.md` - trust cues worth noting.
- `essential-signals/aggregator-pressure-v1.md` - marketplace and directory pressure.
- `essential-signals/semantic-contamination-v1.md` - non-commercial and mixed-intent leakage.

## STOP ANALYSIS Cues

Stop analysis when:

- STOP NOW: one PPC decision is clear enough;
- STOP NOW: three findings already exist;
- STOP NOW: the next document is being opened "just in case";
- the next note will not change the PPC action;
- the finding is already clear enough for a human decision;
- the evidence is weak and would require guessing;
- the review is becoming a full audit;
- the operator is comparing documents instead of reviewing PPC evidence;
- a platform change needs fresh human confirmation.

## Anti-Fatigue Cues

- Shorter is safer when judgment quality drops.
- Fast Path is the default; Starter Core is not a menu to exhaust.
- Do not open every related document.
- Do not classify every weak term.
- Do not inventory every competitor proof point.
- Mark SAFE UNKNOWN instead of forcing certainty.
- Split the session if a second PPC object appears.

## Assembly Areas

- `search-terms-review/` - semantic cleanliness and negative keyword review.
- `landing-match/` - intent-to-page fit.
- `ad-copy/` - ad message and CTA fit.
- `campaign-qa-assembly/` - final human QA before platform work.

## ORCA Standards (ORCA-RS)

Research publication standards — **ORCA-owned**. Website Factory **consumes** outputs; Factory **does not** own these standards.

| Doc | Role |
|-----|------|
| [orca-standards-register-v1.md](orca-standards-register-v1.md) | Standards index — ORCA-RS-* |
| [standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md](standards/ORCA-RS-001-EXECUTIVE-RESEARCH-PUBLICATION-STANDARD-v1.md) | **ACTIVE** — Executive Research Package; Publication Gate; two-level research model |
| [standards/README.md](standards/README.md) | Standards folder entry |

**Reference implementation:** BZPM Market Intelligence — Executive Presentation Package v2.1 RU — `projects/website-factory/execution-cases/bzpm-market-intelligence/executive-report/`

**Factory consumer lanes:** [../mars-website-factory/research-standards-v1.md](../mars-website-factory/research-standards-v1.md) · [../mars-website-factory/publication-standards-v1.md](../mars-website-factory/publication-standards-v1.md)

## ORCA Content Export Layer v0

Landing **semantic** export (content packs → DOCX / Markdown → Website Factory). **Not** Commander `exporter-cli`. **Not** runtime.

| Doc | Role |
|-----|------|
| [content-packs/README.md](content-packs/README.md) | Layer entry — pack ≠ HTML |
| [content-packs/OPERATIONAL-INDEX.md](content-packs/OPERATIONAL-INDEX.md) | Reading order, schemas, workflows, exporters |
| [content-packs/export-pipeline-v0.md](content-packs/export-pipeline-v0.md) | Research → pack → export → Factory |
| [content-packs/semantic-lock-export-rules-v0.md](content-packs/semantic-lock-export-rules-v0.md) | MODE 1 export + Factory lock rules |
| [content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md](content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md) | Reference capability pack (Triumph 5 т) |

**Bridge:** approved pack → [intelligence/orca-website-factory-semantic-lock-v0.md](intelligence/orca-website-factory-semantic-lock-v0.md) → Factory handoff ([content-packs/workflows/pack-to-factory-workflow-v0.md](content-packs/workflows/pack-to-factory-workflow-v0.md)).

## ORCA Calibration Layer v0

Human-operated loop: research / packs / PPC ↔ Factory implementation ↔ operational lessons. **Not** analytics or runtime.

| Doc | Role |
|-----|------|
| [calibration/README.md](calibration/README.md) | Layer entry |
| [calibration/OPERATIONAL-INDEX.md](calibration/OPERATIONAL-INDEX.md) | Reading order — first case: Triumph master hot |
| [calibration/orca-calibration-system-v0.md](calibration/orca-calibration-system-v0.md) | System definition + drift philosophy |

**Canonical case v0:** [calibration/triumph-manipulator/](calibration/triumph-manipulator/) — «Аренда манипулятора в Краснодаре» (`grp_fc12_zakaz`, `workspaces/triumph-manipulator-landing-v6/`).

## ORCA Intelligence Foundation v0

Pre-implementation architecture layer — intake, projects, evidence, campaign modes, artifacts, research, Factory semantic lock. **Not** runtime. **Not** orchestration.

| Doc | Role |
|-----|------|
| [orca-operational-principles-v0.md](orca-operational-principles-v0.md) | Layer principles and gate questions |
| [intake/orca-universal-intake-architecture-v0.md](intake/orca-universal-intake-architecture-v0.md) | Raw pack → manifest → normalize → distribute |
| [projects/project-structure-contract-v0.md](projects/project-structure-contract-v0.md) | Canonical per-project folder tree |
| [projects/project-md-contract-v0.md](projects/project-md-contract-v0.md) | `PROJECT.md` navigation and status contract |
| [evidence/evidence-classification-system-v0.md](evidence/evidence-classification-system-v0.md) | Evidence grading vocabulary |
| [campaign-modes/orca-campaign-mode-architecture-v0.md](campaign-modes/orca-campaign-mode-architecture-v0.md) | Search / RSYA / retarget / brand / local / experimental separation |
| [intelligence/orca-website-factory-semantic-lock-v0.md](intelligence/orca-website-factory-semantic-lock-v0.md) | ORCA → Website Factory content lock |
| [intelligence/orca-factory-bridge-index-v0.md](intelligence/orca-factory-bridge-index-v0.md) | ORCA → Factory handoff flow index |
| [artifacts/orca-artifact-system-v0.md](artifacts/orca-artifact-system-v0.md) | Artifact types and lifecycle |
| [artifacts/approval-gates-contract-v0.md](artifacts/approval-gates-contract-v0.md) | HITL approval gates (no auto-launch) |
| [research/orca-research-layer-v0.md](research/orca-research-layer-v0.md) | Human-operated research collection |

## ORCA PPC Semantic Intelligence — World Practice Research (2026-06)

**Analytical source only** — not approved architecture, not runtime, not phrase authority. Operator decisions D1–D7 recorded. Campaign production and Corvonero semantic rerun **blocked** until promotion backlog P0-A through P0-G pass and Semantic Core sign-off (P0-H).

| Doc | Role |
|-----|------|
| [research/ppc-semantic-intelligence/world-practice-2026-06/README.md](research/ppc-semantic-intelligence/world-practice-2026-06/README.md) | Package entry — lifecycle and canonical source |
| [research/ppc-semantic-intelligence/world-practice-2026-06/decisions/ORCA-PPC-SEMANTIC-INTELLIGENCE-OPERATOR-DECISIONS-v1.md](research/ppc-semantic-intelligence/world-practice-2026-06/decisions/ORCA-PPC-SEMANTIC-INTELLIGENCE-OPERATOR-DECISIONS-v1.md) | Operator decisions D1–D7 |
| [research/ppc-semantic-intelligence/world-practice-2026-06/gap-analysis/ORCA-PPC-SEMANTIC-INTELLIGENCE-GAP-MATRIX-v1.md](research/ppc-semantic-intelligence/world-practice-2026-06/gap-analysis/ORCA-PPC-SEMANTIC-INTELLIGENCE-GAP-MATRIX-v1.md) | 20-layer research-to-ORCA gap matrix |
| [research/ppc-semantic-intelligence/world-practice-2026-06/promotion/ORCA-PPC-SEMANTIC-INTELLIGENCE-PROMOTION-BACKLOG-v1.md](research/ppc-semantic-intelligence/world-practice-2026-06/promotion/ORCA-PPC-SEMANTIC-INTELLIGENCE-PROMOTION-BACKLOG-v1.md) | P0-A through P0-H selective promotion backlog |

**Canonical source:** `research/ppc-semantic-intelligence/world-practice-2026-06/ORCA-PPC-SEMANTIC-CORE-WORLD-PRACTICE-RESEARCH-v1.md` (SHA-256 verified at intake). **Role:** analytical source only — not architecture authority.

**Corvonero clean-room v1:** `DIAGNOSTIC FAILED — COMMERCIAL ADMISSION LOGIC NOT APPROVED` — see [projects/corvonero-direct-v2-clean-room/PROJECT.md](projects/corvonero-direct-v2-clean-room/PROJECT.md). Reusable corpus preserved; semantic decisions frozen. **Mode:** CONSERVATIVE (initial admission, post-gates). **Rerun:** BLOCKED.

## ORCA Semantic Intelligence Architecture v1

**Document-first target architecture** — approved specification; not runtime, not classifier, implementation not started.

| Doc | Role |
|-----|------|
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md) | Architecture Decision Record — **APPROVED — IMPLEMENTATION NOT STARTED** |
| [architecture/semantic-intelligence/decisions/ORCA-SEMANTIC-INTELLIGENCE-ADR-V1-OPERATOR-APPROVAL.md](architecture/semantic-intelligence/decisions/ORCA-SEMANTIC-INTELLIGENCE-ADR-V1-OPERATOR-APPROVAL.md) | Operator approval record A1–A7 |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-RESEARCH-PROMOTION-MATRIX-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-RESEARCH-PROMOTION-MATRIX-v1.md) | Selective research promotion (20 items) |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-AUTHORITY-MODEL-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-AUTHORITY-MODEL-v1.md) | 12-rank authority hierarchy |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-FLOW-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-FLOW-v1.md) | Layers SI-01–SI-17, state machine, prohibited shortcuts |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-ADMISSION-POLICY-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-ADMISSION-POLICY-v1.md) | ACCEPT / REJECT / ABSTAIN policy and risk modes |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-QUALITY-GATES-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-QUALITY-GATES-v1.md) | D3 thresholds + proposed metrics |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-COMPONENT-RESPONSIBILITY-MATRIX-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-COMPONENT-RESPONSIBILITY-MATRIX-v1.md) | Rules, models, LLM, human, operator boundaries |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-CONTRACT-FAMILY-PLAN-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-CONTRACT-FAMILY-PLAN-v1.md) | 12 planned contracts — status PLANNED |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-MIGRATION-BOUNDARY-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-MIGRATION-BOUNDARY-v1.md) | Reusable vs diagnostic vs must-create |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ARCHITECTURE-RISKS-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ARCHITECTURE-RISKS-v1.md) | Risk register R-01–R-18 |
| [architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ARCHITECTURE-VALIDATION-v1.md](architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-ARCHITECTURE-VALIDATION-v1.md) | Documentation validation — PASS |

## ORCA Semantic Intelligence — Taxonomy and Record Schema v1 (P0-B)

**Implementation-neutral specification locus** — not runtime, not classifier, not benchmark. Status: **APPROVED — IMPLEMENTATION NOT STARTED** (operator B1–B7).

| Doc | Role |
|-----|------|
| [semantic-intelligence/README.md](semantic-intelligence/README.md) | P0-B locus entry — taxonomy, schema, invariants, fixtures |
| [semantic-intelligence/taxonomy/ORCA-SEMANTIC-TAXONOMY-PRINCIPLES-v1.md](semantic-intelligence/taxonomy/ORCA-SEMANTIC-TAXONOMY-PRINCIPLES-v1.md) | 15 design principles |
| [semantic-intelligence/taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md](semantic-intelligence/taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md) | 26 primary intents |
| [semantic-intelligence/schemas/ORCA-SEMANTIC-RECORD-SCHEMA-v1.md](semantic-intelligence/schemas/ORCA-SEMANTIC-RECORD-SCHEMA-v1.md) | Canonical semantic record schema |
| [semantic-intelligence/contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md](semantic-intelligence/contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md) | 20 record invariants |
| [semantic-intelligence/decisions/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-DECISION-v1.md](semantic-intelligence/decisions/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-DECISION-v1.md) | P0-B decision record |

| [semantic-intelligence/decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md](semantic-intelligence/decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md) | P0-B operator approval B1–B7 |

**Promotion backlog P0-B:** `APPROVED — CHECKPOINTED` (commit `3151953`).

## ORCA Semantic Intelligence — Annotation Guideline v1 (P0-C)

**Human annotation specification** — not runtime, not classifier, not benchmark. Status: **APPROVED — IMPLEMENTATION NOT STARTED** (operator C1–C7).

| Doc | Role |
|-----|------|
| [semantic-intelligence/annotation/README.md](semantic-intelligence/annotation/README.md) | P0-C locus entry |
| [semantic-intelligence/annotation/guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md](semantic-intelligence/annotation/guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md) | Main annotation handbook |
| [semantic-intelligence/annotation/decision-trees/ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md](semantic-intelligence/annotation/decision-trees/ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md) | Decision trees — ACCEPT / REJECT / ABSTAIN terminals |
| [semantic-intelligence/annotation/examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md](semantic-intelligence/annotation/examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md) | Training illustrations — not gold labels |
| [semantic-intelligence/annotation/decisions/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md](semantic-intelligence/annotation/decisions/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md) | P0-C decision record |
| [semantic-intelligence/annotation/decisions/ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md](semantic-intelligence/annotation/decisions/ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md) | P0-C operator approval C1–C7 |

**Promotion backlog P0-C:** `APPROVED — CHECKPOINTED` (commit `78b0557`).

## Triumph-to-ORCA Capability Recovery Audit v1

**Forensic audit** — no implementation. Status: **APPROVED — CHECKPOINTED** (decision I1, 2026-06-22).

| Doc | Role |
|-----|------|
| [audits/triumph-to-orca-capability-recovery-v1/README.md](audits/triumph-to-orca-capability-recovery-v1/README.md) | Audit locus entry |
| [audits/triumph-to-orca-capability-recovery-v1/reports/REPORT-triumph-to-orca-capability-recovery-audit-v1.md](audits/triumph-to-orca-capability-recovery-v1/reports/REPORT-triumph-to-orca-capability-recovery-audit-v1.md) | Full audit report |
| [audits/triumph-to-orca-capability-recovery-v1/decisions/ORCA-P0-D-BENCHMARK-CHARTER-HOLD-v1.md](audits/triumph-to-orca-capability-recovery-v1/decisions/ORCA-P0-D-BENCHMARK-CHARTER-HOLD-v1.md) | P0-D hold record |

| [audits/triumph-to-orca-capability-recovery-v1/decisions/TRIUMPH-TO-ORCA-CAPABILITY-RECOVERY-AUDIT-APPROVAL-v1.md](audits/triumph-to-orca-capability-recovery-v1/decisions/TRIUMPH-TO-ORCA-CAPABILITY-RECOVERY-AUDIT-APPROVAL-v1.md) | Audit approval (I1) |

**Next gate:** P0-I integration pilot (phrase selection and execution) → operator review of pilot outputs.

## ORCA Semantic Intelligence — Admission Integration (P0-I)

**Integration and enforcement** — bounded core checkpointed. Status: **CORE IMPLEMENTATION APPROVED — INTEGRATION PILOT AUTHORIZED**.

| Doc | Role |
|-----|------|
| [semantic-intelligence/integration/README.md](semantic-intelligence/integration/README.md) | P0-I locus entry |
| [semantic-intelligence/integration/runtime/README.md](semantic-intelligence/integration/runtime/README.md) | Runtime I-01–I-07 |
| [semantic-intelligence/integration/decisions/ORCA-ADMISSION-ENFORCEMENT-CORE-OPERATOR-APPROVAL-v1.md](semantic-intelligence/integration/decisions/ORCA-ADMISSION-ENFORCEMENT-CORE-OPERATOR-APPROVAL-v1.md) | Operator approval K1–K9 |
| [semantic-intelligence/integration/charters/ORCA-SEMANTIC-ADMISSION-INTEGRATION-CHARTER-v1.md](semantic-intelligence/integration/charters/ORCA-SEMANTIC-ADMISSION-INTEGRATION-CHARTER-v1.md) | Master integration charter |
| [semantic-intelligence/integration/decisions/ORCA-P0-I-ADMISSION-INTEGRATION-OPERATOR-APPROVAL-v1.md](semantic-intelligence/integration/decisions/ORCA-P0-I-ADMISSION-INTEGRATION-OPERATOR-APPROVAL-v1.md) | Operator approval J1–J7 |
| [semantic-intelligence/integration/decisions/ORCA-P0-I-OPERATOR-DECISIONS-v1.md](semantic-intelligence/integration/decisions/ORCA-P0-I-OPERATOR-DECISIONS-v1.md) | Operator decisions I2–I7 |

**Audit v1:** `APPROVED — CHECKPOINTED` (commit `a09380d`).

## ORCA Semantic Intelligence — Universal Benchmark Charter v1 (P0-D)

**Benchmark program charter** — not runtime, not classifier, not benchmark rows. Status: **PROPOSED — ON HOLD** (pending capability recovery audit operator review; uncommitted).

| Doc | Role |
|-----|------|
| [semantic-intelligence/benchmark/README.md](semantic-intelligence/benchmark/README.md) | P0-D locus entry |
| [semantic-intelligence/benchmark/charters/ORCA-UNIVERSAL-SEMANTIC-BENCHMARK-CHARTER-v1.md](semantic-intelligence/benchmark/charters/ORCA-UNIVERSAL-SEMANTIC-BENCHMARK-CHARTER-v1.md) | Master benchmark charter |
| [semantic-intelligence/benchmark/decisions/ORCA-UNIVERSAL-BENCHMARK-CHARTER-DECISION-v1.md](semantic-intelligence/benchmark/decisions/ORCA-UNIVERSAL-BENCHMARK-CHARTER-DECISION-v1.md) | P0-D decision record |

**Promotion backlog P0-A:** `APPROVED — CHECKPOINTED` (commit `f17c270`).  
**Promotion backlog P0-B:** `APPROVED — CHECKPOINTED` (commit `3151953`).  
**P0-C:** `APPROVED — CHECKPOINTED` (commit `78b0557`, C1–C7).  
**P0-I:** `DIAGNOSTIC INTEGRATION EVIDENCE — NOT PRODUCTION WORKFLOW` — reclassification [ORCA-P0-I-PILOT-RECLASSIFICATION-DECISION-v1](semantic-intelligence/integration/decisions/ORCA-P0-I-PILOT-RECLASSIFICATION-DECISION-v1.md).  
**I-01–I-07:** `APPROVED — CHECKPOINTED`.  
**I-08:** `TECHNICAL PASS — DIAGNOSTIC EVIDENCE ONLY`.  
**P0-D:** `ON HOLD`.  
**Search PPC Lifecycle v1:** `APPROVED — CHECKPOINTED` — [projects/mars-search-ppc-production/](../mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md). Wave 1 state enforcement authorized.  
**Blocked:** classifier, benchmark rows, Corvonero rerun, campaign production, Commander.

**Contracts (v0):** [landing-route-registry-contract-v0.md](intelligence/landing-route-registry-contract-v0.md) · [ppc-landing-qa-contract-v0.md](intelligence/ppc-landing-qa-contract-v0.md) · [competitor-snapshot-contract-v0.md](research/competitor-snapshot-contract-v0.md) · [research-session-snapshot-contract-v0.md](research/research-session-snapshot-contract-v0.md) · [moderation-incident-registry-v0.md](moderation/moderation-incident-registry-v0.md)

## ORCA Campaign Production Contract v1

**Authority layer above classifier, repair package, and pipeline validators.** Derived from Triumph Manipulator battle production evidence. **Not** runtime.

| Doc | Role |
|-----|------|
| [contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md](contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md) | Canonical production contract — scope, seeds, viability, QA boundary |
| [contracts/orca-campaign-production-contract-v1.json](contracts/orca-campaign-production-contract-v1.json) | Machine-readable contract |
| [contracts/orca-campaign-production-invariants-v1.json](contracts/orca-campaign-production-invariants-v1.json) | Invariant registry |
| [knowledge/triumph-manipulator-production-evidence-inventory.md](knowledge/triumph-manipulator-production-evidence-inventory.md) | Triumph evidence inventory |
| [knowledge/triumph-manipulator-production-process-v1.md](knowledge/triumph-manipulator-production-process-v1.md) | Reconstructed Triumph production process |
| [knowledge/triumph-derived-orca-laws-v1.md](knowledge/triumph-derived-orca-laws-v1.md) | 15 reusable ORCA laws |
| [architecture/orca-production-contract-integration-plan-v1.md](architecture/orca-production-contract-integration-plan-v1.md) | Pipeline authority integration plan |
| [tools/validate-campaign-production-contract.mjs](tools/validate-campaign-production-contract.mjs) | Read-only contract validator |

**Corvonero v7 contract gate (FINAL):** [projects/corvonero-yandex-direct/production/validation/orca-production-contract-audit-v7.md](projects/corvonero-yandex-direct/production/validation/orca-production-contract-audit-v7.md) — **PASS — V7 AUTHORITY SYNCHRONIZED**; actual XLSX review and Commander dry-run authorized after external file review. Authority sync: [operator-scope-authority-sync-v7.json](projects/corvonero-yandex-direct/production/audit/operator-scope-authority-sync-v7.json).

## ORCA Landing Readiness Layer v1

Source-agnostic landing verification between Semantic and PPC — deployed copy and URL truth before export. **Not** runtime. **Not** Website Factory dependency. Battle source: [freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md](freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md).

| Doc | Role |
|-----|------|
| [intelligence/landing-readiness-layer-v1.md](intelligence/landing-readiness-layer-v1.md) | Layer architecture — problem, position, source-agnostic philosophy |
| [intelligence/landing-ready-contract-v1.md](intelligence/landing-ready-contract-v1.md) | Landing Ready Contract — URL, copy, CTA, PPC alignment, readiness gate |
| [intelligence/final-website-copy-pack-v1.md](intelligence/final-website-copy-pack-v1.md) | Final Website Copy Pack artifact — semantic pack ≠ deployed copy |

**Intake drop zone:** `incoming/orca/<project-id>-raw-pack/` (see intake architecture).

## Active ORCA project containers

| project_id | Status | Entry |
|------------|--------|-------|
| `triumph-manipulator-krasnodar` | launch-prep (Search export) | [projects/triumph-manipulator-krasnodar/PROJECT.md](projects/triumph-manipulator-krasnodar/PROJECT.md) |
| `corvonero-yandex-direct` | **HISTORICAL DIAGNOSTIC — NOT SEMANTIC SOURCE** (v1–v7.1) | [projects/corvonero-yandex-direct/PROJECT.md](projects/corvonero-yandex-direct/PROJECT.md) |
| `corvonero-direct-v2-clean-room` | **FROZEN PENDING SEARCH PPC PRODUCTION LIFECYCLE IMPLEMENTATION AND GAP CLOSURE** | [projects/corvonero-direct-v2-clean-room/PROJECT.md](projects/corvonero-direct-v2-clean-room/PROJECT.md) |

## MARS Search PPC Production Lifecycle v1

**Canonical cross-system lifecycle** for Yandex Direct search campaigns. **Status:** `PROPOSED — OPERATOR REVIEW`.

| Doc | Role |
|-----|------|
| [../mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md](../mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md) | Primary lifecycle authority (SPPC-01–23) |
| [../mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs](../mars-search-ppc-production/validators/validate-search-ppc-lifecycle.mjs) | Lifecycle readiness validator — `IMPLEMENTED — NOT VALIDATED AT SCALE` |
| [../mars-search-ppc-production/reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](../mars-search-ppc-production/reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md) | Gap audit — `COMPLETE` |
| [../mars-search-ppc-production/roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md](../mars-search-ppc-production/roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md) | Repair roadmap — `PROPOSED` |

**ORCA consumer obligation:** stages SPPC-04–09, campaign production stages SPPC-14–20 — link to lifecycle; do not duplicate full text.

## ORCA Route Family Freeze v1

**Triumph Manipulator** — production semantic route family frozen 2026-05-28 (12/12 packs, pre-implementation rollout). **Not** launch approval, **not** runtime.

| Doc | Role |
|-----|------|
| [freeze/route-family-freeze-v1/ORCA-ROUTE-FAMILY-FREEZE-v1.md](freeze/route-family-freeze-v1/ORCA-ROUTE-FAMILY-FREEZE-v1.md) | Main freeze — family complete, differentiation, pack format, ORCA ↔ Factory |
| [freeze/route-family-freeze-v1/ROUTE-FAMILY-INDEX-v1.md](freeze/route-family-freeze-v1/ROUTE-FAMILY-INDEX-v1.md) | Per-route table (semantic class, tone, trust, CTA, Factory/mobile/calibration) |
| [freeze/route-family-freeze-v1/ROLLUP-STATUS-v1.md](freeze/route-family-freeze-v1/ROLLUP-STATUS-v1.md) | READY vs PENDING rollup |
| [freeze/route-family-freeze-v1/SURVIVABILITY-CHECKPOINT-v1.md](freeze/route-family-freeze-v1/SURVIVABILITY-CHECKPOINT-v1.md) | Git/backup checkpoint — label `orca-route-family-freeze-v1` |
| [freeze/route-family-freeze-v1/FACTORY-HANDOFF-STATE-v1.md](freeze/route-family-freeze-v1/FACTORY-HANDOFF-STATE-v1.md) | Factory vs ORCA roles at handoff |
| [freeze/route-family-freeze-v1/KNOWN-OPEN-ITEMS-v1.md](freeze/route-family-freeze-v1/KNOWN-OPEN-ITEMS-v1.md) | Open items + SAFE UNKNOWN register |

**Coordination (live):** [coordination/remaining-routes-status-matrix-v1.md](coordination/remaining-routes-status-matrix-v1.md) · [coordination/route-priority-roadmap-v1.md](coordination/route-priority-roadmap-v1.md)

## ORCA PPC Exporter Production Baseline v1

**Triumph Manipulator Search PPC** — production export baseline frozen 2026-05-29 (ORCA → JSON → Exporter v1.2 → XLSX → Commander → Human QA). **Not** launch, **not** ad/copy/URL edits, **not** runtime.

| Doc | Role |
|-----|------|
| [freeze/ppc-exporter-production-baseline-v1/PPC-EXPORTER-PRODUCTION-BASELINE-v1.md](freeze/ppc-exporter-production-baseline-v1/PPC-EXPORTER-PRODUCTION-BASELINE-v1.md) | Main freeze — pipeline, SoT hierarchy, export READY gates |
| [freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md](freeze/ppc-exporter-production-baseline-v1/COMMANDER-TEMPLATE-SOT-v1.md) | Commander Search Manual Bids Template SoT (`template-v1.xlsx`) |
| [freeze/ppc-exporter-production-baseline-v1/EXPORTER-V1.2-APPROVAL-v1.md](freeze/ppc-exporter-production-baseline-v1/EXPORTER-V1.2-APPROVAL-v1.md) | Exporter transport split v1.2 approval |
| [freeze/ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md](freeze/ppc-exporter-production-baseline-v1/BID-MANAGEMENT-RULES-v1.md) | Default bid range 400–600 ₽ · within-group spread 10–90 ₽ |
| [freeze/ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md](freeze/ppc-exporter-production-baseline-v1/CROSS-NEGATIVE-RULES-v1.md) | Route-family cross-negative matrix — mandatory pre-export |
| [freeze/ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md](freeze/ppc-exporter-production-baseline-v1/COMMANDER-HYGIENE-AUDIT-v1.md) | Pre-export READY hygiene checklist |
| [freeze/ppc-exporter-production-baseline-v1/COMMANDER-CALIBRATION-FINDINGS-v1.md](freeze/ppc-exporter-production-baseline-v1/COMMANDER-CALIBRATION-FINDINGS-v1.md) | Human calibration findings from full cycle |
| [freeze/ppc-exporter-production-baseline-v1/GIT-CHECKPOINT-v1.md](freeze/ppc-exporter-production-baseline-v1/GIT-CHECKPOINT-v1.md) | Git checkpoint — label `orca-ppc-exporter-production-baseline-v1` |

**Template asset:** `ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx`

## ORCA Battle Pilot Triumph Search v1

**Triumph Manipulator Search PPC** — first real Commander import battle milestone frozen 2026-05-30 (ORCA → JSON → Exporter v1.4 → XLSX → Direct Commander → Human QA). **Not** launch approval, **not** runtime.

| Doc | Role |
|-----|------|
| [freeze/battle-pilot-triumph-search-v1/README.md](freeze/battle-pilot-triumph-search-v1/README.md) | Main battle freeze — outcome, artifact map, backups |
| [freeze/battle-pilot-triumph-search-v1/BATTLE-PILOT-SUMMARY-v1.md](freeze/battle-pilot-triumph-search-v1/BATTLE-PILOT-SUMMARY-v1.md) | Battle timeline, confirmed systems, gaps |
| [freeze/battle-pilot-triumph-search-v1/COMMANDER-IMPORT-FINDINGS-v1.md](freeze/battle-pilot-triumph-search-v1/COMMANDER-IMPORT-FINDINGS-v1.md) | Real Commander import observations |
| [freeze/battle-pilot-triumph-search-v1/CAMPAIGN-SETTINGS-LAYER-v1.md](freeze/battle-pilot-triumph-search-v1/CAMPAIGN-SETTINGS-LAYER-v1.md) | XLSX transport vs post-import UI setup |
| [freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md](freeze/battle-pilot-triumph-search-v1/ORCA-LESSONS-LEARNED-v1.md) | Deep post-battle analysis (10 areas) |
| [freeze/battle-pilot-triumph-search-v1/ORCA-UPGRADE-BACKLOG-v1.md](freeze/battle-pilot-triumph-search-v1/ORCA-UPGRADE-BACKLOG-v1.md) | P0/P1/P2 upgrade backlog |
| [freeze/battle-pilot-triumph-search-v1/NEXT-CHAT-MIGRATION-PROMPT-v1.md](freeze/battle-pilot-triumph-search-v1/NEXT-CHAT-MIGRATION-PROMPT-v1.md) | Migration prompt — «ORCA Upgrade After Battle Test» |
| [freeze/battle-pilot-triumph-search-v1/STABLE-BACKUP-MANIFEST-v1.md](freeze/battle-pilot-triumph-search-v1/STABLE-BACKUP-MANIFEST-v1.md) | Backup locations, reproduction, restore |

**Stable backups:** [archive/stable-orca-after-triumph-battle-v1/](archive/stable-orca-after-triumph-battle-v1/) · [ppc/triumph-manipulator/archive/stable-search-rk-after-commander-import-v1/](ppc/triumph-manipulator/archive/stable-search-rk-after-commander-import-v1/)

## Project operational packs

- `ppc/triumph-manipulator/` - Triumph Manipulator search PPC pack (doctrine, intent tiers, landing blueprints, Commander export foundation). Start: `ppc/triumph-manipulator/OPERATIONAL-INDEX.md`. Relationship to Intelligence Foundation: [ppc/triumph-manipulator/TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md](ppc/triumph-manipulator/TRIUMPH-RELATIONSHIP-TO-INTELLIGENCE-v0.md).

## Reality Audit

- `reality-audit/operator-fatigue-review-v1.md`
- `reality-audit/workflow-friction-review-v1.md`
- `reality-audit/low-value-layer-review-v1.md`
- `reality-audit/starter-core-survivability-v1.md`

## Boundaries

ORCA is a human-supervised PPC operational toolkit. It does not bid, launch, optimize, schedule, validate, or orchestrate campaigns.

Groundtruth ownership (ecosystem rule — ORCA = Interpretation Owner R2): [../../shared/contracts/groundtruth-ownership-rule-v1.md](../../shared/contracts/groundtruth-ownership-rule-v1.md)

ATLAS context binding (RC-01 pointers — `PROJECT.md` subject refs): [../../shared/contracts/atlas-context-binding-rule-v1.md](../../shared/contracts/atlas-context-binding-rule-v1.md)
