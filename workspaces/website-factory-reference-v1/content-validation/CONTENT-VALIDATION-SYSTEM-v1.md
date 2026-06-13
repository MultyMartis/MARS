# Website Factory — Content Validation System v1

**Версия:** v1  
**Дата:** 2026-06-01  
**Operator:** APPROVED BY OPERATOR  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** Content Validation Layer — **documentation only**

**Не является:** content generation, content QA automation, runtime validation, prompt library, copywriting, SEO text production, CMS plugin, MIG/ORCA integration.

---

## 1. Назначение

Content Validation System v1 — **второй validation-слой** Website Factory (после Page → Block Validation). Слой отвечает на вопрос:

> **Соответствует ли content architecture (семантические signals) каноническим Content Contracts для данного `site_type_code` + `page_type` + `block_id`?**

Проверяется **архитектура контента** — наличие, отсутствие и совместимость **content signals**, не сгенерированный текст, не финальный copy, не runtime output.

---

## 2. Каноническая цепочка (расширенная)

```text
Site Type Registry
        ↓
   Blueprints
        ↓
Page Architecture
        ↓
 Block Registry
        ↓
Page Block Validation          ← ACCEPTED (blocks on page)
        ↓
   SEO Architecture             ← ACCEPTED
        ↓
  Design System Mapping          ← ACCEPTED (pattern families)
        ↓
  Content Contracts              ← ACCEPTED (signals only)
        ↓
  Content Validation             ← THIS WORKSTREAM (v1)
        ↓
 Frontend Layer                  ← FUTURE
```

**Gate rule:** Content Validation **не запускается**, если Page Block Validation для целевой страницы имеет `status` = **FAIL** или содержит **CRITICAL** в missing/forexpected blocks.

---

## 3. Роль Content Validation

| Делает | Не делает |
|--------|-----------|
| Проверяет обязательные `signal_id` на block/page | Не пишет и не переписывает copy |
| Проверяет forbidden signals отсутствуют | Не генерирует landing/article |
| Проверяет LEGAL_PAGE ↔ Legal Pack alignment | Не валидирует факты в runtime |
| Проверяет trust/conversion signal architecture | Не заменяет human legal review |
| Эмитит PASS / PASS_WITH_WARNINGS / FAIL | Не запускает automated QA bots |
| Ссылается на 29 `block_id`, 10 `page_type`, Core 5 | Не добавляет taxonomy |

---

## 4. Inputs (обязательные)

| Input | Источник | Использование |
|-------|----------|---------------|
| `site_type_code` | [registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) | SITE-TYPE-CONTENT-MAPPING + matrix overlays |
| `blueprint_ref` | [blueprints/](../blueprints/) | IA scope, commerce model |
| `page_type` | [page-architecture/PAGE-TYPE-REGISTRY-v1.md](../page-architecture/PAGE-TYPE-REGISTRY-v1.md) | PAGE-CONTENT-CONTRACTS |
| `block_id` | [block-registry/BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) | BLOCK-CONTENT-CONTRACTS |
| Block stack stance | PAGE-BLOCK-MAPPING, page-block validation outcome | Validate signals **only** for blocks present / REQUIRED |
| Content contracts | [content-contracts/](../content-contracts/) | Signal requirements |
| Page block validation | [page-block-validation/](../page-block-validation/) | Upstream gate |
| Legal Pack | [legal/](../legal/) (FROZEN) | LEGAL_PAGE, consent, disclosures |
| Legal Entity Card | [legal-entity/](../legal-entity/) | NAP / entity signals |

---

## 5. Outputs (v1)

| Artefact | Файл | Содержание |
|----------|------|------------|
| System (this doc) | CONTENT-VALIDATION-SYSTEM-v1.md | Layer role, chain, gates |
| Contract | [CONTENT-VALIDATION-CONTRACT-v1.md](CONTENT-VALIDATION-CONTRACT-v1.md) | Validation run fields |
| Rules | [CONTENT-VALIDATION-RULES-v1.md](CONTENT-VALIDATION-RULES-v1.md) | Architecture gates |
| Matrix | [CONTENT-SIGNAL-VALIDATION-MATRIX-v1.md](CONTENT-SIGNAL-VALIDATION-MATRIX-v1.md) | Signals × types × blocks |
| Failure library | [CONTENT-FAILURE-LIBRARY-v1.md](CONTENT-FAILURE-LIBRARY-v1.md) | Typed failures |
| Severity | [CONTENT-SEVERITY-SYSTEM-v1.md](CONTENT-SEVERITY-SYSTEM-v1.md) | INFO–CRITICAL |
| Gaps | [CONTENT-VALIDATION-GAPS-v1.md](CONTENT-VALIDATION-GAPS-v1.md) | Future work register |
| Roadmap | [CONTENT-VALIDATION-ROADMAP-v1.md](CONTENT-VALIDATION-ROADMAP-v1.md) | Maturity path |

---

## 6. Validation unit

**Один validation run** = один scope:

| Scope | `validation_target` | Typical use |
|-------|---------------------|-------------|
| **Block** | `site_type_code` + `page_type` + `block_id` | Per REQUIRED block on page stack |
| **Page** | `site_type_code` + `page_type` (page-level signals) | After all block runs |
| **Legal route** | `LEGAL_PAGE` + document binding | Legal Pack gate |

Block-level runs **агрегируются** в page-level status по правилам [CONTENT-VALIDATION-CONTRACT-v1.md](CONTENT-VALIDATION-CONTRACT-v1.md).

---

## 7. Relationship to Content Contracts

| Layer | Question |
|-------|----------|
| **Content Contracts** | What signals **should** exist? |
| **Content Validation** | Do declared slots **satisfy** contracts for this architecture? |

Content Contracts **не изменяются** этим workstream. Validation **только ссылается** на них.

---

## 8. Operator workflow (v1 manual)

1. Confirm Page Block Validation **PASS** or **PASS_WITH_WARNINGS** (no CRITICAL).
2. Resolve `site_type_code`, Blueprint, `page_type`, block stack.
3. For each **REQUIRED** `block_id` on stack — run block content validation (checklist).
4. Run page-level content validation (PAGE-CONTENT-CONTRACTS).
5. Apply SITE-TYPE-CONTENT-MAPPING forbidden patterns.
6. Record outcome per [CONTENT-VALIDATION-CONTRACT-v1.md](CONTENT-VALIDATION-CONTRACT-v1.md).
7. **Halt** on FAIL / CRITICAL before Frontend or Generation Contracts.

---

## 9. Explicit exclusions (v1)

| Exclusion | Status |
|-----------|--------|
| Generated text validation | FUTURE — [CONTENT-VALIDATION-GAPS-v1.md](CONTENT-VALIDATION-GAPS-v1.md) |
| Fact-checking / evidence verification automation | FUTURE |
| Industry-specific validators | FUTURE |
| Runtime / CI validators | FUTURE |
| New `site_type_code`, `page_type`, `block_id`, `signal_id` | **FORBIDDEN** without charter |
| Prompts / Generation Contracts | **OUT OF SCOPE** — not queued |

---

## 10. SAFE UNKNOWN

- Whether operator uses single spreadsheet vs per-page markdown for validation runs — **not prescribed**.
- Integration with Design `VF_*` selection tooling — **FUTURE** manual cross-check only in v1.
- Acceptance criteria for semi-automatic phase — **FUTURE** charter.

---

*Content Validation System version: v1.*
