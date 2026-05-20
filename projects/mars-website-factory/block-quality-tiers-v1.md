# Block quality tiers v1 (Wave 6)

**Status:** **documented** — lightweight operational quality model for Website Factory reusable blocks.  
**Registry:** [block-registry-v0.md](block-registry-v0.md) · **Extraction:** [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md).  
**Catalog:** [curated-library-index-v1.md](curated-library-index-v1.md).

**Not:** automated tier enforcement, **not** a scoring engine, **not** governance expansion.

---

## Tier model

| Tier | Meaning | Library admission |
|------|---------|-------------------|
| **experimental** | Structure exists; not production-proven in Factory | Reference only; **no** client template default |
| **validated** | Real extraction or battle-tested adoption; QA evidence on record | Curated library; pilot adoption allowed |
| **battle-tested** | Survived replacement + freeze on reference or ≥1 pilot | Default for high-traffic commercial landings |
| **canonical** | Operator default; documented in golden slice + consolidation map | Copy without HITL for structure; brand tokens still per client |

**Direction:** promote **up** only with evidence; demote on drift or failed pilot (human decision).

---

## Promotion criteria

| From → To | Requires |
|-----------|----------|
| experimental → validated | Real extraction REPORT **or** reference build PASS + [operational-qa-entry-v1.md](operational-qa-entry-v1.md) compact PASS + survivability static/replace check |
| validated → battle-tested | [section-swap-demo-flow-v1.md](section-swap-demo-flow-v1.md) run **or** pilot adoption REPORT with replacement PASS |
| battle-tested → canonical | Golden slice pointer + consolidation map entry + no open HARDENING FINDINGS on block |

**Blockers (any tier):** client trademarks in library, fake metrics, Triumph-specific selectors, missing `data-block-id`, registry row missing.

---

## Extraction criteria (entry to library)

All from [implementation-extraction-discipline-v1.md](implementation-extraction-discipline-v1.md):

- Maps to `block_id` in block registry  
- Second-use plausible  
- Neutralized copy/assets  
- Token pass complete  
- No section JS **or** lifecycle `destroy` documented  
- Extraction REPORT committed under `operational-examples/`

**First library commit:** tier = **validated** (not canonical until battle-tested).

---

## Survivability requirements

| Check | experimental | validated+ |
|-------|--------------|------------|
| `data-section` + `data-block-id` | required | required |
| `destroySection` safe | documented | tested or static-only |
| No leaked global listeners | required | required |
| Replacement partial path stable | required | required |

---

## Responsive requirements

- Spot-check **375 / 768 / desktop** before tier ≥ validated  
- Primary CTA visible at 375 for conversion blocks  
- No mandatory horizontal scroll for core content  
- Record gaps as **SAFE UNKNOWN** in extraction REPORT

---

## Lifecycle requirements

- Partial: `partials/sections/{block_id}.html`  
- SCSS: `scss/sections/_{block_id}.scss` in `main.scss`  
- Optional JS: `js/sections/{block_id}.js` + `data-module` only when needed  
- **Freeze:** tier ≥ validated blocks need [freeze-discipline-v1.md](freeze-discipline-v1.md) section row before client delivery freeze

---

## QA evidence requirements

| Tier | Minimum evidence |
|------|------------------|
| experimental | `npm run build` PASS |
| validated | build PASS + compact QA checklist + extraction REPORT |
| battle-tested | above + swap demo or pilot REPORT |
| canonical | above + golden slice mention + consolidation map |

---

## Adoption requirements

| Tier | Pilot project | Production freeze |
|------|---------------|-------------------|
| experimental | HITL only | not allowed as library copy |
| validated | allowed with charter | section freeze after QA |
| battle-tested | recommended default | workspace freeze when 3+ validated blocks |
| canonical | default bootstrap blocks | foundation freeze rules apply |

---

## Anti-entropy rules

1. **No** new `block_id` without registry row or explicit REPORT gap.  
2. **No** duplicate partials (`pricing_v2`, `faq2`) — replace in place with REPORT.  
3. **Max one** extraction REPORT per block per wave; append fixes to same file if minor.  
4. **Curated surface** — [curated-library-index-v1.md](curated-library-index-v1.md) is the only default library table (not block-registry rows alone).  
5. Demote tier when implementation diverges from registry without [registry-sync-discipline-v1.md](registry-sync-discipline-v1.md) update.

---

*Wave 6 — block quality tier discipline.*
