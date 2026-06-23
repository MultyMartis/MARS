# FP-0002 V6 YOGA/BOS AND FINAL FORM CORRECTIONS REVIEW

**Date:** 2026-06-23  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6`  
**Branch:** `mars/post-cycle8-live-tests`

## Operator source protection

| File | Diff after a404dcb | Operator-authored | Preserve | Allowed edit |
| ---- | ------------------ | ----------------: | -------: | -----------: |
| `src/js/main.js` | Specialists Swiper breakpoints | YES | YES | YES (final-form scope only) |
| `src/partials/sections/home-comfort.html` | Logo decor + gallery trim | YES | YES | NO |
| `src/partials/sections/home-rehabilitation-program.html` | Direction img/wrapper layout | YES | YES | NO |
| `src/scss/style.scss` | Program/comfort/FAQ spacing | YES | YES | YES (scoped final-form + articles alt only) |
| `src/partials/sections/home-articles.html` | NONE at checkpoint | NO | YES | YES (yoga/BOS alt only) |
| `src/partials/sections/home-final-form.html` | NONE at checkpoint | NO | YES | YES |

**Operator values overwritten:** 0 in frozen blocks.

## Operator checkpoint

| Field | Value |
| ----- | ----- |
| Commit | `5011969` |
| Message | `chore(fp-0002): checkpoint latest operator home polish` |
| Push | SUCCESS (`mars/post-cycle8-live-tests`) |
| Files | `main.js`, `home-comfort.html`, `home-rehabilitation-program.html`, `style.scss` |

## Yoga Figma image

| Field | Value |
| ----- | ----- |
| Page | Home canvas — frame `1:1268` «Статьи» |
| Frame | `1:1280` INSTANCE «Статья» (column 2) |
| Node name | `Статья` (image override on component child `165:1041`) |
| Node ID | `1:1280` |
| Image-fill hash | `2a1c33e99775c186541c8d81d3d8bec41973239c` |
| Native dimensions | 1920×1280 |
| Asset path | `src/img/content/home-articles/article-yoga-therapy.webp` |
| SHA-256 | `cd45890292f951654bd829202fb3ecf758117e3c96f810091f18c3c4d996c86d` |
| White margins | ZERO |
| HTML partial | `src/partials/sections/home-articles.html` (card 2) |
| Exact title | Йога в терапии: снятие абстинентного синдрома, снижение кортизола |

## BOS Figma image

| Field | Value |
| ----- | ----- |
| Page | Home canvas — frame `1:1268` «Статьи» |
| Frame | `1:1281` INSTANCE «Статья» (column 3) |
| Node name | `Статья` (image override on component child `165:1041`) |
| Node ID | `1:1281` |
| Image-fill hash | `4e1d0887e79c3d8aec97e6a90a7cfa54a7dbd725` |
| Native dimensions | 2048×1365 |
| Asset path | `src/img/content/home-articles/article-bos-therapy.webp` |
| SHA-256 | `63492634ed32e5dc8f56f8d3eeee0577abe7bf167d0d73038b0d531db9fb68e1` |
| White margins | ZERO |
| HTML partial | `src/partials/sections/home-articles.html` (card 3) |
| Exact title | БОС-терапия: тренировка конкретных зон мозга с помощью технологий |

## Triumph consent source

| Field | Value |
| ----- | ----- |
| Authority map | `projects/triumph-manipulator-landing/frontend-workspace.md` → active rollout `workspaces/triumph-manipulator-landing-v6/` |
| Triumph source file | `workspaces/triumph-manipulator-landing-v6/src/partials/sections/v5-ppc/zakaz/final-contact-cta.html` |
| Legacy `triumph-manipulator-landing/` | NO consent checkbox — not used |
| Checkbox structure | `<label>` wrapping hidden checkbox + visual control + text with two legal links |
| Required | `required` on checkbox |
| JS validation | Native `required` only (no Triumph `data-validate` chain) |
| CSS classes adapted | `.home-final-form__consent*` (not Triumph `site-form__*`) |

## Exact consent text

Я даю согласие на обработку персональных данных в соответствии с Согласием на обработку персональных данных и соглашаюсь с Политикой конфиденциальности.

(HTML uses `&nbsp;` and non-breaking spaces per project law.)

## Privacy link resolution

| Field | Value |
| ----- | ----- |
| Triumph consent URL | `/consent-personal-data/` |
| Triumph privacy URL | `/privacy-policy/` |
| FP-0002 privacy URL used | `/consent-personal-data/` and `/privacy-policy/` (same paths; present in `src/partials/layout/footer.html`) |
| URL substitution | NONE |

## Final form field correction

| Field | Value |
| ----- | ----- |
| Partial | `src/partials/sections/home-final-form.html` |
| Fields before | name, phone, email, message, static consent paragraph |
| Fields after | name, phone, message, required consent checkbox, submit |
| Email removed | YES (HTML) |
| Email JS removed | YES |
| Desktop primary row | name + phone (`home-final-form__row`, 2 columns ≥1025) |
| Mobile stack | single column ≤1024 |
| Submit text | Записаться на консультацию |
| Submit classes | `btn btn_dark btn--primary` |
| `novalidate` removed | YES (native validation enabled) |

## Email removal

Removed from HTML, layout grids, and `initHomeFinalForm()` email selectors/validators.

## Desktop two-column layout

`home-final-form__row` → `grid-template-columns: repeat(2, minmax(0, 1fr))` on desktop.

## Mobile layout

`home-final-form__row` → single column at ≤1024 via existing responsive block.

## Final form Figma background

| Field | Value |
| ----- | ----- |
| Page | Home canvas |
| Frame | `1:1295` «Консультация» |
| Background node | `1:1295` (IMAGE fill layer on frame) |
| Node ID | `1:1295` |
| Image-fill hash | `e4f40bb169a20b7239113b6f0154ecdf4769b142` |
| Native dimensions | 1957×1113 |
| Fill mode | IMAGE `FILL` at 10% opacity over solid `#475371` token |
| Export path | `src/img/content/home-final-form/home-final-form-background.webp` |
| CSS owner | `.home-final-form__band::before` |
| Overlay/fallback | `background-color: var(--color-text-primary)` + `opacity: 0.1` on decorative layer |
| White margins | ZERO |

## Inputmask

| Field | Value |
| ----- | ----- |
| Hook | `data-phone-input` |
| Duplicate guard | `!phoneInput.inputmask` |
| Mask | `+7 999 999 - 99 - 99` |

## Native consent validation

Checkbox `required`; form without `novalidate`; `:focus-visible` on control box; label clickable; links remain tabbable inside label.

## Backend boundary

`action="#"` retained; `preventDefault` on submit; no fake success message; backend NOT_CONNECTED.

## Responsive results

| Width | Overflow |
| ----- | -------- |
| 320 | 0 |
| 375 | 0 |
| 390 | 0 |
| 430 | 0 |
| 768 | 0 |
| 1024 | 0 |
| 1025 | 0 |
| 1398 | 0 |

Evidence: `reviews/main-content/final-corrections/RESPONSIVE-OVERFLOW-CHECK.json`

## Regressions

| Check | Result |
| ----- | ------ |
| Previous sections | NONE |
| Swiper (3 instances) | NONE |
| Fancybox comfort group | ACTIVE |
| Footer | NONE |
| Font/FOUT | NONE |

## Build result

**Build succeeded** (`npm run build`, 2026-06-23).

Validation: `reviews/main-content/final-corrections/BUILD-VALIDATION.json`

## Screenshots

`reviews/main-content/final-corrections/`

- `YOGA-BOS-IMAGES-DESKTOP.png`
- `YOGA-BOS-IMAGES-MOBILE-390.png`
- `FINAL-FORM-DESKTOP.png`
- `FINAL-FORM-MOBILE-390.png`
- `FINAL-FORM-CONSENT-FOCUS.png`
- `FINAL-FORM-BACKGROUND-COMPARISON.png`
- `FULL-HOME-AFTER-FINAL-CORRECTIONS.png`

## Remaining unknowns

NONE for this correction scope.

## Final verdict

**IMPLEMENTED_PENDING_OPERATOR_REVIEW** — exact Figma exports installed; Triumph v6 consent contract applied with FP-0002 legal paths; operator canonical blocks preserved.
