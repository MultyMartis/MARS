# Stable Triumph Search PPC Backup — After Commander Import v1

**Label:** `triumph-search-rk-stable-after-commander-import-v1`  
**Date:** 2026-05-30  
**Project:** Триумф Манипулятор — РК на поиске

---

## Purpose

Point-in-time snapshot of Triumph Search PPC project after successful v1.4 Commander import. Includes JSON SoT, exporter/validation source, Commander template, and battle freeze references.

---

## Contents

| Path | Role |
|------|------|
| `schema/instances/triumph-s-tier-draft-v1.json` | PPC JSON SoT |
| `tools/_build-full-cycle-draft.js` | Draft builder |
| `tools/exporter-cli/` | Exporter v1.4 source |
| `tools/validation-cli/` | Validation engine source |
| `assets/direct-commander-template/` | Commander template v1 SoT |
| `freeze-references/` | Battle freeze doc copies / pointers |
| `OPERATIONAL-INDEX.md` | Project entry map |
| `doctrine/`, `export/`, `schema/`, `validation/`, `exporter/` | Core docs |

---

## XLSX reproduction

Output XLSX is **not** stored (gitignored generated artifact).

```bash
cd tools/validation-cli && node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json
cd ../exporter-cli && npm install && npm run export:sheet1-patch:launch-ready-v1.4
npm run validate:launch-ready-v1.4
```

Output: `tools/exporter-cli/output/triumph-sheet1-patch-launch-ready-v1.4.xlsx`

---

## Post-import checklist

[CAMPAIGN-SETTINGS-LAYER-v1.md](freeze-references/CAMPAIGN-SETTINGS-LAYER-v1.md)

---

## Boundaries

**Not** launch approved. **Not** runtime. Human-operated backup only.
