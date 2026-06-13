# Website Factory — Content Validation Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** future work register — **no implementation**  
**Связь:** [CONTENT-VALIDATION-ROADMAP-v1.md](CONTENT-VALIDATION-ROADMAP-v1.md), [content-contracts/CONTENT-GAPS-v1.md](../content-contracts/CONTENT-GAPS-v1.md)

---

## Назначение

Этот документ регистрирует **только будущую** работу. Записи **не** утверждают наличие продуктов, runtime, automation или orchestration.

---

## Gap register

| ID | Gap | Notes | Status |
|----|-----|-------|--------|
| CVG-01 | **Generated text validation** | Post-generation copy vs contracts | NOT STARTED |
| CVG-02 | **Fact validation** | Automated claim ↔ source matching | NOT STARTED |
| CVG-03 | **Industry-specific validation** | Medical, finance, regulated verticals | NOT STARTED |
| CVG-04 | **Content QA automation** | Bots, linters, CI content gates | NOT STARTED |
| CVG-05 | **Evidence verification** | SOURCE_DOCUMENTED / UGC_AUTHENTIC enforcement | NOT STARTED |
| CVG-06 | **MIG integration** | Request/outcome bridge for content validation | NOT STARTED |
| CVG-07 | **Runtime validators** | CLI, API, CMS plugins | NOT STARTED |
| CVG-08 | **JSON Schema for validation contract** | Machine-readable CONTENT-VALIDATION-CONTRACT | NOT STARTED |
| CVG-09 | **Semi-automatic checklist tooling** | Spreadsheet/import helpers — S5 boundary | NOT STARTED |
| CVG-10 | **Locale-specific evidence rules** | Multi-jurisdiction content gates | NOT STARTED |
| CVG-11 | **CART_PAGE / CHECKOUT_PAGE page profiles** | ECOMMERCE extension page-level signals | NOT STARTED |
| CVG-12 | **Signal ↔ CMS field mapping** | Implementation bridge | NOT STARTED |
| CVG-13 | **Design VF_* automated cross-check** | Pattern vs required signal expressibility | NOT STARTED |
| CVG-14 | **Extended site types** | SAAS, WEB_APPLICATION, MARKETPLACE matrices | NOT STARTED — charter required |

---

## Explicit non-gaps (out of scope forever for v1 doc layer)

| Item | Reason |
|------|--------|
| Content generation | Generation Contracts — separate charter |
| Prompt libraries | Not content validation |
| SEO copy production | SEO architecture is structural only |
| Page block validation | **ACCEPTED** separate layer — do not duplicate |

---

## Dependency on other future workstreams

| Upstream future | Enables |
|-----------------|---------|
| Generation Contracts (CG-08) | Generated text validation (CVG-01) |
| Content QA product charter | CVG-04 |
| MIG operational charter | CVG-06 |

---

## SAFE UNKNOWN

- Priority order among CVG-* — **not scheduled**; operator charter per item.
- Whether CVG-09 qualifies as S5 helper vs escalation — **review at charter time**.

---

*Content Validation Gaps version: v1.*
