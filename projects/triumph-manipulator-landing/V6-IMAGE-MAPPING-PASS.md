# V6 Image Mapping Pass v1

**Status:** Applied — second-screen mapping complete  
**Workspace:** `workspaces/triumph-manipulator-landing-v6`  
**Checkpoint:** `dc05c47` — checkpoint triumph v6 route source reality  
**Date:** 2026-05-29  
**Scope:** Image references only — no copy, layout, CSS, or route structure changes

---

## Phase 1 — Image inventory

### Asset roots

| Root | Contents |
|------|----------|
| `src/img/hero/` | `hero-bg-final.jpg` (active hero on all 12 routes), `hero-bg-final.png` (unused in HTML) |
| `src/img/v5/second-screen/` | 14 route/test portraits (see table below) |
| `src/img/reconstruction/` | Legacy PNGs — not wired in v6 PPC routes |
| `src/assets/` | Font Awesome vendor only |
| `design/` | Empty in workspace — **SAFE UNKNOWN** |

### Second-screen library (`src/img/v5/second-screen/`)

| File | Route slug |
|------|------------|
| `second-screen-zakaz.jpg` | index |
| `second-screen-5-tonn.jpg` | 5-tonn |
| `second-screen-bytovki.jpg` | bytovki |
| `second-screen-konteynery.jpg` | konteynery |
| `second-screen-oborudovanie.jpg` | oborudovanie |
| `second-screen-fbs-zhbi.jpg` | fbs-zhbi |
| `second-screen-armatura.jpg` | armatura |
| `second-screen-kirpich-bloki.jpg` | kirpich-bloki |
| `second-screen-stroymaterialy.jpg` | stroymaterialy |
| `second-screen-vezdehod.jpg` | vezdehod |
| `second-screen-yurlic.jpg` | yurlic |
| `second-screen-kray.jpg` | kray |
| `second-screen-index-baseline.jpg` | Generic fallback — **no longer referenced in 12 routes** |
| `second-screen-test-01.jpg` | v5-page01 test only (outside accepted 12) |

### Per-route inventory (pre-pass → post-pass)

| Route | Current hero image | Current second-screen (before) | Available route-specific images | Recommended image | Confidence |
|-------|-------------------|-------------------------------|--------------------------------|-------------------|------------|
| index | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-zakaz.jpg` | `second-screen-zakaz.jpg` | High |
| 5-tonn | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-5-tonn.jpg` | `second-screen-5-tonn.jpg` | High |
| bytovki | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-bytovki.jpg` | `second-screen-bytovki.jpg` | High |
| konteynery | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-konteynery.jpg` | `second-screen-konteynery.jpg` | High |
| oborudovanie | `hero-bg-final.jpg` | `second-screen-oborudovanie.jpg` ✓ | `second-screen-oborudovanie.jpg` | KEEP | High |
| fbs-zhbi | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-fbs-zhbi.jpg` | `second-screen-fbs-zhbi.jpg` | High |
| armatura | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-armatura.jpg` | `second-screen-armatura.jpg` | High |
| kirpich-bloki | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-kirpich-bloki.jpg` | `second-screen-kirpich-bloki.jpg` | High |
| stroymaterialy | `hero-bg-final.jpg` | `second-screen-index-baseline.jpg` | `second-screen-stroymaterialy.jpg` | `second-screen-stroymaterialy.jpg` | High |
| vezdehod | `hero-bg-final.jpg` | `second-screen-vezdehod.jpg` ✓ | `second-screen-vezdehod.jpg` | KEEP | High |
| yurlic | `hero-bg-final.jpg` | `second-screen-yurlic.jpg` ✓ | `second-screen-yurlic.jpg` | KEEP | High |
| kray | `hero-bg-final.jpg` | `second-screen-kray.jpg` ✓ | `second-screen-kray.jpg` | KEEP | High |

Hero partials (`screen-01-hero.html`) contain no `<img>` — hero visual is page-level `first-screen__bg-media` only.

---

## Phase 2 — Mapping decisions

| Route | Second screen | Hero | Reason |
|-------|---------------|------|--------|
| index | **REPLACE** → `second-screen-zakaz.jpg` | **KEEP** `hero-bg-final.jpg` | Dedicated zakaz asset exists; semantics match index |
| 5-tonn | **REPLACE** → `second-screen-5-tonn.jpg` | **KEEP** | Dedicated 5-tonn asset exists |
| bytovki | **REPLACE** → `second-screen-bytovki.jpg` | **KEEP** | Dedicated bytovki asset exists |
| konteynery | **REPLACE** → `second-screen-konteynery.jpg` | **KEEP** | Dedicated konteynery asset exists |
| oborudovanie | **KEEP** | **KEEP** | Already mapped |
| fbs-zhbi | **REPLACE** → `second-screen-fbs-zhbi.jpg` | **KEEP** | Dedicated FBS/ЖБИ asset exists |
| armatura | **REPLACE** → `second-screen-armatura.jpg` | **KEEP** | Dedicated armatura asset exists |
| kirpich-bloki | **REPLACE** → `second-screen-kirpich-bloki.jpg` | **KEEP** | Dedicated kirpich-bloki asset exists |
| stroymaterialy | **REPLACE** → `second-screen-stroymaterialy.jpg` | **KEEP** | Dedicated stroymaterialy asset exists |
| vezdehod | **KEEP** | **KEEP** | Already mapped |
| yurlic | **KEEP** | **KEEP** | Already mapped |
| kray | **KEEP** | **KEEP** | Already mapped |

Hero per-route differentiation **deferred** — no dedicated hero set in `src/img/hero/` beyond shared `hero-bg-final.jpg`. Reconstruction PNGs not wired (legacy / unverified semantics).

---

## Phase 3 — Applied changes

### Mapping log

| Route | Old image | New image | Reason | Status |
|-------|-----------|-----------|--------|--------|
| index | `second-screen-index-baseline.jpg` | `second-screen-zakaz.jpg` | Route-specific zakaz portrait available | **Applied** |
| 5-tonn | `second-screen-index-baseline.jpg` | `second-screen-5-tonn.jpg` | Route-specific 5-tonn portrait available | **Applied** |
| bytovki | `second-screen-index-baseline.jpg` | `second-screen-bytovki.jpg` | Route-specific bytovki portrait available | **Applied** |
| konteynery | `second-screen-index-baseline.jpg` | `second-screen-konteynery.jpg` | Route-specific konteynery portrait available | **Applied** |
| oborudovanie | `second-screen-oborudovanie.jpg` | *(unchanged)* | Already correct | **KEEP** |
| fbs-zhbi | `second-screen-index-baseline.jpg` | `second-screen-fbs-zhbi.jpg` | Route-specific FBS/ЖБИ portrait available | **Applied** |
| armatura | `second-screen-index-baseline.jpg` | `second-screen-armatura.jpg` | Route-specific armatura portrait available | **Applied** |
| kirpich-bloki | `second-screen-index-baseline.jpg` | `second-screen-kirpich-bloki.jpg` | Route-specific kirpich-bloki portrait available | **Applied** |
| stroymaterialy | `second-screen-index-baseline.jpg` | `second-screen-stroymaterialy.jpg` | Route-specific stroymaterialy portrait available | **Applied** |
| vezdehod | `second-screen-vezdehod.jpg` | *(unchanged)* | Already correct | **KEEP** |
| yurlic | `second-screen-yurlic.jpg` | *(unchanged)* | Already correct | **KEEP** |
| kray | `second-screen-kray.jpg` | *(unchanged)* | Already correct | **KEEP** |

All routes: hero **KEEP** `/assets/img/hero/hero-bg-final.jpg` (page shell).

### Files changed

| File | Change |
|------|--------|
| `src/partials/sections/v5-ppc/zakaz/screen-02-specs.html` | `src` → `second-screen-zakaz.jpg` |
| `src/partials/sections/v5-ppc/5-tonn/screen-02-specs.html` | `src` → `second-screen-5-tonn.jpg` |
| `src/partials/sections/v5-ppc/bytovki/screen-02-specs.html` | `src` → `second-screen-bytovki.jpg` |
| `src/partials/sections/v5-ppc/konteynery/screen-02-specs.html` | `src` → `second-screen-konteynery.jpg` |
| `src/partials/sections/v5-ppc/fbs-zhbi/screen-02-specs.html` | `src` → `second-screen-fbs-zhbi.jpg` |
| `src/partials/sections/v5-ppc/armatura/screen-02-specs.html` | `src` → `second-screen-armatura.jpg` |
| `src/partials/sections/v5-ppc/kirpich-bloki/screen-02-specs.html` | `src` → `second-screen-kirpich-bloki.jpg` |
| `src/partials/sections/v5-ppc/stroymaterialy/screen-02-specs.html` | `src` → `second-screen-stroymaterialy.jpg` |

---

## Phase 4 — ALT QA

Audited all 12 `screen-02-specs.html` second-screen `<img alt="...">` values.

| Route | Alt text | Action |
|-------|----------|--------|
| index | Манипулятор 5 т на объекте в Краснодаре | **KEEP** — route-specific, commercial |
| 5-tonn | Манипулятор 5 тонн с крановой установкой на объекте в Краснодаре | **KEEP** |
| bytovki | Манипулятор при перевозке бытовки в Краснодаре | **KEEP** |
| konteynery | Манипулятор перевозит контейнер и разгружает его стрелой на площадке в Краснодаре | **KEEP** |
| oborudovanie | Манипулятор аккуратно перевозит оборудование… | **KEEP** |
| fbs-zhbi | Манипулятор доставляет ФБС и ЖБИ… | **KEEP** |
| armatura | Манипулятор доставляет арматуру… | **KEEP** |
| kirpich-bloki | Манипулятор доставляет кирпич и блоки… | **KEEP** |
| stroymaterialy | Манипулятор доставляет стройматериалы… | **KEEP** |
| vezdehod | Манипулятор-вездеход 6×6 на строительном объекте… | **KEEP** |
| yurlic | Манипулятор на строительном объекте… для организации | **KEEP** |
| kray | Манипулятор на маршруте по Краснодарскому краю… | **KEEP** |

No generic alts found (`Image`, `Photo`, `Truck`). **No alt edits required.**

Hero bg uses `alt=""` (decorative) — unchanged per scope.

---

## Phase 5 — Build verification

```text
npm run build  →  exit 0  (gulp build, 2026-05-29)
```

All 14 second-screen JPGs present in `dist/assets/img/v5/second-screen/`.  
No `second-screen-index-baseline.jpg` references in built HTML.

---

## Phase 6 — Route verification

| Check | Result |
|-------|--------|
| 12 routes exist in `dist/` | **PASS** — index, 5-tonn, bytovki, konteynery, oborudovanie, fbs-zhbi, armatura, kirpich-bloki, stroymaterialy, vezdehod, yurlic, kray |
| One `id="contacts"` per route | **PASS** — count = 1 on each HTML file |
| No `.hero__notice` | **PASS** — none in dist |
| No mock handlers | **PASS** — none in dist html/js |
| No `send.php` references | **PASS** — none in dist |

Dist second-screen slug per route: zakaz, 5-tonn, bytovki, konteynery, oborudovanie, fbs-zhbi, armatura, kirpich-bloki, stroymaterialy, vezdehod, yurlic, kray — all route-specific.

---

## Remaining unmapped routes

| Layer | Status |
|-------|--------|
| Second screen (12 routes) | **Fully mapped** — no route still on baseline |
| Hero (12 routes) | **Shared** `hero-bg-final.jpg` on all — intentional KEEP; no per-route hero library |
| `second-screen-index-baseline.jpg` | Orphan asset (still copied to dist, unused in markup) |
| `src/img/reconstruction/*.png` | Not mapped — legacy candidates, semantics unverified |
| `design/` | Empty — external design drops unknown |

---

## Regression risks

1. **Crop / focal point** — route-specific portraits may crop differently under `_screen-02-prices.scss` cover rules on mobile vs desktop; human visual QA recommended.
2. **Hero homogeneity** — all routes still share one hero photo; acceptable per freeze but weak route differentiation on first screen.
3. **Orphan baseline asset** — `second-screen-index-baseline.jpg` remains in bundle until explicitly pruned (out of scope).

---

## SAFE UNKNOWN

- **`design/`** — no files in workspace; cannot confirm external design inventory.
- **Visual QA** — pixel-level crop/focal review not performed in this pass (build + reference audit only).
- **Reconstruction PNGs** — `v1-02-manipulator-5t.png` may suit 5-tonn hero but not wired; 7t/10t route fit unknown.
- **Hero per-route pass** — deferred until dedicated hero assets supplied or approved from reconstruction set.

---

## Do not touch (unchanged)

- Route copy, headings, SEO, forms, CTA, FAQ
- CSS architecture, layout, spacing, route structure, mailer
- Orphan `final-contact-cta.html` partials
- Manual `dist/` edits (regenerated via build)

**NO COMMIT. NO PUSH.**
