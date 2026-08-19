# FP-0003 — Project Passport

**Document type:** Factory Project passport (foundation)  
**Factory Project ID:** FP-0003  
**Project name:** OVERSEO  
**Domain:** overseo.ru  
**Date:** 2026-08-20  
**Charter:** FP-0003 Phase 0B — Project Registration + Materials Intake Skeleton  

---

## 1. Project identifiers

| Field | Value |
|-------|-------|
| Factory Project ID | **FP-0003** |
| Factory Project name | **OVERSEO** |
| Canonical LOC-ZONE name | **FP-0003-OVERSEO** |
| Primary hostname | **overseo.ru** |
| Intake slug | `overseo` |
| Population slice | **client_delivery** *(AUTHORIZED — operator intent)* |
| Current phase | **PHASE 0B** — Project registered / materials intake ready |

---

## Production mode

| Field | Value |
|-------|-------|
| production_mode | **PIXEL_PERFECT** |
| mode_declared_at | 2026-08-20 |
| mode_declared_by | Operator charter FP-0003 Phase 0B |
| mode_rationale | Site will be built against explicit operator-approved visual design targets generated screen-by-screen before frontend implementation. Frontend must reproduce approved visual targets rather than freely reinterpret them. Olga rough mockup = source material only until design wave produces approved targets. |
| mode_waivers | (none at registration) |

### mode_history[]

| # | from | to | at | by | report_ref |
|---|------|-----|-----|-----|------------|
| 1 | — | PIXEL_PERFECT | 2026-08-20 | Operator charter FP-0003 Phase 0B | [REPORTS/REPORT-OVERSEO-PHASE-0B-PROJECT-REGISTRATION.md](REPORTS/REPORT-OVERSEO-PHASE-0B-PROJECT-REGISTRATION.md) |

**Contract:** [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md)

---

## 2. ATLAS references

| Class | ID | Status |
|-------|-----|--------|
| ATLAS Project | — | **NOT YET CREATED** |
| ATLAS Website | — | **NOT YET CREATED** |
| ATLAS Domain | — | **NOT YET CREATED** |
| ATLAS Organization (client) | — | **NOT YET CREATED** |

**Binding status:** `ATLAS PROJECT/WEB/DOMAIN BINDING — NOT YET CREATED`

Future ATLAS population is a **separate bounded wave**. No ORG, PRJ, WEB, DOM, or REL records were minted in Phase 0B.

---

## 3. Coordinator / client context

| ID | Name | Role context | Evidence |
|----|------|--------------|----------|
| PER-0010 | Дягилева Ольга | Client coordination; materials intake; primary acceptance context | **VERIFIED** — [ATLAS-WAVE2-PERSON-ATTESTATION-v1.md](../../../projects/atlas/population/ATLAS-WAVE2-PERSON-ATTESTATION-v1.md) (PER-0010 **active**, E1) |

**Boundary:** PER-0010 is an **existing documented Person identity** referenced only. No Person ↔ Project edges minted for FP-0003 in this wave.

---

## 4. Canonical paths

| Role | Path | State |
|------|------|-------|
| LOC-ZONE | `X:\AI MARS\workspaces\website-factory-operations\FP-0003-OVERSEO\` | **ACTIVE** |
| Future frontend workspace | `X:\AI MARS\workspaces\fp-0003-overseo-v1\` | **NOT CREATED** |
| Future local runtime domain | `overseo.test` | **NOT CREATED** *(RECOMMENDED name)* |
| Storage bulk intake | `X:\AI MARS STORAGE\incoming\overseo.ru\` | **DOCUMENTED ONLY** |

---

## 5. Source-material intake model

| Stage | Location | Purpose |
|-------|----------|---------|
| Bulk drop | `X:\AI MARS STORAGE\incoming\overseo.ru\` | Large originals outside Git |
| Design promotion | `INCOMING/01_DESIGN/` | Mockups, screenshots, visual drafts |
| Notes | `INCOMING/07_NOTES/` | Telegram excerpts, coordination notes |
| Client materials | `INCOMING/08_CLIENT_MATERIALS/` | Briefs, content, brand materials |

Intake ≠ approval. Source materials ≠ approved design target.

---

## 6. Lifecycle intent

**AUTHORIZED sequence:**

Design → Gulp frontend → Forge WordPress → QA / launch / operations

Detailed flow documented in [README.md](README.md).

---

## 7. Implementation state

| Dimension | State |
|-----------|-------|
| Design implementation | **NOT STARTED** |
| Frontend implementation | **NOT STARTED** |
| WordPress implementation | **NOT STARTED** |
| Local runtime | **NOT STARTED** |
| Production intake | **NOT STARTED** |
| Factory manifest enrollment (ROC-01) | **NOT STARTED** |
| Factory registry enrollment | **NOT STARTED** |

---

## 8. Production / hosting (honesty)

| Dimension | State |
|-----------|-------|
| Production site state | **SAFE UNKNOWN** |
| Hosting provider | **SAFE UNKNOWN** |
| DNS | **SAFE UNKNOWN** |
| Current live CMS | **SAFE UNKNOWN** |

Do not infer production facts until Phase 1+ intake or verified operator evidence.

---

## 9. Validation lifecycle (display — optional)

| Field | Value |
|-------|-------|
| lifecycle_state | `—` |
| validation_status | `—` |

Not applicable until frontend/design validation waves begin.

---

## 10. Process precedent

**FP-0002 Shpigovsky.ru** — process precedent for lifecycle ordering and Factory discipline only. **Not** a template for OVERSEO implementation, assets, or architecture.

---

*Foundation passport only. No runtime. No ATLAS mutation in Phase 0B.*
