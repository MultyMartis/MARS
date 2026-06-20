# REPORT — WF-R01.3 G2-R1 W3-A PROMO SOURCE INVENTORY AND CONTRACT CONFIRMATION

**Artifact ID:** WF-R01.3 G2-R1 W3-A PROMO Source Inventory (v1)  
**Date:** 2026-06-20  
**Mode:** documentation-only · source-inventory-only · contract-confirmation-only  
**Honesty boundary:** **Not** implementation · **not** RPC accrual · **not** G2 evaluation

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Inventory state** | **PUBLISHED** — [wf-r01-3-g2-r1-w3-promo-source-inventory-v1.md](../projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-source-inventory-v1.md) |
| **SERVICES selection** | Primary: `category-grid.html` · Secondary: `benefits.html`, `segments-applications-grid.html` |
| **SERVICES quality** | **Q3** (primary) |
| **TEAM selection** | Primary: `testimonials.html` card anatomy · Secondary: FP-0002 BLK-026 doc, numeric design rules |
| **TEAM quality** | **Q2** (primary — adaptation required) |
| **ABOUT selection** | Primary: `benefits.html` header/lead shell (composite) · Secondary: `page-intro.html`, FP-0002 BLK-036–038 doc |
| **ABOUT quality** | **Q2** (primary — composite adaptation) |
| **W3-B authorization** | **W3-B IMPLEMENTATION AUTHORIZED** |
| **TEAM readiness** | **READY WITH CONSTRAINTS** |
| **ABOUT readiness** | **READY WITH CONSTRAINTS** |
| **RC** | **32/32** — unchanged |
| **RPC** | **23/32** — unchanged |
| **RSC** | **3/10** — unchanged |
| **SC** | **LANDING PASS · CATALOG PARTIAL** — unchanged |
| **PC** | **1/1 LANDING · 1/1 CATALOG corridor** — unchanged |
| **G2-R1 state** | **CHARTERED · NOT IMPLEMENTED · NOT COMPLETE** |
| **G2 state** | **CHARTERED · READY WITH BLOCKERS · NOT EVALUATED · NOT PASSED · NOT CLOSED** |
| **Next task** | **WF-R01.3 G2-R1 W3-B — SERVICES Reference Partial** |

---

## 2. Git Safety

| Field | Value |
|-------|-------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD before task** | `9567b64` — foundry: accept G2-R1 W3 promo reference charter |
| **G2-R1 charter remote state** | Remote branch tip **`9567b64`** — charter present on remote |
| **Staged files** | **None** at task start |
| **Foreign WIP** | **Present** (modified/untracked across repo) — **excluded** from commit scope |
| **Selective scope** | 4 documentation files only |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| G2-R1 W3 charter | `projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-reference-completion-charter-v1.md` | W3 normative authority |
| G2-R1 charter pass | `reports/wf-r01-3-g2-r1-w3-promo-charter-pass-v1.md` | ACCEPTED snapshot |
| G2 formal gate charter | `projects/mars-website-factory/wf-r01-3-g2-formal-gate-pass-charter-v1.md` | Parent gate |
| G2 charter pass | `reports/wf-r01-3-g2-formal-gate-pass-charter-pass-v1.md` | G2 readiness |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | Metrics rules |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 semantics |
| Program design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | Wave map |
| Post-G1 track selection | `reports/wf-r01-3-post-g1-track-selection-v1.md` | G2 composite semantics |
| Registry expansion design | `reports/foundry-registry-expansion-program-design-v1.md` | Programme context |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Host shell order |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | Shell slots |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | Scaffold boundary |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Identity SSOT |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Library inventory |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Gap rows |
| Site-Type Block Matrix | `workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md` | Applicability |
| Page-Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | Page applicability |
| Catalog inventory precedent | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | Q-model precedent |

---

## 4. Registry Reconfirmation

| Target | block_id | Family | Current state | RPC eligible | Competing partial |
|--------|----------|--------|---------------|--------------|-------------------|
| **SERVICES** | `SERVICES` | F3 · COMPANY | Not implemented | Yes | **None** |
| **TEAM** | `TEAM` | F3 · COMPANY | Not implemented | Yes | **None** |
| **ABOUT** | `ABOUT` | F3 · COMPANY | Not implemented | Yes | **None** |

---

## 5. Search Boundary

- **Included locations:** reference workspace partials/pages/scss; Triumph v2/v6/landing workspaces; FP-0002 doc-first case; programme authority docs
- **Excluded locations:** `.recovery-temp/`; `incoming/mig/` production dumps; BZPM live captures; external sites
- **Search terms:** services, team, about, specialists, segments, advantages, page-intro, BLK-010/026/036
- **Source count:** 16 candidates evaluated across three targets (6 + 5 + 5)
- **No-external-research confirmation:** **Yes**

---

## 6. Source Quality Model

| Quality | Definition |
|---------|------------|
| **Q3** | Implemented, validated, reusable and sufficiently universal |
| **Q2** | Implemented or well-documented, structurally useful, requires adaptation/sanitization |
| **Q1** | Prototype or partial evidence; corroboration only |
| **Q0** | Weak, obsolete, incompatible or misleading |
| **SAFE UNKNOWN** | Relevance or authority cannot be confirmed |

---

## 7. SERVICES Candidate Sources

| Source ID | Exact path | Type | Quality | Reusable structure | Rejected content | Decision |
|-----------|------------|------|---------|-------------------|------------------|----------|
| SVC-CAND-01 | `workspaces/website-factory-reference-v1/src/partials/components/category-grid.html` | HTML | **Q3** | Card collection; title; description; media; link | Catalog identity; counts | **primary** |
| SVC-CAND-02 | `workspaces/website-factory-reference-v1/src/partials/sections/benefits.html` | HTML | **Q3** | Header + icon item grid | Benefit framing | **secondary** |
| SVC-CAND-03 | `workspaces/triumph-manipulator-landing-v2/src/partials/sections/segments-applications-grid.html` | HTML | **Q2** | Media card grid + lead | Client taxonomy/copy | **secondary** |
| SVC-CAND-04 | `workspaces/triumph-manipulator-landing/src/partials/sections/advantages.html` | HTML | **Q2** | Minimal list | Too weak | **rejected** |
| SVC-CAND-05 | `workspaces/triumph-manipulator-landing-v6/.../screen-02-tasks.html` | HTML | **Q0** | Task grid | Wrong identity | **rejected** |
| SVC-CAND-06 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md` | Doc | **Q1** | IA notes only | No HTML | **rejected** |

---

## 8. SERVICES Selection

- **Primary source:** `category-grid.html` + `_category-grid.scss`
- **Secondary sources:** `benefits.html`; `segments-applications-grid.html`
- **Rejected sources:** advantages starter; v6 tasks; FP-0002 doc-only; BZPM catalog grids
- **Sanitization:** `wf-services` namespace; fictional copy; strip counts; `#` links
- **Contract implications:** Card-grid canonical minimum; ≥3 items in host; no JS
- **Final quality:** **Q3**

---

## 9. TEAM Candidate Sources

| Source ID | Exact path | Type | Quality | Reusable structure | Rejected content | Decision |
|-----------|------------|------|---------|-------------------|------------------|----------|
| TEAM-CAND-01 | `workspaces/website-factory-reference-v1/src/partials/sections/testimonials.html` | HTML | **Q2** | Avatar; name; role card | Quotes; ratings | **primary** |
| TEAM-CAND-02 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md` (BLK-026) | Doc | **Q1** | Grid semantics | No HTML | **secondary** |
| TEAM-CAND-03 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-NUMERIC-DESIGN-RULES-v2.md` | Doc | **Q1** | Responsive tokens | Not HTML | **secondary** |
| TEAM-CAND-04 | `workspaces/triumph-manipulator-landing-v2/.../trust-reviews.html` | HTML | **Q0** | Reviews | TESTIMONIALS identity | **rejected** |
| TEAM-CAND-05 | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` | HTML dump | **Q0** | Forensic | PII risk | **rejected** |

---

## 10. TEAM Selection

- **Primary source:** `testimonials.html` member-card anatomy
- **Secondary sources:** FP-0002 BLK-026; numeric design rules v2
- **Rejected sources:** trust-reviews; mig snapshots; full testimonials block
- **Privacy/sanitization:** Fictional names/roles only; placeholder portraits; no real PII
- **Contract implications:** Member grid; ≥3 fictional members; no modal bios; no JS
- **Final quality:** **Q2**

---

## 11. ABOUT Candidate Sources

| Source ID | Exact path | Type | Quality | Reusable structure | Rejected content | Decision |
|-----------|------------|------|---------|-------------------|------------------|----------|
| ABT-CAND-01 | `workspaces/website-factory-reference-v1/src/partials/sections/benefits.html` | HTML | **Q2** | Header + lead shell | Benefits grid body | **primary** |
| ABT-CAND-02 | `workspaces/triumph-manipulator-landing-v2/src/partials/sections/page-intro.html` | HTML | **Q2** | Lead paragraph density | Page H1 semantics | **secondary** |
| ABT-CAND-03 | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/FP-0002-BLOCK-INVENTORY-v1.md` (BLK-036–038) | Doc | **Q1** | Narrative zones | No HTML | **secondary** |
| ABT-CAND-04 | `workspaces/triumph-manipulator-landing-v6/.../screen-01-hero.html` | HTML | **Q0** | Hero stack | HERO identity | **rejected** |
| ABT-CAND-05 | `workspaces/triumph-manipulator-landing-v2/src/pages/about.html` | Page | **Q0** | Starter page mix | Wrong composition | **rejected** |

---

## 12. ABOUT Selection

- **Primary source:** `benefits.html` header/lead pattern (composite with new highlights region)
- **Secondary sources:** `page-intro.html`; FP-0002 about narrative docs
- **Rejected sources:** v6 hero; starter about page; trust/process embeds
- **Sanitization:** Fictional organisation narrative and facts
- **Contract implications:** Lead + narrative + ≥2 highlights; optional media; no JS
- **Final quality:** **Q2**

---

## 13. Sanitization Matrix

| Content/data | Allowed | Required action |
|--------------|---------|-----------------|
| Structural hierarchy | Yes | Normalize to charter minimum |
| CSS/layout idea | Yes | Rebuild in WF namespace |
| Client brand | No | Remove |
| Real employee data | No | Fictional personas |
| Real portrait | No by default | Neutral placeholder |
| Production URL | No | Replace with `#` |
| Real commercial claim | No | Neutral copy |
| CMS/backend logic | No | Reject |
| Analytics/tracking | No | Reject |
| Project-specific classes | No | Rename to `wf-*` |
| Licensed media | Only if approved | Otherwise replace |
| Catalog counts | No | Strip from SERVICES adaptation |
| Testimonial quotes/ratings | No | Strip for TEAM adaptation |

---

## 14. Vocabulary Contract Confirmation

### SERVICES

Purpose, ownership, internal units, required/optional content, and exclusions **match** BLOCK-REGISTRY-v1 and G2-R1 charter §17. **No drift.**

### TEAM

Purpose, ownership, member units, privacy policy, and exclusions **match** authority. **No drift.**

### ABOUT

Purpose, ownership, narrative + highlights regions, and exclusions **match** authority. **No drift.**

### PROCESS and neighboring blocks

`PROCESS` excluded from W3 implementation (existing reference). TRUST/TESTIMONIALS/CONTACTS/LEAD_FORM/CTA remain separate owners.

**Vocabulary reconciliation:** **NOT REQUIRED**

---

## 15. Block Boundary Confirmation

| Concern | Owner | Source extraction rule |
|---------|-------|------------------------|
| Service directions | SERVICES | Card/list collection layer only |
| Workflow steps | PROCESS | Reject task/step sources |
| People and roles | TEAM | Member card anatomy; strip quotes |
| Organisation narrative | ABOUT | Header/lead/narrative; reject hero stacks |
| Proof and reassurance | TRUST / CASES / TESTIMONIALS | Do not import |
| Benefits | BENEFITS / FEATURES | Layout convention only |
| Contact information | CONTACTS | Not embedded |
| Lead capture | LEAD_FORM | Not embedded |
| Commercial action | CTA | Optional link only |

---

## 16. Applicability Confirmation

### Site types

| Block | Surface | Matrix state | Decision |
|-------|---------|--------------|----------|
| SERVICES | PROMO | REQ | Authorized |
| SERVICES | CORPORATE | REQ | Authorized |
| SERVICES | LANDING/CATALOG/ECOMMERCE | FORBIDDEN | N/A for reference |
| TEAM | PROMO/CORPORATE | OPT | Authorized |
| TEAM | LANDING/CATALOG/ECOMMERCE | FORBIDDEN | N/A |
| ABOUT | PROMO/CORPORATE | REQ | Authorized |
| ABOUT | LANDING/CATALOG/ECOMMERCE | FORBIDDEN | N/A |

### Page types

| Block | Surface | Matrix state | Decision |
|-------|---------|--------------|----------|
| SERVICES | HOME_PAGE (PROMO/CORPORATE) | REQ | Authorized |
| TEAM | ABOUT_PAGE | OPT | Authorized |
| ABOUT | ABOUT_PAGE | REQ | Authorized |
| All three | LANDING/CATALOG/PRODUCT/SERVICE money pages | FORB/N/A | Not applicable |

**Matrix drift:** None recorded.

---

## 17. Canonical Implementation Paths

- **SERVICES partial:** `src/partials/components/services.html`
- **TEAM partial:** `src/partials/components/team.html`
- **ABOUT partial:** `src/partials/components/about.html`
- **SCSS:** `src/scss/components/_services.scss`, `_team.scss`, `_about.scss`
- **Host:** `src/pages/promo-block-references.html` (W3-B initial creation)
- **JS decision:** None (all three)
- **Build integration:** `@use` imports in `src/scss/main.scss`; gulp build PASS required

---

## 18. Bounded Host Strategy

- **Selected option:** Option A — combined host
- **Composition:** HEADER_NAV · MAIN (SERVICES → TEAM → ABOUT) · FOOTER · LEGAL_LINKS
- **Hook policy:** One `data-block-id` per section root
- **Scaffold boundary:** Not a page-type scaffold; not RSC/PC/SC evidence
- **Coverage boundary:** Host accrues zero metrics
- **Incremental build:** W3-B host + SERVICES; W3-C adds TEAM; W3-D adds ABOUT

---

## 19. Implementation Wave Order

| Wave | Target | Readiness | Expected output |
|------|--------|-----------|-----------------|
| W3-A | Inventory | **COMPLETE** | Inventory + this REPORT |
| W3-B | SERVICES | **AUTHORIZED** | Partial + SCSS + host + REPORT |
| W3-C | TEAM | **READY WITH CONSTRAINTS** | Partial + SCSS + host hook + REPORT |
| W3-D | ABOUT | **READY WITH CONSTRAINTS** | Partial + SCSS + host hook + REPORT |
| W3-E | Exit | Pending W3-D | G2-R2 handoff REPORT |

---

## 20. W3-B Authorization

```text
W3-B IMPLEMENTATION AUTHORIZED
```

**Rationale:** SERVICES Registry row confirmed; primary source **Q3** (`category-grid.html`); universal contract and paths confirmed; sanitization and bounded-host strategy documented; no vocabulary conflict; no new Registry identity; applicability does not block implementation.

---

## 21. TEAM and ABOUT Readiness

- **W3-C state:** **READY WITH CONSTRAINTS** — primary Q2; no native TEAM HTML; testimonial-layer stripping required
- **W3-D state:** **READY WITH CONSTRAINTS** — primary Q2 composite; highlights region to be authored in implementation
- **Constraints:** Fictional data only; no Triumph v6 PROMO multi-page HTML available
- **Remaining unknowns:** FP-0002 HTML for BLK-026/036 (**SAFE UNKNOWN** — doc-only corroboration)

---

## 22. Coverage Accounting

- **RC:** 32/32 — unchanged
- **RPC:** 23/32 — unchanged
- **RSC:** 3/10 — unchanged
- **SC:** LANDING PASS · CATALOG PARTIAL — unchanged
- **PC:** 1/1 LANDING · 1/1 CATALOG corridor — unchanged
- **Potential future delta:** +3 RPC max after W3-B/C/D (26/32)
- **No-accrual confirmation:** W3-A accrues **zero**

---

## 23. Files Created

| File | Purpose |
|------|---------|
| `projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-source-inventory-v1.md` | Canonical W3 source inventory |
| `reports/wf-r01-3-g2-r1-w3-a-promo-source-inventory-v1.md` | W3-A execution REPORT |

---

## 24. Files Modified

| File | Change |
|------|--------|
| `projects/mars-website-factory/roadmap.md` | W3-A COMPLETE; inventory PUBLISHED; next W3-B |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | W3-A COMPLETE; inventory link; next W3-B |

---

## 25. Validation

- [x] Registry identities confirmed
- [x] Competing partials absent
- [x] Local source search completed
- [x] Primary sources exist on disk
- [x] Quality assigned with rationale
- [x] Secondary sources not promoted over primary
- [x] Rejected sources explained
- [x] No real PII transferred into inventory
- [x] Vocabulary matches authority — no reconciliation STOP
- [x] Applicability verified against matrices
- [x] Future paths conflict-free
- [x] Host not declared scaffold
- [x] W3-B authorization documented
- [x] Coverage unchanged
- [x] No implementation files touched
- [x] Registry not modified

---

## 26. Documentation State

- **roadmap:** W3-A COMPLETE; next W3-B
- **OPERATIONAL-INDEX:** W3-A COMPLETE; inventory PUBLISHED
- **G2-R1 state:** CHARTERED · NOT IMPLEMENTED · NOT COMPLETE
- **Next task:** WF-R01.3 G2-R1 W3-B — SERVICES Reference Partial

---

## 27. Git Result

| Field | Value |
|-------|-------|
| **Commit hash** | `57903e6` |
| **Commit message** | `foundry: publish G2-R1 W3 promo source inventory` |
| **Push result** | **Success** — `9567b64..57903e6` → `origin/mars/post-cycle8-live-tests` |
| **Files committed** | 4 — inventory v1, W3-A REPORT, roadmap, OPERATIONAL-INDEX |
| **No foreign lane confirmation** | **Confirmed** — staged diff contained documentation only; no `src/`, block-registry, or recovery paths |

---

## 28. Drift and Risks

| Severity | Finding | Effect | Destination |
|----------|---------|--------|-------------|
| Medium | Triumph v6 lacks PROMO W3 HTML | Factory-internal primaries selected | This inventory |
| Medium | TEAM/ABOUT lack Q3 monolithic sources | W3-C/D adaptation overhead | W3-C/D waves |
| Low | SERVICES adapted from catalog card grid | Sanitization discipline required | W3-B wave |

---

## 29. Final Status

**COMPLETE**

---

## 30. Next Task

```text
WF-R01.3 G2-R1 W3-B — SERVICES Reference Partial
```

**Not executed in this pass.**

---

## 31. Exact Evidence Paths

See inventory §26 Evidence Paths — full list published in [wf-r01-3-g2-r1-w3-promo-source-inventory-v1.md](../projects/mars-website-factory/wf-r01-3-g2-r1-w3-promo-source-inventory-v1.md).

---

## 32. Stop Confirmation

```text
W3-B implementation: NOT STARTED
SERVICES partial: NOT CREATED
TEAM partial: NOT CREATED
ABOUT partial: NOT CREATED
PROMO bounded host: NOT CREATED
Registry: NOT MODIFIED
Coverage metrics: UNCHANGED
G2-R1 exit: NOT STARTED
G2 formal evaluation: NOT EXECUTED
G2 PASS: NOT GRANTED
Production readiness: NOT CLAIMED
```

---

*W3-A REPORT: `reports/wf-r01-3-g2-r1-w3-a-promo-source-inventory-v1.md` · v1 · 2026-06-20*
