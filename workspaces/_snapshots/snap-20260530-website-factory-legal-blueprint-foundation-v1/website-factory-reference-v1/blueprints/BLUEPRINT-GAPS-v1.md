# Website Factory — Blueprint Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/blueprints/`  
**Статус:** gap register — что **отсутствует** до full website generation from Blueprints  
**Связь:** [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

**Honesty boundary:** Blueprint System v1 — **architecture documentation only**. Items below are **missing** for automated or semi-automated end-to-end generation.

---

## Gap summary

| # | Gap area | Severity | Roadmap link |
|---|----------|----------|--------------|
| G1 | Block Registry alignment | **High** | Priority 2 — BLOCK REGISTRY alignment |
| G2 | Design System mapping | **High** | Priority 4 — DESIGN SYSTEM MAPPING |
| G3 | Page Architecture contracts | **High** | Not yet queued |
| G4 | SEO Mapping v2 depth | **Medium** | Priority 3 — SITE-TYPE-SEO-MAPPING-v2 |
| G5 | Conversion patterns library | **Medium** | Not yet queued |
| G6 | Blueprint machine schema | **Medium** | Not queued |
| G7 | ECOMMERCE legal extension | **High** (for ecommerce go-live) | Legal Pack Extension — FUTURE |
| G8 | Extended Type Blueprints | **Low** (by design) | Charter per type |
| G9 | Automated validation gates | **Medium** | Survivability / CI — FUTURE |
| G10 | Content generation contracts | **High** | Not in Blueprint scope |

---

## G1 — Block Registry alignment

**Current state:**

- Blueprints reference block **roles** aligned with [SITE-TYPE-BLOCK-MAPPING-v1.md](../registry/SITE-TYPE-BLOCK-MAPPING-v1.md)
- Canonical `block_id` lives in `projects/mars-website-factory/block-registry-v0.md` — **different vocabulary** (`site_type_id` names differ from v1 Registry)
- Reference partials exist for LANDING subset only: `src/partials/sections/`

**Missing:**

- Block Registry v1 with stable `block_id` ↔ partial path ↔ site type matrix
- Blocks for CATALOG, ECOMMERCE, CORPORATE (cart, checkout, PLP, filters) in reference workspace
- Machine-checkable block ↔ Blueprint compatibility

**Blocks full generation until:** Priority 2 complete + reference partials expanded or project-scaffold charter.

---

## G2 — Design System mapping

**Current state:**

- LANDING tokens/partials in reference workspace (`src/scss/foundations/_tokens.scss`)
- Visual contract v0 at `projects/orca/visual-semantics/contracts/website-factory-visual-contract-v0.md`

**Missing:**

- Per-site-type design token profiles
- Component variants for catalog grid, checkout, corporate mega-nav
- Blueprint → design component mapping table
- Density / visual budget per site type

**Blocks full generation until:** Priority 4 — DESIGN SYSTEM MAPPING.

---

## G3 — Page Architecture contracts

**Current state:**

- Blueprints define `required_pages` and URL patterns at documentation level
- No formal Page Architecture Contract (analogous to LEGAL-GENERATION-CONTRACT-v1)

**Missing:**

- Page template IDs per page role
- Section slot ordering schema (machine-readable)
- Hybrid subtree inheritance rules (CORPORATE → CATALOG) as formal contract
- Thank-you / confirmation page variants per conversion type

**Blocks full generation until:** Page Architecture Contract chartered and versioned.

---

## G4 — SEO Mapping v2

**Current state:**

- [SITE-TYPE-SEO-MAPPING-v1.md](../registry/SITE-TYPE-SEO-MAPPING-v1.md) — priority + architecture narrative
- Blueprints embed `seo_requirements` derived from v1

**Missing:**

- v2 matrix depth (parity with Legal Mapping v2)
- Faceted SEO addendum for CATALOG
- Schema template library
- Indexation rule engine (even as documentation checklist v2)

**Blocks SEO automation until:** Priority 3 — SITE-TYPE-SEO-MAPPING-v2.

**Note:** SEO **strategy** can proceed from Blueprint + v1; SEO **pack generation** cannot.

---

## G5 — Conversion patterns library

**Current state:**

- Conversion requirements documented per Blueprint
- LANDING reference implements form + sticky CTA + modal callback wiring

**Missing:**

- Canonical conversion pattern IDs (lead-form-v1, rfq-v1, checkout-guest-v1, etc.)
- Analytics event contract per pattern
- A/B variant policy for landings
- Multi-step form architecture for CORPORATE / ECOMMERCE

**Blocks conversion automation until:** pattern library chartered.

---

## G6 — Blueprint machine schema

**Current state:**

- Markdown-only canonical Blueprints
- [BLUEPRINT-CONTRACT-v1.md](BLUEPRINT-CONTRACT-v1.md) — human field contract

**Missing:**

- JSON Schema / YAML export for Blueprint instances
- Project Blueprint instance file format (`project.blueprint.yaml`)
- Diff tool: project IA vs canonical Blueprint

**Blocks tooling integration until:** schema defined.

---

## G7 — ECOMMERCE legal extension

**Current state:**

- Legal Pack v1 FROZEN — Core L1–L4 only
- [ECOMMERCE-BLUEPRINT-v1.md](ECOMMERCE-BLUEPRINT-v1.md) documents dependency on E1–E4 Extension

**Missing:**

- E1 Public Offer, E2 Payment Rules, E3 Delivery Rules, E4 Return Policy templates
- Extension footer link taxonomy
- Generation workflow for Extension Pack

**Blocks ecommerce production go-live until:** Extension Pack chartered + legal sign-off (may proceed with Core for staging only — HITL).

---

## G8 — Extended Type Blueprints

**By design — not a v1 gap for Core Factory:**

- No Blueprints for `SAAS`, `WEB_APPLICATION`, `MARKETPLACE`
- Extended Types require architecture charter before any Blueprint fork

**Future work:** separate charter per Extended Type.

---

## G9 — Automated validation gates

**Current state:**

- Human operator checklists in Implementation Rules
- mars-survivability Factory enforcement docs exist at project level

**Missing:**

- CI check: Blueprint referenced in project manifest
- Drift detector: cart block on CATALOG classified project
- Pre-deploy gate: required_pages exist

**Blocks unattended generation until:** validation strategy implemented (documentation-only enforcement today).

---

## G10 — Content generation contracts

**Explicitly out of Blueprint v1 scope but required for full Factory:**

**Missing:**

- Hero/copy generation contract per site type
- Product content model (PIM feed → PDP)
- Legal content — covered by Legal Pack (exists); Extension content — missing
- Blog/news content workflow for PROMO / CORPORATE

**Blocks content automation until:** separate content pack charters (Orca / content-packs trajectory).

---

## What Blueprints v1 **do** enable today

| Capability | Status |
|------------|--------|
| Site type → IA skeleton decision | **Yes** — operator + agent |
| Required vs optional page/block planning | **Yes** |
| Exclusion enforcement (documentation) | **Yes** |
| Legal/SEO requirement pointers | **Yes** |
| LANDING reference frontend pattern | **Yes** — manual |
| Automatic full site generation | **No** |

---

## Recommended closure sequence

Aligns with [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md):

1. ~~SITE-TYPE-BLUEPRINTS-v1~~ — **this deliverable**
2. BLOCK REGISTRY alignment
3. SITE-TYPE-SEO-MAPPING-v2
4. DESIGN SYSTEM MAPPING
5. Page Architecture Contract (proposed — not yet in register)
6. Conversion patterns library (proposed)
7. ECOMMERCE Legal Extension (when ecommerce projects charter)

---

## SAFE UNKNOWN

- Timeline for Page Architecture Contract — **not scheduled**
- Owner for Block Registry v1 vs v0 migration — **UNKNOWN**
- Whether Triumph workspace will serve as PROMO reference — **UNKNOWN** (Triumph not modified per task constraint)
- Integration specs (payment, PIM, ATS) — **per project**

---

*Blueprint gaps version: v1.*
