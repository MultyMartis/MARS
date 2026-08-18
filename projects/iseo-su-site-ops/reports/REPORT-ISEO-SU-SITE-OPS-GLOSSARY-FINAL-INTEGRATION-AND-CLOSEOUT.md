# REPORT — ISEO-SU SITE OPS GLOSSARY FINAL INTEGRATION AND CLOSEOUT

**Programme:** ISEO-SU-SITE-OPS  
**Task ID:** ISEO-SU-SITE-OPS-GLOSSARY-FINAL-INTEGRATION-AND-CLOSEOUT  
**Date:** 2026-08-18  
**Final status:** **COMPLETE — GLOSSARY FINAL INTEGRATION COMPLETE / PRODUCTION BASELINE FROZEN**

---

## 1. Execution Summary

Completed bounded glossary closeout: promoted operator manual production CSS into canonical MARS source; added **Глоссарий** to the shared desktop services submenu immediately after **Калькулятор SEO (free)**; removed unwanted **Архив** prefix from the glossary archive Yoast/HTML title; validated archive/singles/navigation/regression; froze final production baseline. No article body changes, no redesign, no new glossary content phase.

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `AI WS` (X:) |
| Branch | `mars/canonical-post-recovery` |
| HEAD (start) | `f8126b0353cc8378315cf389ea32bbc66127c62d` |
| origin/mars/canonical-post-recovery | `e49af6317b961a008df26e4a31c4e7ada8a4f013` |
| Unpushed commits | present (pre-existing) |
| Staged index | **not empty** — foreign `client-ops-reporting-bridge` WIP preserved; excluded from this commit |
| Foreign WIP | preserved |

## 3. Backup State

| Layer | Evidence |
|-------|----------|
| Full hosting | Operator confirmed existing full backup for this work sequence; agent did not open Beget |
| Scoped remote backups | `.bak-glossary-final-20260818T070304Z` for `content-topbar.php`, `glossary-cpt.php` |
| Local rollback copies | `_glossary-scratch/final-integration/rollback-20260818T070304Z/` |
| DB backup | **not taken** — no database write |

## 4. Manual CSS Reality

| Field | Value |
|-------|-------|
| Changed production file | **`css/main.css` only** |
| Production mtime | **2026-08-18T06:47:41Z** (after hero deploy `20260818T062716Z`) |
| Production SHA-256 | `8e1774ba8996ed3f8be33c6c9750c5db2db4752ff9c93bb54a46b0a5860f2580` |
| Prior MARS snapshot | `_glossary-scratch/layout-fix/prod-css__main.css` (`1424631c…`) |
| Scope | glossary breadcrumbs/search label/hero span tone + shared list spacing split |
| `media.css` / `style.css` | unchanged vs prior snapshots |

## 5. CSS Promotion

Promoted exact production bytes to:

`projects/iseo-su-site-ops/production-source/css/main.css`

Post-promotion canonical SHA-256 **matches live production**. Production CSS was **not** re-deployed.

Evidence: `ISEO-SU-GLOSSARY-MANUAL-CSS-PROMOTION-EVIDENCE-v1.md`

## 6. Main Menu Source

| Field | Value |
|-------|-------|
| Authority | `wp-content/themes/iseoblog/template-parts/content-topbar.php` |
| Consumption | WP `header.php` + static marketing HTML PHP includes (e.g. `services.html`) |
| Pattern | hardcoded `sub_menu__title` links inside services dropdown |
| Mobile | separate `content-mobilemenu.php` tree (unchanged; no calculator/glossary titles pre-existing) |

## 7. Main Menu Change

Inserted immediately after calculator line:

```html
<a href="/glossary/" class="sub_menu__title">Глоссарий</a>
```

Package mirror: `wordpress/iseoblog-glossary/template-parts/content-topbar.php`

Validated on `/`, `/services.html`, `/glossary/`, representative singles — calculator unchanged; glossary present once; adjacent order correct; href `/glossary/`.

## 8. Glossary Archive Title Root Cause

| Layer | Before |
|-------|--------|
| Yoast HTML `<title>` | `Архив Глоссарий - INTLSEO Studio` |
| Yoast `og:title` | same |
| Schema `CollectionPage.name` | same |
| H1 (unaffected) | `Глоссарий` |

**Cause:** Yoast SEO default CPT archive title template prepends Russian archive prefix **Архив** to post-type archive label **Глоссарий**. Not from theme H1 or CPT registration alone.

## 9. Archive Title Fix

Added glossary-archive-only filters in `inc/glossary-cpt.php`:

- `wpseo_title`, `wpseo_opengraph_title`, `wpseo_twitter_title`
- `wpseo_schema_webpage` name alignment
- `document_title_parts` fallback

**After:** `Глоссарий - INTLSEO Studio` (HTML, OG, schema). Blog title control unchanged (`Блог - INTLSEO Studio`).

## 10. Single Title Regression

| URL | Title basis | `Архив` |
|-----|-------------|---------|
| `/glossary/nofollow` | Nofollow | absent |
| `/glossary/geo` | GEO | absent |
| `/glossary/e-e-a-t` | E-E-A-T | absent |
| `/glossary/core-web-vitals` | Core Web Vitals | absent |
| `/glossary/kanonicheskij-url` | Канонический URL | absent |

Canonical URLs and indexable robots unchanged.

## 11. Production Deployment

SFTP stamp **`20260818T070304Z`**

| File | Action |
|------|--------|
| `template-parts/content-topbar.php` | upload |
| `inc/glossary-cpt.php` | upload |
| `css/main.css` | **not uploaded** (production already operator authority) |

Receipt: `_glossary-scratch/final-integration/deploy-final-receipt.json`

## 12. Glossary Validation

| Check | Result |
|-------|--------|
| `/glossary/` HTTP | 200 |
| Archive title | `Глоссарий - INTLSEO Studio` |
| H1 | `Глоссарий` |
| Hero / CTA | `Подробнее` → `#SecondScreen`; rates absent |
| Listing term links | **184** |
| Related terms | present on probed singles |
| Yoast glossary sitemap child | **184** URLs |
| Non-public negatives | Sandbox/SSL id probes not exposed |

Receipt: `_glossary-scratch/final-integration/validate-final.json`

## 13. Menu Validation

| Surface | Result |
|---------|--------|
| Desktop header (home/services/glossary/single) | calculator + glossary adjacent; glossary href `/glossary/` |
| Desktop glossary href in DOM | verified |
| Mobile offcanvas | unchanged separate nav (no glossary/calc titles — pre-existing pattern) |
| Click path | desktop validates href; mobile offcanvas not modified by charter |

Playwright: `_glossary-scratch/final-integration/playwright-final.json`

## 14. Site Regression

Bounded routes `/`, `/services.html`, `/blog/`, `/tariff-calc`, `/offers`, `/privacy-policy.html`, `/glossary/` + representative singles → **HTTP 200**, no PHP fatal, no maintenance mode, menu healthy on probed pages.

## 15. Final Production Baseline

Created: `ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md`

## 16. Files Created or Updated

**Created**

- `production-source/css/main.css`
- `wordpress/iseoblog-glossary/template-parts/content-topbar.php`
- `ISEO-SU-GLOSSARY-FINAL-PRODUCTION-BASELINE-v1.md`
- `ISEO-SU-GLOSSARY-MANUAL-CSS-PROMOTION-EVIDENCE-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-GLOSSARY-FINAL-INTEGRATION-AND-CLOSEOUT.md`

**Updated**

- `wordpress/iseoblog-glossary/inc/glossary-cpt.php`
- `wordpress/iseoblog-glossary/README.md`
- `ISEO-SU-GLOSSARY-TEMPLATE-COMPONENT-MAP-v1.md`
- `ISEO-SU-GLOSSARY-ARCHITECTURE-AND-CONTENT-MODEL-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `OPERATIONAL-INDEX.md`

Scratch/deploy/validation under `_glossary-scratch/final-integration/` = local operational evidence only.

## 17. Production Mutations

Two theme files uploaded (menu + title filters). CSS left as operator production version. No DB, plugin, WP core, article, or `services.html` mutation.

## 18. Rollback

| Target | Restore from |
|--------|--------------|
| Menu | remote `.bak-glossary-final-20260818T070304Z` for `content-topbar.php` |
| Title filters | remote `.bak-glossary-final-20260818T070304Z` for `glossary-cpt.php` |
| CSS | operator/Beget backup of `css/main.css` if ever needed |
| Local rollback | `_glossary-scratch/final-integration/rollback-20260818T070304Z/` |

## 19. Git Persistence

One scoped commit after validation. Subject: `fix(iseo-su): finalize glossary integration and production baseline`. **No push.** Foreign staged WIP excluded via pathspec-only staging.

## 20. Final Decision

Glossary public integration is **closed** for this phase. Production baseline frozen. Optional future work (custom static sitemap glossary inclusion, mobile offcanvas parity) requires separate charter.

## 21. Stop Condition

**COMPLETE — GLOSSARY FINAL INTEGRATION COMPLETE / PRODUCTION BASELINE FROZEN**

No further glossary phase started automatically.

---

*REPORT · 2026-08-18 · production stamp 20260818T070304Z.*
