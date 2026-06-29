# MARS X-Drive Deferred Path Register v1

**Status:** **ACTIVE** — intentionally unresolved old-path families after X9 closure.  
**Authority:** [mars-x-drive-migration-closure-v1.md](mars-x-drive-migration-closure-v1.md)  
**Is not:** per-file inventory, automated enforcement list, or deletion queue.

---

## Purpose

Record every **family** of remaining old-path references that X9 **preserved** by design. Each entry has exactly one classification. Future reconciliation requires a **programme-specific charter** — not blind mass replacement.

---

## Register

| ID | System | Path/family | Classification | Reason preserved | Future action |
| -- | ------ | ----------- | -------------- | ---------------- | ------------- |
| DEF-001 | OCPilot | `projects/ocpilot/**/*-work/*.py` | **B** — active script drift (deferred) | One-time execution captures and generated work files mixed with reusable tools; not batch-edited | Per-script charter: classify reusable vs capture; reconcile only clean static tools |
| DEF-002 | OCPilot | `projects/ocpilot/sites/site-002/backups/*.bak`, deploy/rollback captures | **J** — generated artefact | Pre-migration backup and deployment evidence | Preserve; promote only if operator re-scopes site work |
| DEF-003 | OCPilot | `projects/ocpilot/sites/**/reports/*RESTORE*`, `*STABLE-PDP*` | **H** — historical release/freeze | Frozen site restore points with embedded C/E paths | Preserve as site history |
| DEF-004 | Corvonero | `.tools/corvonero-*` (untracked) | **D** — foreign WIP | Operator checkpoint/commander tooling created outside X9 scope | Operator commits or scopes in dedicated charter |
| DEF-005 | Corvonero | `projects/mars-search-ppc-production/pilots/corvonero/CORVONERO-COMMANDER-*` (untracked) | **D** — foreign WIP | Commander import/validation wave artefacts | Preserve until Corvonero programme charter |
| DEF-006 | Corvonero | `workspaces/corvonero-yandex-direct/**` (if present, dirty) | **D** — foreign WIP | Commander/checkpoint operator work | Preserve; do not batch-edit |
| DEF-007 | ATLAS | `projects/atlas/**` (modified/untracked WIP) | **D** — foreign WIP | Population registers, legal-entity sync — operator in progress | Operator commit scope; citation paths may retain historical refs until scoped |
| DEF-008 | FP-0002 | `workspaces/fp-0002-shpigovsky-v7/**`, `v8/**` (modified) | **D** — foreign WIP | Frontend implementation and audit JSON — active delivery | Do not modify frontend source in migration closure |
| DEF-009 | FP-0002 | `workspaces/fp-0002-shpigovsky-v8/tools/**` (untracked) | **K** — forensic evidence | Visual discrepancy and operator-manual polish tooling | Programme charter if paths become active config |
| DEF-010 | FP-0002 | `workspaces/fp-0002-shpigovsky-v8/audits/**/data/*.json` | **K** — forensic evidence | Consolidation and QA checkpoints with session paths | Preserve |
| DEF-011 | MIG | `projects/mig/**/evidence/**`, live-validation receipts | **G** — historical report/receipt | Run captures with historical roots | Preserve; separate active-config charter if needed |
| DEF-012 | ORCA | `projects/orca/**/receipts/**`, semantic cache paths | **J** — generated artefact | Semantic run receipts and caches | Preserve; regenerate only under ORCA charter |
| DEF-013 | EAR | `projects/ear-runtime/R1.8*.md`, `R2.5-EVIDENCE-QUARANTINE-LAYOUT-v1.md` | **L** — immutable hashed/signed baseline | Frozen charter tables with C-path persistence layout | Preserve; supersede only via new EAR charter wave |
| DEF-014 | Website Factory / Forge | `projects/mars-website-factory/subsystems/forge-wordpress/FW-07C*.md` | **H** — historical release/freeze | Safety enforcement preflight with Phoenix reconstruction paths | Preserve |
| DEF-015 | Website Factory / Forge | `projects/mars-website-factory/subsystems/forge-wordpress/enforcement/README.md` denylist | **O** — test fixture/denylist | Intentionally lists deprecated roots for denial testing | Preserve |
| DEF-016 | MLI | `projects/mars-localhost-infrastructure/reports/MLI-03R*.md`, `MLI-01*.md` | **E** — historical incident evidence | D:/E: runtime incident narrative | Preserve |
| DEF-017 | Phoenix / DR | `governance/mars-disaster-recovery-2026-06-24-closure-v1.md`, `mars-phoenix-recovery-cutover-receipt-v1.md`, `mars-legacy-tree-retention-decision-v1.md` | **E/F** — historical incident/recovery evidence | Immutable closure and cutover records | Preserve |
| DEF-018 | Survivability / boundary | `AGENTS.md`, `.cursorrules`, `mars-x-drive-root-authority-v1.md` §6, `protected-zones-registry-v1.md`, `validator-rules-registry-v1.json` | **M** — deprecated root table | Active denylist of C/D/E roots — **not** drift | Preserve |
| DEF-019 | Web-GPT legacy | `web-gpt-sources/mars-v2*/**`, `web-gpt-sources/chat-migration/**`, `01_system.md` … `14_roadmap.md` | **P** — legacy source pack | Pre-X imported packs — historical bootstrap | Preserve; use `mars-current-x-drive-2026-06/` for current chats |
| DEF-020 | Web-GPT current pack | `web-gpt-sources/mars-current-x-drive-2026-06/04_INFRASTRUCTURE_REALITY.md` deprecated table | **M** — deprecated root table | Lists historical roots for chat clarity | Preserve |
| DEF-021 | Wave reports | `reports/mars-x-drive-migration-x*.md` | **G** — historical report/receipt | X0–X8 audit evidence with before/after path counts | Preserve |
| DEF-022 | Recovery temp | `.recovery-temp/**`, `.restore-test-temp/**` (untracked) | **J** — generated artefact | Forensic/recovery scratch captures | Preserve; operator cleanup outside migration |
| DEF-023 | Site-local legacy | `mars-runtime/**` scripts referencing historical roots (if any) | **R** — SAFE UNKNOWN | Not exhaustively re-executed in X9 | Inspect under runtime charter if activated |
| DEF-024 | MySQL | Live MySQL datadir on operator machine | **R** — SAFE UNKNOWN | Location not verified from non-secret config in X9 | Operator follow-up from MLI config when convenient |
| DEF-025 | External chats | Web-GPT / Cursor chats outside repo | **R** — SAFE UNKNOWN | Manual pack upload required | Operator uploads current pack |
| DEF-026 | Lifecycle historical | `logs/lifecycle-log.md` rows evt-2026-0023 (SITE-002 `C:\AI MARS STORAGE`) | **G** — historical report/receipt | Append-only historical registration event | Preserve; new events use X paths |
| DEF-027 | Triumph / workspaces | `workspaces/triumph-manipulator-landing*/**` handoff docs | **G/Q** — historical/superseded | Pre-X workspace notes | Preserve unless workspace charter |
| DEF-028 | OCPilot index | `projects/ocpilot/OPERATIONAL-INDEX.md` residual historical refs in evidence links | **G** — historical report/receipt | Mixed operational + evidence pointers | Programme charter for any active script updates |
| DEF-029 | External server | Production FTP/host paths in OCPilot site reports | **N** — external server path | Remote server paths — not MARS local roots | Preserve |
| DEF-030 | Node portable | `.tools/node-portable/**`, `.tools/node-runtime/**` (untracked) | **J** — generated artefact | Operator-local runtime bundles | Preserve; out of git scope |

---

## Classification legend

| Class | Meaning |
|-------|---------|
| B | Active script/config drift (deferred) |
| D | Foreign dirty WIP |
| E–L | Historical, generated, frozen, forensic — preserve |
| M | Deprecated root table (intentional) |
| N | External server path |
| O | Test fixture / denylist |
| P | Legacy source pack |
| Q | Superseded document |
| R | SAFE UNKNOWN — document only |

---

## Rules

1. **No blind replacement** across this register.
2. **Foreign WIP** (class D) — preserve until operator commits or charters.
3. **Historical evidence** (E–L) — never rewrite for cosmetic migration closure.
4. **New work** — use `X:\AI MARS\`, `X:\AI MARS STORAGE\`, `X:\MARS-Localhost\` per [mars-x-drive-root-authority-v1.md](mars-x-drive-root-authority-v1.md).

---

*End of MARS X-Drive Deferred Path Register v1.*
