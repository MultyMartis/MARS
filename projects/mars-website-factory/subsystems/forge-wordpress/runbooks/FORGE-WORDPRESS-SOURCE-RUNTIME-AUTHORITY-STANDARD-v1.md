# Forge WordPress — Source / Runtime Authority Standard v1

**ID:** FW-RB-01  
**Status:** ACTIVE — CANONICAL  
**Date:** 2026-08-18  
**Class:** C  
**Evidence:** FP-0002 SOURCE-AUTHORITY; P04-FU02; P14

---

## Triple authority

| Surface | Role |
|---------|------|
| Production filesystem (host docroot) | **LIVE RUNTIME TRUTH** for PHP/CSS/JS that is deployed |
| Production database | **LIVE CONTENT / ADMIN TRUTH** |
| MARS Git `WORDPRESS/` (theme, plugin, ACF JSON) | **CODE AUTHORITY** |

Local MLI copies are **dev references**. They must not automatically overwrite production.

When the operator edits production files or Admin:

```text
PRODUCTION DRIFT MUST BE INTAKEN AND CANONIZED BEFORE THE NEXT AUTOMATED DEPLOY
```

---

## Filesystem procedure

1. Download current prod file  
2. Hash (SHA256)  
3. Compare to Git source  
4. Classify: operator-legitimate / accidental / ours  
5. Canonize legitimate work into Git  
6. Modify source  
7. Exact deploy of allowlisted files  
8. Production-after hash; **source/prod parity**

Never: theme directory mirror, `robocopy /MIR`, stale source, uploads overwrite, old DB restore over live Admin content without explicit approval.

---

## Content procedure

Prefer WP Admin (or chartered WPilot write) for posts, ACF **values**, menus, media, forms, SEO values. If a value has a Git representation, canonize back.

---

*FW-RB-01 v1.*
