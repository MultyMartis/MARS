# FP-0002 V6 Final Release Manifest

**Release ID:** `FP-0002-V6-FINAL-BEFORE-V7-OPERATOR-STABLE-01`  
**Created:** 2026-06-24  
**Workspace:** `workspaces/fp-0002-shpigovsky-v6/`  
**Status:** `FROZEN_FALLBACK`  
**Current src:** `OPERATOR_CANONICAL`

## Release meaning

Last operator-canonical FP-0002 V6 state after manual polish and reuse-only services rollback, before V7 workspace creation and before package #001 implementation.

## Baseline references

| Field | Value |
|-------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| Last FP-0002 commit before operator post-114b064 edits | `114b064d7398f09e9cc50686ed46b3482ef2c7b9` |
| Freeze commit | *(set at tag creation)* |
| Annotated tag | `fp-0002-v6-final-before-v7-operator-stable-01` |

## Page status

| Field | Value |
|-------|-------|
| Home page | PRESENT |
| Services page mode | REUSE_ONLY |
| Services new unique blocks | 0 |
| Services remaining blocks | NOT IMPLEMENTED |

## Interaction status

| Component | Status |
|-----------|--------|
| Gallery Swiper | ACTIVE |
| Reviews Swiper | ACTIVE |
| Specialists Swiper | ACTIVE |
| Comfort Fancybox | ACTIVE |
| Modal system | FRONTEND IMPLEMENTED |
| Form backend | BLOCKED |
| Captcha configuration | BLOCKED |

## Design and package boundaries

| Field | Value |
|-------|-------|
| Design source at V6 freeze | HISTORICAL PRE-V7 BASELINE |
| Spig_v1.2 migration | NOT STARTED |
| Package #001 | NOT STARTED |
| V7 workspace | NOT CREATED at snapshot time |

## Operator-authored src changes after `114b064`

All changes inside active V6 `src/` after baseline commit `114b064` are operator-authored and preserved without normalization:

| File | Diff after 114b064 | Operator-authored | Preserve | Include in V6 freeze | Copy to V7 |
| ---- | ------------------ | ----------------: | -------: | -------------------: | ---------: |
| `src/partials/sections/hero.html` | YES (whitespace/formatting) | YES | YES | YES | YES |
| `src/scss/style.scss` | YES (overflow, Fancybox compensation, section padding, treatment panel) | YES | YES | YES | YES |

## Excluded from freeze authority (classified separately)

| Category | Treatment |
|----------|-----------|
| Review screenshots under `reviews/` | Historical capture artefacts — NOT operator source |
| `scripts/_capture_image_reviews.py` | Capture tooling — NOT operator source |
| Temporary exports / recovery archives | EXCLUDED |
| Unrelated repository WIP | EXCLUDED |

## Validation snapshot (2026-06-24)

```text
Home page present = YES
Services page present = YES
Project-owned SCSS files = 1
Main JS entry = src/js/main.js
Google Fonts references in active HTML/SCSS/JS = 0
External Inter references in active HTML/SCSS/JS = 0
data-safe-unknown = 0
Legacy radius tokens = 0
button-letter-spacing token = 0

Gallery Swiper instances = 1
Reviews Swiper instances = 1
Specialists Swiper instances = 1
Comfort Fancybox = ACTIVE
Modal component = ACTIVE
FAQ = ACTIVE
Final form = PRESENT

Home desktop 1398 horizontal overflow = 0
Home mobile 390 horizontal overflow = 0
Services desktop 1398 horizontal overflow = 0
Services mobile 390 horizontal overflow = 0
```

## Known baseline issues (documented, not fixed at freeze)

```text
home_faq_answers_2_10: BLOCKED
home_reviews_content: DEMO
services_unimplemented_blocks: service-hero, addictions, mental-health, eating-disorders
form_backend: BLOCKED
captcha_configuration: BLOCKED
INTER-FONT-PROVENANCE.md contains historical Google Fonts URL (documentation only, not runtime)
```

## External backup

| Field | Value |
|-------|-------|
| Archive | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v6\releases\FP-0002-V6-FINAL-BEFORE-V7-OPERATOR-STABLE-01-SOURCE.zip` |
| SHA-256 | *(see CHECKSUMS-SHA256.txt and BACKUP-MANIFEST in archive)* |

## Restore

See `RESTORE-INSTRUCTIONS.md` in this release directory.
