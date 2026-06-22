# ORCA Semantic Annotation Anti-Patterns v1

**Library ID:** `orca-semantic-annotation-anti-patterns`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Catalogue of **prohibited annotation logic** for ORCA Semantic Intelligence v1. Each anti-pattern documents wrong reasoning, a B2B IT/PPC example, damage, correct action, and a detection rule for future QA validators.

**Binding:** Referenced from [`ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md) Section 17.

---

## Anti-pattern 1 — Service-term presence = ACCEPT

| Field | Content |
|-------|---------|
| **Wrong logic** | Any occurrence of «услуга», «сопровождение», «внедрение», «доработка» automatically yields ACCEPT. |
| **Example** | «сопровождение 1с» → ACCEPT because «сопровождение» is a service noun in operator catalogue. |
| **Damage** | Broad head terms enter core without hire evidence; budget waste on informational and competitor traffic. |
| **Correct action** | Apply short-head and commercial-evidence standards; ABSTAIN unless STRONG/EXPLICIT path or operator seed. |
| **Detection rule** | ACCEPT with only WEAK/MEDIUM topical signals and ≤3 tokens; no hire/scope verb in `evidence_span`. |

---

## Anti-pattern 2 — Topic match = commercial intent

| Field | Content |
|-------|---------|
| **Wrong logic** | Phrase mentions 1С/CRM/ERP domain → commercial intent assumed. |
| **Example** | «1с» → ACCEPT because operator sells 1С services. |
| **Damage** | Violates invariant 1; inflates core with navigational, educational, and random topical queries. |
| **Correct action** | Separate `primary_intent` from eligibility; SHORT_HEAD → ABSTAIN. |
| **Detection rule** | ACCEPT where `signals[]` contain only TOPIC/DOMAIN markers without task or hire signals. |

---

## Anti-pattern 3 — Error/problem = provider intent

| Field | Content |
|-------|---------|
| **Wrong logic** | Any error or malfunction phrase implies user wants paid specialist. |
| **Example** | «1с не работает» → ACCEPT because problems drive service demand. |
| **Damage** | DIY and self-help traffic misclassified; false precision on problem stratum. |
| **Correct action** | Three-interpretation protocol; ABSTAIN in conservative mode without explicit provider signal. |
| **Detection rule** | ACCEPT on PROBLEM_UNRESOLVED with no PROVIDER_HIRE/SUPPORT signal STRONG+. |

---

## Anti-pattern 4 — High frequency = commercial

| Field | Content |
|-------|---------|
| **Wrong logic** | High Wordstat frequency proves commercial value → ACCEPT. |
| **Damage** | Popular educational, career, and navigational phrases over-admitted. |
| **Example** | «программист 1с» (high volume) → ACCEPT for spend scaling. |
| **Correct action** | Frequency may inform risk only; never overrides intent and evidence rules. |
| **Detection rule** | ACCEPT justified primarily by `frequency_evidence` without phrase-level commercial signals. |

---

## Anti-pattern 5 — Group membership inherited as label

| Field | Content |
|-------|---------|
| **Wrong logic** | Sister phrase in cluster was ACCEPT → this phrase inherits ACCEPT. |
| **Example** | Cluster «внедрение crm» ACCEPT → «crm» alone ACCEPT. |
| **Damage** | Head-term leakage; cluster-level false positives propagate. |
| **Correct action** | Annotate each `raw_query` independently; cluster is metadata only. |
| **Detection rule** | Identical eligibility across all cluster members without per-phrase rationale spans. |

---

## Anti-pattern 6 — One keyword modifier overrides full phrase meaning

| Field | Content |
|-------|---------|
| **Wrong logic** | Single word «заказать» or «цена» overrides dominant educational/career reading. |
| **Example** | «курсы 1с цена» → ACCEPT because «цена» appears. |
| **Damage** | Protected strata leak into commercial core. |
| **Correct action** | Dominant intent from full phrase; REJECT when EDUCATIONAL dominates. |
| **Detection rule** | ACCEPT with protected primary intent and only price token as commercial evidence. |

---

## Anti-pattern 7 — Long inline negatives rescue a bad phrase

| Field | Content |
|-------|---------|
| **Wrong logic** | Append «бесплатно», «вакансия», «скачать» as campaign negative to keep ACCEPT on trunk phrase. |
| **Example** | ACCEPT «1с» and minus «вакансия», «курсы», «скачать» instead of ABSTAIN/REJECT trunk. |
| **Damage** | Export-time patching hides annotation failure; unstable negatives. |
| **Correct action** | Decide eligibility on full phrase first; negatives are downstream, not rescue logic. |
| **Detection rule** | ACCEPT on high-ambiguity phrase with disproportionate inline negative list in export notes. |

---

## Anti-pattern 8 — Operator scope forces artificial demand

| Field | Content |
|-------|---------|
| **Wrong logic** | Service exists in operator catalogue → phrase must be ACCEPT to represent scope. |
| **Example** | «платёжный календарь 1с» → ACCEPT because CR2-SVC-014 exists in scope manifest. |
| **Damage** | Scope catalog becomes demand proof; false core entries. |
| **Correct action** | Scope informs landing fit check only after user demand is evidenced. |
| **Detection rule** | Rationale cites service_id or scope manifest as primary ACCEPT evidence. |

---

## Anti-pattern 9 — Copied rationale

| Field | Content |
|-------|---------|
| **Wrong logic** | Reuse same explanation text across phrases. |
| **Example** | «Соответствует услуге внедрения, коммерческий запрос» on 50 different phrases. |
| **Damage** | Fails phrase-specific standard; masks annotator error; breaks audit. |
| **Correct action** | Six-part phrase-specific rationale per [`ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](../guidelines/ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md). |
| **Detection rule** | Rationale text similarity > threshold across unrelated `raw_query` rows. |

---

## Anti-pattern 10 — Cluster-level decision applied to every phrase

| Field | Content |
|-------|---------|
| **Wrong logic** | Adjudicator resolves cluster once → bulk-apply to all members. |
| **Example** | Cluster «интеграция 1с» adjudicated ABSTAIN → all integration phrases auto-ABSTAIN without read. |
| **Damage** | Loses phrase-level nuance; violates unit-of-annotation rule. |
| **Correct action** | Cluster adjudication may inform policy, not replace per-phrase Steps 1–10. |
| **Detection rule** | Batch eligibility update without per-phrase `literal_interpretation` timestamp change. |

---

## Anti-pattern 11 — Model confidence treated as evidence

| Field | Content |
|-------|---------|
| **Wrong logic** | LLM or classifier probability ≥ 0.9 → ACCEPT without human signals. |
| **Example** | `confidence: 0.92` on «erp» → ACCEPT. |
| **Damage** | Automation bias; ungrounded decisions in audit trail. |
| **Correct action** | Model scores are hints only; cite phrase spans in `signals[]`. |
| **Detection rule** | ACCEPT/REJECT with empty `signals[]` but populated model confidence only. |

---

## Anti-pattern 12 — LLM validates its own output

| Field | Content |
|-------|---------|
| **Wrong logic** | Same LLM pass annotates and reviews; or LLM marked `HUMAN_REVIEWED`. |
| **Example** | GPT adjudication chain: draft → self-approve ACCEPT. |
| **Damage** | Circular validation; violates human-in-the-loop authority model. |
| **Correct action** | LLM assistant role limited to structured evidence; human or blind second annotator reviews. |
| **Detection rule** | `audit.annotator_role` = LLM and `review.workflow_status` = APPROVED_FOR_CORE without human id. |

---

## Anti-pattern 13 — Product intent silently converted to service intent

| Field | Content |
|-------|---------|
| **Wrong logic** | «купить 1с» relabelled REQUEST_IMPLEMENTATION to force service ACCEPT. |
| **Example** | BUY_PRODUCT_OR_MODULE → REQUEST_IMPLEMENTATION without user saying настроить/внедрить. |
| **Damage** | Product buyers routed to service landing; landing mismatch. |
| **Correct action** | PRODUCT_VS_SERVICE adjudication; REJECT or ABSTAIN; never silent intent swap. |
| **Detection rule** | Primary intent changed at adjudication from product family to commercial without new evidence spans. |

---

## Anti-pattern 14 — Career intent treated as customer demand

| Field | Content |
|-------|---------|
| **Wrong logic** | Job seeker queries treated as buyers of programming services. |
| **Example** | «работа программистом 1с» → ACCEPT as hire-service demand. |
| **Damage** | Protected career stratum leak; violates D3 protected FPR gate. |
| **Correct action** | CAREER_EMPLOYMENT dominant → REJECT; career vs provider tie → ABSTAIN. |
| **Detection rule** | ACCEPT with career markers (вакансия, резюме, зарплата, работа) in `raw_query`. |

---

## Anti-pattern 15 — ABSTAIN suppressed to inflate automation rate

| Field | Content |
|-------|---------|
| **Wrong logic** | Convert mandatory ABSTAIN to ACCEPT or REJECT to reduce review queue. |
| **Example** | «программист 1с» forced REJECT instead of ABSTAIN to avoid reviewer load. |
| **Damage** | Under-reports ambiguity; false negatives on career/provider border. |
| **Correct action** | ABSTAIN is valid terminal outcome per D4; route to review. |
| **Detection rule** | REJECT on SHORT_HEAD or CAREER_VS_PROVIDER without `reason_code` from REJECT family and without resolved ambiguity. |

---

## Anti-pattern 16 — Semantic decision made during export

| Field | Content |
|-------|---------|
| **Wrong logic** | Eligibility decided in PPC exporter, Commander script, or campaign build step. |
| **Example** | Export script ACCEPTs phrase because it matched a keyword group file. |
| **Damage** | Decisions lack schema record, provenance, and benchmark regression anchors. |
| **Correct action** | Eligibility must exist in semantic record before export; export reads decision only. |
| **Detection rule** | Core promotion without matching `query_id` in semantic record store. |

---

## Related documents

- [`../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md)
- [`../guidelines/ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](../guidelines/ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md)
- [`ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md`](ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md)

---

**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Note:** Training and QA reference only — not gold benchmark labels.
