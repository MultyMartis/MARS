# ATLAS Card Presence Validation Rule v1



**Status:** **documented** — population governance safeguard (normative for stewards).  

**Program:** ATLAS — Business Reality Registry  

**Date:** 2026-06-06  

**Trigger:** [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) — active attestation requires provable CC folder state before evidence conclusions.  

**Parent:** [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md)  

**Is not:** Foundation amendment, runtime policy, automated filesystem watcher, OCR rule set.



**Constraint:** This document **adds** population discipline. It does **not** modify existing Foundation documents.



---



## 1. Purpose



Prevent **false absence** and **false presence** claims about Counterparty Cards (CC) during Organization intake and attestation. Stewards must **prove** folder state on disk before asserting that evidence exists, is missing, or supports identity conclusions.



---



## 2. Normative rules



### CPV-01 — Inventory required before evidence conclusions



| Rule | Meaning |

|------|---------|

| **Requirement** | Before any evidence sufficiency verdict, identity extraction, or attestation gate closure, the steward **must** produce a **filesystem inventory table** for the target org slug folder under `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\<org-folder>\`. |

| **Minimum columns** | filename · format · size · role |

| **Stop** | If inventory is **not** produced → **STOP** — no attestation, no «CC absent» marker update, no duplicate-review closure on CC-backed claims. |



### CPV-02 — Card missing claims require filesystem verification



| Rule | Meaning |

|------|---------|

| **Requirement** | A claim that a Counterparty Card is **missing**, **absent**, or **not placed** **must** cite the result of a **direct folder listing** (or equivalent filesystem check) at the canonical external path. |

| **Prohibition** | Do **not** infer CC absence from population package age, prior ME-* markers, or narrative context alone. |

| **Revocation** | When a prior «CC absent» marker is contradicted by filesystem proof → **obsolete** the marker in the verification or attestation record; do not silently overwrite population packages. |



### CPV-03 — Evidence absent claims require inventory proof



| Rule | Meaning |

|------|---------|

| **Requirement** | A claim that evidence is **insufficient** or **not found** for a specific field **must** reference the inventory row set and state which expected artifact types are absent **after** listing. |

| **Placeholder exclusion** | `_PLACE_FILES_HERE.txt` and empty-folder markers **do not** count as non-placeholder evidence. |

| **Minimum bar** | At least **one non-placeholder** evidence file must exist in the org folder before CC-backed **active** Organization attestation for W1-B / W1-C external clients. |



### CPV-04 — No identity decisions before evidence inventory



| Rule | Meaning |

|------|---------|

| **Gate** | Canonical name finalization, legal entity field binding, alias register changes, and merge/split class decisions **must not** proceed until CPV-01 inventory is complete for the target org slug. |

| **Alignment** | Works with [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) EFV-04 — CC content overrides assumptions **after** inventory confirms CC presence. |



### CPV-05 — No duplicate review before card verification



| Rule | Meaning |

|------|---------|

| **Gate** | Duplicate-review verdicts that depend on INN, OGRN, or legal name **must not** be marked **Pass** (distinct or same-subject) until CPV-01 inventory is complete and, when CC is present, primary CC fields are extracted. |

| **Alignment** | Reinforces EFV-05 — evidence review mandatory before duplicate conclusions. |

| **Cross-org compare** | When comparing two org slugs, inventory **both** folders (or document explicit **SAFE UNKNOWN** for the absent folder) before distinct/subject verdict. |



---



## 3. Required workflow (Organization intake / active attest)



```text

1. Verify target folder exists at canonical external path

2. List all files → produce inventory table (CPV-01)

3. Confirm ≥1 non-placeholder file (CPV-03)

4. Cite primary Counterparty Card filename and path

5. Extract legal entity facts from primary CC

6. Run duplicate review on CC-backed identifiers

7. Only then → attestation sequence (proposed → active)

```



---



## 4. Stop conditions



| Stop ID | Condition | Action |

|---------|-----------|--------|

| **STOP-CPV-01** | Attestation or verification report lacks inventory table | **STOP** — complete inventory first |

| **STOP-CPV-02** | «CC missing» recorded without filesystem listing | Reopen gap register; run inventory |

| **STOP-CPV-03** | Active attest attempted; folder empty or placeholder-only | Block **active** |

| **STOP-CPV-04** | Duplicate review **Pass** on INN/OGRN; inventory not done | Reopen duplicate review |

| **STOP-CPV-05** | Primary CC cited but path not in inventory | Reconcile path; re-run inventory |



---



## 5. Relationship to existing rules



| Document | Relationship |

|----------|--------------|

| [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) | CPV operationalizes **when** CC must be confirmed on disk; EFV governs **how** CC content is used |

| [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) | CPV enforces external storage path discipline |

| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | Canonical path reference for CPV-01 |



---



## 6. Related documents



| Doc | Role |

|-----|------|

| [ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md](ATLAS-WAVE1B-BZPM-EVIDENCE-VERIFICATION-v1.md) | Reference inventory + extraction |

| [ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1B-BZPM-ACTIVE-ATTESTATION-v1.md) | First active attest applying CPV |

| [ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md](ATLAS-WAVE1C-SIBCAR-ACTIVE-ATTESTATION-v1.md) | Parallel W1-C attest pattern |



---



*ATLAS Card Presence Validation Rule v1 — documentation only.*

