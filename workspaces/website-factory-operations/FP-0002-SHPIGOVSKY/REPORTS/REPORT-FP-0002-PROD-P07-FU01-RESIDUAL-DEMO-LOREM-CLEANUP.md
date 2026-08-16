# REPORT — FP-0002 PROD-P07-FU01 Residual DEMO/Lorem Cleanup

**Date:** 2026-08-14  
**Host:** `http://shpigovsky.beget.tech/`  
**Docroot:** `/home/s/shpigovsky/shpigovsky.ru/public_html`  
**Evidence:** `REPORTS/evidence/prod-p07-fu01-residual-demo-lorem-cleanup/`  
**Continuation:** **PROD-P07-FU01-CONT2** exact-file deploy after Beget IP unblock

```text
PROD-P07 TECHNICAL CLOSEOUT COMPLETE — FINAL OPERATOR VISUAL ACCEPTANCE PENDING
PROD-P07 FINAL ACCEPTANCE READY
CURRENT POST-P07 LAYER A BACKUP = OPERATOR CONFIRMED
3/3 SOURCE ↔ PRODUCTION MATCH
NO DB/ADMIN MUTATION — HISTORICAL NON-RENDERED PLACEHOLDERS LEFT UNCHANGED
```

---

## 1. Status

* **PASS**
* transport: **BEGET FILE TRANSPORT RESTORED** (SSH/SFTP)
* production file writes: **3**
* DB/Admin writes: **0**
* WPilot business writes: **0** (`write_enabled=false`)
* commit/push: **none**

---

## 2. Root Cause / Transport

```text
PRIOR TRANSPORT FAILURE ROOT CAUSE = BEGET IP BLOCK — OPERATOR IP UNBLOCKED BY BEGET SUPPORT
```

* SSH/SFTP: **PASS** (`shpigovsky.beget.tech:22`, account `shpigovsky_mars`, `pwd` = production docroot)
* FTP: **NOT_TESTED** (SSH succeeded)
* Selected transport: **SSH/SFTP**

No fail2ban/credential/user/password/security-config work.

---

## 3. Layer B

Snapshot: `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p07-fu01-cont2-layer-b-pre\`  
Created: `2026-08-14T11:58:25Z`  
Captured: **3/3** production-before files + SHA-256 manifest + timestamp + production path map.

| File | Production-before SHA-256 |
|------|---------------------------|
| `inc/v9-static-content.php` | `5ee639d1b05ff4e603c35fc5ec23e7271a639d060b1ef4f14f84dd305d158026` |
| `inc/services-hub-helpers.php` | `ff4024d0a18ab9690741f594c3371794eb1e15efb68751d0ad7e9023887c5d0b` |
| `inc/service-general-helpers.php` | `163f7d2de0fa13d32138f44302ae6dc0fba42d5e713e20be1b1a123b819f89ee` |

Rollback readiness: Layer A operator-confirmed + Layer B exact bytes.

---

## 4. Drift Gate

**MATCH.** Production was still accepted P07. Local canonical was ahead only by approved Lorem/DEMO suppression. No new operator production edits. No canonize-from-production.

`php -l` (Laragon 8.3.30): **No syntax errors detected** on all three local files.

---

## 5. Deploy

Exact upload (3 files, no other surfaces):

1. `wp-content/themes/shpigovsky/inc/v9-static-content.php`
2. `wp-content/themes/shpigovsky/inc/services-hub-helpers.php`
3. `wp-content/themes/shpigovsky/inc/service-general-helpers.php`

Production-after SHA = local canonical:

| File | SHA-256 |
|------|---------|
| `v9-static-content.php` | `3471898fa12c253f97820a7c33754524d2d0e9cab1c50f2aa222755901e55604` |
| `services-hub-helpers.php` | `6e11bbc453d33f395d8bdfe7f6a00e913ce3ee0777c66d46942ff2aca391e305` |
| `service-general-helpers.php` | `b4ac89d7d9e67d7cfabe3c06b3f9ab617863b512b3e0bf210936e73b8eb74293` |

```text
3/3 SOURCE ↔ PRODUCTION MATCH
```

---

## 6. Hub Cleanup (`/uslugi/`)

* Lorem before: **9**
* Lorem after: **0**
* `DEMO —` after: **0**
* Real four-card copy: **preserved**
* Titles / URLs / gallery images (5) / order: **unchanged**
* Empty card `<p class="…__service-text">`: omitted (not malformed empty paragraphs)

---

## 7. Alcohol Cleanup

* Signs Lorem editorial: **before LOREM → after OMITTED**
* Signs items: **9 REAL preserved**
* Program Lorem lead/intros: **before LOREM → after OMITTED** (heading + 4 program cards remain; `$use_emergency` hub chrome did not fire because heading is non-empty)
* FAQ: **10 REAL ACF preserved**; no placeholder fallback; no FAQ DB mutation
* Fabricated clinical content: **NO**
* Guest Visit CTA + Comfort Fancybox: **present**; HTTP 200; no PHP noise

---

## 8. P07 Regression Check

* Desktop program-card 2×2 alignment: **intact**
* Mobile natural card flow: **intact**
* Guest Visit contextual CTA: **intact**
* Generic «Остались вопросы?» on subdivision stages: **intact**
* Approach cards on `/uslugi/zavisimosti/` and `/o-centre/`: **visible**
* Reusable blocks + long-form Generic Content on `/o-centre/programma-lecheniya/`: **styled / present**
* Routes 200: `/uslugi/zavisimosti/`, `/o-centre/programma-lecheniya/`, `/o-centre/`, `/`, `/kontakty/`

---

## 9. Responsive

* Desktop ~1440: no overflow, no empty headings/accordions, no malformed cards
* Mobile ~390: same
* Decorative landscape/corridor image sections are image-only (not cleanup gaps)

---

## 10. DB/Admin

```text
NO DB/ADMIN MUTATION — HISTORICAL NON-RENDERED PLACEHOLDERS LEFT UNCHANGED
```

---

## 11. WPilot

* Public ping 200: plugin `metacode-wpilot`; `write_enabled=false`; bridge on; token-generated
* Proven version remains **0.3.2 / 0.3.2-RC1** (ping body still has no version field)
* Business writes **0**
* Write was **not** enabled

---

## 12. Remaining Residue

* User-facing approved-scope residue: **0** (hub Lorem/DEMO and alcohol signs/program Lorem no longer rendered)
* Historical non-rendered DB residue: ACF Lorem/DEMO values may still exist in Admin; **left unchanged**
* Unrelated migration tails: `.test` URLs, `blogname`, `WP_DEBUG`, `WP_ENVIRONMENT_TYPE`, `home`/`siteurl`, HTTPS, sitemap, DNS, home `demo-pagination-article-*` slugs — **deferred** (not PROD-P06)

---

## 13. Acceptance

```text
PROD-P07 TECHNICAL CLOSEOUT COMPLETE — FINAL OPERATOR VISUAL ACCEPTANCE PENDING
PROD-P07 FINAL ACCEPTANCE READY
```

Do **not** treat this as operator final acceptance.

---

## 14. Git / Secrets

* commit: **none**
* push: **none**
* exposed secrets: **0**
* foreign WIP: **untouched**

---

## 15. Next Recommendation

1. Operator visual review of `/uslugi/` and the alcohol leaf.
2. Operator final P07 acceptance.
3. Fresh full Beget backup after acceptance.
4. Later separate **PROD-P06**.

Do not execute the next wave from this continuation.
