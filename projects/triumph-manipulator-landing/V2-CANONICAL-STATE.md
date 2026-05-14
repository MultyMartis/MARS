# Triumph Manipulator Landing V2 — Frontend workspace state

## 1. What this note is

A short map of **where the V2 landing files live** in this repo: the normal Gulp workspace folder, project-side design references, build output, and the local Font Awesome checkout. **Not** a MARS subsystem, **not** governance, **not** automation or a “platform”.

## 2. Folders

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/`** | **Current** Triumph layout — HTML/SCSS/JS under `src/`. Regular frontend workspace; not a separate architectural layer inside MARS. |
| **`workspaces/triumph-manipulator-landing/`** | **Older / frozen** reference (tag **`triumph-manipulator-v1`** @ `309d81a`). Do not use for new V2 edits. |

## 3. Design references

| Path | Role |
|------|------|
| **`projects/triumph-manipulator-landing/design/`** | Mockups, PDF rules, design-side markdown next to the project pack. |
| **`projects/triumph-manipulator-landing/design-system/triumph-manipulator-design-system.md`** | Written design system (linked from the V2 workspace README). |

## 4. Where to edit implementation

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/src/`** | **Source** — pages, partials, SCSS, JS, images, SVG inputs, favicon. **Edit here**, not in **`dist/`**. |

**Homepage partials (from `src/pages/index.html`):** `hero-conversion`, `machine-specs-transport-lists`, `trust-cases-social-proof`, `segments-applications-grid`, `problem-solution-matrix`, `consultation-lead-form`, `site-footer-v2` — not the older **`landing-strip-*`** chain as the main layout.

## 5. Build output

| Path | Role |
|------|------|
| **`workspaces/triumph-manipulator-landing-v2/dist/`** | **Generated** by `npm run build` / Gulp. Not a hand-editing target. At the **repo root** this tree is **not** on the V2 allow-list — keep it **out** of normal source commits. |

## 6. Shared folder (icons)

| Path | Role |
|------|------|
| **`shared/`** | Local shared files (e.g. Font Awesome checkout). See repo [`README.md`](../../README.md) and [`shared/README.md`](../../shared/README.md). **Not** `mars-runtime/`, **not** governance. |
| **`shared/assets/icon-libraries/`** | Font Awesome Pro tree + [`fontawesome-pro-5.15.4-usage.md`](../../shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md). |

## 7. Font Awesome Pro

**Path:** `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`

- **Use:** local icon name/style reference; copy **selected** SVGs into the project `src/` when needed.  
- **Licensing:** your Font Awesome agreement applies; this note **does not** grant redistribution rights.  
- **Not:** governance, not runtime code, **not** an instruction to commit the whole vendor tree.

More detail: [`shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md`](../../shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md). Example project note: [`notes/icon-source-policy.md`](notes/icon-source-policy.md).

## 8. Legacy strip partials

**`landing-strip-*`** under `workspaces/.../src/` — **continuity** with early mockup-strip scaffolding; **not** today’s main V2 homepage wiring.

**`design/frontend-section-map.md`** — continuity map for mockup → strip placeholders (may still mention the V1 workspace path); read its **Scope** line first.

## 9. Website Factory documentation

**`projects/mars-website-factory/`** is **Markdown-only** process documentation here. It does **not** run this workspace. Use it as vocabulary for handoff; **paths in this file** stay the practical map for files on disk.

## 10. Do not treat as sole truth

- **`web-gpt-sources/chat-migration/*`** — old snapshots; paths may be wrong or stale.  
- Other docs that say “never commit `dist/`” — for V2, root **`.gitignore`** keeps **`dist/`** off the allow-list; use this file + `.gitignore` for what is trackable.  
- Any claim that MARS **automatically** builds or verifies this site — incorrect; work is **local** Gulp + human review.

## 11. Quick answers

| Question | Answer |
|----------|--------|
| Where do I edit the live V2 page? | **`workspaces/triumph-manipulator-landing-v2/src/`** |
| Where are mockups / PDF rules? | **`projects/triumph-manipulator-landing/design/`** (+ design-system doc) |
| Where is Font Awesome Pro on disk? | **`shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`** |
| Where does `npm run build` write? | **`workspaces/.../dist/`** (regenerate locally) |
| Is `shared/` random clutter? | **No** — see [`shared/README.md`](../../shared/README.md). |

## 12. SAFE UNKNOWN

- Whether built pages load FA **webfonts** from `dist/` or rely mostly on the **SVG sprite** — inspect built HTML/CSS when it matters for weight or licensing.  
- Whether every design asset has a twin under `src/img/` — not enumerated here.

## 13. Keeping this file honest

Update this note when paths or the real partial list change. Edits here **do not** change the Gulp pipeline by themselves.

---

*Documentation only — V2 frontend workspace paths.*
