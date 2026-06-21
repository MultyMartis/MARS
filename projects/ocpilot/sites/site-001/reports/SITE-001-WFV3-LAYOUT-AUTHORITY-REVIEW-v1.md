# REPORT — SITE-001 WF-V3 LAYOUT AUTHORITY REVIEW

**Type:** Layout authority audit — documentation only  
**Date:** 2026-06-13  
**Site:** SITE-001 — Автосалон СИБКАР  
**Program:** Website Factory · WF-V3  
**Trigger:** HITL-review WF-V3 PDP — архитектурный дефект inner-zone grid при уже замороженном container contract (WF-GRID-DISCIPLINE)

**Explicit exclusions (honored):** No OpenCart · No TEST · No FTP · No Twig · No CSS · No JS · No prototype changes · No implementation · No commit implied

**Evidence sources (read-only):**

| Source | Path | Role |
|--------|------|------|
| WF-V3 PDP Prototype | `workspaces/site-001-wf-v3-pdp-prototype/` | Implemented layout patterns |
| WF-V3 Homepage Prototype | `workspaces/site-001-wf-v3-homepage-prototype/` | Homepage layout patterns |
| Container discipline | `workspaces/site-001-wf-v3-pdp-prototype/docs/CONTAINER-GRID-DISCIPLINE-v1.md` | Outer grid contract |
| Foundation grid rule | `workspaces/website-factory-reference-v1/frontend-rules/WF-GRID-DISCIPLINE-v1.md` | Section/container separation (promoted) |
| PDP design freeze | `projects/ocpilot/sites/site-001/governance/SITE-001-WFV3-PDP-DESIGN-AUTHORITY-FREEZE-v1.md` | Frozen 65/35 hero **concept** |
| Homepage blueprint | `projects/ocpilot/sites/site-001/reports/SITE-001-WFV3-HOMEPAGE-BLUEPRINT-v1.md` | Planned homepage zones |

**Scope:** Только layout-архитектура и grid-система. Цвета, фото, контент — **вне scope**.

---

## Executive Summary

WF-GRID-DISCIPLINE закрывает **outer container contract** (`1280px` max, `24px` pad, section ≠ container). Это **не** решает **inner-zone layout authority** — как делить пространство **внутри** контейнера между gallery/offer, card columns, credit panels, trust items.

Аудит выявил **смешанные и несогласованные модели** inner grid:

| Zone | Current model | Consistency |
|------|---------------|-------------|
| PDP Hero | `65%` / `35%` + `40px` gap | **DEFECT** — percentage + gap |
| Homepage Hero | `1fr` / `42%` + `40px` gap | **DEFECT** — hybrid, ≠ PDP |
| Credit Block | `5fr` / `7fr` | Stable fr ratio |
| Featured Inventory | `repeat(4, 1fr)` | Stable equal columns |
| Trust Row | `flex` + `flex: 1` | Stable equal flex, ≠ grid elsewhere |
| Equipment / Banks | `repeat(N, 1fr)` | Stable equal columns |

**Container discipline — READY.** **Inner zone authority — NOT READY** для freeze WF-V3.

---

## Container Baseline (already authoritative)

| Parameter | Value | Authority |
|-----------|-------|-----------|
| `--wf-v3-container-max` | `1280px` | `_utilities.scss` / tokens |
| `--wf-v3-container-pad` | `24px` desktop · `16px` ≤767px | `_utilities.scss` |
| Effective inner content width (desktop) | `1280 − 48 = 1232px` | CONTAINER-GRID-DISCIPLINE-v1 |
| Section/container split | Section shell → inner `.wf-v3-container` | WF-GRID-DISCIPLINE v1 (Foundation) |

**Verdict:** Outer grid **PASS** — не предмет данного review, кроме как baseline для расчётов inner zones.

---

## 1. PDP Hero Grid

### 1.1 Current model

| Property | Value | Source |
|----------|-------|--------|
| Selector | `.wf-v3-pdp-hero__grid` | `_pdp-hero.scss` |
| `display` | `grid` | |
| `grid-template-columns` | `65%` `35%` | tokens `$hero-gallery-ratio` / `$hero-offer-ratio` |
| `gap` | `40px` (`$space-8`) | |
| `align-items` | `start` | |
| Nested offer grids | CTA `repeat(3, 1fr)` · specs `repeat(3, 1fr)` | offer column internals |
| Responsive | **None in prototype** | desktop-only |

**Computed desktop geometry (1232px inner width):**

| Track | Formula | Approx px |
|-------|---------|-----------|
| Gallery | `65% × 1232` | **~801px** |
| Offer | `35% × 1232` | **~431px** |
| Gap | fixed | **40px** |
| **Sum** | | **~1272px > 1232px** |

Percentage tracks суммируются в `100%` контейнера, **gap добавляется сверху** — типичный CSS Grid overflow / implicit shrink. Абсолютные ширины gallery и offer **плавают** при любом изменении container max, pad или gap.

### 1.2 Pros

| # | Pro | Note |
|---|-----|------|
| P1 | Семантически совпадает с frozen concept **65/35** | Design freeze § Hero 65/35 |
| P2 | Простота чтения ratio в tokens | `$hero-gallery-ratio: 65%` |
| P3 | Gallery доминирует визуально | Соответствует P-01 car first |
| P4 | Offer column узкая — price/CTA фокус справа | Соответствует frozen reading flow |

### 1.3 Cons

| # | Con | Severity |
|---|-----|----------|
| C1 | **Percentage + gap arithmetic conflict** — tracks + gap > 100% inner width | **CRITICAL** |
| C2 | Абсолютная ширина gallery/offer **зависит от container math**, не от design intent | **HIGH** |
| C3 | Offer ~431px при 3-col CTA → ~135px/button — риск переноса CTA (RU labels) | **HIGH** |
| C4 | Offer ~431px при 3-col specs — риск переноса label/value | **MEDIUM** |
| C5 | Нет `min-width` floor на offer column | **HIGH** |
| C6 | Нет responsive stack authority | **MEDIUM** (SAFE UNKNOWN mobile) |
| C7 | Повторяет класс ошибки WF-V2 **layout drift** — cosmetic tweak container/gap меняет hero geometry | **CRITICAL** |

### 1.4 Model variants

| Model | Example | Gallery @1232px | Offer @1232px | Gap handling | Drift risk |
|-------|---------|-----------------|---------------|--------------|------------|
| **A — Percentage** (current) | `65% 35%` + `40px` gap | ~801px | ~431px | **Broken** — overflow | **HIGH** |
| **B — Fraction** | `13fr 7fr` (≈65/35) + `40px` gap | ~748px | ~444px | **Correct** — fr absorbs gap | **LOW** |
| **C — Fixed-zone** | `minmax(0, 1fr) minmax(360px, 420px)` | remainder | **360–420px floor** | Explicit min on offer | **LOW** |
| **D — Fixed-zone (gallery-led)** | `minmax(720px, 1fr) minmax(360px, 35%)` | min 720px | min 360px | Design-led px floors | **LOWEST** for CTA stability |

**Fraction math (Model B):** available = `1232 − 40 = 1192px` → gallery `1192 × 13/20 ≈ 775px`, offer `1192 × 7/20 ≈ 417px`.

### 1.5 Recommendation (PDP Hero)

| Item | Recommendation |
|------|----------------|
| **Preserve** | Conceptual **65/35 visual ratio** (frozen design authority) |
| **Replace** | Percentage implementation → **fr ratio tokens** (`13fr 7fr` or named `$hero-gallery-fr: 13`, `$hero-offer-fr: 7`) |
| **Add** | Offer column **`minmax(360px, …)` floor** — защита 3-col CTA/specs |
| **Add** | Document **responsive stack breakpoint** before freeze (currently SAFE UNKNOWN) |
| **Do not** | Менять 65/35 **proportion intent** без authority review |

---

## 2. Homepage Hero

### 2.1 Current model (homepage prototype v0.1)

| Property | Value | Source |
|----------|-------|--------|
| Selector | `.wf-v3-home-hero__inner` | `_homepage-hero.scss` |
| `grid-template-columns` | `1fr` `42%` | **≠ PDP model** |
| `gap` | `40px` | |
| Search fields | `repeat(4, 1fr)` inside left column | nested grid |
| Visual column | photo + 3 fleet thumbs (`flex: 1` each) | right ~42% |

**Computed desktop geometry:**

| Track | Approx px @1232px inner |
|-------|-------------------------|
| Visual (42%) | **~517px** |
| Content (`1fr` remainder after 42% + gap) | **~675px** |
| Gap | **40px** |

### 2.2 Future risk assessment

| Risk | Likelihood | Impact | Evidence |
|------|------------|--------|----------|
| **Repeat PDP percentage defect** on homepage | **HIGH** if copied from PDP tokens | Hero/search geometry drift | Homepage uses **different** hybrid `1fr`/`42%` — already inconsistent |
| Search 4-col grid inside narrow left column | MEDIUM | Field truncation @ smaller viewports | 675px − search pad → ~627px / 4 ≈ 157px field |
| H2/H3 overlap geometry undefined in blueprint | HIGH | First-screen cluster unstable | Blueprint §12 UNKNOWN |
| Same container, different split logic vs PDP | **CONFIRMED** | Brand sibling test failure | PDP `%/%` vs Homepage `fr/%` |

### 2.3 Recommendation (Homepage Hero)

| Item | Recommendation |
|------|----------------|
| **Do not** inherit PDP `65%/35%` — homepage ≠ offer column layout (blueprint: no 65/35 on H2) |
| **Do** define homepage hero under **same inner-zone authority doc** as PDP |
| **Prefer** `7fr 5fr` or `minmax(0, 1fr) minmax(480px, 42%)` — explicit visual column min for car photography |
| **Document** search field grid as **2×2 below breakpoint** or **4-col only when content column ≥ N px** |
| **Block homepage freeze** until hero split model is written in Layout Authority (not ad-hoc SCSS) |

---

## 3. Featured Inventory Grid

### 3.1 Current model

| Property | Value | Source |
|----------|-------|--------|
| Selector | `.wf-v3-featured__grid` | `_featured-inventory.scss` |
| `grid-template-columns` | `repeat(4, 1fr)` | fixed 4 columns |
| `gap` | `20px` (`$space-5`) | |
| Card photo | `aspect-ratio: 16/10` | stable card height from width |

**Computed card width @1232px:** `(1232 − 60) / 4 ≈ **293px**` per card.

### 3.2 Authority options

| Model | Use case | Drift risk | WF-V3 fit |
|-------|----------|------------|-----------|
| **Fixed N + equal fr** (current) | Homepage featured (4 cards), banks (8 logos) | LOW within fixed N; card px floats with container | **RECOMMENDED** for curated rows |
| **auto-fit / minmax** | Catalog listing, unknown card count | MEDIUM — column count changes with viewport | **Catalog only** — future charter |
| **Fixed px columns** | Strict card width (e.g. 280px cards) | LOW for cards; may leave orphan space | Optional catalog variant |

### 3.3 Recommendation (Featured Inventory)

| Item | Recommendation |
|------|----------------|
| **Authority** | **`repeat(N, minmax(0, 1fr))`** with **documented N per zone** |
| Homepage featured | **N = 4** desktop (frozen in blueprint §6) |
| Catalog (future) | **Separate rule:** `repeat(auto-fill, minmax(280px, 1fr))` — not on homepage |
| **Add** | Card **min-width floor** (~260px) — below that, reduce N or stack |
| **Do not** | Use percentage column widths for card grids |

---

## 4. Credit Block Layout

### 4.1 Current model

| Property | Value | Source |
|----------|-------|--------|
| Selector | `.wf-v3-credit__inner` | `_credit-block.scss` |
| `grid-template-columns` | `5fr` `7fr` | ratio 5:12 / 7:12 |
| `gap` | `48px` (`$space-9`) | |
| Panel divider | `padding-left: 48px` + `border-left` | reduces form usable width |
| Form grid | `repeat(2, 1fr)` | inside 7fr panel |

**Computed desktop geometry @1232px:**

| Zone | Approx px |
|------|-----------|
| Head (5fr) | `(1232−48) × 5/12 ≈ **493px**` |
| Panel (7fr) | `(1232−48) × 7/12 ≈ **691px**` |
| Panel content (after pad-left 48) | **~643px** |

### 4.2 Drift risk

| Factor | Assessment |
|--------|------------|
| **fr model vs gap** | **LOW risk** — fr correctly accounts for gap |
| **5:7 ratio stability** | **LOW** — ratio preserved across container widths |
| **Panel padding-left 48px** | **MEDIUM** — shinks form area; couples to 7fr absolute width |
| **Cross-page consistency** | **PASS** — identical in PDP and Homepage prototypes |
| **vs PDP hero % model** | **INCONSISTENT** — credit uses fr, hero uses % |

### 4.3 Recommendation (Credit Block)

| Item | Recommendation |
|------|----------------|
| **Keep** | `5fr 7fr` as **reference pattern** for two-zone content modules |
| **Promote** | fr-ratio model as **default inner split** across WF-V3 |
| **Review** | Panel `padding-left: 48px` — consider gap-only separation or tokenized divider width |
| **Document** | Credit split in Layout Authority as **Module Type M2** (head + panel) |

---

## 5. Trust Row

### 5.1 Current model

| Property | Value | Source |
|----------|-------|--------|
| Selector | `.wf-v3-trust__inner` | `_trust-row.scss` |
| Layout | `display: flex` | not CSS Grid |
| Items | `flex: 1` · `min-width: 0` | equal distribution |
| Separators | `border-left` on `item + item` | |
| Item count | 5 (PDP) | frozen trust model |

**Computed item width @1232px:** `(1232 − 4×gap) / 5 ≈ **~230px**` per item (with `$space-5` gaps).

### 5.2 Percentage dependency

| Question | Answer |
|----------|--------|
| Uses `%` columns? | **No** — flex equal split |
| Container-dependent? | **Yes** — absolute item width floats with container |
| Percentage-equivalent behavior? | **Yes** — each item ≈ 20% of row (flex: 1) |
| Drift vs fr grid? | **LOW** for equal splits; **MEDIUM** for text wrap at narrow item width |

### 5.3 Recommendation (Trust Row)

| Item | Recommendation |
|------|----------------|
| **Accept** | Equal-split pattern for 5 proof items |
| **Prefer** | `grid-template-columns: repeat(5, minmax(0, 1fr))` — **align with grid family**, same gap semantics as featured/banks |
| **Add** | **`min-width` per item** (~180px) — below that, stack or horizontal scroll with documented breakpoint |
| **Homepage H5** | Same grammar — dealer vs vehicle proof only differs in content |

---

## 6. Cross-Surface Layout Inventory

| Surface | Block | Model | Gap | Drift class | Status |
|---------|-------|-------|-----|-------------|--------|
| PDP | Hero gallery/offer | `65%` / `35%` | 40px | **D1 — defective** | FIX required |
| Homepage | Hero content/visual | `1fr` / `42%` | 40px | **D2 — inconsistent** | FIX required |
| PDP + HP | Credit block | `5fr` / `7fr` | 48px | **S1 — stable** | KEEP |
| Homepage | Featured inventory | `repeat(4, 1fr)` | 20px | **S1 — stable** | KEEP |
| Homepage | Dealer advantages | `repeat(4, 1fr)` | 24px | **S1 — stable** | KEEP |
| PDP + HP | Equipment | `repeat(3, 1fr)` | 48px | **S1 — stable** | KEEP |
| PDP + HP | Banks | `repeat(8, 1fr)` | 16px | **S1 — stable** | KEEP |
| PDP + HP | Trust row | flex `1` | 20px | **S2 — acceptable** | ALIGN to grid |
| PDP | Offer CTA | `repeat(3, 1fr)` | 12px | **S3 — nested** | Needs offer min-width |
| PDP | Offer specs | `repeat(3, 1fr)` | 16px | **S3 — nested** | Needs offer min-width |
| Both | Header nav | `auto 1fr auto` | — | **S1 — stable** | KEEP |
| Both | Footer bands | mixed fr | — | **S1 — stable** | KEEP |

**Drift classes:** D = defective · S1 = stable · S2 = acceptable, normalize · S3 = depends on parent zone width

---

## 7. WF-V3 Layout Authority Candidate

Предлагаемый **единый принцип** inner-zone layout для freeze. Дополняет WF-GRID-DISCIPLINE (outer), **не заменяет** его.

### 7.1 Two-layer model

```text
Layer 1 — PAGE GRID (frozen)
  WF-GRID-DISCIPLINE: section shell → .wf-v3-container
  Contract: max 1280px · pad 24px · one page = one container contract

Layer 2 — ZONE GRID (candidate — requires iteration)
  Inside .wf-v3-container only
  Split types L1–L5 (see table below)
```

### 7.2 Zone split types

| Type | Name | Pattern | Example zones |
|------|------|---------|---------------|
| **L1** | Proportional split | `{gallery-fr}fr {offer-fr}fr` + documented ratio | PDP Hero 13fr 7fr |
| **L2** | Asymmetric hero | `{content-fr}fr minmax({visual-min}px, {visual-max}fr)` | Homepage Hero |
| **L3** | Fixed-count equal grid | `repeat(N, minmax(0, 1fr))` | Featured (N=4), Banks (N=8), Equipment (N=3) |
| **L4** | Module head/panel | `{head-fr}fr {panel-fr}fr` | Credit 5fr 7fr |
| **L5** | Equal proof strip | `repeat(N, minmax({item-min}px, 1fr))` | Trust (N=5) |

### 7.3 Global rules (candidate)

| Rule ID | Rule | Severity |
|---------|------|----------|
| WF-LAYOUT-001 | **No `%` grid tracks when `gap > 0`** — use `fr` or `minmax` | CRITICAL |
| WF-LAYOUT-002 | **Hero ratio intent in tokens as fr pair**, not `%` pair | CRITICAL |
| WF-LAYOUT-003 | **Offer/commerce columns: min-width floor** (recommended `360px`) | HIGH |
| WF-LAYOUT-004 | **Card grids: fixed N at desktop**; auto-fit only on catalog with charter | HIGH |
| WF-LAYOUT-005 | **One zone type = one pattern** — no mixing `%` and `fr` on sibling heroes | CRITICAL |
| WF-LAYOUT-006 | **Nested grids inherit parent min-width** — validate CTA/specs inside narrowest parent | HIGH |
| WF-LAYOUT-007 | **Document responsive collapse** per zone before production freeze | HIGH |
| WF-LAYOUT-008 | **Gap values from spacing tokens only** — no ad-hoc gap breaking ratio math | MEDIUM |

### 7.4 Surface mapping

| Surface | Primary zone types | Authority notes |
|---------|-------------------|-----------------|
| **PDP** | L1 hero · L5 trust · L3 equipment · L4 credit · L3 banks | L1 **must migrate** off `%` |
| **Homepage** | L2 hero · L3 featured · L5 trust · L3 advantages · L4 credit teaser · L3 banks | L2 **must be defined** before freeze |
| **Catalog** (future) | L3 auto-fill variant · card minmax 280px | Separate from homepage N=4 |
| **Finance** | L4 credit (full) · L3 banks | Inherit L4 from PDP |
| **Trust** | L5 strip | PDP vehicle proof · Homepage dealer proof — same L5 |
| **Future pages** | L3 default · L4 for split modules · L1 only for gallery/commerce splits | Charter picks type |

### 7.5 Token candidate (documentation — not implemented)

```scss
// WF-V3 INNER ZONE TOKENS (candidate)
$hero-gallery-fr: 13;
$hero-offer-fr: 7;
$hero-offer-min: 360px;
$hero-zone-gap: $space-8; // 40px

$credit-head-fr: 5;
$credit-panel-fr: 7;

$featured-cols-desktop: 4;
$trust-items: 5;
$trust-item-min: 180px;

$card-min-width: 260px;
```

### 7.6 Promotion path

| Step | Action | Owner |
|------|--------|-------|
| 1 | Operator HITL on this review | Operator |
| 2 | Author `WF-LAYOUT-DISCIPLINE-v1.md` in `website-factory-reference-v1/frontend-rules/` | Factory |
| 3 | Prototype iteration: PDP hero `%` → `fr` + offer min (charter, not silent) | Frontend prototype |
| 4 | Prototype iteration: Homepage hero L2 definition | Frontend prototype |
| 5 | Update PDP freeze **implementation appendix** — ratio intent unchanged, model fixed | Governance |
| 6 | WF-GRID-005 QA extended with inner-zone checks | Production QA |

---

## 8. Gap vs WF-V2 Lessons

| WF-V2 failure | WF-V3 status after this review |
|---------------|-------------------------------|
| Container width drift per page | **Fixed** — WF-GRID-DISCIPLINE |
| Hero ratio via `%` / scoped widen | **Partially repeated** — WF-V3 hero still `%` inside fixed container |
| 68/32 tuned to viewport not tokens | **Risk** — no min-width floor on offer |
| Mixed layout models across waves | **Present** — credit `fr`, hero `%`, trust flex |
| Layout drift under cosmetic pass | **Risk remains** until WF-LAYOUT rules frozen |

---

## 9. Decision Matrix

| Criterion | Pass? | Blocker? |
|-----------|-------|----------|
| Container contract unified | YES | — |
| Inner zone authority documented | **NO** | **YES** |
| PDP hero implementation model sound | **NO** | **YES** |
| Homepage hero consistent with authority | **NO** | **YES** |
| Credit / featured / trust patterns classifiable | YES | — |
| Responsive layout authority | **SAFE UNKNOWN** | **YES** (before production) |
| Cross-surface pattern unification | **NO** | **YES** |

---

## 10. Final Decision

### **B — Additional Layout Iteration Required**

WF-V3 **не готов** к полной заморозке layout authority. Container layer (WF-GRID-DISCIPLINE) — **ready**. Inner zone layer — **requires one controlled iteration** before freeze.

### Required before re-review (minimum)

| # | Deliverable | Blocks |
|---|-------------|--------|
| 1 | Migrate PDP hero off `%` → **fr ratio + offer min-width** (charter) | Layout freeze |
| 2 | Define Homepage hero **L2 pattern** in writing | Homepage freeze |
| 3 | Publish **WF-LAYOUT-DISCIPLINE-v1** (or equivalent) at Factory Foundation | Cross-project |
| 4 | Normalize Trust row to **L5 grid** (optional but recommended) | Pattern consistency |
| 5 | Document **responsive collapse** per hero/trust/featured | Production handoff |

### What may proceed without layout iteration

| Work | Allowed? |
|------|----------|
| Asset replacement (photos, logos) | YES |
| Typography / color polish inside fixed zones | YES |
| Content copy changes | YES |
| OpenCart / TEST integration | **NO** — until layout authority re-review PASS |
| WF-V3 full program freeze | **NO** |

---

## UNKNOWN / SECURITY

| Item | Status |
|------|--------|
| Mobile/tablet stack breakpoints for hero/trust/featured | **SAFE UNKNOWN** — no rules in prototype |
| Catalog card grid (full listing) | **NOT PROTOTYPED** — L3 auto-fill is candidate only |
| Operator preference: 13/7 vs 12/8 fr for hero | **OPEN** — visual HITL after fr migration |
| Exact offer min-width (360px vs 380px) | **OPEN** — depends on CTA label length |
| CI / automated layout lint | **NOT IMPLEMENTED** |

**SECURITY RISK:** None (documentation only).

---

*SITE-001 WF-V3 Layout Authority Review v1 — audit and recommendation only; no implementation; no commit implied.*
