# CSS Variable First Law v1

**Status:** **MANDATORY PRODUCTION CONTRACT**

**Scope:** All Website Factory execution cases; frontend agents; Cursor prompts; block implementation specifications; SCSS production; visual QA correction passes.

**Enforcement:** **DOCUMENTED MANDATORY GATE** — **AUTOMATED ENFORCEMENT — NOT YET IMPLEMENTED**

**Registry:** [website-factory-cross-layer-artefact-registry-v1.md](website-factory-cross-layer-artefact-registry-v1.md) · [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

## Purpose

Production SCSS must not receive arbitrary design values copied from screenshots, estimates, or prior projects. Every **reusable** design value must trace through the shared token system before it reaches block styles. Truly unique evidence-backed geometry may remain **direct CSS** local to the owning block — it must not pollute `:root` as a selector-specific or one-use alias.

**Companion law:** [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md) — compact scale, no selector tokens, no alias chains, physical padding/margin properties.

---

## Core law (corrected interpretation)

1. **No arbitrary production value before token lookup** for any **reusable** spacing, radius, type, or color role.
2. **No repeated production value without token registration** — repeated magnitudes belong on the compact site scale ([universal-style-scale-law-v1.md](universal-style-scale-law-v1.md)), not as selector-named aliases.
3. **No block styling before style foundation approval.**
4. **No magic-number correction during visual QA.**
5. **No fallback literal that silently replaces a missing required token.**
6. **New tokens require evidence, role, and scope.**
7. **Exact geometry exceptions must remain explicit and local.**
8. **Token assignment must match structural owner** — `var(--token)` on the wrong selector still violates production law when the value creates section-boundary or container geometry at the wrong layer.

---

## Mandatory chain (allowed)

```text
visual evidence
→ style role
→ existing design token
→ var(--token)
→ block SCSS
```

When no suitable token exists:

```text
visual evidence
→ new token proposal
→ token registration
→ operator/specification approval
→ var(--new-token)
→ block SCSS
```

---

## Forbidden chain

```text
visual estimate
→ arbitrary number
→ production SCSS
```

---

## Token lookup order

Apply in order; stop and register a proposal when no level fits:

1. **Site-wide foundation token** (`:root` / Style Foundation JSON)
2. **Shared component token** (controls, buttons, icons, surfaces)
3. **Page-family token** (page-scoped custom properties)
4. **Approved block-level token** (documented in Block Implementation Specification)
5. **Exact geometry exception** (local, classified, evidenced)
6. **Technical CSS value** (`0`, `100%`, `auto`, `1px` border, local `z-index`)

If none apply:

```text
STOP
→ register token proposal
→ document evidence
→ approve
→ implement
```

---

## Token scope model

| Scope | Description | Owner document |
|-------|-------------|----------------|
| `GLOBAL` | Site-wide `:root` tokens | Site-Wide Style Foundation |
| `COMPONENT` | Reusable control/icon/surface tokens | Style Foundation + component layer |
| `PAGE_FAMILY` | Page-scoped variables | Page Implementation Specification |
| `BLOCK` | Block-local registered tokens | Block Implementation Specification |
| `EXACT_EXCEPTION` | Art-directed geometry not on scale | Block spec exception register |
| `TECHNICAL` | Browser/layout technical values | Pre-SCSS checklist technical list |

Each new token must record: **name**, **value**, **role**, **scope**, **source evidence**, **reuse expectation**, **status**, **owner document**.

---

## Token naming law

- **lowercase-kebab-case** only
- Examples: `--font-size-base`, `--pad-gap`, `--control-height-primary`, `--radius-full`, `--container-main`
- Forbidden: `--base-Font-size`, `--Title-h1-Font-size`, `--pad-btns`, `--hero-button-width-297`, `--header-random-gap`, `--footer-column-gap`, `--header-padding-block-start`
- **Selector names are not valid token reasons** for ordinary spacing or radius — see [universal-style-scale-law-v1.md](universal-style-scale-law-v1.md) No Selector Token Law

---

## Prohibited patterns (violations)

Without documented classification and approval:

```scss
width: 297px;
max-width: calc(100% - 40px);
padding: 27px;
gap: 33px;
font-size: 17px;
border-radius: 13px;
```

Also prohibited:

- arbitrary visual tuning during QA
- duplicated token values under different names
- selector-specific spacing/radius aliases (`--footer-*`, `--header-*`, `--section-name-*` for primitive scale)
- alias chains that only rename an existing primitive for one block
- logical `padding-block` / `padding-inline` / `margin-block` / `margin-inline` / `inset-block` / `inset-inline` in production SCSS (physical properties required by default)
- local redefinition of global values without scope
- component width from screenshot when content sizing is correct
- magic-number overflow prevention
- hidden fallback literals: `var(--token, 30px)` for required foundation tokens
- copying numbers from a different project

---

## Allowed exceptions

Require **classification**, **evidence**, **reason**, **scope**, **review status**:

- exact image crop geometry
- art-directed `object-position`
- unique overlay coordinates
- local stacking indexes
- `1px` technical borders
- source aspect ratios
- browser/device technical values

---

## SCSS variable policy

Sass variables (`$…`) are for **compile-time only**: build paths, maps, mixins, functions, vendor configuration. Production design values flow through **CSS custom properties** first. If a Sass bridge is required, one authoritative value must be documented — not parallel unrelated systems.

---

## Layer contracts

| Transition | Contract |
|------------|----------|
| Foundation → tokens | [site-wide-style-foundation-contract-v1.md](site-wide-style-foundation-contract-v1.md) |
| Normalization → tokens | [practical-value-normalization-contract-v1.md](practical-value-normalization-contract-v1.md) |
| Block → SCSS | [block-implementation-specification-contract-v1.md](block-implementation-specification-contract-v1.md) |
| Pre-SCSS gate | [frontend-pre-scss-validation-checklist-v1.md](frontend-pre-scss-validation-checklist-v1.md) |
| Pipeline | [frontend-implementation-pipeline-v1.md](frontend-implementation-pipeline-v1.md) |
| Visual QA | [frontend-qa-reporting-standard-v1.md](frontend-qa-reporting-standard-v1.md) · [operator-visual-approval-law-v1.md](operator-visual-approval-law-v1.md) |

---

## Visual QA correction rule

Visual QA **must not** fix mismatch with:

- an arbitrary number
- a new local container width
- padding on the last child
- margin on the first child
- negative margin between sections
- a duplicating wrapper `max-width`

Route through:

```text
evidence
→ identify correct structural owner
→ identify existing token
→ update owner/token
→ apply var()
→ rerender
```

Every Visual QA report must include:

```text
Tokens changed
Exceptions changed
Arbitrary values introduced: 0
Arbitrary values remaining: 0
```

---

## Production report fields (mandatory)

```text
Core spacing tokens reused:
Core radius tokens reused:
Selector-specific tokens found:
Selector-specific tokens removed:
Selector-specific tokens remaining:
One-use tokens found:
One-use tokens removed:
One-use tokens remaining:
Alias chains found:
Alias chains removed:
Alias chains remaining:
Logical CSS properties found:
Logical CSS properties removed:
Logical CSS properties remaining:
Direct exact values:
New global tokens:
New shared component tokens:
Token admission result:
Variables reused
New tokens proposed
New tokens approved
Block-level tokens
Exact geometry exceptions
Technical CSS values
Arbitrary values found
Arbitrary values removed
Arbitrary values remaining
Fallback literals found
Fallback literals remaining
Primary container reused:
Custom container exceptions:
Duplicate container rules found:
Duplicate container rules remaining:
Section rhythm owners:
Boundary spacing workarounds found:
Boundary spacing workarounds removed:
Boundary spacing workarounds remaining:
```

---

## Changelog

| Date | Change |
|------|--------|
| 2026-06-22 | v1 — Mandatory production contract; FP-0002 V6 pilot cleanup |
| 2026-06-22 | v1.1 — Structural owner law; container/rhythm Visual QA ban; mandatory report fields |
| 2026-06-23 | v1.2 — Corrected interpretation: reusable values from shared scale; direct exact geometry allowed locally; Universal Style Scale Law cross-ref; expanded report fields |
