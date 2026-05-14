# Triumph Manipulator Landing V2 — handoff

## Project paths

| Role | Path |
|------|------|
| **V2 frontend workspace (this tree)** | `D:\AI MARS\workspaces\triumph-manipulator-landing-v2` |
| **V1 workspace (locked — do not edit)** | `D:\AI MARS\workspaces\triumph-manipulator-landing` |
| **V1 git tag** | `triumph-manipulator-v1` @ `309d81a` |
| **Project docs / design repo area** | `D:\AI MARS\projects\triumph-manipulator-landing` |

## Mandatory rules files

| Document | Path |
|----------|------|
| Design system (canonical MD) | `D:\AI MARS\projects\triumph-manipulator-landing\design-system\triumph-manipulator-design-system.md` |
| V2 design & frontend rules (PDF) | `D:\AI MARS\projects\triumph-manipulator-landing\design\TRIUMPH LANDING V2 — DESIGN & FRONTEND RULES.pdf` |

**Note:** The PDF lives under `projects/triumph-manipulator-landing/design/`, not under `design-system/`.

## Source asset folders (repo)

| Purpose | Path |
|---------|------|
| Design working notes, mockups index, section map | `D:\AI MARS\projects\triumph-manipulator-landing\design\` |
| Design assets (brand, hero, icons, reviews, social) | `D:\AI MARS\projects\triumph-manipulator-landing\design\assets\` |
| Workspace-local design drop (if used) | `D:\AI MARS\workspaces\triumph-manipulator-landing-v2\src\assets\design\` |
| **Font Awesome Pro 5.15.4** (icon source of truth) | `D:\AI MARS\shared\assets\icon-libraries\Font Awesome Pro 5.15.4\` |

## Build commands

Run from the V2 workspace root:

```bash
cd "D:\AI MARS\workspaces\triumph-manipulator-landing-v2"
npm install
npm run build
```

- **`npm run build`** — production Gulp build (`gulp build`).
- **`npm run watch`** — watch mode (`gulp watch`).

## AI frontend agent rules (V2)

1. **Read first:** `triumph-manipulator-design-system.md` and the V2 PDF before changing layout, copy, or styles.
2. **No border-radius** anywhere unless a human documents an explicit exception in the task.
3. **Typography:** Roboto (body), Montserrat (headings); respect the design system’s sizing units (e.g. `px` for `font-size` where the DS mandates).
4. **Icons:** Font Awesome Pro **5.15.4** only from the shared library path above; **no AI-generated icons**; prefer established extraction/sprite workflow already in this workspace (`tools/`, sprite pipeline) over ad-hoc SVGs.
5. **Conversion:** Primary CTAs = **form** and **phone**. **Do not** ship a **WhatsApp-first** or messenger-primary hero CTA. MAX / Telegram / WhatsApp = **secondary**, **header/footer** only for messenger icons.
6. **Product framing:** V2 = **one specific serious machine for specific tasks**, **not** a fleet narrative. Refactor copy and sections accordingly when implementation starts.
7. **Sources only:** Edit under `src/`; never hand-edit `dist/`.
8. **Do not modify** V1 workspace, `mars-runtime/`, or `projects/seo-content-agent/`.

## Current V2 status

**Workspace initialized** from V1 as a technical Gulp starter; **V2-specific design and section implementation not started** (content and structure still reflect V1 until a scoped build task runs).
