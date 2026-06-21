# Triumph Manipulator Landing V2 — handoff

## Project paths

| Role | Path |
|------|------|
| **V2 frontend workspace (this tree)** | `C:\AI MARS\workspaces\triumph-manipulator-landing-v2` |
| **V1 workspace (locked — do not edit)** | `C:\AI MARS\workspaces\triumph-manipulator-landing` |
| **V1 git tag** | `triumph-manipulator-v1` @ `309d81a` |
| **Project docs / design repo area** | `C:\AI MARS\projects\triumph-manipulator-landing` |

## Mandatory rules files

| Document | Path |
|----------|------|
| Design system (canonical MD) | `C:\AI MARS\projects\triumph-manipulator-landing\design-system\triumph-manipulator-design-system.md` |
| Design folder map (v1 / v2 / shared-assets; isolation rules) | `C:\AI MARS\projects\triumph-manipulator-landing\design\README.md` |
| V2 frontend source of truth + matrices | `C:\AI MARS\projects\triumph-manipulator-landing\V2-FRONTEND-SOURCE-OF-TRUTH.md` (see §4 Design version isolation), `V2-SECTION-SOURCE-MATRIX.md`, `V2-VISUAL-SOURCE-MATRIX.md` |
| Forge V2 production rules | `C:\AI MARS\projects\triumph-manipulator-landing\docs\TRIUMPH-FORGE-V2-FRONTEND-PRODUCTION-RULES.md` |

**Retired:** `TRIUMPH LANDING V2 — DESIGN & FRONTEND RULES.pdf` was removed from `design/` — do not cite as authority ([`V2-CLEANUP-DECISION-LOG.md`](../../projects/triumph-manipulator-landing/V2-CLEANUP-DECISION-LOG.md)).

## Source asset folders (repo)

| Purpose | Path |
|---------|------|
| Design working notes, `mockups-index.md` (V1 slice index), section map, versioned PNG exports (`v1/`, `v2/`) | `C:\AI MARS\projects\triumph-manipulator-landing\design\` |
| Shared reusable visuals (brand, hero, icons, reviews, social) | `C:\AI MARS\projects\triumph-manipulator-landing\design\shared-assets\` |
| Workspace-local design drop (if used) | `C:\AI MARS\workspaces\triumph-manipulator-landing-v2\src\assets\design\` |
| **Font Awesome Pro 5.15.4** (icon source of truth) | `C:\AI MARS\shared\assets\icon-libraries\Font Awesome Pro 5.15.4\` |

## Build commands

Run from the V2 workspace root:

```bash
cd "C:\AI MARS\workspaces\triumph-manipulator-landing-v2"
npm install
npm run build
```

- **`npm run build`** — production Gulp build (`gulp build`).
- **`npm run watch`** — watch mode (`gulp watch`).

## NEXT IMPLEMENTATION RULE (V2 validation)

**Freeze state (2026-05-17):** current rebuilt homepage Screens 01–07 are **READY FOR FREEZE WITH MINOR KNOWN DRIFT**. See [`../../projects/triumph-manipulator-landing/V2-FREEZE-STATE.md`](../../projects/triumph-manipulator-landing/V2-FREEZE-STATE.md).

The completed clean rebuild cycle restored the homepage flow in order from [`../../projects/triumph-manipulator-landing/design/v2/01.png`](../../projects/triumph-manipulator-landing/design/v2/01.png) through `07.png`.

- **Do not** treat the freeze as permission for further polish or redesign.
- **Do not** restart another rebuild unless a new operator-approved production phase is opened.
- **Do not** use **`design/v1/`** as semantic source for V2.
- **Do not** use **`equipment-prices`** on the **homepage** — removed **2026-05-16**; block lives on **`validation-equipment-prices.html`** only ([equipment-prices-quarantine.md](../../projects/triumph-manipulator-landing/design/v2/validation/equipment-prices-quarantine.md)).
- **Do not** invent copy or legal URLs; unresolved URLs remain outside freeze until the real content / legal URL phase.

**Next production phases:** (1) asset replacement, (2) real content / legal URL phase, (3) mobile-first refinement, (4) conversion optimization, (5) optional pixel / overlay QA.

Full rule: [`../../projects/triumph-manipulator-landing/V2-FRONTEND-SOURCE-OF-TRUTH.md`](../../projects/triumph-manipulator-landing/V2-FRONTEND-SOURCE-OF-TRUTH.md) — **NEXT IMPLEMENTATION RULE**.

## AI frontend agent rules (V2)

1. **Read first:** `triumph-manipulator-design-system.md`, **`design/v2/`** PNG exports, [V2-FRONTEND-SOURCE-OF-TRUTH.md](../../projects/triumph-manipulator-landing/V2-FRONTEND-SOURCE-OF-TRUTH.md), [V2-FREEZE-STATE.md](../../projects/triumph-manipulator-landing/V2-FREEZE-STATE.md), and [`design/README.md`](../../projects/triumph-manipulator-landing/design/README.md) before changing layout, copy, or styles.
2. **No border-radius** anywhere unless a human documents an explicit exception in the task.
3. **Typography:** Roboto (body), Montserrat (headings); respect the design system’s sizing units (e.g. `px` for `font-size` where the DS mandates).
4. **Icons:** Font Awesome Pro **5.15.4** only from the shared library path above; **no AI-generated icons**; prefer established extraction/sprite workflow already in this workspace (`tools/`, sprite pipeline) over ad-hoc SVGs.
5. **Conversion:** Primary CTAs = **form** and **phone**. **Do not** ship a **WhatsApp-first** or messenger-primary hero CTA. MAX / Telegram / WhatsApp = **secondary**, **header/footer** only for messenger icons.
6. **Product framing:** V2 = **one specific serious machine for specific tasks**, **not** a fleet narrative. Refactor copy and sections accordingly when implementation starts.
7. **Sources only:** Edit under `src/`; never hand-edit `dist/`.
8. **Do not modify** V1 workspace, `mars-runtime/`, or `projects/seo-content-agent/`.

## Current V2 status

Clean rebuild completed and frozen for handoff: the active homepage flow (`hero-conversion`, `machine-specs-transport-lists`, `trust-cases-social-proof`, `segments-applications-grid`, `problem-solution-matrix`, `consultation-lead-form`, `site-footer-v2`) represents Screens `01` through `07` and is **READY FOR FREEZE WITH MINOR KNOWN DRIFT**. **`equipment-prices`** is **off the homepage** — **EXPERIMENTAL / VALIDATION** on `validation-equipment-prices.html` only ([quarantine doc](../../projects/triumph-manipulator-landing/design/v2/validation/equipment-prices-quarantine.md)).

**Known drift to carry forward:** Screen `01` background raster is not exact canonical asset; Screen `04` image crops are composite-PNG extractions and may show minor raster ghost traces at `768` / `1024`; Screen `06` background crop / raster parity is not final; exact pixel parity, physical device QA, final legal URLs, and production asset replacement are outside this freeze.
