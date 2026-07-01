# FP-0002 V8 Phase 07B — Documentation Drift Reconciliation

**Date:** 2026-07-01

---

## Stale items discovered

| ID | Stale claim | Location | Current truth | Disposition |
|----|-------------|----------|---------------|-------------|
| D-01 | V7 `ACTIVE_DEVELOPMENT` | PROJECT-STATUS workspace table | V8 active | **update now** |
| D-02 | O-Centre `REJECTED` / `BLOCKED` | FP-0002-V8-OPERATIONAL-STATUS | Baseline STABLE_PREVIOUSLY_APPROVED | **annotate superseded** in operational status |
| D-03 | V6 described as current pilot in WF index | OPERATIONAL-INDEX FP-0002 bullets | V8 baseline | **update now** — add V8 pointer |
| D-04 | Blog article unfinished | None in baseline — historical reports only | OPERATOR_APPROVED | **preserve historical** |
| D-05 | Page count 11 design vs 10 implemented | Page inventory vs V8 | Both valid — different scopes | **leave with justification** |
| D-06 | `C:\`, `D:\`, `E:\` paths | Old reports | X: canonical only | **preserve historical** in old reports |
| D-07 | Missing static demo phase | Pre-07B docs | 07C spec created | **update now** |
| D-08 | Missing operator polish phase | Pre-07B | Documented in 07B | **update now** |
| D-09 | `mars/post-cycle8-live-tests` in old inventories | PAGE-INVENTORY header | `mars/canonical-post-recovery` | **preserve historical** |
| D-10 | PDF as sole visual SoT in page inventory | PAGE-INVENTORY v1 | Figma `Spig_v1.2.fig` active for V8 | **annotate superseded** for V8 work |

---

## Updates applied (07B)

| File | Change |
|------|--------|
| PROJECT-STATUS.md | Phase 07B complete pointer; V8 workspace authority |
| README.md (V8) | Link to documentation pack |
| FP-0002-V8-OPERATIONAL-STATUS.md | Phase + doc links; supersede note on O-Centre conflict |
| OPERATIONAL-INDEX.md | V8 baseline + lessons learned link |
| execution-cases-registry-v1.md | V8 doc pack pointer |

---

## Preserved as historical (not rewritten)

- Phase reports under `REPORTS/`  
- V6/V7 milestone manifests  
- O-Centre forensic reports — add cross-link to baseline authority  
- PAGE-INVENTORY v1 intake headers  

---

## Justified unchanged

| Item | Reason |
|------|--------|
| PAGE-INVENTORY 11 design pages | Design-scope document — still valid for PDF pack |
| Forge WP foundation docs | Local install scope unchanged by 07B |

---

*Drift reconciliation — Phase 07B.*
