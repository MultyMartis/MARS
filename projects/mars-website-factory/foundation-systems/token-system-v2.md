# Foundation token system v2

**Status:** documented implementation architecture. **Not** a design-system product or token linter.

**Aligns with (intent only):** [cadence-tier-model.md](../cadence-tier-model.md), [design-token-intelligence-governance.md](../design-token-intelligence-governance.md).

---

## 1. Token layers

| Layer | Scope | Where defined | Override rule |
|-------|--------|---------------|---------------|
| **Global** | Brand + layout primitives shared site-wide | `scss/_tokens.scss` | HITL + Critical blast radius |
| **Semantic** | Role names (`$color-cta-primary`, `$space-section-m`) | same file, maps → globals | Prefer semantic in sections |
| **Local** | One section/block (`$hero-overlay-opacity`) | section SCSS top | Must not redefine globals |
| **Section override** | Single boundary exception | section SCSS + REPORT | Document reason; no silent global change |

**Rule:** sections consume **semantic** tokens; globals change only via `_tokens.scss`.

---

## 2. Required token families

### Spacing

```scss
// Scale: 4px base step (project may remap)
$space-1: 4px;
$space-2: 8px;
$space-3: 12px;
$space-4: 16px;
$space-5: 24px;
$space-6: 32px;
$space-7: 48px;
$space-8: 64px;

// Section rhythm (maps cadence tiers — project maps px)
$section-gap-xs: $space-3;
$section-gap-s:  $space-5;
$section-gap-m:  $space-7;
$section-gap-l:  $space-8;
$section-gap-xl: 96px; // project token — not Factory universal px
```

**Section rhythm:** apply `$section-gap-*` on **section wrapper** (`padding-block` or margin utility), not random inner margins.

### Containers

```scss
$container-max: 1200px;   // project default
$container-pad: $space-5;
$container-pad-mobile: $space-4;
```

Use `.container` mixin: `max-width` + horizontal padding; sections do not invent new max-widths.

### Breakpoints (reference — confirm in handoff)

```scss
$bp-sm: 576px;
$bp-md: 768px;
$bp-lg: 1024px;
$bp-xl: 1280px;
```

### Z-index / layers

See [modal-overlay-system-v2.md](modal-overlay-system-v2.md). Centralize in `scss/_layers.scss`:

```scss
$z-base: 1;
$z-dropdown: 100;
$z-sticky-cta: 200;
$z-header: 300;
$z-overlay-readability: 10; // local stacking inside section
$z-modal-backdrop: 1000;
$z-modal: 1010;
$z-toast: 1100;
```

**Forbidden:** section-local `z-index: 99999`.

### Radius

```scss
$radius-sm: 4px;
$radius-md: 8px;
$radius-lg: 12px;
$radius-pill: 999px;
```

CTA/input share `$radius-md` unless handoff marks FLEXIBLE.

### Shadows

```scss
$shadow-sm: 0 1px 2px rgba(0,0,0,.06);
$shadow-md: 0 4px 12px rgba(0,0,0,.08);
$shadow-lg: 0 12px 32px rgba(0,0,0,.12);
```

Cards/modals only — not hero atmosphere.

### Timing / transitions

```scss
$duration-fast: 150ms;
$duration-base: 250ms;
$duration-slow: 400ms;
$ease-standard: cubic-bezier(0.4, 0, 0.2, 1);
$ease-out: cubic-bezier(0, 0, 0.2, 1);
```

Pair with [interaction-motion-system-v2.md](interaction-motion-system-v2.md).

### Elevation

Map elevation → shadow token only (no duplicate box-shadow literals in sections).

### Overlay darkness (readability)

```scss
$overlay-dark-25: rgba(0, 0, 0, 0.25);
$overlay-dark-40: rgba(0, 0, 0, 0.40);
$overlay-dark-55: rgba(0, 0, 0, 0.55);
```

Hero text-on-image uses **section-local** variable referencing these globals.

---

## 3. Responsive adaptation logic

| Token class | Mobile rule |
|-------------|-------------|
| `$section-gap-*` | Reduce one tier on `< $bp-md` unless handoff forbids |
| `$container-pad` | Use `-mobile` variant |
| Typography scale | See [responsive-system-v2.md](responsive-system-v2.md) — fluid via `clamp()` or stepped `@media` |

**Desktop-first exception:** only when handoff `responsive_rules` says so; still define tokens once in `_tokens.scss`.

---

## 4. SCSS structure (target)

```text
scss/
├── _tokens.scss      # globals + semantic maps
├── _layers.scss      # z-index stack
├── _breakpoints.scss # media mixins
└── sections/         # local overrides only
```

**Entry import order:** tokens → layers → breakpoints → foundations → sections.

---

## 5. Survivability (section replacement)

- Replacing a section must **not** add new global tokens without REPORT + Critical review.
- Local tokens die with the section partial — no orphan `$hero-*` in globals after delete.
- Renaming a semantic token = **global** blast radius per [section-replacement-contract-v1.md](../section-replacement-contract-v1.md).

---

## 6. Anti-patterns

- Raw hex/spacing in section SCSS when a semantic token exists.
- Per-section breakpoint values.
- `!important` on token-driven properties.
- Mixing atmosphere gradient tokens with modal backdrop tokens.

*Wave 2 — token architecture.*
