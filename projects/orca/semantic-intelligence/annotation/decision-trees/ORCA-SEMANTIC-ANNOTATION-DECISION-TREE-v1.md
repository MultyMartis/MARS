# ORCA Semantic Annotation Decision Tree v1

**Tree ID:** `orca-semantic-annotation-decision-tree`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-annotation-decision-tree-v1.json`](orca-semantic-annotation-decision-tree-v1.json)

---

## Purpose

Human decision trees for ORCA Semantic Intelligence v1 annotation. Each subtree routes a phrase class to exactly one terminal outcome: **ACCEPT**, **REJECT**, or **ABSTAIN**.

**No subtree** may terminate in service mapping, campaign grouping, or cluster assignment.

**Usage:** Follow after mandatory 10-step annotation order ([`ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md)). Trees assist eligibility (Step 8); they do not replace literal reading or signal extraction.

---

## Global pre-check (all subtrees)

```
START
  │
  ├─ Malformed / empty / irrelevant? ──YES──► SUBTREE: Malformed
  │
  ├─ Complete Steps 1–7 of annotation order?
  │     NO ──► STOP (do not assign eligibility)
  │
  └─ Route to class subtree below
```

---

## Subtree 1 — Clear commercial requests

**Entry signals:** Explicit hire/implementation verbs; scoped service object; no dominant protected stratum.

```
COMMERCIAL_SUBTREE
  │
  ├─ Dominant protected intent (education/career/DIY/regulatory/nav)? ──YES──► Route to protected subtree
  │
  ├─ Mandatory ambiguity unresolved? ──YES──► ABSTAIN
  │
  ├─ STRONG/EXPLICIT commercial signal + eligible primary intent?
  │     ├─ YES + landing compatible + no opposing protected dominance ──► ACCEPT
  │     └─ NO ──► ABSTAIN (insufficient evidence)
  │
  └─ Clear informational/quote-only without hire path? ──► REJECT or ABSTAIN (prefer ABSTAIN if hire possible)
```

**Examples (training only):**

| Phrase | Terminal |
|--------|----------|
| «заказать внедрение crm под ключ москва» | ACCEPT |
| «нужен подрядчик на интеграцию 1с с сайтом» | ACCEPT |
| «стоимость внедрения erp» | ABSTAIN |

---

## Subtree 2 — Career / education

**Entry signals:** вакансия, резюме, курсы, обучение, с нуля, сертификация, экзамен.

```
CAREER_EDUCATION_SUBTREE
  │
  ├─ Dominant CAREER_EMPLOYMENT or EDUCATIONAL intent? ──YES──► REJECT (service core)
  │
  ├─ Career vs provider both plausible? ──YES──► ABSTAIN
  │     e.g. «программист 1с», «1с специалист»
  │
  ├─ Embedded commercial hire for training delivery by vendor? ──YES──► ABSTAIN (support vs implementation)
  │
  └─ Clear commercial implementation with education modifier only? ──► Route COMMERCIAL_SUBTREE
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «вакансия программист 1с удалённо» | REJECT |
| «курсы 1с бухгалтерия с нуля» | REJECT |
| «программист 1с» | ABSTAIN |

---

## Subtree 3 — DIY / how-to

**Entry signals:** как сделать, как настроить самому, пошагово, инструкция, своими руками, пример кода.

```
DIY_SUBTREE
  │
  ├─ Dominant DIY_HOW_TO or DOCUMENTATION_LOOKUP? ──YES──► REJECT (service core)
  │
  ├─ Provider vs DIY unresolved? ──YES──► ABSTAIN
  │     e.g. «настроить обмен 1с», «исправить ошибку проведения»
  │
  ├─ Explicit hire verb overrides DIY? ──YES──► Route COMMERCIAL_SUBTREE
  │
  └─ Problem + DIY markers only? ──► REJECT or ABSTAIN (conservative: ABSTAIN)
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «как настроить обмен 1с самому пошагово» | REJECT |
| «инструкция печатная форма 1с» | REJECT |
| «настроить обмен 1с» | ABSTAIN |

---

## Subtree 4 — Problem queries

**Entry signals:** не работает, ошибка, не проводится, не подключается, сбой, не синхронизируется.

```
PROBLEM_SUBTREE
  │
  ├─ Apply three-interpretation protocol (paid specialist / DIY / insufficient)
  │
  ├─ Explicit provider/support signal present? ──YES──► Route COMMERCIAL_SUBTREE
  │
  ├─ Explicit DIY/how-to signal? ──YES──► DIY_SUBTREE
  │
  ├─ Problem signal only, no resolution? ──YES──► ABSTAIN (conservative)
  │
  └─ Irrelevant problem to service scope? ──► REJECT
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «1с не работает вызвать специалиста» | ACCEPT |
| «ошибка обмена 1с как исправить» | REJECT |
| «1с не работает» | ABSTAIN |

---

## Subtree 5 — Product / module queries

**Entry signals:** купить, лицензия, модуль, скачать, дистрибутив, сравнить программы, установить.

```
PRODUCT_MODULE_SUBTREE
  │
  ├─ Dominant BUY_PRODUCT_OR_MODULE / DOWNLOAD_RESOURCE? ──YES──► REJECT (service-only scope)
  │
  ├─ Product vs service unresolved? ──YES──► ABSTAIN
  │     e.g. «купить и настроить 1с», «модуль обмена 1с»
  │
  ├─ Configuration/integration of owned product with hire path? ──► Route COMMERCIAL_SUBTREE
  │
  └─ Compare/research software only? ──► REJECT or ABSTAIN (INFORMATIONAL dominance)
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «купить лицензию 1с предприятие» | REJECT |
| «скачать модуль маркировки 1с» | REJECT |
| «купить и внедрить crm под ключ» | ABSTAIN |

---

## Subtree 6 — Short head terms

**Entry signals:** 1–3 tokens; broad category noun; role name; product name without verb.

```
SHORT_HEAD_SUBTREE
  │
  ├─ Severity HIGH/CRITICAL SHORT_HEAD_TERM? ──YES──► ABSTAIN (mandatory if unresolved)
  │
  ├─ Operator seed policy with audit tag? ──YES──► ACCEPT (operator path only)
  │
  ├─ Additional tokens resolve intent? ──YES──► Route appropriate subtree
  │
  └─ Dictionary/frequency match attempted? ──FORBIDDEN──► ABSTAIN
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «1с» | ABSTAIN |
| «сопровождение 1с» | ABSTAIN |
| «заказать сопровождение 1с» | ACCEPT |

---

## Subtree 7 — Regulatory queries

**Entry signals:** закон, ФЗ, постановление, требования, сроки введения, обязательна ли, нормативный документ.

```
REGULATORY_SUBTREE
  │
  ├─ Dominant REGULATORY informational? ──YES──► REJECT
  │
  ├─ Regulatory vs implementation under norm both plausible? ──YES──► ABSTAIN
  │     e.g. «маркировка 1с требования», «внедрение честный знак под ключ»
  │
  ├─ Explicit paid implementation for compliance? ──YES──► Route COMMERCIAL_SUBTREE
  │
  └─ Pure compliance research? ──► REJECT
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «требования маркировки молочной продукции 2025» | REJECT |
| «обязательна ли маркировка для ИП» | REJECT |
| «внедрение маркировки в 1с под ключ» | ACCEPT |

---

## Subtree 8 — Navigational / login

**Entry signals:** официальный сайт, личный кабинет, вход, портал, авторизация, скачать с официального сайта.

```
NAVIGATIONAL_SUBTREE
  │
  ├─ Dominant NAVIGATIONAL or LOGIN_ACCOUNT_ACCESS? ──YES──► REJECT
  │
  ├─ Navigational + embedded commercial verb? ──YES──► ABSTAIN
  │
  └─ Download from vendor site only? ──► REJECT (route PRODUCT if purchase intent)
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «личный кабинет 1с итс вход» | REJECT |
| «официальный сайт 1с скачать» | REJECT |
| «1с итс продлить подписку» | ABSTAIN |

---

## Subtree 9 — Malformed / irrelevant

**Entry signals:** gibberish, empty, wrong language, off-topic, spam, duplicate tokens without meaning.

```
MALFORMED_SUBTREE
  │
  ├─ MALFORMED or IRRELEVANT primary intent clear? ──YES──► REJECT
  │
  ├─ Typo still plausibly domain term? ──YES──► ABSTAIN (route SHORT_HEAD if 1–2 tokens)
  │
  └─ Unclear if malformed vs short head? ──► ABSTAIN
```

**Examples:**

| Phrase | Terminal |
|--------|----------|
| «asdf 1с qqq» | REJECT |
| «бесплатные игры онлайн» | REJECT |
| «1сc» (typo) | ABSTAIN |

---

## Subtree routing index

| Phrase class | Subtree | Typical terminal |
|--------------|---------|------------------|
| Explicit commercial hire | 1 Commercial | ACCEPT |
| Career / education | 2 Career/Education | REJECT / ABSTAIN |
| DIY / how-to | 3 DIY | REJECT / ABSTAIN |
| Problem / error | 4 Problem | ABSTAIN |
| Product / module | 5 Product/Module | REJECT / ABSTAIN |
| Short head | 6 Short head | ABSTAIN |
| Regulatory | 7 Regulatory | REJECT / ABSTAIN |
| Navigational / login | 8 Navigational | REJECT |
| Malformed / irrelevant | 9 Malformed | REJECT / ABSTAIN |

---

## Related documents

- [`../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md)
- [`../guidelines/ORCA-ABSTAIN-STANDARD-v1.md`](../guidelines/ORCA-ABSTAIN-STANDARD-v1.md)
- [`../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md)

---

**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`
