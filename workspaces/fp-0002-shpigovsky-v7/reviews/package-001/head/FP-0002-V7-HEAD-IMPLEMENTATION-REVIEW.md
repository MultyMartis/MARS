# FP-0002 V7 Head Implementation Review

**Date:** 2026-06-24  
**Package:** #001 Phase 2  
**Status:** COMPLETE_PENDING_OPERATOR_REVIEW

---

## Implementation summary

| Item | Path / value |
|------|----------------|
| Shared partial | `src/partials/layout/head.html` |
| Home page | `src/pages/index.html` — `@@include` + parameters |
| Services page | `src/pages/uslugi.html` — `@@include` + parameters |
| Favicon source | Emblem mark derived from `src/img/branding/logo.svg` (Spig_v1.2 branding family) |
| Favicon set | `src/favicon/favicon.svg`, `favicon-32x32.png`, `apple-touch-icon.png`, `favicon.ico` |
| Social preview | `src/img/social/og-default.jpg` (1200×630, hero-main center crop) |
| Gulp favicon task | `gulpfile.js` → `dist/assets/favicon/**` |
| WP migration contract | `foundation/FP-0002-V7-HEAD-WORDPRESS-MIGRATION.md` |
| Social contract | `foundation/FP-0002-V7-SOCIAL-PREVIEW-CONTRACT.md` |

---

## Page head data

### Home

| Field | Value |
|-------|-------|
| title | Шпиговский дом — центр профилактики и лечения зависимостей |
| description | Шпиговский дом — центр профилактики и лечения зависимостей. Программа восстановления с уважением к личности. TEMPORARY_SEO_COPY |
| canonical | https://shpigovsky.ru/ |
| robots | index, follow |
| og:image | https://shpigovsky.ru/assets/img/social/og-default.jpg |

### Services

| Field | Value |
|-------|-------|
| title | Услуги — Шпиговский дом |
| description | Услуги центра «Шпиговский дом»: программа реабилитации, сопровождение и поддержка на пути восстановления. TEMPORARY_SEO_COPY |
| canonical | https://shpigovsky.ru/uslugi/ |
| robots | index, follow |
| og:image | https://shpigovsky.ru/assets/img/social/og-default.jpg |

---

## Body regression boundary

Head-only change scope:

- No `src/partials/sections/*` edits
- No `src/scss/*` edits
- No `src/js/*` edits
- Body markup unchanged except `<head>` extraction

Expected: **body pixel differences = 0** (head not in viewport captures).

---

## Operator review checklist

- [ ] Approve TEMPORARY_SEO_COPY descriptions
- [ ] Approve og-default.jpg crop/composition
- [ ] Approve favicon emblem at 16×16 / 32×32
- [ ] Confirm production absolute URLs for staging cutover

---

## Verdict

```text
PHASE 2 HEAD — IMPLEMENTED — PENDING OPERATOR REVIEW
```
