# FP-0002 V6 PRE MODALS OPERATOR STABLE 01 — Release Manifest

**Release ID:** `FP-0002-V6-PRE-MODALS-OPERATOR-STABLE-01`  
**Date:** 2026-06-23  
**Branch:** `mars/post-cycle8-live-tests`  
**Base commit:** `5dd483a` (operator delta uncommitted at freeze start)  
**Authority:** operator manual HTML/SCSS after checkpoint `5dd483a`

## Source authority

| Field | Value |
|-------|-------|
| Current src | **OPERATOR CANONICAL** |
| Full home page | **PRESENT** |
| Current manual HTML/SCSS/JS | **FROZEN** |
| Gallery Swiper | **ACTIVE** |
| Reviews Swiper | **ACTIVE** |
| Specialists Swiper | **ACTIVE** |
| Comfort Fancybox | **ACTIVE** |
| Final form | **PRESENT** |
| Final form backend | **NOT CONNECTED** |
| Modal system | **NOT STARTED** |
| Modal forms | **NOT STARTED** |
| Modal triggers | **NOT CONNECTED** |
| Triumph form logic port | **NOT STARTED** |

## Operator-authored delta (vs `5dd483a`)

| File | Diff after last FP-0002 commit | Operator-authored | Preserve | Include in freeze |
| ---- | ------------------------------ | ----------------: | -------: | ----------------: |
| `src/scss/style.scss` | CTA band background overlay (+31 lines) | YES | YES | YES |
| `src/img/content/home-articles/article-bos-therapy.webp` | Re-exported asset (binary) | YES | YES | YES |
| `src/img/content/home-articles/article-yoga-therapy.webp` | Re-exported asset (binary) | YES | YES | YES |

## Build validation snapshot (pre-freeze)

| Check | Result |
|-------|--------|
| Project SCSS files | 1 |
| Main JS entry | `src/js/main.js` |
| Google Fonts in active src | 0 |
| External Inter in active src | 0 |
| `data-safe-unknown` | 0 |
| Legacy radius tokens | 0 |
| Gallery Swiper instances | 1 |
| Reviews Swiper instances | 1 |
| Specialists Swiper instances | 1 |
| Total Swiper instances | 3 |
| Comfort Fancybox | ACTIVE |
| Final form name fields | 1 |
| Final form phone fields | 1 |
| Final form email fields | 0 |
| Final form message fields | 1 |
| Final form consent | REQUIRED |
| Final form submit | 1 |
| Final form backend | NOT CONNECTED |
| Modal partials | 0 |
| Modal markup | 0 |
| Modal triggers | 0 |
| Modal initializers | 0 |

## Unrelated WIP (excluded from freeze commit)

| Path | Note |
|------|------|
| `reviews/foundation/visual/*` | Capture artifact refresh |
| `reviews/main-content/pre-reviews-image-fix/*` | Capture artifact refresh |
| `scripts/_capture_image_reviews.py` | Capture tooling |

## Archive

`C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-PRE-MODALS-OPERATOR-STABLE-01-SOURCE.zip`
