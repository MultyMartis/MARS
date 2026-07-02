# FP-0002 — Home to Services General Reuse Forecast v1

**Audit ID:** `home-style-baseline-01`  
**Authority:** `f5a9ecd7` + high-level PNG review  
**Design PNGs:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/26.06.2026/`  
**Files:** `Услуги общая - Десктоп.png` (~9.2 MB), `Услуги общая - Мобильная.png` (~5.1 MB)  
**Date:** 2026-06-26

**Method:** High-level comparison only — no full geometry extraction. Existing `uslugi.html` partial reuse treated as proven evidence.

---

## Services area forecast

| Services area | Likely source pattern | Reuse confidence | Next audit needed |
| ------------- | --------------------- | ---------------: | ----------------: |
| Site header / footer | `layout/header`, `layout/footer` | 100% | No |
| Inner page hero | `hero-inner.html` (`.hero--inner`) | 85% | Yes — hero copy + image mapping |
| Page H1 / intro copy block | `.home-recovery-intro` text column (not whole section) | 60% | Yes — block boundary audit |
| Service category accordion | `.home-treatment-prevention` | 90% | Yes — content/category mapping |
| Program 4 directions | `.home-rehabilitation-program` (**on uslugi**) | **100% proven** | Minor — heading param only |
| Founder / trust block | `.home-founder-quote` (**on uslugi**, variant A) | **100% proven** | No |
| Comfort / facility gallery | `.home-comfort` (**on uslugi**) | **100% proven** | No |
| FAQ | `.home-faq` (**on uslugi**) | **100% proven** | Content swap only |
| Final CTA form | `.home-final-form` (**on uslugi**) | **100% proven** | `leadSource` param |
| Consultation modal | `modal-consultation.html` | 100% | No |
| Outline feature cards | `.home-feature-grid__card-grid` | 70% | Yes — if mock shows 3-col cards |
| Dark CTA band | `.home-rehabilitation-requirements__cta-band` | 65% | Yes — if mock shows mid-page CTA |
| Reviews carousel | `.home-reviews` | 50% | Yes — confirm on mock |
| Specialists carousel | `.home-specialists` | 50% | Yes — confirm on mock |
| Video block | `.home-videos` | 40% | Yes — if mock includes video |
| Articles / blog teasers | `.home-articles` | 30% | Yes — unlikely on Services hub |
| Genotyping block | `.home-genotyping` | 35% | Yes — specialty-specific |
| Full-width photo bands | `.home-staff-photo` / `.home-clinic-landscape` | 55% | Yes — asset mapping |
| Requirements / intake steps | `.home-rehabilitation-requirements` | 45% | Yes — page-specific |
| Home hero | `.hero--home` | 0% | No — use inner hero |

---

## Alignment with existing `uslugi.html`

Current Services stub already implements the **core reuse stack** identified in PROJECT-STATUS:

- program, founder, comfort, FAQ, final form

**Gap vs «Услуги общая» mock (expected):**

- Inner hero (not present on stub page)
- Treatment/category accordion or equivalent service listing
- Possible intro lead section
- Header nav active state (already wired)

---

## Reuse type legend

| Type | Meaning |
|------|---------|
| Proven | Live include on `uslugi.html` @ f5a9ecd7 |
| High | Strong visual match; partial exists |
| Medium | Pattern exists; content/structure TBD |
| Low | Home-specific or unconfirmed on mock |

---

## Planning gate outputs required

Next task **FP-0002 V7 — Services General Page Design-to-Source Mapping and Build Plan** should produce:

1. Section-by-section map: PNG block → partial → reuse status  
2. Inner hero spec (copy, image, height)  
3. List of **new** blocks not covered by Home partials  
4. Confirmation whether stub `uslugi.html` order matches mock top-to-bottom  
5. Mobile-specific overrides per block  

**Not in scope:** implementation, SCSS edits, class renames.

---

*End of services reuse forecast v1.*
