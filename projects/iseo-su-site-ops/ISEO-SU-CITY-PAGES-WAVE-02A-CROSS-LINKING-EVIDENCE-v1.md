# ISEO-SU CITY PAGES WAVE 02A CROSS-LINKING EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-CITY-PAGES-WAVE-02A-CROSS-LINKING`  
**Date:** 2026-09-04  
**Site:** `https://i-seo.su/`  
**Decision:** **PASS / COMPLETE — 5 CITY SEO PAGES FULLY CROSS-LINKED / HUB + CITY NAVIGATION MODEL ACTIVE**

---

## 1. Scope

WAVE 02A only:

- Compact City ↔ City navigation block on all 5 published regional SEO city pages
- Preserve existing Hub ↔ City linking (hub → 5 cities; each city → hub)
- No sitemap / title / description / H1 / FAQ / canonical / menu / form / calculator consent changes
- No new CSS file; reuse existing `content_block` / `uni_check_list__list` pattern from hub

**Not started:** additional city page pack (await separate operator charter).  
**Hub `b-regionakh.html`:** no functional change (already links to all 5 cities).

---

## 2. Linking Model (after WAVE 02A)

| Edge | Status |
|------|--------|
| Hub → 5 cities | retained (WAVE 02) |
| Each city → Hub | retained (WAVE 02) |
| Each city → all 5 cities | **added** (current city non-linked span; 4 outbound `<a>`) |

Future additional city/page pack (when approved) must extend the same `#city-seo-cross-nav` pattern — do not invent speculative URLs here.

---

## 3. Source Paths

Canonical editable source (pre-production):

`X:\AI MARS\projects\iseo-su-site-ops\production-source\static-html\services\seo\`

| Page | Source file |
|------|-------------|
| Санкт-Петербург | `prodvizhenie-v-sankt-peterburge.html` |
| Казань | `prodvizhenie-v-kazani.html` |
| Екатеринбург | `prodvizhenie-v-ekaterinburge.html` |
| Новосибирск | `prodvizhenie-v-novosibirske.html` |
| Красноярск | `prodvizhenie-v-krasnoyarske.html` |

Shared include model for city list: **absent** — static HTML markup duplicated with identical structure; documented for easy expansion.

---

## 4. Block Spec

| Field | Value |
|-------|-------|
| Block id | `city-seo-cross-nav` |
| Title (all pages) | **Продвижение сайтов в других городах** |
| Placement | After main city SEO `content_block`, immediately before «Тарифы» (`<h2>Тарифы</h2>` / `02`) |
| Current city | `<span class="city-seo-cross-nav__current" aria-current="page">…</span>` (not clickable) |
| Other cities | plain `<a href="https://i-seo.su/services/seo/…">` — no `rel="nofollow"`, no `target="_blank"` |
| CSS | existing classes only; no new stylesheet |

---

## 5. Production Backup

Backup root:

`X:\AI MARS\local\sites\iseo-su-production\_city-pages-wave-02a-cross-linking\backup-20260904T014744Z`

| Production path | Backup path | SHA-256 before | Timestamp UTC |
|-----------------|-------------|----------------|---------------|
| `/home/n/nikel0rv/i-seo.su/public_html/services/seo/prodvizhenie-v-sankt-peterburge.html` | `…\backup-20260904T014744Z\prodvizhenie-v-sankt-peterburge.html` | `d023d3d79cf5e8c494fc2d9f1fb261d223fe2762a9b2001280c323bbbd08605f` | 20260904T014744Z |
| `…/prodvizhenie-v-kazani.html` | `…\prodvizhenie-v-kazani.html` | `318eb1950edaf6f5135be204513d3c4c96ab751fa3de54475cf161f9f194a756` | 20260904T014744Z |
| `…/prodvizhenie-v-ekaterinburge.html` | `…\prodvizhenie-v-ekaterinburge.html` | `4bba37ebbc8f668bdc1d31877940bf53110cf6358eeae38b3f5c9fc160c8f4fb` | 20260904T014744Z |
| `…/prodvizhenie-v-novosibirske.html` | `…\prodvizhenie-v-novosibirske.html` | `8c9e7ecc6a30570ca0d04f97f5cb3065221d22a0b9e661949bf1e3e404dd1ce1` | 20260904T014744Z |
| `…/prodvizhenie-v-krasnoyarske.html` | `…\prodvizhenie-v-krasnoyarske.html` | `8f180a319e358d9d89dec396ee79016abe0e4c3f9737ee350c9dd1dfef7799a2` | 20260904T014744Z |

---

## 6. Deployment

SFTP scoped upload of **5 city HTML only** (source → production). Verify match TRUE for all.

| File | Post-deploy SHA-256 | Verify |
|------|---------------------|--------|
| `prodvizhenie-v-sankt-peterburge.html` | `eb0244287b752493222ee9e120fabb4d0667266a21616024c0d57ce9817c2398` | TRUE |
| `prodvizhenie-v-kazani.html` | `d0444217d6d16eaeb16891fe346c028c9e3504ffdc4f2bcc0d2d25353b74a09b` | TRUE |
| `prodvizhenie-v-ekaterinburge.html` | `f17027925c6b842cb0029449183166b6457f2a9fd3e5e8fb69a0924086939005` | TRUE |
| `prodvizhenie-v-novosibirske.html` | `de54cb53b728f26fa8d63e0d03868154347a1c8006d828ec042f0f55d61ebf8d` | TRUE |
| `prodvizhenie-v-krasnoyarske.html` | `c0bcc2f6ac7f00e17533454ce64d73adc6a058a937f8422eada7444f544dad5d` | TRUE |

**PRODUCTION/SOURCE ALIGNED:** YES

---

## 7. Live Validation Summary

JSON evidence: `tools/_wave02a_deploy_validate.json`

| Check | Result |
|-------|--------|
| CITY PAGES CHECKED | 5 |
| CITY NAV BLOCK ADDED | YES |
| CITY NAV BLOCK PAGES | 5/5 |
| CURRENT CITY STATE | DISTINCT / NON-LINKED |
| CROSS-CITY LINKS PER PAGE | 4 |
| CROSS-CITY TARGETS VALID | 20/20 |
| CITY ↔ CITY CONNECTIVITY | PASS |
| CITY → HUB BACKLINK | 5/5 |
| HUB → CITY LINKS | 5/5 |
| TITLE / DESCRIPTION / H1 / FAQ / CANONICAL | unchanged |
| SITEMAP CHANGED | NO |
| STATIC SITEMAP URL COUNT | 132 |
| FORM / CALCULATOR CONSENT | NONE regression |
| LAYOUT REGRESSION | NONE |

Hub smoke: HTTP 200; city links 5/5; cross-nav block **absent** on hub (expected).

---

## 8. Tools Used

- `tools/_wave02a_patch_source.py` — insert nav into 5 source HTML files
- `tools/_wave02a_backup_deploy_validate.py` — backup, deploy, live validate
- `tools/_wave02a_deploy_validate.json` — machine evidence

---

## 9. Git / Remote Sync

| Field | Value |
|-------|--------|
| Isolated worktree | `X:\AI MARS STORAGE\git-sync-iseo-su-city-pages-wave-02a-cross-linking\repo` |
| Sync base | `origin/mars/canonical-post-recovery` @ `97b53b5f` (`docs(iseo-su): record usa-uae wave-03 remote sync`) |
| Feature commit | `d2b162e1` — `feat(iseo-su): cross-link regional seo city pages` |
| Remote sync | FF to `origin/mars/canonical-post-recovery` without force (`97b53b5f..d2b162e1`) |
| PROJECT-OWNED UNCOMMITTED | 0 (after docs sync closeout) |
| FOREIGN WIP | preserved on dirty main worktree |

---

## 10. Stop Condition

WAVE 02A closed. Do **not** start additional city pages without a new operator charter.

**COMPLETE** — 5 city SEO pages fully cross-linked; Hub + City navigation model active; remote sync COMPLETE @ `d2b162e1`.
