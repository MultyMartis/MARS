# SITE-002-UNIVERSAL-CORPORATE-CTA-01

**Task:** SITE-002 — UNIVERSAL CORPORATE CTA v2 (M9.14–M9.18)  
**Branch:** `mars/canonical-post-recovery`  
**Live site:** https://zpm.new-site.space  
**Deploy pass:** `site-002-universal-corporate-cta-v2`  
**Timestamp (UTC):** 2026-06-28T20:01:16Z  

## Summary

Внедрена единая система корпоративного CTA **`zpm-corp-cta`** на шести страницах. Компонент визуально повторяет каталожный Commercial Trust (сертификат, 3 benefit-карточки, decor-logo, форма), но использует **отдельные классы и CSS** — `.zpm-commercial-trust` на каталоге не изменён.

OpenCart не поддерживает вложенный `{% include %}` в information-шаблонах (Twig ArrayLoader). CTA встроен inline в каждую страницу из канонических section-артефактов; исходник поддерживается через `build_corpcta_sections.py`.

## Authority preserved

- SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01  
- SITE-002-STABLE-LIVE-LOCAL-FONTS-01  
- SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02  

Не изменялись: Home layout, каталог PLP/PDP, `blockcommercialtrust.twig`, controllers, `main.js`, формы (поля/валидация/JS).

## Git checkpoints

| Step | Commit | Note |
|------|--------|------|
| Pre-implementation | `2ecd27ba` | `checkpoint: pre SITE-002 universal corporate CTA v2` |
| Post-QA | *(this commit)* | Implementation + documentation |

## Backups (FTP + local)

Suffix: `.pre-site-002-corp-cta-v2.bak`  
Directory: `projects/ocpilot/sites/site-002/backups/`

| Remote path | Backup file |
|-------------|-------------|
| `assets/css/style.css` | `style.css.pre-site-002-corp-cta-v2.bak` |
| `catalog/view/theme/default/template/information/about.twig` | `catalog__view__theme__default__template__information__about.twig.pre-site-002-corp-cta-v2.bak` |
| `catalog/view/theme/default/template/information/delivery.twig` | `catalog__view__theme__default__template__information__delivery.twig.pre-site-002-corp-cta-v2.bak` |
| `catalog/view/theme/default/template/information/payment.twig` | `catalog__view__theme__default__template__information__payment.twig.pre-site-002-corp-cta-v2.bak` |
| `catalog/view/theme/default/template/information/guarantee.twig` | `catalog__view__theme__default__template__information__guarantee.twig.pre-site-002-corp-cta-v2.bak` |
| `catalog/view/theme/default/template/information/dealers.twig` | `catalog__view__theme__default__template__information__dealers.twig.pre-site-002-corp-cta-v2.bak` |
| `catalog/view/theme/default/template/information/custom_equipment.twig` | `catalog__view__theme__default__template__information__custom_equipment.twig.pre-site-002-corp-cta-v2.bak` |
| Section partials (new) | `catalog__view__theme__default__template__sections__*.pre-site-002-corp-cta-v2.bak` |

## SHA256 (pre → post)

See `projects/ocpilot/sites/site-002/reports/corp-cta-v2-work/deploy-sha256.json`.

Key page hashes (final deploy):

| File | pre | post |
|------|-----|------|
| about.twig | `2e1fdf5d…` | `427772de…` |
| delivery.twig | `6db8da22…` | `dd966884…` |
| payment.twig | `d878062c…` | `1e507319…` |
| guarantee.twig | `cc9dd986…` | `e353f274…` |
| dealers.twig | `ecc6dc8b…` | `873f6f9e…` |
| custom_equipment.twig | `59fcaca9…` | `19848c87…` |
| style.css | `5069589f…` | `5069589f…` *(CSS block appended on first pass; unchanged on final pass)* |

## Deploy manifest

- `projects/ocpilot/sites/site-002/reports/corp-cta-v2-work/preflight-manifest.json`
- `projects/ocpilot/sites/site-002/reports/corp-cta-v2-work/deploy-manifest.json`
- `projects/ocpilot/sites/site-002/reports/corp-cta-v2-work/deploy-sha256.json`

Deploy scripts:

- `site-002-corp-cta-v2-deploy.py` — backup, patch, upload, QA
- `site-002-corp-cta-v2-restore.py` — emergency rollback of 6 page twigs
- `build_corpcta_sections.py` — generates full section HTML per page

## Component architecture

| Layer | Path / class | Role |
|-------|----------------|------|
| Shell reference | `sections/blockcorporatecta.twig` | Parametric shell (documentation / future controller use) |
| Page sections | `sections/corpcta-{page}.twig` | Full self-contained CTA block per page |
| Form partials | `sections/corpcta-form-{page}.twig` | Form fields only (source for builder) |
| Built sections | `corp-cta-v2-work/corpcta-section-*.twig` | Generated inline HTML spliced into pages |
| CSS | `zpm-corp-cta.css` → appended to `assets/css/style.css` | Independent styles, project tokens only |

## Changed files (live)

**Pages (CTA block only):**

- `catalog/view/theme/default/template/information/about.twig`
- `catalog/view/theme/default/template/information/delivery.twig`
- `catalog/view/theme/default/template/information/payment.twig`
- `catalog/view/theme/default/template/information/guarantee.twig`
- `catalog/view/theme/default/template/information/dealers.twig`
- `catalog/view/theme/default/template/information/custom_equipment.twig`

**New sections:**

- `catalog/view/theme/default/template/sections/blockcorporatecta.twig`
- `catalog/view/theme/default/template/sections/corpcta-*.twig` (6 pages)
- `catalog/view/theme/default/template/sections/corpcta-form-*.twig` (6 forms)

**CSS:**

- `assets/css/style.css` — block `SITE-002 — Universal Corporate CTA v2 (zpm-corp-cta)`

## Rollback

1. Run `python projects/ocpilot/sites/site-002/reports/corp-cta-v2-work/site-002-corp-cta-v2-restore.py` (pages only).  
2. Restore `style.css` from `backups/style.css.pre-site-002-corp-cta-v2.bak` via FTP.  
3. Delete new `sections/corpcta-*` and `blockcorporatecta.twig` from remote if required.  
4. Clear Twig cache (`system/storage/cache/template`).

Or restore all files from `.pre-site-002-corp-cta-v2.bak` backups manually.

## QA (2026-06-28)

| Page | URL | HTTP | zpm-corp-cta | cert | benefits×3 | form | decor | old CTA removed |
|------|-----|------|--------------|------|------------|------|-------|-----------------|
| About | /about | 200 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Delivery | /delivery | 200 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Payment | /payment-methods | 200 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Warranty | /guarantee | 200 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Dealers | /dealers | 200 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Custom | /custom-equipment | 200 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Additional checks:

- Home: `zpm-corp-cta` absent; Home Commercial Trust present — **OK**
- PLP sample (`/nejtralnoe-oborudovanie/stoly/`): `zpm-corp-cta` absent; `zpm-commercial-trust` present — **OK**
- Delivery FAQ accordion (`data-accordion-button`) still present — **OK**
- Forms: existing field names, `data-mask="phone"`, `data-validate="email"`, page-specific submit labels preserved

**qa_all_pass:** `true` (see deploy-manifest.json)

## Incident note (resolved)

First deploy attempt used broken regex `{#.*?CTA` with DOTALL — it matched from `{# §01` through first `CTA` in §06 and wiped page bodies. **Immediately rolled back** from backups; patch logic replaced with page-specific markers + size guard; OpenCart include replaced with inline section HTML.

## Stable checkpoint

**SITE-002-STABLE-LIVE-UNIVERSAL-CORPORATE-CTA-01** — post-QA commit on `mars/canonical-post-recovery`.

## UNKNOWN

- Tablet/mobile visual sign-off (automated QA is HTTP/markup only; no screenshot diff in this pass).
- Console JS errors on live (not probed in this pass; forms reuse existing `main.js` hooks).

## SECURITY RISK

Deploy scripts contain live FTP credentials (existing SITE-002 pattern). Treat `*-deploy.py` as sensitive; do not publish credentials.
