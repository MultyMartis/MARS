# FP-0002 V7 — Recovery Life Geometry Map

| Property | Desktop | Mobile | Confidence | Evidence |
| -------- | ------: | -----: | ---------- | -------- |
| Section width | 1437px frame | 100% viewport | HIGH | `77:4225` bbox; responsive CSS |
| Container width | 1170px content | 100% minus `--pad-x` | HIGH | child nodes 1170px; project `.container` |
| Section top/bottom padding | global `--pad-y` | global `--pad-y` | HIGH | no root override; `main > section` rhythm |
| Heading width | 1170px | 100% | HIGH | `77:4227` |
| Heading font size | 36px | `--font-size-h2` (36px) | HIGH | node `77:4227` |
| Heading line height | 1.2 raw (~43px) | token `--line-height-h2` | HIGH | node `77:4227` |
| Intro highlight width | 1170px outer / 1120px text | 100% | HIGH | `77:4228`–`77:4232` |
| Columns | 3 | 1 stack ≤1024px | HIGH | `77:4241` horizontal; project breakpoint |
| Grid gap | 30px | 30px | HIGH | `(1170 - 3×370) / 2` |
| Card width | 370px | 100% | HIGH | `77:4242`/`4245`/`4248` |
| Card min-height | 293 / 360 / 438 | auto | HIGH | per-card bbox |
| Card padding | ~41px top, 30px sides | same tokens | MEDIUM | transform offsets on text nodes |
| Icon/image size | background fill only | same | HIGH | `77:4226` image @ 40% opacity |
| Radius | 30px cards; ~35px highlight band | tokens | HIGH | `cornerRadius` on frames |
| Item spacing | 30px section gaps | `--pad-gap` | HIGH | y-offset deltas between blocks |
| Mobile stack order | heading → highlight → intro → cards 1–3 | same DOM order | HIGH | Figma vertical stack + CSS grid 1fr |

**Root padding decision:** USE GLOBAL RHYTHM — no `.home-recovery-life { padding-top/bottom }` override.

**New direct values:** card padding `41px 30px 30px` (Figma-evidenced); intro `line-height: 1.48`; stage list `16px / 1.4`.

**Verdict:** VERIFIED desktop geometry; mobile layout derived from desktop content + project ≤1024 stack convention (no dedicated mobile Figma frame).
