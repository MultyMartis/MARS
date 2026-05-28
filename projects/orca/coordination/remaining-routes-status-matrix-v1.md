# Remaining Routes Status Matrix v1

**Snapshot date:** 2026-05-28  
**Frontend baseline:** `workspaces/triumph-manipulator-landing-v6/`  
**Registry:** `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json`  
**Legend:** `●` done / partial · `○` pending · `?` SAFE UNKNOWN

**Note:** Registry still references v4 Factory paths for some routes — matrix reflects **V6 operational truth** unless operator updates registry.

---

## Summary

| Metric | Count |
|--------|-------|
| Total PPC landing routes (incl. master) | 12 |
| V6 built (in `npm run build`) | 1 (`zakaz` / `index.html`) |
| V6 partial scaffolds present | 11 slugs under `v5-ppc/` |
| ORCA production packs ready for Factory | 0 fully approved (zakaz + 5t draft) |
| Launch-ready | 0 |

---

## Matrix

| route | route_id (registry) | intent | current status | visual semantics | content readiness | frontend readiness | pack readiness | QA status | launch readiness |
|-------|---------------------|--------|----------------|------------------|-------------------|--------------------|----------------|-----------|------------------|
| **zakaz** (master hot) | `zakazat-manipulyator` | Hot general · `grp_fc12` | V6 **production-stable** (mailer MVP) | ● Example bundle (`triumph-zakaz-hero-visual-semantics-v1`) | ● Draft pack `triumph-manipulyator-zakaz-pack-v1` | ● `index.html` built | ○ Draft — `approved_for_factory: false` | ○ D1/D2 drift open; device QA partial | ○ |
| **5-tonn** | `manipulyator-5-tonn` | Capability 5 т · group 01 | Scaffold in V6; v4 dist existed | ○ Route bundle not authored | ● Pack v0 + handoff (v5 paths) | ○ No V6 page HTML; partials exist | ○ Needs V6-aligned pack bump | ○ v5-page01 QA exists — not V6 | ○ |
| **bytovki** | `perevozka-bytovok` | Use-case · group 02 | Scaffold only | ○ | ○ Blueprint only | ○ Partials only | ○ | ○ | ○ |
| **stroymaterialy** | `dostavka-stroymaterialov` | Use-case · group 03 | Scaffold only | ○ | ○ Blueprint only | ○ Partials only | ○ | ○ | ○ |
| **oborudovanie** | `perevozka-oborudovaniya` | Use-case · group 06 | Scaffold only | ○ | ○ Blueprint only | ○ Partials only | ○ | ○ | ○ |
| **yurlic** | `manipulyator-dlya-yurlic` | B2B · group 04 | Scaffold only | ○ | ○ Blueprint only | ○ Partials only | ○ | ○ | ○ |
| **vezdehod** | `manipulyator-vezdehod` | Capability 6×6 · group 05 | Scaffold only | ○ | ○ Blueprint only | ○ Partials only | ○ | ○ | ○ |
| **kray** | `manipulyator-krasnodarskiy-kray` | Geo intercity · group 11 | Scaffold only | ○ | ○ Blueprint only | ○ Partials only | ○ | ○ | ○ |
| **fbs-zhbi** | `fbs-zhbi` | Use-case · group 10 | Scaffold only | ○ | ○ Blueprint | ○ Partials; URL `/perevozka-fbs-zhbi/` | ○ | ○ | ○ |
| **konteynery** | `perevozka-konteynerov` | Use-case · group 07 | Scaffold only | ○ | ○ Blueprint path ? in registry | ○ Partials only | ○ | ○ | ○ |
| **armatura** | `perevozka-armatury` | Use-case · group 08 | Scaffold only | ○ | ○ Blueprint | ○ Partials only | ○ | ○ | ○ |
| **kirpich-bloki** | `dostavka-kirpicha-blokov` | Use-case · group 09 | Scaffold only | ○ | ○ Blueprint | ○ Partials only | ○ | ○ | ○ |

---

## Homepage charter (outside 11)

| Item | Status |
|------|--------|
| `01-master-hot-general.md` on `/` vs zakaz index | **SAFE UNKNOWN** — operator must confirm URL map (rollout plan notes homepage may share zakaz baseline) |
| Separate homepage build | Not in V6 build closure |

---

## Pack and handoff inventory

| Route | Pack artifact | Handoff MD | `approved_for_factory` |
|-------|---------------|------------|------------------------|
| zakaz | `content-packs/examples/triumph-manipulyator-zakaz-pack-v1/` | Missing (mirror 5-ton pattern) | false |
| 5-tonn | `content-packs/examples/triumph-manipulyator-5-tonn-pack-v0.md` | `ppc/.../triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md` | per approval file |
| Others | — | — | — |

---

## QA and launch gates (project-level)

| Gate | Status |
|------|--------|
| `approved_for_commander_import` | Not signed (human) |
| `approved_for_ads` | Pending — page 01 / zakaz |
| `approved_for_launch` | No |
| Live production deploy | **SAFE UNKNOWN** |

---

## Update protocol

After each route pilot:

1. Update row in this matrix (date in commit message if committing later).
2. Sync `landing-route-registry.json` `factory_status` / `handoff_status` when operator confirms.
3. Add REPORT under `workspaces/triumph-manipulator-landing-v6/reports/`.

---

## Related

- [route-priority-roadmap-v1.md](route-priority-roadmap-v1.md)
- `projects/triumph-manipulator-landing/V6-PAGE-ROLLOUT-PLAN.md`
