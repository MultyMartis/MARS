# Website Factory — Validation Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** known missing capabilities — **documentation only**  
**Дата:** 2026-05-31

---

## Назначение

Validation Gaps v1 фиксирует, что **ещё не существует** после authoring Page Block Validation System v1. Предотвращает ложные заявления о runtime, automation, или полноте validation coverage.

---

## Implementation gaps

| Gap | Description | v1 status | Target phase |
|-----|-------------|-----------|--------------|
| **Automated validator** | Executable engine applying PAGE-BLOCK-VALIDATION-RULES | **NOT IMPLEMENTED** | Automated Validation |
| **CLI validator** | Command-line tool reading project manifest → VALIDATION-CONTRACT output | **NOT IMPLEMENTED** | Semi-Automatic Validation |
| **Blueprint validator** | Cross-page required_pages + site-wide FORBIDDEN sweep | **NOT IMPLEMENTED** | Semi-Automatic Validation |
| **Frontend validator** | Template / component scan vs page contract | **NOT IMPLEMENTED** | Automated Validation |
| **Page scanner** | DOM or static HTML analysis of deployed/preview pages | **NOT IMPLEMENTED** | Runtime QA Layer |
| **JSON Schema** | Machine-readable VALIDATION-CONTRACT + PAGE-CONTRACT schemas | **NOT DEFINED** | Semi-Automatic Validation |
| **CI integration** | Validation gate in build pipeline | **NOT IMPLEMENTED** | Automated Validation |
| **Batch validation envelope** | Single run for entire site IA | **NOT DEFINED** | Semi-Automatic Validation |

---

## Documentation / registry gaps

| Gap | Description | Impact on validation | Resolution owner |
|-----|-------------|----------------------|------------------|
| **Mobile sticky CTA** | Resolved — canonical `CTA`; sticky = implementation variant | Validate as `CTA` present; sticky partial optional | **CLOSED** (2026-06-04) |
| **Embedded video** | Resolved — not a `block_id`; media within HERO/content | Out of block validation scope | **CLOSED** (2026-06-04) |
| **THANK_YOU_PAGE** | Not in PAGE-TYPE-REGISTRY v1 minimum | No validation rows | Page Architecture extension |
| **CART_PAGE / CHECKOUT_PAGE** | Documented in PAGE-DEPENDENCY-RULES; not canonical page_type | Utility routes validated by reference only | Page Architecture extension |
| **required_block_groups formal syntax** | OR-groups manual in v1 | Operator burden | Validation Contract v2 |
| **Extended site types** | SAAS, WEB_APPLICATION, MARKETPLACE — no validation matrices | Out of scope | Registry charter |

---

## Cross-layer inconsistencies (documented, not auto-resolved)

Alignment pass at validation v1 authoring:

| # | Inconsistency | Layers | Validation handling |
|---|---------------|--------|---------------------|
| 1 | Mobile sticky CTA labeled `STICKY_CTA` in legacy docs | Page Architecture ↔ Block Registry | **RESOLVED** — use `CTA` (VF-015 updated) |
| 2 | `VIDEO` as pseudo block_id in legacy docs | Page Architecture ↔ Block Registry | **RESOLVED** — media embed note only |
| 3 | LANDING `FAQ` severity: mapping REQUIRED; task examples say WARNING for generic FAQ | Mapping ↔ Severity examples | Context-dependent: LANDING = ERROR/WARNING strict |
| 4 | LEGAL_PAGE `required_blocks: none` vs `LEGAL_LINKS` REQUIRED elsewhere | Legal ↔ Page validation | Cross-route rule (Rule 6) |
| 5 | CORPORATE subtree inherits CATALOG/ECOMMERCE block rows | Blueprint ↔ Page validation | Document route groups; manual sweep |
| 6 | Block Registry Alignment operator COMPLETE gate | Priorities ↔ Validation | **UNKNOWN** — validation authored; gate pending |

**Verdict:** Site Type Registry → Blueprints → Page Architecture → Block Registry chain is **MOSTLY ALIGNED** for Core Types. Validation System v1 **references** authoritative mappings; does not mutate upstream layers.

---

## Manual validation gaps

| Gap | Description |
|-----|-------------|
| No standard project manifest path | Operator must collect `actual_blocks` from IA doc ad hoc |
| No validation report template | VALIDATION-CONTRACT YAML is reference only |
| No operator training checklist beyond PAGE-BLOCK-VALIDATION-RULES | **FUTURE** operator guide |
| No integration with mars-survivability diff advisor | **FUTURE** optional helper |

---

## Explicit non-gaps (in scope for v1)

| Delivered | Location |
|-----------|----------|
| Validation system definition | PAGE-BLOCK-VALIDATION-SYSTEM-v1.md |
| Validation contract fields | VALIDATION-CONTRACT-v1.md |
| Validation rules | PAGE-BLOCK-VALIDATION-RULES-v1.md |
| Page type matrix | PAGE-TYPE-VALIDATION-MATRIX-v1.md |
| Blueprint matrix | BLUEPRINT-VALIDATION-MATRIX-v1.md |
| Severity system | VALIDATION-SEVERITY-SYSTEM-v1.md |
| Failure library | VALIDATION-FAILURE-LIBRARY-v1.md |
| Evolution roadmap | VALIDATION-ROADMAP-v1.md |

---

## SAFE UNKNOWN

- Timeline for closing each gap — **not scheduled**
- Whether CLI lives in `website-factory-reference-v1/tools/` or separate repo — **UNKNOWN**
- Operator COMPLETE gate for Block Registry Alignment v1 — **pending**

---

*Validation Gaps version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
