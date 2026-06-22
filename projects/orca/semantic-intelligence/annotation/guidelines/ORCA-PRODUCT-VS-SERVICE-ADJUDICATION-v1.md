# ORCA Product vs Service Adjudication v1

**Adjudication ID:** `orca-product-vs-service-adjudication`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Distinguishes **product/module purchase** intent from **service execution** intent. ORCA PPC gates target **paid service/provider** paths; product-only intent is typically REJECT (`INCOMPATIBLE_PRODUCT_ONLY_INTENT`) or ABSTAIN when the phrase genuinely mixes both.

Aligns with:

- Intent `BUY_PRODUCT_OR_MODULE` vs `REQUEST_*` / `HIRE_SERVICE`
- Signals `TRANSACTION`, `PRODUCT_MODULE` vs `PROVIDER_HIRE`, `IMPLEMENTATION`
- Ambiguity type `PRODUCT_VS_SERVICE` (mandatory ABSTAIN if unresolved)
- Invariant 17: product intent cannot silently map to service intent

---

## Definitions

| Concept | User's dominant next task | Typical verbs (RU) | Primary intent |
|---------|---------------------------|-------------------|----------------|
| **Product** | Acquire license, box, module, subscription SKU | купить, лицензия, подписка, цена продукта | `BUY_PRODUCT_OR_MODULE` |
| **Service** | Hire execution of work on site/remotely | заказать, внедрение, настроить (outsource), подрядчик | `HIRE_SERVICE`, `REQUEST_*` |
| **Bundled** | Purchase includes install OR buy + install ambiguous | купить и установить, поставка с монтажом | **Adjudicate** — often ABSTAIN |

---

## Core rules

1. **Product-dominant → REJECT** for service PPC core unless campaign explicitly includes product lines (out of scope for default ORCA service gate).
2. **Service-dominant → ACCEPT path** when commercial evidence satisfies accept standard.
3. **Genuine bundle ambiguity → ABSTAIN** (`PRODUCT_SERVICE_CONFLICT`); never guess service ACCEPT.
4. **«Купить» + implementation noun** is not automatically service — assess whether user wants SKU or project.

---

## Product indicators

| Signal / pattern | Strength | Example (RU) |
|------------------|----------|--------------|
| `PRODUCT_MODULE` EXPLICIT | EXPLICIT | «купить лицензию 1с erp» |
| `TRANSACTION` + product noun | STRONG | «цена 1с бухгалтерия коробка» |
| Subscription SaaS SKU | STRONG | «подписка битрикс24 тариф» |
| Marketplace download (paid) | STRONG | «купить конфигурацию 1с» |
| Comparison shopping | MEDIUM | «сравнить тарифы crm» |

**Outcome:** `primary_intent: BUY_PRODUCT_OR_MODULE` → `commercial_eligibility.decision: REJECT`, `reason_code: INCOMPATIBLE_PRODUCT_ONLY_INTENT`.

---

## Service indicators

| Signal / pattern | Strength | Example (RU) |
|------------------|----------|--------------|
| `PROVIDER_HIRE` EXPLICIT | EXPLICIT | «заказать внедрение 1с» |
| `IMPLEMENTATION` without buy verb | STRONG | «внедрение crm под ключ» |
| `CONFIGURATION` outsource | STRONG | «настроить 1с специалистом» |
| Subcontractor | EXPLICIT | «подрядчик на монтаж» |

**Outcome:** Commercial `REQUEST_*` or `HIRE_SERVICE` → ACCEPT path per evidence standard.

---

## High-conflict patterns

| Query | Product read | Service read | Required outcome |
|-------|--------------|--------------|------------------|
| «купить и установить 1с» | License + install SKU | Implementation project | **ABSTAIN** |
| «1с цена с установкой» | Bundled product offer | Service quote | **ABSTAIN** |
| «заказать лицензию и внедрение» | Two tasks | Two tasks | **ABSTAIN** or split task dominance |
| «купить 1с» | Product | Weak service | **REJECT** product-dominant |
| «внедрение 1с стоимость» | Quote on service | Service | ACCEPT path if hire implied |
| «монтаж вентиляции цена» | Could be product+install | Service quote | ABSTAIN if DIY/provider also open |

---

## Adjudication procedure

### Step 1 — Token scan

List `TRANSACTION`, `PRODUCT_MODULE`, `PROVIDER_HIRE`, `IMPLEMENTATION`, `CONFIGURATION` with strength.

### Step 2 — Task question

Ask: *What does the user want to **own** vs what do they want **done for them**?*

- Own = product path
- Done = service path

### Step 3 — Bundle detection

If phrase contains **both**:

- purchase verb (`купить`, `приобрести`, `лицензия`)
- **and** execution verb (`установить`, `внедрить`, `монтаж`, `настроить`)

→ Flag `PRODUCT_VS_SERVICE`. If dominance not provable → ABSTAIN.

### Step 4 — Campaign scope check

If service mapping would attach a SKU-only intent to a service landing → `LANDING_MISMATCH` REJECT.

### Step 5 — Record

- `ambiguity.types[]` includes `PRODUCT_VS_SERVICE` when applicable
- `ambiguity.unresolved_questions` for ABSTAIN — e.g. «Покупка коробки или заказ проекта внедрения?»

---

## Dominance heuristics (non-binding aids)

| Cue | Lean |
|-----|------|
| «лицензия», «коробка», «подписка», «тариф» | Product |
| «под ключ», «подрядчик», «на объекте» | Service |
| «внедрение» without «купить» | Service |
| «скачать» / «демо» | Neither — download stratum |
| Brand + single head | ABSTAIN — short head rules |

Heuristics **do not override** mandatory ABSTAIN when conflict unresolved.

---

## Examples table (RU)

| Query | Decision | reason_code | Rationale summary |
|-------|----------|-------------|-------------------|
| «купить 1с бухгалтерию» | REJECT | `INCOMPATIBLE_PRODUCT_ONLY_INTENT` | Product SKU |
| «заказать внедрение 1с erp» | ACCEPT | `EXPLICIT_PROVIDER_REQUEST` | Service hire |
| «купить и установить crm» | ABSTAIN | `PRODUCT_SERVICE_CONFLICT` | Bundle ambiguity |
| «стоимость лицензии 1с с внедрением» | ABSTAIN | `PRODUCT_SERVICE_CONFLICT` | Dual task |
| «настроить купленную 1с» | ABSTAIN | `PROVIDER_DIY_CONFLICT` / product | Post-purchase config — DIY vs outsource |
| «интеграция 1с с сайтом» | ACCEPT path | `EXPLICIT_SERVICE_REQUEST` | Service task — no product verb |

---

## Anti-patterns

| Anti-pattern | Correct handling |
|--------------|------------------|
| Map all «1с» queries to implementation service | Head term ABSTAIN |
| ACCEPT «купить 1с» as implementation | REJECT product |
| REJECT «внедрение» as product because software named | Service path |
| Collapse bundle into product for convenience | ABSTAIN |
| Silent `service_id` assignment on product intent | Invariant 9 — CANDIDATE_ONLY pre-ACCEPT |

---

## Related documents

- [`ORCA-SHORT-HEAD-TERM-ADJUDICATION-v1.md`](ORCA-SHORT-HEAD-TERM-ADJUDICATION-v1.md)
- [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
- [`../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md)
