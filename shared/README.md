# `shared/` — shared local files

This folder holds **local shared files** for frontends on this machine (for example a Font Awesome Pro checkout used for icon lookup). It is **not** a scratch dump, **not** governance truth, and **not** part of `mars-runtime/`.

## Classification

| Statement | Meaning |
|-----------|---------|
| **Controlled use** | Contents are intentional; do not delete paths here casually without a task. |
| **Local / selective** | For **trusted workstations** and deliberate wiring (icon names, curated SVG export into a project `src/`). **Not** a substitute for normal project assets in shipped HTML. |
| **Licensing-sensitive** | Third-party packs (e.g. Font Awesome Pro) remain subject to **your** license agreement. This README does **not** perform legal review and does **not** authorise redistribution beyond what **you** are entitled to do. |

## `shared/assets/` and `shared/assets/icon-libraries/`

- **`shared/assets/`** — shared binaries or vendor trees that several frontends may reference from one path.  
- **`shared/assets/icon-libraries/`** — local checkout of **Font Awesome Pro 5.15.4** (folder name `Font Awesome Pro 5.15.4/`). **Intentional** icon reference for landing work; **not** an accidental drop.

## Intended usage

- **Frontend implementation** — align markup and styles with glyphs that exist in the pinned FA build.
- **Icon sourcing and SVG extraction** — discover names and styles locally; ship **only** curated, exported single-icon SVGs (or small hand-built sprites) into each project’s own asset paths.
- **Selective usage** — no wholesale copy of `webfonts/` or full `all.min.css` into `dist/` unless your agreement and deployment policy explicitly allow it.

Operational detail, file layout, and guardrails: [`shared/assets/icon-libraries/fontawesome-pro-5.15.4-usage.md`](assets/icon-libraries/fontawesome-pro-5.15.4-usage.md).

Per-project rules (example): `projects/triumph-manipulator-landing/notes/icon-source-policy.md`.
