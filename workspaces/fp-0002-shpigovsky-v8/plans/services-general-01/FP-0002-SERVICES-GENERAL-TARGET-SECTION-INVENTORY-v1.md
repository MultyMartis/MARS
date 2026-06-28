# FP-0002 — Services General Target Section Inventory v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26  
**Design authority (composition):**  
`INCOMING/01_DESIGN/26.06.2026/Услуги общая - десктоп.png`  
`INCOMING/01_DESIGN/26.06.2026/Услуги общая - мобильная.png`  
**Figma cross-check:** `Spig_v1.2.fig` → frames `Услуги хаб` (1437×11999), `Услуги хаб - моб` (380×17611)

---

## Target section table

| Order | Target section | Desktop structure | Mobile structure | Interaction | Evidence |
| ----: | -------------- | ----------------- | ---------------- | ----------- | -------- |
| 0 | Site header | Full desktop header + nav; active «Услуги» | Mobile bar + hamburger | Off-canvas nav, messengers | PNG both; shared `header.html` |
| 1 | Inner hero | Full-bleed interior photo; bottom-rounded panel; H1 «Лечение и профилактика»; tagline/lead; red CTA | Stacked hero image + panel; reduced type | CTA → consultation modal | PNG desktop/mobile; Figma `1 - Главный экран` inside `Услуги хаб`; `hero-inner.html` |
| 2 | Category hub — Зависимости | Section head + lead; expanded service list (4+ links); 3-col image strip; category CTA | Vertical stack: head → lead → list → images → CTA | Service links; CTA modal | PNG; Figma `3- Услуги` (h≈1413); Home accordion panel 1 content |
| 3 | Category hub — Психическое здоровье | Same pattern; distinct lead + services | Same stack | Links + CTA | PNG; Figma `3- Услуги` (h≈1698); accordion item 2 label |
| 4 | Category hub — Расстройства пищевого поведения | Same pattern | Same stack | Links + CTA | PNG; Figma accordion item 3 |
| 5 | Category hub — Генотипирование | Same pattern (shorter block possible) | Same stack | Links + CTA | PNG; Figma `3- Услуги` (h≈804); accordion item 4 |
| 6 | Program directions | Section head «Наши программы…» / program lead; 4 direction cards (image + title + copy) | Cards stack vertically | «подробнее» link (decorative `#` today) | PNG 2×2 grid; Figma `Программа центра`; `home-rehabilitation-program` |
| 7 | Founder quote | 2-col: quote + portrait; red quote mark; CTA on figure | Single column: quote then portrait | CTA modal | PNG; Figma `Слово спецу`; `home-founder-quote` variant A |
| 8 | Comfort gallery | Head + lead; logo tile + photo grid; Fancybox | 1-col gallery stack | Fancybox lightbox | PNG «Комфорт…»; Figma `преимущества`; `home-comfort` |
| 9 | Mid-page CTA band *(optional)* | Dark band: lead + phone + «Записаться» | Stacked band | Phone link + modal | PNG mid-page strip; pattern ≈ `.home-rehabilitation-requirements__cta-band` — **confirm on implementation** |
| 10 | FAQ | H2 + accordion list | Full-width accordion | `data-accordion` one-open | PNG «ОТВЕТЫ НА ВОПРОСЫ»; Figma `faq`; `home-faq` |
| 11 | Final lead form | Dark band + 2-col copy/form | Stacked copy + form | `data-lead-form`, phone mask | PNG; `home-final-form` |
| 12 | Footer | 4-col links + legal | Stacked footer | Links | Shared `footer.html` |

---

## Section notes

- **Do not merge** the four category hubs into one accordion — PNG shows **four separate compositional blocks** with image galleries each.
- **Do not merge** program directions with category hubs — distinct visual blocks in PNG order.
- Mobile PNG is authority for stacking; desktop uses multi-column galleries within each category block.
- Decorative background watermark (lifebuoy) visible in PNG — treat as **section-specific asset**, not Home reuse.

---

*End of target section inventory v1.*
