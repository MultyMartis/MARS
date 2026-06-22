# FP-0002 V6 SECTION-002 SOURCE-TO-TOKEN MAP

| Role/property | Existing token | Reused | New proposal | Exception | Decision |
|---------------|----------------|--------|--------------|-----------|----------|
| Section background | `--color-page-background` | YES | NONE | — | GLOBAL |
| Card surface | `--color-surface` | YES | NONE | — | GLOBAL |
| Primary text | `--color-text-primary` | YES | NONE | — | GLOBAL |
| Secondary text | `--color-text-secondary` | YES | NONE | — | GLOBAL |
| Accent bar/icons | `--color-accent` | YES | NONE | — | GLOBAL |
| Container width | `--container-main` | YES | NONE | — | GLOBAL |
| Side padding | `--page-padding-inline` | YES | NONE | — | GLOBAL |
| Group padding | `--section-padding-standard` | YES | NONE | — | GLOBAL (registered `:root`) |
| Same-bg gap | `--section-gap-same-bg` | YES | NONE | — | GLOBAL (registered `:root`) |
| H2 typography | `--font-size-h2`, `--line-height-h2` | YES | NONE | — | GLOBAL |
| Body typography | `--font-size-base`, `--line-height-base` | YES | NONE | — | GLOBAL |
| Heading gap | `--heading-content-gap` | YES | NONE | — | GLOBAL |
| Text stack gap | `--text-stack-gap` | YES | NONE | — | GLOBAL |
| Card grid gap | `--grid-gap-standard` | YES | NONE | — | GLOBAL |
| Card padding | `--card-padding-standard` | YES | NONE | — | GLOBAL |
| Card radius | `--radius-medium` | YES | NONE | — | GLOBAL |
| Card border | `--border-width`, `--border-color-subtle` | YES | NONE | — | GLOBAL |
| Accordion row spacing | `--accordion-row-spacing` | YES | NONE | — | GLOBAL (margin) |
| Toggle circle size | `--icon-size-small` | YES | NONE | — | COMPONENT |
| Founder CTA | `button--compact` + control tokens | YES | NONE | — | COMPONENT |
| Accent bar width | `--space-5` | YES | NONE | — | BLOCK via `$intro-programs-accent-bar-width` |
| Quote mark size | `--font-size-h1` | YES | NONE | EXACT_GEOMETRY | BLOCK |
| Clinical aspect | `1` | — | NONE | TECHNICAL | aspect-ratio |
| Bullet diamond | `--space-5` + `rotate(45deg)` | YES | NONE | TECHNICAL | CSS shape |
| Clinical placeholder fill | `--color-border-subtle` | YES | NONE | — | Until assets |
