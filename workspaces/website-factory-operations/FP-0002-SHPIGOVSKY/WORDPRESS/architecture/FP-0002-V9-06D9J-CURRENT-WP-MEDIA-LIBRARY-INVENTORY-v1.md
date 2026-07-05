# FP-0002 V9-06D9J Current WP Media Library Inventory v1

**Date:** 2026-07-05  
**Mode:** READ_ONLY  
**Evidence:** `validation/v9-06d9j-media-selection-upload-plan/current-wp-media-library-inventory.json`

## Summary

| Metric | Value |
|--------|-------|
| Uploads directory | `wp-content/uploads` — **exists** |
| Attachment count | **0** |
| Home ACF image attachments | **0** |

## Read-only finding

The WordPress Media Library contains **no attachments** at D9-J baseline. All Home imagery is served from theme static assets under `wp-content/themes/shpigovsky/assets/`.

## Implication for D9-K

D9-K will create the **first** FP-0002 Home-related media attachments. No deduplication against existing library entries is required; filename/checksum manifest must be recorded at upload time.

## Safe candidate mapping

No existing attachments match static/theme assets by ID. All five D9-K upload candidates are **new attachment creates**.
