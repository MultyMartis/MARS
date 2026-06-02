# OCPilot — Operational Index



**Lane:** B — External Systems (OpenCart).  

**Status:** documented navigation only; **not** automated router.  

**Domain root:** [README.md](README.md)  

**Family:** [cms-ecommerce-pilots-family.md](cms-ecommerce-pilots-family.md)



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

| 3.7 | **External Storage Architecture** | **DONE** | [external-storage-registry.md](external-storage-registry.md), [baseline-storage-migration-plan.md](baseline-storage-migration-plan.md), [mars-storage-family-note.md](mars-storage-family-note.md) — root `C:\AI MARS STORAGE` |

| 4 | **First Project Site Intake** | **DONE** | [project-site-registry.md](project-site-registry.md), [sites/site-001/](sites/site-001/site-passport.md), [site-passport-standard.md](site-passport-standard.md), [baseline-match-workflow.md](baseline-match-workflow.md), [intake-readiness-review.md](intake-readiness-review.md) |

| 4.99 | **SITE-001 Audit Charter** | **DONE** | [sites/site-001/AUDIT-CHARTER.md](sites/site-001/AUDIT-CHARTER.md), [sites/site-001/materials/INTAKE-COMPLETE.md](sites/site-001/materials/INTAKE-COMPLETE.md), [intake-readiness-review.md](intake-readiness-review.md) |

| 5 | **First Read-Only Site Audit** | **paused** (init done) | [sites/site-001/reports/RUN-5-FIRST-FINDINGS.md](sites/site-001/reports/RUN-5-FIRST-FINDINGS.md), [freeze/site-001-pre-runtime-bridge/](freeze/site-001-pre-runtime-bridge/README.md), [shared/external-access-runtime/](../../shared/external-access-runtime/README.md) |

| 6 | **Catalog / Theme / Controller Planning** | planned | SAFE UNKNOWN — spec TBD after baseline + audit |

| 7 | **First Change Plan** | planned | SAFE UNKNOWN — spec TBD; rollback required per [boundaries.md](boundaries.md) |

| 8 | **First Battle Pilot** | planned | [battle-pilot-workflow.md](battle-pilot-workflow.md), [freeze/README.md](freeze/README.md) |



**Rule:** Runs **1** through **4.99** marked DONE. Run **5** initialization **done**; execution **paused** pending **External Access Runtime (EAR)** direction — not downgrading readiness.

**First project site:** SITE-001 (`sites/site-001/`) — **READY FOR AUDIT** (unchanged); intake closed Run 4.99. **[AUDIT-CHARTER.md](sites/site-001/AUDIT-CHARTER.md)** authorizes read-only Run 5. Run 5 allowed **YES** per [intake-readiness-review.md](intake-readiness-review.md). Run 5 **not executing** until artifact acquisition path defined ([freeze/site-001-pre-runtime-bridge/](freeze/site-001-pre-runtime-bridge/README.md)).

### Operational lesson (Run 5 initialization)

| Topic | Finding |
|-------|---------|
| Bottleneck | **Artifact acquisition**, not audit logic or baseline readiness |
| Prior flow | Operator → WinSCP / manual exports → files → OCPilot |
| Target flow | SITE → [EAR](../../shared/external-access-runtime/README.md) → Snapshot Package → OCPilot |
| Future dependency | **EAR v1** — document-first under `shared/external-access-runtime/`; **no runtime claimed** |
| Freeze | [freeze/site-001-pre-runtime-bridge/](freeze/site-001-pre-runtime-bridge/README.md) |

**Knowledge layer:** [knowledge/](knowledge/README.md) — skeleton + [knowledge-storage-principles.md](knowledge/knowledge-storage-principles.md) (Run 3.6).

**Storage policy (canonical):** [recommended-storage-model.md](recommended-storage-model.md) — Option D; approved external root `C:\AI MARS STORAGE` ([external-storage-registry.md](external-storage-registry.md)); local promoted cache gitignored; grandfathered Run 3.5 trees unchanged.

**Priority first baselines:** `baselines/ocstore-3038-rs2/` and `baselines/ocstore-3039-rs1/` — **READY** for file-level comparison after Run 3.5 promotion ([run-3.5-readiness-recheck.md](run-3.5-readiness-recheck.md)). Canonical ZIPs remain in repo `incoming/baselines/` until migration ([baseline-storage-migration-plan.md](baseline-storage-migration-plan.md)).



---



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
- External bulk root: `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\` (materials, audits, snapshots, backups, reports, temp; `secrets/` for credentials outside git)
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
6b. [external-storage-registry.md](external-storage-registry.md) — external bulk root `C:\AI MARS STORAGE`  

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


