# Commander Template Sanitization Spec v1

**Status:** IMPLEMENTED  
**Module:** `tools/commander-transport/src/template-sanitizer.mjs`  
**Manifest:** `tools/commander-transport/contracts/template-sanitization-manifest-v1.json`

## Requirement

Mandatory sanitization phase **before** project data is applied to Commander template.

## Operations

- Clear E9 campaign negatives
- Clear E12 organization metadata
- Clear E11 promotion URL
- Clear E7 campaign type (generator sets)
- Clear col 50 organization on all data rows
- Clear sitelink columns 58–60 on data rows

## Contamination detector

`scanTemplateContamination()` reports populated semantic fields and matched stale signatures.

## Integration

`commander-patcher-adapter.mjs` calls `sanitizeTemplateSheetXml()` before row extension and patching.
