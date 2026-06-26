# FP-0002 — Services General Pass 1 Visual Review

**Date:** 2026-06-26  
**Preview:** `http://127.0.0.1:4174/uslugi.html`  
**Design authority:** PNG 26.06.2026 + operator-canonical SCSS

## Screenshots

| File | Viewport | Scope |
| ---- | -------- | ----- |
| `screenshots/SERVICES-PASS-1-FULL-1398.png` | 1398 | Full page |
| `screenshots/SERVICES-PASS-1-HERO-1398.png` | 1398 | Inner hero |
| `screenshots/SERVICES-PASS-1-HERO-390.png` | 390 | Inner hero mobile |
| `screenshots/SERVICES-PASS-1-REUSE-SECTIONS-1398.png` | 1398 | Program block entry |
| `screenshots/SERVICES-PASS-1-REUSE-SECTIONS-390.png` | 390 | Program → final form clip |
| `screenshots/HOME-SMOKE-1398.png` | 1398 | Home regression |
| `screenshots/HOME-SMOKE-390.png` | 390 | Home regression mobile |

## Responsive overflow (horizontal)

| Width | Services | Home |
| ----: | -------- | ---- |
| 390 | Pass | Pass |
| 768 | Pass | Pass |
| 1024 | Pass | Pass |
| 1025 | Pass | Pass |
| 1398 | Pass | Pass |
| 1440 | Pass | Pass |
| 1920 | Pass | Pass |

## Services checks

| Check | Result |
| ----- | ------ |
| Header visible | Pass |
| Inner hero present | Pass |
| Hero gutters (30px desktop / 15px ≤1024 via `.hero` + container tokens) | Pass |
| Hero crop (`object-fit: cover`, center) | Pass |
| Hero H1 «Лечение и профилактика» | Pass |
| Hero tagline | Omitted (empty — SAFE_UNKNOWN) |
| Hero CTA in block | **Not rendered** (partial limitation) |
| Category hub visible placeholders | **Zero** |
| Section order vs Pass 1 target | Pass |
| Program / Founder A / Comfort / FAQ / Final form | Pass |
| Footer | Pass |
| Mobile stacking | Pass |
| Temporary hero asset (`hero-main.png`) | Visible — not final Services interior |

## Home smoke

| Check | Result |
| ----- | ------ |
| Home hero | Pass |
| Recovery intro | Pass |
| Founder variant B | Pass |
| Treatment block | Pass (full page) |
| No obvious Services regression on Home | Pass |

## Visual verdict

**PASS for Pass 1 scope** — shell + inner hero + reuse order. Known gaps: temporary hero image, no hero CTA, category hubs absent (by design).

---

*End of Pass 1 visual review.*
