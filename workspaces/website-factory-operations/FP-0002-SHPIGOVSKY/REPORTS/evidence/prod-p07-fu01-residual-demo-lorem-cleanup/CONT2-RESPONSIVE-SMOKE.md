# PROD-P07-FU01-CONT2 — Responsive smoke

Primary routes: `/uslugi/`, alcohol leaf, `/uslugi/zavisimosti/`.  
Viewports: desktop ~1440px; mobile ~390px.

| Check | Desktop 1440 | Mobile 390 |
|-------|--------------|------------|
| Overflow-X | none (`scrollWidth` ≤ client) | none |
| Empty headings | 0 | 0 |
| Empty accordion shells | 0 | 0 |
| Malformed cards (bbox) | 0 | 0 |
| Footer collision | no | no |
| Large blank (false-positive filter) | decorative `clinic-landscape` / corridor image sections only | none |

Full-page PNGs can look empty when downsampled because `data-reveal` keeps below-fold nodes at opacity 0 until scrolled. Targeted scrolled shots confirm live blocks:

* `cont2-responsive/uslugi-desktop-first-cards.png`
* `cont2-responsive/uslugi-mobile-first-card.png`
* `cont2-responsive/alcohol-desktop-signs.png`
* `cont2-responsive/alcohol-desktop-program.png` (2×2 equal-height cards)
* `cont2-responsive/alcohol-desktop-faq.png`
* `cont2-responsive/alcohol-mobile-signs.png`

**Verdict:** responsive cleanup regression **not** found. No redesign.

JSON: `cont2-responsive-smoke.json`
