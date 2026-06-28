# OCPilot — Operational Index



**Lane:** B — External Systems (OpenCart).  

**Status:** documented navigation only; **not** automated router.  

**Domain root:** [README.md](README.md)  

**Family:** [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md)

**Localhost (pointer only, 2026-06-22):** OCPilot may consume OpenCart runtime profile on `E:\MARS-Localhost` via [MARS Localhost Infrastructure](../mars-localhost-infrastructure/MARS-LOCALHOST-CONSUMER-MODEL-v1.md) — **no** OCPilot runtime migration in MLI-00.



---



## Core Run



| # | Run | Status | Entry |

|---|-----|--------|-------|

| 1 | **Phase 0 — Repository Skeleton** | **DONE** | [phase-0-charter.md](phase-0-charter.md), [README.md](README.md) |

| 1.5 | **Baseline & Shared Access Alignment** | **DONE** | [baselines/README.md](baselines/README.md), [shared/external-access-patterns/](../../shared/external-access-patterns/README.md), [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md) |

| 2 | **Baseline Preparation — Ingestion Model** | **DONE** | [baseline-storage-model.md](baseline-storage-model.md), [baseline-comparison-methodology.md](baseline-comparison-methodology.md), [baseline-readiness-checklist.md](baseline-readiness-checklist.md), [baselines/README.md](baselines/README.md) |

| 2.5 | **Intake & Acquisition Layer** | **DONE** | [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md), [incoming/README.md](incoming/README.md), [intake-workflow.md](intake-workflow.md), [quarantine-policy.md](quarantine-policy.md), [templates/intake-report-template.md](templates/intake-report-template.md) |

| 2.6 | **Target Version Baseline Alignment** | **DONE** | [baselines/ocstore-3038-rs2/](baselines/ocstore-3038-rs2/README.md), [baselines/ocstore-3039-rs1/](baselines/ocstore-3039-rs1/README.md), [baselines/README.md](baselines/README.md) |

| 2.7 | **Archive Intake & Storage Policy** | **DONE** | [baselines/storage-policy.md](baselines/storage-policy.md), [archive-intake-rules.md](archive-intake-rules.md), [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md), [run-3-preparation.md](run-3-preparation.md), [incoming/baselines/README.md](incoming/baselines/README.md) |

| 3 | **First Baseline Acquisition** | **DONE** | [run-3-preparation.md](run-3-preparation.md), [comparison-notes/run-3-initial-comparison-v1.md](comparison-notes/run-3-initial-comparison-v1.md), [baselines/ocstore-3038-rs2/](baselines/ocstore-3038-rs2/README.md), [baselines/ocstore-3039-rs1/](baselines/ocstore-3039-rs1/README.md) |

| 3.5 | **Baseline Promotion** | **DONE** | [baseline-promotion-strategy.md](baseline-promotion-strategy.md), [baseline-sanitization-review.md](baseline-sanitization-review.md), [run-3.5-readiness-recheck.md](run-3.5-readiness-recheck.md), [comparison-notes/3038-vs-3039-structured-review-v1.md](comparison-notes/3038-vs-3039-structured-review-v1.md), [knowledge/](knowledge/README.md) |

| 3.6 | **Baseline Storage Review** | **DONE** | [storage-audit-run-3.6.md](storage-audit-run-3.6.md), [storage-strategy-options.md](storage-strategy-options.md), [recommended-storage-model.md](recommended-storage-model.md), [git-storage-policy.md](git-storage-policy.md), [knowledge/knowledge-storage-principles.md](knowledge/knowledge-storage-principles.md) |

| 3.7 | **External Storage Architecture** | **DONE** | [external-storage-registry.md](external-storage-registry.md), [baseline-storage-migration-plan.md](baseline-storage-migration-plan.md), [mars-storage-family-note.md](mars-storage-family-note.md) — root `C:\MARS Phenix\AI MARS STORAGE` |

| 4 | **First Project Site Intake** | **DONE** | [project-site-registry.md](project-site-registry.md), [sites/site-001/](sites/site-001/site-passport.md), [site-passport-standard.md](site-passport-standard.md), [baseline-match-workflow.md](baseline-match-workflow.md), [intake-readiness-review.md](intake-readiness-review.md) |

| 4.99 | **SITE-001 Audit Charter** | **DONE** | [sites/site-001/AUDIT-CHARTER.md](sites/site-001/AUDIT-CHARTER.md), [sites/site-001/materials/INTAKE-COMPLETE.md](sites/site-001/materials/INTAKE-COMPLETE.md), [intake-readiness-review.md](intake-readiness-review.md) |

| 4.100 | **SITE-001 Phase 1 — Brand Replacement Authorization** | **DONE** (decision: **NOT AUTHORIZED** — superseded for planning by Run 4.101) | [sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md), [sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.101 | **SITE-001 W1 Pre-Execution Package** | **DONE** (authorization: **AUTHORIZED WITH NOTES**; W1A gates closed 2026-06-08) | [sites/site-001/reports/SITE-001-W1-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W1-WRITE-CHARTER-v1.md), [sites/site-001/reports/SITE-001-W1-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W1-CHANGE-REQUEST-v1.md), [sites/site-001/reports/SITE-001-W1-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W1-ROLLBACK-PLAN-v1.md), [sites/site-001/reports/SITE-001-W1-BACKUP-PROCEDURE-v1.md](sites/site-001/reports/SITE-001-W1-BACKUP-PROCEDURE-v1.md), [sites/site-001/reports/SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](sites/site-001/reports/SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md), [sites/site-001/reports/SITE-001-W1-EXECUTION-PACK-v1.md](sites/site-001/reports/SITE-001-W1-EXECUTION-PACK-v1.md), [sites/site-001/reports/SITE-001-W1A-EXECUTION-SPEC-v1.md](sites/site-001/reports/SITE-001-W1A-EXECUTION-SPEC-v1.md), [sites/site-001/reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md), [sites/site-001/project-access-brief.md](sites/site-001/project-access-brief.md) |

| 4.102 | **SITE-001 W1A — Store Settings Execution** | **DONE** (2026-06-08; verdict: **PASS WITH NOTES**) | [sites/site-001/reports/SITE-001-W1A-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1A-EXECUTION-v1.md), [sites/site-001/reports/SITE-001-W1A-DECISION-v1.md](sites/site-001/reports/SITE-001-W1A-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.103 | **SITE-001 W1A — Post-Execution Audit** | **DONE** (2026-06-08; verdict: **PASS**) | [sites/site-001/reports/SITE-001-W1A-POST-AUDIT-v1.md](sites/site-001/reports/SITE-001-W1A-POST-AUDIT-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.104 | **SITE-001 W1B — Theme Branding Discovery** | **DONE** (2026-06-08; authorization: **AUTHORIZED WITH NOTES**) | [sites/site-001/reports/SITE-001-W1B-THEME-BRANDING-MAP-v1.md](sites/site-001/reports/SITE-001-W1B-THEME-BRANDING-MAP-v1.md), [sites/site-001/reports/SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.105 | **SITE-001 W1B–W1D — Theme + Controller + Logo Execution** | **DONE** (2026-06-08) | [SITE-001-W1B-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1B-EXECUTION-v1.md), [SITE-001-W1C-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1C-EXECUTION-v1.md), [SITE-001-W1D-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1D-EXECUTION-v1.md) |

| 4.106 | **SITE-001 W1F — Legacy Remediation (C1/B/A)** | **DONE** (2026-06-08; all **PASS WITH NOTES**) | [SITE-001-W1F-LEGACY-SWEEP-v1.md](sites/site-001/reports/SITE-001-W1F-LEGACY-SWEEP-v1.md), [SITE-001-W1F-C1-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1F-C1-EXECUTION-v1.md), [SITE-001-W1F-B-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1F-B-EXECUTION-v1.md), [SITE-001-W1F-A-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1F-A-EXECUTION-v1.md) |

| 4.107 | **SITE-001 Phase 1 — Stable Snapshot + Final Audit** | **DONE** (2026-06-09; interim decision: **PHASE 1 COMPLETE WITH NOTES**) | [SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md), [SITE-001-PHASE1-FINAL-AUDIT-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-v1.md), [SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md), [OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md](knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.108 | **SITE-001 W1G — SEO DB Cleanup** | **DONE** (2026-06-09; verdict: **PASS WITH NOTES**) | [SITE-001-W1G-SEO-DB-CLEANUP-v1.md](sites/site-001/reports/SITE-001-W1G-SEO-DB-CLEANUP-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.109 | **SITE-001 Phase 1 — Final Acceptance** | **DONE** (2026-06-09; decision: **PHASE 1 ACCEPTED WITH NOTES**) | [SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md), [SITE-001-PHASE1-FINAL-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.110 | **SITE-001 Phase 1 — Stable Checkpoint** | **DONE** (2026-06-09; decision: **APPROVED**; status: **ACTIVE**) | [SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md), [SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.111 | **SITE-001 W2 — Visual Refresh Discovery** | **DONE** (2026-06-09; decision: **DISCOVERY COMPLETE**) | [SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md), [SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.112 | **SITE-001 W2.1 — Visual Refresh Specification** | **DONE** (2026-06-09; decision: **READY FOR PHASE 2 IMPLEMENTATION**) | [SITE-001-W2-VISUAL-SPECIFICATION-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-SPECIFICATION-v1.md), [SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md](sites/site-001/reports/SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md), [SITE-001-W2-DECISION-v1.md](sites/site-001/reports/SITE-001-W2-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.113 | **SITE-002 Registration — ЗПМ (BZPM)** | **DONE** (2026-06-09; status: **AWAITING INTAKE**) | [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/project-access-brief.md](sites/site-002/project-access-brief.md), [sites/site-002/reports/SITE-002-REGISTRATION-v1.md](sites/site-002/reports/SITE-002-REGISTRATION-v1.md), [project-site-registry.md](project-site-registry.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.114 | **SITE-001 W3-C — Footer Reduction** | **DONE** (2026-06-09; decision: **PASS WITH NOTES**; **ROLLED BACK** Run 4.115) | [SITE-001-W3C-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3C-DISCOVERY-v1.md), [SITE-001-W3C-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3C-EXECUTION-v1.md), [SITE-001-W3C-DECISION-v1.md](sites/site-001/reports/SITE-001-W3C-DECISION-v1.md), [SITE-001-W2-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W2-WRITE-CHARTER-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.115 | **SITE-001 W3-C — T1 Rollback** | **DONE** (2026-06-09; decision: **PASS**) | [SITE-001-W3C-ROLLBACK-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-EXECUTION-v1.md), [SITE-001-W3C-ROLLBACK-DECISION-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-DECISION-v1.md), [SITE-001-W3C-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-PLAN-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.116 | **SITE-001 W3-V — Visual Layer Refresh** | **DONE** (2026-06-09; decision: **PASS WITH NOTES**) | [SITE-001-W3V-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3V-DISCOVERY-v1.md), [SITE-001-W3V-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3V-EXECUTION-v1.md), [SITE-001-W3V-DECISION-v1.md](sites/site-001/reports/SITE-001-W3V-DECISION-v1.md), [SITE-001-W3V-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3V-WRITE-CHARTER-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.117 | **SITE-001 W3-UX — Density & Visual Effectiveness Discovery** | **DONE** (2026-06-09; decision: **DISCOVERY COMPLETE**) | [SITE-001-W3UX-DENSITY-AUDIT-v1.md](sites/site-001/reports/SITE-001-W3UX-DENSITY-AUDIT-v1.md), [SITE-001-W3UX-DENSITY-DECISION-v1.md](sites/site-001/reports/SITE-001-W3UX-DENSITY-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.118 | **SITE-001 W3UX-C1 — Used Catalog Card Density** | **DONE** (2026-06-09; decision: **PASS WITH NOTES**) | [SITE-001-W3UX-C1-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-DISCOVERY-v1.md), [SITE-001-W3UX-C1-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-EXECUTION-v1.md), [SITE-001-W3UX-C1-DECISION-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-DECISION-v1.md), [SITE-001-W3UX-C1-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-WRITE-CHARTER-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.119 | **SITE-001 W3V2 — Visual Identity Refresh** | **DONE** (2026-06-09; decision: **PASS WITH NOTES**) | [SITE-001-W3V2-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3V2-DISCOVERY-v1.md), [SITE-001-W3V2-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3V2-EXECUTION-v1.md), [SITE-001-W3V2-DECISION-v1.md](sites/site-001/reports/SITE-001-W3V2-DECISION-v1.md), [SITE-001-W3V2-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3V2-WRITE-CHARTER-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.120 | **SITE-001 W3VIS-01 — Visual Hierarchy & Surface System Discovery** | **DONE** (2026-06-09; decision: **DISCOVERY COMPLETE**) | [SITE-001-W3VIS-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3VIS-01-DISCOVERY-v1.md), [SITE-001-W3VIS-01-DECISION-v1.md](sites/site-001/reports/SITE-001-W3VIS-01-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.121 | **SITE-001 W3VIS — T1 Rollback (01A + 01B)** | **DONE** (2026-06-09; decision: **PASS**) | [SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md), [SITE-001-W3VIS-ROLLBACK-DECISION-v1.md](sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.122 | **SITE-001 W3COLOR-01 — Global Palette & Atmosphere Discovery** | **DONE** (2026-06-09; decision: **DISCOVERY COMPLETE**) | [SITE-001-W3COLOR-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3COLOR-01-DISCOVERY-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.123 | **SITE-001 W3ATMOSPHERE-01A — Visual Preview** | **DONE** (2026-06-09; decision: **READY FOR W3ATMOSPHERE-01 EXECUTION**) | [SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.124 | **SITE-001 W3ATMOSPHERE-01 — Global Atmosphere Refresh** | **DONE** (2026-06-09; decision: **PASS WITH NOTES**) | [SITE-001-W3ATMOSPHERE-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-DISCOVERY-v1.md), [SITE-001-W3ATMOSPHERE-01-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-EXECUTION-v1.md), [SITE-001-W3ATMOSPHERE-01-DECISION-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-DECISION-v1.md), [SITE-001-W3ATMOSPHERE-01-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-WRITE-CHARTER-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.125 | **SITE-001 Website Factory — Design Direction Pack** | **DONE** (2026-06-09; decision: **READY FOR OCPILOT IMPLEMENTATION**) | [SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md), [SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md), [SITE-001-WEBSITE-FACTORY-DECISION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.126 | **SITE-001 W3WF-01 — Visual Impact Map** | **DONE** (2026-06-09; decision: **READY FOR W3WF-01 IMPLEMENTATION**) | [SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md](sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md), [SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md](sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.127 | **SITE-001 Visual Change Failure Audit** | **DONE** (2026-06-09; verdict: **mixed cause** — CSS live on TEST; **STOP** new design) | [SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](sites/site-001/reports/SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.128 | **SITE-001 W4 — Used PDP Structural Visual Slice** | **DONE** (2026-06-09; decision: **PASS WITH NOTES**) | [SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md), [SITE-001-W4-USED-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-EXECUTION-v1.md), [SITE-001-W4-USED-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-DECISION-v1.md), [SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.129 | **SITE-001 W4 Stable Backup + W4.1 Header & Hero Authority** | **DONE** (2026-06-09; decision: **PASS WITH NOTES**) | [SITE-001-W4-STABLE-BACKUP-v1.md](sites/site-001/reports/SITE-001-W4-STABLE-BACKUP-v1.md), [SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md), [SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md), [SITE-001-W4-1-HEADER-HERO-DECISION-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.130 | **SITE-001 W4.1 — Visual Proof Pack** | **DONE** (2026-06-09; verdict: **PARTIAL SUCCESS**) | [SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](sites/site-001/reports/SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.131 | **SITE-001 Website Factory — Concept Workshop** | **DONE** (2026-06-09; decision: **Concept B — Modern Dealer**; implementation **STOPPED**) | [SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md), [SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.135 | **SITE-001 W5 Stable Backup + W5-C Used PDP Commercial Stage** | **DONE** (2026-06-10; decision: **PASS WITH NOTES**) | [SITE-001-W5-STABLE-BACKUP-v1.md](sites/site-001/reports/SITE-001-W5-STABLE-BACKUP-v1.md), [SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md), [SITE-001-W5C-USED-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-EXECUTION-v1.md), [SITE-001-W5C-USED-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.136 | **SITE-001 WF-V2-W1 — Hybrid Header System** | **DONE** (2026-06-10; decision: **PASS WITH NOTES**) | [SITE-001-WF-V2-GAP-ANALYSIS-v1.md](sites/site-001/reports/SITE-001-WF-V2-GAP-ANALYSIS-v1.md), [SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md](sites/site-001/reports/SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md), [SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md), [SITE-001-WFV2-W1-HEADER-DECISION-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.137 | **SITE-001 WF-V2-W2 — Flat Used PDP Stage** | **DONE** (2026-06-10; decision: **PASS WITH NOTES**) | [SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md), [SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.138 | **SITE-002 — Stable Live Manual Compact Checkpoint** | **DONE** (2026-06-14; status: **STABLE LIVE CHECKPOINT** — superseded by 4.139 for live truth) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md), [sites/site-002/reports/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md](sites/site-002/reports/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/SITE-002-WORKING-RULES.md](sites/site-002/SITE-002-WORKING-RULES.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.139 | **SITE-002 — Stable Live PDP V5.1 Checkpoint** | **DONE** (2026-06-14; status: **STABLE LIVE CHECKPOINT** — superseded by 4.140 for live truth) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.140 | **SITE-002 — Stable Live M9.8 UX Polish Checkpoint** | **DONE** (2026-06-19; status: **STABLE LIVE CHECKPOINT** — superseded by 4.142 for live truth) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.141 | **SITE-002 — M9.8.9 Minor Fixes Pack #1 Registration** | **DONE** (2026-06-19; status: **ACTIVE WORK PACKAGE**) | [sites/site-002/reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md](sites/site-002/reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md), [BZPM-PRODUCT-ROADMAP-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.142 | **SITE-002 — Stable Live M9.8.9 Filter Recovery Checkpoint + Technical Knowledge Map** | **DONE** (2026-06-19; status: **STABLE LIVE CHECKPOINT** — superseded by 4.143 for live truth) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-AND-KNOWLEDGE-MAP-REGISTRATION.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-AND-KNOWLEDGE-MAP-REGISTRATION.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.143 | **SITE-002 — Stable Live M9.8.9 Filter UX Complete Checkpoint** | **DONE** (2026-06-19; status: **STABLE LIVE CHECKPOINT** — superseded by 4.144 for live truth) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-FILTER-UX-COMPLETE-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-FILTER-UX-COMPLETE-01.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.144 | **SITE-002 — Stable Live M9.8.9 Commercial Trust Checkpoint** | **DONE** (2026-06-21; status: **STABLE LIVE CHECKPOINT** — superseded by 4.145 for live truth) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md), [sites/site-002/reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/](sites/site-002/reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.145 | **SITE-002 — Stable Live M9.8.9 Catalog UX Complete Checkpoint** | **DONE** (2026-06-21; status: **STABLE LIVE CHECKPOINT** — superseded by 4.146 for live truth) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-CATALOG-UX-COMPLETE-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-CATALOG-UX-COMPLETE-01.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.146 | **SITE-002 — Stable Live M9.13 About Company Restored Checkpoint** | **DONE** (2026-06-23; status: **STABLE LIVE CHECKPOINT**) | [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md), [sites/site-002/reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](sites/site-002/reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.147 | **SITE-002 — BZPM Post-Recovery Completeness Reconciliation** | **DONE** (2026-06-28; documentation only) | [sites/site-002/reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md](sites/site-002/reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 4.148 | **SITE-002 — BZPM Recovery Closeout & Production Transition** | **DONE** (2026-06-28; documentation only) | [sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md), [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md), [BZPM-PRODUCT-ROADMAP-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) |
| 4.149 | **SITE-002 — M9.14 Delivery Implementation** | **DONE** (2026-06-28; verdict: **QA PASSED** on TEST) | [sites/site-002/reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](sites/site-002/reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.14-DELIVERY-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.14-DELIVERY-01.md), [sites/site-002/reports/m9.14-work/deploy-manifest.json](sites/site-002/reports/m9.14-work/deploy-manifest.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.150 | **SITE-002 — M9.15 Payment Implementation** | **DONE** (2026-06-28; verdict: **QA PASSED** on TEST) | [sites/site-002/reports/SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](sites/site-002/reports/SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md), [sites/site-002/reports/m9.15-work/deploy-manifest.json](sites/site-002/reports/m9.15-work/deploy-manifest.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.151 | **SITE-002 — M9.17 Warranty Implementation Charter** | **DONE** (2026-06-28; verdict: **READY** for implementation) | [sites/site-002/reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md](sites/site-002/reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.152 | **SITE-002 — M9.17 Warranty Implementation** | **DONE** (2026-06-28; checkpoint `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01`; QA PASS) | [sites/site-002/reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](sites/site-002/reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md), [sites/site-002/reports/m9.17-work/](sites/site-002/reports/m9.17-work/), [sites/site-002/qa/m9.17-warranty-screenshots/](sites/site-002/qa/m9.17-warranty-screenshots/) |
| 4.153 | **SITE-002 — M9.16 Dealers Implementation Charter** | **DONE** (2026-06-28; verdict: **READY** for implementation; B3 PLP out of scope) | [sites/site-002/reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md](sites/site-002/reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.154 | **SITE-002 — M9.16 Dealers Implementation** | **DONE** (2026-06-28; checkpoint `SITE-002-STABLE-LIVE-M9.16-DEALERS-01`; QA PASS; B3 OPEN) | [sites/site-002/reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION.md](sites/site-002/reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md), [sites/site-002/reports/m9.16-work/](sites/site-002/reports/m9.16-work/), [sites/site-002/qa/m9.16-dealers-screenshots/](sites/site-002/qa/m9.16-dealers-screenshots/) |
| 4.155 | **SITE-002 — M9.18 Custom Manufacturing Implementation Charter** | **DONE** (2026-06-28; verdict: **READY** for implementation; terminal corp page charter) | [sites/site-002/reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](sites/site-002/reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [sites/site-002/README.md](sites/site-002/README.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.156 | **SITE-002 — M9.18 Custom Manufacturing Implementation** | **DONE** (2026-06-28; checkpoint `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`; QA PASS; terminal corp page) | [sites/site-002/reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](sites/site-002/reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md), [sites/site-002/reports/m9.18-work/](sites/site-002/reports/m9.18-work/), [sites/site-002/qa/m9.18-custom-screenshots/](sites/site-002/qa/m9.18-custom-screenshots/) |
| 4.157 | **SITE-002 — Corporate Pages Visual Polish Pass 1** | **REJECTED BY OPERATOR** (2026-06-28; deployed then rolled back — see 4.158) | [sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md](sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md), [sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md](sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.158 | **SITE-002 — Corporate Pages Visual Polish Pass 1 Rollback + Pass 1.1 Rules** | **DONE** (2026-06-28; TEST `style.css` restored to Pre-Pass-1; Pass 1.1 operator rules registered) | [sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01-ROLLBACK.md](sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01-ROLLBACK.md), [sites/site-002/reports/site-002-visual-polish-pass1-work/rollback-manifest.json](sites/site-002/reports/site-002-visual-polish-pass1-work/rollback-manifest.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [sites/site-002/site-passport.md](sites/site-002/site-passport.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.159 | **SITE-002 — Corporate Pages Visual Polish Pass 1.1** | **DONE** (2026-06-28; superseded by 4.160) | [sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1.md](sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1.md), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.160 | **SITE-002 — Corporate Pages Visual Polish Pass 1.2** | **DONE** (2026-06-28; superseded by 4.161) | [sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](sites/site-002/reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md), [sites/site-002/reports/site-002-visual-polish-pass1.2-work/deploy-manifest.json](sites/site-002/reports/site-002-visual-polish-pass1.2-work/deploy-manifest.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.161 | **SITE-002 — Operator Manual Polish Canonical Checkpoint 01** | **DONE** (2026-06-29; superseded by 4.162 for checkpoint authority; visual baseline retained) | [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md), [sites/site-002/reports/site-002-operator-manual-polish-01-work/capture-manifest.json](sites/site-002/reports/site-002-operator-manual-polish-01-work/capture-manifest.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.162 | **SITE-002 — Local Fonts Migration** | **DONE** (2026-06-29; superseded by 4.163 for About authority; fonts retained) | [sites/site-002/reports/SITE-002-LOCAL-FONTS-MIGRATION.md](sites/site-002/reports/SITE-002-LOCAL-FONTS-MIGRATION.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md), [sites/site-002/reports/local-fonts-work/deploy-manifest.json](sites/site-002/reports/local-fonts-work/deploy-manifest.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.163 | **SITE-002 — M9.13 About Company Redesign Re-activation** | **DONE** (2026-06-29; checkpoint `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`; TEST deploy) | [sites/site-002/reports/SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md](sites/site-002/reports/SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md), [sites/site-002/reports/m9.13-restore-v2-work/restore-v2-manifest.json](sites/site-002/reports/m9.13-restore-v2-work/restore-v2-manifest.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |
| 4.164 | **SITE-002 — Home Commercial Trust Replacement** | **DONE** (2026-06-29; checkpoint `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01`; Home CTA only; `/katalog` legacy dealers preserved) | [sites/site-002/reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md](sites/site-002/reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md), [sites/site-002/baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md), [sites/site-002/reports/home-commercial-trust-work/fix-manifest-20260628-193747.json](sites/site-002/reports/home-commercial-trust-work/fix-manifest-20260628-193747.json), [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md), [OCPILOT-STATE.md](OCPILOT-STATE.md) |

| 5 | **First Read-Only Site Audit** | **paused** (init done) | [sites/site-001/reports/RUN-5-FIRST-FINDINGS.md](sites/site-001/reports/RUN-5-FIRST-FINDINGS.md), [freeze/site-001-pre-runtime-bridge/](freeze/site-001-pre-runtime-bridge/README.md), [shared/external-access-runtime/](../../shared/external-access-runtime/README.md) |

| 6 | **Catalog / Theme / Controller Planning** | planned | SAFE UNKNOWN — spec TBD after baseline + audit |

| 7 | **First Change Plan** | planned | SAFE UNKNOWN — spec TBD; rollback required per [boundaries.md](boundaries.md) |

| 8 | **First Battle Pilot** | planned | [battle-pilot-workflow.md](battle-pilot-workflow.md), [freeze/README.md](freeze/README.md) |



**Rule:** Runs **1** through **4.99** marked DONE. Run **5** initialization **done**; execution **paused** pending **External Access Runtime (EAR)** direction — not downgrading readiness.

---

## Run 4.128 deliverables (summary)

- [sites/site-001/reports/SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-DESIGN-PLAN-v1.md) — block grouping, preserved elements, CSS goals, visual change matrix
- [sites/site-001/reports/SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-WRITE-CHARTER-v1.md) · [SITE-001-W4-USED-PDP-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-CHANGE-REQUEST-v1.md) · [SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-ROLLBACK-PLAN-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-W4-USED-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-EXECUTION-v1.md) · [SITE-001-W4-USED-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-W4-USED-PDP-DECISION-v1.md) — execution cycle
- Backup `pre-w4-20260609` — `product.twig`, `main.css`, `media.css`
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W4 marked **DONE** · W3 cosmetic waves **STOPPED** for PDP

**Site modification:** TEST only — `product.twig` wrapper grouping + scoped W4 CSS. No PHP/JS/DB. No commit. No push. Production **NOT AUTHORIZED**.

**Operator takeaway:** Open [target used PDP](https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799) with hard refresh. Hero should read as single showroom card; trust strip is light (not dark nav clone). Visual HITL screenshots **PENDING**.

**Next gate:** Operator rates used PDP visual impact (target ≥7/10) → accept W4 or T1 rollback.

---

## Run 4.135 deliverables (summary)

- [sites/site-001/reports/SITE-001-W5-STABLE-BACKUP-v1.md](sites/site-001/reports/SITE-001-W5-STABLE-BACKUP-v1.md) — pre-W5-C stable checkpoint
- [sites/site-001/reports/SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-COMMERCIAL-STAGE-DESIGN-PLAN-v1.md) — commercial stage architecture; safety **SAFE**
- [sites/site-001/reports/SITE-001-W5C-USED-PDP-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-WRITE-CHARTER-v1.md) · [SITE-001-W5C-USED-PDP-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-CHANGE-REQUEST-v1.md) · [SITE-001-W5C-USED-PDP-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-ROLLBACK-PLAN-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-W5C-USED-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-EXECUTION-v1.md) · [SITE-001-W5C-USED-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-W5C-USED-PDP-DECISION-v1.md) — execution cycle
- Backup `pre-w5c-commercial-stage-20260610-0002` — header (backup only), product.twig, main.css, media.css
- Screenshots — `sites/site-001/qa/w5c-used-pdp-commercial-stage-screenshots/` (before/after × 6 desktop + 2 mobile)
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W5-C **DONE** on TEST; operator visual HITL **PENDING**

**Site modification:** TEST only — `product.twig` commercial stage wrappers + W5-C CSS block. No PHP/JS/DB. No footer edit. No commit. No push. Production **NOT AUTHORIZED**.

**Operator takeaway:** Hard-refresh [target used PDP](https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799) — hero + trust should read as one offer deck; price 52px anchor; modals light on «Купить в кредит». Compare before/after screenshots. Rate ≥7/10 or T1 rollback.

**Next gate:** Operator W5-C visual HITL → accept or T1 rollback from `pre-w5c-commercial-stage-20260610-0002`.

---

## Run 4.146 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md) — stable checkpoint after operator-approved About page restoration
- [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §17 About Page History, PRE-TASK rule for About page tasks
- [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md) — registration report
- [sites/site-002/reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](sites/site-002/reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md) — restoration evidence
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — authority → M9.13 About Company Restored 01

**Site modification:** **NONE** — documentation only. No FTP. No deploy.

**Authority:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`

**Supersedes for live truth:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`

**Registered scope:** catalog UX cluster (carried forward) · M9.13 About lifecycle (IMPLEMENTED · QA PASSED · REJECTED · RESTORED) · About page canonical = restored pre-redesign version

**PRE-TASK RULE:** for About page — read Knowledge Map §17 + restoration / redesign / polish reports before any new redesign; treat restored version as source of truth.

---

## Run 4.147 deliverables (summary)

- [sites/site-002/reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md](sites/site-002/reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md) — post-recovery completeness audit semantics reconciled against Web-GPT project context
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — cross-reference + M9.14/M9.15 **NOT_IMPLEMENTED** clarification

**Site modification:** **NONE** — documentation only.

**Index lag (acknowledged, not resolved):** dedicated runs still absent for Contacts delivery · Corporate Pages registration · Copy registration · M9.13 redesign/polish — see reconciliation §5. **DOCUMENTATION_LAG** only; artefacts exist elsewhere.

---

## Run 4.148 deliverables (summary)

- [sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](sites/site-002/reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) — BZPM UX Redesign recovery **CLOSED**; production preparation; operator implementation queue; active blockers B6/B8/B1/B3
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — project banner + lifecycle sync
- [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md) · [BZPM-PRODUCT-ROADMAP-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) — operator implementation order registered (design order unchanged)

**Site modification:** **NONE** — documentation only.

**Recovery status:** **CLOSED** — recovery is **not** an active blocker.

**Production status:** **READY AFTER OPERATOR GATES** — Corporate Pages implementation **NOT STARTED** (M9.14+).

**Authority unchanged:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01`

---

## Run 4.145 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md) — stable checkpoint after catalog UX cluster completion
- [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §16 Catalog State Persistence, PRE-TASK rule for filters/sort/pagination/limit/only_with_price
- [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-CATALOG-UX-COMPLETE-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-CATALOG-UX-COMPLETE-01.md) — registration report
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — authority → M9.8.9 Catalog UX Complete 01

**Site modification:** **NONE** — documentation only. No FTP. No deploy.

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` — **superseded by 4.146**

**Supersedes for live truth:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01`

**Registered scope:** filter recovery (06D–06M) · filter UX (04–08A) · tooltips (01) · Commercial Trust (03B/03C + operator polish) · catalog state persistence (09A–09C) · hub cleanup (10)

**Joint behaviour:** filter + limit + sort + pagination + only_with_price work together on PLP.

**PRE-TASK RULE:** for filters/sort/pagination/limit/only_with_price — read Knowledge Map §16 + passes 09A/09B/09C before any work.

---

## Run 4.144 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md) — stable checkpoint after filter recovery + filter UX + Commercial Trust + operator manual polish
- [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §14 Commercial Trust Block, PRE-TASK rule update for trust/CTA tasks
- [sites/site-002/reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/](sites/site-002/reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/) — FTP read-only capture (`blockcommercialtrust.twig`, `style.css`, `category.php`) + SHA256 manifest
- [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md) — registration report
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — authority → M9.8.9 Commercial Trust 01 (superseded by 4.145)

**Site modification:** **NONE** — documentation + read-only FTP capture only. No deploy.

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` — **superseded by 4.145** (live truth superseded by 4.146)

**Supersedes for live truth:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01`

**PRE-TASK RULE:** read Knowledge Map + latest Stable Checkpoint; for trust block / certificates / dealers form / category CTA — read §14 + checkpoint before any work.

**Explicitly not fixed:** limit + filter persistence · page-intro__description

---

## Run 4.143 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md) — metadata-only stable checkpoint after filter recovery + filter UX polish
- [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §7 Filter Architecture, §8 Live Files With Business Logic, PRE-TASK rule update
- [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-FILTER-UX-COMPLETE-01.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-M9.8.9-FILTER-UX-COMPLETE-01.md) — registration report
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — authority → M9.8.9 Filter UX Complete 01

**Site modification:** **NONE** — documentation only. No FTP. No deploy.

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` — **superseded by 4.144**

**Supersedes for live truth:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01`

**PRE-TASK RULE:** read Knowledge Map + latest Stable Checkpoint before any SITE-002 work; domain-specific rule for filter/catalog/1C/price/PLP in Knowledge Map §13.

---

## Run 4.142 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md) — metadata-only stable checkpoint after product reset, 1C import, filter recovery
- [sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](sites/site-002/knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — persistent technical knowledge map (1C, pricing, price index, filters, overlays, PDP, catalog)
- [sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-AND-KNOWLEDGE-MAP-REGISTRATION.md](sites/site-002/reports/SITE-002-STABLE-CHECKPOINT-AND-KNOWLEDGE-MAP-REGISTRATION.md) — registration report
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — authority → M9.8.9 Filter Recovery 01

**Site modification:** **NONE** — documentation only. No FTP. No deploy.

**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` — **superseded by 4.143**

**Supersedes for live truth:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`

**PRE-TASK RULE:** read Knowledge Map + latest Stable Checkpoint before any SITE-002 work.

---

## Run 4.141 deliverables (summary)

- [sites/site-002/reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md](sites/site-002/reports/SITE-002-M9.8.9-MINOR-FIXES-PACK-01-REGISTRATION.md) — M9.8.9 pack registration (8 tasks)
- [BZPM-PRODUCT-ROADMAP-v1.md](../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) — § M9.8.9 active work package
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [OCPILOT-STATE.md](OCPILOT-STATE.md) — active stage → M9.8.9

**Site modification:** **NONE** — documentation only. No FTP. No deploy.

**Authority unchanged at 4.141:** `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` — **superseded by 4.142**

**Next recommended task at 4.141:** **M9.8.9-06** Filter Bug Investigation — **resolved** by filter recovery wave; see 4.142

**Next gate:** Audit-only charter for M9.8.9-06 before any live filter fix.

---

## Run 4.140 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md) — metadata-only stable checkpoint after M9.8.1/2/5 + operator manual PLP polish
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) — updated active baseline and stable state
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — SITE-002 **STABLE LIVE CHECKPOINT** (M9.8 UX Polish 01)

**Site modification:** **NONE** — metadata/docs only. No FTP. No deploy. No file capture.

**Active live state:** M9.8.1 PDP Gallery Compact · M9.8.2 PDP Lightbox Constraints · M9.8.5 Products Per Page Selector · operator PLP/filter/breakpoint/CSS/Twig polish.

**Rollback source:** Beget full backup + current live TEST + file-level pass backups.

**Supersedes for live truth:** `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14`.

**Next gate:** Before next SITE-002 task — live-capture only the specific files in scope.

---

## Run 4.139 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) — metadata-only stable checkpoint after PDP V5.1 scroll offset polish
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) — updated active baseline and stable state
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — SITE-002 **STABLE LIVE CHECKPOINT** (PDP V5.1 + Category V2.3.1)

**Site modification:** **NONE** — metadata/docs only. No FTP. No deploy. No file capture.

**Active live state:** PDP V5.1 (specs collapse, scroll UX, scroll offset) · Category V2.3.1 · operator manual polish.

**Rollback source:** Beget global backup + operator live state on hosting.

**Supersedes for live truth:** `SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14` — **superseded by 4.140**.

**Next gate:** Before next SITE-002 task — live-capture only the specific files in scope.

---

## Run 4.138 deliverables (summary)

- [sites/site-002/baselines/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md](sites/site-002/baselines/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md) — metadata-only stable checkpoint definition
- [sites/site-002/reports/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md](sites/site-002/reports/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md) — registration report
- [sites/site-002/site-passport.md](sites/site-002/site-passport.md) · [sites/site-002/README.md](sites/site-002/README.md) · [sites/site-002/SITE-002-WORKING-RULES.md](sites/site-002/SITE-002-WORKING-RULES.md) — updated state and working rules
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — SITE-002 **STABLE LIVE CHECKPOINT**

**Site modification:** **NONE** — metadata/docs only. No FTP. No deploy. No file capture.

**Rollback source:** Beget global backup + operator live state on hosting.

**Next gate:** Before next SITE-002 task — live-capture only the specific files in scope.

---

## Run 4.137 deliverables (summary)

- [sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-WRITE-CHARTER-v1.md) · [SITE-001-WFV2-W2-FLAT-PDP-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-CHANGE-REQUEST-v1.md) · [SITE-001-WFV2-W2-FLAT-PDP-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-ROLLBACK-PLAN-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-EXECUTION-v1.md) · [SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md](sites/site-001/reports/SITE-001-WFV2-W2-FLAT-PDP-DECISION-v1.md) — execution cycle
- Backup `pre-wfv2-w2-flat-pdp-20260610-0304` — product.twig, main.css, media.css
- Screenshots — `sites/site-001/qa/wfv2-w2-flat-pdp-screenshots/` (before/after × 7 desktop + 2 mobile crops)
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — WF-V2-W2 **DONE** on TEST; operator visual HITL **PENDING**

**Site modification:** TEST only — `wfv2-flat-pdp` twig hook + WF-V2-W2 subtractive CSS block. No PHP/JS/DB. No header/footer/home/catalog. No commit. No push. Production **NOT AUTHORIZED**.

**Operator takeaway:** Hard-refresh [used PDP](https://sibcar.new-site.space/audi-a1-2012-s-probegom-149-000-km-799) — fewer boxes/borders; price 56px anchor; trust as single band; specs/equipment as flat grids. Compare before/after screenshots. If change not obvious → T1 rollback.

**Next gate:** Operator WF-V2-W2 visual HITL → accept or T1 rollback from `pre-wfv2-w2-flat-pdp-20260610-0304` → then authorize WF-V2-W3.

---

## Run 4.136 deliverables (summary)

- [sites/site-001/reports/SITE-001-WF-V2-GAP-ANALYSIS-v1.md](sites/site-001/reports/SITE-001-WF-V2-GAP-ANALYSIS-v1.md) · [SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md](sites/site-001/reports/SITE-001-WF-V2-IMPLEMENTATION-PLAN-v1.md) — planning inputs
- [sites/site-001/reports/SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-WRITE-CHARTER-v1.md) · [SITE-001-WFV2-W1-HEADER-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-CHANGE-REQUEST-v1.md) · [SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-ROLLBACK-PLAN-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-EXECUTION-v1.md) · [SITE-001-WFV2-W1-HEADER-DECISION-v1.md](sites/site-001/reports/SITE-001-WFV2-W1-HEADER-DECISION-v1.md) — execution cycle
- Backup `pre-wfv2-w1-header-20260610-0216` — header.twig, main.css, media.css
- Screenshots — `sites/site-001/qa/wfv2-w1-header-screenshots/` (before/after × 4 pages × desktop/mobile)
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — WF-V2-W1 **DONE** on TEST; operator visual HITL **PENDING**

**Site modification:** TEST only — hybrid header twig + WF-V2-W1 CSS block. No PHP/JS/DB. No product.twig. No commit. No push. Production **NOT AUTHORIZED**.

**Operator takeaway:** Hard-refresh [homepage](https://sibcar.new-site.space/) — light contact rail, dark primary band, light promo strip. Phone/WhatsApp only in top rail. Original logo visible. Compare before/after screenshots vs concept mock `01`.

**Next gate:** Operator WF-V2-W1 visual HITL → accept or T1 rollback from `pre-wfv2-w1-header-20260610-0216` → then authorize WF-V2-W2.

---

## Run 4.134 deliverables (summary)

- [sites/site-001/reports/SITE-001-W5A-STABILIZATION-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-WRITE-CHARTER-v1.md) · [SITE-001-W5A-STABILIZATION-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-CHANGE-REQUEST-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-W5A-STABILIZATION-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-EXECUTION-v1.md) · [SITE-001-W5A-STABILIZATION-DECISION-v1.md](sites/site-001/reports/SITE-001-W5A-STABILIZATION-DECISION-v1.md) — stabilization cycle
- Backup `pre-w5a-stabilization-20260609-2325` — `header.twig`, `main.css`, `media.css`
- Screenshots — `sites/site-001/qa/w5a-stabilization-screenshots/` (before/after × 3 pages × desktop/mobile)
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W5-A-S **DONE** on TEST; W5-A operator COMPLETE **NO** (HITL **PENDING**)

**Site modification:** TEST only — nav «Ещё» grouping + W5-A-S CSS block. No PHP/JS/DB. No commit. No push. Production **NOT AUTHORIZED**.

**Operator takeaway:** Hard-refresh [used catalog](https://sibcar.new-site.space/cars/) — promo strip should sit flush below header (no overlap). Hover «Услуги» and «Ещё» at 1280px. Compare before/after screenshots. If visual **PASS** → mark W5-A **COMPLETE** and authorize W5-B.

**Next gate:** Operator W5-A visual HITL → accept or T1 rollback from `pre-w5a-stabilization-20260609-2325` → then authorize W5-B.

---

## Run 4.133 deliverables (summary)

- [sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-WRITE-CHARTER-v1.md) · [SITE-001-W5A-HEADER-SHELL-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-CHANGE-REQUEST-v1.md) · [SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-ROLLBACK-PLAN-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-EXECUTION-v1.md) · [SITE-001-W5A-HEADER-SHELL-DECISION-v1.md](sites/site-001/reports/SITE-001-W5A-HEADER-SHELL-DECISION-v1.md) — execution cycle
- Backup `pre-w5a-header-shell-20260609-2251` — `header.twig`, `main.css`, `media.css`
- Screenshots — `sites/site-001/qa/w5a-header-shell-screenshots/` (before/after × 4 pages × desktop/mobile)
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W5-A **DONE** on TEST; operator visual HITL **PENDING**

**Site modification:** TEST only — `header.twig` DOM regroup + W5-A CSS block. No PHP/JS/DB. No commit. No push. Production **NOT AUTHORIZED**.

**Operator takeaway:** Hard-refresh [homepage](https://sibcar.new-site.space/) and [used catalog](https://sibcar.new-site.space/cars/). Header should read as **one dealer shell** (contact rail + primary band + inset promo) — not three competing bands. Sticky **gone**. Rate 3-second test; if subtle → T1 rollback per charter.

**Next gate:** Operator W5-A visual HITL → accept or T1 rollback → then authorize W5-B.

---

## Run 4.132 deliverables (summary)

- [sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md](sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-BLUEPRINT-v1.md) — Concept B architecture: current-state analysis · header/homepage/PDP blueprints · ASCII wireframes · visual impact map · W5-A…D phases · 3-second test
- [sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md](sites/site-001/reports/SITE-001-W5-FIRST-IMPRESSION-DECISION-v1.md) — blueprint **APPROVED**; 3→7/10 without full redesign **YES**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W5 blueprint **DONE**; operator HITL **PENDING**

**Site modification:** **NONE** — design blueprint only. No FTP · No CSS · No Twig · No DB.

**Operator takeaway:** Review six blueprint sections; confirm architecture or override. Implementation phases: W5-A header shell → W5-B homepage → W5-C magazine PDP → W5-D integration HITL. No OCPilot writes until W5 implementation charter.

**Next gate:** Operator sign-off on blueprint → authorize W5 implementation charter (separate task).

---

## Run 4.131 deliverables (summary)

- [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-WORKSHOP-v1.md) — 3 visual concepts (A Regional Pro · B Modern Dealer · C Premium Showroom); 3-second test; scope header + homepage + used PDP first screen
- [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-CONCEPT-DECISION-v1.md) — **Concept B selected**; A/C rejected; Graphite Salon / W3WF-01 superseded for first impression
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — implementation **STOPPED**; operator HITL **PENDING**

**Site modification:** **NONE** — design workshop only. No FTP · No CSS · No Twig · No DB.

**Operator takeaway:** Review three concepts; confirm Concept B or override. Sticky header direction **rejected**. No OCPilot writes until W5 First Impression charter.

**Next gate:** Operator sign-off on Concept B → Website Factory drafts W5 implementation charter (separate task).

---

## Run 4.130 deliverables (summary)

- [sites/site-001/reports/SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md](sites/site-001/reports/SITE-001-W4-1-VISUAL-PROOF-PACK-v1.md) — 7 desktop before/after pairs + header/promo/PDP hero crops; scoring; verdict **PARTIAL SUCCESS**
- Screenshots — `sites/site-001/qa/w4-1-header-hero-screenshots/` (16 full) + `crops/` (header, promo, PDP hero)
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W4.1 visual proof **DONE** · operator HITL **READY**

**Site modification:** **NONE** — read-only analysis of existing QA captures.

**Operator takeaway:** Promo strip (red → graphite CAPS) **YES** without A/B on used PDP + `/cars/`. Header polish **MAYBE**. Homepage first screen **NO**. Accept W4.1 or T1 rollback from `pre-w4-1-stable-20260609-1506`.

---

## Run 4.129 deliverables (summary)

- [sites/site-001/reports/SITE-001-W4-STABLE-BACKUP-v1.md](sites/site-001/reports/SITE-001-W4-STABLE-BACKUP-v1.md) — stable checkpoint `pre-w4-1-stable-20260609-1506` before W4.1
- [sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-DESIGN-PLAN-v1.md) · [SITE-001-W4-1-HEADER-HERO-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-WRITE-CHARTER-v1.md) · [SITE-001-W4-1-HEADER-HERO-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-CHANGE-REQUEST-v1.md) · [SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-ROLLBACK-PLAN-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-EXECUTION-v1.md) · [SITE-001-W4-1-HEADER-HERO-DECISION-v1.md](sites/site-001/reports/SITE-001-W4-1-HEADER-HERO-DECISION-v1.md) — execution cycle
- Backup `pre-w4-1-stable-20260609-1506` — 5 files (header, footer, product, main.css, media.css)
- Screenshots — `sites/site-001/qa/w4-1-header-hero-screenshots/` (16 before/after PNG)
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W4.1 marked **DONE** · stable backup **ACTIVE**

**Site modification:** TEST only — header/product twig classes + W4.1 CSS block. W4 Used PDP **preserved**. No footer edit. No commit. No push. Production **NOT AUTHORIZED**.

**Next gate:** ~~Operator rates first-screen visual impact~~ → superseded by Run **4.130** visual proof pack.

---

## Run 4.127 deliverables (summary)

- [sites/site-001/reports/SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md](sites/site-001/reports/SITE-001-VISUAL-CHANGE-FAILURE-AUDIT-v1.md) — read-only live HTTP audit: CSS load order, markers, selector hit/miss, cascade, cache, root cause
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — audit gate recorded; **new design / atmosphere CSS STOPPED**

**Site modification:** **NONE** — HTTP fetch + documentation only.

**Root cause:** **mixed cause** — W3ATMOSPHERE/W3V2 CSS **is on TEST and wins cascade**; operator sees no change primarily because deltas are **too weak** (incremental waves) + **expectation mismatch**; secondary **browser cache** risk (`max-age=604800`).

**Operator takeaway:** Hard-refresh `https://sibcar.new-site.space/` and compare QA before/after screenshots. Do **not** start new design waves until expectation workshop. W3WF-01 **ON HOLD**.

**Next gate:** Operator verification → choose audit §8 path C1 (W3WF consolidation) or C2 (structural charter).

---

## Run 4.126 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md](sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-MAP-v1.md) — 10-zone before/after vs **current TEST** (W3ATMOSPHERE active); reality check; design risk assessment
- [sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md](sites/site-001/reports/SITE-001-W3WF-01-VISUAL-IMPACT-DECISION-v1.md) — decision **READY FOR W3WF-01 IMPLEMENTATION**; honest LOW–MEDIUM perceptual delta vs live TEST
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3WF-01 visual impact gate recorded

**Site modification:** **NONE** — visual planning only. No FTP · No CSS · No Twig · No DB.

**Operator takeaway:** W3ATMOSPHERE already delivered ~70–80% «Graphite Salon»; W3WF-01 = consolidation + legacy purge, not second transformation.

**Next OCPilot wave:** Operator preview sign-off → W3WF-01 charter + CR + backup + CSS execution.

---

## Run 4.125 deliverables (summary)

- [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DESIGN-DIRECTION-v1.md) — design diagnosis; single direction «Graphite Salon»; palette/surfaces/depth/header/footer/forms/catalog/PDP widgets
- [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-IMPLEMENTATION-BRIEF-v1.md) — OCPilot CSS rules; allowed/forbidden properties; W3WF-01 phases A–J; 10-point acceptance checklist
- [sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DECISION-v1.md](sites/site-001/reports/SITE-001-WEBSITE-FACTORY-DECISION-v1.md) — decision **READY FOR OCPILOT IMPLEMENTATION**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — Website Factory design owner recorded; next wave **W3WF-01**

**Site modification:** **NONE** — design direction and planning only. No FTP · No CSS · No Twig · No DB.

**Next OCPilot wave:** **W3WF-01** — charter + CR + backup + CSS-only implementation per implementation brief.

---

## Run 4.124 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-WRITE-CHARTER-v1.md) · [SITE-001-W3ATMOSPHERE-01-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-CHANGE-REQUEST-v1.md) · [SITE-001-W3ATMOSPHERE-01-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-ROLLBACK-PLAN-v1.md) — pre-write package
- [sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-DISCOVERY-v1.md) · [SITE-001-W3ATMOSPHERE-01-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-EXECUTION-v1.md) · [SITE-001-W3ATMOSPHERE-01-DECISION-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01-DECISION-v1.md) — execution cycle
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3ATMOSPHERE-01 marked **DONE** · decision **PASS WITH NOTES**
- Backup: `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3atmosphere-01-20260609-1156\`
- Screenshots: `sites/site-001/qa/w3atmosphere-01-screenshots/` (24 files: before/after × desktop/tablet/mobile × 4 pages)

**Site modification:** **TEST ONLY** — `css/main.css` + `css/media.css` via FTP; caches cleared.

**Evidence (local):** `.recovery-temp/site-001-w3atmosphere-01-result.json`

---

## Run 4.123 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md](sites/site-001/reports/SITE-001-W3ATMOSPHERE-01A-VISUAL-PREVIEW-v1.md) — 8-zone before/after preview; top 10 visible / not-changed lists; invisible-improvement risk; decision **READY FOR W3ATMOSPHERE-01 EXECUTION**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3ATMOSPHERE preview marked **DONE**

**Site modification:** **NONE** — preview only; no FTP, CSS, Twig, cache, or admin.

---

## Run 4.122 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3COLOR-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3COLOR-01-DISCOVERY-v1.md) — palette/surface/depth inventory; `--w3color-*` token proposal; top 20 visual problems
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3COLOR-01 discovery marked **DONE**

**Site modification:** **NONE** — read-only HTTP probe + live CSS fetch.

**Evidence (local):** `.recovery-temp/site-001-w3color-01-probe.json`

---

**First project site:** SITE-001 (`sites/site-001/`) — **READY FOR AUDIT** (unchanged); intake closed Run 4.99.

**Second project site:** SITE-002 (`sites/site-002/`) — **STABLE TEST CHECKPOINT M9.7E HOMEPAGE COMPLETE** (2026-06-15); TEST `zpm.new-site.space`; active baseline `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE`; QA **33/33 PASS**; rollback = baseline files + category WebP + Beget global backup. CRO backlog: [REPORT-BZPM-CATALOG-IMPROVEMENT-BACKLOG.md](sites/site-002/reports/REPORT-BZPM-CATALOG-IMPROVEMENT-BACKLOG.md). [SITE-002-WORKING-RULES.md](sites/site-002/SITE-002-WORKING-RULES.md).

**Phase 1 (SITE-001):** Run **4.100** — initial authorization review (2026-06-07) **NOT AUTHORIZED**. Run **4.101** — W1 pre-execution package **complete** (2026-06-08). Runs **4.102–4.106** — W1A through W1F-A execution **complete** on TEST (2026-06-08). Run **4.107** — Phase 1 stable snapshot + interim final audit **complete** (2026-06-09). Run **4.108** — W1G DB SEO cleanup **complete** (2026-06-09). Run **4.109** — Phase 1 final acceptance **complete** (2026-06-09): decision **[PHASE 1 ACCEPTED WITH NOTES](sites/site-001/reports/SITE-001-PHASE1-FINAL-DECISION-v1.md)**; 13/13 public URLs legacy-clean. Run **4.110** — Phase 1 stable checkpoint **ACTIVE** (2026-06-09): decision **[APPROVED](sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md)**; official recovery point before Phase 2. Run **4.111** — W2 Visual Refresh Discovery **complete** (2026-06-09): decision **[DISCOVERY COMPLETE](sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md)**. Run **4.112** — W2.1 Visual Refresh Specification **complete** (2026-06-09): decision **[READY FOR PHASE 2 IMPLEMENTATION](sites/site-001/reports/SITE-001-W2-DECISION-v1.md)**; W3 execution **NOT AUTHORIZED** until Phase 2 write charter. Deferred W1F-D/E (SMTP, `anketa.php`, `backup_yml`). Next: Phase 2 write charter + authorization or **W1F-D** → **W1F-E**. Program state: [OCPILOT-STATE.md](OCPILOT-STATE.md).

### Operational lesson (Run 5 initialization)

| Topic | Finding |
|-------|---------|
| Bottleneck | **Artifact acquisition**, not audit logic or baseline readiness |
| Prior flow | Operator → WinSCP / manual exports → files → OCPilot |
| Target flow | SITE → [EAR](../../shared/external-access-runtime/README.md) → Snapshot Package → OCPilot |
| Future dependency | **EAR v1** — document-first under `shared/external-access-runtime/`; **no runtime claimed** |
| Freeze | [freeze/site-001-pre-runtime-bridge/](freeze/site-001-pre-runtime-bridge/README.md) |

**Knowledge layer:** [knowledge/](knowledge/README.md) — skeleton + [knowledge-storage-principles.md](knowledge/knowledge-storage-principles.md) (Run 3.6).

**Storage policy (canonical):** [recommended-storage-model.md](recommended-storage-model.md) — Option D; approved external root `C:\MARS Phenix\AI MARS STORAGE` ([external-storage-registry.md](external-storage-registry.md)); local promoted cache gitignored; grandfathered Run 3.5 trees unchanged.

**Priority first baselines:** `baselines/ocstore-3038-rs2/` and `baselines/ocstore-3039-rs1/` — **READY** for file-level comparison after Run 3.5 promotion ([run-3.5-readiness-recheck.md](run-3.5-readiness-recheck.md)). Canonical ZIPs remain in repo `incoming/baselines/` until migration ([baseline-storage-migration-plan.md](baseline-storage-migration-plan.md)).



---



---

---

---

---

## Run 4.121 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-EXECUTION-v1.md) — T1 restore `css/main.css` + `css/media.css` from `pre-w3vis-01a-20260609-0517`; cache clear; 9/9 verification
- [sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-DECISION-v1.md](sites/site-001/reports/SITE-001-W3VIS-ROLLBACK-DECISION-v1.md) — decision **PASS** · W3VIS-01A/01B inactive · next: **Global Palette Refresh**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3VIS rollback marked **DONE** · Global Palette Refresh **PLANNED**

**Site modification:** W3VIS rollback on TEST — `css/main.css`, `css/media.css` only — removes W3VIS-01A + W3VIS-01B blocks; W3UX-C1 **preserved**.

**Backup used:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3vis-01a-20260609-0517\`

**Evidence (local):** `.recovery-temp/site-001-w3vis-rollback-result.json`

---

## Run 4.120 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3VIS-01-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3VIS-01-DISCOVERY-v1.md) — hierarchy audit HF-01–HF-20 · surface map · PDP/catalog/home analysis
- [sites/site-001/reports/SITE-001-W3VIS-01-DECISION-v1.md](sites/site-001/reports/SITE-001-W3VIS-01-DECISION-v1.md) — decision **DISCOVERY COMPLETE** · top 10 impact changes · execution order
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3VIS-01 marked **DISCOVERY DONE**

**Site modification:** **NONE** — discovery only; superseded for execution by Global Palette Refresh direction.

**Evidence (local):** `.recovery-temp/site-001-w3vis-01-probe.json`

---

## Run 4.118 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3UX-C1-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-WRITE-CHARTER-v1.md) — W3UX-C1 write charter — **ACTIVE** (CSS-only, `.used_catalog`)
- [sites/site-001/reports/SITE-001-W3UX-C1-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-CHANGE-REQUEST-v1.md) — CR-SITE-001-W3UX-C1-2026-06
- [sites/site-001/reports/SITE-001-W3UX-C1-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-DISCOVERY-v1.md) — selector map U-01–U-11
- [sites/site-001/reports/SITE-001-W3UX-C1-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-EXECUTION-v1.md) — FTP upload, cache clear, 5/5 verification, −24% desktop card height
- [sites/site-001/reports/SITE-001-W3UX-C1-DECISION-v1.md](sites/site-001/reports/SITE-001-W3UX-C1-DECISION-v1.md) — decision **PASS WITH NOTES**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3UX-C1 marked **DONE**

**Site modification:** W3UX-C1 wave on TEST — `css/main.css`, `css/media.css` only — `.used_catalog` scoped density block.

**Backup:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3ux-c1-20260609-0416\`

**Screenshots:** `sites/site-001/qa/w3ux-c1-screenshots/` (before/after desktop, tablet, mobile)

---

## Run 4.116 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3V-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W3V-WRITE-CHARTER-v1.md) — W3-V Phase 2 write charter — **ACTIVE** (CSS-only)
- [sites/site-001/reports/SITE-001-W3V-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W3V-CHANGE-REQUEST-v1.md) — CR-SITE-001-W3V-2026-06-09
- [sites/site-001/reports/SITE-001-W3V-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3V-ROLLBACK-PLAN-v1.md) — T1 rollback instance (2 CSS files)
- [sites/site-001/reports/SITE-001-W3V-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3V-DISCOVERY-v1.md) — CSS inventory + visual baseline
- [sites/site-001/reports/SITE-001-W3V-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3V-EXECUTION-v1.md) — FTP upload, cache clear, 7/7 verification
- [sites/site-001/reports/SITE-001-W3V-DECISION-v1.md](sites/site-001/reports/SITE-001-W3V-DECISION-v1.md) — decision **PASS WITH NOTES**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3-V marked **DONE**

**Site modification:** W3-V wave on TEST — `css/main.css`, `css/media.css` only — **no twig/markup changes**.

**Backup:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3v-20260609-0327\`

---

## Run 4.115 deliverables (summary)

- [sites/site-001/reports/SITE-001-W3C-ROLLBACK-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-EXECUTION-v1.md) — T1 restore from `pre-w3c-20260609-0259`, cache clear, 7/7 verification
- [sites/site-001/reports/SITE-001-W3C-ROLLBACK-DECISION-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-DECISION-v1.md) — decision **PASS**
- [sites/site-001/reports/SITE-001-W3C-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-PLAN-v1.md) — T1 procedure instance
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3-C marked **ROLLED BACK**

**Site modification:** T1 rollback on TEST — restored `footer.twig`, `main.css`, `media.css` to pre-W3C state.

**Rollback source:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3c-20260609-0259\`

**Operator reason:** Visual direction not accepted. Beget global backup **not used**.

---

## Run 4.114 deliverables (summary)

- [sites/site-001/reports/SITE-001-W2-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W2-WRITE-CHARTER-v1.md) — Phase 2 write charter — **ACTIVE**
- [sites/site-001/reports/SITE-001-W2-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W2-CHANGE-REQUEST-v1.md) — CR-SITE-001-W3C-2026-06-09
- [sites/site-001/reports/SITE-001-W3C-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W3C-ROLLBACK-PLAN-v1.md) — W3-C rollback instance
- [sites/site-001/reports/SITE-001-W3C-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W3C-DISCOVERY-v1.md) — footer inventory + height baseline
- [sites/site-001/reports/SITE-001-W3C-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W3C-EXECUTION-v1.md) — FTP upload, cache clear, 7/7 verification
- [sites/site-001/reports/SITE-001-W3C-DECISION-v1.md](sites/site-001/reports/SITE-001-W3C-DECISION-v1.md) — decision **PASS WITH NOTES** — **superseded on TEST by Run 4.115 rollback**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W3-C execution recorded; later **ROLLED BACK** (Run 4.115)

**Site modification:** W3-C wave on TEST — `footer.twig`, `main.css`, `media.css` — **reverted** Run 4.115.

**Backup:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w3c-20260609-0259\`

---

## Run 4.112 deliverables (summary)

- [sites/site-001/reports/SITE-001-W2-VISUAL-SPECIFICATION-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-SPECIFICATION-v1.md) — Phase 2 visual goals, design tokens, component rules, footer/catalog/PDP strategies
- [sites/site-001/reports/SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md](sites/site-001/reports/SITE-001-W2-IMPLEMENTATION-ROADMAP-v1.md) — W3-A…F execution sequence with risk/rollback/UX impact
- [sites/site-001/reports/SITE-001-W2-DECISION-v1.md](sites/site-001/reports/SITE-001-W2-DECISION-v1.md) — decision **READY FOR PHASE 2 IMPLEMENTATION**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W2.1 specification marked **COMPLETE**

**Site modification:** **None** — documentation only.

---

## Run 4.111 deliverables (summary)

- [sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DISCOVERY-v1.md) — W2A–W2F theme/CSS/component/risk/readiness discovery
- [sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md](sites/site-001/reports/SITE-001-W2-VISUAL-REFRESH-DECISION-v1.md) — decision **DISCOVERY COMPLETE**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W2 discovery marked **COMPLETE**

**Site modification:** **None** — FTP read-only + HTTP fetch on TEST.

---

## Run 4.110 deliverables (summary)

- [sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-v1.md) — official Phase 1 stable checkpoint; recovery point before Phase 2; 13/13 verification summary; rollback + deferred inventory
- [sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-CHECKPOINT-DECISION-v1.md) — decision **APPROVED**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — Phase 1 Stable Checkpoint marked **ACTIVE**
- Recommended git tag: `site-001-phase1-stable-2026-06`

**Site modification:** **None** — documentation only.

---

## Run 4.109 deliverables (summary)

- [sites/site-001/reports/SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-ACCEPTANCE-v1.md) — final acceptance package; 13-URL verification matrix; deferred inventory; production blockers
- [sites/site-001/reports/SITE-001-PHASE1-FINAL-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-DECISION-v1.md) — decision **PHASE 1 ACCEPTED WITH NOTES**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — program state updated

**Site modification:** **None** — read-only HTTP verification + documentation only.

---

## Run 4.108 deliverables (summary)

- [sites/site-001/reports/SITE-001-W1G-SEO-DB-CLEANUP-v1.md](sites/site-001/reports/SITE-001-W1G-SEO-DB-CLEANUP-v1.md) — 206 DB rows updated; `/auto/` remediated; admin `product_form.twig` JS default fixed
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W1G marked **DONE**

**Site modification:** W1G wave only (TEST DB + one admin template) — documented in W1G report; not part of Run 4.109 acceptance run.

---

## Run 4.107 deliverables (summary)

- [sites/site-001/reports/SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md](sites/site-001/reports/SITE-001-PHASE1-STABLE-SNAPSHOT-v1.md) — Phase 1 stable checkpoint; waves W1A–W1F-A; rollback + backup status
- [sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-v1.md) — read-only HTTP audit of 14 URLs; controller meta generator table
- [sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md](sites/site-001/reports/SITE-001-PHASE1-FINAL-AUDIT-DECISION-v1.md) — decision **PHASE 1 COMPLETE WITH NOTES**
- [knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md](knowledge/OCPILOT-RULE-CONTROLLER-META-GENERATORS-v1.md) — OCPilot inspection rule for controller/DB meta generators
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — program state updated

**Site modification:** **None** — read-only HTTP audit + documentation only.

---

## Run 4.104 deliverables (summary)

- [sites/site-001/reports/SITE-001-W1B-THEME-BRANDING-MAP-v1.md](sites/site-001/reports/SITE-001-W1B-THEME-BRANDING-MAP-v1.md) — W1B theme inventory; replacement map; 7–10 files estimated; risk assessment
- [sites/site-001/reports/SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-W1B-AUTHORIZATION-REVIEW-v1.md) — verdict **AUTHORIZED WITH NOTES**; C-04 WhatsApp conditional
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W1B discovery marked **DONE**

**Site modification:** **None** — FTP read-only scan + HTTP spot-check on TEST.

---

## Run 4.103 deliverables (summary)

- [sites/site-001/reports/SITE-001-W1A-POST-AUDIT-v1.md](sites/site-001/reports/SITE-001-W1A-POST-AUDIT-v1.md) — W1A post-audit: 6 fields Unicode-checked; verdict **PASS**; no corrections
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W1A post-audit marked **DONE**

**Site modification:** **None** — read-only verification on TEST admin.

---

## Run 4.102 deliverables (summary)

- [sites/site-001/reports/SITE-001-W1A-EXECUTION-v1.md](sites/site-001/reports/SITE-001-W1A-EXECUTION-v1.md) — W1A execution report (before/after, cache, verification)
- [sites/site-001/reports/SITE-001-W1A-DECISION-v1.md](sites/site-001/reports/SITE-001-W1A-DECISION-v1.md) — verdict **PASS WITH NOTES**; rollback **NO**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — W1A marked **DONE**

**Site modification:** TEST only — admin Store Settings (`setting/setting`); 6 fields. No production. No commit.

---

## Run 4.101 deliverables (summary)

- [sites/site-001/reports/SITE-001-W1-WRITE-CHARTER-v1.md](sites/site-001/reports/SITE-001-W1-WRITE-CHARTER-v1.md) — TEST-only write charter; waves W1A–W1F; approval chain
- [sites/site-001/reports/SITE-001-W1-CHANGE-REQUEST-v1.md](sites/site-001/reports/SITE-001-W1-CHANGE-REQUEST-v1.md) — CR-SITE-001-W1-2026-06-08 — **READY FOR EXECUTION**
- [sites/site-001/reports/SITE-001-W1-ROLLBACK-PLAN-v1.md](sites/site-001/reports/SITE-001-W1-ROLLBACK-PLAN-v1.md) — rollback tiers T1/T2/T3
- [sites/site-001/reports/SITE-001-W1-BACKUP-PROCEDURE-v1.md](sites/site-001/reports/SITE-001-W1-BACKUP-PROCEDURE-v1.md) — pre-W1A backup checklist
- [sites/site-001/reports/SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](sites/site-001/reports/SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) — **AUTHORIZED WITH NOTES**; C-08 **SATISFIED**
- [sites/site-001/reports/SITE-001-W1A-EXECUTION-SPEC-v1.md](sites/site-001/reports/SITE-001-W1A-EXECUTION-SPEC-v1.md) — W1A Store Settings execution table
- [sites/site-001/reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md) — W1A **AUTHORIZED WITH NOTES**
- [sites/site-001/project-access-brief.md](sites/site-001/project-access-brief.md) — TEST write flags **YES**; approver **Андрей**; **PRODUCTION WRITES FORBIDDEN**
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — program state updated

**No site modification.** Documentation only.

---

## Run 4.100 deliverables (summary)

- [sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md](sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-REVIEW-v1.md) — Phase 1 readiness review; pre-execution checklist; incremental wave plan
- [sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) — decision **NOT AUTHORIZED** for immediate brand replacement execution on TEST
- [OCPILOT-STATE.md](OCPILOT-STATE.md) — program state updated for SITE-001 Phase 1 gate

**No site modification.** No FTP, admin writes, or deployment. Review and planning only.

---

## Run 4.99 deliverables (summary)

- [sites/site-001/AUDIT-CHARTER.md](sites/site-001/AUDIT-CHARTER.md) — read-only audit scope; status **READY FOR RUN 5**
- [sites/site-001/materials/INTAKE-COMPLETE.md](sites/site-001/materials/INTAKE-COMPLETE.md) — operator intake closure marker
- [sites/site-001/site-passport.md](sites/site-001/site-passport.md) — status **READY FOR RUN 5**
- [project-site-registry.md](project-site-registry.md) — SITE-001 **READY FOR AUDIT**
- [intake-readiness-review.md](intake-readiness-review.md) — Run 5 allowed **YES**

**No audit execution.** No FTP, SSH, phpMyAdmin, admin, or live site access. No commits.

---

## Run 4 deliverables (summary)

- [project-site-registry.md](project-site-registry.md) — SITE-001 registered (Run 4 container; intake completed Run 4.99)
- [sites/site-001/](sites/site-001/) — full template structure + [site-passport.md](sites/site-001/site-passport.md) + [project-access-brief.md](sites/site-001/project-access-brief.md) (stub; **required before Run 5**)
- [templates/project-access-brief-template.md](templates/project-access-brief-template.md) — standard access brief for project sites
- External bulk root: `C:\MARS Phenix\AI MARS STORAGE\ocpilot\project-sites\site-001\` (materials, audits, snapshots, backups, reports, temp; `secrets/` for credentials outside git)
- [site-passport-standard.md](site-passport-standard.md) — mandatory passport fields
- [baseline-match-workflow.md](baseline-match-workflow.md) — 3038-rs2 vs 3039-rs1 selection workflow
- [intake-readiness-review.md](intake-readiness-review.md) — Run 5 gate; SITE-001 **NO** at end of Run 4

**No real dealership onboarded.** No FTP, phpMyAdmin, admin, audit, or site modifications. No commits.

---

## Run 3.6 deliverables (summary)

- [storage-audit-run-3.6.md](storage-audit-run-3.6.md) — measured file counts, size, growth scenarios (2 / 10 / 25 / 50 baselines)
- [storage-strategy-options.md](storage-strategy-options.md) — Options A–D evaluation
- [recommended-storage-model.md](recommended-storage-model.md) — **Option D** selected: external baseline storage + metadata in git; local promoted cache for active READY baselines
- [git-storage-policy.md](git-storage-policy.md) — allow/deny list; bulk excluded from git
- [knowledge/knowledge-storage-principles.md](knowledge/knowledge-storage-principles.md) — reference knowledge vs archived internet

**Run 3.5 promoted trees unchanged.** No `.gitignore` edits. No commits.

---

## Run 3.5 deliverables (summary)

- [baseline-promotion-strategy.md](baseline-promotion-strategy.md) — Acquisition ZIP → Verified Archive → Promoted Baseline → Site Comparison
- [baseline-sanitization-review.md](baseline-sanitization-review.md) — pre-promotion allowed/forbidden review for both baselines
- Promoted `files/` trees: `baselines/ocstore-3038-rs2/files/` (4055 files), `baselines/ocstore-3039-rs1/files/` (3553 files)
- [database/database-metadata-v1.md](baselines/ocstore-3038-rs2/database/database-metadata-v1.md) per baseline — metadata only
- [comparison-notes/3038-vs-3039-structured-review-v1.md](comparison-notes/3038-vs-3039-structured-review-v1.md) — evidence-based path-set diff
- [run-3.5-readiness-recheck.md](run-3.5-readiness-recheck.md) — both priority baselines **READY**
- [knowledge/](knowledge/README.md) — skeleton knowledge layer (no content collection)

**Canonical ZIP unchanged** in `incoming/baselines/`. No commits. No production sites.

---

## Run 3 deliverables (summary)

- Verified archives: `opencart-3.0.3.8-rs.zip`, `opencart-3.0.3.9-rs.zip`
- Manifests and passports for `ocstore-3038-rs2`, `ocstore-3039-rs1`
- [comparison-notes/run-3-initial-comparison-v1.md](comparison-notes/run-3-initial-comparison-v1.md)

---

## Run 2.7 deliverables (summary)

- [baselines/storage-policy.md](baselines/storage-policy.md) — canonical ZIP, temporary extract, permanent metadata; repo growth control
- [archive-intake-rules.md](archive-intake-rules.md) — Archive Root, Package Root, OpenCart Root; detection rules; real examples `upload-3038-rs2`, `upload-3039-rs1`
- [baseline-acquisition-precheck.md](baseline-acquisition-precheck.md) — stop/go checklist before intake
- [run-3-preparation.md](run-3-preparation.md) — Run 3 operator actions and OCPilot task list
- [incoming/baselines/README.md](incoming/baselines/README.md) — expected ZIPs, operator dropzone rules

**No archive import, extraction, or baseline population in Run 2.7.**

---

## Run 2.6 deliverables (summary)

- Priority baseline folders: `baselines/ocstore-3038-rs2/`, `baselines/ocstore-3039-rs1/` (subfolder contract + README; placeholders only — **no** files imported)
- [baselines/README.md](baselines/README.md) — priority target table and Run 2.6 status
- [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) — priority acquisition targets
- [baseline-readiness-checklist.md](baseline-readiness-checklist.md) — priority baseline paths

---

## Run 2.5 deliverables (summary)



- [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) — sources, trust levels, acquisition order, rejection criteria

- [incoming/README.md](incoming/README.md) — quarantine / intake zone architecture

- [incoming/baselines/README.md](incoming/baselines/README.md) — baseline candidate dropzone

- [incoming/project-sites/README.md](incoming/project-sites/README.md) — project site material dropzone

- [intake-workflow.md](intake-workflow.md) — baseline and project site intake steps (human approval gate)

- [templates/intake-report-template.md](templates/intake-report-template.md) — standard intake report for both package types

- [quarantine-policy.md](quarantine-policy.md) — quarantine rules, stop conditions, SAFE UNKNOWN triggers



**Core safety principle (Run 2.5):**

```
Incoming Material  ≠  Trusted Baseline
Incoming Material  ≠  Project Site
Incoming Material  must pass intake
```



---



## Run 2 deliverables (summary)



- [baseline-storage-model.md](baseline-storage-model.md) — allowed/forbidden content, storage philosophy

- [templates/versioned-baseline-passport-template.md](templates/versioned-baseline-passport-template.md) — standard baseline passport

- [baseline-comparison-methodology.md](baseline-comparison-methodology.md) — five-layer comparison model

- [baseline-readiness-checklist.md](baseline-readiness-checklist.md) — required vs optional readiness gate

- Extended baseline subfolders: `manifest/`, `passports/`, `comparison-notes/` in all versioned baselines

- [project-sites-workflow.md](project-sites-workflow.md) — Baseline Selection section



---



## Run 1.5 deliverables (summary)



- Versioned baseline folders: `baselines/opencart-230/`, `opencart-3037/`, `opencart-4x/`, `ocstore-230/`, `ocstore-3037/`

- Legacy `baselines/clean-opencart/` marked as generic placeholder

- Expanded `sites/_template-site/` OpenCart analysis zones

- Shared layer: [shared/external-access-patterns/](../../shared/external-access-patterns/README.md)

- Family note: [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md)



---



## Quick orientation



1. [boundaries.md](boundaries.md) — что запрещено  

2. [access-and-safety.md](access-and-safety.md) — доступ и бэкапы  

3. [architecture.md](architecture.md) — standalone + siblings + family  

4. [baseline-storage-model.md](baseline-storage-model.md) — модель хранения baseline  

5. [baseline-acquisition-strategy.md](baseline-acquisition-strategy.md) — как baseline packages входят в систему  

6. [baselines/storage-policy.md](baselines/storage-policy.md) — ZIP vs extract vs metadata  
6b. [external-storage-registry.md](external-storage-registry.md) — external bulk root `C:\MARS Phenix\AI MARS STORAGE`

7. [archive-intake-rules.md](archive-intake-rules.md) — Archive / Package / OpenCart Root  

8. [incoming/README.md](incoming/README.md) — quarantine / intake zone  

9. [intake-workflow.md](intake-workflow.md) — workflow intake  

10. [quarantine-policy.md](quarantine-policy.md) — правила карантина  

11. [baseline-comparison-methodology.md](baseline-comparison-methodology.md) — методология сравнения  

12. [shared/external-access-patterns/](../../shared/external-access-patterns/README.md) — shared access patterns  
12b. [shared/external-access-runtime/](../../shared/external-access-runtime/README.md) — EAR snapshot acquisition layer (documentation v1)  

13. Templates в [templates/](templates/) — including [project-access-brief-template.md](templates/project-access-brief-template.md) (Run 5 prerequisite for project sites)  

14. MARS Core: HITL, REPORT, SAFE UNKNOWN — [AGENTS.md](../../AGENTS.md); не дублировать governance waterfall здесь  



---



## Cross-references (patterns only)



| Source | OCPilot use |

|--------|-------------|

| shared/external-access-patterns | Browser, FTP, PMA gates — **not** WPilot-owned |
| shared/external-access-runtime | **EAR** — supervised snapshot acquisition (docs v1); Run 5 dependency |

| WPilot (`projects/wpilot/`) | Bridge/safety/read-only/rollback **patterns** — WordPress logic **не** переносить слепо |

| ORCA (`projects/orca/`) | Battle pilot, freeze, FAST PATH discipline |

| mars-survivability | Backup, risk classes, rollback discipline |

| MARS governance | External system boundaries — см. [external-system-boundaries.md](../../governance/external-system-boundaries.md) |



---



## Reports



Каждый operational run заканчивается отчётом: `# REPORT — <run name>` (см. AGENTS.md). Шаблоны — [templates/](templates/).


