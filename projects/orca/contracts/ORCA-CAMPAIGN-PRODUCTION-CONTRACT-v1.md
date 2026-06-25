# ORCA Campaign Production Contract v1

**Status:** CANONICAL — authority above classifier, repair package, and pipeline validators  
**Derived from:** Triumph Manipulator battle production evidence  
**Machine-readable:** [orca-campaign-production-contract-v1.json](orca-campaign-production-contract-v1.json)  
**Invariants:** [orca-campaign-production-invariants-v1.json](orca-campaign-production-invariants-v1.json)  
**Validator:** `tools/validate-campaign-production-contract.mjs`

---

## Purpose

Prevent recurrence of Corvonero v1–v7 failures where automation:

- removed operator commercial services;
- excluded protected seeds;
- HOLD'd narrow commercial groups;
- retained informational queries;
- substituted templates for operator decisions;
- declared PASS on commercially invalid campaigns.

This contract codifies the **proven Triumph production discipline** as mandatory ORCA law.

**Cross-system lifecycle:** Campaign production stages SPPC-14–20 are governed by [MARS Search PPC Production Lifecycle v1](../../mars-search-ppc-production/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-v1.md). This contract remains the **campaign SoT invariant layer** within those stages — not a substitute for full lifecycle prerequisites (semantic, market evidence, strategy).

---

## Authority order (non-negotiable)

Lower levels **cannot** override higher levels:

1. Explicit operator decisions  
2. Operator-approved business/service scope  
3. Operator-approved campaign architecture  
4. Operator-approved group/intent architecture  
5. Verified market and semantic evidence  
6. Production rules (this contract, Triumph laws)  
7. Classifier suggestions  
8. QA and repair suggestions  
9. Export formatting  

---

## Section A — Operator Scope Lock

Every mandatory service receives:

- stable `service_id`
- campaign representation status
- owner `group_id`
- `landing_id` / URL mapping
- absence policy (`absence_from_production_permitted`)

**Prohibited:** classifier or repair scripts silently changing scope fields.  
**Block export:** any required service missing from export.

---

## Section B — Commercial Seed Protection

Every operator-approved direct commercial seed receives:

- `protected` status in recovery/scope artefact
- group ownership
- allowed normalization rules (documented)
- explicit operator-removal requirement

**Automatic EXCLUDE of protected seeds is forbidden.**

---

## Section C — Campaign Architecture First

Before final semantic processing, freeze:

- campaign count
- logical directions
- groups and intent boundaries
- landing ownership
- ad ownership

Corvonero: **one unified campaign** remains operator decision — contract does not auto-split.

---

## Section D — Group Viability

A group is viable when:

- it owns a distinct paid-service intent
- it has ≥1 legitimate commercial phrase
- it has an ad
- it has a landing mapping
- negative separation is safe

**No arbitrary minimum keyword count.**

---

## Section E — Semantic Admission

Every active phrase must answer:

1. What paid service is sought?  
2. Why may the user hire a provider?  
3. Which group owns it?  
4. What informational alternative exists?  
5. Why is ACTIVE or CONTROLLED TEST justified?

---

## Section F — Controlled Tests

Each controlled test requires:

- phrase-specific hypothesis
- specific noise risk
- group, ad, landing
- lower-risk bid tier
- post-launch success rule
- pause/exclusion rule

**No copied cross-topic hypothesis templates.**

---

## Section G — Inline Negative Limit

Phrases requiring extensive inline-minus exclusions should be:

- rewritten,
- replaced,
- excluded, or
- isolated only with explicit operator evidence.

**Threshold:** >3 inline-minus tokens or long phrase with ≥2 inline minuses → violation.

**Base-phrase rule (v7.1):** Inline negatives may narrow a valid commercial phrase; they may **not** convert an invalid, informational, educational, regulatory, or ambiguous **positive base** into a commercial keyword. Validators must:

1. Strip inline negatives and evaluate the positive base phrase  
2. Check `operator-semantic-exclusion-registry` (normalization does not bypass)  
3. Flag destructive rescue tails (multiple unrelated negative categories on a weak base)

**Invariants:** `INV-EXCL-01`, `INV-INLINE-01`, `INV-INLINE-02`, `INV-SEM-EDU-01`

---

## Section H — Negative Architecture

Negatives are produced **after** final phrase ownership.

Every negative must identify:

- protected intent
- competing intent
- scope (campaign / direction / group)
- collision result
- semantic-risk result

---

## Section I — QA Authority Boundary

QA **may:** detect, warn, block, recommend.  

QA **may not:**

- remove mandatory services
- exclude protected seeds
- merge approved groups without operator decision
- change campaign count or landing ownership
- invent commercial scope

---

## Section J — External Artefact Gate

Final Commander XLSX and review workbook must be:

- independently reopened
- inspected for placeholder/index defects
- reconciled with canonical JSON counts

Internal pipeline PASS is **not** independent proof.

---

## Section K — Commercial Validity Gate

PASS requires:

- service coverage (operator scope)
- protected seed coverage
- intent purity per group
- ad and landing alignment
- safe negative architecture
- no critical contract invariant failure

**Technical structural PASS alone is insufficient.**

---

## Application

| Project | Config |
|---------|--------|
| Corvonero v7 | `projects/corvonero-yandex-direct/production/validation/orca-contract-audit-config-v7.json` |

Run:

```bash
node projects/orca/tools/validate-campaign-production-contract.mjs \
  --config projects/orca/projects/corvonero-yandex-direct/production/validation/orca-contract-audit-config-v7.json
```

---

## Boundaries

- Documentation and read-only validator — **not** runtime orchestration  
- Does not authorize launch, import, or Commander v8  
- Operator approval remains mandatory after contract PASS
