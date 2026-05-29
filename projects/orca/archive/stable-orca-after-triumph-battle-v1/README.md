# Stable ORCA Backup — After Triumph Battle v1

**Label:** `orca-stable-backup-after-triumph-battle-v1`  
**Date:** 2026-05-30  
**Source battle freeze:** [freeze/battle-pilot-triumph-search-v1/](../freeze/battle-pilot-triumph-search-v1/)

---

## Purpose

Point-in-time snapshot of ORCA system state after first real Triumph Manipulator Search PPC Commander import battle. Documentation and source maps only — **not** a runnable deployment.

---

## Contents

| Path in backup | Source |
|----------------|--------|
| `OPERATIONAL-INDEX.md` | `projects/orca/OPERATIONAL-INDEX.md` |
| `freeze/` | `projects/orca/freeze/` |
| `coordination/` | `projects/orca/coordination/` |
| `calibration/` | `projects/orca/calibration/` |
| `visual-semantics/` | `projects/orca/visual-semantics/` |
| `content-packs/examples/triumph-*-pack-v1/` | Semantic route packs |
| `ppc/triumph-manipulator/` | Triumph PPC pack (docs, schema, tools source, template) |

---

## Excluded (by design)

- `node_modules/` — run `npm install` in exporter-cli / validation-cli  
- `tools/exporter-cli/output/*.xlsx` — regenerate per [STABLE-BACKUP-MANIFEST-v1.md](../freeze/battle-pilot-triumph-search-v1/STABLE-BACKUP-MANIFEST-v1.md)  
- `dist/`, `.env`, secrets, logs  

---

## Restore

See [STABLE-BACKUP-MANIFEST-v1.md](../freeze/battle-pilot-triumph-search-v1/STABLE-BACKUP-MANIFEST-v1.md).

---

## Boundaries

Human-operated documentation backup. **Not** runtime. **Not** orchestration.
