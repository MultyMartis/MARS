# Forge WordPress — Pre-Cutover and Launch SOP v1

**ID:** FW-RB-08  
**Status:** ACTIVE — CANONICAL LAUNCH SEQUENCE  
**Date:** 2026-08-18  
**Class:** D  
**Evidence:** FP-0002 P17 / P17-FU02 / P18A (operator NS + URL cutover; SSL/origin bind still open)

---

## Sequence

```text
freeze
→ fresh full backup
→ source/prod parity
→ DNS / NS (or A-record)
→ authoritative DNS verification (web AND mail)
→ SSL
→ home / siteurl          ← skip if operator already set them; intake instead
→ exact URL migration (bounded manifest)
→ rewrite flush / cache
→ smoke while INDEXING CLOSED
→ SMTP
→ forms delivery proof
→ robots / indexability
→ sitemap submissions
→ final crawl
```

If the operator already switched NS and/or `home`/`siteurl`: **do not wait** on those steps and **do not revert** them. Continue from SSL / origin bind / HTTPS smoke.

Readiness matrix: [PRE-CUTOVER-READINESS-MATRIX](../templates/FORGE-WORDPRESS-PRE-CUTOVER-READINESS-MATRIX-v1.md).

---

## Indexing gate

```text
DO NOT OPEN INDEXING JUST BECAUSE THE DOMAIN WORKS.
```

Required **before** `blog_public=1` / robots Allow:

| Gate | Result needed |
|------|----------------|
| HTTPS | PASS |
| Canonical host | PASS |
| Sitemap on **final** domain | PASS |
| Frontend smoke | PASS |
| WP Admin | PASS |
| Forms | PASS |
| SMTP delivery | PASS |
| Redirects | PASS |

Then: robots/indexability → Webmaster / Search Console → submit sitemap → final crawl.

---

## Forbidden in pre-cutover waves

NS switch without freeze+backup; SSL before DNS; home/siteurl to final host before cert; SMTP skip; indexing open; hardcoded future-host redirects before smoke.

---

*FW-RB-08 v1.*
