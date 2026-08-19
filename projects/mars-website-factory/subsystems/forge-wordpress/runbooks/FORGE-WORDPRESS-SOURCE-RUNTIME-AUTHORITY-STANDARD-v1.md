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

When the operator edits production files or Admin **or WordPress options (home/siteurl) during an active cutover**:

```text
PRODUCTION DRIFT MUST BE INTAKEN AND CANONIZED BEFORE THE NEXT AUTOMATED DEPLOY
DO NOT BLINDLY EXECUTE AN OLD RUNBOOK STEP THAT WOULD REVERT A LEGITIMATE OPERATOR CHANGE
```

Procedure for a mid-cutover manual change:

1. Fresh intake (read actual options / DNS / HTTP).  
2. Verify.  
3. Accept and canonize if legitimate.  
4. Rewrite the **remaining** plan (skip completed steps).

Evidence: FP-0002 P18A — operator set `home`/`siteurl` to `https://shpigovsky.ru` before the planned P18 mutation.

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

Explicit rule:

```text
EDITORIAL DB CHANGE THROUGH NORMAL WORDPRESS ADMIN
≠
UNCONTROLLED CODE DRIFT
```

Do not restore an older full DB snapshot over live editorial/Admin work merely to recover a technical configuration. Technical rollback must use the smallest scoped object/file restore that resolves the fault.

---

*FW-RB-01 v1.2 — includes editorial/Admin truth distinction for technical closeout waves.*
