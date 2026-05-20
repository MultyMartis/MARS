# Exporter CLI — future expansion notes v0

**Scope:** Documentation of possible next steps only. **Not implemented** in prototype v0.

---

## Commander fidelity expansion

**v0 done (analysis):** `template-reader.js` + [commander-header-map-v0.json](commander-header-map-v0.json) + [template-sheet-index-v0.json](template-sheet-index-v0.json).

**v0 done (template-fill prototype):** `template-fill-writer.js` + `--template-fill` in [export.js](export.js) — clone template, write verified columns into **Тексты** from row 16. See [template-fill-notes-v0.md](template-fill-notes-v0.md).

**v0 done (XLSX integrity hardening):** exact-cell writes, no range clears, `xlsx-integrity-check.js` fail-closed reopen gate. See [xlsx-integrity-notes-v0.md](xlsx-integrity-notes-v0.md), [sample-integrity-run.md](sample-integrity-run.md).

**v0 done (OOXML forensics):** `ooxml-forensics.js` + structure indexes + diff/risk docs. Finding: ExcelJS full `writeFile` rewrites all sheets; Excel recovery likely from sheet2 sparse collapse + sharedStrings migration — **not fixed by integrity-only path**. See [ooxml-diff-report-v0.md](ooxml-diff-report-v0.md), [ooxml-risk-analysis-v0.md](ooxml-risk-analysis-v0.md).

**v0 done (sheet1 ZIP patch):** `sheet1-patch-export.js` + `sheet1-xml-builder.js` + `xlsx-zip-patch.js` — clone template, patch **only** `xl/worksheets/sheet1.xml`, SHA-verify sheet2/sheet3/rels byte-identical. See [sheet1-patch-notes-v0.md](sheet1-patch-notes-v0.md), [sample-sheet1-patch-run.md](sample-sheet1-patch-run.md). Commander import still **experimental**.

**v0 done (template cleanup + new entity mode):** stale-row neutralization (clear writable cells, no row delete), `new_campaign_mode` clears Commander ID columns on export rows. See [template-cleanup-rules-v0.md](template-cleanup-rules-v0.md), [new-entity-mode-notes-v0.md](new-entity-mode-notes-v0.md), [sample-cleanup-run.md](sample-cleanup-run.md).

**Future (not implemented):**

- True XML row deletion with regression packs (v0 clears cells only — see [template-cleanup-rules-v0.md](template-cleanup-rules-v0.md))  
- Row virtualization for sparse templates  
- Import-safe ID generation (local deterministic IDs — **not** Direct API)  
- Commander roundtrip reconciliation packs  
- True OOXML patch engine (DOM-based delta, not regex row patch)  
- sharedStrings preservation strategy if Commander ever requires shared index model  
- Minimal XML diff patching with golden-byte regression packs  
- XML diff tools comparing output OOXML vs golden template  
- Template checksum validation (SHA-256 of source xlsx before/after clone)  
- Workbook regression fixtures (committed sample outputs + integrity snapshots)  
- Commander import regression testing (human-operated test account → diff vs JSON)  

- Row-level fidelity (Доп. объявление группы, keyword-only vs ad-only row shapes)  
- Metadata block overwrite (campaign negatives, promotion URL) with operator opt-in  
- Commander-native fastlink/callout delimiter (replace `||` v0 encoding)  
- Match type encoding inside phrase text (documented convention)  
- Multi-template support (template_id + revision adapters)  
- Import roundtrip tests (human-operated Commander test account → diff vs JSON)  
- Schema-template synchronization when `schema_version` or template revision changes  

## Schema adapters

- Support future `schema_version` migration adapters (v1 → v2) without semantic rewrite in transport layer  

## Real template column mapping

- **Done (v0):** clone template xlsx and fill known cells (`--template-fill`)  
- Logical multi-sheet mode remains for architecture testing  

## Batch export

- Multiple documents in one operator session (still human-triggered, still no daemon)  

## Validation-report handshake

- Stale report detection (`STALE_VALIDATION_REPORT`) via document mtime vs `validation_timestamp`  
- Strict `safe_unknown` blocking per [export-preconditions-v1.md](../../exporter/export-preconditions-v1.md)  
- Export manifest JSON alongside XLSX  

## Importer round-trip tests

- Human-operated import to test Commander account → diff against source JSON  

---

## Explicitly out of scope (do not implement without new charter)

- Auto upload to Direct  
- Direct API client  
- CI export gates (unless human requests separate lane)  
- Daemon / watcher / scheduler  
- Orchestration or multi-agent export coordination  
- Auto-fix of validation failures in exporter  
