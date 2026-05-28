# Export readiness — DOCX (structure only)

**No exporter run in this task.**

## Pilot status

- DOCX pilot exists: `projects/orca/content-packs/exporters/docx-pilot/`
- Sample output: `triumph-manipulyator-5-tonn-pack-v1.docx` (5-ton only)
- Master hot export: **deferred** until operator approves this pack

## Readiness checklist

| Item | Status |
|------|--------|
| Pack folder structure | **ready** |
| `PACK-METADATA.md` envelope | **ready** |
| Section files for renderer | **ready** (markdown per section) |
| `APPROVALS.md` | **ready** (unsigned) |
| `SAFE-UNKNOWN.md` | **ready** |
| Visual semantics YAML block | **ready** in metadata |
| `approved_for_client_export` | **false** |

## Proposed export profile

```yaml
export_profile: master-hot-v1
source_root: triumph-manipulyator-zakaz-pack-v1/
render_order:
  - PACK-METADATA.md
  - content/*.md (section order)
  - ppc/*.md
  - visual-semantics/hero-visual-semantics.md
  - factory/factory-rules.md
  - factory/allowed-drift.md
  - factory/forbidden-drift.md
  - calibration/calibration-summary.md
  - APPROVALS.md
  - SAFE-UNKNOWN.md
```

## Blockers before export

1. Operator sign-off on gates
2. Extend `pack-parser.js` / render scripts for folder pack (today: single MD file for 5-ton)
3. Resolve D2 for client-facing PPC summary

## Boundary

Export pipeline documents architecture only — **not** automated approval.
