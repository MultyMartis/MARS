# Export Runbook v1 — ORCA DOCX Pilot

## Prerequisites

- Node.js **18+**
- npm
- Microsoft Word or compatible DOCX viewer (for verification)
- Human operator with pack read access

## Install

```bash
cd projects/orca/content-packs/exporters/docx-pilot
npm install
```

Installs `docx` (npm) only. No global CLI registration.

## Export command

**Pilot default (Triumph 5 tonn):**

```bash
npm run export:pilot
```

**Custom paths:**

```bash
node scripts/export-content-pack-docx.js \
  ../../examples/triumph-manipulyator-5-tonn-pack-v0.md \
  output/triumph-manipulyator-5-tonn-pack-v1.docx
```

Optional environment:

```bash
set ORCA_EXPORTED_BY=operator-name
npm run export:pilot
```

## Output path

| Artifact | Path |
|----------|------|
| Pilot DOCX | `output/triumph-manipulyator-5-tonn-pack-v1.docx` |

## Expected console

```
--- ORCA DOCX Export Pilot v1 ---
Input:  .../triumph-manipulyator-5-tonn-pack-v0.md
Output: .../output/triumph-manipulyator-5-tonn-pack-v1.docx
[OK] DOCX written (N bytes)
Sections exported: 10
```

## Verification checklist

Run [validation/export-checklist-v1.md](validation/export-checklist-v1.md) after every export.

Minimum:

1. DOCX opens in Word without repair prompt
2. Cover shows project_id, route_id, export_version, generated_at
3. All 10 content sections present
4. SAFE UNKNOWN section visible (amber/warning styling)
5. Approval gates match pack frontmatter snapshot
6. No mojibake in Russian copy
7. No invented prices, fleet claims, or stats beyond pack source

## Manual review requirements

| Reviewer action | Required |
|-----------------|----------|
| Compare DOCX to source `.md` for hero H1 and spec table | yes |
| Confirm SAFE UNKNOWN not resolved in DOCX | yes |
| Confirm `approved_for_factory` snapshot matches project approvals | yes |
| Sign approval footer if promoting to client export | human only |
| Do **not** treat DOCX generation as ads/launch approval | always |

## Failure handling

| Symptom | Action |
|---------|--------|
| `Input pack not found` | Check relative path from `docx-pilot/` |
| `Expected 10 sections` warning | Inspect pack `# 01`…`# 10` headers; fix MD, re-export |
| Word encoding issues | Re-export; verify source MD UTF-8 |
| Missing npm module | Re-run `npm install` in `docx-pilot/` |

## Boundary reminder

Human-triggered only. No scheduled export. No automatic gate changes.
