# ISEO-SU GLOSSARY FINAL PRODUCTION BASELINE v1

**Programme:** ISEO-SU-SITE-OPS  
**Date frozen:** 2026-08-18  
**Status:** **PUBLIC GLOSSARY FINAL INTEGRATION COMPLETE / PRODUCTION BASELINE FROZEN**

Primary baseline for future glossary work. Supersedes ad-hoc “next steps” menu/title notes in OPERATIONAL-INDEX for glossary navigation/SEO title scope.

---

## 1. Status

| Field | Value |
|-------|-------|
| Public launch | **2026-07-26** controlled publication |
| Hero alignment | **2026-08-18** services `page_scene` (`f8126b03`) |
| Manual CSS promoted | **2026-08-18** (`production-source/css/main.css`) |
| Main menu link | **2026-08-18** desktop services submenu |
| Archive SEO title fix | **2026-08-18** glossary-archive-only Yoast filters |
| Final integration stamp | `20260818T070304Z` |

## 2. Public Routes

| Route | HTTP | Notes |
|-------|------|-------|
| `/glossary/` | 200 | public archive |
| `/glossary/{slug}/` | 200 | published eligible singles only |
| Non-eligible drafts/MERGED/DEFERRED/EXCLUDED | 404 / not exposed | unchanged |

## 3. Published Corpus

| Bucket | Count |
|--------|------:|
| Published eligible canonical articles | **184** |
| Archive unique term links (listing `<main>`) | **184** |

Authority: `ISEO-SU-GLOSSARY-PUBLICATION-LAUNCH-MANIFEST-v1.md`, launch CSV.

## 4. Non-Public Corpus

| Disposition | Count | Public exposure |
|-------------|------:|-----------------|
| MERGED | 30 | none |
| DEFERRED | 14 | none |
| EXCLUDED | 13 | none |
| **Total non-eligible drafts** | **57** | none |

Negative probes (Sandbox id 2669, SSL id 2674): not exposed as term pages.

## 5. Archive

- H1: **Глоссарий**
- Hero: services-derived `page_scene`; **no** `.page_scene__rates`
- Archive description: exact operator sentence in hero `span` (once)
- Search: `?glossary_q=` server-side filter
- Alphabet nav + letter groups unchanged
- Listing query: `iseo_glossary_get_archive_posts()`

## 6. Single Template

- Hero: same services `page_scene`; **no** hero description `span`
- H1: canonical term title
- Article body unchanged by this closeout task
- Synonyms block when filled
- Related terms: published eligible targets only
- Back link to archive

## 7. Hero

Shared helper: `template-parts/content-glossary-page-scene.php`  
Decorative asset: `/img/services_title_img.svg`  
CTA: **`Подробнее`** → `#SecondScreen` (no `modalbox`)

## 8. CTA / SecondScreen

- Exactly one `#SecondScreen` on `<main>`
- Yellow CTA + `see_more_btn` smooth scroll (inline script on `iseoblog-common`; `common.js` unchanged)
- Validated desktop/mobile scroll on archive + representative singles

## 9. Manual CSS Promoted

| File | Canonical path | Production SHA-256 |
|------|----------------|--------------------|
| Shared marketing CSS | `production-source/css/main.css` | `8e1774ba8996ed3f8be33c6c9750c5db2db4752ff9c93bb54a46b0a5860f2580` |

Evidence: `ISEO-SU-GLOSSARY-MANUAL-CSS-PROMOTION-EVIDENCE-v1.md`

Key glossary-facing selectors: `.glossary-template-default .breadcrumbs`, `.post-type-archive-glossary #SecondScreen … label`, `.info_span`, split `main .content` list margins.

## 10. Main Menu Integration

| Field | Value |
|-------|-------|
| Source | `wp-content/themes/iseoblog/template-parts/content-topbar.php` |
| Also consumed by | static marketing HTML via PHP include (`services.html`, etc.) |
| Item | `<a href="/glossary/" class="sub_menu__title">Глоссарий</a>` |
| Placement | immediately after `Калькулятор SEO (free)` |
| Mobile offcanvas | **unchanged** (`content-mobilemenu.php` — separate tree; no calculator/glossary titles there pre-existing) |

Package mirror: `wordpress/iseoblog-glossary/template-parts/content-topbar.php`

## 11. SEO Title

| Surface | Title |
|---------|-------|
| Glossary archive HTML/Yoast/OG | **Глоссарий - INTLSEO Studio** |
| Prior unwanted form | ~~Архив Глоссарий - INTLSEO Studio~~ |
| Mechanism | glossary-archive-only filters in `inc/glossary-cpt.php` (`wpseo_*`, `document_title_parts`, schema webpage name) |
| Singles | unchanged canonical Yoast titles (e.g. Nofollow, GEO, E-E-A-T, Core Web Vitals, Канонический URL) |
| Blog archive control | **Блог - INTLSEO Studio** unchanged |

## 12. Related Terms

Live on singles via `iseo_glossary_get_related_public_links()` — links only to **published eligible** targets; no MERGED/DEFERRED/EXCLUDED leakage.

## 13. Sitemap

| Source | Count | Notes |
|--------|------:|-------|
| `wp-sitemap-posts-glossary-1.xml` | **184** | authoritative Yoast/WP sitemap child |
| Custom `sitemap.xml` (robots primary index) | unchanged | no glossary URLs by design at launch |

## 14. Navigation

Desktop header/services dropdown includes **Глоссарий** after calculator on WP routes and static marketing pages sharing `content-topbar.php`. Glossary pages use same chrome.

## 15. Protected Boundaries

Do **not** without new charter:

- publish non-eligible terms
- mutate 184 article bodies
- redesign glossary hero/templates
- overwrite production `css/main.css` from stale automation
- add glossary to mobile offcanvas without explicit mobile-nav charter
- rewrite global Yoast title system

See `ISEO-SU-PROTECTED-ZONES-v1.md`.

## 16. Future Editing Rules

1. **Manual production CSS/theme edits** must be reconciled runtime→source before later automation overwrites (`production-source/` for shared CSS; `wordpress/iseoblog-glossary/` for theme package).
2. Glossary visual tweaks prefer bounded edits to `production-source/css/main.css` with forensic diff evidence — not full-file replace from old snapshots.
3. Menu changes require `content-topbar.php` (global chrome); remember static HTML includes the same part.
4. Archive title prefix removal is implemented in `glossary-cpt.php` — do not global-strip `Архив` for other post types.
5. Next optional work (out of scope for this baseline): custom `sitemap.xml` glossary discovery, mobile offcanvas parity, MERGED alias polish.

---

*Glossary final production baseline v1 · frozen 2026-08-18.*
