# Website Factory — Design System Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** future work register — **no implementation**

**Связь:** [DESIGN-SYSTEM-MAPPING-v1.md](DESIGN-SYSTEM-MAPPING-v1.md), [ARCHITECTURE-FOUNDATION-v1.md](../ARCHITECTURE-FOUNDATION-v1.md)

---

## Purpose

Register **approved future layers** without starting implementation. Items require **operator charter** before workstream promotion.

---

## Gap register

| ID | Gap | Notes | Depends on |
|----|-----|-------|------------|
| DG-01 | **Design Tokens** | Color, spacing, radius semantic tokens | Design Layer v1 ACCEPTED |
| DG-02 | **Color Systems** | Brand/theme palettes | DG-01 |
| DG-03 | **Typography Systems** | Type scale, roles | DG-01 |
| DG-04 | **Component Systems** | Reusable UI components bound to `pattern_id` | DG-01–03, Frontend charter |
| DG-05 | **Design QA** | Human/automated pattern compliance checks | Validation automation roadmap |
| DG-06 | **Figma Integration** | Library sync, Code Connect | Orca/visual-semantics alignment |
| DG-07 | **Pattern Library Expansion** | Additional `VF_*` variants per family | Production evidence from pilots |
| DG-08 | **Responsive Design Rules** | Breakpoint architecture per pattern | DG-04 |
| DG-09 | **Animation / Motion Rules** | Motion charter per pattern family | DG-04 |
| DG-10 | **Frontend Mapping** | `pattern_id` → partial/component path contract | Frontend Layer charter |
| DG-11 | **Content Contracts** | Content shape per pattern (copy slots) | Next roadmap item |
| DG-12 | **Generation Contracts** | AI/human generation boundaries | Content Contracts |
| DG-13 | **Extended Site Type Design Profiles** | SAAS, WEB_APPLICATION, MARKETPLACE | Registry charter |
| DG-14 | **ECOMMERCE utility page_types** | CART_PAGE, CHECKOUT_PAGE formal design mapping | Page Architecture extension |
| DG-15 | **Design project log format** | Machine-readable pattern selection per route | DG-10 |
| DG-16 | **STICKY_CTA / VIDEO registry closure** | Align reference partials to block_id policy | **CLOSED** (2026-06-04) — `CTA` variant + media embed note |
| DG-17 | **Accessibility pattern hints** | a11y role per VF_* | DG-04 |
| DG-18 | **Dark/light theme architecture** | Theme binding to tokens | DG-02, DG-03 |
| DG-19 | **website-factory-visual-contract-v0 reconciliation** | Merge or supersede external v0 | Operator decision |
| DG-20 | **Runtime design validator** | CI gate for pattern/block/SEO alignment | VALIDATION-ROADMAP + DG-05 |

---

## Explicitly out of scope (v1 gaps doc)

| Item | Status |
|------|--------|
| Implement tokens/CSS | NOT STARTED |
| Generate mockups | NOT STARTED |
| Build Storybook | NOT STARTED |
| Orchestration / MIG design agent | NOT STARTED |

---

## Suggested sequence (non-binding)

1. Accept Design System Mapping v1  
2. Content Contracts (roadmap)  
3. Design Tokens + Typography + Color (charter)  
4. Frontend Mapping + Component Systems  
5. Figma + Design QA  

**Dates:** not scheduled — see SAFE UNKNOWN in priorities doc.

---

*Design System Gaps version: v1.*
