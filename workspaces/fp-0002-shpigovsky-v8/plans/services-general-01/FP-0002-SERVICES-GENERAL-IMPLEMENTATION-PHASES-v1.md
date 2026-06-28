# FP-0002 — Services General Implementation Phases v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26

---

## Phase table

| Phase | Scope | Files likely changed | Partials reused | New partials | Assets | Risk | Validation |
| ----: | ----- | -------------------- | --------------- | ------------ | ------ | ---- | ---------- |
| 1 | Page shell + inner hero | `uslugi.html`, `style.scss` | `hero-inner.html`, header/footer | — | Services hero image export | Low | Build; hero @1440/1024/390 |
| 2 | Exact reusable sections repositioned | `uslugi.html` | program, founder, comfort, FAQ, final form | — | None | Low | Order vs PNG top-to-bottom |
| 3 | Category hub block 1 (Зависимости) | `uslugi.html`, `style.scss`, new partial | service list pattern | `services-category-hub.html` (or similar) | Cat.1 gallery ×3 + watermark | Medium | Desktop 3-col; mobile stack |
| 4 | Category hubs 2–4 | same + partial params | same pattern | invoke 3× or extend partial | 9 images + copy | Medium | Content completeness |
| 5 | Responsive completion | `style.scss` | — | — | — | Medium | ≤1024, 767, 390 widths |
| 6 | Build + visual QA | dist via gulp | — | — | All exports in place | Medium | Compare PNG; no Home diff |
| 7 | Operator review | status docs only | — | — | — | Low | HITL sign-off |

---

## Rollback boundaries

| After phase | Rollback action |
|-------------|-----------------|
| 1 | Revert `uslugi.html` + hero SCSS only |
| 2 | Revert page includes order |
| 3–4 | Remove new partial + `.services-*` SCSS block |
| 5–6 | Revert responsive SCSS for Services scope |
| Full | Restore from checkpoint `FP-0002-V7-OPERATOR-DELTA-BEFORE-SERVICES-PLANNING-01-SOURCE.zip` |

---

## main.js

**Not expected for Pass 1** — accordion, Fancybox, modal, lead form already initialized globally. Category hubs are static links + modal CTA.

---

*End of implementation phases v1.*
