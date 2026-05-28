# Triumph Manipulator Landing V6

**Canonical production base** for multi-page PPC rollout (one page at a time).

## Lineage

| Workspace | Role |
|-----------|------|
| **V6** (`workspaces/triumph-manipulator-landing-v6/`) | Active rollout base — edit here |
| **V5** (`workspaces/triumph-manipulator-landing-v5/`) | Historical stable source (mailer MVP final) — reference only |
| Snapshot | `workspaces/_snapshots/snap-20260528-triumph-v5-mailer-mvp-final-stable/` — frozen recovery point |

V6 was copied from V5 mailer MVP final stable state (2026-05-28). Visuals, forms, and JS behavior are unchanged at bootstrap.

## Rules (operators / agents)

**Single source of truth:** [`projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md`](../../projects/triumph-manipulator-landing/TRIUMPH-V6-CURRENT-FRONTEND-RULES.md)

**Rollout plan:** [`projects/triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md`](../../projects/triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md)

## Build discipline

- Edit **`src/`** only — never hand-edit **`dist/`**.
- Build: `npm run build` → output under `dist/`.
- Forms POST to **`backend/send-lead.php`** (copied to `dist/backend/` on build).
- Main layout breakpoint: **1024 / 1025**. Header nav breakpoint: **1490** (if present). Do not introduce **980 / 981** breakpoints on new work.

## Canonical page (baseline)

`src/pages/index.html` — **zakaz** PPC page (`v5-ppc/zakaz/*` partials). All new pages start from this structure until individually replaced.

## Commands

```bash
npm install   # first time or after toolchain change
npm run build
```

Local preview: `file:///…/workspaces/triumph-manipulator-landing-v6/dist/index.html`

## Reports

Pass reports live under `reports/` per task. Do not treat `dist/` as durable source.
