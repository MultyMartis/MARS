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

**v0.1 done (Commander import feedback fix):** distinct `group_number`, group name normalization, autotarget phrase suppression, metadata block patch (rows 7–12), empty status export, stale-row transport mask (`-`). See [import-feedback-fixes-v0.1.md](import-feedback-fixes-v0.1.md), [commander-import-observations-v0.md](commander-import-observations-v0.md), [sample-feedback-fix-run.md](sample-feedback-fix-run.md).

**v0.2 done (domain + max fastlinks):** production host `manipulator-triumph.ru`, SEO slug routing in schema/fixture, 8-fastlink ORCA doctrine in validation/prompts, `normalizeFastlinksForTransport()` in mapping.js. See [domain-fastlinks-v0.2-notes.md](domain-fastlinks-v0.2-notes.md).

**v0.3 done (display URL + sitelink routing):** Commander short display path transport (no domain/slash), `normalizeDisplayPathForTransport()`, fastlink URL dedupe + production slug discipline, fixture display paths + diversified sitelinks. See [display-url-routing-v0.3-notes.md](display-url-routing-v0.3-notes.md), [sample-display-url-routing-run.md](sample-display-url-routing-run.md).

**v0.4 done (import refinement):** Image/creative column cleanup (64–66), geo col 52 for all export rows, `normalizeTransportText()` (×→x), search-only ad type mask (`-`). See [image-cleanup-notes-v0.4.md](image-cleanup-notes-v0.4.md), [geo-routing-notes-v0.4.md](geo-routing-notes-v0.4.md), [transport-symbol-normalization-v0.4.md](transport-symbol-normalization-v0.4.md), [sample-import-refined-v0.4-run.md](sample-import-refined-v0.4-run.md).

**v0.5 done (ad type literal):** col 2 «Тип объявления» = **Текстово-графическое** on export rows; image/creative cleanup preserved. See [ad-type-literal-fix-v0.5.md](ad-type-literal-fix-v0.5.md), [sample-ad-type-v0.5-run.md](sample-ad-type-v0.5-run.md).

**v0.6 done (region import fix):** col 52 = single label **Краснодарский край** (no multi-line city); operator `direct.xlsx` evidence. See [commander-region-fix-v0.6.md](commander-region-fix-v0.6.md), [sample-region-v0.6-run.md](sample-region-v0.6-run.md).

**v0 done (safe sheet1 data row removal):** physical removal of stale template data rows after `lastExportRow`, dimension update when deterministic, merge-cell safety check. Default `rowRemovalMode: true`; `--no-row-removal` for legacy neutralization. See [safe-row-removal-notes-v0.md](safe-row-removal-notes-v0.md), [sample-row-removal-run.md](sample-row-removal-run.md).

**Future (not implemented):**

- Conditional formatting / ignoredErrors audit after row removal  
- True XML row deletion with golden-byte regression packs beyond triumph fixture  
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
