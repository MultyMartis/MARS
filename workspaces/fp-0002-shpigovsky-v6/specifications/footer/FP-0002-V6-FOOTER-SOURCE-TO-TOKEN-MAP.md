# FP-0002 V6 FOOTER SOURCE-TO-TOKEN MAP

| Role | Existing token | Reused | Proposal | Scope | Decision |
| ---- | -------------- | -----: | -------- | ----- | -------- |
| Footer background | `--color-page-background` | YES | NONE | GLOBAL | REUSE |
| Primary text | `--color-text-primary` | YES | NONE | GLOBAL | REUSE |
| Muted text | `--color-text-secondary` | YES | NONE | GLOBAL | REUSE |
| Inverse CTA text | `--color-text-inverse` | YES | NONE | GLOBAL | REUSE |
| Accent CTA | `--color-accent` | YES | NONE | GLOBAL | REUSE |
| Border / dividers | `--border-color-subtle`, `--border-width` | YES | NONE | GLOBAL | REUSE |
| Container width | `--container-main` | YES | NONE | GLOBAL | REUSE |
| Container padding | `--page-padding-inline` | YES | NONE | GLOBAL | REUSE |
| Footer block padding | `--section-padding-compact` | YES | `--footer-padding-block` | LAYOUT_REGION | APPROVED alias |
| Column gap | `--space-30` / foundation `footer-gap` | YES | `--footer-column-gap` | LAYOUT_REGION | APPROVED |
| Row gap (top/main/legal) | `--space-40` | YES | `--footer-row-gap` | LAYOUT_REGION | APPROVED |
| Legal links gap | `--space-40` | YES | `--footer-legal-gap` | LAYOUT_REGION | APPROVED |
| Contact stack gap | `--space-20` | YES | `--footer-contact-stack-gap` | LAYOUT_REGION | APPROVED |
| Nav heading gap | `--space-15` | YES | `--footer-nav-heading-gap` | LAYOUT_REGION | APPROVED |
| Nav link gap | `--space-10` | YES | `--footer-nav-link-gap` | LAYOUT_REGION | APPROVED |
| Legal row padding-top | `--space-30` | YES | `--footer-legal-row-padding-block` | LAYOUT_REGION | APPROVED |
| Top row flex gap | `--space-20` | YES | NONE | GLOBAL | REUSE |
| Social gap | `--space-10` | YES | NONE | GLOBAL | REUSE |
| Contact item gap | `--space-15` | YES | NONE | GLOBAL | REUSE |
| Phone typography | `--font-size-large`, `--font-weight-semibold` | YES | NONE | GLOBAL | REUSE |
| Meta typography | `--font-size-small`, `--line-height-small` | YES | NONE | GLOBAL | REUSE |
| Nav heading typography | `--font-size-base`, semibold | YES | NONE | GLOBAL | REUSE |
| Primary button | `--control-height-primary`, `--button-*` | YES | NONE | COMPONENT | REUSE |
| Outline callback | `--control-height-compact`, compact padding | YES | `$footer-callback-font-size` | FOOTER_BLOCK | APPROVED 12px |
| Social / contact icon size | `--icon-size-medium`, `--icon-size-small` | YES | NONE | COMPONENT | REUSE |
| Icon circle surface | `--color-surface` | YES | NONE | GLOBAL | REUSE |
| Logo dimensions | Header exception 182×82 | YES | `$footer-logo-width/height` | EXACT_EXCEPTION | REUSE |
| Grid columns | `repeat(4, minmax(0, 1fr))` | — | — | TECHNICAL | ALLOWED |
| Phone `margin-left: auto` | — | — | — | TECHNICAL | ALLOWED |
| Legal underline | `text-decoration: underline` | — | — | TECHNICAL | ALLOWED |

## Authorization gate

```text
footer_identified: true
footer_text_inventory_complete: true
footer_asset_inventory_complete: true
token_lookup_complete: true
arbitrary_values_allowed: false
arbitrary_values_count: 0
hidden_fallback_literals_count: 0
html_authorized: true
scss_authorized: true
javascript_authorized: false
responsive_authorized: false
```
