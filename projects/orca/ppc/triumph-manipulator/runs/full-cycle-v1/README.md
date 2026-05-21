# ORCA Triumph — Full Cycle v1

Human-operated end-to-end pass: campaign draft → validation → Commander sheet1 patch export.

| Artifact | Path |
|----------|------|
| Campaign JSON | `schema/instances/triumph-s-tier-draft-v1.json` |
| Validation report | `tools/validation-cli/output/validation-report.output.json` |
| Commander XLSX (local only, gitignored) | `tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.xlsx` |
| Git checkpoint (MVP tools) | commit `fd6b0ba` — *ORCA Triumph Commander export MVP* |

## Reproduce

```bash
cd projects/orca/ppc/triumph-manipulator/tools
node _build-full-cycle-draft.js

cd ../validation-cli
npm install
node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json

cd ../exporter-cli
npm install
npm run export:sheet1-patch:full-cycle-v1
node _validate-full-cycle-v1.js
```

## Docs in this folder

- [full-cycle-summary-v1.md](full-cycle-summary-v1.md)
- [campaign-structure-v1.md](campaign-structure-v1.md)
- [validation-summary-v1.md](validation-summary-v1.md)
- [export-summary-v1.md](export-summary-v1.md)
- [commander-import-checklist-v1.md](commander-import-checklist-v1.md)

**Not** runtime · **not** Direct API · **not** auto-launch.
