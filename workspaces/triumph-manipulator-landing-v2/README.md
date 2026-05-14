# Triumph Manipulator Landing — V2 frontend workspace

This folder is the **local working area for Landing V2** (Gulp static frontend), forked as a technical starter from the V1 workspace. **V1 is frozen:** do not change `workspaces/triumph-manipulator-landing/`. The V1 release is pinned at git tag **`triumph-manipulator-v1`** (commit `309d81a`).

## V2 product intent (summary)

V2 is **not** a fleet landing. It communicates **one serious machine for specific tasks**. Conversion priority:

1. **Form submission**
2. **Phone call**
3. **MAX / Telegram / WhatsApp** only as **secondary** channels — messenger icons belong in **header/footer**, not as the primary CTA. **No WhatsApp-first CTA.**

## Mandatory design and frontend rules

All V2 design and frontend work must follow:

| Document | Path |
|----------|------|
| Design system (canonical) | [`../../projects/triumph-manipulator-landing/design-system/triumph-manipulator-design-system.md`](../../projects/triumph-manipulator-landing/design-system/triumph-manipulator-design-system.md) |
| V2 design and frontend rules (PDF) | [`../../projects/triumph-manipulator-landing/design/TRIUMPH LANDING V2 — DESIGN & FRONTEND RULES.pdf`](../../projects/triumph-manipulator-landing/design/TRIUMPH%20LANDING%20V2%20%E2%80%94%20DESIGN%20%26%20FRONTEND%20RULES.pdf) |

Hard constraints from those sources (non-exhaustive checklist):

- **No `border-radius`** (corners stay square).
- **Typography:** Roboto for body text, Montserrat for headings.
- **Icons:** **Font Awesome Pro 5.15.4** as the icon source — see repo [`../../shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`](../../shared/assets/icon-libraries/Font%20Awesome%20Pro%205.15.4/). **No AI-drawn icons.**

## Project documentation

See [`../../projects/triumph-manipulator-landing/README.md`](../../projects/triumph-manipulator-landing/README.md) and [`../../projects/triumph-manipulator-landing/frontend-workspace.md`](../../projects/triumph-manipulator-landing/frontend-workspace.md). **Operator handoff for V2:** [`V2-HANDOFF.md`](V2-HANDOFF.md).

## MARS workspace policy

- Do not commit **build output** or unreviewed **client assets** into MARS without explicit approval.
- Follow [`../../agents/frontend-gulp-agent/`](../../agents/frontend-gulp-agent/) for operational discipline.

---

# Gulp Starter (inherited)

**Universal starter template** — production-ready base for static HTML, SCSS, and JavaScript using `gulp-file-include`. V2 currently **reuses the V1 starter tree** until V2 sections are implemented per the rules above.

## Structure

- `src/pages` — page entry points (`index.html`, `about.html`, `service.html`)
- `src/partials/sections` — large page blocks
- `src/partials/components` — reusable UI parts
- `src/scss` — `base`, `utils`, `layout`, `sections`, `components`
- `src/js/main.js` — initialization entry point
- `src/js/modules` — feature/component logic
- `src/js/utils` — shared helpers when needed
- `dist` — generated output

## Commands

- `npm install`
- `npm run build`
- `npm run watch`

## Rules (starter)

- Edit only `src` for source changes; **`dist` is generated — do not edit `dist` manually.**
- `src/pages` contains only final pages; no partials inline.
- Naming: lowercase, kebab-case; HTML and SCSS names should match (e.g. `hero.html` ↔ `_hero.scss`).
- Layout: structural parts only (`head`, `header`, `footer`, `scripts`).
- JS: `main.js` bootstraps; `modules` hold block logic; prefer `data-*` hooks for behavior.
- SEO: one `h1` per page; sensible heading hierarchy; semantic landmarks.

Progressive enhancement, gallery boundaries, and interaction notes: root **`AGENTS.md`**.
