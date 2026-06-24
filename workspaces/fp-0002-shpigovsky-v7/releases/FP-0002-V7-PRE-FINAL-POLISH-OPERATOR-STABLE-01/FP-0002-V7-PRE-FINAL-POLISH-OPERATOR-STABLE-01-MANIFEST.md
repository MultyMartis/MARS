# FP-0002 V7 Pre-Final Polish Release Manifest

**Release ID:** `FP-0002-V7-PRE-FINAL-POLISH-OPERATOR-STABLE-01`  
**Created:** 2026-06-24  
**Workspace:** `workspaces/fp-0002-shpigovsky-v7/`  
**Lifecycle:** `PRE_FINAL_POLISH_STABLE`  
**Source authority:** `OPERATOR_CANONICAL`  
**Design authority:** `Spig_v1.2.fig`

## Baseline references

| Field | Value |
|-------|-------|
| Branch | `mars/post-cycle8-live-tests` |
| Confirmed V7 commit | `5a8fd0a6` — refactor(fp-0002): normalize section vertical rhythm |
| Freeze HEAD at capture | `6d99b039` |
| Annotated tag | `fp-0002-v7-pre-final-polish-operator-stable-01` |

## Package #001 status at freeze

| Phase | Status |
|-------|--------|
| Phase 1 — Figma rules | COMPLETE |
| Phase 2 — Head | TECHNICALLY_COMPLETE |
| Phase 3A — Intro content | COMPLETE |
| Phase 3B — Founder quote SVG | COMPLETE |
| Phase 3B — Gallery captions | IMPLEMENTED_BUT_PLACEMENT_REQUIRES_FIX |
| Phase 3C — Recovery life | CONDITIONALLY_ACCEPTED |
| Phase 4A — Spacing cleanup | COMPLETE |
| Global visual polish | NOT_STARTED |

## Gallery captions

```text
CONTENT_VERIFIED
PLACEMENT_INCORRECT
REQUIRED: BELOW_IMAGE
```

## Recovery life

```text
DESKTOP_FIGMA_VERIFIED
MOBILE_RESPONSIVE_DERIVED
FINAL_VISUAL_REVIEW_REQUIRED
```

## Head

```text
TECHNICALLY_COMPLETE
SEO_COPY_REVIEW_PENDING
FAVICON_VISUAL_REVIEW_PENDING
OG_VISUAL_REVIEW_PENDING
```

## Form backend

```text
BLOCKED
Captcha: BLOCKED
```

## Operator-authored src protection

| File | Diff after 5a8fd0a6 | Operator-authored | Preserve | Freeze in stable | Allowed polish edit |
| ---- | ------------------- | ----------------: | -------: | ---------------: | ------------------: |
| `src/pages/index.html` | NO | YES | YES | YES | YES (gallery DOM only) |
| `src/pages/uslugi.html` | NO | YES | YES | YES | NO |
| `src/scss/style.scss` | NO | YES | YES | YES | YES (proven mismatches) |
| `src/js/main.js` | NO | YES | YES | YES | ONLY IF PROVEN |
| `src/partials/sections/*` | NO | YES | YES | YES | YES (gallery partial) |
| `src/partials/layout/*` | NO | YES | YES | YES | NO |
| `src/partials/components/*` | NO | YES | YES | YES | NO |
| `gulpfile.js` | NO | YES | YES | YES | NO |
| `package.json` | NO | YES | YES | YES | NO |
| `package-lock.json` | NO | YES | YES | YES | NO |
| `foundation/*` | NO | YES | YES | YES | YES (status docs) |
| `reviews/package-001/*/_fig_extract_temp/` | untracked | YES | NO | NO | NO |
| Unrelated repository WIP | N/A | NO | NO | NO | NO |

## Validation snapshot (pre-polish freeze)

```text
dist/index.html = PRESENT
dist/uslugi.html = PRESENT
Project SCSS files = 1
Main JS entry = src/js/main.js
data-safe-unknown = 0
legacy radius tokens = 0
button-letter-spacing = 0

Gallery Swiper instances = 1
Reviews Swiper instances = 1
Specialists Swiper instances = 1
Comfort Fancybox = ACTIVE
FAQ = ACTIVE
Modal = ACTIVE
Final form = PRESENT

Home horizontal overflow (320,390,768,1024,1025,1398) = 0
Services horizontal overflow (320,390,768,1024,1025,1398) = 0
```

## Known issues recorded (not fixed at freeze)

```text
gallery_caption_placement: OVERLAY — fix scheduled post-backup-gate
recovery_life_mobile: RESPONSIVE_DERIVED — final review during polish
head_seo_copy: PENDING_MARKETING_REVIEW
head_favicon_visual: PENDING_OPERATOR_REVIEW
head_og_visual: PENDING_OPERATOR_REVIEW
form_backend: BLOCKED
captcha: BLOCKED
services_unimplemented_blocks: hero, addictions, mental-health, eating-disorders (intentional)
```

## External backup

| Field | Value |
|-------|-------|
| Archive | `C:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v7\releases\FP-0002-V7-PRE-FINAL-POLISH-OPERATOR-STABLE-01-SOURCE.zip` |
| SHA-256 | see `CHECKSUMS-SHA256.txt` |

## Parent reference

| Field | Value |
|-------|-------|
| V6 workspace | `workspaces/fp-0002-shpigovsky-v6/` |
| V6 lifecycle | `FROZEN_FALLBACK` |
| V6 tag | `fp-0002-v6-final-before-v7-operator-stable-01` |
