# ATLAS Evidence-First Validation Rule v1

**Status:** **documented** — population governance safeguard (normative for stewards).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Trigger:** [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) — identity pollution from project-context inference without Counterparty Card review.  
**Parent:** [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) · [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) · [ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md](../foundation/ATLAS-ORGANIZATION-ACQUISITION-RULES-v1.md)  
**Is not:** Foundation amendment, runtime policy, automated validator, OCR rule set.

**Constraint:** This document **adds** population discipline. It does **not** modify existing Foundation documents.

---

## 1. Purpose

Prevent **identity pollution** during Organization population: merging distinct legal subjects, minting aliases from project or website naming, or closing duplicate review before Counterparty Card (CC) evidence is inspected.

---

## 2. Normative rules

### EFV-01 — No alias without evidence

| Rule | Meaning |
|------|---------|
| **Prohibition** | Do **not** register, propose, or attest an **alias** on an Organization unless the alias string (or accepted transliteration) appears on a cited **E1+** evidence artifact for **that same legal subject**, or an explicit steward attestation note cites cross-document proof. |
| **Operator codenames** | Internal project codenames (e.g. tranche labels) are **not** aliases unless CC or E2 registrar extract corroborates them as trade names of the same subject. |
| **Hostname stems** | Domain or subdomain strings support **Website** / **Domain** candidates only; they do **not** alone prove alias equivalence between two trade names. |

### EFV-02 — No organization merge from project context

| Rule | Meaning |
|------|---------|
| **Prohibition** | OCPilot site ids, EAR acquisition tracks, pilot charters, MIG packs, and project codenames **must not** be used to merge two Organization proposals. |
| **Class boundary** | Project and Website context may **correlate** with a future Organization edge — they do **not** substitute for Organization identity evidence. |

### EFV-03 — No organization equivalence from website / project naming

| Rule | Meaning |
|------|---------|
| **Prohibition** | Similar or related **site titles**, **URL slugs**, or **operator folder names** do **not** establish that two names refer to one legal entity. |
| **Example pattern (forbidden)** | «Site brand X» + «operator codename Y» → single Organization alias cluster **without CC review**. |

### EFV-04 — Counterparty Card overrides assumptions

| Rule | Meaning |
|------|---------|
| **Priority** | When a CC exists in `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\<org-folder>\`, stewards **must** read it **before** finalizing canonical name, legal entity fields, or alias register for that intake. |
| **Override** | CC fields **override** prior population assumptions, duplicate-review passes, and operational-context narratives. |
| **Contradiction** | If CC contradicts a prior conclusion → **correction record** required ([ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) is the reference pattern). |

### EFV-05 — Evidence review mandatory before duplicate conclusions

| Rule | Meaning |
|------|---------|
| **Gate** | Duplicate-review verdicts (**Pass** / **Fail** / **Open**) for Organization intake **must not** be marked **Pass** on alias-cluster or same-org claims until CC intake is **complete or explicitly waived** with documented **SAFE UNKNOWN** and **blocked active attestation**. |
| **Waive** | Waiving CC review for **active** external-client Organization attestation is **forbidden** per Wave 1B STOP-W1-04 analog. |

### EFV-06 — Identity decisions require cited evidence source

| Rule | Meaning |
|------|---------|
| **Citation** | Every identity decision (canonical name, legal entity binding, alias add/remove, merge/split class) **must** cite at least one evidence ref: `EV-*`, CC path, registrar extract, or attestation note. |
| **Format** | Reports use: **claim → evidence ref → field quote or identifier** — no uncited inference. |
| **SAFE UNKNOWN** | Unknown fields remain **SAFE UNKNOWN**; do not fill from naming similarity. |

---

## 3. Required workflow (Organization intake)

```text
1. Check CC folder for target org slug
2. If CC present → extract legal entity facts → cite in proposal
3. Compare CC facts to any prior alias / merge assumptions
4. If mismatch → correction record before attestation
5. Run duplicate review using CC-backed identifiers (INN, OGRN, legal name)
6. Only then → attestation sequence
```

---

## 4. Stop conditions

| Stop ID | Condition | Action |
|---------|-----------|--------|
| **STOP-EFV-01** | Alias proposed without CC or E2 quote | Reject alias; keep **proposed** or **SAFE UNKNOWN** |
| **STOP-EFV-02** | Duplicate review **Pass** on same-org claim; CC not reviewed | Reopen review; downgrade verdict |
| **STOP-EFV-03** | CC contradicts registered alias cluster | Correction record + steward sign-off |
| **STOP-EFV-04** | Active attestation attempted while CC contradicts proposal | Block **active** until corrected |

---

## 5. Relationship to existing Foundation

| Foundation doc | This rule |
|----------------|-----------|
| [ATLAS-ALIAS-MODEL-v1.md](../foundation/ATLAS-ALIAS-MODEL-v1.md) | Operationalizes alias evidence requirement for population |
| [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) | Reinforces CC-first intake |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) | Merge/split classes still apply; this rule prevents premature merge |

---

## 6. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) | Reference verification report |
| [ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md](ATLAS-WAVE1B-BZPM-IDENTITY-CORRECTION-v1.md) | Reference correction record |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | CC storage pointer |

---

*ATLAS Evidence-First Validation Rule v1 — documentation only.*
