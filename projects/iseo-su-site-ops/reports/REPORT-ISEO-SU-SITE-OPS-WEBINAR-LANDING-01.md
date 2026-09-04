# REPORT — ISEO-SU-SITE-OPS-WEBINAR-LANDING-01

**Task ID:** `ISEO-SU-SITE-OPS-WEBINAR-LANDING-01`  
**Lane:** ISEO-SU-SITE-OPS — WEBINAR LANDING / RSYA / INTLSEO  
**Date (UTC evidence):** 2026-09-04  
**FINAL STATUS:**  
**COMPLETE — ISEO-SU WEBINAR LANDING LIVE / RSYA READY / INTLSEO / SECURE REGISTRATION FORM**

---

## 1. Summary

Production campaign landing for RSYA traffic for INTLSEO webinar by Nikita Shvakov:

| Field | Value |
|-------|--------|
| Final URL | `https://i-seo.su/webinar-seo-podryadchik.html` |
| Topic | «Как выбрать подрядчика в SEO и не ошибиться?» |
| Date / time | 3 сентября 2026 · 19:00 МСК |
| Participation | бесплатное |
| Nikita asset | `/img/iSEO_Boss.png` (existing site authority; not generated) |
| Form family | `page` → `/page__FORM.php` |
| Consent | client + server (`personal_data_consent`) |
| Recipient | `nikel007i33@yandex.ru` |
| Menu / sitemap | **NO** / **NO** |
| Indexability | NORMAL / DIRECT-READY (no noindex) |

## 2. Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume X: | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Main HEAD vs origin | dirty/divergent (foreign WIP preserved) |
| Sync strategy | clean STORAGE worktree onto `origin/mars/canonical-post-recovery` |

Foreign WIP: preserved. No reset / clean / stash / `git add .` / force push.

## 3. URL decision

Preferred root static URL selected (matches existing campaign/static HTML contour):

`https://i-seo.su/webinar-seo-podryadchik.html`

Not nested under `/services/seo/` (campaign landing, not SEO service page).

## 4. Source mutations

| Path | Action |
|------|--------|
| `production-source/static-html/webinar-seo-podryadchik.html` | CREATE |
| `production-source/css/webinar-seo-podryadchik.css` | CREATE |
| `tools/_webinar-landing-01-backup-deploy-validate.py` | CREATE (helper) |
| `tools/_webinar-landing-01-screenshots.py` | CREATE (helper) |
| `tools/_webinar-landing-01-overflow-debug.py` | CREATE (helper) |
| Evidence / reports / authority docs | CREATE / UPDATE |

Homepage not modified. Sitemap / menu not modified. No new mail handler.

## 5. Hero / branding

- Dark first screen; yellow eyebrow «Вебинар»; white topic H1
- INTLSEO logo `/img/logo-intl.svg`
- Safe first-screen pattern: `body.new-seo-landing-flex-first-screen` + `height:auto; min-height:100vh`
- Spelling: «недобросовестный»
- CTA: «Зарегистрироваться» → `#webinar-register`

## 6. Form / security

| Item | Value |
|------|--------|
| Handler | `/page__FORM.php` (`#page__FORM_seo`) |
| Fields | `pf_name`, `pf_phone`, hidden `pf_contact`, hidden `pf_site=WEBINAR SEO CONTRACTOR 2026-09`, optional `pf_comment` |
| Consent field | `personal_data_consent` (id `personal_data_consent_webinar`) |
| Privacy | `https://i-seo.su/privacy-policy.html` |
| HMAC / honeypot / min-fill / rate / CRLF | preserved via shared architecture |
| Test mode final | **OFF** |

Negative tests (no consent / consent=0 / malformed): **REJECT**, mail **0**.

## 7. Deploy / backup

Backup root: `X:\AI MARS\local\sites\iseo-su-production\_webinar-landing-01\`  
Latest: `backup-20260904T064640Z`  
Scoped upload of HTML + CSS; remote checksums aligned with source.

## 8. Live validation

| Check | Result |
|-------|--------|
| HTTP | **200** |
| Hero direction | PASS |
| Program items | 4/4 |
| After-webinar items | 4/4 |
| CTA | works |
| Consent client/server | YES / YES |
| Broken assets | 0 |
| JS errors (viewport QA) | 0 |

## 9. Viewport QA

Evidence: `evidence/webinar-landing-01/_viewport_qa_latest.json` (`20260904T064652Z`)

| Viewport | Result |
|----------|--------|
| 1920×1080 | PASS |
| 1440×900 | PASS |
| 1366×768 | PASS |
| 1280×720 | PASS |
| 1440×600 | PASS |
| 390×844 | PASS |
| 360×800 | PASS |

LAYOUT OVERLAP: **0**

Screenshots: `evidence/webinar-landing-01/screenshots/20260904T064652Z/`

## 10. Indexability / discovery

| Item | State |
|------|--------|
| Menu entry | **NO** |
| Sitemap entry | **NO** (static sitemap unchanged **139**) |
| robots/noindex | not set |
| Direct/RSYA ready | **YES** |

## 11. Docs updated

- `ISEO-SU-WEBINAR-LANDING-01-EVIDENCE-v1.md`
- `reports/ISEO-SU-WEBINAR-LANDING-01-RU.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-WEBINAR-LANDING-01.md`
- `ISEO-SU-CURRENT-STATE-v1.md`
- `OPERATIONAL-INDEX.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`

## 12. Git Persistence

Main checkout remained dirty/divergent (`HEAD` ≠ origin). Isolated sync used worktree:

`X:\AI MARS STORAGE\git-sync-iseo-su-webinar-landing-01\repo`

Allowlisted paths only. Foreign WIP not staged. No `git add .` / `-A`. No force push.

Feature commit:

`8028ea5df3000686dc91629bf7b02d8c215efe6f` — `feat(iseo-su): add seo contractor webinar landing page`

## 13. Remote Sync

FF push without force onto `origin/mars/canonical-post-recovery` from the isolated worktree:

- Before: `1657c211ad445d11d97aff875e4f0ccdbda57d18`
- Feature tip pushed: `8028ea5df3000686dc91629bf7b02d8c215efe6f`
- `origin/mars/canonical-post-recovery` verified equal to that tip after `git fetch`

REMOTE SYNC: **COMPLETE**

## 14. Stop Condition

Stop after landing creation, deploy, visual validation, form validation, docs and scoped Git sync. Do **not** modify unrelated SEO pages.

---

## HARD CHECK

```
FINAL URL: https://i-seo.su/webinar-seo-podryadchik.html
PAGE CREATED: YES
HTTP: 200

HERO MATCHES APPROVED DIRECTION: YES
NIKITA SOURCE ASSET: /img/iSEO_Boss.png
NIKITA GENERATED/ALTERED: NO
INTLSEO BRANDING: PASS

DATE: 3 сентября 2026
TIME: 19:00 МСК
PARTICIPATION: бесплатное

TITLE: Вебинар «Как выбрать подрядчика в SEO и не ошибиться?» | INTLSEO
DESCRIPTION: Бесплатный вебинар Никиты Швакова о выборе SEO-подрядчика. 3 сентября 2026 в 19:00 МСК. Разберем критерии выбора агентства, риски и реальные результаты SEO.
H1: Как выбрать подрядчика в SEO и не ошибиться?
SELF-CANONICAL: https://i-seo.su/webinar-seo-podryadchik.html

ABOUT COPY EXACT: YES
PROGRAM ITEMS: 4/4
AFTER-WEBINAR ITEMS: 4/4

CTA WORKS: YES
FORM FAMILY: page (/page__FORM.php)
CONSENT CLIENT: YES
CONSENT SERVER: YES
NORMAL RECIPIENT: nikel007i33@yandex.ru
TEST MODE FINAL: OFF

MENU ENTRY: NO
SITEMAP ENTRY: NO
INDEXABILITY: NORMAL / DIRECT-READY

VIEWPORT 1920x1080: PASS
VIEWPORT 1440x900: PASS
VIEWPORT 1366x768: PASS
VIEWPORT 1280x720: PASS
VIEWPORT 1440x600: PASS
MOBILE 390x844: PASS
MOBILE 360x800: PASS

LAYOUT OVERLAP: 0
BROKEN ASSETS: 0
JS ERRORS: 0

PRODUCTION/SOURCE ALIGNED: YES
PROJECT-OWNED UNCOMMITTED: 0 (after Storage sync)
FOREIGN WIP PRESERVED: YES
REMOTE SYNC: COMPLETE (origin tip 8028ea5df3000686dc91629bf7b02d8c215efe6f)

FINAL STATUS:
COMPLETE — ISEO-SU WEBINAR LANDING LIVE / RSYA READY / INTLSEO / SECURE REGISTRATION FORM
```
