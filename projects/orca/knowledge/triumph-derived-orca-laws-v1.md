# Triumph-Derived ORCA Laws v1

**Authority:** Triumph Manipulator battle production evidence  
**Contract:** `contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md`

---

## ORCA-LAW-01 — Operator scope lock

| Field | Value |
|-------|-------|
| **Statement** | Operator business/service scope is fixed before semantic processing and cannot be silently narrowed by automation |
| **Triumph evidence** | Route family freeze before JSON build; 12/12 routes mandatory |
| **Rationale** | Prevents classifier/repair from deleting commercially required services |
| **Enforcement** | Pre-semantic scope registry; contract validator INV-SCOPE-01 |
| **Severity** | critical |
| **Automated** | Yes |
| **Human check** | Operator confirms scope registry matches charter |

---

## ORCA-LAW-02 — Protected commercial seeds

| Field | Value |
|-------|-------|
| **Statement** | Operator-approved direct commercial seeds cannot be auto-EXCLUDED |
| **Triumph evidence** | Primary phrases per route (`is_primary: true` in JSON) |
| **Rationale** | Corvonero v6 lost 41 seeds — proven failure mode |
| **Enforcement** | Recovery package + INV-SEED-01 |
| **Severity** | critical |
| **Automated** | Yes |
| **Human check** | Anchor phrase spot-check in XLSX |

---

## ORCA-LAW-03 — One intent per group

| Field | Value |
|-------|-------|
| **Statement** | One group owns one distinguishable commercial intent |
| **Triumph evidence** | SE-01; 12 route groups |
| **Rationale** | Budget bleed and ad↔query mismatch |
| **Enforcement** | Semantic validator; group architecture freeze |
| **Severity** | critical |
| **Automated** | Partial |
| **Human check** | Group-by-group intent review |

---

## ORCA-LAW-04 — Narrow group validity

| Field | Value |
|-------|-------|
| **Statement** | Narrow groups are valid when intent is commercially distinct |
| **Triumph evidence** | Low-count capability routes in battle export |
| **Rationale** | Corvonero v6 wrongly HOLD'd operator-required narrow groups |
| **Enforcement** | INV-HOLD-01; viability ≠ keyword count |
| **Severity** | critical |
| **Automated** | Yes |
| **Human check** | Confirm distinct user need per narrow group |

---

## ORCA-LAW-05 — Group size ≠ service existence

| Field | Value |
|-------|-------|
| **Statement** | Keyword count and frequency do not determine whether an operator-required service exists |
| **Triumph evidence** | Intent tiers prioritize S routes regardless of volume |
| **Rationale** | Prevents false HOLD on low-data commercial services |
| **Enforcement** | Group viability logic must not use min-kw threshold |
| **Severity** | high |
| **Automated** | Yes |
| **Human check** | Operator confirms service commercial viability |

---

## ORCA-LAW-06 — No informational filler

| Field | Value |
|-------|-------|
| **Statement** | Information queries cannot be retained merely to fill a group |
| **Triumph evidence** | SE-03 employment/education blocklist |
| **Rationale** | Corvonero v4–v6 informational leakage |
| **Enforcement** | INV-SEM-01 blocklist |
| **Severity** | critical |
| **Automated** | Yes |
| **Human check** | Edge-case regulatory phrases |

---

## ORCA-LAW-07 — Inline minus limit

| Field | Value |
|-------|-------|
| **Statement** | Weak phrases cannot be rescued via long inline-minus tails |
| **Triumph evidence** | Group negatives used instead of phrase-level hacks |
| **Rationale** | Unmaintainable phrases; false PASS |
| **Enforcement** | INV-INLINE-01 |
| **Severity** | high |
| **Automated** | Yes |
| **Human check** | Review flagged phrases |

---

## ORCA-LAW-08 — Ownership before negatives

| Field | Value |
|-------|-------|
| **Statement** | Phrase ownership finalized before cross-negatives |
| **Triumph evidence** | Cross-negative matrix runs on frozen JSON instance |
| **Rationale** | Negatives on wrong ownership create collisions |
| **Enforcement** | Pipeline order gate |
| **Severity** | critical |
| **Automated** | Partial |
| **Human check** | Collision evidence review |

---

## ORCA-LAW-09 — Negatives separate, not manufacture

| Field | Value |
|-------|-------|
| **Statement** | Negatives separate valid neighboring intents; they do not manufacture artificial architecture |
| **Triumph evidence** | CROSS-NEGATIVE-RULES-v1 sibling-route tokens |
| **Rationale** | Artificial separation hides missing groups |
| **Enforcement** | Negative architecture review |
| **Severity** | high |
| **Automated** | Partial |
| **Human check** | Neighbor group rationale |

---

## ORCA-LAW-10 — Ad/phrase/group/landing alignment

| Field | Value |
|-------|-------|
| **Statement** | Ad, phrase, group and landing must express the same need |
| **Triumph evidence** | LM-* landing continuity; keyword_alignment in JSON |
| **Rationale** | Conversion and quality score risk |
| **Enforcement** | INV-AD-01 |
| **Severity** | critical |
| **Automated** | Yes (base URL) |
| **Human check** | Copy-level continuity |

---

## ORCA-LAW-11 — QA boundary

| Field | Value |
|-------|-------|
| **Statement** | QA may block but cannot silently change operator scope |
| **Triumph evidence** | Validator flags; human import; no auto-launch |
| **Rationale** | Corvonero v4–v6 classifier/repair overreach |
| **Enforcement** | Contract section I; pipeline integration plan |
| **Severity** | critical |
| **Automated** | Partial |
| **Human check** | Diff scope registry after QA runs |

---

## ORCA-LAW-12 — Service disappearance blocks export

| Field | Value |
|-------|-------|
| **Statement** | Any disappearance of a required service blocks export |
| **Triumph evidence** | 12/12 route export fidelity QA |
| **Rationale** | Commercial invalidity despite structural PASS |
| **Enforcement** | INV-SCOPE-01 |
| **Severity** | critical |
| **Automated** | Yes |
| **Human check** | Service family checklist |

---

## ORCA-LAW-13 — Classifier advisory only

| Field | Value |
|-------|-------|
| **Statement** | Machine classification is advisory, not business authority |
| **Triumph evidence** | Human-triggered validation-cli; doctrine copilot role |
| **Rationale** | v4 identical template evidence on 324 phrases |
| **Enforcement** | Authority order in contract |
| **Severity** | critical |
| **Automated** | No |
| **Human check** | Operator semantic sign-off |

---

## ORCA-LAW-14 — External artefact gate

| Field | Value |
|-------|-------|
| **Statement** | Final XLSX must be independently reopened and audited |
| **Triumph evidence** | GROUP-FIDELITY-QA; Commander import human spot-check |
| **Rationale** | v5 ExcelJS shared-string placeholder failure |
| **Enforcement** | workbook-xlsx-inspector pattern |
| **Severity** | high |
| **Automated** | Partial |
| **Human check** | Commander desktop dry-run |

---

## ORCA-LAW-15 — Technical ≠ commercial validity

| Field | Value |
|-------|-------|
| **Statement** | Campaign may be structurally valid and commercially invalid |
| **Triumph evidence** | Import PASS with launch not approved; lessons learned §commercial |
| **Rationale** | Corvonero v6 structural tools PASS with scope loss |
| **Enforcement** | Contract validator commercial gate |
| **Severity** | critical |
| **Automated** | Yes (contract layer) |
| **Human check** | Operator commercial sign-off |

---

## Project-specific Triumph rules (not generalized)

| Rule | Scope |
|------|-------|
| 5t / 14m capability claims | Triumph equipment line only |
| Krasnodar geo in copy | Triumph region targeting |
| manipulator-triumph.ru URL set | Triumph landing registry |
| 12 route slug taxonomy | Triumph route family freeze |
| Fastlink cross-route pattern | Triumph ad extensions |
