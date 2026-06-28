# FP-0002 — Services General Risk Register v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26

---

| Risk | Probability | Impact | Prevention | Stop condition |
| ---- | ----------- | ------ | ---------- | -------------- |
| Home regression | Medium | High | Scope SCSS to `.page-uslugi` / new roots; no `.home-*` edits | Any Home visual diff @ index.html |
| Over-abstraction | Medium | Medium | No universal classes; one category partial parameterized | Proposal to rename `.home-*` globally |
| CSS selector collision | Low | Medium | New `.services-category-hub*` namespace | Unscoped rules affecting Home |
| Duplicate patterns | Medium | Low | Copy structure not class names from treatment | Two diverging list styles |
| Incorrect mobile interpretation | Medium | High | Mobile PNG authority; test 380px | Desktop-only stack assumption |
| Figma/PNG drift | Low | Medium | PNG 26.06.2026 wins composition; Figma for text/assets | Irreconcilable layout diff |
| Missing assets | High | Medium | Asset map + Figma export before QA | Placeholder images without approval |
| Content uncertainty | High | Low | SAFE_UNKNOWN list; Pass 1 uses proven cat.1 strings | Blocking: empty cat. 2–4 panels |
| Hero mismatch | Low | Medium | Use `hero-inner` not home hero | Wrong hero partial |
| Accordion duplication | Medium | Medium | Do not include whole `home-treatment-prevention` | Accordion on Services hub |
| Slider misuse | Low | Low | No sliders on Services General mock | Adding Swiper without evidence |
| Build/watch conflict | Low | Low | http-server on 4174 may serve stale dist | dist lock — rebuild when free |

---

## Highest risks

1. **Home regression** via unscoped SCSS in monolithic `style.scss`  
2. **Missing assets** for category galleries  
3. **Content uncertainty** for categories 2–4 and FAQ heading

---

## Stop conditions

- Operator canonical Home source altered without approval  
- Mass `.home-*` rename proposed during implementation  
- Design evidence contradicts PNG without operator ruling  

---

*End of risk register v1.*
