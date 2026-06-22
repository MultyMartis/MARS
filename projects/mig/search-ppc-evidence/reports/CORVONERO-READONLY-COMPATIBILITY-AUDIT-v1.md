# Corvonero Read-Only Compatibility Audit v1

**Date:** 2026-06-23  
**Corvonero status:** FROZEN — no new collection  
**Session inspected:** `incoming/mig/pilots/corvonero/session-mig-20260622-corv01`

## Findings

| Area | Compatibility | Notes |
|------|---------------|-------|
| Source registry | PARTIAL | Legacy schema 0.1 lacks Wave 2 required fields |
| Corpus intake | INCOMPATIBLE AS-IS | Pilot keyword/demand artifacts need mapping |
| Normalization/provenance | PARTIAL | phrase_normalized exists; source_row refs missing |
| SERP classification | PARTIAL | Paid ads often embedded in organic_results via yabs URLs |
| Dates/times | COMPATIBLE | ISO timestamps present |
| Paid vs organic | NEEDS RECLASSIFICATION | visible_ads frequently empty |
| CAPTCHA/incomplete | COMPATIBLE | captcha_status field used |

## Migration/repair list (no canonical mutation)

1. Sidecar mapping from legacy source-registry 0.1 → Wave 2 schema
2. Read-only reclassification index for yabs URLs found in organic_results
3. Retroactive timezone/business-hours metadata where operator approves
4. keyword_registry → canonical-registry mapping charter
5. **Do not** modify frozen Corvonero canonical evidence to pass new validators
