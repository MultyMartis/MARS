# Sample OOXML Analysis — Operator Runbook

**Phase:** ORCA OOXML Workbook Forensics v0  
**NOT:** Direct API · auto-import · runtime · exporter auto-fix

---

## Prerequisites

- Node.js ≥ 18  
- Generated draft exists: run `export.js --template-fill` first  
- Windows: uses PowerShell `System.IO.Compression.ZipFile` (same as manual Expand-Archive)

---

## Command example

```bash
cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli
npm install

node export.js \
  ../../schema/instances/triumph-s-tier-draft-v1.json \
  fixtures/validation-report.export-allowed.fixture.json \
  --template-fill

node ooxml-forensics.js
```

Custom paths:

```bash
node ooxml-forensics.js \
  ../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx \
  output/triumph-commander-template-fill-draft.xlsx
```

npm script (if added): `npm run forensics:ooxml`

---

## Expected outputs

| Artifact | Purpose |
|----------|---------|
| [xlsx-structure-index-v0.json](xlsx-structure-index-v0.json) | ZIP + worksheet index — **template** |
| [generated-xlsx-structure-index-v0.json](generated-xlsx-structure-index-v0.json) | ZIP + worksheet index — **generated** |
| [ooxml-comparison-v0.json](ooxml-comparison-v0.json) | Machine comparison (deltas, worksheet table) |
| Console summary | Top byte deltas + worksheet cell counts |

### Expected console highlights (2026-05-20 baseline)

- `Only in generated: xl/sharedStrings.xml`
- sheet2 cells: `102170 → 17344`
- sheet1 cells: `9402 → 5665`
- `XML parse: … ok` (both packages)

---

## How to inspect findings

1. **Quick human read:** [ooxml-diff-report-v0.md](ooxml-diff-report-v0.md)  
2. **Decision framing:** [ooxml-risk-analysis-v0.md](ooxml-risk-analysis-v0.md)  
3. **Numbers:** `ooxml-comparison-v0.json` → `worksheetComparison`  
4. **Per-file XML head:** structure indexes → `worksheets[].xmlHead`  
5. **Excel confirmation:** open generated XLSX in Excel — note recovery dialog paths (`sheet1.xml` …)

### Manual ZIP inspect (optional)

```powershell
Add-Type -AssemblyName System.IO.Compression.FileSystem
$z = [IO.Compression.ZipFile]::OpenRead("output\triumph-commander-template-fill-draft.xlsx")
$z.Entries | Select-Object FullName, Length | Format-Table
$z.Dispose()
```

---

## Likely next operator actions

| Step | Action |
|------|--------|
| 1 | Record exact Excel recovery dialog text (screenshot / copy) |
| 2 | If Excel offers repair — **do not** use repaired file for Commander import without diff vs template |
| 3 | Treat `xlsx-integrity-check.js` PASS as **necessary not sufficient** |
| 4 | Escalate to engineering charter: **template-preservation** or **ZIP surgical edit** (see risk analysis) |
| 5 | Keep using template-fill only for **analysis** until new transport strategy approved |

---

## Fail / block examples

| Condition | Behavior |
|-----------|----------|
| Template missing | Exit 1 — path error |
| Generated missing | Exit 1 — run export first |
| PowerShell unavailable | ZIP listing fails — **SAFE UNKNOWN** on non-Windows |

---

## Related

- [xlsx-integrity-notes-v0.md](xlsx-integrity-notes-v0.md)  
- [sample-integrity-run.md](sample-integrity-run.md)  
- [template-fill-notes-v0.md](template-fill-notes-v0.md)
