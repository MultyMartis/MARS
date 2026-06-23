# FP-0002 Services Exact Reuse Matrix v1

**Mockup authority:** `INCOMING/01_DESIGN/services-hub/SERVICES-HUB-DESKTOP.png` (SHA-256 `3D5DA9190612B1AB4D73C41CDE3C238798EE2E0DCF36CA3B6E04A76E8FFB1072`), `SERVICES-HUB-MOBILE.png` (SHA-256 `8D866A941733470D9DC5BC634D47A9CC217955D6566A5C620CD7D91A6C9A9339`)  
**Figma:** `INCOMING/01_DESIGN/Шпиговский.fig` (SHA-256 `D25A13617664040045A88AE9B804FEB737076007CB317D49699196F92232B64B`) — structure reference only  
**Date:** 2026-06-23  
**Mode:** REUSE_ONLY — hard gate enforced

## Matrix

| Order | Mockup block | Matching home partial | Structure match | Allowed action | Confidence |
| ----: | ------------ | --------------------- | --------------- | -------------- | ---------- |
| 1 | Header | `partials/layout/header.html` | EXACT_100 | REUSE_UNCHANGED | HIGH |
| 2 | Service Hero (breadcrumb band + H1 + body + CTA) | `partials/sections/hero.html` | NO_MATCH | DO_NOT_IMPLEMENT_YET | HIGH |
| 3 | Зависимости и пристрастия (index, topics, image cards, CTA) | `partials/sections/home-treatment-prevention.html` | NO_MATCH | DO_NOT_IMPLEMENT_YET | HIGH |
| 4 | Психическое здоровье (index, topics, image cards, CTA) | `partials/sections/home-treatment-prevention.html` | NO_MATCH | DO_NOT_IMPLEMENT_YET | HIGH |
| 5 | Расстройства пищевого поведения (index, topic list, CTA) | `partials/sections/home-treatment-prevention.html` | NO_MATCH | DO_NOT_IMPLEMENT_YET | HIGH |
| 6 | Программа центра (4 directions) | `partials/sections/home-rehabilitation-program.html` | EXACT_100 | REUSE_WITH_PARAMETERS | HIGH |
| 7 | Founder quote | `partials/sections/home-founder-quote.html` | EXACT_100 | REUSE_WITH_PARAMETERS | HIGH |
| 8 | Comfort gallery | `partials/sections/home-comfort.html` | EXACT_100 | REUSE_UNCHANGED | HIGH |
| 9 | FAQ | `partials/sections/home-faq.html` | EXACT_100 | REUSE_UNCHANGED | HIGH |
| 10 | Final form | `partials/sections/home-final-form.html` | EXACT_100 | REUSE_WITH_PARAMETERS | HIGH |
| 11 | Footer | `partials/layout/footer.html` | EXACT_100 | REUSE_UNCHANGED | HIGH |
| 12 | Modal | `partials/components/modal-consultation.html` | EXACT_100 | REUSE_UNCHANGED | HIGH |

## Hard-gate summary

| Classification | Count |
| -------------- | ----: |
| EXACT_100 | 7 |
| SAME_DOM_DIFFERENT_CONTENT | 0 |
| PARTIAL_SIMILARITY | 0 |
| NO_MATCH | 4 |
| **Hard-gate PASS (included)** | **7** |
| **Hard-gate FAIL (excluded)** | **4** |

---

## Proof records (included blocks)

### Header — PASS

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Top chrome with logo, nav, phone, CTA; mobile burger | `header.html` desktop + mobile bar + off-canvas | Same landmark, nav item count, logo placement, modal trigger pattern | Active nav param on `/uslugi/` only |

### Program — PASS

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| «Наша программа включает 4 направления» + 4 direction articles with image/title/body | `home-rehabilitation-program.html` | 1×`h2`, 2 intro `p`, 4×`article` with image + `h3` + `p`; same grid/stack order desktop/mobile | Heading text via `programHeading` param only |

### Founder quote — PASS

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Blockquote + founder photo + modal CTA | `home-founder-quote.html` | 4 quote `p`, figure photo, name, role, modal button with `data-modal-open` | `modalSource` param value `services-founder` |

### Comfort — PASS

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Heading + lead + gallery grid with Fancybox | `home-comfort.html` | Head row, lead `p`, gallery items incl. decor logo + linked images | Content copy identical (shared partial) |

### FAQ — PASS

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| «Нас часто спрашивают» accordion | `home-faq.html` | `h2` + `data-accordion` items with button/panel pairs | Shared home FAQ copy |

### Final form — PASS

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| «Остались вопросы?» band + name/phone/consent form | `home-final-form.html` | Copy column + form with hidden lead fields, 3 fields, consent checkbox | `leadSource` param `services-final` |

### Footer + Modal — PASS

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Standard site footer / consultation modal | `footer.html`, `modal-consultation.html` | Same DOM systems as home | NONE |

---

## Proof records (excluded blocks — hard-gate FAIL)

### Service Hero — FAIL

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Full-bleed image + overlay container + eyebrow `p` + `h1` «Лечение и профилактика» + long body + CTA + **breadcrumb nav below hero** | `hero.html` | Both have full-bleed image + CTA button pattern | Mockup: overlay inside image, eyebrow, body paragraph, breadcrumbs `nav>ol`; Home: panel tagline + site name `h1`, **no breadcrumbs**, **no body paragraph**, different class system |

### Зависимости и пристрастия — FAIL

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Index `01`, `h2`, 2 intro `p`, **4 topic articles** (title + link + long body each), **3 image cards**, bottom CTA button | `home-treatment-prevention.html` | Section discusses same clinical domain | Home: accordion with **4 toggles**, only panel 1 has **link list** (no topic bodies, no image cards, no section index, no bottom CTA). **Different element count, order, and grid type.**

### Психическое здоровье — FAIL

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Index `02`, topics + **3 image cards** + topic links + CTA | `home-treatment-prevention.html` | Accordion item label text matches category name only | Panel 2 is **empty** on home; no cards, no intro copy, no CTA. **DOM not reusable.**

### Расстройства пищевого поведения — FAIL

| Mockup evidence | Home block evidence | Matching elements | Differences |
| --------------- | ------------------- | ----------------- | ----------- |
| Index `03`, intro + **topic link rows** + CTA | `home-treatment-prevention.html` | Accordion item label matches category | Panel 3 **empty** on home; mockup uses standalone section layout, not accordion panel. **NO_MATCH.**

---

**REJECTED IMPLEMENTATION — NOT CURRENT AUTHORITY:** prior `services-*` partials from commit `feff069` (archived, reverted).
