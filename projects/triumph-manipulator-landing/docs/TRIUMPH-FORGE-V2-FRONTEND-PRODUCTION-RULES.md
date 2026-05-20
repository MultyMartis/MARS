# TRIUMPH FORGE V2 — FRONTEND PRODUCTION RULES

**Status:** operational rules for AI-assisted implementation (human-operated).  
**Scope:** Triumph Manipulator Landing **V2** only.  
**Implementation locus:** `workspaces/triumph-manipulator-landing-v2/src/` — edit source only; never hand-edit `dist/`.  
**Not:** governance, runtime, orchestration, autonomous build/QA, or pixel-perfect certification.

**Authority stack (conflict order):**

1. **Canonical V2 visuals:** `projects/triumph-manipulator-landing/design/v2/` for the slice (see [`design/README.md`](../design/README.md)). **Do not** substitute `design/v1/`, `design/shared-assets/`, or a retired PDF as homepage structure truth for V2. A replacement PDF may be reissued later — until then, PNG exports + MD stack govern.
2. [`design-system/triumph-manipulator-design-system.md`](../design-system/triumph-manipulator-design-system.md) — visual law.
3. This file — production execution law for V2.
4. Workspace `AGENTS.md` — architecture and Gulp discipline.
5. MARS Forge overlay — phased workflow + freeze ([`agents/mars-forge/workflow.md`](../../../agents/mars-forge/workflow.md), [`agents/mars-forge/qa-checklist.md`](../../../agents/mars-forge/qa-checklist.md)).
6. Font Awesome governance — icon semantics / family / optical rhythm discipline ([`projects/mars-website-factory/font-awesome-governance-layer.md`](../../mars-website-factory/font-awesome-governance-layer.md), [`agents/mars-forge/font-awesome-governance-checklist.md`](../../../agents/mars-forge/font-awesome-governance-checklist.md)).

**Canonical page map:** [`V2-CANONICAL-STATE.md`](../V2-CANONICAL-STATE.md).  
**Legacy:** `workspaces/triumph-manipulator-landing/` (V1) — reference only; do not edit for V2 tasks.

---

## 1. PURPOSE

Provide **deterministic, measurable** rules so AI and operators can:

- implement or regenerate **one section at a time** without layout drift;
- stabilize responsive behavior before cosmetic tuning;
- freeze approved sections and detect unsafe edits;
- run repeatable frontend QA without claiming unverified automation.

**Success criteria:** build passes; no horizontal overflow at 320–1440px spot widths; section order and container logic unchanged unless explicitly unfrozen; tokens and spacing from defined scales only.

---

## 2. CORE IMPLEMENTATION PRINCIPLES

| # | Rule |
|---|------|
| P1 | **One primary section per task** — match a single partial under `src/partials/sections/` + its `_*.scss` (+ scoped JS if any). |
| P2 | **Phases in order:** structure → layout → styling → responsive → interaction → QA → freeze (Forge phases 1–7). |
| P3 | **Source-first:** all durable changes in `src/`; run `npm run build` in the V2 workspace before claiming done. |
| P4 | **No cross-section drive-by:** do not refactor frozen or unrelated partials in the same task. |
| P5 | **Evidence over narrative:** list changed paths, build result, spot viewport checks; flag gaps as **SAFE UNKNOWN**. |
| P6 | **Survivability over pixel-match:** readable type, stable stack, overflow prevention beat visual micro-tuning. |
| P7 | **Semantic HTML:** one `h1` per page; logical heading order; `main` / `header` / `footer` landmarks preserved. |

**Homepage section order (frozen until explicit restructure approval):**

`hero-conversion` → `machine-specs-transport-lists` → `trust-cases-social-proof` → `segments-applications-grid` → `problem-solution-matrix` → `consultation-lead-form` → `site-footer-v2` (footer outside `<main>` per `index.html`).

---

## 3. HARD FREEZE RULES

### 3.1 Always frozen (without written unfreeze)

| Item | Frozen element |
|------|----------------|
| F1 | `src/pages/index.html` **include order** and section list |
| F2 | Gulp folder architecture (`pages`, `partials/layout`, `partials/sections`, `partials/components`, mirrored `scss/`) |
| F3 | Global tokens in `src/scss/utils/_tokens.scss` and layout primitives in `_variables.scss` |
| F4 | Base container classes `.tm-container`, `.tm-container--wide`, `.tm-section` in `src/scss/base/_base.scss` |
| F5 | Shared components: `.btn` variants in `src/scss/components/_button.scss` |
| F6 | Color HEX table from design system §5 (no new brand colors without human approval) |

### 3.2 Frozen after section sign-off

When a section is marked **frozen** in the task REPORT:

- DOM skeleton (landmark tags, heading levels, major regions);
- BEM block root name (e.g. `.hero-conversion`, not renamed to `.hero-v3`);
- vertical rhythm for that section (`padding-block` from §5);
- CTA variant assignment (primary / outline / outline-on-dark) for that section;
- `@@include` graph for that partial.

### 3.3 Classification

| Class | Meaning | Examples |
|-------|---------|----------|
| **Frozen** | Change only with documented unfreeze + human approval | Index section order, approved hero layout grid |
| **Adaptive** | May change inside breakpoints per mockup / QA | Column count, stack order, image `object-position` per section brief |
| **Editable** | Copy, images, legal text, form labels (not structure) | Body text, alt strings, equipment rows |
| **Optional** | Omit if SAFE UNKNOWN blocks content | Reviews block, JSON-LD, CRM hook |

### 3.4 Unfreeze protocol

1. State **block_id** / partial name and reason.  
2. Limit diff to that partial + its SCSS (+ scoped JS).  
3. Re-run §14 checklist for that scope and adjacent frozen neighbors (spot).  
4. Record new freeze state in REPORT.

---

## 4. CONTAINER SYSTEM

**Single container pattern** — use existing classes only; do not nest `.tm-container` inside `.tm-container`.

| Token / class | Desktop (≥1025px) | Tablet (≤1024px) | Mobile (≤768px) |
|---------------|--------------------|------------------|-----------------|
| `.tm-container` max-width | **1400px** | 1400px | 1400px |
| `.tm-container` padding-inline | **40px** | **32px** | **16px** |
| `.tm-container--wide` max-width | **1720px** | 1720px | 1720px |
| `.tm-container--wide` padding-inline (desktop) | **56px** | 32px | 16px |

**Rules:**

- C1: Section root may be full-bleed; **content** sits in one `.tm-container` or `.tm-container--wide` child.
- C2: **Wide container** allowed only for **first-screen** blocks (hero + header track) per mockup `design/v2/01.png`; default sections use standard `.tm-container`.
- C3: `min-width` on `body` = **320px**; no fixed widths wider than viewport on content columns.
- C4: `margin-inline: auto` on containers only; sections do not set horizontal centering on arbitrary wrappers.
- C5: No third container width tier without design-system amendment.

---

## 5. SPACING SYSTEM

### 5.1 Allowed spacing scale (px only for new rules)

Use **only** these values for margin, padding, and gap unless a task cites an approved exception:

**4 / 8 / 12 / 16 / 20 / 24 / 32 / 40 / 48 / 64 / 96**

Maps to `$tm-space-*` in `_tokens.scss` (8px rhythm base).

### 5.2 Section vertical rhythm (frozen)

| Breakpoint | `padding-block` on `.tm-section` |
|------------|----------------------------------|
| Desktop (default) | **96px** |
| ≤1024px | **72px** |
| ≤768px | **56px** |

- S1: **No `margin-top` between sections** — separation is `padding-block` on section roots only.
- S2: **No negative margins** to pull sections together.
- S3: Internal block gaps: **24px** default grid gap; **16px** between stacked paragraphs; **32px** below `.tm-section-title` (24px with `.tm-section-title--tight`).

### 5.3 Forbidden spacing

- Arbitrary values: 10px, 15px, 18px, 22px, 36px, 50px, etc.
- Percent/vw padding on section shells (except full-bleed media internals).
- Doubling section padding via both parent and child (measure shared boundary — one gap only).

---

## 6. TYPOGRAPHY SYSTEM

### 6.1 Families and weights

| Role | Font | Weight |
|------|------|--------|
| Body, forms, FAQ answers | Roboto | **400** |
| Headings, eyebrows, buttons | Montserrat | **500** |

### 6.2 Size scale (`font-size` — **px only**)

| Token | px | Use |
|-------|-----|-----|
| caption | 12 | Legal, eyebrows |
| small | 14 | Secondary, buttons |
| body | 16 | Default text (minimum for marketing body on mobile) |
| lead | 18 | Lead paragraphs |
| subtitle | 22 | Large subheads |
| h3 | 24 | H3 |
| h2 | 32 | Section titles |
| h1 | 40 | H1 mobile/base |
| h1-lg | 48 | H1 at `min-width: 1200px` |

- T1: **No `font-size` below 14px** except **12px** legal/caption slots.
- T2: **No `rem` / `em` / `%` / `clamp()` for `font-size`.**
- T3: **`letter-spacing: 0` everywhere** — no negative tracking.
- T4: Body / lead: `line-height: calc(font-size + 4px)`.
- T5: Headings / buttons: `line-height: 1`.

### 6.3 Page heading law

- Exactly **one** `h1` on `index.html`.
- Do not skip levels (e.g. `h1` → `h4`).
- Section titles: prefer `h2` with class `.tm-section-title` unless mockup defines otherwise for that block.

---

## 7. CTA SYSTEM

### 7.1 Button geometry (frozen)

| Property | Value |
|----------|-------|
| Class base | `.btn` |
| Height | **40px** (`height` + `min-height` 40px) |
| Padding inline | **32px** default; hero may use **24px** (`.btn--hero`) |
| Border-radius | **0** |
| Font | Montserrat **500**, **14px**, uppercase allowed |
| Primary fill | `$tm-fill-accent` (#e30621); hover `$tm-fill-accent-hover` |
| Outline | 1px `$tm-color-accent` on light; `.btn--outline-on-dark` on dark surfaces |

### 7.2 Hierarchy (frozen roles)

| Level | Variant | Max per viewport area |
|-------|---------|------------------------|
| Primary | `.btn--primary` / `.btn--accent` | **1** primary action per hero / form cluster |
| Secondary | `.btn--outline` or `.btn--outline-on-dark` | **1** secondary beside primary |
| Tertiary | text link or icon link | Unlimited; must not compete visually with primary (no duplicate red filled buttons) |

### 7.3 CTA consistency rules

- C1: Reuse `partials/components/button.html` or matching markup — do not invent parallel button classes.
- C2: `tel:` / messenger links: min touch target **40×40px** effective area.
- C3: Icon + label gap: **8px** (`$tm-space-2`).
- C4: No `transform: translateY` or shadow hover on V2 buttons (flat industrial — tokens set `$tm-shadow-button: none`).
- C5: Modal triggers use `data-modal-open` with existing modal partial — no new modal framework.

---

## 8. SECTION ISOLATION RULES

- I1: Edit **only** the target partial + `src/scss/sections/_<name>.scss` (+ block JS module if exists).
- I2: Do not change `src/scss/style.scss` import order except when **adding** a new section file.
- I3: Selectors scoped under section BEM root (e.g. `.trust-cases-social-proof { … }`); no bare `.card` / `.title` globals.
- I4: Do not alter frozen partials when fixing a neighbor — if cascade bleed is found, fix selector specificity in the **active** section, not frozen SCSS.
- I5: Background / surface switches stay inside section root; do not change `body` background per section task.
- I6: Footer (`site-footer-v2`) is a section partial but lives after `</main>` — preserve that pattern.

---

## 9. RESPONSIVE SURVIVABILITY RULES

### 9.1 Breakpoints (use only these)

| Token | Value | Typical use |
|-------|-------|-------------|
| `$bp-desktop` | **1200px** | H1 size step, desktop grid |
| `$bp-tablet` | **1024px** | Container padding step, section padding step |
| `$bp-mobile` | **768px** | Single-column stack, section padding mobile |
| `$bp-small` | **480px** | Tight stacks, optional type step |

**Main layout switch:** multi-column above **768px** unless section spec says single-column desktop.

### 9.2 Stack and overflow

- R1: **Mobile stack below 768px** for multi-column section grids (`.tm-grid-12` → 1 column at ≤768px).
- R2: **No horizontal overflow** on `html`/`body` at 320, 375, 768, 1024, 1280, 1440px — fix before close.
- R3: Images: `max-width: 100%`, `height: auto` in content; hero background uses `object-fit: cover` with documented `object-position` (hero default **72% center** unless brief overrides).
- R4: Prefer `overflow-x: clip` or `hidden` on section media shells — not on `body` except modal open (existing modal.js pattern).
- R5: Long words / phones: allow `overflow-wrap: anywhere` on narrow columns — do not shrink body below 16px.
- R6: Sticky header: preserve tap targets; verify focused form fields not permanently hidden under fixed chrome (manual check).

### 9.3 When mockup breakpoint is missing

- Collapse to **single column** at 768px.
- Keep CTA full-width stack only if mockup shows it; otherwise keep button intrinsic width with min 40px height.
- Record ambiguity as **SAFE UNKNOWN** — do not invent a third layout variant.

---

## 10. CARD SYSTEM RULES

- K1: `border-radius: 0` on all cards.
- K2: Border: **1px** `var(--tm-border-on-light)` or `$tm-color-border-dark` on dark.
- K3: Padding: **24px** default; **32px** desktop dense content cards; **16px** minimum on mobile.
- K4: Desktop grid cards in one row: **equal min-height** on siblings (`min-height` or flex stretch — pick one per section and keep consistent).
- K5: Card title: Montserrat 500, **18px** or **22px** from scale; `line-height: 1`.
- K6: No card-level box-shadow unless task cites design-system §30 exception (V2 default: **no shadow**).
- K7: Trust / review partner logos: use committed assets under `src/img/reviews/` — no recolor of partner marks.

---

## 11. GRID SYSTEM RULES

- G1: Use `.tm-grid-12` for 12-column layouts: `repeat(12, minmax(0, 1fr))`, gap **24px**.
- G2: At ≤768px: `grid-template-columns: 1fr`, gap **24px** (or **16px** only if already used in that section — do not mix).
- G3: Column spans expressed with `grid-column` on children — no faux columns via floats.
- G4: **No nested 12-column grids** — one grid per content region.
- G5: Flex fallbacks allowed only where grid is unsupported by design (e.g. simple button row); document in REPORT if used.
- G6: Minimum gutter between unrelated content columns: **16px** at mobile, **24px** at desktop.

---

## 12. FORM IMPLEMENTATION RULES

- F1: Inputs / selects: **height 40px**, `border-radius: 0`, **16px** Roboto, `line-height: calc(16px + 4px)`.
- F2: Every control has visible `<label>` associated (`for` / `id`) or `aria-label` for icon-only.
- F3: Error text: **14px**, placed **8px** below field; use `aria-live="polite"` on error container when JS validation exists.
- F4: Submit uses `.btn--primary` — one submit per form.
- F5: **No invented `action` URL** — if endpoint unknown, leave `action` empty or documented placeholder and flag **SAFE UNKNOWN** (no fake production endpoint).
- F6: Required fields marked in HTML (`required` or `aria-required="true"`) consistent with visible UI.
- F7: On mobile, ensure active field scrolls into view (no manual pixel nudge — use `scroll-margin-top` ≤ header height if needed).

---

## 13. JS BEHAVIOR RULES

- J1: **No inline scripts** or `onclick` in partials.
- J2: Init only from `src/js/main.js`; feature code in `src/js/modules/`.
- J3: Hooks: **`data-*` only** for behavior (`data-modal`, `data-modal-open`, `data-modal-close`, `data-accordion`, etc.) — not bare `.btn` selectors.
- J4: **Idempotent init** — safe if `DOMContentLoaded` pattern re-run in dev.
- J5: **Progressive enhancement:** FAQ / legal content visible in HTML without JS; accordions enhance closed state only.
- J6: **No new libraries** without task approval; existing: modal module only unless scope adds accordion/tabs.
- J7: Transitions: **150–200ms** on `color`, `background-color`, `border-color`, `opacity` — **no `transition: all`**.
- J8: Respect `prefers-reduced-motion: reduce` — disable non-essential motion.
- J9: One interaction owner per region (no Swiper + manual scroll on same axis).

---

## 14. FRONTEND QA CHECKLIST

Run before closing a implementation task (check = verifiable).

### Build and scope

- [ ] `npm run build` in `workspaces/triumph-manipulator-landing-v2/` — success or errors listed
- [ ] Changed files ⊆ declared section scope
- [ ] No edits under `dist/`

### Layout and freeze

- [ ] `index.html` section order unchanged (unless unfreeze documented)
- [ ] One `h1`; heading levels sequential in touched partial
- [ ] Container: single `.tm-container` / `--wide` per content stack; no nesting

### Spacing and type

- [ ] Section padding uses 96 / 72 / 56 only (via `.tm-section` or explicit equivalent)
- [ ] Spacing values ∈ {4,8,12,16,20,24,32,40,48,64,96}px
- [ ] `font-size` only from §6 scale; `letter-spacing: 0`
- [ ] No body text < 16px except 12px legal/caption

### Responsive

- [ ] No horizontal scroll at **320, 375, 768, 1024, 1280**px
- [ ] Grids collapse to 1 column ≤768px
- [ ] Primary CTA remains visible and ≥40px tall at 375px

### CTA and components

- [ ] Primary/secondary hierarchy matches §7
- [ ] Buttons use `.btn` variants; border-radius 0

### Assets and icons

- [ ] No placeholder images in production paths
- [ ] Icons from project SVG sprite / committed assets / FA Pro 5.15.4 per [`notes/icon-source-policy.md`](../notes/icon-source-policy.md) — no AI-generated icon SVGs
- [ ] Icon roles checked against FA governance: semantic fidelity, section-local family/style consistency, optical rhythm, and documented brand/custom exceptions

### JS and a11y

- [ ] Critical content not JS-only
- [ ] Focus visible on interactive controls (`:focus-visible` / `$tm-focus-ring`)
- [ ] Modal: `aria-hidden` toggled; body scroll lock only while open

### Regression (when editing near frozen sections)

- [ ] Spot-check adjacent **frozen** sections unchanged at 375px and 1280px

---

## 15. FORBIDDEN IMPLEMENTATION PATTERNS

| ID | Pattern |
|----|---------|
| X1 | Hand-editing `dist/` or committing build output as source of truth |
| X2 | Nested `.tm-container` elements |
| X3 | `margin-top` on section roots for vertical spacing |
| X4 | `border-radius` ≠ 0 on UI components |
| X5 | `font-size` in rem/em/%/clamp; `letter-spacing` ≠ 0 |
| X6 | New brand HEX colors outside design system §5 |
| X7 | Glassmorphism, neumorphism, heavy gradients on surfaces (V2: flat fills; hero overlay only if specified) |
| X8 | Global `!important` waves to fix cascade |
| X9 | Inline `<style>` in HTML partials |
| X10 | Presentational classes as sole JS selectors |
| X11 | Multiple primary red CTAs in one hero/form cluster |
| X12 | Horizontal scroll caused by fixed widths or `100vw` + padding misuse |
| X13 | Lorem ipsum or fake phone numbers presented as production |
| X14 | Rewriting entire page to fix one section |
| X15 | Editing V1 workspace for V2 delivery |
| X16 | Claiming pixel-perfect, Lighthouse, or WCAG audit without evidence |

---

## 16. FREEZE SEMANTICS

| State | Definition | REPORT field |
|-------|------------|--------------|
| **draft** | Structure or layout in progress; not QA-gated | `freeze: draft` |
| **qa-pass** | §14 complete for scope; awaiting human approval | `freeze: qa-pass` |
| **frozen** | Human approved; change requires unfreeze | `freeze: true` |
| **hotfix** | Targeted fix with explicit unfreeze note | `freeze: hotfix-<id>` |

**Freeze includes:** DOM regions, heading map, container tier (standard vs wide), section `padding-block`, CTA variant roles, and grid column intent for that section.

**Freeze excludes:** marketing copy swaps, image file replacements, legal text updates that do not alter structure.

**Anti-drift:** After `frozen: true`, AI tasks default to **read-only** on that partial unless user message contains `unfreeze` or `hotfix` + section name.

---

## 17. VALIDATION CHECKPOINTS

| Gate | When | Pass condition |
|------|------|----------------|
| **G0** | Before coding | Design sources listed; unknowns logged; scope = one section |
| **G1** | After layout + responsive | No horizontal overflow at mandated widths; stack rules pass |
| **G2** | After interaction | Hooks match DOM; init idempotent; PE intact |
| **G3** | Pre-freeze | §14 checklist complete or explicit partial deferrals |
| **G4** | Post-edit near frozen | Adjacent frozen sections spot-check pass |

**Build gate:** `npm run build` exit 0 — required for **G3** when build tooling is available.

**Human gate:** freeze promotion `qa-pass` → `frozen` requires explicit operator approval (not AI self-approve).

---

## 18. SAFE UNKNOWN BOUNDARIES

Do **not** invent production truth for:

| Topic | Allowed AI behavior |
|-------|---------------------|
| Form `action` / CRM endpoint | Markup shell only; flag **SAFE UNKNOWN** |
| NAP / JSON-LD / legal claims | No structured data or certified claims without legal input |
| Final hero copy / pricing | Use task-supplied copy only |
| Pixel-perfect vs mockup | State “not verified” if screens not compared |
| Font delivery (CDN vs local) | Follow existing `head` partial; do not add new CDN without approval |
| FA webfont vs SVG-only | Inspect built output; do not assume |
| Final FA glyph choice for unresolved icon-bearing rows | Use approved source + FA governance; if meaning or availability is unclear, flag **SAFE UNKNOWN** instead of visual approximation |
| Full WCAG / Lighthouse / visual diff | Out of scope unless task supplies tool output |
| Autonomous CI / MARS runtime | **Not claimed** — local Gulp + human review only |

When unknown: **stop**, list missing input, propose smallest compliant stub (e.g. `button type="button"` disabled submit), continue only if task waives.

---

## Changelog

| Date | Change |
|------|--------|
| 2026-05-15 | Initial Forge V2 frontend production rules (documentation only). |
| 2026-05-16 | Added Font Awesome governance authority pointer and icon QA checks. |

---

*End of TRIUMPH FORGE V2 — FRONTEND PRODUCTION RULES*
