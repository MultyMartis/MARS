# FP-0002 Service Subdivision — PNG Runtime Comparison v1 (before fixes)

Captured: `runtime-crops-before/` @ preview `http://127.0.0.1:4174/usluga-podrazdel-v1.html`  
Desktop viewport 1437px; mobile 380px. DOM-scoped screenshots.

## Desktop

| № | Block | Heading match | Text match | Structure | Count | Asset | Order | Action |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Header/Hero | PASS | PASS (Lorem) | PASS | PASS | PASS | PASS | KEEP |
| 2 | Upper nav | PASS | PASS | PASS | PASS | PASS | PASS | KEEP |
| 3 | Intro (`service-subdivision-intro-v1`) | FAIL | FAIL | FAIL | FAIL (3 cards) | FAIL | FAIL | **REMOVE_RUNTIME_BLOCK** |
| 4 | Procedure (`service-subdivision-procedure-v1`) | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **REMOVE_RUNTIME_BLOCK** |
| 5 | Dependencies | PASS heading | FAIL labels | FAIL layout | FAIL (4 wrong rows) | FAIL | FAIL | **REPLACE_CONTENT** + **CORRECT_COUNT** + **CORRECT_DESKTOP_LAYOUT** |
| 6 | Nature | PASS heading | FAIL (missing subheads) | FAIL | FAIL (missing НЕЙРОБИОЛОГИЯ/ГЕНОТИПИРОВАНИЕ) | FAIL | PASS | **REPLACE_COMPONENT** + **REPLACE_CONTENT** |
| 7 | CTA-01 (`#service-subdivision-start`) | UNKNOWN | UNKNOWN | UNKNOWN | — | — | — | **CORRECT_DESKTOP_LAYOUT** (capture selector mismatch) |
| 8 | Program | PARTIAL | FAIL (non-Lorem body) | PARTIAL | PASS (4) | PASS | PASS | **REPLACE_CONTENT** |
| 9 | Team/stats | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | **REPLACE_COMPONENT** (needs crop diff) |
| 10 | Stages | PARTIAL | PARTIAL | PASS | PASS (4) | PASS | FAIL (design after program; runtime same — verify team order) | **REORDER** (team vs stages) |
| 11 | CTA-02 | UNKNOWN | UNKNOWN | UNKNOWN | — | — | — | CORRECT_DESKTOP_LAYOUT |
| 12 | Approach | UNKNOWN | UNKNOWN | UNKNOWN | — | — | — | REPLACE_COMPONENT |
| 13 | Specialists | PARTIAL | UNKNOWN | PARTIAL | UNKNOWN | UNKNOWN | PASS | REUSE_WITH_SCOPED_VARIANT |
| 14 | Founder | PARTIAL | UNKNOWN | PARTIAL | PASS | PASS | PASS | REUSE_WITH_CONTENT |
| 15 | Comfort | PARTIAL | UNKNOWN | PARTIAL | UNKNOWN | UNKNOWN | PASS | REUSE_WITH_SCOPED_VARIANT |
| 16 | Reviews | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | PASS | REUSE_WITH_CONTENT |
| 17 | FAQ | PASS heading | UNKNOWN | PARTIAL | UNKNOWN | PASS | PASS | REUSE_WITH_CONTENT |
| 18 | Final form | PASS heading | PARTIAL | PASS | PASS | PASS | PASS | REUSE_WITH_CONTENT |
| 19 | Footer | PASS | PASS | PASS | 1 | PASS | PASS | KEEP |

## Mobile

| № | Block | Heading | Text | Structure | Count | Asset | Order | Action |
|---:|---|---:|---:|---:|---:|---:|---:|---|
| 1 | Hero | FAIL | FAIL | FAIL | — | PASS | FAIL | CORRECT_MOBILE_LAYOUT + REPLACE_CONTENT |
| 2 | Upper | PARTIAL | PASS | PASS | PASS | — | FAIL | CORRECT_MOBILE_LAYOUT |
| 3 | Intro | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **REMOVE_RUNTIME_BLOCK** |
| 4 | Procedure | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | **REMOVE_RUNTIME_BLOCK** |
| 5 | Dependencies | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | REPLACE_CONTENT + CORRECT_COUNT |
| 6 | Nature | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | REPLACE_COMPONENT |
| 7–18 | Lower blocks | — | — | — | — | — | FAIL (not verified per-block) | **INCOMPLETE** — requires per-crop mobile pass |

**Gate:** Desktop comparison complete for upper/mid blocks with confirmed FAIL on intro, procedure, dependencies content/count, nature structure. Mobile lower blocks not fully crop-verified in this pass → overall **INCOMPLETE**.
