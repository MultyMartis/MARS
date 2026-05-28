# Hero Implementation Contract v0

**Scope:** PPC `hero--v5` pattern — first proven on Triumph zakaz.

## Required DOM zones

| Zone | Class (Triumph) | Required when |
|------|-----------------|---------------|
| Shell | `.hero__shell` | always |
| Main | `.hero__main` | `grid_form_aside` or `stacked` |
| Content | `.hero__content` | always |
| Aside | `.hero__aside` | `cta_priority: form` |
| Lower | `.hero__lower` | `proof_priority: hero_strip` OR cargo OR qualification |

## Background

| Element | Rule |
|---------|------|
| `.first-screen` | bg `<img>` + overlay — per productive drift P3 |
| No competing inline machine collage in content column | |

## Content order (`hero__content`)

1. H1 (single)
2. Lead
3. Capability specs (prefer list, not 6 paragraphs)

## Form (`hero__aside`)

- Primary submit = pack CTA label
- Consent block — expect mobile wrap risk
- Production endpoint — out of visual semantics; must be wired before launch

## Lower band

| Component | Max items (default) |
|-----------|---------------------|
| proof strip | 4 ops OR hybrid 3 |
| cargo cards | 6 desktop / 4 mobile (calibration target) |
| qualification notice | 1 line when `qualification_mode` requires |

## Forbidden

- `hero__rate` fake hourly
- fleet claims in hero
- second H1
- 6+ feature paragraphs in main without lower band split

## SCSS isolation

`hero--v5` scoped to PPC `data-page-type` — do not leak to legacy index partials.

## Partial path (zakaz)

`workspaces/triumph-manipulator-landing-v5/src/partials/sections/v5-ppc/zakaz/screen-01-hero.html`  
`workspaces/triumph-manipulator-landing-v5/src/scss/sections/_v5-hero-extensions.scss`

**Read-only cite** — v0 docs do not modify workspace.

## Acceptance

- [ ] Fields in pack match as-built zones
- [ ] `mobile_critical` items reachable on 390px or documented exception
- [ ] `destructive` drift empty
