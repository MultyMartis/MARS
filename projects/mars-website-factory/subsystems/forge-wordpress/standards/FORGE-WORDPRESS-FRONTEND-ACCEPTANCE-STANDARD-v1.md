# Forge WordPress — Frontend acceptance standard v1

**ID:** FW-S-46  
**Status:** ACTIVE — QA STANDARD  
**Date:** 2026-08-18  

A component is **not DONE** because a screenshot matches.

---

## 1. Acceptance dimensions

| Dimension | Pass means |
|-----------|------------|
| Data states | filled / empty optional / unpublished relation |
| Empty state | no demo, no broken card chrome ([COMPONENT-DATA-CONTRACT](FORGE-WORDPRESS-COMPONENT-DATA-CONTRACT-STANDARD-v1.md)) |
| Long text | titles/excerpts wrap; no overflow hiding CTAs |
| Short text | layout still holds |
| Missing optional media | placeholder policy honored (none or designed fallback — **not** a random stock image unless approved) |
| Keyboard | [FW-S-37](FORGE-WORDPRESS-ACCESSIBILITY-BASELINE-v1.md) |
| Responsive | [FW-S-36](FORGE-WORDPRESS-FRONTEND-INTERACTION-OWNERSHIP-STANDARD-v1.md) §4 |
| Device/input | [FW-S-42](FORGE-WORDPRESS-REGRESSION-PACK-v1.md) risk matrix |
| Editor mutation | change the CMS field; frontend updates; no code deploy |
| Accessibility basics | labels, focus, alt |

---

## 2. Content stress tests (CMS + frontend)

Maintain fixtures or a one-time QA object covering:

- very long title  
- very short title  
- missing optional image  
- 1 repeater row  
- many allowed repeater rows (at the documented max)  
- Cyrillic  
- punctuation / NBSP (typography owner still correct; search still finds)  
- long URL in a field that can contain URLs  
- unpublished relation  
- deleted relation (no fatal, no empty link)

Do not design only around perfect demo content.

---

*FW-S-46 v1.*
