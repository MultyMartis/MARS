# Stable Backup Manifest v1

**Operation:** ORCA Battle Pilot — stable backup after Triumph Search Commander import  
**Date:** 2026-05-30  
**Label:** `orca-stable-backup-after-triumph-battle-v1`

---

## Backup locations

| Backup | Path | Scope |
|--------|------|-------|
| **ORCA system** | `projects/orca/archive/stable-orca-after-triumph-battle-v1/` | ORCA docs, freezes, coordination, calibration, semantic packs, PPC tools |
| **Triumph Search PPC** | `projects/orca/ppc/triumph-manipulator/archive/stable-search-rk-after-commander-import-v1/` | JSON instance, exporter, template, battle references |

---

## ORCA system backup — included

| Category | Source path | Notes |
|----------|-------------|-------|
| Operational index | `projects/orca/OPERATIONAL-INDEX.md` | Entry map |
| Freeze (all) | `projects/orca/freeze/` | All freeze milestones including battle pilot |
| Coordination | `projects/orca/coordination/` | Route batch, priority matrices |
| Calibration | `projects/orca/calibration/` | Triumph calibration case |
| Visual semantics | `projects/orca/visual-semantics/` | Hero/density/trust schemas |
| Content packs | `projects/orca/content-packs/examples/triumph-*-pack-v1/` | 12 route semantic packs |
| Triumph PPC docs | `projects/orca/ppc/triumph-manipulator/` (docs only) | Doctrine, schema, export, validation |
| Exporter CLI source | `.../tools/exporter-cli/` | JS source, configs, fixtures — **no node_modules** |
| Validation CLI source | `.../tools/validation-cli/` | JS source, fixtures — **no node_modules** |
| Commander template | `.../assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` | Transport SoT |

---

## ORCA system backup — excluded

| Category | Reason |
|----------|--------|
| `node_modules/` | Regenerate via `npm install` |
| `tools/exporter-cli/output/*.xlsx` | Generated — reproduce via export commands |
| `dist/` | Build artifact |
| `.env` / secrets | Security |
| Unrelated governance/workspaces/logs | Out of scope per charter |

---

## Triumph Search PPC backup — included

| File / path | Role |
|-------------|------|
| `schema/instances/triumph-s-tier-draft-v1.json` | JSON SoT |
| `tools/_build-full-cycle-draft.js` | Draft builder |
| `tools/exporter-cli/` (source) | Exporter v1.4 |
| `tools/validation-cli/` (source) | Validation engine |
| `assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx` | Template SoT |
| `freeze-references/` | Pointers to battle freeze docs |
| `OPERATIONAL-INDEX.md` | Project entry map |
| Key docs: doctrine, export, schema, validation | Battle-stable references |

---

## Triumph Search PPC backup — excluded

| Category | Reason |
|----------|--------|
| `node_modules/` | Regenerate |
| `output/*.xlsx` | Generated artifact |
| Temp files / logs | Not stable state |

---

## Generated XLSX reproduction

Battle import file is **not** stored in git (gitignored). Reproduce:

```bash
cd projects/orca/ppc/triumph-manipulator/tools/validation-cli
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json

cd ../exporter-cli
npm install
npm run export:sheet1-patch:launch-ready-v1.4
npm run validate:launch-ready-v1.4
```

**Output:** `output/triumph-sheet1-patch-launch-ready-v1.4.xlsx`

**Verify:** 84 rows · 12 groups · 20 ads · 64 keywords · 0 duplicate ads

---

## Key commits (restore reference)

| Commit | Label |
|--------|-------|
| `7666829` | ORCA route family freeze v1 |
| `f235bf1` | ORCA commander export URL synchronization v1 |
| `2f01941` | ORCA PPC exporter production baseline v1 |
| _(this commit)_ | ORCA battle pilot Triumph search stable v1 |

---

## Restore procedure

1. Check out commit with battle pilot freeze  
2. Or copy from `archive/stable-orca-after-triumph-battle-v1/` to working tree  
3. Run `npm install` in exporter-cli and validation-cli  
4. Regenerate XLSX per reproduction commands above  
5. Follow [CAMPAIGN-SETTINGS-LAYER-v1.md](CAMPAIGN-SETTINGS-LAYER-v1.md) post-import  

---

## Integrity notes

- Backup is **documentation + source snapshot** — not a running system  
- Template XLSX is binary — included in Triumph backup  
- JSON instance SHA should match git at freeze commit  
- No runtime, orchestration, or autonomous recovery claimed
