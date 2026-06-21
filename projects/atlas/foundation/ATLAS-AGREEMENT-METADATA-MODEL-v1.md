# ATLAS Agreement Metadata Model v1



**Status:** **documented** — Wave AGM-01 operational metadata overlay (documentation only).  

**Program:** ATLAS — Business Reality Registry  

**Date:** 2026-06-10  

**Wave:** AGM-01 — Agreement Metadata Layer  

**Parent:** [ATLAS-AGREEMENT-REALITY-MODEL-v1.md](ATLAS-AGREEMENT-REALITY-MODEL-v1.md) · [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) · [OPS-ATLAS-ALIGNMENT-v1.md](OPS-ATLAS-ALIGNMENT-v1.md)  

**Is not:** legal document storage, contract management, accounting schema, CRM deal object, runtime type definition, API schema.



---



## 1. Purpose



Define a **minimal metadata overlay** on attested Agreement entities (AGR-*) so operational systems (OPS) can answer questions beyond structural binding:



| Question | Metadata field |

|----------|----------------|

| Is agreement active? | `operational_status` |

| When does it expire? | `start_date`, `end_date` |

| Does it require renewal attention? | `renewal_posture` |

| Which operational documents are expected? | `document_expectation` |

| Which counterparty profile is used? | `counterparty_profile` |

| How strong is the evidence? | `evidence_level` |



**Normative ruling:**



> Agreement Metadata registers **operational consumption facts** — not legal clauses, contract text, signatures, or payment terms.



**Relationship to AGL-01:** Agreement entity rows remain canonical in [ATLAS-AGREEMENT-REGISTER-v1.md](../population/ATLAS-AGREEMENT-REGISTER-v1.md). Metadata register is a **companion overlay** — one metadata row per attested agreement; does not replace or mutate AGL-01 register semantics.



---



## 2. Expansion admission (AGM-01)



| Criterion | Assessment |

|-----------|------------|

| A-01 Consumer necessity | OPS WF-02 Live Pilot (2026-06-10) identified incomplete agreement metadata as PARTIAL blocker |

| A-02 Non-redundancy | AGL-01 `status` + `scope_summary` insufficient for renewal visibility and document expectation |

| A-03 Boundary cleanliness | No contract text, PDFs, workflows, or accounting — metadata pointers only |

| A-04 Human attestability | Fields derivable from existing ATLAS evidence or marked SAFE UNKNOWN |

| A-05 No runtime | Documentation register only |



---



## 3. Metadata record definition



### 3.1 Scope



One metadata record per attested `AGR-*` row in Agreement Register v1. **No metadata rows** for population-plan-only candidates (e.g. Makita futures).



### 3.2 Fields



| Field | Required | Description |

|-------|----------|-------------|

| **agreement_id** | **Yes** | Foreign key to attested Agreement (`AGR-*`) |

| **operational_status** | **Yes** | Operational lifecycle posture — see §4 |

| **start_date** | **Yes*** | ISO date or **SAFE UNKNOWN** |

| **end_date** | **Yes*** | ISO date or **SAFE UNKNOWN** |

| **renewal_posture** | **Yes** | Renewal visibility — see §5 |

| **counterparty_profile** | **Yes** | Minimal counterparty reference — see §6 |

| **document_expectation** | **Yes** | Expected operational document class — see §7 |

| **evidence_level** | **Yes** | E0–E3 tier — copied from Agreement register; not upgraded without new attestation |

| **notes** | Optional | Attestation rationale, evidence pointers, boundary notes |



\*Field is **required on record**; value may be **SAFE UNKNOWN** when evidence insufficient — not omitted.



### 3.3 Explicit exclusions (normative)



| Excluded | Belongs to |

|----------|------------|

| Contract full text | Legal archive |

| PDF / scan payload | Evidence vault pointer only |

| Signature workflow state | Legal / OPS document tracking |

| Payment terms, amounts | Accounting / ERP |

| Renewal automation rules | CRM / billing |

| Structured requisites fields (INN, bank) | Legal Entity layer + CC evidence — **pointer only** via counterparty_profile |

| Legal clause enumeration | Legal counsel systems |



---



## 4. Operational status vocabulary



Mirrors Agreement Register `status` where attested. Metadata layer does **not** introduce new lifecycle engine.



| Value | Meaning | Source |

|-------|---------|--------|

| **ACTIVE** | Commercial arrangement currently in effect | AGL-01 register + ACTIVE attestation act |

| **EXPIRED** | Arrangement concluded | AGL-01 register + deprecated project lifecycle |

| **SAFE UNKNOWN** | **Not valid on metadata row** — insufficient Agreement attestation → no metadata row |



**Rule AGM-MD-ST-01:** `operational_status` must match Agreement Register `status` for the same `agreement_id`. Metadata pass does not re-derive status.



---



## 5. Renewal posture vocabulary



Minimal vocabulary — metadata only; no workflow logic.



| Value | Meaning | Typical signal |

|-------|---------|----------------|

| **UNKNOWN** | Renewal cadence not attested | No dates; no operator renewal statement |

| **ONGOING** | Arrangement treated as continuing without fixed end | Active project + ongoing delivery attestation; retainer type |

| **FIXED_TERM** | Attested start/end or fixed term extract | E2+ date evidence with bounded period |

| **EXPIRED** | No renewal expected — arrangement concluded | EXPIRED operational_status |



**Rules:**



- **AGM-RP-01:** Do not infer FIXED_TERM from project start alone.

- **AGM-RP-02:** EXPIRED operational_status → renewal_posture **EXPIRED** (not UNKNOWN).

- **AGM-RP-03:** ACTIVE + no end_date attested → ONGOING only when ongoing delivery or retainer type attested; otherwise **UNKNOWN**.



---



## 6. Counterparty profile vocabulary



Minimal reference to existing ATLAS reality — **no Legal Entity layer redesign**.



| Form | Meaning | When used |

|------|---------|-----------|

| `LE-NNNN` | Attested Legal Entity id bound to client_org | LE attested and bound in Organization register |

| `LE-NNNN; EV-*` | LE reference + evidence pointer | CC or commercial evidence ref corroborates client org |

| **SAFE UNKNOWN** | No attested LE or CC for client party | Makita-style gaps; not used on AGM-01 register rows |



**Vendor org (ORG-0001):** Not repeated on metadata row — Agreement register already carries `vendor_org`. Metadata `counterparty_profile` refers to **client-side** document and requisites consumption context.



**Structured requisites consumption:** OPS may **follow pointers** (LE id, EV ref) to external CC storage per [COUNTERPARTY-CARD-STORAGE-README-v1.md](../population/COUNTERPARTY-CARD-STORAGE-README-v1.md). ATLAS metadata does **not** store INN, bank account, or signer blocks.



---



## 7. Document expectation vocabulary



Minimal vocabulary — metadata only; no workflow logic.



| Value | Meaning | Typical agreement signal |

|-------|---------|---------------------------|

| **UNKNOWN** | Document obligation class not attested | Insufficient scope or type evidence |

| **MONTHLY_REPORT** | Periodic client reporting expected | SEO_RETAINER; WF-01 consumer contour |

| **MONTHLY_CLOSING** | Periodic document closing (acts, annexes) on calendar rhythm | **Not attested in AGM-01** without explicit operator or E2 extract |

| **PROJECT_DELIVERY** | Milestone or delivery-phase document closing | DEVELOPMENT type; WF-02 pilot contour |

| **MIXED** | Multiple document classes under one anchor | Only when operator attests multiple obligation classes |



**Rules:**



- **AGM-DE-01:** Infer MONTHLY_REPORT from attested `SEO_RETAINER` agreement_type only.

- **AGM-DE-02:** Infer PROJECT_DELIVERY from attested `DEVELOPMENT` agreement_type + active project delivery graph.

- **AGM-DE-03:** Do not assign MONTHLY_CLOSING without explicit attestation — WF-02 pilot did not validate calendar closing cadence.

- **AGM-DE-04:** MIXED requires explicit multi-class attestation — not inferred from type alone.



---



## 8. Evidence discipline



| Tier | Metadata use |

|------|--------------|

| **E0** | Operator attestation + structural graph — metadata fields conservative |

| **E1** | CC or commercial spreadsheet pointer — counterparty_profile may include EV ref |

| **E2+** | Formal extract **reference** — dates may become attestable in future pass |



**Minimum for metadata register admission:**



1. Parent Agreement row attested in AGL-01 register

2. `operational_status` matches parent

3. All required fields present — **SAFE UNKNOWN** where evidence insufficient

4. No fabricated dates or renewal schedules



---



## 9. OPS consumer mapping (read-only)



| OPS workflow | Metadata fields consumed |

|--------------|-------------------------|

| **WF-01** Monthly reporting | `document_expectation` = MONTHLY_REPORT; `operational_status`; `agreement_id` |

| **WF-02** Document closing | `document_expectation`; `counterparty_profile`; `renewal_posture`; dates when attested |

| **WF-03** Client follow-up | `renewal_posture`; `end_date` when attested; `operational_status` |



OPS **reads** metadata at documentation layer. OPS does **not** store canonical metadata roster.



---



## 10. Anti-patterns



| Anti-pattern | Ruling |

|--------------|--------|

| Store contract PDF in metadata notes | **Forbidden** |

| Invent agreement dates | **Forbidden** |

| Upgrade evidence_level without attestation act | **Forbidden** |

| Duplicate LE requisites inline | **Forbidden** — pointer only |

| Metadata row without parent Agreement | **Forbidden** |

| CRM renewal automation fields | **Forbidden** |



---



## 11. Related documents



| Document | Role |

|----------|------|

| [ATLAS-AGREEMENT-REGISTER-v1.md](../population/ATLAS-AGREEMENT-REGISTER-v1.md) | Parent Agreement roster |

| [ATLAS-AGREEMENT-METADATA-REGISTER-v1.md](../population/ATLAS-AGREEMENT-METADATA-REGISTER-v1.md) | Attested metadata roster |

| [ATLAS-AGREEMENT-METADATA-POPULATION-PLAN-v1.md](../population/ATLAS-AGREEMENT-METADATA-POPULATION-PLAN-v1.md) | Evidence evaluation per agreement |

| [ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md](../population/ATLAS-AGREEMENT-METADATA-ATTESTATION-v1.md) | Attestation methodology |

| [ATLAS-AGREEMENT-METADATA-ACTIVE-ATTESTATION-v1.md](../population/ATLAS-AGREEMENT-METADATA-ACTIVE-ATTESTATION-v1.md) | ACTIVE subset completeness act |

| [REPORT-atlas-agreement-metadata-layer-v1.md](../reports/REPORT-atlas-agreement-metadata-layer-v1.md) | Wave AGM-01 pass record |



---



*ATLAS Agreement Metadata Model v1 — Wave AGM-01. Operational metadata overlay only. Documentation only.*

