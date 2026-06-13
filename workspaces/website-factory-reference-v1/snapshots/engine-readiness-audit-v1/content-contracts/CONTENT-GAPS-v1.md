# Website Factory — Content Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-contracts/`  
**Статус:** future work register — **no implementation**

**Не является:** commitment schedule, charter approval, backlog with dates.

---

## Назначение

Регистр **будущих** workstreams, явно **вне** Content Architecture Layer v1. Записи здесь **не** меняют канон Block/Page/Site registries.

---

## Gap register

| Gap ID | Workstream | Description | Depends on | Status |
|--------|------------|-------------|------------|--------|
| CG-01 | **Copywriting Frameworks** | Tone, voice, readability, locale style — separate from signal architecture | Content Contracts v1 | NOT STARTED |
| CG-02 | **Offer Systems** | Structured offer models, campaign variants, message-match rules | Copywriting (CG-01) | NOT STARTED |
| CG-03 | **FAQ Libraries** | Curated Q&A banks by industry — still HITL-governed | Content Contracts v1 | NOT STARTED |
| CG-04 | **Objection Libraries** | Objection taxonomy → signal mapping playbooks | FAQ Libraries (CG-03) | NOT STARTED |
| CG-05 | **Industry Packs** | Vertical signal requirements (medical, finance, etc.) | Content Contracts v1 | NOT STARTED |
| CG-06 | **Content QA** | Human review checklists beyond signal presence | Copywriting (CG-01) | NOT STARTED |
| CG-07 | **Content Validation** | Automated signal / claim / placeholder linter | Content Contracts v1, Validation evolution | NOT STARTED |
| CG-08 | **Generation Contracts** | Prompt-safe generation bindings — **not queued** per roadmap | Content + Legal + SEO gates | NOT STARTED |
| CG-09 | **MIG Integration** | Bridge to `incoming/mig/` request pipeline for content ops | Generation Contracts (CG-08) | NOT STARTED |
| CG-10 | **CMS Field Mapping** | signal_id ↔ CMS schema / component props | Frontend charter | NOT STARTED |
| CG-11 | **Localization Layer** | Per-locale required signals and legal text variants | Legal Pack evolution | NOT STARTED |
| CG-12 | **Extended Site Types** | SAAS, WEB_APPLICATION, MARKETPLACE content profiles | Site Type charter | NOT STARTED |
| CG-13 | **Utility Page Profiles** | CART_PAGE, CHECKOUT_PAGE content contracts | Page Architecture extension | NOT STARTED |
| CG-14 | **JSON Schema Export** | Machine-readable content contract schema | Content Validation (CG-07) | NOT STARTED |
| CG-15 | **SEO Text Generation** | Meta/title/body SEO generation — explicitly out of Content v1 | SEO Architecture | NOT STARTED |

---

## Explicitly out of scope (v1)

| Item | Rationale |
|------|-----------|
| Runtime content engine | No implementation in reference workspace |
| Prompt libraries | Generation Contracts (CG-08) |
| Marketing copy examples | Architecture-only charter |
| Article / blog content types | No `page_type` in v1 minimum |
| Automated MIG execution | Human-operated pipeline only |

---

## Promotion criteria (documentation)

Workstream may graduate from GAP → charter when:

1. Content Contracts v1 **ACCEPTED** by operator.
2. Upstream Validation + Legal gates documented.
3. No new taxonomy introduced without registry charter.
4. Evidence rules preserved (no relaxation of CT-R13–CT-R18).

---

## SAFE UNKNOWN

- Priority order among CG-01–CG-15 — **not scheduled** in this document.
- Resource ownership — **UNKNOWN**.

---

*Content Gaps version: v1.*
