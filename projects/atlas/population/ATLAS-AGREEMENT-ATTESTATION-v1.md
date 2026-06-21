# ATLAS Agreement Attestation v1

**Status:** **attested** — Wave AGL-01 Agreement Layer attestation methodology and act.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-10  
**Wave:** AGL-01 — Agreement Layer Foundation  
**Attestor role:** Registry Steward (delegated) · Program Owner confirmation  
**Parent:** [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) · [ATLAS-AGREEMENT-REALITY-MODEL-v1.md](../foundation/ATLAS-AGREEMENT-REALITY-MODEL-v1.md) · [ATLAS-AGREEMENT-POPULATION-PLAN-v1.md](ATLAS-AGREEMENT-POPULATION-PLAN-v1.md)  
**Is not:** runtime, API, database export, contract ingestion, Foundation amendment to MVP six.

---

## 1. Attestation act

По [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) §1:

> Nothing is canonical until a qualified human attests under documented evidence discipline.

Настоящий акт фиксирует **каноническую attestation** Wave AGL-01: **8** Agreement records переведены в attested register state — **6 ACTIVE**, **2 EXPIRED**.

**Scope of this act:**

| In scope | Out of scope |
|----------|--------------|
| Agreement entity registration (documentation) | Contract text / PDF storage |
| Project-scoped commercial reality anchors | Legal signature workflow |
| Status ACTIVE / EXPIRED from project lifecycle | Accounting / invoice fields |
| Evidence tier assignment E0–E1 | Runtime / API / registry file changes |
| SAFE UNKNOWN for dates | Invented contract dates |

**Binding operator corrections (enforced):**

- Agreement = **business reality anchor**, not legal contract clone.
- Default granularity: **one agreement per attested Project delivery stream**.
- **ORG-0007 Makita:** no Agreement rows — evidence insufficient.
- **start_date / end_date:** **SAFE UNKNOWN** unless E2+ date pointer attested — no fabrication.

---

## 2. Attestation methodology

### 2.1 Minimum admission checklist (AGR-AT-01)

An Agreement **must** satisfy **all** rows to enter register:

| # | Requirement | Failure posture |
|---|-------------|-----------------|
| 1 | `client_org` — attested Organization **active** | **SAFE UNKNOWN** — no row |
| 2 | `vendor_org` — attested Organization **active** | **SAFE UNKNOWN** — no row |
| 3 | `scope_summary` — non-empty, evidence-backed | **SAFE UNKNOWN** — no row |
| 4 | `status` — ACTIVE, EXPIRED, or PLANNED | UNKNOWN → no row |
| 5 | `agreement_type` — from controlled vocabulary | Infer only from attested project scope |
| 6 | `related_projects` — ≥1 attested `PRJ-*` | **SAFE UNKNOWN** — no row |
| 7 | Paired **COMMISSIONED_BY** + **EXECUTES** for project | **SAFE UNKNOWN** — no row |
| 8 | `evidence_level` — E0 minimum; E1 when CC/commercial ref exists | No fabricated tier |
| 9 | No contract text stored | Pointer refs only |

### 2.2 Status derivation rules

| Project lifecycle | Agreement status | Rule |
|-------------------|------------------|------|
| **active** | **ACTIVE** | AGR-ST-01 — ongoing delivery |
| **deprecated** | **EXPIRED** | Completed delivery phase — not date inference |
| No project | **PLANNED** only | Requires explicit future-scope attestation — none in AGL-01 |
| Insufficient graph | — | **Do not register** |

### 2.3 Type derivation rules

| Signal | agreement_type |
|--------|----------------|
| Project canonical name contains «SEO» | SEO_RETAINER |
| Web build / platform / landing delivery | DEVELOPMENT |
| Attested PPC-only scope with project | PPC_RETAINER |
| Multiple lines under one attested umbrella | MIXED |
| Ambiguous | OTHER + explicit scope_summary |

### 2.4 Evidence tier assignment

| Tier | When assigned (AGL-01) |
|------|------------------------|
| **E1** | Triumph projects — E1 dataset + EV-0005 + Wave 3B E1 edges |
| **E0** | ZPM / SIBCAR — operator attestation + E0 project edges + CC where present |
| **E2+** | **Not used** in AGL-01 — no contract date extract attested |

### 2.5 Relationship to CLIENT_OF

CLIENT_OF (org↔org) **corroborates** parties but **does not alone** justify Agreement row. Required: project scope + COMMISSIONED_BY / EXECUTES pair + status derivation.

---

## 3. Attestation tranches executed

| Tranche | Agreements | Basis | Outcome |
|---------|------------|-------|---------|
| **AT-AGL-01** | AGR-0001 | PRJ-0004 deprecated; REL-0017/0018; REL-0016; E1 | **EXPIRED** |
| **AT-AGL-02** | AGR-0002 | PRJ-0005 active; REL-0019/0020; REL-0016; E1 | **ACTIVE** |
| **AT-AGL-03** | AGR-0003 | PRJ-0006 active; SEO scope; REL-0021/0022; E1 | **ACTIVE** |
| **AT-AGL-04** | AGR-0004 | PRJ-0007 active; REL-0023/0024; E1 | **ACTIVE** |
| **AT-AGL-05** | AGR-0005 | PRJ-0008 active; REL-0025/0026; WF-01 pilot; E1 | **ACTIVE** |
| **AT-AGL-06** | AGR-0006 | PRJ-0009 active; REL-ZPM-PJ-01/02; REL-0040; E0 | **ACTIVE** |
| **AT-AGL-07** | AGR-0007 | PRJ-0010 deprecated; REL-ZPM-PJ-03/04; E0 | **EXPIRED** |
| **AT-AGL-08** | AGR-0008 | PRJ-0011 active; REL-SIBCAR-PJ-01/02; REL-0041; E0 | **ACTIVE** |

---

## 4. Per-agreement attestation records

### 4.1 AGR-0001 — Triumph / Редизайн (EXPIRED)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0001 |
| **client_org** | ORG-0004 Триумф |
| **vendor_org** | ORG-0001 Полигон |
| **related_projects** | PRJ-0004 |
| **attestation_basis** | PRJ-0004 **deprecated**; REL-0017 COMMISSIONED_BY + REL-0018 EXECUTES **active**; REL-0016 CLIENT_OF; E1 dataset + EV-0005 |
| **evidence_level** | **E1** |
| **status** | **EXPIRED** |
| **notes** | LT-P01 historical pattern — structural truth preserved |

### 4.2 AGR-0002 — Triumph / Грузотакси (ACTIVE)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0002 |
| **attestation_basis** | PRJ-0005 **active**; REL-0019/0020; REL-0016; WEB-0008; E1 |
| **evidence_level** | **E1** |
| **status** | **ACTIVE** |

### 4.3 AGR-0003 — Triumph / SEO (ACTIVE)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0003 |
| **agreement_type** | SEO_RETAINER |
| **attestation_basis** | PRJ-0006 **active**; project identity «SEO gktriumph.ru»; REL-0021/0022; E1 |
| **evidence_level** | **E1** |
| **status** | **ACTIVE** |

### 4.4 AGR-0004 — Triumph / Блог (ACTIVE)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0004 |
| **attestation_basis** | PRJ-0007 **active**; REL-0023/0024; WEB-0007; E1 |
| **evidence_level** | **E1** |
| **status** | **ACTIVE** |

### 4.5 AGR-0005 — Triumph / Манипулятор (ACTIVE)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0005 |
| **attestation_basis** | PRJ-0008 **active**; REL-0025/0026; WEB-0009; OPS WF-01 live binding contour; E1 |
| **evidence_level** | **E1** |
| **status** | **ACTIVE** |
| **notes** | Closes WF-01 agreement binding gap for PRJ-0008 at documentation layer |

### 4.6 AGR-0006 — ZPM / Каталог-платформа (ACTIVE)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0006 |
| **attestation_basis** | PRJ-0009 **active**; AT-W3-ZPM-01; REL-ZPM-PJ-01/02; REL-0040; EV-ZPM-OP-ACT-01; EV-W1B-CC-01 |
| **evidence_level** | **E0** |
| **status** | **ACTIVE** |

### 4.7 AGR-0007 — ZPM / Исходный сайт (EXPIRED)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0007 |
| **attestation_basis** | PRJ-0010 **deprecated**; AT-W3-ZPM-02; REL-ZPM-PJ-03/04; EV-ZPM-OP-HIST-01; LT-P01 |
| **evidence_level** | **E0** |
| **status** | **EXPIRED** |

### 4.8 AGR-0008 — SIBCAR / OpenCart dealership (ACTIVE)

| Field | Value |
|-------|-------|
| **agreement_id** | AGR-0008 |
| **attestation_basis** | PRJ-0011 **active**; AT-W3-SIBCAR-01; REL-SIBCAR-PJ-01/02; REL-0041; EV-W1C-CC-01; EV-OCP-01..04 |
| **evidence_level** | **E0** |
| **status** | **ACTIVE** |

---

## 5. Rejected candidates (attestation declined)

| Candidate | Reason | Posture |
|-----------|--------|---------|
| ORG-0007 Makita SEO agreement | No Project; no CLIENT_OF; CC absent | **SAFE UNKNOWN** |
| ZPM FUT-01 SEO | No PRJ-* | **SAFE UNKNOWN** |
| Triumph umbrella AGR | Legal boundary unknown | **Deferred** |
| Any row with invented dates | AT-E-05 violation | **Rejected** |

---

## 6. Governance compliance

| Check | Result |
|-------|--------|
| ATLAS-BOUNDARIES — no contract storage | **Pass** |
| Evidence First — no fabricated tiers | **Pass** |
| OPS-ATLAS-ALIGNMENT — C-07 structural registration | **Pass** |
| No runtime / registry / topology changes | **Pass** |
| Makita — no guessing | **Pass** |

---

## 7. Related documents

| Document | Role |
|----------|------|
| [ATLAS-AGREEMENT-REGISTER-v1.md](ATLAS-AGREEMENT-REGISTER-v1.md) | Canonical roster |
| [ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md](ATLAS-AGREEMENT-ACTIVE-ATTESTATION-v1.md) | ACTIVE subset act |
| [ATLAS-AGREEMENT-POPULATION-PLAN-v1.md](ATLAS-AGREEMENT-POPULATION-PLAN-v1.md) | Readiness source |

---

*ATLAS Agreement Attestation v1 — Wave AGL-01. Methodology and attestation act.*
