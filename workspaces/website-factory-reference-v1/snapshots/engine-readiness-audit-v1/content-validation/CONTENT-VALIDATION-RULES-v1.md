# Website Factory — Content Validation Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** architecture gates for Content Validation Layer — **documentation only**  
**Связь:** [CONTENT-VALIDATION-SYSTEM-v1.md](CONTENT-VALIDATION-SYSTEM-v1.md), [content-contracts/CONTENT-RULES-v1.md](../content-contracts/CONTENT-RULES-v1.md)

**Не является:** automated linter, copy style guide, runtime policy engine.

---

## Severity legend

| Level | Meaning |
|-------|---------|
| **CRITICAL** | Halt — architecture invalid; no Frontend |
| **ERROR** | Must fix before production content gate |
| **WARNING** | Document operator exception |
| **INFO** | Log only |

Full definitions: [CONTENT-SEVERITY-SYSTEM-v1.md](CONTENT-SEVERITY-SYSTEM-v1.md).

---

## Upstream gates

| ID | Rule | Severity |
|----|------|----------|
| CV-R01 | **Page Block Validation first** — do not run content validation on FAIL/CRITICAL page-block outcome | CRITICAL |
| CV-R02 | **No new taxonomy** — no new `site_type_code`, `page_type`, `block_id`, `signal_id` in validation workstream | CRITICAL |
| CV-R03 | **Validate architecture only** — signals and slots; not final copy quality or readability | CRITICAL |
| CV-R04 | **No generation in validation** — validation does not produce or rewrite text | CRITICAL |
| CV-R05 | **No runtime** — rules describe human-operated checks; no validator product claimed | CRITICAL |

---

## Signal presence

| ID | Rule | Severity |
|----|------|----------|
| CV-R06 | **Required signals must exist** — every `signal_id` in merged `required_signals` must be satisfiable in declared architecture | ERROR |
| CV-R07 | **Forbidden signals must not exist** — any `forbidden_signals` binding → FAIL | ERROR–CRITICAL per matrix |
| CV-R08 | **Unsupported signals must fail** — `signal_id` not in CONTENT-SIGNAL-REGISTRY-v1 → unexpected + FAIL | ERROR |
| CV-R09 | **Optional signals** — absence alone does not FAIL; absence on REQUIRED block when site-type recommends → WARNING | WARNING |
| CV-R10 | **No contradictory signals** — e.g. `payment` on CATALOG PDP primary path + RFQ-only Blueprint without charter | CRITICAL |
| CV-R11 | **No placeholder leakage** — `TBD`, lorem, `[COMPANY]`, template tokens in production-bound signal slots | ERROR |

---

## Legal and trust

| ID | Rule | Severity |
|----|------|----------|
| CV-R12 | **LEGAL_PAGE content must align with Legal Pack** — only `legal_disclosure` + `entity_identity` (+ optional `contact`); marketing signals forbidden | CRITICAL |
| CV-R13 | **Forms require consent architecture** — `LEAD_FORM` / `CHECKOUT` instances must declare `consent` when block REQUIRED | CRITICAL |
| CV-R14 | **Required trust signals** — when `TRUST`, `TESTIMONIALS`, `REVIEWS`, or `CERTIFICATES` block REQUIRED, block-level `proof`/`trust`/`review`/`certificate` rules apply | ERROR |
| CV-R15 | **Required conversion signals** — when conversion block REQUIRED (`HERO`, `CTA`, `LEAD_FORM`, `CHECKOUT`), `cta` must be satisfiable | ERROR |
| CV-R16 | **NAP follows Legal Entity Card** — `contact`, `location`, `entity_identity` on CONTACTS/FOOTER must reference documented entity | ERROR |

---

## Evidence and truth (architecture)

| ID | Rule | Severity |
|----|------|----------|
| CV-R17 | **No fake evidence** — `proof` without evidence_rule plan (HITL_REQUIRED / SOURCE_DOCUMENTED) documented | CRITICAL |
| CV-R18 | **No fake review signal** — `review` binding without UGC_AUTHENTIC plan; fabricated review slot | CRITICAL |
| CV-R19 | **No unsupported claims** — `certificate`, `guarantee`, `experience`, `urgency` without required evidence path | CRITICAL |
| CV-R20 | **Urgency requires source** — `urgency` only when SOURCE_DOCUMENTED rule attached in architecture notes | ERROR |

---

## Layer alignment

| ID | Rule | Severity |
|----|------|----------|
| CV-R21 | **Content follows Blueprint** — signals must not imply blocks/pages excluded by active Blueprint | CRITICAL |
| CV-R22 | **Content follows Page Architecture** — page-level forbidden signals enforced | CRITICAL |
| CV-R23 | **Content follows Block Registry** — validate only registry `block_id`; no signals for non-registry blocks | CRITICAL |
| CV-R24 | **SEO subordination** — page signals must not contradict PAGE-SEO-CONTRACT role | ERROR |
| CV-R25 | **Design expressibility** — required signals must be expressible in selected `VF_*` pattern (manual cross-check v1) | WARNING |

---

## Commerce path

| ID | Rule | Severity |
|----|------|----------|
| CV-R26 | **CATALOG: no payment architecture** — `payment` forbidden on CATALOG site-type primary paths unless reclassification | CRITICAL |
| CV-R27 | **ECOMMERCE: checkout signals** — `CHECKOUT` REQUIRED routes must declare `payment`, `delivery`, `consent`, `process` | ERROR |
| CV-R28 | **Price signal matches model** — listed `price` vs RFQ stance documented per Blueprint | ERROR |

---

## Scope boundaries

| ID | Rule | Severity |
|----|------|----------|
| CV-R29 | **No SEO copy validation** — meta, keywords, body SEO text out of scope | CRITICAL (scope) |
| CV-R30 | **No prompts** — defer to Generation Contracts (not queued) | CRITICAL (scope) |
| CV-R31 | **No content creation** — validation records gaps; does not fill slots | CRITICAL (scope) |

---

## Mapping to Content Rules

Content Validation rules **implement** checks implied by [CONTENT-RULES-v1.md](../content-contracts/CONTENT-RULES-v1.md) (CT-R01–CT-R25) at validation time. On conflict, **Content Contracts + Content Rules** are normative for signal definitions; **this document** is normative for validation procedure and status aggregation.

---

## Pre-flight checklist (human-operated)

1. Page Block Validation — not FAIL; no CRITICAL block issues.
2. Load `site_type_code`, Blueprint, `page_type`, block stack.
3. Merge required/optional/forbidden signals per [CONTENT-SIGNAL-VALIDATION-MATRIX-v1.md](CONTENT-SIGNAL-VALIDATION-MATRIX-v1.md).
4. For each REQUIRED `block_id` — block validation run.
5. Page-level signal run.
6. Apply SITE-TYPE-CONTENT-MAPPING forbidden patterns.
7. Record contract fields; set `status`.
8. On FAIL/CRITICAL — consult [CONTENT-FAILURE-LIBRARY-v1.md](CONTENT-FAILURE-LIBRARY-v1.md).

---

## SAFE UNKNOWN

- Automated enforcement of CV-R* — **FUTURE**
- Per-industry rule packs — **FUTURE**

---

*Content Validation Rules version: v1.*
