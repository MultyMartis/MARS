# ORCA Triumph — Full Cycle v1.1

Expansion pass: **10 → 12** intent groups (regional + hot master), same v0.6 transport.

| Artifact | Path |
|----------|------|
| Campaign JSON | `schema/instances/triumph-s-tier-draft-v1.json` |
| Validation report | `tools/validation-cli/output/validation-report.output.json` |
| Commander XLSX (local only, gitignored) | `tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.1.xlsx` |
| Prior baseline | [../full-cycle-v1/README.md](../full-cycle-v1/README.md) |

## Reproduce

```bash
cd projects/orca/ppc/triumph-manipulator/tools/validation-cli
npm install
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json

cd ../exporter-cli
npm install
npm run export:sheet1-patch:full-cycle-v1.1
node _validate-full-cycle-v1.1.js
```

## Docs in this folder

- [full-cycle-summary-v1.1.md](full-cycle-summary-v1.1.md)
- [campaign-structure-v1.1.md](campaign-structure-v1.1.md)
- [validation-summary-v1.1.md](validation-summary-v1.1.md)
- [export-summary-v1.1.md](export-summary-v1.1.md)
- [commander-import-checklist-v1.1.md](commander-import-checklist-v1.1.md)

**Not** runtime · **not** Direct API · **not** auto-launch.
