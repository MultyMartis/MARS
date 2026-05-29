# V6 Image Mapping Pass — Inventory

**Status:** Inventory only — **no markup edits in this pass**  
**Workspace:** `workspaces/triumph-manipulator-landing-v6`  
**Search roots:** `src/img/`, `src/assets/` (vendor only), `design/` (empty in workspace)  
**Date:** 2026-05-29

---

## Asset library summary

### Hero (`src/img/hero/`)

| File | Notes |
|------|--------|
| `hero-bg-final.jpg` | **Current** first-screen image on all 12 routes (page shell `<img>`) |
| `hero-bg-final.png` | Alternate format; not referenced in page HTML |
| `_base.scss` | CSS fallback `background-image: url('../img/hero/hero-bg-final.jpg')` on `.hero--v5` |

### Reconstruction / legacy (`src/img/reconstruction/`)

| File | Possible use |
|------|----------------|
| `v1-02-manipulator-5t.png` | 5-tonn semantic hero candidate |
| `v1-02-manipulator-7t.png` | UNKNOWN route fit |
| `v1-02-manipulator-10t.png` | UNKNOWN route fit |
| `v1-04-contact-truck.png` | Contact / CTA strip (not first-screen) |
| `v2-02-machine.png` | Legacy v4 second-screen (not used in v6 PPC routes) |

### Second screen — dedicated v5 set (`src/img/v5/second-screen/`)

| File | Semantic slug |
|------|----------------|
| `second-screen-index-baseline.jpg` | Generic / fallback |
| `second-screen-zakaz.jpg` | index (`zakaz` prefix) |
| `second-screen-5-tonn.jpg` | 5-tonn |
| `second-screen-bytovki.jpg` | bytovki |
| `second-screen-konteynery.jpg` | konteynery |
| `second-screen-oborudovanie.jpg` | oborudovanie ✓ wired |
| `second-screen-fbs-zhbi.jpg` | fbs-zhbi |
| `second-screen-armatura.jpg` | armatura |
| `second-screen-kirpich-bloki.jpg` | kirpich-bloki |
| `second-screen-stroymaterialy.jpg` | stroymaterialy |
| `second-screen-vezdehod.jpg` | vezdehod ✓ wired |
| `second-screen-yurlic.jpg` | yurlic ✓ wired |
| `second-screen-kray.jpg` | kray ✓ wired |
| `second-screen-test-01.jpg` | v5-page01 test only (not in accepted 12) |

### `src/assets/`

Font Awesome vendor only — no route imagery.

### `design/`

No files in workspace — **SAFE UNKNOWN** for external design drops.

---

## Per-route inventory

Legend — **Alt:** `empty` = `alt=""` on decorative hero bg; `ok` = meaningful alt on second-screen `<img>`; `gap` = missing or generic.

| Route | Page file | Current hero image | Current second-screen image | Expected semantic image (if obvious) | Alt text status | Action needed |
|-------|-----------|-------------------|------------------------------|--------------------------------------|-----------------|---------------|
| **index** | `src/pages/index.html` | `/assets/img/hero/hero-bg-final.jpg` (page shell) | `second-screen-index-baseline.jpg` via `v5-ppc/zakaz/screen-02-specs.html` | Hero: generic OK or `hero-bg-final`; 2nd: `second-screen-zakaz.jpg` | Hero: `empty` (decorative); 2nd: `ok` | Map 2nd screen to `second-screen-zakaz.jpg`; optional hero route variant later |
| **5-tonn** | `src/pages/5-tonn.html` | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-5-tonn.jpg`; hero optional `v1-02-manipulator-5t.png` | Hero: `empty`; 2nd: `ok` (route-specific alt) | Wire `second-screen-5-tonn.jpg` |
| **bytovki** | `src/pages/bytovki.html` | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-bytovki.jpg` | Hero: `empty`; 2nd: `ok` | Wire `second-screen-bytovki.jpg` |
| **konteynery** | `src/pages/konteynery.html` | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-konteynery.jpg` | Hero: `empty`; 2nd: `ok` | Wire `second-screen-konteynery.jpg` |
| **oborudovanie** | `src/pages/oborudovanie.html` | `hero-bg-final.jpg` | `second-screen-oborudovanie.jpg` ✓ | Already aligned | Hero: `empty`; 2nd: `ok` | **None** (2nd screen); optional hero differentiation |
| **fbs-zhbi** | `src/pages/fbs-zhbi.html` | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-fbs-zhbi.jpg` | Hero: `empty`; 2nd: `ok` | Wire `second-screen-fbs-zhbi.jpg` |
| **armatura** | `src/pages/armatura.html` | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-armatura.jpg` | Hero: `empty`; 2nd: `ok` | Wire `second-screen-armatura.jpg` |
| **kirpich-bloki** | `src/pages/kirpich-bloki.html` | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-kirpich-bloki.jpg` | Hero: `empty`; 2nd: `ok` | Wire `second-screen-kirpich-bloki.jpg` |
| **stroymaterialy** | `src/pages/stroymaterialy.html` | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-stroymaterialy.jpg` | Hero: `empty`; 2nd: `ok` | Wire `second-screen-stroymaterialy.jpg` |
| **vezdehod** | `src/pages/vezdehod.html` | `hero-bg-final.jpg` | `second-screen-vezdehod.jpg` ✓ | Already aligned | Hero: `empty`; 2nd: `ok` | **None** (2nd screen); optional hero 6×6 asset if added |
| **yurlic** | `src/pages/yurlic.html` | `hero-bg-final.jpg` | `second-screen-yurlic.jpg` ✓ | Already aligned | Hero: `empty`; 2nd: `ok` | **None** (2nd screen) |
| **kray** | `src/pages/kray.html` | `hero-bg-final.jpg` | `second-screen-kray.jpg` ✓ | Already aligned | Hero: `empty`; 2nd: `ok` | **None** (2nd screen) |

### Partial paths (second screen)

| Route | Second-screen partial |
|-------|------------------------|
| index | `partials/sections/v5-ppc/zakaz/screen-02-specs.html` |
| 5-tonn | `partials/sections/v5-ppc/5-tonn/screen-02-specs.html` |
| bytovki | `partials/sections/v5-ppc/bytovki/screen-02-specs.html` |
| konteynery | `partials/sections/v5-ppc/konteynery/screen-02-specs.html` |
| oborudovanie | `partials/sections/v5-ppc/oborudovanie/screen-02-specs.html` |
| fbs-zhbi | `partials/sections/v5-ppc/fbs-zhbi/screen-02-specs.html` |
| armatura | `partials/sections/v5-ppc/armatura/screen-02-specs.html` |
| kirpich-bloki | `partials/sections/v5-ppc/kirpich-bloki/screen-02-specs.html` |
| stroymaterialy | `partials/sections/v5-ppc/stroymaterialy/screen-02-specs.html` |
| vezdehod | `partials/sections/v5-ppc/vezdehod/screen-02-specs.html` |
| yurlic | `partials/sections/v5-ppc/yurlic/screen-02-specs.html` |
| kray | `partials/sections/v5-ppc/kray/screen-02-specs.html` |

Hero content partials (`screen-01-hero.html`) contain **no** `<img>` — hero visual is page-level `first-screen__bg-media` only.

---

## Mapping pass scope (next step, not this commit)

1. Update `src` in `screen-02-specs.html` only (9 routes on baseline → dedicated file).
2. Rebuild; verify dist copies under `dist/assets/img/v5/second-screen/`.
3. Visual QA per route (mobile + desktop crop).
4. Hero per-route assets — **deferred** unless design supplies 12 variants; shared `hero-bg-final.jpg` is acceptable interim per freeze.

---

## Do not touch

- Orphan `final-contact-cta.html` partials (all routes).
- `dist/` manual edits.
- Route copy / structure.
