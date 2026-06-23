# FP-0002 Services Hub Unique Block Audit v1

**Authority:** `SERVICES-HUB-DESKTOP.png` + `SERVICES-HUB-MOBILE.png` + Figma frame `Услуги хаб` (`1:1310`) / `Услуги хаб - моб` (`1:4624`)  
**Date:** 2026-06-23

| Order | Block | Desktop bounds | Mobile bounds | Existing/New | Text authority | Image authority |
| ----: | ----- | -------------- | ------------- | ------------ | -------------- | --------------- |
| 1 | Header (reuse) | top chrome | mobile header + menu | EXISTING | operator header partial | NONE |
| 2 | Service Hero | `1:1311` hero band | `1:4625` mobile hero | NEW | Figma `1:1355–1:1357`, breadcrumb `1:1364–1:1366` | Figma `1:1351` hash `1244eb1e5374a84f8164f521dc48d8e99c2cc630` |
| 3 | Зависимости и пристрастия | `1:1405` | `1:4676` | NEW | Figma `1:1409–1:1463` + PNG subsection order | Cards `1:1470`, `1:1471`, `1:1472` |
| 4 | Психическое здоровье | `1:1474` | `1:4744` | NEW | Figma `1:1478–1:1558` (no lorem bodies) | Cards `1:1565`, `1:1566`, `1:1567` |
| 5 | Расстройства пищевого поведения | `1:1569` | `1:4832` | NEW | Figma `1:1573–1:1601` (no lorem bodies) | NONE (text-first section) |
| 6 | Program (reuse) | `1:1610` | `1:4880` | EXISTING | parameterized heading on `/uslugi/` | existing program assets |
| 7 | Founder quote (reuse) | `1:1649` | `1:4913` | EXISTING | shared partial | existing founder photo |
| 8 | Comfort (reuse) | `1:1665` | `1:4932` | EXISTING | shared partial | existing comfort gallery |
| 9 | FAQ (reuse) | `1:1720` | `1:4985` | EXISTING | shared partial | NONE |
| 10 | Final form (reuse) | below FAQ | below FAQ | EXISTING | shared partial | NONE |
| 11 | Footer (reuse) | `1:1747` | `1:5011` | EXISTING | operator footer partial | NONE |

## Confirmed scroll order (PNG + Figma hub frame)

1. Header  
2. Service Hero — «Лечение и профилактика»  
3. Зависимости и пристрастия  
4. Психическое здоровье  
5. Расстройства пищевого поведения  
6. Наша программа включает 4 направления (shared Program)  
7. Founder quote  
8. Comfort  
9. FAQ  
10. Final form  
11. Footer  
12. Modal component (once)

## Excluded from hub render

| Block in Figma | Reason |
| -------------- | ------ |
| `2 - Дом - вступление` (`1:1374`) | Not present between Hero and addictions on operator PNG authority |
| `С чего начать` dark CTA (`1:1715`) | Not in operator PNG unique zone; deferred |
| Genotyping promo tail (`32:4586`) | Not in operator PNG hub order |

## URL notes

| Item | Status |
| ---- | ------ |
| Mental health cards «Стресс», «Неврозы» | **URL — BLOCKED** (no confirmed leaf slug); rendered as static cards |
| All other internal links | `/slug/` from `foundation/FP-0002-V6-URL-MAP.md` |
