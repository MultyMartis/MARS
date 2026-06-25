# FP-0002 V7 Head Preflight Audit

**Date:** 2026-06-24  
**Workspace:** `workspaces/fp-0002-shpigovsky-v7/`  
**Bootstrap commit:** `af152616`

---

## Previous head locations

| Location | Role |
|----------|------|
| `src/pages/index.html` | Inline `<head>` (dev noindex skeleton title) |
| `src/pages/uslugi.html` | Inline `<head>` (partial production title) |
| `src/partials/layout/` | No head partial before this package |

---

## Element audit

| Element | Home current (pre) | Services current (pre) | Required | Action |
| ------- | ------------------ | ---------------------- | -------- | ------ |
| charset | UTF-8 | UTF-8 | utf-8 | Normalize in shared partial |
| viewport | width=device-width | width=device-width | width=device-width, initial-scale=1 | Shared partial |
| x-ua-compatible | absent | absent | ie=edge | Add in partial |
| title | FP-0002 Shpigovsky v6 — Zero Skeleton | Услуги — Шпиговский дом | Unique per page | Home + Services parameters |
| description | absent | absent | Non-empty | TEMPORARY_SEO_COPY from H1/theme |
| author | absent | absent | Шпиговский дом | Set in partial |
| robots | noindex, nofollow | noindex, nofollow | index, follow (production template) | Page parameters |
| canonical | absent | absent | Absolute production URL | https://shpigovsky.ru/… |
| theme-color | absent | absent | Brand token | #475371 |
| og:type | absent | absent | website | Page parameter |
| og:site_name | absent | absent | Шпиговский дом | Partial constant |
| og:title | absent | absent | Per page | Parameters |
| og:description | absent | absent | Per page | Parameters |
| og:url | absent | absent | Absolute | Match canonical |
| og:image | absent | absent | 1200×630 absolute | og-default.jpg |
| og:image dimensions | absent | absent | 1200×630 | Partial constants |
| og:locale | absent | absent | ru_RU | Partial constant |
| twitter:card | absent | absent | summary_large_image | Partial |
| twitter:title/description/image | absent | absent | Mirror OG | Partial |
| twitter:site | absent | absent | Omit if unconfirmed | NOT APPLICABLE |
| favicon links | absent | absent | svg + png + ico + apple | New `src/favicon/` |
| CSS vendor links | Swiper, Fancybox, style | same | Preserve order | Moved to partial |
| font preload | 3× inter woff2 | same | Preserve | Moved to partial |
| duplicate tags | none | none | none | Verified post-build |

---

## Canonical domain

| Field | Value |
|-------|-------|
| Authority | `FP-0002-PROJECT-PASSPORT.md` — DOM-SHPIG-01 |
| Production host | `shpigovsky.ru` |
| Status | **CONFIRMED** |

---

## Verdict (preflight)

```text
HEAD PREFLIGHT — READY FOR SHARED PARTIAL IMPLEMENTATION
```
