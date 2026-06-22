# ORCA Semantic Annotation Guideline v1

**Guideline ID:** `orca-semantic-annotation-guideline`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-annotation-guideline-v1.json`](orca-semantic-annotation-guideline-v1.json)

---

## 1. Purpose

This handbook defines the **human annotation and adjudication process** for ORCA Semantic Intelligence v1 search-query phrases. It is the operational binding between:

- Approved P0-B taxonomy and semantic record schema
- Operator decisions D1–D7 and approvals A1–A7, B1–B7
- Future benchmark annotation (P0-D), baseline evaluation (P0-F), and Semantic Core production (P0-H)

**Audience:** PPC specialist, domain expert, trained annotator, adjudicator, structured LLM assistant (non-final), validator designer.

**Scope:** How to read a phrase, assign intent and signals, assess ambiguity, decide commercial eligibility (`ACCEPT` / `REJECT` / `ABSTAIN`), record risk and provenance.

**Out of scope:** Benchmark gold labels, classifier implementation, campaign export, Corvonero corpus relabelling, runtime validation.

**Training vs benchmark:** Examples in `examples/` are **training illustrations only** — not gold benchmark authority.

---

## 2. Annotation authority

| Rank | Source | Role |
|------|--------|------|
| 1 | Operator policy and overrides | Final authority on thresholds, seeds, releases |
| 2 | This guideline + sub-standards in `guidelines/` | Mandatory procedure |
| 3 | P0-B taxonomy and record schema | Controlled vocabulary and shape |
| 4 | Approved ADR v1 and admission policy | Architectural constraints |
| 5 | Structured LLM assistant output | Evidence and alternatives only — **not** final decision |

**Terminal outcomes:** Only `ACCEPT`, `REJECT`, or `ABSTAIN` at the commercial eligibility boundary. No subtree or shortcut may terminate in service mapping, cluster assignment, or campaign grouping.

**Forbidden annotation truth:** Old Corvonero labels, `ACTIVE`/`HOLD`/`EXCLUDE` statuses, prior service mappings, model explanations from defective pipelines.

---

## 3. Unit of annotation

**Unit:** One **raw query phrase** (`raw_query`) as received from corpus intake — typically a Wordstat or search-console row, normalized but not reinterpreted.

| Principle | Rule |
|-----------|------|
| Phrase integrity | Annotate the full phrase; do not split into artificial sub-phrases unless corpus policy requires |
| One record per phrase | One semantic record per `query_id` per annotation pass |
| Immutability | `raw_query` is immutable; corrections go to `normalized_query` with audit |
| No cluster inheritance | Cluster or group membership does **not** propagate labels to member phrases |
| No export-time decisions | Eligibility must be decided before export; export does not re-adjudicate |

---

## 4. Required reading order

Before annotating, read in order:

1. This guideline (full handbook)
2. [`ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md`](ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md)
3. [`ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md`](ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md)
4. [`ORCA-PROBLEM-QUERY-ADJUDICATION-v1.md`](ORCA-PROBLEM-QUERY-ADJUDICATION-v1.md)
5. [`ORCA-PRODUCT-VS-SERVICE-ADJUDICATION-v1.md`](ORCA-PRODUCT-VS-SERVICE-ADJUDICATION-v1.md)
6. [`ORCA-SHORT-HEAD-TERM-ADJUDICATION-v1.md`](ORCA-SHORT-HEAD-TERM-ADJUDICATION-v1.md)
7. [`ORCA-ACCEPT-STANDARD-v1.md`](ORCA-ACCEPT-STANDARD-v1.md)
8. [`ORCA-REJECT-STANDARD-v1.md`](ORCA-REJECT-STANDARD-v1.md)
9. [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md)
10. [`ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md)
11. [`../decision-trees/ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md`](../decision-trees/ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md)
12. [`../examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md`](../examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md)
13. [`../examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md`](../examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md)
14. P0-B taxonomies under `../../taxonomy/` and record schema under `../../schemas/`

---

## 5. Literal interpretation

**Rule:** State what the phrase **literally says** before any commercial inference.

**Write** `literal_interpretation` as a neutral paraphrase in the phrase language.

**Do not add:**

- Imagined business context not in the phrase
- Operator service catalogue context as if it were user intent
- A desired paid outcome the user did not express
- Domain expertise that changes the literal reading

**Example:**

| Phrase | Correct literal reading | Wrong reading |
|--------|-------------------------|---------------|
| «1с не работает» | Пользователь сообщает, что 1С не функционирует | Пользователь ищет подрядчика по сопровождению 1С |
| «программист 1с» | Упоминание роли/профессии в контексте 1С | Заказ услуг программиста 1С |

Literal interpretation is **Step 1** of the mandatory annotation order (Section 19).

---

## 6. Likely user goal

**Field:** `likely_user_goal` — from [`ORCA-USER-GOAL-TAXONOMY-v1.md`](../../taxonomy/ORCA-USER-GOAL-TAXONOMY-v1.md).

**Question:** What is the user **most likely trying to do next**?

| Goal class | Examples (RU, B2B IT) |
|------------|----------------------|
| Hire external provider | заказать внедрение ERP, найти подрядчика на интеграцию |
| Buy product/module | купить лицензию 1С, скачать модуль обмена |
| Configure / implement | настроить CRM, внедрить складской учёт |
| Learn / train | курсы 1С с нуля, обучение администратору |
| DIY / self-serve | как настроить обмен самому, инструкция по отчёту |
| Solve problem | ошибка проведения документа, не синхронизируется касса |
| Find documentation | документация API Битрикс, руководство пользователя |
| Download resource | скачать дистрибутив, шаблон печатной формы |
| Find employment | вакансия программист 1С, резюме 1С |
| Hire employee (business) | найти сотрудника 1С в штат |
| Regulatory compliance | требования маркировки, сроки ФЗ-54 |
| Navigate / login | личный кабинет 1С:ИТС, официальный сайт |
| Unknown | insufficient evidence |

**Distinction:** `likely_user_goal` is **not** `primary_intent` and **not** commercial eligibility.

---

## 7. Primary intent

**Field:** `primary_intent` — one of **27 intents** from [`ORCA-PRIMARY-INTENT-TAXONOMY-v1.md`](../../taxonomy/ORCA-PRIMARY-INTENT-TAXONOMY-v1.md).

**Rule:** Assign the intent that best describes the **dominant next task**, not topical category.

| Critical boundary | Meaning |
|-------------------|---------|
| Intent ≠ eligibility | `HIRE_SERVICE` may still be ABSTAIN; `PROBLEM_UNRESOLVED` may be ACCEPT with strong provider evidence |
| Topic ≠ intent | «1с» is topical, not an intent |
| Protected classes | `EDUCATIONAL`, `CAREER_EMPLOYMENT`, `DIY_HOW_TO`, `REGULATORY`, `NAVIGATIONAL` require conservative handling |

Assign primary intent in **Step 4** — **before** commercial eligibility (**Step 8**).

---

## 8. Secondary intent

**Field:** `secondary_intents[]` — competing intent_ids with plausible support.

**When required:**

- Any ambiguity type `INTENT`, `MULTIPLE`, or protected conflict
- ABSTAIN records — at least one competing intent documented
- Borderline ACCEPT/REJECT — document the rejected alternative

**Rule:** Secondary intent documents **competition**, not a wish list. List only interpretations that a reasonable Russian-speaking B2B searcher might hold.

---

## 9. Signal extraction

**Field:** `signals[]` — typed evidence per [`ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md`](../../taxonomy/ORCA-SEMANTIC-SIGNAL-TAXONOMY-v1.md).

**Step 3** of annotation order:

1. Extract **positive** commercial and task signals separately from **negative / suppressing** signals
2. Map each to `signal_id` and `strength` (NONE / WEAK / MEDIUM / STRONG / EXPLICIT)
3. Include `evidence_span` — substring from `raw_query`
4. Document opposing signals even when decision seems clear

**Core distinctions (B4):**

| Signal | Is NOT |
|--------|--------|
| Provider-hire signal | Mere service noun or software name |
| Problem signal | Automatic provider-hire signal |
| Topic relevance | Commercial intent |
| Service candidate mapping | Service ownership or eligibility |

See [`ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md`](ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md) for ACCEPT evidence paths.

---

## 10. Ambiguity assessment

**Field:** `ambiguity` object — types, severity, competing interpretations, unresolved questions.

**Types:** From [`ORCA-AMBIGUITY-TAXONOMY-v1.md`](../../taxonomy/ORCA-AMBIGUITY-TAXONOMY-v1.md) — 13 types including `PRODUCT_VS_SERVICE`, `PROVIDER_VS_DIY`, `CAREER_VS_PROVIDER`, `SHORT_HEAD_TERM`, `MULTIPLE`.

**Mandatory ABSTAIN when unresolved:**

- `PROVIDER_VS_DIY`
- `PRODUCT_VS_SERVICE`
- `CAREER_VS_PROVIDER`
- `SUPPORT_VS_INFORMATION`
- `SHORT_HEAD_TERM` (severity HIGH or CRITICAL)
- `MULTIPLE`

**Step 5** — list plausible competing interpretations before provider-hire assessment.

---

## 11. Commercial eligibility

**Field:** `commercial_eligibility.decision` — **ACCEPT**, **REJECT**, or **ABSTAIN** only.

**Assign only in Step 8** after literal reading, goals, intents, signals, ambiguity, provider-hire likelihood, and landing compatibility.

| Decision | When |
|----------|------|
| **ACCEPT** | All seven ACCEPT requirements met — see [`ORCA-ACCEPT-STANDARD-v1.md`](ORCA-ACCEPT-STANDARD-v1.md) |
| **REJECT** | Clear incompatible primary intent, unsupported service, malformed/irrelevant, landing mismatch, dominant protected non-commercial — see [`ORCA-REJECT-STANDARD-v1.md`](ORCA-REJECT-STANDARD-v1.md) |
| **ABSTAIN** | Mandatory ambiguity unresolved, insufficient evidence, assessor disagreement, conservative mode — see [`ORCA-ABSTAIN-STANDARD-v1.md`](ORCA-ABSTAIN-STANDARD-v1.md) |

**D4 operator rule:** ABSTAIN is **mandatory** when commercial intent is not sufficiently supported by evidence.

**Invariant:** No lexical marker alone may auto-produce ACCEPT.

---

## 12. Risk assessment

**Field:** `risk` object — per [`ORCA-SEMANTIC-RISK-TAXONOMY-v1.md`](../../taxonomy/ORCA-SEMANTIC-RISK-TAXONOMY-v1.md).

**Assess in Step 9:**

| Dimension | Annotator question |
|-----------|-------------------|
| `OVER_ADMISSION` | Would ACCEPT mislead spend toward non-buyers? |
| `NEGATIVE_OVERBLOCKING` | Would REJECT hide real demand? |
| `PROTECTED_STRATUM_LEAK` | Could career/education/DIY traffic enter core? |
| `LANDING_MISMATCH` | Can any honest landing satisfy the phrase? |
| `AMBIGUITY_UNRESOLVED` | Are mandatory ambiguity types still open? |

Set `reviewer_required: true` per risk taxonomy and ACCEPT/REJECT/ABSTAIN standards.

**Authorized production thresholds (D3):** commercial precision ≥ 0.95; protected-strata FPR ≤ 0.01 — apply at evaluation gate, not as per-phrase guess.

---

## 13. Service candidate handling

**Field:** `service_candidate` — `mapping_status` only `NOT_STARTED` or `CANDIDATE_ONLY` **until** eligibility is approved for core path.

**Rules:**

- Do **not** assign final service ownership during initial annotation
- Do **not** use operator scope catalogue as proof of user demand
- Map service candidate **after** ACCEPT (or operator-directed pilot), not as a substitute for eligibility
- Product-only phrases — no service mapping without product-vs-service resolution

Eligibility first; mapping second.

---

## 14. Reviewer status

**Field:** `review.workflow_status` — from [`ORCA-SEMANTIC-REVIEW-STATUS-v1.md`](../../taxonomy/ORCA-SEMANTIC-REVIEW-STATUS-v1.md).

| Status | Typical trigger |
|--------|-----------------|
| `DRAFT` | First-pass annotation incomplete |
| `ABSTAIN_PENDING_REVIEW` | ABSTAIN with open questions |
| `PENDING_SECOND_ANNOTATION` | Benchmark double-annotation queue |
| `DISAGREEMENT_FLAGGED` | Annotators differ |
| `HUMAN_REVIEWED` | Adjudicator resolved |
| `ADJUDICATED` | Formal adjudication complete |
| `APPROVED_FOR_CORE` | Eligible for core promotion path |
| `REJECTED_FROM_CORE` | Final negative |

`reviewer_required` on `commercial_eligibility` must align with risk and decision standards.

---

## 15. Decision trace

**Field:** `audit` + decision trace per [`ORCA-SEMANTIC-DECISION-TRACE-v1.md`](../../schemas/ORCA-SEMANTIC-DECISION-TRACE-v1.md).

**Step 10 — record:**

1. Annotation steps completed (1–10 checklist)
2. Decision tree subtree path used
3. Strongest supporting and opposing evidence spans
4. Alternatives considered and rejected or left unresolved
5. `reason_code` from commercial-eligibility taxonomy
6. Annotator role and timestamp

Decision trace must be **phrase-specific** — see rationale standard. Generic rationales fail quality gates.

---

## 16. Evidence requirements

Every completed record must satisfy:

| Requirement | Source |
|-------------|--------|
| Schema-valid shape | `orca-semantic-record-schema-v1` |
| All required top-level fields | Record schema § Required fields |
| `literal_interpretation` non-empty | Step 1 |
| `signals[]` with typed strength | Step 3; invariant 1–2 for ACCEPT |
| `reason_code` on eligibility | Invariant 5 |
| `unresolved_questions` min 1 when ABSTAIN | Schema + invariant 4 |
| `versioning` object complete | Section 20 |
| Phrase-specific rationale | Phrase-specific rationale standard |
| No skipped annotation steps | Section 19 |

**ACCEPT evidence minimum:** At least one STRONG or EXPLICIT commercial signal path, or validated `OPERATOR_SEED` with audit tag.

**REJECT evidence minimum:** Dominant incompatible intent or protected stratum with documented spans.

**ABSTAIN evidence minimum:** Named unresolved question, competing interpretations, missing evidence class.

---

## 17. Prohibited reasoning

Annotators, adjudicators, and LLM assistants **must not**:

1. Treat service-term presence as automatic ACCEPT
2. Treat topic match as commercial intent
3. Treat error/problem as provider-hire intent
4. Treat high frequency as commercial proof
5. Inherit group/cluster labels as phrase truth
6. Let one keyword override full phrase meaning
7. Use long inline negatives to rescue bad phrases
8. Force artificial demand from operator scope
9. Copy-paste generic rationales
10. Apply cluster-level decisions to every phrase
11. Treat model confidence as evidence
12. Let LLM validate its own output as final
13. Silently convert product intent to service intent
14. Treat career intent as customer demand
15. Suppress ABSTAIN to inflate automation rate
16. Make semantic decisions during export

Full catalogue: [`../examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md`](../examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md).

---

## 18. Escalation rules

| Condition | Route |
|-----------|-------|
| Mandatory ambiguity unresolved after annotator pass | ABSTAIN → human review queue |
| Annotator disagreement on eligibility or intent | Adjudicator per disagreement policy |
| Protected stratum vs commercial tie | ABSTAIN; adjudicator with domain expert input |
| `SHORT_HEAD_TERM` CRITICAL | Operator or senior adjudicator |
| Risk `PROTECTED_STRATUM_LEAK` elevated | Mandatory reviewer |
| Operator seed candidate | Operator approval before seed ACCEPT |
| Policy gap not covered by trees | Operator escalation — do not guess ACCEPT |

Domain expert **clarifies terminology**; does **not** alone determine commercial eligibility.

---

## 19. Operator override

Operator may override `commercial_eligibility.decision` with:

- `audit.override_type` = `OPERATOR_OVERRIDE`
- Preserved `audit.prior_decision` (invariant 12)
- Documented business justification
- Explicit `OPERATOR_SEED` tag when seeding broad head terms

**Operator-seed ACCEPT** must not pretend to be Wordstat-proven commercial intent.

Overrides do not bypass schema, prohibited reasoning, or benchmark blind-split integrity.

---

## 20. Versioning

**Field:** `versioning` object — mandatory on every record.

| Key | Example value |
|-----|---------------|
| `taxonomy_version` | `v1` |
| `schema_version` | `v1` |
| `guideline_version` | `orca-semantic-annotation-guideline-v1` |
| `rule_pack_version` | `null` until rules baseline |
| `model_version` | `null` for human-only |
| `prompt_version` | `null` for human-only |

**Guideline changes:** Semver bump on material procedure change; operator approval required before benchmark relabelling.

**Record `record_version`:** Per-phrase annotation revision; increment on adjudication change.

---

## Mandatory 10-step annotation order

**No step may be skipped.** Steps 1–7 precede eligibility; Step 8 assigns ACCEPT/REJECT/ABSTAIN only.

### Step 1 — Read literally

Write `literal_interpretation`. Do not add imagined context, operator service context, or unstated paid outcomes.

### Step 2 — Identify likely next user action

Assign `likely_user_goal`. Choose from: hire, buy, configure, learn, perform independently, solve problem, find documentation, download, find employment, hire employee, comply with regulation, navigate, log in, unknown.

### Step 3 — Extract signals

Record positive and negative evidence separately in `signals[]` with strength and `evidence_span`.

### Step 4 — Assign primary and secondary intent

Set `primary_intent` and `secondary_intents[]`. **Do not assign commercial eligibility yet.**

### Step 5 — Assess competing interpretations

Populate `ambiguity.competing_interpretations` and ambiguity types for plausible alternatives.

### Step 6 — Assess provider-hire likelihood

Evaluate whether paid external execution is likely. **Not inferred from:** service noun alone, software name alone, error alone, thematic relevance alone.

### Step 7 — Check landing compatibility

> Could an honest service landing page directly satisfy this query without changing its meaning?

Document mismatch in risk if REJECT or ABSTAIN path.

### Step 8 — Assign eligibility

Set `commercial_eligibility.decision` to **ACCEPT**, **REJECT**, or **ABSTAIN** with `reason_code`.

### Step 9 — Assess risk and review requirement

Complete `risk` object; set `reviewer_required` and `review.workflow_status`.

### Step 10 — Record decision trace

Complete audit, decision trace, phrase-specific rationale, and versioning.

---

## Related documents

| Document | Path |
|----------|------|
| Annotation locus README | [`../README.md`](../README.md) |
| Decision trees | [`../decision-trees/`](../decision-trees/) |
| Example library | [`../examples/`](../examples/) |
| Record invariants | [`../../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md`](../../contracts/ORCA-SEMANTIC-RECORD-INVARIANTS-v1.md) |
| Admission policy | [`../../architecture/semantic-intelligence/ORCA-SEMANTIC-ADMISSION-POLICY-v1.md`](../../architecture/semantic-intelligence/ORCA-SEMANTIC-ADMISSION-POLICY-v1.md) |

---

**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Next gate:** Operator approval of P0-C → P0-D Benchmark Charter
