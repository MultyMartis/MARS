# REPORT — WF-R01.3.5 CORPORATE & COMMERCE REFERENCE SLICES CHARTER PASS

**Date:** 2026-06-21  
**Mode:** authority-only · charter-only · scope-reconciliation-only  
**Branch:** `mars/post-cycle8-live-tests`

---

## 1. Result

| Field | Value |
|-------|-------|
| **Status** | **COMPLETE** |
| **Charter decision** | **ACCEPTED** |
| **Charter path** | `projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md` |
| **Package identity** | **WF-R01.3.5 — Corporate & Commerce Reference Slices** |
| **Parent programme** | **WF-R01.3 — Reference Implementation Expansion** (**OPEN · DESIGN · CONTINUES**) |
| **Entry coverage** | RC **32/32** · RPC **26/32** · RSC **7/11** · SC **LANDING/CATALOG/PROMO PASS** · PC **LANDING/CATALOG/PROMO 1/1** |
| **RPC gaps** | **6 binding** — `CART` · `CHECKOUT` · `PAYMENT` · `DELIVERY` · `CERTIFICATES` · `PARTNERS` |
| **G3 target** | RPC **≥29/32** — minimum **+3** (`CART` · `CHECKOUT` · `PAYMENT`) |
| **G4 target** | RPC **32/32** + RSC/SC/PC/blueprint-instance obligations per Coverage Model |
| **W6 decision** | Four commerce **`block_id` units** + utility-route scaffolds — **not** four new page types |
| **W7 decision** | Two **binding** corporate gaps + three **hygiene** partials (`FEATURES` · `REVIEWS` · `MAP`) |
| **Corporate slice** | CORPORATE `site_type_code` reference blueprint-instance + existing page-type scaffolds |
| **Ecommerce slice** | ECOMMERCE staging chain + catalog inheritance + cart/checkout utility references |
| **Page-type decision** | **PARTIAL EXPANSION IN DEDICATED WAVES** — no Registry mutation in charter pass |
| **Block-authority decision** | All W6/W7 units have canonical rows — **implementation only** |
| **SC decision** | **EXISTING SC DIMENSIONS ONLY** |
| **PC decision** | **PC ADDENDUM REQUIRED** for ECOMMERCE corridor before accrual |
| **RSC decision** | **NO DENOMINATOR CHANGE** (11) in charter pass |
| **Package state** | **CHARTERED · NOT IMPLEMENTED · NOT COMPLETE** |
| **G3 state** | **PLANNED · NOT EVALUATED · NOT PASSED · NOT CLOSED** |
| **Next task** | **WF-R01.3.5 W6-A — Commerce Block Reference Preflight** |

---

## 2. Git Safety

| Field | Value |
|-------|-------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD** | Contains `1d38be8` (G2 closure) · `29631b7` (lifecycle decision) |
| **G2/lifecycle remote state** | Present on branch history |
| **Staged files** | **None** at pass open |
| **Foreign WIP** | **Present** (governance, pilots, unrelated projects) — **excluded** from commit |
| **Selective scope** | Charter + report + roadmap + OPERATIONAL-INDEX only |

---

## 3. Authority Reviewed

| Document | Path | Role |
|----------|------|------|
| Reference expansion program design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | R01.3.5 · W6–W7 · gates |
| Coverage Model charter | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | G0–G4 · five dimensions |
| Post-G2 lifecycle decision | `projects/mars-website-factory/wf-r01-3-post-g2-lifecycle-decision-v1.md` | CONTINUE into R01.3.5 |
| G2 handoff | `reports/wf-r01-3-g2-to-wf-r01-3-5-handoff-v1.md` | Entry metrics |
| G2 operator closure | `projects/mars-website-factory/wf-r01-3-g2-operator-sign-off-and-gate-closure-v1.md` | G2 CLOSED |
| G2 formal evaluation | `projects/mars-website-factory/wf-r01-3-g2-formal-evaluation-decision-v1.md` | RPC 26/32 · six-gap debt |
| G2-R5 evidence assembly | `projects/mars-website-factory/wf-r01-3-g2-r5-gate-evidence-assembly-v1.md` | Gap table reconciliation |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | 32 rows |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Missing partials |
| Page Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | Utility routes |
| Page Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | 11 types |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | Shell policy |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC chain |
| Roadmap · OPERATIONAL-INDEX | `projects/mars-website-factory/roadmap.md` · `OPERATIONAL-INDEX.md` | Operator sync |

---

## 4. Duplicate Charter Check

| Field | Value |
|-------|-------|
| **Search terms** | `wf-r01-3-5` · `corporate-commerce-reference` · `w6-w7-charter` · `g3-reference-slices` |
| **Existing artefacts** | Program design § R01.3.5 · G2-23 handoff · lifecycle decision |
| **Competing charter** | **None** |
| **Decision** | **Proceed** — publish sole ACCEPTED charter |

---

## 5. Package Identity

| Field | Value |
|-------|-------|
| **ID** | WF-R01.3.5 |
| **Name** | Corporate & Commerce Reference Slices |
| **Parent** | WF-R01.3 |
| **Lifecycle** | **CHARTERED · NOT IMPLEMENTED · NOT COMPLETE** |
| **Predecessor** | Gate G2 closure |
| **Gate relationship** | Primary delivery path to **G3** then **G4** |
| **Purpose** | W6–W7 reference slices for commerce + corporate coverage |

---

## 6. Coverage Freeze

```text
RC  = 32/32
RPC = 26/32
RSC = 7/11
SC  = LANDING PASS · CATALOG PASS · PROMO PASS
PC  = 1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor
```

**No accrual in charter pass.**

---

## 7. RPC Unit Reconciliation

| Candidate | Registry | Eligible | Current maturity | Earned | Gap |
|-----------|----------|----------|------------------|--------|-----|
| CART | `CART` | Yes | None | No | **Binding** |
| CHECKOUT | `CHECKOUT` | Yes | None | No | **Binding** |
| PAYMENT | `PAYMENT` | Yes | None | No | **Binding** |
| DELIVERY | `DELIVERY` | Yes | None | No | **Binding** |
| CERTIFICATES | `CERTIFICATES` | Yes | None | No | **Binding** |
| PARTNERS | `PARTNERS` | Yes | None | No | **Binding** |
| MAP | `MAP` | Yes | CONTACTS substitute | Substitution | Hygiene |
| FEATURES | `FEATURES` | Yes | BENEFITS substitute | Substitution | Hygiene |
| REVIEWS | `REVIEWS` | Yes | TESTIMONIALS substitute | Substitution | Hygiene |

- **Earned total:** **26/32**
- **Gap total (binding register):** **6**
- **Arithmetic:** **26 + 6 = 32** ✓
- **6/7 discrepancy decision:** G2-R5 lists **7 names** omitting FEATURES/REVIEWS; binding count is **6**. **MAP** is **W7 hygiene**, not a seventh binding RPC gap. See charter §11.

---

## 8. G3 Threshold

| Criterion | Current | Required | Gap |
|-----------|---------|----------|-----|
| RPC | 26/32 | ≥29/32 | −3 |
| RC | 32/32 | 32/32 | 0 |
| RSC | 7/11 | CORPORATE/ECOMMERCE scaffolds | Open |
| SC CORPORATE | Not PASS | G3 pilot | Open |
| SC ECOMMERCE | Not PASS | Staging HITL | Open |
| PC | 3 corridors | Maintain + ECOMMERCE addendum | Planning |
| Build | PASS at G2 | PASS per wave | Revalidate |
| G3 evaluation | Not executed | G3-E + G3-F | Open |

---

## 9. G4 Threshold

| Criterion | Current | Required | Gap |
|-----------|---------|----------|-----|
| RPC | 26/32 | 32/32 | −6 binding |
| RSC | 7/11 | Primary scaffolds | −4+ |
| SC Core 5 | 3/5 PASS | 5/5 (excl. ECOMMERCE legal E1–E4) | 2 types |
| Blueprint-instances | Partial | Core 5 docs | CORPORATE · ECOMMERCE |
| Programme exit | OPEN | G4 PASS | Open |

**RPC alone insufficient for G4.**

---

## 10. W6 Authority

| Entity | Registry role | Page type | Existing evidence | RPC role | Decision |
|--------|---------------|-----------|-------------------|----------|----------|
| CART | Commerce block | Utility `/cart/` | No partial | Binding #1 | Block + scaffold |
| CHECKOUT | Primary conversion | Utility `/checkout/` | No partial | Binding #2 | Block + scaffold |
| PAYMENT | Checkout trust | Checkout region | No partial | Binding #3 | Block region |
| DELIVERY | Shipping info | Checkout region | No partial | Binding #4 | Block region |

---

## 11. W7 Authority

| Entity | Registry state | Maturity | Existing evidence | RPC gap | Decision |
|--------|----------------|----------|-------------------|---------|----------|
| FEATURES | Registered | Substitute | BENEFITS partial | Hygiene | W7-B-FEATURES |
| REVIEWS | Registered | Substitute | TESTIMONIALS | Hygiene | W7-B-REVIEWS |
| CERTIFICATES | Registered | None | — | Binding #5 | W7-A |
| PARTNERS | Registered | None | — | Binding #6 | W7-A |
| MAP | Registered | Substitute | CONTACTS | Hygiene | W7-B-MAP |

---

## 12. Corporate Slice Contract

- **Site type:** `CORPORATE`
- **Pages:** `ABOUT_PAGE` · `CONTACT_PAGE` (+ optional `REVIEWS_PAGE`)
- **Blocks:** ABOUT · TEAM · PARTNERS · CERTIFICATES · SERVICES · CONTACTS · MAP · trust/shell set
- **Scaffolds:** Enhance existing ABOUT/CONTACT; optional REVIEWS host
- **RPC:** +2 binding (CERTIFICATES · PARTNERS)
- **RSC:** Optional +1 if REVIEWS scaffold earned
- **SC:** G3 CORPORATE pilot target
- **PC:** No mandatory new corridor for G3 floor

---

## 13. Ecommerce Slice Contract

- **Site type:** `ECOMMERCE`
- **Pages:** Inherit catalog types + utility cart/checkout references
- **Blocks:** CATALOG set + CART · CHECKOUT · PAYMENT · DELIVERY
- **Scaffolds:** Cart/checkout utility reference pages
- **RPC:** +4 binding (W6)
- **RSC:** Utility pages need addendum before numerator accrual
- **SC:** G3 staging HITL
- **PC:** PRODUCT → CART → CHECKOUT — addendum required

---

## 14. Page-Type Expansion Decision

| Candidate | Registry state | Required | Coverage effect | Decision |
|-----------|----------------|----------|-----------------|----------|
| CART_PAGE | Extension doc only | Deferred | RSC addendum if registered | Not in charter pass |
| CHECKOUT_PAGE | Extension doc only | Deferred | Same | Not in charter pass |
| REVIEWS_PAGE | Registered | Optional scaffold | +1 RSC possible | Use existing type |
| CORPORATE_PAGE | None | No | — | Not required |

**Decision:** **PARTIAL EXPANSION REQUIRED IN DEDICATED WAVES**

---

## 15. Block Authority Decision

All W6/W7 units have **existing Registry rows**. **No new block IDs.** Implementation waves deliver T1+ partials only.

---

## 16. Structural Coverage Decision

- **Existing dimensions:** LANDING · PROMO · CATALOG PASS
- **New dimension:** None
- **Addendum:** None
- **Decision:** **EXISTING SC DIMENSIONS ONLY**

---

## 17. Page Corridor Decision

- **Existing:** LANDING · CATALOG · PROMO corridors PASS
- **Candidate:** ECOMMERCE `PRODUCT_PAGE → CART → CHECKOUT`
- **Addendum:** Required before accrual
- **Decision:** **PC ADDENDUM REQUIRED**

---

## 18. RSC Decision

- **Denominator:** **11** — unchanged
- **Numerator:** **7/11**
- **Addendum:** Required before `CART_PAGE`/`CHECKOUT_PAGE` registration
- **Accrual:** Registered `page_type` scaffolds only

---

## 19. Template-Art Boundary

| Concern | WF-R01.3.5 | WF-R01.7 |
|---------|------------|----------|
| Reference partials | Owner | Consumer |
| SC evidence | Delivers | Policy owner |
| Visual pilot | Static reference | Template-Art matrix |
| WF-A03 | Out of scope | Parallel |

---

## 20. Runtime and Data Boundary

- **Allowed:** Static cart/checkout · fictional data · presentation-only UI
- **Forbidden:** Real payments · network · CMS · production claims
- **Fictional data:** Mandatory for reference slice
- **Network:** Forbidden
- **Production claims:** Forbidden

---

## 21. G3 Minimum Delivery

| Unit | Current | Required work | RPC delta | Priority |
|------|---------|---------------|-----------|----------|
| CART | Gap | W6-B partial + scaffold | +1 | P0 |
| CHECKOUT | Gap | W6-B partial + scaffold | +1 | P0 |
| PAYMENT | Gap | W6-B checkout region | +1 | P0 |

**G3 floor:** **29/32**

---

## 22. G4 Completion Delivery

| Remaining unit | Required work | Wave |
|----------------|---------------|------|
| DELIVERY | T1+ partial | W6-C |
| CERTIFICATES | T1+ partial | W7-A |
| PARTNERS | T1+ partial | W7-A |
| FEATURES · REVIEWS · MAP | Hygiene partials | W7-B-* |
| RSC/SC/PC gaps | Scaffolds + compositions | W7-C · G4-E |

---

## 23. Implementation Waves

See charter §28 — first executable wave: **W6-A Commerce Block Reference Preflight**.

---

## 24. Exit Criteria

### G3-ready exit

RPC ≥29/32 · W6 validated · G3-E complete · G3-F separate

### WF-R01.3.5 complete exit

W6–W7 waves complete · binding gaps closed · handoff to G4-E

### WF-R01.3 programme exit

G4 PASS · RPC 32/32 · Core SC — **not** identical to R01.3.5 complete

---

## 25. G3 Readiness Contract

- **Mandatory:** W6 +3 RPC · build PASS · G3-E pack
- **Allowed debt:** Browser QA · substitution hygiene with waiver
- **G4-only:** DELIVERY · CERTIFICATES · PARTNERS if G3 uses minimum +3 only
- **Sign-off:** G3-F human evaluation — not executed in this pass

---

## 26. Debt and SAFE UNKNOWN

| Item | Blocking | Owner | Destination |
|------|----------|-------|-------------|
| Substitution policy split | No | WF-R01.6 / R01.3.5 | W7 hygiene |
| Utility route RSC | No | Coverage addendum | Pre-Registry |
| Named steward | No | Operator | G3-F sign-off |

---

## 27. Handoff

- **First wave inputs:** G2 metrics · BLOCK-GAPS · utility route mapping
- **Coverage freeze:** §6
- **Exclusions:** G2 rebuild · WF-A03 · Registry mutation

---

## 28. Files Created

| File | Purpose |
|------|---------|
| `projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md` | ACCEPTED charter |
| `reports/wf-r01-3-5-corporate-commerce-reference-slices-charter-pass-v1.md` | This report |

---

## 29. Files Modified

| File | Change |
|------|--------|
| `projects/mars-website-factory/roadmap.md` | R01.3.5 ACCEPTED · next task W6-A |
| `projects/mars-website-factory/OPERATIONAL-INDEX.md` | R01.3.5 ACCEPTED · G3 PLANNED |

---

## 30. Validation

| Check | Result |
|-------|--------|
| Identity | ✓ |
| RPC arithmetic | ✓ 26+6=32 |
| G3/G4 thresholds | ✓ |
| W6/W7 scope | ✓ |
| Slices defined | ✓ |
| No implementation | ✓ |
| No accrual | ✓ |
| Duplicate charter | ✓ None |

---

## 31. Documentation State

- **roadmap:** R01.3.5 **ACCEPTED**
- **OPERATIONAL-INDEX:** synced
- **WF-R01.3.5:** **CHARTERED · NOT IMPLEMENTED**
- **G3:** **PLANNED · NOT EVALUATED**
- **Next task:** **W6-A Commerce Block Reference Preflight**

---

## 32. Git Result

*(Updated after commit/push)*

---

## 33. Drift and Risks

| Severity | Finding | Blocking | Destination |
|----------|---------|----------|-------------|
| Medium | G2-R5 seven-name table vs six-count | No | Resolved in charter §11 |
| Medium | Substitution policy for FEATURES/REVIEWS/MAP | No | W7 hygiene · WF-R01.6 |
| Low | Utility routes vs RSC accrual | No | Coverage addendum |

---

## 34. Final Status

**COMPLETE**

---

## 35. Next Task

```text
WF-R01.3.5 W6-A — Commerce Block Reference Preflight
```

**Do not execute in this pass.**

---

## 36. Exact Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md
reports/wf-r01-3-5-corporate-commerce-reference-slices-charter-pass-v1.md
reports/wf-r01-3-reference-expansion-program-design-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/wf-r01-3-post-g2-lifecycle-decision-v1.md
reports/wf-r01-3-post-g2-lifecycle-decision-v1.md
reports/wf-r01-3-g2-to-wf-r01-3-5-handoff-v1.md
projects/mars-website-factory/wf-r01-3-g2-operator-sign-off-and-gate-closure-v1.md
projects/mars-website-factory/wf-r01-3-g2-formal-evaluation-decision-v1.md
projects/mars-website-factory/wf-r01-3-g2-r5-gate-evidence-assembly-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md
workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md
workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
```

---

## 37. Stop Confirmation

```text
WF-R01.3.5 implementation: NOT STARTED
W6 implementation: NOT STARTED
W7 implementation: NOT STARTED
G3 evaluation: NOT EXECUTED
G3 PASS: NOT GRANTED
G4 evaluation: NOT EXECUTED
WF-R01.3 closure: NOT PERFORMED
Production readiness: NOT CLAIMED
Coverage accrual: NONE
```

---

*Charter pass report: `reports/wf-r01-3-5-corporate-commerce-reference-slices-charter-pass-v1.md` · v1 · 2026-06-21*
