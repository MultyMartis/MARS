# ATLAS Operational Organization Evidence Rule v1

**Status:** **documented** — population governance rule (normative for stewards).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Trigger:** i-SEO channel clients (e.g. Makita Snab) — real operational counterparties without contract or Counterparty Card access.  
**Parent:** [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) · [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) · [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** Foundation amendment, runtime policy, automated validator, CRM integration spec.

**Constraint:** This document **adds** population discipline for channel-specific Organization intake. It does **not** modify existing Foundation documents.

---

## 1. Purpose

Formalize **when an Organization may exist without Counterparty Card (CC) evidence** — without conflating Organization existence with Legal Entity attestation.

**Business reality:**

- Atlas serves **multiple channels** (Polygon, Metallka, SERM Moscow, i-SEO, operator core).
- Not every real organization is accessible through contracts, accounting, or CC folders.
- Blocking valid operational counterparties solely because CC is absent creates **registry blind spots**.

**Normative separation:**

```text
Organization existence  ≠  Legal Entity attestation

Organization may exist at E0 operational evidence.
Legal Entity requires E1+ documentary evidence.
```

---

## 2. Evidence categories

### 2.1 Category A — Counterparty Card REQUIRED

| Aspect | Rule |
|--------|------|
| **Applies to** | Polygon clients · Metallka clients · SERM Moscow clients |
| **Reason** | Contractual relationship exists or is expected; steward has or will obtain CC path |
| **Organization population** | **Allowed** — CC preferred path per OAR-01 |
| **Legal Entity population** | **Required path through Counterparty Card** — LE-* from CC-backed fields |
| **Minimum tier — Organization active** | **E1** (CC path) for external client |
| **Minimum tier — Legal Entity active** | **E1+** from CC |

**Channel mapping (operator-confirmed):**

| Channel | CC folder slug examples | Category |
|---------|-------------------------|----------|
| Polygon | `polygon`, `triumph`, `bzpm`, `sibcar` | **A** |
| Metallka | `metallka` | **A** |
| SERM Moscow | `moscow-serm` | **A** |

**Category A safeguards:**

- EFV-04, EFV-05, CPV-01..05 remain **fully applicable**.
- Absent CC → Organization **active** attestation **blocked** (STOP-W1-04 analog).
- Waiving CC for Category A external-client **active** attestation is **forbidden**.

---

### 2.2 Category B — Counterparty Card OPTIONAL

| Aspect | Rule |
|--------|------|
| **Applies to** | **i-SEO clients** |
| **Examples** | Makita Snab · future i-SEO SEO clients · future i-SEO Direct clients |
| **Reason** | Operational relationship confirmed; CC, contracts, and accounting **not** in steward scope |
| **Organization population** | **Allowed** at **E0** when operational evidence satisfies §3 |
| **Legal Entity population** | **Deferred** — LE-* creation **SAFE UNKNOWN** until E1+ evidence appears |
| **Minimum tier — Organization active** | **E0** (operational evidence path) |
| **Minimum tier — Legal Entity active** | **E1+** — **not authorized** without CC or E2 registry extract |

**Operational evidence requirements (Category B — Organization layer only):**

At least **two** of the following must be steward-attested with cited `EV-*` refs:

| Signal | Examples |
|--------|----------|
| Direct communication | Named contact; phone; messenger — steward-confirmed |
| Active work | SEO delivery, Direct campaigns, ongoing service |
| Known websites | Operator-confirmed URLs — **candidates only**; no WEB-* mint required |
| Known owner / contact | Given name or role — **not** sufficient alone for PER-* |
| Confirmed business relationship | Client of i-SEO; steward operational scope documented |

**Category B explicit deferrals:**

| Field / entity | State |
|----------------|-------|
| Legal entity name | **SAFE UNKNOWN** |
| INN / KPP / OGRN | **SAFE UNKNOWN** |
| Legal signatory | **SAFE UNKNOWN** |
| EDO | **SAFE UNKNOWN** |
| LE-* | **Not created** until E1+ |
| CC folder absent | **Not a blocker** for Organization **active** at E0 |

---

## 3. Operational Organization Evidence Path

**OOEP** — approved intake workflow for Category B Organization population.

```text
1. Classify channel → Category B (i-SEO client)
2. Inventory operational evidence (EV-* refs) — CPV optional for org layer
3. Record operational signals — contact, work scope, website candidates
4. Run duplicate review on display name + hostname candidates (no INN/OGRN close required)
5. Mint ORG-* with evidence_tier E0 — legal_entity_id = SAFE UNKNOWN
6. Steward attestation → Organization active
7. Defer LE-*, PER-*, WEB-*, DOM-*, PRJ-*, REL-* to future waves
```

**Reference implementation:** [ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md).

---

## 4. Rule outcome — layer separation

| Layer | Category A | Category B |
|-------|------------|------------|
| **Organization** | CC-backed E1+ typical | E0 operational — **active allowed** |
| **Legal Entity** | CC-required LE-* | **Deferred** — SAFE UNKNOWN |
| **Aliases** | CC-backed only (EFV-01) | Display name only — no legal aliases without CC |
| **Relationships** | Future waves per commercial evidence | Future waves — **not inferred** from steward scope |
| **Websites / Domains** | CC or registrar E1 when populated | **Candidates only** until Wave 4 / 5 |

**Critical invariant:**

> Closing Organization **active** at E0 under Category B **does not** authorize Legal Entity population, INN assignment, or duplicate-review closure on legal identifiers.

---

## 5. Safeguards — prevent accidental blocking of valid i-SEO organizations

### OOER-01 — CC absence is not an Organization blocker (Category B)

| Rule | Meaning |
|------|---------|
| **Prohibition** | Do **not** reject Category B Organization population solely because `counterparty-cards\<slug>\` is absent or empty. |
| **Override** | CPV-03 / STOP-CPV-03 **Organization active** block applies to **Category A** external clients — **not** Category B at Organization layer. |

### OOER-02 — EFV-05 scoped waiver (Organization layer only)

| Rule | Meaning |
|------|---------|
| **Scope** | For Category B, duplicate review **Pass** on legal-identity claims remains **Open** — expected. |
| **Permitted** | Duplicate review **Pass** on **distinct-org** claims using display name + hostname disambiguation **without** INN/OGRN. |
| **Prohibition** | Waive does **not** extend to Legal Entity layer or alias attestation without CC. |

### OOER-03 — Intake-only posture must not persist when OOEP satisfied

| Rule | Meaning |
|------|---------|
| **Trigger** | Category B candidate with operational evidence per §2.2 and OOEP steps 1–5 complete. |
| **Action** | Proceed to Organization population — **do not** hold at «INTAKE ONLY — AWAITING CC» when OOEP gates pass. |
| **CC later** | CC arrival triggers **Legal Entity wave** — not retroactive invalidation of Organization **active**. |

### OOER-04 — Category misclassification guard

| Rule | Meaning |
|------|---------|
| **Check** | Before applying Category B, confirm client is **i-SEO channel** — not Polygon / Metallka / SERM Moscow. |
| **Misclass risk** | Applying Category B to Category A client → **governance violation** — reopen intake. |

### OOER-05 — No hostname-only Organization (unchanged)

| Rule | Meaning |
|------|---------|
| **Prohibition** | URL or domain string **alone** does **not** satisfy OOEP — OAR-BAN-03 analog applies. |
| **Requirement** | Operational relationship signals (§2.2) must accompany website candidates. |

### OOER-06 — Service context does not mint edges

| Rule | Meaning |
|------|---------|
| **Prohibition** | «Client of i-SEO» operational context **must not** create REL-* CLIENT_OF without Wave 6+ commercial review. |
| **Reference** | ORG-0003 i-SEO may appear as **informational vendor context** only. |

---

## 6. Stop conditions

| Stop ID | Condition | Action |
|---------|-----------|--------|
| **STOP-OOER-01** | Category B Organization **active** attempted with fewer than two operational signals | Block **active** — remain **proposed** or enrich evidence |
| **STOP-OOER-02** | LE-* created for Category B without E1+ documentary evidence | **Reject** LE mint — correction required |
| **STOP-OOER-03** | Category A client processed under Category B | Reopen intake — apply CC path |
| **STOP-OOER-04** | Legal Entity fields filled from display name similarity | Revert to **SAFE UNKNOWN** |
| **STOP-OOER-05** | Organization blocked at intake solely for absent CC (Category B, OOEP satisfied) | **Violation** — apply OOER-03 |

---

## 7. Relationship to existing rules

| Document | Interaction |
|----------|-------------|
| [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | EFV-01..06 apply; EFV-05 legal-identity closure waived at Organization layer for Category B only |
| [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md) | CPV inventory still recommended; CC absence not blocking Category B Organization **active** |
| [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md) | OAR-01 CC-first preserved for Category A; Category B adds documented alternate path |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) | E0 operator-known path extended to i-SEO operational clients at Organization layer |

---

## 8. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md](ATLAS-WAVE1D-MAKITA-ORGANIZATION-POPULATION-v1.md) | First Category B population reference |
| [ATLAS-MAKITA-INTAKE-ANALYSIS-v1.md](ATLAS-MAKITA-INTAKE-ANALYSIS-v1.md) | Prior intake — superseded for population by Wave 1D |
| [ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md) | Operational evidence source |

---

*ATLAS Operational Organization Evidence Rule v1 — documentation only.*
