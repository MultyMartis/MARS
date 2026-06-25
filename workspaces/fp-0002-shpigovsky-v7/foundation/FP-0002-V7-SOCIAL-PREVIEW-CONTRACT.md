# FP-0002 V7 Social Preview Contract

**Workspace:** `workspaces/fp-0002-shpigovsky-v7/`  
**Package:** #001 Phase 2

---

## Default asset

| Field | Value |
|-------|-------|
| Path (source) | `src/img/social/og-default.jpg` |
| Path (build) | `dist/assets/img/social/og-default.jpg` |
| Format | JPG |
| Dimensions | **1200 × 630** |
| Max practical weight | ≤ 350 KB (optimize on change) |

---

## Source composition

| Input | Role |
|-------|------|
| `src/img/hero/hero-main.png` | Primary photo — center crop to 1200×630 |
| Branding | No full wordmark overlay in default asset |
| Screenshot of page | **Not used** as final OG |

---

## Safe text area

- Assume center crop may trim edges on some networks.
- Avoid small type or long claims in raster OG; page-level `og:title` / `og:description` carry copy.
- Keep lower third relatively calm for platform UI overlays.

---

## Page-specific override

Head partial accepts per-page `ogImage` / `ogImageAlt`. Current mapping:

| Page | og:image |
|------|----------|
| Home | `og-default.jpg` |
| Services | `og-default.jpg` |

Future pages may pass unique absolute URLs without changing partial structure.

---

## Absolute production URL requirement

Social meta uses **absolute** production URLs:

```text
https://shpigovsky.ru/assets/img/social/og-default.jpg
```

Authority: `FP-0002-PROJECT-PASSPORT.md` — `DOM-SHPIG-01` / `shpigovsky.ru`.

Local/preview hosts must not rewrite production OG URLs in the static template contract.

---

## Review gate

Operator review required before treating OG asset as marketing-approved (status: **IMPLEMENTED — PENDING OPERATOR REVIEW**).
