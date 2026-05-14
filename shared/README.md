# `shared/` — controlled shared asset layer

This directory holds **operator-approved, implementation-adjacent assets** kept in-repo for **local** frontend and factory-style work. It is **not** a scratch area, **not** a governance source of truth, and **not** part of the MARS runtime (`mars-runtime/`).

## Classification

| Statement | Meaning |
|-----------|---------|
| **Controlled layer** | Contents are intentional; do not treat the tree as disposable clutter or “vendor noise” to delete without an explicit task. |
| **Local / shared dependency posture** | Assets are for **trusted workstations** and **deliberate** project wiring (e.g. icon name lookup, curated SVG export). They are **not** a substitute for project-level `src/` assets in shipped builds. |
| **Licensing-sensitive** | Third-party packs (e.g. Font Awesome Pro) remain subject to **your** license agreement. This README does **not** perform legal review and does **not** authorise redistribution beyond what **you** are entitled to do. |

## `shared/assets/` and `shared/assets/icon-libraries/`

- **`shared/assets/`** — home for shared binary or vendor-adjacent material that multiple frontends or docs may reference under a single canonical path.
- **`shared/assets/icon-libraries/`** — canonical checkout location for **Font Awesome Pro 5.15.4** (folder name: `Font Awesome Pro 5.15.4/`). That tree is an **intentional** icon source for **Website Factory** and landing work, **not** an accidental drop.

## Intended usage

- **Frontend implementation** — align markup and styles with glyphs that exist in the pinned FA build.
- **Icon sourcing and SVG extraction** — discover names and styles locally; ship **only** curated, exported single-icon SVGs (or small hand-built sprites) into each project’s own asset paths.
- **Selective usage** — no wholesale copy of `webfonts/` or full `all.min.css` into `dist/` unless your agreement and deployment policy explicitly allow it.

Operational detail, file layout, and guardrails: [`shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md`](assets/icon-libraries/fontawesome-pro-5.15.4-usage.md).

Per-project rules (example): `projects/triumph-manipulator-landing/notes/icon-source-policy.md`.
