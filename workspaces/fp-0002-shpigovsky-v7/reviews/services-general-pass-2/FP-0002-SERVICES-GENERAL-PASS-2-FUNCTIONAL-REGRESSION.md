# FP-0002 — Services General Pass 2 Functional Regression

**Date:** 2026-06-26  
**Method:** Playwright capture + manual hook audit

| Check | Result |
| ----- | ------ |
| Header / mobile menu hooks | Present (unchanged partial) |
| Hero CTA `data-modal-open` | Present |
| Hub CTA ×4 | Present (`services-addictions` … `services-genotyping`) |
| Category service links | 14 WordPress-ready `/slug/` hrefs |
| Founder / Comfort / FAQ / Final form | Reused unchanged |
| Console errors (Services) | 0 |
| Console errors (Home smoke) | 0 |
| Missing requests | 0 |
| Duplicate IDs | Not detected in spot check |
| Broken local links | 0 |

**Home regression:** `index.html` smoke — no console errors, no failed requests.

**Result:** PASS
