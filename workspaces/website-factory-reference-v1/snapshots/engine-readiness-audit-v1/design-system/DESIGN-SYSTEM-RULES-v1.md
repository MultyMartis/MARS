# Website Factory — Design System Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/design-system/`  
**Статус:** architecture rules — **documentation only**  
**Связь:** [DESIGN-SYSTEM-MAPPING-v1.md](DESIGN-SYSTEM-MAPPING-v1.md), [page-block-validation/PAGE-BLOCK-VALIDATION-RULES-v1.md](../page-block-validation/PAGE-BLOCK-VALIDATION-RULES-v1.md), [seo-architecture/SEO-IMPLEMENTATION-RULES-v1.md](../seo-architecture/SEO-IMPLEMENTATION-RULES-v1.md)

**Не является:** automated linter, design police bot, CI gate.

---

## Rule categories

| ID | Rule | Severity |
|----|------|----------|
| DS-R01 | **Design follows Blueprint** — pattern selection must respect Blueprint IA, required pages, and block stacks | CRITICAL |
| DS-R02 | **Design subordinate to Block Registry** — only 29 v1 `block_id`; patterns bind to existing blocks only | CRITICAL |
| DS-R03 | **Design cannot violate Validation** — FORBIDDEN/CRITICAL block stances prohibit pattern binding | CRITICAL |
| DS-R04 | **Design cannot bypass required blocks** — REQUIRED blocks must have a pattern from allowed set in BLOCK-VISUAL-MAPPING | CRITICAL |
| DS-R05 | **Design cannot bypass SEO intent** — page design role must not contradict PAGE-SEO-CONTRACT and SITE-TYPE-SEO-MAPPING-v2 | HIGH |
| DS-R06 | **LEGAL_PAGE inherits project design** — global chrome (footer/nav) only; VF_LEGAL_DOCUMENT_BODY for body; no marketing patterns | CRITICAL |
| DS-R07 | **No styling in architecture docs** — colors, typography, spacing, CSS, Figma specs forbidden in Design Layer v1 artefacts | CRITICAL |
| DS-R08 | **No new taxonomy in Design workstream** — no new `site_type_code`, `page_type`, or `block_id` | CRITICAL |
| DS-R09 | **Legal Pack FROZEN** — design rules must not require Legal Pack modification | CRITICAL |
| DS-R10 | **Foundation FROZEN** — Design Layer maps; does not rewrite Registry/Blueprint/Block/Page/Validation/SEO canon | HIGH |
| DS-R11 | **Single primary action per Blueprint** — multiple competing CTA pattern families on one page require operator sign-off | HIGH |
| DS-R12 | **HITL for regulated claims** — trust/pricing/comparison patterns do not replace human review of claims | HIGH |
| DS-R13 | **Extended site types** — no design profile claim for SAAS/WEB_APPLICATION/MARKETPLACE until charter | MEDIUM |
| DS-R14 | **Reference workspace ≠ canon** — `src/partials/` informs examples only; pattern choice follows registry maps | MEDIUM |
| DS-R15 | **Stop on Validation FAIL** — no Frontend or visual implementation binding until block validation resolved | CRITICAL |

---

## Layer interaction rules

### Blueprint

- Blueprint `required_pages` determine which PAGE-TYPE-DESIGN-MAPPING profiles apply.
- Blueprint-level FORBIDDEN blocks (BLUEPRINT-BLOCK-MAPPING) **invalidate** entire pattern families site-wide for that block.

### Page Architecture

- `page_type` from [PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) only.
- PAGE-CONTRACT required sections must be expressible via allowed patterns (content shape — future Content Contracts).

### Block Registry

- One block instance → one primary `pattern_id` per placement (secondary variants documented in project log).
- Blocks without pattern in BLOCK-VISUAL-MAPPING → **gap**, not ad-hoc invention.

### Validation

- PASS (manual) documented before design sign-off.
- VALIDATION-SEVERITY CRITICAL = halt.

### SEO

- LANDING: design supports minimal SEO — no multi-hub patterns as primary.
- ECOMMERCE: checkout utility routes — no SEO-led marketing patterns on cart/checkout.
- FAQ_PAGE: accordion hub aligns with informational intent — not legal document pattern.

### Legal

- Legal Entity Discovery data required before CONTACT/LEAD_FORM patterns implying NAP/PII.
- Consent rules apply to LEAD_FORM patterns — Legal Pack, not Design Layer.

---

## Forbidden claims (documentation discipline)

| Forbidden claim | Correct statement |
|-----------------|-------------------|
| «Design system implemented» | Design **architecture** documented only |
| «Components ready» | Pattern families defined; components in gaps |
| «Figma synced» | FUTURE — see gaps |
| «Auto-validates design» | Human-operated; no runtime |

---

## Operator checklist (pre-Frontend)

1. `site_type_code` + Blueprint frozen  
2. Page list → `page_type` mapped  
3. Per-page block stack validated  
4. Per REQUIRED block: `pattern_id` chosen from BLOCK-VISUAL-MAPPING  
5. SITE-TYPE + PAGE-TYPE design profiles checked  
6. LEGAL_PAGE pattern = VF_LEGAL_DOCUMENT_BODY only  
7. No styling specs in architecture log  

---

*Design System Rules version: v1.*
