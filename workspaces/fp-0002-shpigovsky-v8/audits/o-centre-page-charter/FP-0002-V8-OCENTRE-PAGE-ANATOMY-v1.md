# FP-0002 V8 O-Centre Page Anatomy v1

**Date:** 2026-06-29
**Method:** Reconcile PG-005 block inventory (canonical composition) with Spig_v1.2.fig section parse (visual evidence).

| Order | Block ID | Design name | Visual role | Content | Desktop behavior | Mobile behavior |
|---:|---|---|---|---|---|---|
| 0 | OC-G00 | Header (BLK-001/002) | Global chrome | Logo, contacts, primary nav, search | Two-row header; fixed production pattern | Offcanvas + sticky bar (BLK-004) |
| 1 | OC-B01 | 1 - Главный экран | Inner page hero | H1, eyebrow, lead, consultation CTA | Full-width image + overlay panel; service hero variant 007ˢ | Stacked copy; shorter hero (~604px frame) |
| 2 | OC-B02 | Breadcrumbs + subnav (005/006) | Wayfinding | Breadcrumb trail; in-page anchor list | Below hero; horizontal subnav | Same DOM; subnav scroll/wrap |
| 3 | OC-B03 | Дом - вступление / «Кто мы» (036) | About narrative intro | H2, lead bar, multi-paragraph institutional copy | Single-column editorial in container | Long-form stacked text |
| 4 | OC-B04 | Услуги / «Кого мы лечим» (036 ext.) | Condition spectrum + optional gallery | H2, intro, bullet categories, 3-up gallery | Text + static gallery grid (not Swiper) | «Зависимости…» + «Кого мы лечим» split frames |
| 5 | OC-B05 | Этапы процедуры (018) | **RETIRED** — mislabeled frame; actual block is OC-B04 at `1:2310` | — | — | — | **NOT IN COMPOSITION** |
| 6 | OC-B06 | Программа центра (020) | Four-direction program | H2, leads, 4 program tiles with images | Vertical program stack (services-program pattern) | Tall program band (~2184px) |
| 7 | OC-B07 | Guest visit CTA (019) | Program CTA band | Title, subtitle, phone, button | `program-cta-band` dark wrapper | Repeated CTA pattern |
| 8 | OC-B08 | преимущества / «Наш Дом» (037) | Narrative + advantages | H2, body, feature grid or photo bands | Large composite (~3621px) — infrastructure storytelling | Part of approach/advantage stack |
| 9 | OC-B09 | Expert opinion (022) | Founder / expert quote | Quote, attribution, optional photo | Founder-quote band (variant per page) | Embedded in narrative flow |
| 10 | OC-B10 | Комфорт, приватность (023) | Comfort mosaic gallery | H2, lead, Fancybox grid + logo decor | 3-col mosaic (comfort family) | Vertical gallery (~4958px frame) |
| 11 | OC-B11 | Специалисты (026) | Specialists slider | H2, 3 cards, pagination | Swiper 3-up | Slider 1-up / peek |
| 12 | OC-B12 | Отзывы (015) | Reviews preview | H2, slider cards, read-all | Swiper + stars | Compact slider |
| 13 | OC-B13 | faq (034) | FAQ accordion | H2, ~8 questions | Accordion; **Figma-confirmed** | Accordion |
| 14 | OC-G01 | Подвал (003) | Footer | Links, legal, CTA | 4-column footer | Mobile footer stack |

**Block order confirmed:** Yes for inventory core; FAQ tail confirmed by Figma with inventory **conflict** noted.
**Unresolved blocks:** OC-B08 vs OC-B09 merge on desktop; exact BLK-037/038 DOM split.
**Total content blocks (excl. global chrome):** 13 (+ 2 global).

---

## Per-block notes (accessibility / container)

| Block ID | Section role | Heading | Container | Interactions |
|---|---|---|---|---|
| OC-B01 | Hero landmark | H1 in hero | Full bleed + container copy | Modal CTA |
| OC-B02 | Navigation | — | `.container` | Anchor links |
| OC-B03–B04 | Region / narrative | H2 | `.container` | — |
| OC-B05 | Region | H2 + H3 steps | `.container` | CTA modal |
| OC-B06–B07 | Region | H2 / CTA title | `.container` | Modal + tel link |
| OC-B10 | Region + gallery | H2 | `.container` | Fancybox group `comfort` |
| OC-B11–B12 | Region | H2 | `.container` | Swiper |
| OC-B13 | Region | H2 | `.container` | Accordion buttons |

---

## Responsive anatomy summary

| Block | Desktop structure | Mobile structure | Same DOM | CSS-only | Separate asset | Risk |
|---|---|---:|---:|---:|---|
| OC-B01 | Image backdrop + overlay copy | Content-first stack | Yes | Yes | Possible hero crop | Medium |
| OC-B02 | Breadcrumb + horizontal subnav | Wrap / scroll | Yes | Yes | No | Low |
| OC-B03–B04 | Editorial + 3-col gallery | Stacked | Yes | Yes | Gallery images | Medium |
| OC-B05 | Steps row + CTA bar | Stacked steps | Yes | Yes | No | Low |
| OC-B06 | Program vertical items | Tall stack | Yes | Yes | Program images reuse | Low |
| OC-B10 | Mosaic grid | 1-col gallery | Yes | Yes | Comfort assets reuse | Low |
| OC-B11–B12 | Swiper | Swiper breakpoints | Yes | Yes | No | Low |
| OC-B13 | Accordion | Accordion | Yes | Yes | No | Low |
