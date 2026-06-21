# WF-R01.3.5 W6-G3R G3 Readiness Reconciliation v1

**Subprogram ID:** WF-R01.3.5 W6-G3R — G3 Readiness Reconciliation  
**Program parent:** WF-R01.3 — Reference Implementation Expansion  
**Gate subject:** **Gate G3 — ECOMMERCE + CORPORATE slice**  
**Version:** v1  
**Date:** 2026-06-21  
**Report:** [wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md](../../reports/wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md)

**Honesty boundary:** Readiness-only · authority-reconciliation-only · criteria-extraction-only · gap-classification-only · wave-selection-only. **Not** implementation · **not** coverage accrual · **not** G3 evaluation · **not** G3 PASS · **not** G3 closure · **not** WF-R01.3.5 complete.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Document status** | **PUBLISHED** |
| **W6-G3R pass** | **COMPLETE** |
| **Coverage state** | RC **32/32** · RPC **29/32** · RSC **7/11** · SC **LANDING PASS · CATALOG PASS · PROMO PASS** · PC **1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor** |
| **G3 numeric RPC threshold** | **SATISFIED** (29/32 ≥ 29/32) |
| **G3 formal readiness** | **NOT READY** — multiple evidence gaps remain |
| **Readiness decision** | **G3 NOT READY — MULTIPLE EVIDENCE GAPS** |
| **Next authorized task** | **WF-R01.3.5 W6-D — Commerce Utility Scaffolds** |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Pass ID** | WF-R01.3.5 W6-G3R |
| **Pass name** | G3 Readiness Reconciliation |
| **Parent subprogram** | WF-R01.3.5 — Corporate & Commerce Reference Slices |
| **Parent programme** | WF-R01.3 — Reference Implementation Expansion |
| **Mode** | Documentation / reconciliation only |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.5 charter | [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) | G3 threshold · G3 Readiness Contract · slice contracts · wave map |
| W6-A preflight (project) | [wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md](wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md) | Block vs page-type · PC/RSC timing · G3 minimum +3 |
| W6-A preflight (report) | [wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md](../../reports/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md) | Published preflight evidence |
| W6-B1 report | [wf-r01-3-5-w6-b1-cart-reference-block-v1.md](../../reports/wf-r01-3-5-w6-b1-cart-reference-block-v1.md) | CART partial evidence |
| W6-B2 report | [wf-r01-3-5-w6-b2-checkout-reference-block-v1.md](../../reports/wf-r01-3-5-w6-b2-checkout-reference-block-v1.md) | CHECKOUT partial evidence |
| W6-B3 report | [wf-r01-3-5-w6-b3-payment-reference-block-v1.md](../../reports/wf-r01-3-5-w6-b3-payment-reference-block-v1.md) | PAYMENT partial evidence · RPC threshold note |
| Program design | [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md) | G3 gate definition · W6–W7 deliverables |
| Coverage Model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | Five dimensions · G0–G4 gates · reporting contract |
| Reference Scaffold Contract | [reference-scaffold-contract-v1.md](reference-scaffold-contract-v1.md) | Scaffold artefact requirements · RSC/PC boundaries |
| Global Shell Contract | [global-shell-contract-v1.md](global-shell-contract-v1.md) | Shell order · scaffold prerequisite |
| Page-Type Shell Matrix | [page-type-shell-matrix-v1.md](page-type-shell-matrix-v1.md) | Shell applicability |
| Foundry Vocabulary Canon | [foundry-vocabulary-canon-charter-v1.md](foundry-vocabulary-canon-charter-v1.md) | Terminology boundaries |
| Post-G2 lifecycle | [wf-r01-3-post-g2-lifecycle-decision-v1.md](wf-r01-3-post-g2-lifecycle-decision-v1.md) | G3 relationship · ECOMMERCE utility scaffolds mandatory |
| BLOCK-REGISTRY | [BLOCK-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md) | Block identity SSOT |
| BLOCK-GAPS | [BLOCK-GAPS-v1.md](../../workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md) | Partial maturity |
| PAGE-BLOCK-MAPPING | [PAGE-BLOCK-MAPPING-v1.md](../../workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md) | ECOMMERCE utility routes |
| PAGE-TYPE-REGISTRY | [PAGE-TYPE-REGISTRY-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md) | Registered page types · extensions note |
| PAGE-DEPENDENCY-RULES | [PAGE-DEPENDENCY-RULES-v1.md](../../workspaces/website-factory-reference-v1/page-architecture/PAGE-DEPENDENCY-RULES-v1.md) | CART_PAGE/CHECKOUT_PAGE extensions |
| Roadmap | [roadmap.md](roadmap.md) | Programme tracking |
| OPERATIONAL-INDEX | [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Operator lane pointer |

---

## 4. Purpose

Reconcile **exact readiness path** from current state (**RPC 29/32**, W6-B1/B2/B3 complete) to **READY FOR FORMAL G3 EVALUATION (G3-F)**, separating numeric RPC eligibility from full gate readiness, without implementation, accrual, or formal evaluation.

---

## 5. Scope

- Extract full Gate G3 criteria from normative authority
- Verify CART / CHECKOUT / PAYMENT block evidence integrity
- Classify utility scaffold, page-type, RSC, PC, SC, corporate slice, blueprint-instance, build, and G3-E requirements
- Separate G3 mandatory scope from G4-only scope
- Publish readiness gap matrix and minimal task order
- Select one next authorized task

---

## 6. Out of Scope

- HTML / SCSS / JS implementation
- Utility scaffold creation
- Registry mutation (BLOCK-REGISTRY · PAGE-TYPE-REGISTRY · Shell Matrix · Page-Block Mapping · Site-Type Matrix)
- Coverage addendum · PC addendum publication
- DELIVERY · CERTIFICATES · PARTNERS · W7 hygiene implementation
- RPC / RSC / PC / SC accrual
- G3-E evidence assembly execution
- G3-F formal evaluation · G3 PASS · G3 closure
- WF-R01.3.5 completion claim · G4 start · production readiness claim

---

## 7. Entry State

| Field | Value |
|-------|-------|
| **Branch** | `mars/post-cycle8-live-tests` |
| **HEAD commits (W6-B)** | `d25402f` CART · `4d68dab` CHECKOUT · `7bd633d` PAYMENT |
| **Remote W6-B3** | **PRESENT** — `7bd633d` on `origin/mars/post-cycle8-live-tests` |
| **WF-R01.3.5 waves** | W6-A **COMPLETE** · W6-B1 **COMPLETE** · W6-B2 **COMPLETE** · W6-B3 **COMPLETE** |
| **Gate G2** | **CLOSED · PASS WITH NON-BLOCKING DEBT** |
| **Gate G3** | **PLANNED · NOT EVALUATED · NOT PASSED · NOT CLOSED · RPC THRESHOLD SATISFIED** |
| **RC** | **32/32** |
| **RPC** | **29/32** |
| **RSC** | **7/11** |
| **SC** | **LANDING PASS · CATALOG PASS · PROMO PASS** |
| **PC** | **1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor** |
| **Reference build** | **PASS** (16 dist HTML pages at W6-B3 close) |
| **Foreign WIP** | **Present** — excluded from this pass |

---

## 8. Duplicate Check

| Search term | Finding | Classification |
|-------------|---------|----------------|
| `g3-readiness` | No prior reconciliation artefact | **None** |
| `g3 readiness reconciliation` | Only forward pointers in W6-B3 report and roadmap | **ROADMAP ENTRY** — not accepted decision |
| `w6-g3r` | This pass (first publication) | **NEW** |
| `g3 evidence pack` | G3-E listed in charter wave map — **NOT EXECUTED** | **CHARTER** |
| `g3 gate charter` | No separate G3-F charter found | **SAFE UNKNOWN** — G3-F contract may follow G2 precedent |
| `g3 formal evaluation` | **NOT EXECUTED** | **OPEN** |
| `ecommerce corridor addendum` | W6-I planned — **NOT PUBLISHED** | **DRAFT/planned** |
| `commerce utility scaffolds` | Charter W6-D — **NOT STARTED** | **CHARTER** |

**Decision:** No **ACCEPTED G3 READINESS DECISION** exists. W6-G3R proceeds.

---

## 9. G3 Identity

| Field | Authority wording |
|-------|-------------------|
| **Gate ID** | **G3** |
| **Canonical gate name** | **ECOMMERCE + CORPORATE slice** (Coverage Model Gate table) |
| **Parent programme** | **WF-R01.3 — Reference Implementation Expansion** |
| **Delivery subprogramme** | **WF-R01.3.5 — Corporate & Commerce Reference Slices** |
| **Purpose** | Reach RPC **≥29/32** (~91%); deliver ECOMMERCE staging HITL and CORPORATE pilot evidence; prepare G4 path |
| **Predecessor** | **Gate G2 — CLOSED**; W6 minimum binding partials (**CART · CHECKOUT · PAYMENT**) |
| **Successor** | **Gate G4 — Full Core reference** (RPC 32/32 + full Core SC) |
| **RPC target** | **29/32** (~91%) |
| **Primary deliverables (Coverage Model)** | CART, CHECKOUT, PAYMENT, DELIVERY; PARTNERS, CERTIFICATES, MAP, FEATURES, REVIEWS |
| **Unlocks** | **ECOMMERCE staging HITL**; **CORPORATE pilot** |
| **Evaluation owner** | Human operator — **G3-F formal evaluation** (charter §30: **not authorized by charter pass**) |
| **Sign-off owner** | Human operator (**named steward SAFE UNKNOWN**) |
| **Closure owner** | **WF-R01.3** gate milestone — separate from WF-R01.3.5 subprogram exit |
| **Current gate state** | **PLANNED · NOT EVALUATED · NOT PASSED · NOT CLOSED** |

---

## 10. G3 Criteria

| Criterion ID | Criterion | Mandatory | Required evidence | Current state | Gap |
|--------------|-----------|-----------|-------------------|---------------|-----|
| **G3-C01** | **RPC ≥ 29/32** | **Yes** | T1+ partials + build PASS + wave REPORTs | **29/32 SATISFIED** | **0** |
| **G3-C02** | **RC 32/32 maintained** | **Yes** | Registry completeness | **32/32 SATISFIED** | **0** |
| **G3-C03** | **W6 binding partials (+3 RPC)** CART · CHECKOUT · PAYMENT | **Yes** | Partials · SCSS · bounded hosts · REPORTs | **SATISFIED** | **0** |
| **G3-C04** | **ECOMMERCE utility scaffolds** `/cart/` · `/checkout/` | **Yes** (charter §30 · §29 · post-G2 §100) | Global-shell pages · compositions · manifests · build PASS · REPORT | **OPEN** — bounded hosts only | **HARD** |
| **G3-C05** | **Build PASS** after delivery waves | **Yes** | `npm run build` exit 0 | **SATISFIED** at W6-B3 — **revalidate after W6-D** | **PARTIAL** |
| **G3-C06** | **Five-dimension snapshot** | **Yes** (charter §30 · Coverage Model § Gate exit evidence) | RC · RPC · RSC · SC · PC in gate package | **OPEN** — no G3 gate snapshot REPORT | **HARD** |
| **G3-C07** | **G3-E evidence assembly** | **Yes** (charter §29 · §30) | Gate evidence pack per G2-R5 precedent | **OPEN** | **HARD** |
| **G3-C08** | **G3-F formal evaluation** | **Yes** for gate PASS | Operator evaluation REPORT · sign-off | **NOT EXECUTED** | **HARD** (downstream) |
| **G3-C09** | **SC — LANDING / PROMO / CATALOG maintained** | **Yes** | Prior gate REPORTs | **SATISFIED** | **0** |
| **G3-C10** | **SC — ECOMMERCE staging minimum** | **Yes** (Coverage Model · charter §12 · §29) | Staging slice evidence · utility scaffolds · optional W7-D doc | **OPEN** | **HARD** |
| **G3-C11** | **SC — CORPORATE pilot minimum** | **Yes** (Coverage Model · charter §12 · §16) | Corporate scaffolds/compositions · evaluation toward pilot | **OPEN** | **PARTIAL / HARD** |
| **G3-C12** | **RSC primary scaffolds for slice** | **Qualitative** (charter §12: TBD in waves) | Registered `page_type` scaffolds where applicable | **7/11** — ABOUT · CONTACT · catalog set present | **NON-BLOCKING** at numeric floor |
| **G3-C13** | **PC corridors maintained** | **Yes** | LANDING · CATALOG · PROMO PASS evidence | **SATISFIED** | **0** |
| **G3-C14** | **ECOMMERCE PC corridor** | **No for G3-F floor** (charter §30 G4-only accrual) | PC addendum + composition + scaffold evidence | **Planning only** | **G4-ONLY** for accrual |
| **G3-C15** | **DELIVERY partial** | **No for G3 minimum** (charter §26) | T1+ partial on checkout | **MISSING** | **G4-ONLY** |
| **G3-C16** | **CERTIFICATES · PARTNERS partials** | **No for G3 RPC minimum** (charter §26 · §469) | W7-A partials | **MISSING** | **G4-ONLY** for RPC floor |
| **G3-C17** | **Blueprint-instance docs** | **G4 primary** (charter §13 · §249); **G3 parallel SC** (§469 · W7-D) | CORPORATE · ECOMMERCE slice companion docs | **OPEN** | **PARTIAL** — ECOMMERCE staging doc before SC evaluation |
| **G3-C18** | **Runtime boundary honesty** | **Yes** | Static reference-only; no production commerce | **SATISFIED** in W6-B reports | **0** |

**Key authority resolution:** RPC **29/32** satisfies **G3-C01 eligibility** but **does not satisfy** G3 readiness — charter §30 explicitly lists utility scaffolds · five-dimension snapshot · G3-E pack as **mandatory before G3-F**.

---

## 11. Coverage Snapshot

| Dimension | G3 requirement | Actual | Readiness |
|-----------|----------------|--------|-----------|
| **RC** | **32/32** | **32/32** | **SATISFIED** |
| **RPC** | **≥29/32** | **29/32** | **THRESHOLD SATISFIED** — not full readiness |
| **RSC** | Primary scaffolds for slice (qualitative); **no numeric 11/11 floor at G3** | **7/11** | **ACCEPTABLE** for G3 planning — utility routes **do not accrue RSC** without addendum |
| **SC — LANDING** | **PASS maintained** | **PASS** | **SATISFIED** |
| **SC — CATALOG** | **PASS maintained** | **PASS** | **SATISFIED** |
| **SC — PROMO** | **PASS maintained** | **PASS** | **SATISFIED** |
| **SC — ECOMMERCE** | **Staging HITL minimum** | **Not PASS** | **OPEN** |
| **SC — CORPORATE** | **G3 pilot minimum** | **Not PASS** | **OPEN** |
| **PC — LANDING** | **1/1 maintained** | **1/1 PASS** | **SATISFIED** |
| **PC — CATALOG corridor** | **1/1 maintained** | **1/1 PASS** | **SATISFIED** |
| **PC — PROMO corridor** | **1/1 maintained** | **1/1 PASS** | **SATISFIED** |
| **PC — ECOMMERCE corridor** | **Addendum before accrual** — **not G3-F floor** | **Not accrued** | **G4-ONLY** for accrual |

---

## 12. Commerce Block Evidence

| Block | Registry | Partial | SCSS | Host integration | Build | Report | RPC |
|-------|----------|---------|------|------------------|-------|--------|-----|
| **CART** | `CART` registered | **PARTIAL / T1+** `components/cart.html` | `_cart.scss` | `cart-block-reference.html` bounded host | **PASS** | [w6-b1 report](../../reports/wf-r01-3-5-w6-b1-cart-reference-block-v1.md) | **+1 earned** (`d25402f`) |
| **CHECKOUT** | `CHECKOUT` registered | **PARTIAL / T1+** `components/checkout.html` | `_checkout.scss` | `checkout-block-reference.html` bounded host | **PASS** | [w6-b2 report](../../reports/wf-r01-3-5-w6-b2-checkout-reference-block-v1.md) | **+1 earned** (`4d68dab`) |
| **PAYMENT** | `PAYMENT` registered | **PARTIAL / T1+** `components/payment.html` | `_payment.scss` | Checkout bounded host sibling include | **PASS** | [w6-b3 report](../../reports/wf-r01-3-5-w6-b3-payment-reference-block-v1.md) | **+1 earned** (`7bd633d`) |

**Integrity:** Three independent RPC units · no double-count · CHECKOUT RPC not re-accrued at W6-B3 · **26/32 → 29/32** chain verified in wave REPORTs.

---

## 13. Utility Scaffold Requirement

**Decision:** **BOTH UTILITY SCAFFOLDS REQUIRED FOR G3**

| Scaffold | Required for G3 | Existing | Required evidence | Coverage effect |
|----------|-----------------|----------|-------------------|-----------------|
| **`/cart/` utility scaffold** | **Yes** | **No** — only `cart-block-reference.html` bounded host | Global-shell source page · CART composition · composition doc · scaffold manifest · dist output · build REPORT · static runtime boundary | **No RSC** without page-type addendum · **SC staging evidence** |
| **`/checkout/` utility scaffold** | **Yes** | **No** — only `checkout-block-reference.html` bounded host | Global-shell source page · CHECKOUT + PAYMENT (+ optional DELIVERY region policy) composition · composition doc · manifest · dist · REPORT | Same |

**Authority chain:** charter §106 · §498 · §30 G3 Readiness Contract · §29 G3-ready exit · post-G2 lifecycle §100 · W6-A rule **block before host scaffold**.

**Bounded hosts:** **Insufficient for G3** — valid for block RPC accrual only; not utility-route scaffold packages.

**Per-scaffold artefact checklist (utility-route pattern):**

| Artefact | Required |
|----------|----------|
| Source page (global shell) | **Yes** |
| Block composition | **Yes** |
| Composition document | **Yes** |
| Scaffold manifest | **Yes** |
| Dist output | **Yes** |
| Build report | **Yes** |
| Runtime boundary declaration | **Yes** |

**Note:** Utility scaffolds use **utility-route pattern** without registered `CART_PAGE`/`CHECKOUT_PAGE` at charter entry (charter §18).

---

## 14. Page-Type Authority

| Candidate | Registered now | Required for G3 | Required for RSC | Decision |
|-----------|----------------|-----------------|------------------|----------|
| **CART_PAGE** | Extension documented only — **not in minimal registry** | **No** | Only if addendum + registration | **Deferred** |
| **CHECKOUT_PAGE** | Extension documented only — **not in minimal registry** | **No** | Only if addendum + registration | **Deferred** |
| **Utility route role** | PAGE-BLOCK-MAPPING § ECOMMERCE utility routes | **Yes** for scaffolds | **No RSC accrual** without addendum | **Active pattern** |

**Decision:** **NO PAGE-TYPE REGISTRATION BEFORE G3**

Optional **W6-E** Coverage/page-type addendum only if operator elects formal utility types **before Registry mutation** — **not blocking G3** at current authority.

---

## 15. RSC Requirement

| RSC concern | Current | G3 required | Gap |
|-------------|---------|-------------|-----|
| **Numerator** | **7/11** | Maintain; no G3 mandate for **11/11** | **0 blocking** |
| **Denominator** | **11** | **Unchanged** per charter §22 | **0** |
| **Utility cart/checkout pages** | Not registered types | **Do not accrue RSC** without addendum | **By design** |
| **CORPORATE scaffolds** | ABOUT · CONTACT validated (G2-R2) | Reuse/enhance for pilot | **PARTIAL** |
| **Optional REVIEWS_PAGE** | Registered · optional W7 scaffold | **Optional** for G3 | **NON-BLOCKING** |

**Decision:** **RSC addendum NOT REQUIRED** for G3 floor. **7/11 may persist** through G3-F if evaluator accepts qualitative slice evidence. Denominator expansion (**CART_PAGE**/**CHECKOUT_PAGE**) is **optional / G4-oriented**.

---

## 16. ECOMMERCE PC Requirement

| PC concern | Authority | Current | G3 requirement | Gap |
|------------|-----------|---------|----------------|-----|
| **Candidate corridor** | `PRODUCT_PAGE → CART → CHECKOUT` | **Planning only** | **Intent documented** — **not mandatory for G3-F floor** | **G4-ONLY for accrual** |
| **PC addendum** | Charter §21 · W6-I | **NOT PUBLISHED** | Required **before corridor accrual** | **Not blocking G3 readiness reconciliation path** |
| **Timing vs blocks** | W6-A §21 | Blocks **COMPLETE** | Addendum **not required before block partials** | **0** |
| **Double-count vs CATALOG PC** | W6-A | CATALOG PC = `CATEGORY_PAGE → PRODUCT_PAGE` | ECOMMERCE extends **downstream** | **Policy clear** |

**Decision:** **ECOMMERCE PC REQUIRED ONLY FOR G4** (accrual). **ECOMMERCE PC ADDENDUM NOT REQUIRED BEFORE G3 READINESS** — required before **PC accrual** (W6-I).

---

## 17. SC Requirement

| SC concern | Current | G3 requirement | Gap |
|------------|---------|----------------|-----|
| **New SC dimension** | None | **None** — charter §20 | **0** |
| **LANDING / PROMO / CATALOG** | **PASS** | **Maintain** | **0** |
| **ECOMMERCE staging evidence** | **Not PASS** | Utility scaffolds + catalog inheritance + staging checklist (W7-D supports evaluation) | **OPEN** |
| **CORPORATE pilot** | **Not PASS** | Pilot minimum per Coverage Model · parallel polish (§469) | **OPEN** |
| **Formal SC accrual at G3** | N/A | **Evaluation toward minimum** — not necessarily full PASS before G3-E | **PARTIAL** |
| **Substitution waiver** | FEATURES/REVIEWS/MAP via substitutes | **Allowed debt at G3-F** with documented waiver (charter §30) | **NON-BLOCKING** |

**ECOMMERCE staging SC evidence means:** Static commerce chain demonstration (catalog → cart → checkout utility surfaces) at reference-demo fidelity — **not** production commerce · **not** separate programme SC dimension.

---

## 18. Corporate Slice Requirement

| Corporate concern | Existing evidence | G3 required | Gap |
|-------------------|-------------------|-------------|-----|
| **ABOUT_PAGE scaffold** | G2-R2 P3 validated | Reuse for CORPORATE pilot | **SATISFIED base** |
| **CONTACT_PAGE scaffold** | G2-R2 P2 validated | Reuse | **SATISFIED base** |
| **ABOUT · TEAM · SERVICES partials** | W3 T1+ | Corporate content blocks | **SATISFIED partial** |
| **CASES · TESTIMONIALS · CONTACTS** | Prior waves | Trust/contact blocks | **SATISFIED partial** |
| **CERTIFICATES · PARTNERS** | Registry only | W7-A — **G4 RPC binding** | **G4-ONLY for RPC** · **SC honesty gap** |
| **MAP · FEATURES · REVIEWS dedicated partials** | Substitution credits | W7-B hygiene — waiver allowed at G3-F | **NON-BLOCKING with waiver** |
| **Corporate compositions** | Partial (PROMO/CORPORATE stacks from G2) | Polish / validate for pilot evaluation | **PARTIAL** |
| **CORPORATE blueprint-instance doc** | **Not published** | W7-C — supports G4; parallel for G3 SC evaluation | **PARTIAL** |

**CERTIFICATES / PARTNERS:** **G4 RPC gaps** — **not G3 mandatory RPC** when minimum +3 path used (charter §26 · §30).

**Gate G3 slice ownership:** **Both ECOMMERCE and CORPORATE** required per Coverage Model gate name — CORPORATE evidence **partially exists** from G2/W3; **full pilot evaluation still OPEN**.

---

## 19. Blueprint-Instance Requirement

| Blueprint instance | Required for G3 | Existing | Required artefact |
|--------------------|-----------------|----------|-------------------|
| **ECOMMERCE staging slice doc** | **PARTIAL** — supports SC evaluation (W7-D) | **Not published** | Companion doc + SC checklist |
| **CORPORATE reference slice doc** | **PARTIAL** — parallel SC work (W7-C) | **Not published** | Multi-page slice doc |
| **Full Core 5 blueprint-instances** | **G4-ONLY** (charter §13 · §249) | Partial | G4-E |

**Classification:** Blueprint-instance at G3 = **documentation / SC evidence component** — **not** a substitute for utility scaffolds or G3-E pack.

---

## 20. Five-Dimension Snapshot

**Canonical five dimensions (Coverage Model § Coverage Dimensions):**

```text
RC · RPC · RSC · SC · PC
```

| Dimension | Current evidence | G3 requirement | Gap |
|-----------|------------------|----------------|-----|
| **RC** | **32/32** | Record in G3 gate snapshot | **Data ready** |
| **RPC** | **29/32** | Record · threshold note | **Data ready** |
| **RSC** | **7/11** | Record · utility-route non-accrual note | **Data ready** |
| **SC** | **3/5 Core PASS** · ECOMMERCE/CORPORATE OPEN | Record · pilot/staging evaluation status | **Evaluation OPEN** |
| **PC** | **3 corridors PASS** · ECOMMERCE not accrued | Record · addendum note | **Data ready** |

**Snapshot document:** **Required** as component of **G3-E** gate package (charter §30 · Coverage Model § Gate exit evidence · G2-R5 precedent).

**Not a separate dimension:** Blueprint-instance binds to **SC** component per Coverage Model § Reference artifact classes.

---

## 21. Build Requirement

| Check | Current | G3 requirement |
|-------|---------|----------------|
| Reference workspace build | **PASS** at W6-B3 | **PASS after each wave** |
| Dist HTML count | **16** | Increases with utility scaffolds |
| CART bounded host | **Present** | Block evidence — **not scaffold substitute** |
| CHECKOUT + PAYMENT bounded host | **Present** | Block evidence |
| Dedicated G3 build report | **None** | Part of **G3-E** / W6-D REPORT |

**Decision:** G3 requires **utility-scaffold build** in addition to bounded-host build. **All-reference build PASS** expected after W6-D before G3-E.

---

## 22. DELIVERY Boundary

| Question | Decision |
|----------|----------|
| **Required for G3 RPC floor?** | **No** — G4 priority (charter §26 · W6-A §24) |
| **Required for checkout scaffold honesty?** | **Optional region** — can ship checkout utility scaffold without DELIVERY partial at G3 minimum |
| **Required for PC corridor?** | **No** at G3 floor |
| **Binding RPC gap?** | **Yes** — **1/32** remaining toward G4 |

**Decision:** **DELIVERY NOT REQUIRED FOR G3**

---

## 23. G4-Only Scope

| Item | G3 mandatory | G4 mandatory | Optional/debt |
|------|--------------|--------------|---------------|
| **DELIVERY** | No | Yes (RPC + checkout integration) | — |
| **CERTIFICATES** | No (RPC) | Yes | SC honesty |
| **PARTNERS** | No (RPC) | Yes | SC honesty |
| **FEATURES / REVIEWS / MAP hygiene** | Waiver allowed | Full honesty | W7-B |
| **RSC 11/11** | No numeric floor | Yes toward full Core | — |
| **ECOMMERCE PC accrual** | No | Yes | W6-I addendum |
| **Page-type registration CART/CHECKOUT** | No | Optional | W6-E |
| **Template-Art production claims** | Forbidden | WF-R01.7 | — |
| **G4 full RPC 32/32** | No | Yes | — |
| **Full blueprint-instances Core 5** | Partial parallel | Yes | W7-C · W7-D · G4-E |

---

## 24. Readiness Gap Matrix

| G3 requirement | Current state | Gap | Required task | Blocking readiness |
|----------------|---------------|-----|---------------|-------------------|
| RPC ≥ 29/32 | **29/32** | None | — | **No** |
| W6 binding partials | **COMPLETE** | None | — | **No** |
| Utility scaffolds | **Missing** | Full scaffold packages | **W6-D** | **Yes** |
| Build PASS post-scaffolds | **PASS at B3 only** | Revalidate after W6-D | **W6-D REPORT** | **Yes** |
| ECOMMERCE SC staging evidence | **OPEN** | Scaffolds + staging doc/evaluation | **W6-D · W7-D (parallel)** | **Yes** |
| CORPORATE SC pilot evaluation | **OPEN** | Evaluation package | **W7-C parallel · G3-E** | **Partial** |
| Five-dimension snapshot | **Missing** | G3 gate snapshot | **G3-E** | **Yes** |
| G3-E evidence pack | **Missing** | Assembly | **G3-E** | **Yes** |
| G3-F formal evaluation | **NOT EXECUTED** | Operator pass | **G3-F** | **Yes** (downstream) |
| DELIVERY partial | **Missing** | G4 work | **W6-C** | **No** |
| ECOMMERCE PC accrual | **Not started** | G4 work | **W6-I** | **No** |
| CERTIFICATES / PARTNERS | **Missing** | G4 RPC | **W7-A** | **No** |

### Classification summary

| Class | Items |
|-------|-------|
| **HARD READINESS GAPS** | Utility scaffolds · post-scaffold build · G3-E pack · five-dimension snapshot · G3-F |
| **NON-BLOCKING DEBT** | Browser QA · W3 maturity · substitution hygiene with waiver · Sass warning |
| **G4-ONLY** | DELIVERY · CERTIFICATES · PARTNERS · ECOMMERCE PC accrual · RSC 11/11 · full blueprint-instances |
| **SAFE UNKNOWN** | Named G3-F evaluation charter artefact (may mirror G2 formal gate pass pattern) |

---

## 25. Required Task Order

| Order | Task | Purpose | Required before |
|-------|------|---------|-----------------|
| **1** | **WF-R01.3.5 W6-D — Commerce Utility Scaffolds** | `/cart/` · `/checkout/` global-shell packages · compositions · manifests · build REPORT | G3-E · G3-F |
| **2** | **WF-R01.3.5 W7-D — ECOMMERCE Blueprint-Instance Doc + SC Checklist** (parallel eligible) | ECOMMERCE staging SC evaluation evidence | G3-E (recommended) |
| **3** | **WF-R01.3.5 W7-C — CORPORATE Scaffolds + Blueprint-Instance Doc** (parallel eligible) | CORPORATE pilot SC evaluation evidence | G3-E (recommended) |
| **4** | **WF-R01.3.5 G3-E — G3 Evidence Assembly** | Five-dimension snapshot · gate evidence pack | G3-F |
| **5** | **WF-R01.3 G3-F — Formal G3 Evaluation** | Operator gate PASS/FAIL | G3 closure |
| **—** | W6-I ECOMMERCE PC Addendum | PC accrual only | **G4 corridor accrual** — not G3-E |
| **—** | W6-E Page-Type / Coverage Addendum | Optional Registry path | **Only if formal utility types elected** |
| **—** | W6-C DELIVERY · W7-A · W7-B | G4 RPC/SC completion | **G4** |

**Minimization rule applied:** W6-I and W6-E **not sequenced before G3-E** — authority places PC accrual at G4 and page-type registration as optional.

---

## 26. Readiness Decision

```text
G3 NOT READY — MULTIPLE EVIDENCE GAPS
```

**Rationale:**

1. **RPC 29/32** satisfies numeric **eligibility** only (charter §30 · W6-B3 report).
2. **Utility scaffolds** — mandatory before G3-F — **NOT STARTED**.
3. **G3-E evidence pack** and **five-dimension snapshot** — **NOT EXECUTED**.
4. **ECOMMERCE / CORPORATE SC** evaluation toward pilot/staging minimum — **OPEN**.
5. **G3-F** — **NOT EXECUTED**.

**Not selected:**

- `G3 NOT READY — UTILITY SCAFFOLDS REQUIRED` — true but **understates** G3-E and SC evaluation gaps
- `G3 NOT READY — PC ADDENDUM REQUIRED` — contradicted by charter §30 (PC accrual G4-only)
- `G3 READY FOR EVIDENCE ASSEMBLY` — premature — scaffolds incomplete
- `G3 READY FOR FORMAL EVALUATION` — contradicted by §30 mandatory list
- `G3 READINESS BLOCKED BY AUTHORITY` — authority is **consistent**

---

## 27. Next Authorized Task

```text
WF-R01.3.5 W6-D — Commerce Utility Scaffolds
```

**Rationale:** First hard gap in authority-ordered chain (block partials **complete** → **utility scaffolds** → G3-E → G3-F). W6-A rule: **block before host scaffold**. Charter §498 W6-D is explicit implementation wave.

**Do not execute in W6-G3R.**

---

## 28. Debt and SAFE UNKNOWN

| Item | Blocking | Owner | Destination |
|------|----------|-------|-------------|
| G2 browser QA deferred | No | Operator | Visual QA lane |
| W3 partial maturity | No | WF-R01.3 follow-on | Carried debt |
| FEATURES/REVIEWS/MAP substitution | No at G3-F if waiver | W7-B · WF-R01.6 | Hygiene waves |
| Named steward | No | Operator | G3-F sign-off |
| G3-F formal evaluation charter artefact | No at reconciliation | WF-R01.3.X / operator | Pre-G3-F |
| Utility route RSC accrual policy | No until addendum | W6-E optional | Pre-Registry |

---

## 29. Handoff

### Confirmed for downstream waves

- G3 identity and full criteria list **published**
- RPC threshold **SATISFIED** · readiness **NOT SATISFIED**
- Commerce block evidence **verified**
- Utility scaffolds **required** — bounded hosts **insufficient**
- Page-type registration **deferred**
- RSC **7/11 acceptable** at G3 floor
- ECOMMERCE PC **G4-only for accrual**
- DELIVERY **G4-only**
- Next task: **W6-D**

### Coverage freeze (unchanged by this pass)

```text
RC  = 32/32
RPC = 29/32
RSC = 7/11
SC  = LANDING PASS · CATALOG PASS · PROMO PASS
PC  = 1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor
```

---

## 30. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md
reports/wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md
projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/wf-r01-3-post-g2-lifecycle-decision-v1.md
reports/wf-r01-3-5-w6-b1-cart-reference-block-v1.md
reports/wf-r01-3-5-w6-b2-checkout-reference-block-v1.md
reports/wf-r01-3-5-w6-b3-payment-reference-block-v1.md
workspaces/website-factory-reference-v1/src/partials/components/cart.html
workspaces/website-factory-reference-v1/src/partials/components/checkout.html
workspaces/website-factory-reference-v1/src/partials/components/payment.html
workspaces/website-factory-reference-v1/src/pages/cart-block-reference.html
workspaces/website-factory-reference-v1/src/pages/checkout-block-reference.html
```

---

## 31. Decision

**W6-G3R COMPLETE.** Gate G3 remains **NOT EVALUATED · NOT PASSED · NOT CLOSED**. Programme proceeds to **W6-D — Commerce Utility Scaffolds** as the single next authorized implementation wave before G3 evidence assembly.
