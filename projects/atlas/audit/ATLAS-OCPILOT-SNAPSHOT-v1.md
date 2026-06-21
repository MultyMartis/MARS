# ATLAS ↔ OCPilot Relationship Snapshot v1

**Status:** **documented** — current-state snapshot (read-only).  
**Date:** 2026-06-07  
**Scope:** ATLAS · OCPilot · SITE-001 (SIBCAR)  
**Sources:** [ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md](ATLAS-OCPILOT-SIBCAR-CROSSWALK-AUDIT-v1.md) · [ATLAS-CONSUMER-CONTRACTS-v1.md](../foundation/ATLAS-CONSUMER-CONTRACTS-v1.md) · [SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](../../ocpilot/sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) · [OCPILOT-STATE.md](../../ocpilot/OCPILOT-STATE.md)  
**Is not:** integration design, roadmap, or implementation spec.

---

## 1. Current ATLAS → OCPilot integration model

**Documentation-level adoption only** — no live ATLAS API, sync, or runtime integration is claimed in-repo.

| Layer | Role |
|-------|------|
| **ATLAS** | Canonical business reality: Organization, Legal Entity, Project, Website, Domain, Relationships |
| **OCPilot** | Operational execution: `SITE-001` workspace (audit runs, access brief, snapshots, change governance) |
| **Crosswalk** | **Documentation linkage only** — not graph edges; Atlas registers carry `ocpilot_crosswalk: SITE-001`; OCPilot intake lacks full back-links |

**Ecosystem posture:** OCPilot is an **adjacent CMS-ops consumer** ([OPS-ECOSYSTEM-RELATIONSHIPS-v1.md](../../ops/foundation/OPS-ECOSYSTEM-RELATIONSHIPS-v1.md) §3.8). Evidence for site audit flows **separately** via EAR: `Operator → EAR → Published Snapshot → OCPilot` — OCPilot does not acquire live site evidence when a snapshot path is chartered ([EAR-OCPILOT-INTEGRATION-v1.md](../../../shared/external-access-runtime/EAR-OCPILOT-INTEGRATION-v1.md)).

**SIBCAR mapping (attested):** ORG-0006 · LE-0005 · PRJ-0011 · WEB-SIBCAR-01 ↔ SITE-001 — **same client, same engagement, same TEST deployment** (`sibcar.new-site.space`).

---

## 2. What data OCPilot is allowed to consume from ATLAS

Per [ATLAS-CONSUMER-CONTRACTS-v1.md](../foundation/ATLAS-CONSUMER-CONTRACTS-v1.md) §8.4 (WPilot / OCPilot):

| Permitted | Prohibited |
|-----------|------------|
| **Read / reference:** `WEB-*`, `ORG-*` for site context; L0–L2 depth (ids, display names, aliases, structural relationships) | Mint parallel canonical org/legal/project/website records |
| **Suggest:** site-title alias; flag wrong org link | Treat CMS state (posts, orders, users) as ATLAS entities |
| **Cite attested fields** in authorization / planning reports (e.g. LE-0005 in change-auth review) | Silent overwrite or auto-attest of ATLAS structure |

**Observed for SITE-001:** Legal identifiers (INN, OGRN, KPP) and legal name exist **only in ATLAS** (LE-0005); OCPilot passport/registry correctly omit them. Trade title «Автосалон СИБКАР» is OCPilot display context — not an org alias in ATLAS.

---

## 3. May legal entity data for SITE-001 be sourced from ATLAS?

**Yes — for drafting and planning only**, from attested **LE-0005** / evidence **EV-W1C-CC-01** (E1 counterparty card).

| Field | ATLAS status | OCPilot use |
|-------|--------------|-------------|
| Legal name, INN, OGRN, KPP, address | **active** — AT-W1C-01 | Legal-block text in Brand Replacement Pack |
| Phones, messengers | **SAFE UNKNOWN** in ATLAS | **Not** sufficient from ATLAS alone — operator must supply |
| On-site legal block locations | N/A in ATLAS | **SAFE UNKNOWN** until W0 discovery |

**Not sufficient alone for on-site execution** — Phase 1 decision records C-DEC-OK-04 (Atlas source for drafting) as satisfied; write execution remains blocked on other gates.

---

## 4. Approval gates before using ATLAS data on SITE-001

| Gate | Status | Notes |
|------|--------|-------|
| ATLAS attestation | **Satisfied** for LE-0005, ORG-0006, PRJ-0011, WEB-SIBCAR-01 | DOM-SIBCAR-01 still **proposed** (Wave 5 pending) — not a Phase 1 blocker |
| ATLAS → OCPilot crosswalk | **Pass with findings** (2026-06-07) | Doc drift only; no separate ATLAS approval required to *read* attested fields |
| **Phase 1 Brand Replacement execution** | **NOT AUTHORIZED** | [SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md](../../ocpilot/sites/site-001/reports/SITE-001-CHANGE-AUTHORIZATION-DECISION-v1.md) |
| OCPilot write charter | **NO** | project-access-brief write flags closed; AUDIT-CHARTER read-only |
| Pre-execution checklist C-01..C-11 | **IN PROGRESS** | Brand pack, grep baseline, logos, contacts, backup, Change Request + Rollback Plan |
| EAR Dry Run (2026-06-07) | PASS WITH NOTES | **Does not** authorize CMS writes or live SFTP |

Using ATLAS legal data **in documentation/checklists** is allowed now; **applying it to the live TEST site** requires Phase 1 re-decision (**AUTHORIZED WITH NOTES** v1.1) after checklist completion.

---

## 5. Do recent architecture changes affect SITE-001 Phase 1 Brand Replacement?

| Change (2026-06-07) | Effect on Phase 1 |
|---------------------|-------------------|
| ATLAS SIBCAR Waves 3–4 (PRJ-0011, WEB-SIBCAR-01 **active**) | **Clarifies** engagement/deployment crosswalk — does not authorize writes |
| ATLAS ↔ OCPilot crosswalk audit | **Confirms** identity alignment — **no structural block** |
| Phase 1 authorization review + **NOT AUTHORIZED** decision | **Direct gate** — execution blocked until checklist |
| EAR dry run + Store≠Publish separation | Reinforces evidence path; **does not** substitute for write authorization |
| Run 5 **paused** (no published snapshot) | Overlaps W0 discovery needs; **does not** auto-block Phase 1 but leaves site inventory **SAFE UNKNOWN** |

**Net:** Recent ATLAS population and crosswalk work **support** Phase 1 planning (legal source, identity clarity) but **do not unlock** execution. The binding change is the **NOT AUTHORIZED** Phase 1 decision, not ATLAS Foundation amendment.

---

## 6. Blockers, conflicts, SAFE UNKNOWN

**Blockers (execution):** Phase 1 **NOT AUTHORIZED**; write gates closed; no Brand Replacement Pack v1; no old-brand grep baseline; logos unstaged; contacts incomplete; no fresh verified backup; no Change Request / Rollback Plan; Run 5 paused (no published EAR snapshot).

**Conflicts:** **None** in business identity — crosswalk audit verdict **PASS WITH FINDINGS**; no duplicate org/project/deployment; no ownership inversion.

**SAFE UNKNOWN:**

| Item | Both systems |
|------|--------------|
| Production public URL | Unknown — ME-W1C-02 |
| ATLAS records on live runtime service | Documentation-level only |
| Old-brand strings on TEST site | Not captured in repo |
| Phones / messengers for SIBCAR | Not in ATLAS CC; not in OCPilot pack |
| Run 5 resume date | Not specified |

**Non-blocking findings:** missing OCPilot→Atlas back-links (FINDING-XW-SIBCAR-01); Run 5 status doc drift (FINDING-XW-SIBCAR-02); W1C-D-05 naming variant; DOM-SIBCAR-01 attestation pending.

---

*ATLAS ↔ OCPilot Relationship Snapshot v1 — current state only.*
