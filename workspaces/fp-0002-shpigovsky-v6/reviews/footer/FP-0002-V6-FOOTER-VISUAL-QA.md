# FP-0002 V6 FOOTER VISUAL QA

**Date:** 2026-06-22  
**Viewport:** 1398×2200 (full-page capture); footer reference crop 1398×567 @ JPG Y 15776–16343  
**Metrics:** `reviews/footer/_qa-footer-metrics.json`

---

| Metric | JPG observed | Rendered | Delta | Status |
| ------ | ------------ | -------- | ----- | ------ |
| Footer top boundary | Y 15776 (full-page context) | N/A (isolated page) | N/A | NOT APPLICABLE |
| Footer total height | 567px | 569.95px | +2.95px | ACCEPTABLE |
| Background | `#e6eff6` family | `--color-page-background` | LOW | PASS |
| Container | ~1220 + inline padding | `--container-main` + `--page-padding-inline` | — | PASS |
| Columns | 4 (contacts + 3 nav) | 4-column grid | — | PASS |
| Logo | 182×82 SVG | 182×82 | 0 | PASS |
| Top row | logo, social×3, phone, 2 CTAs | matches | — | PASS |
| Navigation | 3× `Название раздела` + placeholder links | matches | — | PASS |
| Contact groups | address, schedule, email, copyright, privacy | matches | — | PASS |
| Social icons | Telegram, WhatsApp, YouTube | Telegram + WhatsApp; YouTube empty | — | ASSET_REQUIRED |
| CTA | outline + red primary | matches | — | PASS |
| Legal row | Overseo + 2 underlined links | matches | — | PASS |
| Dividers | horizontal rules top/main/legal | border tokens | — | PASS |
| Typography | small/meta + large phone/labels | token roles | — | ACCEPTABLE |
| Bottom spacing | JPG bottom edge Y 16343 | render bottom padding | ~3px | ACCEPTABLE |
| Pixel MAE (top region) | — | 9.21 | — | ACCEPTABLE |

---

## Correction pass

| Field | Value |
|-------|-------|
| Issue | Footer height 610px — duplicate `padding-block` on `__main` |
| Evidence | JPG total 567px; rendered pre-fix 609.95px |
| Token / role | `--footer-row-gap` — apply top edge only before legal separator |
| Change | `padding-block` → `padding-top` on `.site-footer__main` |
| Post-fix height | 569.95px |
| Tokens changed during QA | NONE (same token, edge scope) |
| Exceptions changed during QA | NONE |
| Arbitrary values introduced | 0 |
| Arbitrary values remaining | 0 |

---

## Required token summary

```text
Variables reused:
--color-page-background, --color-text-primary, --color-text-secondary, --color-text-inverse, --color-accent, --color-surface, --container-main, --page-padding-inline, --section-padding-compact, --space-10, --space-15, --space-20, --space-30, --space-40, --footer-column-gap, --footer-gap, --footer-padding-block, --footer-row-gap, --footer-legal-gap, --footer-nav-heading-gap, --footer-nav-link-gap, --footer-contact-stack-gap, --footer-legal-row-padding-block, --font-size-*, --line-height-*, --font-weight-*, --control-*, --button-*, --icon-size-*, --border-*, --radius-*

New tokens proposed:
--footer-column-gap, --footer-gap, --footer-padding-block, --footer-row-gap, --footer-legal-gap, --footer-nav-heading-gap, --footer-nav-link-gap, --footer-contact-stack-gap, --footer-legal-row-padding-block

New tokens approved:
(same as proposed — added to :root)

Layout-region tokens:
--footer-column-gap, --footer-gap, --footer-padding-block, --footer-row-gap, --footer-legal-gap, --footer-nav-heading-gap, --footer-nav-link-gap, --footer-contact-stack-gap, --footer-legal-row-padding-block

Footer block-level tokens:
$footer-callback-font-size (12px)

Exact geometry exceptions:
$footer-logo-width (182px), $footer-logo-height (82px)

Technical CSS values:
repeat(4, minmax(0, 1fr)), margin-left: auto, line-height: 1, margin: 0, width: 100%, flex shorthand, min-width: 0, text-decoration: underline

Arbitrary values found: 0
Arbitrary values removed: 0
Arbitrary values remaining: 0

Hidden fallback literals found: 0
Hidden fallback literals remaining: 0
```
