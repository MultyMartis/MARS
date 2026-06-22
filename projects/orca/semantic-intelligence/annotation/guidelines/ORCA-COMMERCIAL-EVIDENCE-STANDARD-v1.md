# ORCA Commercial Evidence Standard v1

**Standard ID:** `orca-commercial-evidence-standard`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Defines how annotators and adjudicators evaluate **commercial evidence** when assigning `commercial_eligibility.decision` (ACCEPT / REJECT / ABSTAIN). This standard binds to P0-B:

- 27 primary intents ([`ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](../../taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md))
- 31 semantic signals with strength scale ([`ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md`](../../taxonomy/ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md))
- Record invariants 1–2 ([`ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md))

**Commercial evidence** is observable phrase-level support for a paid provider/service engagement. It is **not** the same as `primary_intent` and **not** sufficient alone for ACCEPT.

---

## Core rule: evidence is not an auto-trigger

> **No lexical marker, domain term, or signal strength alone may automatically produce ACCEPT.**

Evidence must be:

1. **Typed** — mapped to a signal_id from the signal taxonomy.
2. **Strength-rated** — NONE / WEAK / MEDIUM / STRONG / EXPLICIT.
3. **Context-bound** — evaluated in the full phrase, not as isolated token lookup.
4. **Aggregated** — combined with opposing evidence, protected strata, and ambiguity policy.

A phrase containing «услуга» or «заказать» without a resolvable service object and without suppression of protected conflicts does **not** auto-qualify for ACCEPT.

---

## Evidence strength model

| Strength | Role in eligibility |
|----------|----------------------|
| `NONE` | No evidence; do not cite as supporting |
| `WEAK` | Topical adjacency only; **cannot** support ACCEPT alone |
| `MEDIUM` | Stable collocation; may support intent, **insufficient alone** for ACCEPT |
| `STRONG` | Multiple coherent markers or durable phrase pattern; may support ACCEPT **with** task object |
| `EXPLICIT` | Direct hire/transaction/implementation verb in task context; primary ACCEPT path |

**Invariant 1:** Topic match alone cannot support ACCEPT.  
**Invariant 2:** ACCEPT requires at least one STRONG or EXPLICIT commercial signal path, or `VALIDATED_OPERATOR_SEED`.

---

## Strong commercial evidence

Strong evidence indicates the user is likely seeking **paid external execution** of a scoped task, not merely browsing the domain.

### Qualifying patterns

| Pattern | Typical signals | Example (RU) |
|---------|-----------------|--------------|
| Explicit provider hire | `PROVIDER_HIRE` EXPLICIT + service object | «заказать внедрение crm под ключ» |
| Explicit implementation ask | `IMPLEMENTATION` EXPLICIT / STRONG + provider path | «внедрение 1с erp на предприятии» |
| Explicit configuration/modification | `CONFIGURATION` / `MODIFICATION` EXPLICIT + outsource context | «доработать отчёт в 1с под требования» |
| Explicit support/recovery | `SUPPORT` / `RECOVERY` EXPLICIT + engagement verb | «заказать восстановление базы 1с» |
| Strong problem + provider path | `PROBLEM` STRONG + `PROVIDER_HIRE` / `SUPPORT` STRONG, DIY absent | «1с не проводит документ срочно вызвать специалиста» |
| Geography + service intent | `GEOGRAPHY` STRONG + commercial task signals | «монтаж вентиляции москва под ключ» |
| Validated operator seed | `VALIDATED_OPERATOR_SEED` with audit trail | Pre-approved phrase list entry |

### Strong lexical families (non-exhaustive)

When **combined with a task object** and **without dominant protected conflict**:

| Family | Example tokens (RU) | Typical signal_id |
|--------|---------------------|-------------------|
| Hire / outsource | заказать, нанять, вызвать, подрядчик, бригада, мастер, специалист, аутсорс | `PROVIDER_HIRE` |
| Turnkey / scope | под ключ, на объекте, у заказчика | `PROVIDER_HIRE`, `IMPLEMENTATION` |
| Service noun | услуга, услуги, сервис (в коммерческом контексте) | `PROVIDER_HIRE` (MEDIUM–STRONG only with object) |
| Implementation | внедрение, развернуть, запуск, инсталляция | `IMPLEMENTATION` |
| Configuration | настроить, конфигурация, параметризация | `CONFIGURATION` |
| Modification | доработать, кастомизация, изменить логику | `MODIFICATION` |
| Integration | интеграция, обмен, синхронизация, api | `INTEGRATION` |
| Support / recovery | техподдержка, сопровождение, восстановить, не работает + срочно | `SUPPORT`, `RECOVERY` |
| Audit / diagnostic (paid) | аудит, обследование, диагностика (с контекстом заказа) | `AUDIT_DIAGNOSTIC` |
| Migration / maintenance | миграция, перенос данных, обслуживание, ТО | `MIGRATION`, `MAINTENANCE` |
| Quote with hire path | расчёт стоимости + заказать / КП + внедрение | `QUOTE_PRICE` + commercial cluster |

---

## Weak commercial evidence

Weak evidence **must not** be upgraded to ACCEPT without additional STRONG/EXPLICIT markers.

| Pattern | Why weak | Typical outcome |
|---------|----------|-----------------|
| Domain noun only | Topic match | ABSTAIN or REJECT (if protected) |
| «услуга» without object or verb | Generic commercial adjacency | ABSTAIN |
| «стоимость», «цена», «сколько стоит» alone | `QUOTE_PRICE` without hire path | INFORMATIONAL → usually not ACCEPT |
| «консультация» without provider path | May be informational | ABSTAIN or REJECT |
| Brand + category head | SHORT_HEAD_TERM risk | ABSTAIN |
| «купить» without product clarity | PRODUCT_VS_SERVICE conflict | ABSTAIN |
| Problem token alone | `PROBLEM` without provider/DIY resolution | ABSTAIN (see problem adjudication) |
| Geo token alone | `GEOGRAPHY` without task | WEAK; not ACCEPT |

### Weak-only examples (RU)

| Query | Evidence assessment | Eligibility guidance |
|-------|---------------------|----------------------|
| «crm» | WEAK topic only | ABSTAIN — `SHORT_HEAD_TERM` |
| «услуги 1с» | MEDIUM service noun, no task | ABSTAIN — insufficient |
| «сколько стоит внедрение crm» | QUOTE + topic; no hire verb | REJECT or ABSTAIN per INFORMATIONAL dominance |
| «холодильник» | WEAK topic | REJECT / ABSTAIN — no commercial path |
| «1с» | WEAK head term | ABSTAIN — `SHORT_AMBIGUOUS_PHRASE` |

---

## Words listed in operational lexicon (reference)

The following Russian tokens are **frequent commercial markers**. Presence in a phrase triggers **signal detection**, not **decision assignment**:

| Token / pattern | Default signal | Auto-ACCEPT? |
|-----------------|----------------|--------------|
| услуга, услуги | `PROVIDER_HIRE` WEAK–MEDIUM | **No** |
| заказать | `PROVIDER_HIRE` EXPLICIT (in task context) | **No** — requires object + no protected conflict |
| нанять, вызвать | `PROVIDER_HIRE` EXPLICIT | **No** |
| подрядчик, мастер, специалист | `PROVIDER_HIRE` STRONG | **No** |
| под ключ | `PROVIDER_HIRE` / `IMPLEMENTATION` STRONG | **No** |
| внедрение | `IMPLEMENTATION` MEDIUM–EXPLICIT | **No** |
| настроить, доработать | `CONFIGURATION` / `MODIFICATION` | **No** |
| купить, лицензия | `TRANSACTION` / `PRODUCT_MODULE` | **No** — product path |
| скачать, бесплатно | `DOWNLOAD` / `FREE` | **No** — protected non-commercial |
| вакансия, работа | `CAREER_SEEKER` | **No** — REJECT stratum |
| курс, обучение | `EDUCATIONAL` | **No** — REJECT stratum |
| как сделать, самому | `DIY` | **No** — REJECT / conflict |
| гост, санпин | `REGULATORY` | **No** — REJECT unless implementation ask |
| официальный сайт | `NAVIGATIONAL` | **No** — REJECT stratum |

---

## Opposing evidence (mandatory consideration)

Before ACCEPT, assessors must scan for opposing signals:

| Opposing signal | Effect |
|-----------------|--------|
| `DIY` EXPLICIT | Blocks ACCEPT unless provider path dominates |
| `EDUCATIONAL` EXPLICIT | REJECT or protected conflict |
| `CAREER_SEEKER` / `EMPLOYEE_HIRING` | REJECT or `CAREER_VS_PROVIDER` ABSTAIN |
| `DOWNLOAD` + `FREE` | REJECT — `FREE_DOWNLOAD_INTENT` |
| `NAVIGATIONAL` / `LOGIN` dominant | REJECT |
| `REGULATORY` without implementation | REJECT |
| `PRODUCT_MODULE` vs service verbs | `PRODUCT_VS_SERVICE` ABSTAIN |

Record opposing evidence in `commercial_eligibility.opposing_evidence`.

---

## Recording requirements

For any eligibility decision citing commercial evidence:

| Field | Requirement |
|-------|-------------|
| `signals[]` | At least one commercial signal with strength and `evidence_span` |
| `commercial_eligibility.supporting_evidence` | Human-readable list tied to spans |
| `commercial_eligibility.opposing_evidence` | Required when any opposing signal ≥ MEDIUM |
| `commercial_eligibility.reason_code` | ACCEPT family code matching evidence type |

---

## Annotator checklist

1. Identify all commercial and opposing signals with strength.
2. Confirm evidence spans are **substrings of the actual phrase** — no rewrite.
3. Ask: «Is there a concrete task object the user wants executed externally?»
4. Ask: «Does any protected stratum dominate?»
5. Ask: «Would ACCEPT require guessing DIY vs provider or product vs service?»
6. If yes to guessing → ABSTAIN, not weak ACCEPT.
7. Document evidence in `phrase_explanation` per phrase-specific rationale standard.

---

## Related documents

- [`ORCA-ACCEPT-STANDARD-v1.md`](ORCA-ACCEPT-STANDARD-v1.md)
- [`ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md`](ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md)
- [`ORCA-PROBLEM-QUERY-ADJUDICATION-v1.md`](ORCA-PROBLEM-QUERY-ADJUDICATION-v1.md)
- [`../../taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-COMMERCIAL-ELIGIBILITY-TAXONOMY-v1.md)
