# Forge WordPress — Frontend interaction ownership standard v1

**ID:** FW-S-36  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Evidence:** FP-0002 menu / Smart Search / sliders / floating header / lifebuoy parallax; INC-03 iOS false PASS

**Companion:** [NAVIGATION](FORGE-WORDPRESS-NAVIGATION-STANDARD-v1.md) · [SLIDER-CAROUSEL](FORGE-WORDPRESS-SLIDER-CAROUSEL-STANDARD-v1.md) · [REAL-DEVICE-QA](FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md)

---

## 1. One interaction → one owner

| Interaction | Typical owner | Must not also be owned by |
|-------------|---------------|---------------------------|
| Menu (desktop L2 + mobile) | one nav JS module | a second “mobile kit” |
| Accordion | one accordion module | slider / hash router |
| Slider | Swiper (or chosen lib) **only** | `scrollBy` on the same axis |
| Search | one REST + one UI module | native form + extra autocomplete lib |
| Modal | one modal module | duplicate CTA overlay |
| Parallax / decorative motion | one motion module | CSS animation **and** JS transform **and** framework |
| Form UX | one forms JS + plugin handler | multiple submit binders |

Multiple listeners/libraries controlling the same DOM state is a **BLOCKER**.

Prefer `data-*` hooks, not presentational classes, as JS selectors.

---

## 2. Initialization and teardown

Every module:

1. **Idempotent init** — `querySelectorAll` on a root; skip if `data-initialized`  
2. **No global duplicate listeners** on `document` without a namespace/guard  
3. **Teardown** on PJAX/BFCache if used; otherwise document “full page load only”  
4. **Fails closed** — if the library is missing, content remains usable ([progressive enhancement](FORGE-WORDPRESS-ACCESSIBILITY-BASELINE-v1.md))

---

## 3. Transform / position / scroll ownership

A visual element must not casually accumulate independent:

- animation `transform`
- parallax `transform`
- centering `translate(-50%, -50%)`
- framework/slider `transform`
- browser workaround `transform`

**Prefer one composed transform owner** (one JS writer or one CSS animation, not both).

Documented risks (FP-0002 iOS lifebuoy):

| Feature | Risk with transformed ancestors / compositor |
|---------|-----------------------------------------------|
| `position: fixed` | containing block becomes the transformed ancestor |
| `sticky` | same; overflow ancestors clip |
| `overflow: hidden` on parents | clips fixed/parallax layers |
| `contain` | can freeze a layer that should move |
| `visualViewport` / `100vh` | iOS chrome; emulation lies |
| stacked `will-change` | extra layers, false PASS in Chromium |

If a cross-engine abstraction fails twice, a **bounded** engine-specific fallback is allowed (physical device evidence required).

---

## 4. Responsive architecture

Do not QA only desktop vs one mobile screenshot.

Each inventoried component states behavior at:

- wide desktop  
- normal desktop  
- tablet  
- narrow mobile  
- physical viewport / browser chrome  

Breakpoint **names** are owned in the design-system map. Page-specific breakpoints need an inventory justification.

Trackpad (MacBook) is an input method for horizontal sliders, not an afterthought.

---

*FW-S-36 v1.*
