# CORVONERO COMMANDER CT-5 ORCHESTRATOR REVIEW v1

**Reviewed:** 2026-06-30  
**Orchestrator:** `pilots/corvonero/tools/execute-ct5-commander-generation-v1.mjs`  
**Git state:** untracked new file at review  
**Repository commit:** `8943e07e5f6b45d8e6cfd209a30cac55e2f0bb86`

## Purpose

Safe CT-5 Commander XLSX generation and forensic verification from committed CT-4 authority. Uses `commander-transport` and Triumph patcher adapter only. Local candidates — no Commander import, no Yandex Direct API.

## Security surface

| Control | Result |
|---------|--------|
| Deprecated C:/D:/E paths | 0 |
| Network access | 0 |
| OpenRouter | 0 |
| Semantic cache | 0 |
| Git mutation | 0 (read-only `git rev-parse`) |
| Commander automation | 0 |
| Yandex Direct | 0 |
| Broad delete | 0 (conditional output-dir rmSync only on prior FAIL) |

## CT-5-only transport fixes

### A. Sheet-row extension

The base patcher patches existing `<row>` nodes only. The v1 template ships prototype transport rows through ~row 84; CA-01 requires 346 rows from data start row 16. `extendSheetForExport` clones prototype row 16 XML for each missing row and updates `<dimension>` in **sheet1.xml only**. Styles, shared strings, relationships and other sheets remain byte-preserved via `patchSheet1InWorkbook`. Maximum tested: 346 rows (CA-01). Failure: throws if prototype row or `</sheetData>` missing.

### B. Metadata-key translation

| Authority key | Payload key | Commander destination | Value source |
|---------------|-------------|----------------------|--------------|
| Тип кампании: | metadata_patches | campaigns.campaign_type (row 7 col 5) | payload-builder |
| Минус-фразы на кампанию: | metadata_patches | campaigns.campaign_negatives (row 9 col 5) | CT-4 negatives |
| Оптимизировать текст объявлений под запрос: | metadata_patches | campaigns.optimize_text (row 10 col 5) | constant `0` |
| Объект продвижения: | metadata_patches | campaigns.promotion_url (row 11 col 5) | first group ad URL base |
| № заказа: | metadata_patches | campaigns.currency (row 8 col 8) | constant `RUB` |

No strategic values invented.

### C. Fastlink clearing

Columns 58–60 cleared to empty strings in `buildFillRows`. Sitelinks **OMITTED** per CT-4 transport config. All five outputs verified empty.

### D. Organization blanking

- Data column: **50**
- Metadata field: **Организация из Яндекс Бизнеса:** (row 12 col 5)
- Output: blank; forbidden ID occurrences: **0**
- Classification: **final safety guard** compensating for upstream defect — base transport does not clear organization after row clone; `TEMPLATE_METADATA_CELL_MAP` lacks organization entry.

## Original output hash verification

**Task binding SHA-256:** not matched (binding values not attested in storage or repository).

**On-disk self-consistency:** verified — recalculated hashes match manifest and generation receipts.

## Classification

**SAFE FOR THIS FROZEN CT-5 OUTPUT BUT REQUIRES BASE TOOLING PATCH BEFORE REUSE**

Recommended moves into `tools/commander-transport/`: row extension, metadata translation, organization blanking; fastlink defaults already partially in adapter.
