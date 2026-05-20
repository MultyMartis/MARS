# REPORT — Wave 6 real extraction (cases block)

**Mode:** Standard  
**Scope:** Extract `cases` from Triumph V2 `trust-cases-social-proof` (case list only) into reference library.

**Discipline:** [implementation-extraction-discipline-v1.md](../implementation-extraction-discipline-v1.md) · **Tier:** validated — [block-quality-tiers-v1.md](../block-quality-tiers-v1.md)

---

## Extraction record

| Field | Value |
|-------|--------|
| **Source** | `workspaces/triumph-manipulator-landing-v2` — `trust-cases-social-proof.html` (`.trust-cases__list` articles only) |
| **block_id** | `cases` (registry row #5) |
| **Not extracted** | Chat correspondence column, proof aside, legal INN rows, Font Awesome, client photos, geo claims |
| **Neutralized** | Russian copy, client names, message bubbles, regulated identifiers |
| **Structural kept** | Eyebrow + title + lead; stacked case cards with media + tag + title + body + meta |
| **Added to reference** | `partials/sections/cases.html`, `scss/sections/_cases.scss`, wired in `index.html` + `main.scss` |

---

## Criterion validation

| Criterion | Result |
|-----------|--------|
| Role clarity | `cases` in block-registry-v0 — PASS |
| Second use | B2B / service landings — PASS |
| Survivability | Static-only — PASS |
| Token hygiene | Foundation tokens only — PASS |
| Content neutral | Anonymized sectors — PASS |
| Responsive | 1-col mobile; media+body grid ≥768 — PASS (SCSS) |
| Forge compatible | Gulp partial — PASS |
| Conversion ownership | Secondary CTA to `#lead-form` — PASS |

---

## Token cleanup

- [x] No raw `#hex`  
- [x] Spacing/radius from tokens  
- [x] No z-index

---

## JS isolation

- [x] No section JS  
- [x] No FA dependency

---

## Survivability checks

- [x] `data-section` + `data-block-id="cases"`  
- [ ] Swap demo — **SAFE UNKNOWN**

---

## Responsiveness checks

| Viewport | Result |
|----------|--------|
| 375px | Single column stack — **PASS** (intent) |
| 768px | Side-by-side media + body — **PASS** |
| Desktop | Container bound — **PASS** |

---

## Build verification

```text
npm run build @ website-factory-reference-v1 — PASS (2026-05-21, agent-run)
```

---

## Anti-poisoning avoided

- No fake chat screenshots  
- No third-party review platform logos  
- No `.trust-case__correspondence` markup  
- No `.tm-section` / Triumph BEM in library

---

## SAFE UNKNOWN

- Image aspect ratios when real assets added — project-local  
- E-E-A-T review for case claims — HITL per client

---

## Risks

- Full Triumph trust screen also needs `trust_block` / `reviews` — not merged into this block  
- Operators may confuse `cases` with `social_proof` — curated index separates roles

---

## Files touched

**Created:**

- `workspaces/website-factory-reference-v1/src/partials/sections/cases.html`
- `workspaces/website-factory-reference-v1/src/scss/sections/_cases.scss`

**Updated:**

- `workspaces/website-factory-reference-v1/src/pages/index.html`
- `workspaces/website-factory-reference-v1/src/scss/main.scss`

*Wave 6 — third real operational extraction (cases).*
