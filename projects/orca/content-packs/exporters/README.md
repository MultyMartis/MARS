# ORCA Content Pack Exporters — README

## Status

**v0 — architecture only.** No exporter CLI in this folder.

## Purpose

Document how **approved landing content packs** will be transformed into:

| Format | Role |
|--------|------|
| **DOCX** | Primary human-approved export |
| **Markdown** | Operational / Git-friendly export |
| **PDF** | Future client-ready layer |

## Not this folder

| System | Location |
|--------|----------|
| Commander XLSX exporter | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/` |
| Validation CLI | `projects/orca/ppc/triumph-manipulator/tools/validation-cli/` |

## Documents

- [docx-export-architecture-v0.md](docx-export-architecture-v0.md)
- [markdown-export-architecture-v0.md](markdown-export-architecture-v0.md)
- [pdf-export-architecture-v0.md](pdf-export-architecture-v0.md)
- [export-modes-v0.md](export-modes-v0.md)

## Execution model (future)

1. Human operator confirms pack `approved` or higher  
2. Human triggers export (script or manual template fill)  
3. Tool writes file + [export metadata](../schemas/export-metadata-schema-v0.md) sidecar  
4. Human reviews output before `approved_for_client_export`  

**No** scheduled jobs. **No** autonomous post-approval export.

## Boundary

Documentation for export design — not implemented tooling in v0.
