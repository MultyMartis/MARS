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

Indexing is **never** opened automatically. Use [SEARCH-INDEXING-CONTROL](../standards/FORGE-WORDPRESS-SEARCH-INDEXING-CONTROL-STANDARD-v1.md).

---

## Operator status panel

Update the production Dashboard / system-status widget in the **same wave** as domain, DNS, SSL, SMTP, indexing, environment, or parity changes. Stale “NS pending / future host” after cutover is a **failed DoD**.

Default SMTP technical sender mailbox: `noreply@<domain>` unless the project names another identity. Do not commit credentials.

SMTP Admin storage (WP options) is **not** a dedicated secret manager. Acceptable for studio sites if: write-only password field; blank keeps existing secret; never rendered/logged/REST/Git; autoload off.

Form reliability: persist the internal lead **before** `wp_mail`. Frontend success may mean “submission accepted”, not “email delivered”. Metrika `reachGoal` fires only after backend-confirmed success.

Mail suppression must have an explicit retirement path: NOT CONFIGURED → CONFIGURED/NOT VERIFIED (still suppressed) → VERIFIED → operator activates delivery. Do not auto-enable on Save. Do not leave a second competing mail switch forever.

---

## Forbidden in pre-cutover waves

NS switch without freeze+backup; SSL before DNS; home/siteurl to final host before cert; SMTP skip; indexing open; hardcoded future-host redirects before smoke.

---

*FW-RB-08 v1.*
