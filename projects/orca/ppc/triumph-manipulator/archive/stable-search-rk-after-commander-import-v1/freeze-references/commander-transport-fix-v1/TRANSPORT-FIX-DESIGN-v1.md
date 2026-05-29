# TRANSPORT FIX DESIGN v1

**Label:** `orca-commander-transport-fix-design-v1`  
**Date:** 2026-05-29  
**Version:** v1.2 transport split

---

## Problem statement

Direct Commander flat import (`sheet1.xml` / «Тексты») treats **each populated row** as an ad candidate when headline + URL columns are filled. The v1.1 exporter wrote **keyword × ad** rows (108), so Commander showed **108 ads** instead of **20**.

---

## Design: split row model

Replace Cartesian product with **two disjoint row kinds** per group:

| Row kind | Count (Triumph instance) | Populated columns | Cleared columns |
|----------|--------------------------|-------------------|-----------------|
| **AD** | 20 | group ids/names, headlines, text, URL, display path, fastlinks, callouts, region, ad type | `keywords.phrase`, `keywords.status` |
| **KEYWORD** | 64 | group ids/names, phrase, keyword status, region | all `ads.*` text/URL/extension cols, `ads.ad_type` |

**Row order per group:** all ads first (stable `ad_id` sort), then all keywords (stable phrase sort).

**Total sheet1 data rows:** 84 (= 20 + 64).

---

## Column 1 — «Доп. объявление группы»

| Row | Value |
|-----|-------|
| First ad in group | empty |
| 2nd+ ad in same group | `+` |
| Keyword row | empty |

Mapped in `commander-header-map-v0.json` as `ads.group_additional_ad` col 1 (verified).

---

## Integrity probe mode

`xlsx-integrity-check.js` gains `probeLogicalKeysMode: "any-row"` when `transport_row_type` is present — first row may be ad-only (no phrase).

---

## Out of scope (unchanged)

- JSON instance semantics
- Keyword phrases, ad copy, URLs
- Commander import / launch
- Match-type column (still unsupported)

---

## Implementation map

| Module | Responsibility |
|--------|----------------|
| `mapping.js` | `mapTemplateFillRows()` → split rows + `transport_row_type` |
| `sheet1-xml-builder.js` | `buildFieldPatches()` routes fields by row type |
| `sheet1-patch-export.js` | ZIP patch + integrity `any-row` probes |
| `_validate-no-duplicate-ads-v1.js` | Post-export counts + duplicate signature QA |
