# FP-0002 V9-06E4 Shared Background Image Blocks Audit

**Date:** 2026-07-06

## Finding

Shared CTA/form backgrounds are **broken visually on WP runtime** because `v9-style.css` retains **static root paths**:

```css
background-image: url("/assets/img/content/home-final-form/home-final-form-background.webp");
```

On `shpigovsky.test`, `/assets/...` returns **404**. Theme path `/wp-content/themes/shpigovsky/assets/...` returns **200**.

## Affected selectors (4 rules)

1. `.home-rehabilitation-requirements__cta-band::before`
2. `.final-form__band::before`
3. `.program-cta-band::before`
4. Recovery-life section background (line ~20333)

## Blocks in scope

| Block | Markup | Background |
|-------|--------|------------|
| `final-form-heading` | Present (`final-form__band`) | **Broken CSS path** |
| `service-subdivision-start-heading` | Present (visually-hidden in program-cta-band-section) | **Broken CSS path** |
| `home-rehabilitation-requirements__cta-band` | Present on home / stages embed | **Broken CSS path** |

Assets **exist** in theme — this is not an asset-delivery gap for `home-final-form-background.webp`.

Evidence JSON: `validation/v9-06e4-services-layout-shared-bg-visual-reconciliation-audit/shared-background-image-blocks-audit.json`
