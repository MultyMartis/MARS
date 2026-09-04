# ISEO-SU-WEBINAR-LANDING-REBUILD-01 — Evidence v1

**Task:** `ISEO-SU-SITE-OPS-WEBINAR-LANDING-REBUILD-01`  
**Date:** 2026-09-04  
**FINAL STATUS:** COMPLETE — WEBINAR LANDING REBUILT ON EXISTING I-SEO SITE DESIGN / CUSTOM DESIGN REMOVED / RSYA READY

Supersedes visual implementation of **WEBINAR-LANDING-01** (historical evidence retained).

---

## 1. Operator decision

Live custom webinar design at `https://i-seo.su/webinar-seo-podryadchik.html` was **REJECTED VISUALLY**.

Do not iterate on rejected custom layout. Rebuild inside existing i-seo.su design system.

## 2. Source page selection

| Field | Value |
|-------|--------|
| **SOURCE PAGE** | `https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html` |
| **SOURCE FILE** | `production-source/static-html/services/seo/prodvizhenie-sajta-restorana.html` |
| **WHY SELECTED** | Modern niche SEO landing with current INTLSEO header/topbar, `body.new-seo-landing-flex-first-screen` (safe `height:auto; min-height:100vh`), `content_block` rhythm, `uni_check_list`, standard `free_audit` form, standard footer/popups/shared CSS/JS. Listed candidates (`seo.html`, `b-regionakh`, `zarubezhnye`, `prodvizhenie-avtomobilnogo-sajta`) lack the current flex-first-screen safe hero pattern. |

**SOURCE PAGE DESIGN PRESERVED:** YES

## 3. Backup

| Field | Value |
|-------|--------|
| Path | `X:\AI MARS\local\sites\iseo-su-production\_webinar-landing-rebuild-01\` |
| Manifest | `BACKUP-MANIFEST.json` |
| Timestamp | `2026-09-04T14:05:55+07:00` |
| Rejected HTML SHA256 | `f3aa41c20ba8737db91d526a7133eb36579659ed90feb3194fc057cd4d15344b` (46960 bytes) |
| Rejected CSS SHA256 | `346984b33384f7324de5eca55feaff44dc7fef1b5c9edc7bffed6afd2a13c79c` (11337 bytes) |

## 4. Implementation

| Path | Role |
|------|------|
| `production-source/static-html/webinar-seo-podryadchik.html` | Rebuilt page (shared site chrome + webinar content) |
| `production-source/css/webinar-seo-podryadchik.css` | Tiny page-scoped overrides only (~85 lines / 2052 bytes) |

**CURRENT CUSTOM DESIGN REMOVED:** YES  
**LARGE CUSTOM WEBINAR CSS REMAINS:** NO (threshold >120 lines; actual 85)

Page-scoped CSS rules (why each needed):

1. `.webinar-eyebrow` — yellow «Вебинар» accent inside existing hero typography  
2. `.page_scene__info_wrap` / img sizing — Nikita visual presence (not tiny)  
3. `.webinar-facts-grid` — flex layout for existing `.achievement_block` without carousel  
4. Mobile `@media` — override shared `media.css` hiding `.page_scene__info` so Nikita remains visible  

## 5. Structure (final)

1. Standard site header (`content-mobilemenu.php`, `content-topbar.php`)  
2. Customized webinar hero inside `page_scene`  
3. О вебинаре  
4. На вебинаре разберем  
5. После вебинара вы сможете  
6. Детали вебинара (facts)  
7. Standard `free_audit` form (heading/copy adapted)  
8. Standard site footer  

## 6. Meta / SEO

| Field | Value |
|-------|--------|
| Title | Вебинар «Как выбрать подрядчика в SEO и не ошибиться?» \| INTLSEO |
| Description | Бесплатный вебинар Никиты Швакова… 3 сентября 2026 в 19:00 МСК… |
| H1 | Как выбрать подрядчика в SEO и не ошибиться? |
| Canonical | `https://i-seo.su/webinar-seo-podryadchik.html` |
| Menu | **NO** |
| Sitemap | **NO** |
| Indexability | NORMAL / DIRECT-READY |

## 7. Form / consent / assets

| Field | Value |
|-------|--------|
| Form source | Restaurant niche page `free_audit` / family `page` → `/page__FORM.php` |
| Heading | Записаться на вебинар |
| Consent | `personal_data_consent` |
| Policy | `https://i-seo.su/privacy-policy.html` |
| Recipient | `nikel007i33@yandex.ru` |
| Nikita image | `/img/iSEO_Boss.png` |
| Nikita generated/altered | **NO** |
| Nikita visual size (1920) | ~794×812 CSS px (prominent) |

## 8. Deploy / live validate

Evidence: `evidence/webinar-landing-rebuild-01/deploy-validate.json`

| Check | Result |
|-------|--------|
| HTTP | 200 |
| Needles | PASS |
| Rejected markers absent | PASS |
| Meta | PASS |
| Menu / sitemap | NO / NO |
| Nikita asset HTTP | 200 |
| pass | **true** |

Deployed:

- HTML SHA256 `0755cbc4ff8c1c23eabca441d3ce7997996b286af4a4c53609f8156570938011` (13706 bytes)  
- CSS SHA256 `1ce30046a29535999b73206c0f47aa4eeec09b0f3ec17150f0037ceb347854c8` (2052 bytes)  

## 9. Viewport QA

Evidence dir: `evidence/webinar-landing-rebuild-01/screenshots/20260904T070951Z/`  
JSON: `evidence/webinar-landing-rebuild-01/viewport-qa.json`

| Viewport | Pass |
|----------|------|
| 1920×1080 | PASS |
| 1440×900 | PASS |
| 1366×768 | PASS |
| 1280×720 | PASS |
| 1440×600 | PASS |
| 390×844 | PASS |
| 360×800 | PASS |

LAYOUT OVERLAP: **0**  
BROKEN ASSETS: **0**  
JS ERRORS (page assets): **0**  

Note: Playwright may log HTTP **409** from third-party `https://lpt-crm.online/track` (site-wide CRM tracker). Not a page asset failure; excluded from broken_assets.

Screenshots produced:

1. Source first screen — `source-hero-desktop-1440x900.png` (if present in run dir; else source URL captured in QA JSON)  
2. Rebuilt first screen — viewport desktop shots  
3. Full page — fullpage shots where captured  
4. Mobile hero — `viewport-mobile-390x844.png`  
5. Mobile form/footer — covered in mobile full-page / form visibility checks  

## 10. Hard checks

| Check | Result |
|-------|--------|
| SOURCE PAGE DESIGN PRESERVED | YES |
| CURRENT CUSTOM DESIGN REMOVED | YES |
| LARGE CUSTOM WEBINAR CSS REMAINS | NO |
| HEADER / FOOTER / FORM SOURCE | restaurant niche page pattern |
| HERO / CONTENT / FORM / FOOTER USE EXISTING SITE DESIGN | YES ×4 |
| NIKITA GENERATED/ALTERED | NO |
| DATE / TIME | 3 сентября 2026 / 19:00 МСК |
| CTA / CONSENT | PASS |
| MENU / SITEMAP | NO / NO |
| ALL VIEWPORTS | PASS |
| PRODUCTION/SOURCE ALIGNED | YES |

## 11. Tools

- `tools/_webinar-landing-rebuild-01-deploy-validate.py`
- `tools/_webinar-landing-rebuild-01-screenshots.py`

## 12. Remote sync

| Item | Value |
|------|--------|
| Worktree | `X:\AI MARS STORAGE\git-sync-iseo-su-webinar-rebuild-01\repo` |
| Message | `fix(iseo-su): rebuild webinar landing on existing site template` |
| Force push | **NO** |
| Feature commit | `6db015261bf5a4a6162f233e2ecdcd940693b0bb` |
| Origin tip after FF push | `6db015261bf5a4a6162f233e2ecdcd940693b0bb` |
| REMOTE SYNC | **COMPLETE** |

## 13. Historical supersession

**WEBINAR-LANDING-01** visual/custom design: **SUPERSEDED BY REBUILD 01**.  
Do not erase: `ISEO-SU-WEBINAR-LANDING-01-EVIDENCE-v1.md`, prior REPORT/RU, `evidence/webinar-landing-01/`, backup `_webinar-landing-01/`.
