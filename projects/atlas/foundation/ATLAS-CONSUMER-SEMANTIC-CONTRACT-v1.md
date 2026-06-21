# ATLAS Consumer Semantic Contract v1

**Status:** **documented** — Phase 6 mandatory interpretation contract (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-CONSUMER-ADOPTION-MODEL-v1.md](ATLAS-CONSUMER-ADOPTION-MODEL-v1.md)  
**Upstream:** Phases 1–5 foundation (lifecycle, relationships, identity, attestation)  
**Is not:** API field schema, i18n catalog, consumer UI copy standard.

**Phase 1–5 constraint:** No changes to approved Phase 1–5 documents unless contradictions are discovered. None identified at Phase 6 authoring.

---

## 1. Purpose

Define the **mandatory interpretation contract** — normative rules ensuring every consumer assigns the **same meaning** to ATLAS vocabulary.

**Contract statement:**

> If two consumers read the same ATLAS record, they **must** draw the same conclusions about canonical posture, relationship semantics, identity stability, and attestation trust — or explicitly halt at **SAFE UNKNOWN**.

---

## 2. Contract scope

| In scope | Out of scope |
|----------|--------------|
| Lifecycle state semantics | Consumer workflow labels |
| Relationship type semantics | CRM picklist values |
| Identity and redirect rules | Display fonts / colors |
| Attestation outcomes | Evidence storage technology |
| SAFE UNKNOWN posture | Business Scope taxonomy (future) |

---

## 3. Lifecycle state interpretation

Authoritative codes: [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md).

### 3.1 Universal core — normative meanings

| Code | **ACTIVE means the same everywhere** | Forward canonical? | Consumer must |
|------|--------------------------------------|-------------------|---------------|
| **proposed** | Candidate claim; **not** trusted canonical | **No** | Show “pending attestation”; block irreversible structural commits |
| **active** | Human-attested current structural truth | **Yes** (if C-01–C-06) | Use id in durable cross-system references |
| **disputed** | Contested; promotion blocked | **No** | Stop auto-linking; surface dispute |
| **deprecated** | Structural claim ended; historical retained | **No** forward default | Prefer successor/redirect; historical queries OK |
| **archived** | Long-term read-only tomb | **No** | Read-only; no structural edits via consumer |

**Rule SC-L01:** **ACTIVE** (registry code `active`) means **“attested canonical structural truth now”** — not “project is running”, “site is live”, “campaign is enabled”.

**Rule SC-L02:** Consumer “active” flags (user account enabled, ad group enabled) are **orthogonal** — must not be persisted as ATLAS lifecycle codes.

### 3.2 Facet states — normative meanings

| Code | Applies to | Meaning (uniform) | Consumer must |
|------|------------|-------------------|---------------|
| **merged** | Entity ids | Absorbed id; survivor in `redirect_to` | Resolve to survivor for forward use |
| **split_source** | Entity ids | Origin after split; children documented | Do not treat as current canonical subject |
| **replaced** | Relationships | Superseded edge; successor in `replaced_by` | Follow successor for current link |

**Rule SC-L03:** **merged** on entities ≠ **replaced** on relationships — never interchange codes.

### 3.3 Forbidden reinterpretations

| Consumer mistake | Correction |
|------------------|------------|
| “Our project is active” ⇒ ATLAS **active** | Map via Mapping Rules; ops “active” ≠ ATLAS **active** |
| CRM “closed won” ⇒ **deprecated** | Requires ATLAS attest to end structural claim |
| “Deleted” ⇒ remove ATLAS row | Use **deprecated** / **merged** / **archived** |
| “Unknown customer” ⇒ **proposed** row | Use **SAFE UNKNOWN** posture without inventing entity |

### 3.4 Display synonyms (allowed, non-normative)

Consumers **may** label in UI:

| ATLAS code | Example display (any language) | Must not persist as code |
|------------|-------------------------------|----------------------------|
| active | Canonical · Verified | `live`, `verified` |
| deprecated | Ended · Historical | `closed`, `inactive` |
| disputed | Contested | `conflict` |
| merged | Absorbed | `deleted` |

Crosswalk: [ATLAS-LIFECYCLE-CROSSWALK-v1.md](ATLAS-LIFECYCLE-CROSSWALK-v1.md) §9.

---

## 4. Relationship type interpretation

Authoritative types: [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md).

### 4.1 Normative rule

**Rule SC-R01:** Relationship type codes are **closed vocabulary** for consumers. Localization does not change direction or family.

**Rule SC-R02:** **CLIENT_OF means the same everywhere:**

> Subject **Organization** is a **client** of object **Organization** in an attested **commercial service relationship** (structural), not a CRM deal stage, not a marketing segment, not a support ticket category.

**Rule SC-R03:** **OWNER means the same everywhere:**

> Subject **Person** has **ownership stake or ultimate control** attested for object **Organization** — not WordPress site admin, not CRM “account owner”, not DNS registrant contact alone.

### 4.2 High-traffic types — uniform interpretation

| Type | Direction | Uniform meaning | Not equivalent to |
|------|-----------|-----------------|-------------------|
| **CLIENT_OF** | Org → Org | Client–vendor structural link | Lead, opportunity, subscriber |
| **OWNER** | Person → Org | Ownership / ultimate control | Site admin, billing contact |
| **EMPLOYEE** | Person → Org | Structural employment | Payroll status |
| **REPRESENTATIVE** | Person → Org | Authorized external representation | Support agent assignment |
| **OWNS** | Org → Project | Org owns initiative structurally | PM “owner” field |
| **EXECUTES** | Org → Project | Delivery org for project | Sprint team membership |
| **COMMISSIONED_BY** | Project → Org | Client/sponsor commissioning project | Invoice paid |
| **OPERATES** | Org → Website | Operating org for site | Hosting panel login |
| **REGISTERED_TO** | Domain → Org | Structural registration subject | DNS A-record operator |

### 4.3 FORMER_* types

**Rule SC-R04:** `FORMER_CLIENT_OF`, `FORMER_EMPLOYEE`, etc. indicate **ended structural role** with historical truth — not “inactive user account”.

### 4.4 Relationship lifecycle coupling

Relationship records use the same lifecycle codes as entities where applicable, plus **replaced** ([ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) §4.3).

**Rule SC-R05:** An **active** `CLIENT_OF` with valid effective dates means the commercial link is **structurally current** — independent of consumer project status.

---

## 5. Identity interpretation

Sources: [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) · [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md) · [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md).

| Concept | Uniform meaning | Consumer must |
|---------|-----------------|---------------|
| **Stable id** | Permanent `ORG-*`, `PER-*`, etc. | Never recycle locally as different entity |
| **Canonical name** | Attested display default | Not durable primary key |
| **Alias** | Alternate label; governance per alias model | May show alias; cite canonical id |
| **merged redirect** | Loser id → survivor | Rewrite foreign keys on notification |
| **split_source** | Origin id after split | Map children explicitly |

**Rule SC-I01:** **canonical** (adjective) means **C-01–C-06 satisfied** — not “preferred locally” or “most recent import”.

**Rule SC-I02:** Display name collision does not imply identity merge.

---

## 6. SAFE UNKNOWN interpretation

**SAFE UNKNOWN** is a **registry posture** at a subject or relationship **slot** — not a lifecycle state ([ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) §7).

| SC-ID | Rule |
|-------|------|
| **SC-U01** | UNKNOWN means **no active canonical** claim is attested for the fact |
| **SC-U02** | UNKNOWN ≠ “we have not checked yet” as excuse to invent ids |
| **SC-U03** | UNKNOWN ≠ **proposed** — zero rows may exist |
| **SC-U04** | Consumers must surface UNKNOWN to operators before irreversible structural acts |
| **SC-U05** | Market-only evidence (MIG) does not clear UNKNOWN without business attestation |

**Normative sentence:**

> **SAFE UNKNOWN** means “ATLAS does not attest this structural fact as canonical now” — consumers must not fill the gap with local canonical invention.

---

## 7. Attestation outcome interpretation

Source: [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md).

| Outcome | Consumer interpretation |
|---------|-------------------------|
| **Attested → active** | Structural claim approved; may use in forward canonical references |
| **Rejected proposal** | No canonical row; remain UNKNOWN or delete proposal only |
| **Dispute opened** | Treat slot as non-canonical until resolution |
| **Merge approved** | Loser **merged**; survivor **active** |
| **Evidence insufficient** | Remain **proposed** or UNKNOWN — no promotion |

**Rule SC-A01:** Attestation is **human structural approval** — not contract signed, not invoice paid, not deploy green.

**Rule SC-A02:** Evidence tier (E0–E3) informs **risk display** for operators; consumers must not downgrade tier locally to force promotion.

**Rule SC-A03:** MIG market evidence may support **proposal** only (AT-E-03).

---

## 8. Disputed and deprecated — special semantics

### 8.1 disputed

| Aspect | Uniform rule |
|--------|--------------|
| Meaning | Competing or insufficient claims |
| Canonical? | **Never** |
| Consumer action | Halt forward joins; offer challenge/dispute flag |

### 8.2 deprecated

| Aspect | Uniform rule |
|--------|--------------|
| Meaning | Structural end; audit kept |
| Forward use? | **No** default |
| Consumer action | Use successor; historical reporting allowed |

**Rule SC-L04:** **deprecated** does not mean “hidden from UI” — it means **ended structural truth**.

---

## 9. Canonical interpretation checklist

Consumers certify semantic compliance ([ATLAS-CONSUMER-CERTIFICATION-v1.md](ATLAS-CONSUMER-CERTIFICATION-v1.md)) by verifying:

- [ ] Only Phase 5 lifecycle codes stored in ATLAS-shaped fields
- [ ] **active** never used for operational workflow
- [ ] **CLIENT_OF** / **OWNER** not overloaded with CRM roles
- [ ] **merged** / **replaced** redirects implemented in reference layer
- [ ] SAFE UNKNOWN explicit in charters and UX copy
- [ ] No consumer code path auto-attests to **active**

---

## 10. Examples — correct vs incorrect

### 10.1 ACTIVE

| Context | Correct | Incorrect |
|---------|---------|-----------|
| ATLAS `ORG-123` lifecycle **active** | “Canonical org exists” | “Org is trading today” |
| WPilot deploy pipeline **active** | Local ops state only | Write `active` to ATLAS |

### 10.2 CLIENT_OF

| Correct | Incorrect |
|---------|-----------|
| Agency Org A **CLIENT_OF** Client Org B (attested) | CRM “Customer” tag on deal |
| Ends with **deprecated** + optional FORMER_* | Deal lost ⇒ auto **deprecated** without attest |

### 10.3 OWNER

| Correct | Incorrect |
|---------|-----------|
| Person **OWNER** Org (attested control) | WordPress `administrator` role ⇒ **OWNER** |
| Multiple attested OWNER allowed | Single CRM owner field ⇒ canonical OWNER |

---

## 11. Contract versioning

Amendments to this contract follow [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) **S4** (vocabulary / consumer-facing semantics).

Consumers must re-certify at least at **C1** when SC-* rules change.

---

*ATLAS Consumer Semantic Contract v1 — Phase 6 Foundation. Documentation only.*
