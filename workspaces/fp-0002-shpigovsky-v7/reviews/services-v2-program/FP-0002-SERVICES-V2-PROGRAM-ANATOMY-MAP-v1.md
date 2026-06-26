# FP-0002 — Services V2 Program Anatomy Map v1

**Authority:** offline `Spig_v1.2.fig` parse (not live MCP read)

| Order | Region | Figma node | Visible content | Runtime component |
| ----: | ------ | ---------- | --------------- | ----------------- |
| 1 | Section root | `1:1610` | Программа центра | `.services-program-v2` `#services-program` |
| 2 | Header row (desktop) | `1:1641`–`1:1648` | H2 + «подробнее» + arrow | `.services-program-v2__head` |
| 3 | Lead marker | `1:1615` | Боль бывает очень похожей… | `.services-program-v2__lead` |
| 4 | Intro | `1:1617` | Каждый человек приходит… | `.services-program-v2__intro` |
| 5 | Grid row 1 | `1:1618` | этап 01 + 02 | `.services-program-v2__grid` |
| 6 | Item 01 | `1:1619`–`1:1623` | title + demo body + image | `.services-program-v2__item` |
| 7 | Item 02 | `1:1624`–`1:1628` | title + Lorem + image | `.services-program-v2__item` |
| 8 | Grid row 2 | `1:1629` | этап 03 + 04 | `.services-program-v2__grid` |
| 9 | Item 03 | `1:1630`–`1:1634` | title + demo body + image | `.services-program-v2__item` |
| 10 | Item 04 | `1:1635`–`1:1639` | title + demo body + image | `.services-program-v2__item` |
| 11 | Guest CTA band | `1:1640` | Запишитесь на гостевой визит… | `.services-program-v2__cta-band` |
| 12 | Mobile foot link | `1:4906`–`1:4908` | подробнее о программе | `.services-program-v2__foot-link` |

- **Desktop node:** `1:1610` — Программа центра
- **Mobile node:** `1:4880` — Программа центра (within `1:4624`)
- **Number of items:** 4
- **Desktop structure:** 2×2 card grid; image-top cards; header link in head row
- **Mobile structure:** H2 → lead → intro → vertical stack (image + title only) → guest CTA → foot link
- **Anatomy verdict:** **MAPPED**
