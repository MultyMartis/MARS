# Calibration Loop v1 — Triumph Master Hot (zakaz)

**Loop ID:** `triumph-manipulator-calibration-loop-v1`  
**Date opened:** 2026-05-28  
**Status:** `draft`  
**Operator:** Assisted documentation pass (repo evidence)

## Scope

| In scope | Out of scope |
|----------|--------------|
| Master hot index (`/`) — zakaz partials in v5 | 11 use-case / capability slugs (scaling rules only) |
| Hero v5 redesign vs ORCA blueprint + legacy v4 | Live Yandex metrics |
| PPC group 12 ads in `triumph-s-tier-draft-v1.json` | Editing workspace files |
| Semantic lock vs as-built copy | `approved_for_ads` sign-off |

## Evidence map

| Layer | Primary artifact |
|-------|------------------|
| ORCA research / blueprint | `projects/orca/ppc/triumph-manipulator/landing-pages/01-master-hot-general.md` |
| PPC instance | `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` → `grp_fc12_zakaz` |
| Content pack (cousin) | `projects/orca/content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md` |
| Handoff | **NONE for zakaz** — 5-ton handoff used as structural pattern only |
| Factory as-built (canonical v6) | `workspaces/triumph-manipulator-landing-v6/src/pages/index.html` |
| Hero partial | `workspaces/triumph-manipulator-landing-v6/src/partials/sections/v5-ppc/zakaz/screen-01-hero.html` |
| Hero SCSS | `workspaces/triumph-manipulator-landing-v6/src/scss/sections/_v5-hero-extensions.scss` |
| Legacy anti-pattern | `workspaces/triumph-manipulator-landing-v4/src/partials/sections/screen-01-hero.html` |
| Factory QA reports (v5 era, historical) | `workspaces/triumph-manipulator-landing-v5/reports/v5-baseline-audit-v1.md`, `v5-production-hardening-audit-v1.md` |

## Loop questions (answered in subfolders)

1. What drifted between ORCA blueprint and v5 zakaz hero?
2. Why was legacy v4 hero insufficient — why does v5 work better?
3. What PPC continuity survived implementation?
4. What did Factory need from ORCA but not receive?
5. What scales to the other 11 pages unchanged vs per-route?

## Deliverables

All `*-v1.md` files in parent subfolders — see [../README.md](../README.md).

## Next loop trigger

Open **loop v2** when any of:

- Dedicated `triumph-manipulator-v5-master-hot-handoff.md` is approved
- Hero structure changes materially (v2 partial)
- Group 12 ads lock new primary H1 strategy
