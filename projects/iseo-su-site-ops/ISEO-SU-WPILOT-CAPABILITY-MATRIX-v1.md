# ISEO-SU WPILOT CAPABILITY MATRIX v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 4B  
**Date:** 2026-07-24  
**Package:** `metacode-wpilot-v0.3.0-rc5.zip` (ACCEPTED MATCH)  
**Proven environments (WPilot authority):** DEV `dev.gktriumph.ru`; local FP-0002 write lifecycle (documented). **i-seo.su production: NOT PROVEN.**

Classification vocabulary (may combine):

- IMPLEMENTED IN CURRENT SOURCE  
- INCLUDED IN CANONICAL PACKAGE  
- PROVEN ON DEV  
- PROVEN LOCALLY  
- DOCUMENTED ONLY  
- NOT IMPLEMENTED  
- PRODUCTION NOT PROVEN  
- SAFE UNKNOWN  

---

## Capability groups

| ID | Capability | Classification |
|----|------------|----------------|
| A | Public/minimal ping | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| B | Authenticated site info | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| C | Themes inventory | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV (active theme only); PRODUCTION NOT PROVEN |
| D | Plugins inventory | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV (active plugins); PRODUCTION NOT PROVEN |
| E | Pages/posts inventory | IMPLEMENTED IN CURRENT SOURCE for **pages**; posts CPT inventory NOT IMPLEMENTED; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| F | Single page read | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| G | Structure inspection | IMPLEMENTED IN CURRENT SOURCE (WPBakery-oriented signals); INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| H | Indexing state | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| I | Dry-run replacement | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| J | Backup creation | IMPLEMENTED IN CURRENT SOURCE (plugin table, page `post_content`); INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN — **not** a Beget full backup substitute |
| K | Controlled replacement | IMPLEMENTED IN CURRENT SOURCE (scoped exact-once page replace); INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PROVEN LOCALLY (FP-0002 evidence in WPilot docs); PRODUCTION NOT PROVEN |
| L | Rollback | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| M | Audit log | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| N | Connection tracking | IMPLEMENTED IN CURRENT SOURCE; INCLUDED IN CANONICAL PACKAGE; PROVEN ON DEV; PRODUCTION NOT PROVEN |
| O | Emergency disable | IMPLEMENTED IN CURRENT SOURCE (option + readiness gate); INCLUDED IN CANONICAL PACKAGE; DOCUMENTED + admin UI; PRODUCTION NOT PROVEN |
| P | ACF read/write | NOT IMPLEMENTED |
| Q | CPT read/write | NOT IMPLEMENTED (pages only) |
| R | Theme settings | NOT IMPLEMENTED |
| S | Menus/widgets | NOT IMPLEMENTED |
| T | Filesystem/static HTML | NOT IMPLEMENTED |
| U | Database administration | NOT IMPLEMENTED (plugin-owned tables only; no general DB admin) |
| V | Media | NOT IMPLEMENTED |
| W | Cache purge | NOT IMPLEMENTED |

---

## Notes for i-seo.su

1. Groups A–O are the only candidates for future production gates; P–W remain out of scope for WPilot on this hybrid site.  
2. Production write readiness (K/L/I beyond dry analysis policy) is **not** part of Phase 4B package-install GO.  
3. Beget full backup remains mandatory operator control independent of capability J.

---

*Capability matrix v1 · 2026-07-24.*
