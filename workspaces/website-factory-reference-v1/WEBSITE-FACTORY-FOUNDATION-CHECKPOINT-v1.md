# Website Factory — Foundation Checkpoint v1

**Версия:** v1  
**Дата checkpoint:** 2026-05-30  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/` + Triumph V6 legal pilot  
**Snapshot:** [../_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/](../_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/)

**Не является:** runtime, CI-валидатором, production deploy authorization, юридической экспертизой.

---

## Purpose

Стабильная точка восстановления **после** завершения Legal Pack foundation и **до** brain polishing / consistency pass по Blueprint и Block Registry.

Checkpoint фиксирует **documentation + validated pilot** состояние — не продукт Website Factory runtime.

---

## Foundation status

| Component | Location | Status |
|-----------|----------|--------|
| **Legal Pack v1** | [legal/](legal/) + [legal-entity/](legal-entity/) | **FROZEN** — [LEGAL-PACK-v1-FREEZE.md](legal/LEGAL-PACK-v1-FREEZE.md) |
| **Legal Entity Discovery v1** | [legal-entity/](legal-entity/) | **ACCEPTED** |
| **Site Type Registry v1** | [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md) | **ACCEPTED** |
| **Site Type Blueprints v1** | [blueprints/](blueprints/) | **IN PROGRESS** |
| **Block Registry Alignment v1** | [block-registry/](block-registry/) | **IN PROGRESS** |

---

## Validated pilot — Triumph Manipulator V6

**Reference implementation:** `workspaces/triumph-manipulator-landing-v6/`

| Artifact | Path |
|----------|------|
| Legal input | `legal/TRIUMPH-LEGAL-INPUT-v1.md` |
| Legal entity card | `legal-entity/LEGAL-ENTITY-CARD-v1.md` |
| L1–L4 pages | `src/pages/privacy-policy/`, `consent-personal-data/`, `user-agreement/`, `cookie-files-policy/` |
| Legal partials | `src/partials/sections/legal/` |
| Legal styles | `src/scss/components/_content-page.scss`, `src/scss/sections/_legal-pages.scss`, `src/scss/style.scss` |

**Validation (2026-05-30):** Footer Rule, Consent Rule, canonical URLs, zero forbidden placeholders — **PASS**. Build **PASS**.

Подробности: [../_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/reports/website-factory-legal-blueprint-foundation-checkpoint-v1.md](../_snapshots/snap-20260530-website-factory-legal-blueprint-foundation-v1/reports/website-factory-legal-blueprint-foundation-checkpoint-v1.md)

---

## Delivered at checkpoint

### Legal Pack v1 (FROZEN)

- Core Legal Pack L1–L4 templates
- Legal Pack Architecture, Generation Contract, Workflow
- Legal Entity Discovery System
- Legal Input Sheet + instructions
- Production rules: Footer Rule, Consent Rule, placeholder gate
- [SITE-TYPE-LEGAL-MAPPING-v2.md](legal/SITE-TYPE-LEGAL-MAPPING-v2.md)

### Site Type Registry v1 (ACCEPTED)

- [registry/SITE-TYPE-REGISTRY-v1.md](registry/SITE-TYPE-REGISTRY-v1.md)
- Matrix, block mapping v1, SEO mapping v1, implementation rules

### Site Type Blueprints v1 (IN PROGRESS)

- [blueprints/BLUEPRINT-SYSTEM-v1.md](blueprints/BLUEPRINT-SYSTEM-v1.md)
- 5 Core Type Blueprints (LANDING, PROMO, CATALOG, ECOMMERCE, CORPORATE)
- Contract, comparison matrix, implementation rules, gaps

### Block Registry Alignment v1 (IN PROGRESS)

- [block-registry/BLOCK-REGISTRY-v1.md](block-registry/BLOCK-REGISTRY-v1.md)
- Categories, core library, SITE-TYPE-BLOCK-MATRIX-v2, dependency rules, conversion roles, gaps

---

## Next workstream

**Immediate:** Website Factory brain polishing / registry consistency pass

**Then (sequenced):**

1. Page Architecture Contracts  
2. SEO Mapping v2  
3. Design System Mapping  

См. [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## Explicit exclusions (post-checkpoint until new charter)

| Item | Status |
|------|--------|
| New legal page generation | **FORBIDDEN** without operator charter |
| Legal Pack modifications | **FORBIDDEN** — FROZEN |
| Triumph visual design changes | **OUT OF SCOPE** |
| SMTP / mailer changes | **OUT OF SCOPE** |
| Extended Type Blueprints | **NOT STARTED** |
| Runtime / CI automation | **FUTURE** |

---

## SAFE UNKNOWN

- Exact delivery dates for Blueprint COMPLETE gate and Block Registry COMPLETE gate — **not scheduled**
- Triumph production deploy authorization — **UNKNOWN**
- Page Architecture Contracts document location — **to be authored** in next workstream
- CI automation for legal placeholder gate — **FUTURE**

---

*Checkpoint v1 — 2026-05-30. Canonical location: `workspaces/website-factory-reference-v1/`.*
