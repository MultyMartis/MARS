# ISEO-SU WEBINAR LANDING 01 EVIDENCE v1

**Task:** `ISEO-SU-SITE-OPS-WEBINAR-LANDING-01`  
**Date:** 2026-09-04  
**Site:** `https://i-seo.su/`  
**Decision:** **PASS / COMPLETE — LIVE / RSYA READY / INTLSEO / SECURE REGISTRATION FORM**

---

## 1. Scope

Campaign landing for RSYA / advertising traffic: free webinar by Nikita Shvakov (INTLSEO) on choosing an SEO contractor. Real HTML/CSS page in current i-seo.su contour; not a flattened banner image. No main-menu entry; no static-sitemap add; normal indexability (no noindex).

## 2. Final URL

| Field | Value |
|-------|--------|
| FINAL URL | `https://i-seo.su/webinar-seo-podryadchik.html` |
| Rationale | Root static campaign page (same pattern family as other Direct-ready root landings); preferred over nested `/services/seo/…` because this is ad/RSYA, not a service SEO landing in the hub tree |
| Aliases | **None** |

## 3. Nikita image authority

| Field | Value |
|-------|--------|
| Live / public asset | `https://i-seo.su/img/iSEO_Boss.png` |
| Path | `/img/iSEO_Boss.png` |
| Dimensions | 880×900 |
| Generated / face-altered | **NO** |
| Selection | Existing homepage / site boss portrait closest to webinar reference (Nikita with laptop / dark-friendly composition) |

## 4. Page design / hero

- Dark / black first screen; INTLSEO logo (`/img/logo-intl.svg`); yellow eyebrow «Вебинар»; white H1 topic; thesis list with spelling «недобросовестный»; date/time; free participation; CTA → `#webinar-register`.
- Body classes: `overlay_on new-seo-landing-flex-first-screen webinar-seo-podryadchik`.
- Safe first screen: shared `new-seo-landing-flex-first-screen` (`height:auto; min-height:100vh`).
- Scoped CSS: `css/webinar-seo-podryadchik.css`.
- Includes: `content-footer.php`, `content-seo-popups.php`; `<div class="scroll_to_top"></div>` (required by `common.js`).

## 5. Copy checklist

| Block | Result |
|-------|--------|
| About / intro | Exact operator copy |
| «На вебинаре разберем» | **4/4** |
| «После вебинара вы сможете» | **4/4** |
| Facts: date / time / online / free | Exact |
| DATE | 3 сентября 2026 |
| TIME | 19:00 МСК |
| PARTICIPATION | бесплатное |

## 6. Meta

| Field | Value |
|-------|--------|
| TITLE | Вебинар «Как выбрать подрядчика в SEO и не ошибиться?» \| INTLSEO |
| DESCRIPTION | Бесплатный вебинар Никиты Швакова о выборе SEO-подрядчика. 3 сентября 2026 в 19:00 МСК. Разберем критерии выбора агентства, риски и реальные результаты SEO. |
| H1 | Как выбрать подрядчика в SEO и не ошибиться? |
| Self-canonical | `https://i-seo.su/webinar-seo-podryadchik.html` |
| robots | normal (no noindex) |

## 7. Form / consent / security

| Field | Value |
|-------|--------|
| Form family | **page** → `/page__FORM.php` (`#page__FORM_seo`) |
| Fields | `pf_name`, hidden `pf_contact`, `pf_phone`, hidden `pf_site`=`WEBINAR SEO CONTRACTOR 2026-09`, optional `pf_comment`, `personal_data_consent` |
| Consent client | **YES** (required checkbox → privacy `https://i-seo.su/privacy-policy.html`) |
| Consent server | **YES** (shared guard; negatives REJECT; mail not sent) |
| Normal recipient | `nikel007i33@yandex.ru` only |
| test_mode final | **OFF** |
| New mail handler | **NO** (reuse existing) |

Negative POST results (2026-09-04T064640Z deploy validate): `no_consent`, `consent_0`, `malformed_empty_name` → body `false`, `mail_sent_signal: false`.

## 8. Menu / sitemap / indexability

| Field | Value |
|-------|--------|
| MENU ENTRY | **NO** |
| SITEMAP ENTRY | **NO** (static sitemap remains **139**; not regenerated) |
| INDEXABILITY | **NORMAL / DIRECT-READY** |

## 9. Assets / JS stack

- CSS: `normalize.css`, owl + fancybox CSS, `main.css`, `media.css`, `new-seo-landing-flex-first-screen.css`, `webinar-seo-podryadchik.css`
- JS: jQuery 3.7.1, owl, fancybox, jquery.mask CDN, `common.js`
- Do **not** use `/js/libs.min.js` or `/css/libs.min.css` (live 404)

## 10. Backup

`X:\AI MARS\local\sites\iseo-su-production\_webinar-landing-01\`  
Latest stamp: `backup-20260904T064640Z` (CREATE page + CSS before/after copies).

## 11. Deploy

SFTP scoped upload: root `webinar-seo-podryadchik.html` + `css/webinar-seo-podryadchik.css`. Remote checksums matched. HTTP **200**.

## 12. Viewport QA

Evidence dir: `evidence/webinar-landing-01/screenshots/20260904T064652Z/`  
JSON: `evidence/webinar-landing-01/_viewport_qa_latest.json`

| Viewport | Result |
|----------|--------|
| 1920×1080 | PASS |
| 1440×900 | PASS |
| 1366×768 | PASS |
| 1280×720 | PASS |
| 1440×600 | PASS |
| 390×844 | PASS |
| 360×800 | PASS |

LAYOUT OVERLAP: **0** · JS ERRORS: **0** · BROKEN ASSETS signal: **0** · horizontal scroll: none

## 13. Source SHA256 (canonical MARS)

| File | SHA256 |
|------|--------|
| `production-source/static-html/webinar-seo-podryadchik.html` | `573AC03EAC6646A201BFC459202A44015C4756100329DA1C5B8EBA493AD8937B` |
| `production-source/css/webinar-seo-podryadchik.css` | `346984B33384F7324DE5ECA55FEAFF44DC7FEF1B5C9EDC7BFFED6AFD2A13C79C` |

## 14. Tools

- `tools/_webinar-landing-01-backup-deploy-validate.py`
- `tools/_webinar-landing-01-screenshots.py`
- `tools/_webinar-landing-01-overflow-debug.py`

## 15. Production / source / WIP

PRODUCTION/SOURCE ALIGNED: **YES**  
PROJECT-OWNED UNCOMMITTED (after Storage sync): **0** for this allowlist  
FOREIGN WIP PRESERVED: **YES**

## 16. Remote sync

| Item | Value |
|------|--------|
| Worktree | `X:\AI MARS STORAGE\git-sync-iseo-su-webinar-landing-01\repo` |
| Feature commit | `8028ea5df3000686dc91629bf7b02d8c215efe6f` |
| Message | `feat(iseo-su): add seo contractor webinar landing page` |
| FF push | `1657c211` → `8028ea5d` on `origin/mars/canonical-post-recovery` |
| Force push | **NO** |
| REMOTE SYNC | **COMPLETE** |
