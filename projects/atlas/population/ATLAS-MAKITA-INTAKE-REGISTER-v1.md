# ATLAS Makita Snab Intake Register v1

**Status:** **documented** — Organization intake register (pre-population).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-07  
**Intake slug:** `makita-snab`  
**Parent:** [ATLAS-MAKITA-INTAKE-ANALYSIS-v1.md](ATLAS-MAKITA-INTAKE-ANALYSIS-v1.md) · [ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md](ATLAS-EVIDENCE-FIRST-VALIDATION-RULE-v1.md) · [ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md](ATLAS-CARD-PRESENCE-VALIDATION-RULE-v1.md)  
**Is not:** canonical Organization registry, attested export, `ORG-*` / `WEB-*` / `DOM-*` assignment.

---

## 1. Register summary

| Metric | Count |
|--------|-------|
| Organization intake candidates | **1** |
| Person intake candidates *(reference)* | **1** |
| Website asset candidates | **2** |
| Domain asset candidates | **2** |
| Relationships created | **0** |
| Projects created | **0** |
| `ORG-*` assigned | **0** |
| Counterparty Card files | **0** |
| Evidence tier (intake) | **E0** |

---

## 2. Organization intake candidates

| intake_label | org_slug | proposed_display_name | wave_tier *(target)* | business_role *(target)* | legal_entity | org_id | evidence_tier | evidence_ref | lifecycle | intake_verdict |
|--------------|----------|----------------------|----------------------|--------------------------|--------------|--------|---------------|--------------|-----------|----------------|
| MAKITA-INTAKE-CAND-O01 | makita-snab | **Макита Снаб** | W1-B *(proposed)* | CLIENT | **SAFE UNKNOWN** | **none** | **E0** | EV-MAKITA-OP-01 | **intake** | **Hold — CC required** |

**CC requirement:**

| Field | Value |
|-------|-------|
| Required path | `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\makita-snab\` |
| Filesystem state (2026-06-07) | **Absent** |
| CPV status | Inventory complete — **0** non-placeholder files |

---

## 3. Person intake candidates *(reference — not minted)*

| intake_label | proposed_name | role_signal | phone | email / tg | person_id | evidence_ref | intake_verdict |
|--------------|---------------|-------------|-------|------------|-----------|--------------|----------------|
| MAKITA-INTAKE-CAND-P01 | **Артём** *(given name only)* | operational owner / primary contact | 8-926-022-30-91 | **SAFE UNKNOWN** | **none** | EV-MAKITA-OP-01 | **Hold** — full name unknown |

---

## 4. Candidate Website assets

| intake_label | hostname | url | org_binding | web_id | evidence_ref | intake_verdict |
|--------------|----------|-----|-------------|--------|--------------|----------------|
| MAKITA-INTAKE-WEB-C01 | makita-snab.ru | https://makita-snab.ru/ | **SAFE UNKNOWN** | **none** | EV-MAKITA-OP-01; EV-MAKITA-OP-02 | **Candidate — Wave 4** |
| MAKITA-INTAKE-WEB-C02 | makita-land.ru | https://makita-land.ru/ | **SAFE UNKNOWN** | **none** | EV-MAKITA-OP-01; EV-MAKITA-OP-02 | **Candidate — Wave 4** |

**Explicit:** Do **not** mint `WEB-*` at intake.

---

## 5. Candidate Domain assets

| intake_label | domain | derived_from | dom_id | evidence_ref | intake_verdict |
|--------------|--------|--------------|--------|--------------|----------------|
| MAKITA-INTAKE-DOM-C01 | makita-snab.ru | MAKITA-INTAKE-WEB-C01 | **none** | EV-MAKITA-OP-01 | **Candidate — Wave 5** |
| MAKITA-INTAKE-DOM-C02 | makita-land.ru | MAKITA-INTAKE-WEB-C02 | **none** | EV-MAKITA-OP-01 | **Candidate — Wave 5** |

**Explicit:** Do **not** mint `DOM-*` at intake.

---

## 6. Operational context register *(informational — no edges)*

| Field | Value | evidence_ref |
|-------|-------|--------------|
| SEO vendor | i-SEO (ORG-0003) — **SEO on both websites** | EV-MAKITA-OP-01; EV-MAKITA-OP-03 |
| Service context | **SEO** (i-SEO) · **Yandex Direct** (steward) | EV-MAKITA-OP-03 |
| Steward scope | Yandex Direct activities only | EV-MAKITA-OP-01 |
| Steward exclusion | Contracts, accounting, **document flow** — **not** managed by steward | EV-MAKITA-OP-01; EV-MAKITA-OP-03 |
| Direct communication | Steward ↔ contact **Артём** | EV-MAKITA-OP-01 |

**No REL-* created.** CLIENT_OF / VENDOR_OF deferred to Wave 6+ after Organization anchor.

---

## 7. Evidence index

| Ref | Artifact | Tier |
|-----|----------|------|
| EV-MAKITA-OP-01 | Steward intake inputs (2026-06-07) | **E0** |
| EV-MAKITA-OP-02 | Steward statement — websites exist | **E0** |
| EV-MAKITA-OP-03 | Intake enrichment pass — operational reality | **E0** |
| *(pending)* | Counterparty Card — `…\makita-snab\` | **E1+ expected** |

---

## 8. Duplicate review index

| review_id | verdict | register impact |
|-----------|---------|-----------------|
| MAKITA-D-01..06 | **Distinct** vs ORG-0001..0006 | No merge |
| MAKITA-D-07 | **Distinct** hostname vs BZPM/SIBCAR | No merge |
| MAKITA-D-08 | ORCA pilot ≠ Organization | Excluded |
| INN/OGRN cross-check | **Open** — CC absent | Blocks **Pass** |

**Duplicate review summary:** **Open — low** (trade-name / global brand); **cannot Pass** on legal identity until CC.

**Integrity checks:** ZPM **Pass** · SIBCAR **Pass** · No merge **Pass**

---

## 9. SAFE UNKNOWN index

| id | topic | blocks_intake |
|----|-------|---------------|
| SU-MAKITA-01 | Legal entity form | **Yes** |
| SU-MAKITA-02 | INN / KPP / OGRN | **Yes** |
| SU-MAKITA-03 | Legal vs trade name | **Yes** |
| SU-MAKITA-04 | Full name — Артём | **No** |
| SU-MAKITA-05 | Contact email / Telegram | **No** |
| SU-MAKITA-06 | Primary website | **No** |
| SU-MAKITA-07 | Commercial edges | **No** |
| SU-MAKITA-08 | Steward ↔ client commercial edge | **No** |
| SU-MAKITA-09 | Contract ownership | **No** |
| SU-MAKITA-10 | Live site verification | **No** |
| SU-MAKITA-11 | Document-flow ownership | **No** |

---

## 10. Readiness summary

| Gate | Status |
|------|--------|
| Intake register complete | **Pass** |
| Intake enrichment complete | **Pass** — see [ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md) |
| EFV / CPV applied | **Pass** |
| CC folder inventory | **Pass** — documented absent |
| Organization population | **Blocked** |
| **Overall** | **PARTIALLY READY** |

---

## 11. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-MAKITA-INTAKE-ANALYSIS-v1.md](ATLAS-MAKITA-INTAKE-ANALYSIS-v1.md) | Full analysis |
| [ATLAS-MAKITA-INTAKE-SUMMARY-v1.md](ATLAS-MAKITA-INTAKE-SUMMARY-v1.md) | Summary |
| [ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md](ATLAS-MAKITA-INTAKE-ENRICHMENT-v1.md) | Operational enrichment |

---

*ATLAS Makita Snab Intake Register v1 — pre-population intake only.*
