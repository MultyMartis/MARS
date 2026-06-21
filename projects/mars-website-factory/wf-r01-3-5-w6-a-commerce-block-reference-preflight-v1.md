# WF-R01.3.5 W6-A Commerce Block Reference Preflight v1

**Subprogram:** WF-R01.3.5 — Corporate & Commerce Reference Slices  
**Wave:** W6-A — Commerce Block Reference Preflight  
**Parent charter:** [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md)  
**Charter pass:** [wf-r01-3-5-corporate-commerce-reference-slices-charter-pass-v1.md](../../reports/wf-r01-3-5-corporate-commerce-reference-slices-charter-pass-v1.md)  
**Date:** 2026-06-21  
**Mode:** authority-only · preflight-only · composition-planning-only · dependency-planning-only · coverage-planning-only

**Honesty boundary:** This document **authorizes W6 composition, dependency, and wave decisions only**. **Not** partial HTML/SCSS/JS. **Not** utility scaffolds. **Not** Registry mutation. **Not** coverage accrual. **Not** G3 evaluation. **Not** production commerce.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **PUBLISHED** |
| **Preflight state** | **COMPLETE** |
| **Implementation state** | **NOT IMPLEMENTED** |
| **Coverage impact** | **None** — RC **32/32** · RPC **26/32** · RSC **7/11** · SC/PC frozen at W6-A entry snapshot |

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Artefact ID** | WF-R01.3.5 W6-A — Commerce Block Reference Preflight v1 |
| **Canonical path** | `projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md` |
| **Report** | [reports/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md](../../reports/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md) |
| **Units in scope** | `CART` · `CHECKOUT` · `PAYMENT` · `DELIVERY` |
| **Out of W6-A scope** | W7 (`CERTIFICATES` · `PARTNERS` · `FEATURES` · `REVIEWS` · `MAP` hygiene) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.5 charter | `projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md` | W6 authority · G3/G4 floors · page-type policy |
| Charter pass | `reports/wf-r01-3-5-corporate-commerce-reference-slices-charter-pass-v1.md` | Accepted baseline |
| Reference expansion design | `reports/wf-r01-3-reference-expansion-program-design-v1.md` | W6 wave map · ECOMMERCE slice |
| Coverage Model | `projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md` | RPC/RSC/SC/PC gates |
| G2 handoff | `reports/wf-r01-3-g2-to-wf-r01-3-5-handoff-v1.md` | Entry metrics |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Canonical `block_id` rows |
| Core Block Library | `workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md` | Placement · maturity notes |
| Block Gaps | `workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md` | Missing partial inventory |
| Block Dependency Rules | `workspaces/website-factory-reference-v1/block-registry/BLOCK-DEPENDENCY-RULES-v1.md` | Commerce chain |
| Page Block Mapping | `workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md` | Utility routes · page stacks |
| Site Type Block Matrix | `workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md` | ECOMMERCE stances |
| Page Type Registry | `workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md` | Registered `page_type` set |
| Page Dependency Rules | `workspaces/website-factory-reference-v1/page-architecture/PAGE-DEPENDENCY-RULES-v1.md` | `CART_PAGE` / `CHECKOUT_PAGE` extension docs |
| Visual Pattern Registry | `workspaces/website-factory-reference-v1/design-system/VISUAL-PATTERN-REGISTRY-v1.md` | VF_CART_* · VF_CHECKOUT_* patterns |
| Global Shell Contract | `projects/mars-website-factory/global-shell-contract-v1.md` | Inherited shell |
| Page-Type Shell Matrix | `projects/mars-website-factory/page-type-shell-matrix-v1.md` | Shell applicability (registered types only) |
| Reference Scaffold Contract | `projects/mars-website-factory/reference-scaffold-contract-v1.md` | RSC accrual chain |
| Vocabulary Canon | `projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md` | F3 block family |
| PRODUCT PAGE composition | `workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md` | Explicit cart/checkout exclusions on PDP |
| Preflight precedent | `projects/mars-website-factory/wf-r01-3-g2-r3-a2-search-results-reference-preflight-composition-decisions-v1.md` | A2 preflight pattern |

**Hierarchy for W6 conflicts:** WF-R01.3.5 ACCEPTED charter **>** BLOCK-REGISTRY + PAGE-BLOCK-MAPPING **>** program design **>** shell matrix (no utility-row override).

---

## 4. Purpose

W6-A establishes normative authority for the four commerce `block_id` units before any implementation wave:

1. Confirm Registry identity and RPC eligibility for each unit.
2. Audit existing reference evidence and maturity.
3. Define block contracts, host ownership, and runtime boundaries.
4. Resolve page-type vs block-level semantics for cart/checkout surfaces.
5. Plan dependency graph, compositions, PC addendum scope, and safe implementation waves.
6. Validate G3 minimum delivery (`+3 RPC`) without accrual.

---

## 5. Scope

### In scope

- Block identity audit for `CART` · `CHECKOUT` · `PAYMENT` · `DELIVERY`
- Existing artefact inventory (partials, compositions, scaffolds, registry docs)
- Block contracts and composition decisions (candidate — not PUBLISHED compositions)
- Dependency graph and independent RPC accrual analysis
- Page-type expansion decision (documentation-only)
- RSC · PC · SC impact preflight
- G3 minimum validation
- Implementation wave map and first authorized wave

### Out of scope (binding)

- HTML · SCSS · JS · partials · scaffolds · compositions · manifests
- BLOCK-REGISTRY · PAGE-TYPE-REGISTRY · Coverage Model · Shell Matrix edits
- PC/RSC addendum publication · coverage accrual · G3 evaluation
- W7 corporate/trust units · FEATURES/REVIEWS/MAP substitution re-evaluation
- Production checkout · payment gateway · network · real commerce data

---

## 6. Out of Scope

See §5. Additionally: Registry row creation; claiming CART/CHECKOUT/PAYMENT/DELIVERY implemented; claiming RPC **>26/32**; claiming G3 PASS; touching W7 charter waves.

---

## 7. Entry State

| Field | Value |
|-------|-------|
| **Gate G2** | **CLOSED · PASS WITH NON-BLOCKING DEBT** |
| **Gate G3** | **PLANNED · NOT EVALUATED · NOT PASSED · NOT CLOSED** |
| **WF-R01.3.5** | **CHARTERED · NOT IMPLEMENTED · NOT COMPLETE** |
| **RC** | **32/32** |
| **RPC** | **26/32** |
| **RSC** | **7/11** |
| **SC** | **LANDING PASS · CATALOG PASS · PROMO PASS** |
| **PC** | **1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor** |
| **Binding RPC gaps (W6 subset)** | **4/6** — `CART` · `CHECKOUT` · `PAYMENT` · `DELIVERY` |

---

## 8. Duplicate Check

| Search term | Result | Classification |
|-------------|--------|----------------|
| `w6-a` | Charter next-task refs only | **COMPLEMENTARY** |
| `commerce-block-reference-preflight` | **None accepted** | — |
| `cart-checkout-preflight` | **None** | — |
| `commerce-reference-preflight` | **None** | — |
| `cart-page` / `checkout-page` | PAGE-DEPENDENCY-RULES extension docs | **REGISTRY PROPOSAL (deferred)** |
| `ecommerce-corridor` | Charter §21 intent only | **CHARTER** |

| Classification | Artefacts |
|----------------|-----------|
| **ACCEPTED PREFLIGHT** | **None** — proceed |
| **COMPLEMENTARY** | WF-R01.3.5 charter · charter pass · G2 handoff |
| **NOT BLOCK EVIDENCE** | Registry rows · matrix docs · visual pattern names |

**Decision:** Proceed — no competing accepted W6-A preflight.

---

## 9. Block Identity Audit

| Unit | Registry row | Canonical ID | RPC eligible | Site types | Current maturity |
|------|--------------|--------------|--------------|------------|------------------|
| **CART** | **REGISTERED** — BLOCK-REGISTRY § CART | `CART` | **Yes** | ECOMMERCE ● · CORPORATE ○ (ecommerce subtree) | **MISSING** — no partial |
| **CHECKOUT** | **REGISTERED** — BLOCK-REGISTRY § CHECKOUT | `CHECKOUT` | **Yes** | ECOMMERCE ● · CORPORATE ○ | **MISSING** — no partial |
| **PAYMENT** | **REGISTERED** — BLOCK-REGISTRY § PAYMENT | `PAYMENT` | **Yes** | ECOMMERCE ● · CORPORATE ○ | **MISSING** — no partial |
| **DELIVERY** | **REGISTERED** — BLOCK-REGISTRY § DELIVERY | `DELIVERY` | **Yes** | ECOMMERCE ○ · CORPORATE ○ | **MISSING** — no partial |

**Preflight result:** All four binding W6 units have **canonical Registry identity**. **No BLOCK AUTHORITY GAP.** **No new `block_id` creation in W6-A.**

---

## 10. Existing Reference Evidence

| Unit | Existing artefact | Authority | Maturity | Reusable | RPC earned |
|------|-------------------|-----------|----------|----------|------------|
| **CART** | BLOCK-REGISTRY · CORE-BLOCK-LIBRARY · PAGE-BLOCK-MAPPING § utility `/cart/` · SITE-TYPE-BLOCK-MATRIX · VF_CART_LINE_ITEMS | Registry + mapping | **PLANNED** | Policy only | **No** |
| **CART** | BLOCK-GAPS-v1 — `—` Not implemented | Gap register | **MISSING** | — | **No** |
| **CART** | No `src/partials/**/cart*` · no `cart-reference.html` | Workspace search | **MISSING** | — | **No** |
| **CHECKOUT** | BLOCK-REGISTRY · PAGE-BLOCK-MAPPING § `/checkout/` · BLOCK-DEPENDENCY-RULES chain · VF_CHECKOUT_FLOW_STEPS | Registry + deps | **PLANNED** | Policy only | **No** |
| **CHECKOUT** | BLOCK-GAPS-v1 — Not implemented | Gap register | **MISSING** | — | **No** |
| **CHECKOUT** | No checkout partial or scaffold HTML | Workspace search | **MISSING** | — | **No** |
| **PAYMENT** | BLOCK-REGISTRY · VF_PAYMENT_METHODS_STRIP · CONTENT-SIGNAL-VALIDATION (checkout signals) | Registry + content | **PLANNED** | Policy only | **No** |
| **PAYMENT** | BLOCK-GAPS-v1 — Not implemented | Gap register | **MISSING** | — | **No** |
| **DELIVERY** | BLOCK-REGISTRY · VF_DELIVERY_INFO_PANEL · optional ECOMMERCE matrix stance | Registry | **PLANNED** | Policy only | **No** |
| **DELIVERY** | BLOCK-GAPS-v1 — Not implemented | Gap register | **MISSING** | — | **No** |
| **All four** | PRODUCT-PAGE-REFERENCE-COMPOSITION — explicit **no cart/checkout** on PDP | Composition exclusion | **N/A** | Exclusion policy | **No** |
| **All four** | `.recovery-temp/` legacy HTML (if any) | **Not reference authority** | **LEGACY / OUT OF SCOPE** | **No** | **No** |

**RPC numerator remains 26/32.** Legacy or foreign workspace HTML does **not** earn RPC.

---

## 11. CART Contract

### Block boundaries

- **Identity:** F3 conversion block `CART` — cart review surface, not header mini-cart utility icon (HEADER_NAV composition ≠ `CART` page block per BLOCK-REGISTRY notes).
- **Primary host:** Utility route **`/cart/`** reference scaffold (documented route role — not a registered `page_type` at W6-A).
- **Secondary context:** ECOMMERCE site type only; **FORBIDDEN** on LANDING · PROMO · CATALOG without reclassification.

### Required content (authority-backed)

| Concern | Stance | Source |
|---------|--------|--------|
| Line item list | **Required** | VF_CART_LINE_ITEMS · CORE-BLOCK-LIBRARY purpose |
| Quantity display | **Required** (presentation-only) | Cart review semantics |
| Remove action | **Allowed** (presentation-only · no persistence) | Reference runtime boundary |
| Subtotal / totals | **Required** (fictional) | Charter §25 fictional totals |
| Empty-cart variation | **Required variation state** | Standard commerce reference honesty |
| Continue-shopping action | **Allowed** (static `href`) | Funnel bridge — not RPC blocker |
| Proceed-to-checkout action | **Required** CTA (static link to checkout route) | BLOCK-CONVERSION-ROLES — SECONDARY_CONVERSION |

### Controls and variations

- **Allowed:** Static quantity labels · presentation-only remove · fictional prices · `href="#"` or static `/checkout/` path in reference scaffold.
- **Forbidden:** Live cart persistence · API · real stock · network requests.

### Runtime boundary

- Static reference only per charter §24–§25.
- **Must not** claim working cart.

### Host page

- **Owner:** Utility-route **cart reference scaffold** (W6-D — after block partial exists).
- Bounded partial host permitted during W6-B (precedent: `pagination-reference.html`, `search-reference.html`).

### RPC evidence chain

`CART` T1+ partial in reference workspace → build PASS → BLOCK-GAPS update in implementation REPORT → RPC **+1** when wave closes with evidence.

---

## 12. CHECKOUT Contract

### Block boundaries

- **Identity:** F3 PRIMARY_CONVERSION block `CHECKOUT` — order completion flow container.
- **Host:** Utility route **`/checkout/`** reference scaffold.
- **Hard deps:** `CART` path · Consent Rule · Legal Pack · `LEGAL_LINKS` (BLOCK-DEPENDENCY-RULES).

### Form semantics (reference-only)

| Concern | Stance | Notes |
|---------|--------|-------|
| Customer / contact fields | **Required** (static · fictional) | Collects PD — Consent Rule applies at implementation |
| Delivery address fields | **Allowed** within CHECKOUT or adjacent DELIVERY region | Not separate page type |
| Order summary | **Scaffold-owned or CHECKOUT-internal region** — **no** separate `block_id` | Not in Registry as standalone block |
| Delivery method selection | **DELIVERY block region** (optional on checkout per PAGE-BLOCK-MAPPING) | See §14 |
| Payment method selection | **PAYMENT block region** (required on checkout) | See §13 |
| Agreement / consent | **Required** at implementation | Legal Pack — not preflight HTML |
| Submit / place order | **Presentation-only** — no order creation | Charter runtime boundary |

### Relationship to PAYMENT and DELIVERY

- **PAYMENT:** Composition sibling on checkout scaffold — **required** stack member.
- **DELIVERY:** Composition sibling — **optional** on checkout (`OPT` in PAGE-BLOCK-MAPPING § utility routes) but **recommended** for ECOMMERCE honesty; **G4 RPC unit**, not G3 minimum.

### Runtime boundary

- Static checkout structure · fictional data · no gateway · no network.

### RPC evidence chain

`CHECKOUT` T1+ partial + checkout context evidence → build PASS → RPC **+1**.

---

## 13. PAYMENT Contract

### Canonical identity

- **Block_id:** `PAYMENT` — payment methods / trust at checkout step.
- **Category:** COMMERCE · TRUST_SUPPORT conversion role.

### Host

- **Primary:** Checkout utility scaffold — `/checkout/` stack member.
- **Not** a standalone marketing page or registered page type.

### Standalone partial requirement

- **Yes** — canonical partial required for RPC (charter W6-B).
- Mounted on checkout host or bounded checkout partial host during implementation; not a separate page scaffold.

### Required method options (reference)

- Fictional payment method labels (e.g. card-on-delivery, invoice, online wallet **presentation-only**).
- Static radio/select UI · trust/security copy strip per VF_PAYMENT_METHODS_STRIP.
- **Forbidden:** Card number fields with real validation · gateway widgets · external payment URLs · credentials.

### Relationship to CHECKOUT

- **requires** `CHECKOUT` (BLOCK-DEPENDENCY-RULES hard dep).
- Composition: CHECKOUT scaffold includes PAYMENT region; PAYMENT is **not** a child DOM subtree requirement but a **required composition member**.

### Independent RPC before DELIVERY?

**Yes — per Coverage authority.**

| Basis | Decision |
|-------|----------|
| Charter §26 G3 corridor | `CART` + `CHECKOUT` + `PAYMENT` = **+3 RPC** |
| Charter §27 G4 | `DELIVERY` is **G4** wave (W6-C) |
| BLOCK-DEPENDENCY-RULES | PAYMENT **requires** CHECKOUT — not DELIVERY |
| CONTENT-VALIDATION CVF-015 | Missing delivery on CHECKOUT = **SC/content signal** concern — **not** RPC numerator blocker at G3 minimum |

---

## 14. DELIVERY Contract

### Canonical identity

- **Block_id:** `DELIVERY` — shipping / delivery info panel.
- **Category:** COMMERCE · INFORMATIONAL conversion role.

### Host

- **Primary:** Checkout utility scaffold (optional region per PAGE-BLOCK-MAPPING).
- **Secondary (future):** Static policy surface — scaffold-owned route without new `page_type` (charter §14).

### Standalone partial requirement

- **Yes** — dedicated T1+ partial for RPC accrual (W6-C).
- Integrated into checkout composition as sibling region to PAYMENT.

### Delivery method options (reference)

- Fictional delivery choices (courier, pickup, postal) with static price/time labels.
- **Forbidden:** Real courier API · postal validation · geocoding · dynamic pricing.

### Address relationship

- Address capture may appear in CHECKOUT form; DELIVERY block focuses on **method / policy / reassurance** panel per VF_DELIVERY_INFO_PANEL.

### RPC eligibility

- **Yes** — binding gap #4 · **G4 priority** per charter §26–§27.
- Independent of PAYMENT RPC accrual order.

---

## 15. Dependency Graph

```
PRODUCT_CARD / catalog context
         ↓
       CART  ──→  /cart/ utility scaffold (W6-D)
         ↓
     CHECKOUT  ──→  /checkout/ utility scaffold (W6-D)
      ↙     ↘
  PAYMENT   DELIVERY (parallel info · optional on checkout · G4 RPC)
     ↑
 LEGAL_LINKS + Consent Rule
```

| Unit | Depends on | Can be implemented independently | Can earn RPC independently |
|------|------------|----------------------------------|----------------------------|
| **CART** | `PRODUCT_CARD` / catalog context (soft-hard per deps) | **Yes** — with bounded host + fictional items | **Yes** |
| **CHECKOUT** | `CART` · Legal Pack · Consent Rule | **After CART partial** (chain policy) | **Yes** — once partial exists |
| **PAYMENT** | `CHECKOUT` | **After CHECKOUT partial** | **Yes** — G3 unit; **before DELIVERY** |
| **DELIVERY** | ECOMMERCE Blueprint · checkout context (soft) | **After CHECKOUT scaffold context** (recommended) | **Yes** — G4 unit |

**Note:** Visual nesting on checkout ≠ automatic RPC dependency. DELIVERY absence does **not** block PAYMENT RPC at G3 floor.

---

## 16. Page-Type Registry Audit

| Candidate | Registry row | Shell authority | Needed for W6 blocks | Reason |
|-----------|--------------|-----------------|----------------------|--------|
| **CART_PAGE** | Extension doc only (PAGE-DEPENDENCY-RULES · PAGE-TYPE-REGISTRY footnote) | **No** Shell Matrix row | **Deferred** | Utility-route scaffold suffices for reference (charter §18) |
| **CHECKOUT_PAGE** | Extension doc only | **No** Shell Matrix row | **Deferred** | Same |
| **ORDER_CONFIRMATION_PAGE** | Extension doc only | **No** | **No** for W6-A | Out of G3 minimum |
| **ECOMMERCE_PAGE** | **No** | **No** | **No** | Use `site_type_code` ECOMMERCE + utility routes |
| **UTILITY_PAGE** | **No** generic code | **No** | **No** | Route roles documented in PAGE-BLOCK-MAPPING |
| **FORM_PAGE** | **No** | **No** | **No** | CHECKOUT is block, not form page type |
| **PRODUCT_PAGE** | **REGISTERED** | **Yes** | **Inherited** | Catalog source · explicit cart exclusion on PDP |
| **CATEGORY_PAGE** | **REGISTERED** | **Yes** | **Inherited** | Catalog chain |

---

## 17. Page-Type Decision

**UTILITY VARIATIONS OF EXISTING PAGE TYPE** — with **PARTIAL EXPANSION IN DEDICATED WAVES** for formal `CART_PAGE` / `CHECKOUT_PAGE` registration.

| Question | Decision |
|----------|----------|
| Registered `CART_PAGE` required for W6 block partials? | **No** — utility-route reference pages + bounded hosts suffice |
| Registered `CHECKOUT_PAGE` required for W6 block partials? | **No** — same |
| Registry mutation in W6 implementation waves? | **Deferred** until Coverage addendum accepts utility page types |
| Page-type expansion before block implementation? | **Not required** for T1+ partials and bounded hosts |

---

## 18. RSC Impact

| Field | Value |
|-------|-------|
| **Current denominator** | **11** registered `page_type` codes |
| **Current numerator** | **7/11** |
| **Utility cart/checkout pages at W6-A** | **Reference artefacts** — not registered types |
| **Candidate denominator** | **11 unchanged** unless future addendum registers `CART_PAGE` / `CHECKOUT_PAGE` |
| **RSC accrual from utility routes** | **No** at W6-A · charter §22 |
| **Required addendum** | **Coverage addendum** before PAGE-TYPE-REGISTRY mutation **if** operator chooses formal utility types for RSC |
| **Mutation order** | Coverage addendum → Registry (if approved) → Shell Matrix row → scaffold accrual |
| **W6-D scaffolds without page types** | **Do not increment RSC** — documented reference pages only |

**Decision:** **NO RSC DENOMINATOR CHANGE** in W6-A or default W6 path.

---

## 19. Shell Contract

Utility commerce hosts inherit **global shell** per [global-shell-contract-v1.md](global-shell-contract-v1.md). No Shell Matrix row exists for utility routes — W6-A defines **candidate shell stacks** from PAGE-BLOCK-MAPPING + global shell precedent.

### CART host (`/cart/` utility scaffold)

| Region | Stance | Identity |
|--------|--------|----------|
| HEADER_NAV | **REQ** | Global shell |
| MAIN | **REQ** | Semantic wrapper |
| BREADCRUMBS | **POL** | Shallow trail (catalog → cart) |
| PAGE_IDENTITY | **SCAFFOLD-OWNED** | H1 / intro — no `block_id` |
| CART | **REQ** | `block_id` CART |
| FOOTER | **REQ** | Global shell |
| LEGAL_LINKS | **REQ** | Nested in FOOTER |
| CHECKOUT on same view | **FORB** | PAGE-BLOCK-MAPPING |

**Shell type:** Minimal **utility shell** — full site shell inheritance (HEADER_NAV + FOOTER + LEGAL_LINKS), not catalog PLP slot duplication.

### CHECKOUT host (`/checkout/` utility scaffold)

| Region | Stance | Identity |
|--------|--------|----------|
| HEADER_NAV | **REQ** | Global shell |
| MAIN | **REQ** | Semantic wrapper |
| BREADCRUMBS | **POL** | Shallow trail |
| PAGE_IDENTITY | **SCAFFOLD-OWNED** | H1 / step intro |
| CHECKOUT | **REQ** | Primary flow block |
| PAYMENT | **REQ** | Composition member |
| DELIVERY | **OPT** | Recommended · G4 integration |
| Order summary | **SCAFFOLD-OWNED** or CHECKOUT-internal | No Registry `block_id` |
| Consent / agreement | **REQ at implementation** | Legal Pack |
| FOOTER + LEGAL_LINKS | **REQ** | Global shell |
| LEAD_FORM as primary | **FORB** | PAGE-BLOCK-MAPPING |

**Shell type:** Full site shell + commerce utility MAIN stack — not LANDING conversion minimal shell.

---

## 20. CART Composition Decision

**Candidate composition (not PUBLISHED):**

```text
HEADER_NAV

MAIN
├── BREADCRUMBS (POL)
├── PAGE_IDENTITY (scaffold-owned)
├── CART (block partial)
└── optional scaffold-owned support region (e.g. fictional promo note)

FOOTER
└── LEGAL_LINKS
```

| Field | Decision |
|-------|----------|
| **Required blocks** | HEADER_NAV · CART · FOOTER · LEGAL_LINKS |
| **Policy blocks** | BREADCRUMBS (POL) |
| **Excluded blocks** | CHECKOUT · PAYMENT · DELIVERY · LEAD_FORM · PRODUCT_GRID on same view |
| **Scaffold-owned regions** | PAGE_IDENTITY · optional empty-cart messaging wrapper |
| **Empty-cart variation** | **Required** — distinct static state with continue-shopping CTA |
| **Runtime boundary** | Fictional line items · static totals · no persistence |

---

## 21. CHECKOUT Composition Decision

**Candidate composition (not PUBLISHED):**

```text
HEADER_NAV

MAIN
├── BREADCRUMBS (POL)
├── PAGE_IDENTITY (scaffold-owned)
├── CHECKOUT (primary flow block)
│   ├── form fields / customer region (CHECKOUT-owned)
│   ├── order summary (scaffold-owned or CHECKOUT-internal)
│   ├── DELIVERY (optional region — DELIVERY block partial)
│   └── PAYMENT (required region — PAYMENT block partial)
├── consent / agreement (implementation — Legal Pack)
└── submit action (presentation-only)

FOOTER
└── LEGAL_LINKS
```

| Question | Decision |
|----------|----------|
| PAYMENT/DELIVERY children of CHECKOUT? | **Composition members** on checkout scaffold — separate canonical partials, not alternate block_ids |
| Order summary canonical block? | **No** — scaffold-owned or CHECKOUT-internal region |
| Form one block or several? | **One CHECKOUT block** owns primary form shell; PAYMENT/DELIVERY are **sibling regions** |
| LEAD_FORM | **FORBIDDEN** as primary on checkout view |

---

## 22. PC Addendum Preflight

| Field | Value |
|-------|-------|
| **Charter requirement** | **PC ADDENDUM REQUIRED** before ECOMMERCE corridor accrual |
| **Candidate corridor** | **`PRODUCT_PAGE → CART → CHECKOUT`** |
| **Rejected as primary (W6-A)** | `CATEGORY_PAGE → …` (already in CATALOG PC) · `→ CONFIRMATION` (no page type / out of W6) |
| **Members** | `PRODUCT_PAGE` (existing scaffold) · CART utility route · CHECKOUT utility route |
| **Denominator** | **+1 ECOMMERCE corridor** (separate from LANDING · CATALOG · PROMO) |
| **Existing CATALOG relationship** | CATALOG PC = `CATEGORY_PAGE → PRODUCT_PAGE` — **no double-count**; ECOMMERCE PC extends **downstream** from PRODUCT |
| **Accrual boundary** | After dedicated PC addendum publication + composition docs + scaffold evidence — **not** in W6-A · **not** with block partials alone |
| **W6-A output** | **PC CORRIDOR DECISION REQUIRES DEDICATED ADDENDUM** — scope defined here; addendum wave **W6-I** (documentation) before accrual |

**Timing:** PC addendum required **before corridor accrual**, **not** before block partial implementation (charter §21).

---

## 23. SC Impact

| Field | Value |
|-------|-------|
| **Existing SC dimensions** | **LANDING · PROMO · CATALOG** — PASS maintained |
| **W6 SC role** | **ECOMMERCE `site_type_code` staging evidence** — extension of catalog chain |
| **New SC dimension** | **None** — charter §20 |
| **W6 evidence class** | **G3 slice evidence** for ECOMMERCE SC evaluation — not separate programme SC |
| **CATALOG SC relationship** | W6 **extends** catalog reference toward commerce; does **not** re-open CATALOG PASS |
| **FEATURES/REVIEWS/MAP** | **Out of W6-A scope** — substitution status unchanged |

---

## 24. G3 Minimum Delivery Validation

| Unit | Current RPC | Required evidence | Independent accrual | G3 eligible |
|------|-------------|-------------------|---------------------|-------------|
| **CART** | Gap (0) | T1+ partial + build PASS | **Yes** | **Yes — P0** |
| **CHECKOUT** | Gap (0) | T1+ partial + checkout context | **Yes** | **Yes — P0** |
| **PAYMENT** | Gap (0) | T1+ partial on checkout host | **Yes** | **Yes — P0** |
| **DELIVERY** | Gap (0) | T1+ partial + checkout integration | **Yes** | **No — G4** |

**Arithmetic:** 26 + 3 = **29/32** ✓

**Decision:** **G3 MINIMUM CONFIRMED** — `CART` + `CHECKOUT` + `PAYMENT` = **+3 RPC** without DELIVERY, without PAGE-TYPE-REGISTRY mutation, without PC accrual.

---

## 25. Implementation Waves

| Wave | Purpose | Type | Output |
|------|---------|------|--------|
| **W6-A** | Commerce block preflight | Documentation | This document · REPORT — **COMPLETE** |
| **W6-B1** | `CART` T1+ reference partial | Implementation | Partial + bounded host + REPORT |
| **W6-B2** | `CHECKOUT` T1+ reference partial | Implementation | Partial + bounded host + REPORT |
| **W6-B3** | `PAYMENT` T1+ reference partial | Implementation | Partial + checkout host integration + REPORT |
| **W6-C** | `DELIVERY` T1+ partial + checkout integration | Implementation | Partial + REPORT |
| **W6-D** | ECOMMERCE utility scaffolds `/cart/` · `/checkout/` | Implementation | Scaffolds · compositions · manifests |
| **W6-E** | Commerce page-type / coverage authority addenda (if operator elects formal utility types) | Documentation | Optional addendum docs — **before Registry mutation only** |
| **W6-I** | ECOMMERCE PC addendum + corridor composition | Documentation | PC addendum — **before PC accrual** |
| **G3-E** | G3 evidence assembly | Gate package | Evidence pack — **separate from W6 opening** |

**Rules preserved:** authority before mutation · preflight before implementation · **block before host scaffold** · coverage only after evidence · one primary `block_id` per implementation pass (default) · G3 evaluation separate.

**Charter W6-B grouping note:** Charter table groups CART/CHECKOUT/PAYMENT in one wave label; W6-A splits into **W6-B1/B2/B3** per one-block-per-pass default unless operator explicitly batches.

---

## 26. First Authorized Wave

```text
WF-R01.3.5 W6-B1 — CART Reference Block
```

**Do not execute in W6-A.**

Rationale: Registry authority confirmed · no page-type blocker · CART is dependency root · bounded host precedent exists · scaffold wave (W6-D) follows block partials.

---

## 27. Debt and SAFE UNKNOWN

| Item | Blocking | Owner | Destination |
|------|----------|-------|-------------|
| CHECKOUT form field schema vs LEAD_FORM | **No** at preflight | W6-B2 implementation | BLOCK-GAPS § form schemas |
| Legal extensions E2/E3 for PAYMENT/DELIVERY copy | **No** at G3 reference | WF-R01.7 / Legal Pack future | Template-Art / legal lane |
| Utility route formal `page_type` registration | **No** for block RPC | W6-E optional addendum | Coverage addendum |
| ECOMMERCE PC corridor publication | **No** for block RPC | W6-I | PC addendum wave |
| Mini-cart in HEADER_NAV | **No** | Future hygiene | Not W6-A scope |
| Machine validation of dependency graph | **No** | WF-R01.6 | Automation gap |
| Named steward | **No** | Operator | G3-F sign-off |

---

## 28. Handoff

### Authority confirmed

- Four canonical `block_id` rows — **REGISTERED**
- G3 minimum **+3** — **CONFIRMED**
- Page-type decision — **utility routes without Registry mutation for block phase**
- PAYMENT RPC **independent of DELIVERY** at G3 floor

### Compositions

- CART and CHECKOUT candidate stacks — §20–§21 (**not PUBLISHED**)

### Addenda (future waves)

- **PC addendum** — W6-I before ECOMMERCE corridor accrual
- **RSC/page-type addendum** — W6-E optional before formal `CART_PAGE`/`CHECKOUT_PAGE` registration

### Coverage freeze

```text
RC  = 32/32
RPC = 26/32
RSC = 7/11
SC  = LANDING PASS · CATALOG PASS · PROMO PASS
PC  = 1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor
```

### Explicit exclusions

- W7 · FEATURES/REVIEWS/MAP substitution re-evaluation · implementation · Registry mutation · G3 evaluation

---

## 29. Evidence Paths

```text
projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md
reports/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md
projects/mars-website-factory/wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md
reports/wf-r01-3-5-corporate-commerce-reference-slices-charter-pass-v1.md
reports/wf-r01-3-reference-expansion-program-design-v1.md
projects/mars-website-factory/wf-r01-3-1-coverage-model-charter-v1.md
projects/mars-website-factory/reference-scaffold-contract-v1.md
projects/mars-website-factory/global-shell-contract-v1.md
projects/mars-website-factory/page-type-shell-matrix-v1.md
projects/mars-website-factory/foundry-vocabulary-canon-charter-v1.md
projects/mars-website-factory/roadmap.md
projects/mars-website-factory/OPERATIONAL-INDEX.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md
workspaces/website-factory-reference-v1/block-registry/CORE-BLOCK-LIBRARY-v1.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-GAPS-v1.md
workspaces/website-factory-reference-v1/block-registry/PAGE-BLOCK-MAPPING-v1.md
workspaces/website-factory-reference-v1/block-registry/SITE-TYPE-BLOCK-MATRIX-v2.md
workspaces/website-factory-reference-v1/block-registry/BLOCK-DEPENDENCY-RULES-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-TYPE-REGISTRY-v1.md
workspaces/website-factory-reference-v1/page-architecture/PAGE-DEPENDENCY-RULES-v1.md
workspaces/website-factory-reference-v1/page-architecture/PRODUCT-PAGE-REFERENCE-COMPOSITION-v1.md
workspaces/website-factory-reference-v1/design-system/VISUAL-PATTERN-REGISTRY-v1.md
```

---

## 30. Decision

```text
W6-A PREFLIGHT — COMPLETE · PUBLISHED
IMPLEMENTATION — NOT STARTED
BLOCK AUTHORITY — CONFIRMED (CART · CHECKOUT · PAYMENT · DELIVERY)
PAGE-TYPE — UTILITY ROUTES · REGISTRY MUTATION DEFERRED
G3 MINIMUM — CONFIRMED (+3: CART · CHECKOUT · PAYMENT)
PAYMENT BEFORE DELIVERY RPC — YES (G3)
RSC DENOMINATOR — UNCHANGED (11)
PC ADDENDUM — REQUIRED BEFORE ACCRUAL (W6-I)
NEXT — WF-R01.3.5 W6-B1 — CART Reference Block
```

---

*Preflight artefact: `projects/mars-website-factory/wf-r01-3-5-w6-a-commerce-block-reference-preflight-v1.md` · v1 · 2026-06-21*
