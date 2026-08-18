# REPORT — FP-0002 PROD-P18A Live Domain + Legal State

**Date:** 2026-08-18  
**Host (WordPress):** `http://shpigovsky.beget.tech/` inner routes; options `https://shpigovsky.ru`  
**Core:** `0.3.10-p18a`  
**WPilot writes:** 0 (`write_enabled=false`)

---

## 1. Status

**PARTIAL PASS**

Legal demo-state fix and operator URL/NS intake are complete. Public apex is **not** yet the WordPress origin (legacy HTML still served on `https://shpigovsky.ru/`). SSL for the WordPress vhost is **not** final.

---

## 2. Live Domain Reality

**OPERATOR LIVE-DOMAIN CUTOVER INTAKEN AS CURRENT PRODUCTION REALITY**

| Item | Exact current value |
|------|---------------------|
| `home` | `https://shpigovsky.ru` |
| `siteurl` | `https://shpigovsky.ru` |
| DNS NS | Beget set (operator cutover **performed**) |
| DNS A apex @8.8.8.8 | `45.130.41.70` — **not** WP vhost `91.106.207.76` |
| DNS A apex local | `92.255.111.71` (legacy REG.RU IP / cache) |
| HTTP `http://shpigovsky.ru/` | 301 → `https://shpigovsky.ru/` |
| HTTPS `https://shpigovsky.ru/` | 200 **legacy** site (not `wp-content`) |
| HTTP beget `/privacy-policy/` etc. | 200 WordPress |
| HTTP beget `/` | 301 → `https://shpigovsky.ru/` (legacy) |
| SSL | See §12 |

Do **not** revert `home`/`siteurl`.

---

## 3. MARS State

**CURRENT MARS BRAIN KNOWS SHPIGOVSKY.RU IS THE LIVE PRODUCTION DOMAIN**

Updated: `PROJECT-STATUS.md`, baseline `FP-0002-PROD-BASELINE-2026-08-18-P18A`, `OPEN-ITEMS-FP-0002-AFTER-P18A.md`, P18 runbook (current execution), `DOCS/PRODUCTION/FP-0002-DNS-CUTOVER-STATUS-v1.md`, MetaCODE dashboard widget.

NS / `home` / `siteurl` are **not** listed as pending.

---

## 4. Legal Page State

| ID | Slug | Status | `legal_status` | `legal_demo_marker` | `legal_production_blocker` |
|----|------|--------|----------------|---------------------|------------------------------|
| 3 | privacy-policy | publish | production_ready | `0` (exists) | `0` |
| 22 | user-agreement | publish | production_ready | `0` | `0` |
| 23 | consent-personal-data | publish | production_ready | `0` | `0` |
| 24 | cookie-files-policy | publish | production_ready | `0` | `0` |

Autosaves exist (#2071/#2077/#2073). Saved flags are on the canonical posts. Screenshot (Production ready + Demo OFF + Blocker OFF) matches **saved** meta, not an unsaved-only preview.

**LEGAL PAGE STATE OWNER IDENTIFIED:** ACF group `group_fp02_page_legal` / meta `legal_*` + template `document-page.php`.

---

## 5. Root Cause

**LEGAL DEMO BANNER ROOT CAUSE PROVEN**

Class **H:** the theme template **hardcoded** the DEMO paragraph and never read `legal_demo_marker`. Single owner. See `evidence/prod-p18a-live-domain-legal-state/ROOT-CAUSE.md`.

---

## 6. Fix

| Path | Change |
|------|--------|
| `theme/inc/legal-helpers.php` | **new** — three-state boolean; demo/blocker/status readers |
| `theme/functions.php` | require helper |
| `theme/template-parts/legal/document-page.php` | banner only if demo marker ON |
| `plugin/src/Fields/FieldGroups.php` | RU editor labels; independent instructions; `ui` on true_false |
| `plugin/src/Admin/EditorRestrictions.php` | blocker notice no longer says DEMO |
| `plugin/src/Admin/SystemDashboard.php` | live domain / SSL / remaining tails |
| `plugin/shpigovsky-core.php` | `0.3.10-p18a` |
| `acf-json/group_fp02_page_legal.json` | labels (Git schema; PHP is runtime) |

**DB writes:** none for legal **text**. Reversible QA toggles on `#3` **restored**. Dashboard option `fp02_metacode_system_meta` updated (operational meta only).

---

## 7. Boolean Semantics

**EXPLICIT FALSE IS PRESERVED AS FALSE — DEFAULTS APPLY ONLY TO UNSET STATE**

`metadata_exists` → if missing, default `true` (historical ACF default). If present, `'0'`/`0`/`false` → OFF. No `?: true`.

Independent machine:

- `legal_status` — editorial status; `production_ready` does **not** imply DEMO  
- `legal_demo_marker` — **only** DEMO banner owner  
- `legal_production_blocker` — Admin stop flag; does **not** drive the banner  

---

## 8. Legal QA

| Case | Result |
|------|--------|
| Demo OFF (all 4 published) | no banner |
| Demo ON (#3) | banner |
| Demo OFF again | no banner |
| Blocker ON + Demo OFF | no banner |
| Preview | helper uses current ID, parent if revision lacks key; published = CASE 1 |

**DEMO MARKER OFF = NO DEMO BANNER**

---

## 9. Placeholder Audit

See `REPORTS/LEGAL-DEMO-PLACEHOLDER-INVENTORY.md`.

Remaining `[ДЕМО]`: **one** on page **24** Cookie — `[ДЕМО: перечень подключённых систем аналитики]` — **OPERATOR CONTENT REQUIRED**. Pages 3/22/23: none. No invented requisites. No legal wording rewrite.

---

## 10. Admin UX

Labels (machine names unchanged): Статус документа, Демо-версия, Дата вступления в силу, Версия документа, Блокирует публикацию. Status choices: Демо / На проверке / Готов к публикации.

---

## 11. Live Domain Regression

On **WordPress** (beget inner routes, no follow):

| Surface | Note |
|---------|------|
| Canonical | `https://shpigovsky.ru/...` (matches WP home) |
| REST | `url`/`home` = `https://shpigovsky.ru`; `shpigovsky/v1` present |
| Sitemap request on beget | 301 → `https://shpigovsky.ru/wp-sitemap.xml` (currently **legacy** host) |
| robots Sitemap line | still `http://shpigovsky.beget.tech/wp-sitemap.xml` (P17 manifest PHASE C; not rewritten here) |
| Media/menus/CTA | no broad search-replace |
| Public apex | **legacy** site — not a WP regression |

Temporary-host 301 of `/` to apex is **already live** and currently sends users to the **legacy** origin. Do not add more host redirects until WP owns public HTTPS.

---

## 12. SSL

- Public apex: Let's Encrypt **valid** (legacy origin).  
- www: valid cert issued **2026-08-18** (Beget-side issuance in progress historically; still not WP HTML).  
- WordPress `beget.tech:443`: timeout.  

**Next:** attach domain to WP docroot; re-verify cert + WordPress generator; then HTTPS smoke. No extra HTTPS force in this wave.

---

## 13. Indexing

**LIVE DOMAIN ACTIVE, INDEXING STILL INTENTIONALLY CLOSED**

`blog_public=0`. WP robots `Disallow: /`.

---

## 14. SMTP

Still suppressed (`pre_wp_mail`). Next after SSL + final-domain smoke.

---

## 15. Dashboard

Live domain `shpigovsky.ru`; cutover DONE BY OPERATOR; SSL IN PROGRESS; mail SUPPRESSED; indexing CLOSED; remaining 1–8 as SSL → smoke → redirects → SMTP → forms → robots → sitemaps → crawl. No “manual NS switch pending”.

---

## 16. Source / Production Parity

**7/7 MATCH**

---

## 17. WP Forge Knowledge Feedback

- Boolean unset / false / true — ACF modeling §6.1; AP-020; AP-CMS-016  
- Preview vs autosave vs published — Editor UX §5.1  
- Manual cutover intake — Source/Runtime Authority; AP-019; Launch SOP skip-if-done  

---

## 18. Git

| Item | Value |
|------|--------|
| Commit 1 | `d96dfce1f4d8e8d18ba026809923e1e1dbb067c6` — `FP-0002: intake live domain and fix legal demo state` |
| Commit 2 | `95ade9bd4baa00f22a80c589e43c55d3ed586e8c` — `WP Forge: boolean false-is-a-value and manual cutover intake` |
| Push | `origin/mars/canonical-post-recovery` @ `95ade9bd4baa00f22a80c589e43c55d3ed586e8c` |
| Secret scan | PASS |
| Foreign WIP | untouched (dirty main; isolated worktree from origin) |

---

## 19. Remaining Launch Work

```text
SSL FINALIZE / BIND APEX TO WORDPRESS
→ HTTPS / FINAL-DOMAIN SMOKE
→ HOST/CANONICAL REDIRECTS
→ SMTP
→ FORM DELIVERY QA
→ ROBOTS/INDEXING
→ SITEMAP SUBMISSIONS
→ FINAL CRAWL
```

---

## 20. Acceptance

**FP-0002 P18A COMPLETE (PARTIAL ON PUBLIC ORIGIN) — SHPIGOVSKY.RU ACCEPTED AS CURRENT LIVE PRODUCTION DOMAIN — MANUAL HOME/SITEURL CUTOVER CANONIZED — SSL TRANSITION STATE RECORDED — LEGAL DEMO STATE OWNER FIXED — EXPLICIT FALSE NO LONGER FALLS BACK TO DEMO DEFAULT — LEGAL PAGES RESPECT ADMIN STATE — INDEXING REMAINS CLOSED — MARS/WP FORGE BRAIN UPDATED FOR CURRENT PRODUCTION REALITY**

MARS no longer waits on NS or WordPress URL cutover. Remaining domain-side work is **public origin bind + SSL finalization + post-SSL verification**. Legal DEMO is one explicit boolean owner.
