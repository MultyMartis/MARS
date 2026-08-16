# FP-0002 — Shpigovsky.ru

**Factory Project ID:** FP-0002  
**Project name:** Shpigovsky.ru  
**Workspace path:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`  
**Created:** 2026-06-11  
**Charter:** FP-0002 Foundation Initialization  

---

## ATLAS references

| Class | ID | Canonical name | State | Attestation |
|-------|-----|----------------|-------|-------------|
| Organization (commissioning) | ORG-0008 | ООО «Сознание» | **active** | AT-W1D-SHPIG-01 |
| Organization (execution) | ORG-0001 | Веб-студия «Полигон» | **active** | Wave 1 |
| Project | PRJ-0012 | Сайт shpigovsky.ru | **active** | AT-W3-SHPIG-01 |
| Website | WEB-SHPIG-01 | shpigovsky.ru | **active** | AT-W4-SHPIG-01 |
| Domain | DOM-SHPIG-01 | shpigovsky.ru | **active** | AT-W5-SHPIG-01 |

**Evidence sources:** EV-SHPIG-OP-01; EV-SHPIG-WEB-01; EV-SHPIG-WEB-02; AT-W1D-SHPIG-01  

**ATLAS register:** [projects/atlas/population/ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md](../../../projects/atlas/population/ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md)

---

## Project purpose

Client delivery production case for **shpigovsky.ru** under Polygon (ORG-0001) execution, commissioned by ORG-0008 **ООО «Сознание»**.

Documented delivery context (EV-SHPIG-OP-01):

- Population slice: **client_delivery**
- Channel: Polygon client delivery via Website Factory
- Planned stack signal: WordPress; possible ACF; possible custom programming *(scope not attested)*
- i-SEO project channel: **excluded**

This workspace is the **operational foundation** for the Factory track — not site production, not design, not WordPress architecture.

---

## Current phase

See [PROJECT-STATUS.md](PROJECT-STATUS.md). Production Beget host: `http://shpigovsky.beget.tech/` (`DNS_CUTOVER = DEFERRED` for `shpigovsky.ru`). Access contour: [DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md](DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md).

---

## Current status

See [PROJECT-STATUS.md](PROJECT-STATUS.md).

---

## Coordinator

| ID | Name | Role context (informational) |
|----|------|------------------------------|
| PER-0010 | Ольга Дягилева | Acquisition; client comms; coordination; SEO supervision; primary acceptance |

**Note:** Person ↔ Project edges are **not minted** in ATLAS Wave 3 scope (SU-SHPIG-PRJ-10). PER-0010 is an attested reference only.

---

## Linked entities

```text
ORG-0001 Полигон
    └── EXECUTES ──► PRJ-0012 Сайт shpigovsky.ru
                        └── COMMISSIONED_BY ──► ORG-0008 ООО «Сознание»
                                                    └── OWNS ──► WEB-SHPIG-01 shpigovsky.ru
                                                                      ▲
                                                                      │ PRIMARY_DOMAIN
                                                                  DOM-SHPIG-01 shpigovsky.ru
```

| Relationship | ID | State |
|--------------|-----|-------|
| PRJ-0012 → ORG-0008 COMMISSIONED_BY | REL-SHPIG-PJ-01 | **active** |
| ORG-0001 → PRJ-0012 EXECUTES | REL-SHPIG-PJ-02 | **active** |
| WEB-SHPIG-01 → PRJ-0012 BELONGS_TO | REL-SHPIG-WB-01 | **active** |
| ORG-0008 → WEB-SHPIG-01 OWNS | REL-SHPIG-WB-02 | **active** |
| DOM-SHPIG-01 → WEB-SHPIG-01 PRIMARY_DOMAIN | REL-SHPIG-DM-01 | **active** |

**Excluded:** ORG-0008 → DOM-SHPIG-01 **OWNS** — registrar evidence absent.

---

## SAFE UNKNOWN

Items **not** attested or **out of scope** at foundation stage — do not infer:

| Area | Status |
|------|--------|
| Delivery phase precision | **SAFE UNKNOWN** (EV-SHPIG-OP-01) |
| Contract / acceptance dates | **SAFE UNKNOWN** |
| ACF / custom programming scope | **SAFE UNKNOWN** (EFV-03 — not split into separate projects) |
| Site structure (pages, blocks, sitemap) | **SAFE UNKNOWN** — awaiting design intake |
| WordPress architecture | **SAFE UNKNOWN** — no design until mockups |
| Domain registrant (ORG → DOM OWNS) | **SAFE UNKNOWN** |
| Legal Entity Card | CC folder absent — deferred |
| Person ↔ Project formal edges | Not minted — PER-0010 reference only |

---

## Workspace index

| Path | Purpose |
|------|---------|
| [PROJECT-STATUS.md](PROJECT-STATUS.md) | Live status register |
| [DECISIONS.md](DECISIONS.md) | Architecture decision journal (ADR) |
| [CHANGELOG.md](CHANGELOG.md) | Project changelog |
| [FP-0002-PROJECT-PASSPORT.md](FP-0002-PROJECT-PASSPORT.md) | Project passport |
| [FP-0002-ONBOARDING-READINESS.md](FP-0002-ONBOARDING-READINESS.md) | Playbook onboarding checklist |
| [WORDPRESS-PRODUCTION-LEARNING-CHARTER.md](WORDPRESS-PRODUCTION-LEARNING-CHARTER.md) | Learning charter |
| [INCOMING/](INCOMING/) | Client and operator intake |
| [DELIVERABLES/](DELIVERABLES/) | Outbound deliverables (future) |
| [KNOWLEDGE-EXTRACTION/](KNOWLEDGE-EXTRACTION/) | Post-project learning containers |
| [REPORTS/](REPORTS/) | Execution reports |
| [FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md](FP-0002-PRODUCTION-STANDARDS-APPROVAL-v3.md) | Production Standards SSOT (approved) |
| [FP-0002-FRONTEND-START-SEQUENCE-v1.md](FP-0002-FRONTEND-START-SEQUENCE-v1.md) | Frontend foundation sequence |

---

*Human-operated Factory project workspace. No runtime. No automation.*
