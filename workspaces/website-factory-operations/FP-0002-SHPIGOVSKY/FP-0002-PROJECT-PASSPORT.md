# FP-0002 — Project Passport

**Document type:** Factory Project passport (foundation)  
**Factory Project ID:** FP-0002  
**Project name:** Shpigovsky.ru  
**Date:** 2026-06-11  
**Charter:** FP-0002 Foundation Initialization  

---

## 1. Project identifiers

| Field | Value |
|-------|-------|
| Factory Project ID | **FP-0002** |
| Factory Project name | **Shpigovsky.ru** |
| ATLAS Project ID | **PRJ-0012** |
| ATLAS Project name | Сайт shpigovsky.ru |
| Intake slug | `shpigovsky` |
| Primary hostname | `shpigovsky.ru` |
| Population slice | **client_delivery** |
| Roster priority | **P0** |
| Evidence tier | **E0/E1** (Project); **E0/E2** (Website/Domain) |

---

## Production mode

| Field | Value |
|-------|-------|
| production_mode | **PIXEL_PERFECT** |
| mode_declared_at | 2026-06-17 |
| mode_declared_by | WF-A01 Pass 01 (retroactive) |
| mode_rationale | Approved FIG visual SSOT (`INCOMING/01_DESIGN/Шпиговский.fig`); pixel delivery stress-test path per FP-0002 forensic and Production Standards chain. |
| mode_waivers | Interaction stubs documented as KNOWN NON-GOALS (FAIL-010) |

### mode_history[]

| # | from | to | at | by | report_ref |
|---|------|-----|-----|-----|------------|
| 1 | — | PIXEL_PERFECT | 2026-06-17 | WF-A01 Pass 01 | [reports/website-factory-production-modes-implementation-pass-01.md](../../../reports/website-factory-production-modes-implementation-pass-01.md) |

**Contract:** [FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md](../FP-XXXX-PROJECT-PASSPORT-FIELDS-v1.md)

---

## 2. ATLAS references

| Class | ID | Canonical name | Lifecycle | Attestation |
|-------|-----|----------------|-----------|-------------|
| Organization (client) | ORG-0008 | ООО «Сознание» | **active** | AT-W1D-SHPIG-01 |
| Organization (executor) | ORG-0001 | Веб-студия «Полигон» | **active** | Wave 1 |
| Project | PRJ-0012 | Сайт shpigovsky.ru | **active** | AT-W3-SHPIG-01 |
| Website | WEB-SHPIG-01 | shpigovsky.ru | **active** | AT-W4-SHPIG-01 |
| Domain | DOM-SHPIG-01 | shpigovsky.ru | **active** | AT-W5-SHPIG-01 |

**Structural relationships (all active):** REL-SHPIG-PJ-01, REL-SHPIG-PJ-02, REL-SHPIG-WB-01, REL-SHPIG-WB-02, REL-SHPIG-DM-01  

**Source registers:**

- [ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md](../../../projects/atlas/population/ATLAS-WAVE3-SHPIGOVSKY-PROJECT-REGISTER-v1.md)
- [ATLAS-SHPIGOVSKY-FAST-TRACK-COMPLETION-v1.md](../../../projects/atlas/population/ATLAS-SHPIGOVSKY-FAST-TRACK-COMPLETION-v1.md)

---

## 3. Coordinator

| ID | Name | Role context |
|----|------|--------------|
| PER-0010 | Ольга Дягилева | Acquisition; client comms; coordination; SEO supervision; primary acceptance |

**Evidence:** EV-SHPIG-OP-01  

**Boundary:** PER-0010 is an attested **reference only** — no Person ↔ Project edges minted in ATLAS (SU-SHPIG-PRJ-10).

---

## 4. Current state

| Dimension | State |
|-----------|-------|
| Project phase | **PRODUCTION / MAINTENANCE — STABLE** (2026-08-20) |
| Live domain | `https://shpigovsky.ru/` |
| Core | `0.3.24-antispam` |
| Indexing | **OPEN — HUMAN-APPROVED** |
| WPilot auth | **`X-WPilot-Token`** (not Bearer) |
| Canonical source | `origin/mars/canonical-post-recovery` @ *(final SHA in stabilization report)* |
| Operational locus | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/` |
| Status authority | [PROJECT-STATUS.md](PROJECT-STATUS.md) |
| Open items | [REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md](REPORTS/OPEN-ITEMS-FP-0002-PRODUCTION-MAINTENANCE.md) |

Historical frontend milestones (V6/V8/V9) remain in archives/tags; they are **not** the active delivery phase.

---

## 5. Project boundaries

### In scope (documented)

- Client delivery for **shpigovsky.ru** under Website Factory discipline
- Polygon (ORG-0001) execution for ORG-0008 **ООО «Сознание»**
- WordPress delivery channel *(stack signal — not architecture design)*
- SEO supervision on delivery *(not i-SEO vendor channel)*

### Explicitly excluded (attested rejections)

| Item | Rejection |
|------|-----------|
| SEO supervision as separate Project | REJ-SHPIG-PRJ-01 |
| Website Factory as separate Project | REJ-SHPIG-PRJ-02 |
| WordPress / Frontend / ACF / Custom as split Projects | REJ-SHPIG-PRJ-03 |
| i-SEO project channel | REJ-SHPIG-PRJ-06 |
| Historical site version twin | REJ-SHPIG-PRJ-07 |

### Out of scope at foundation (forbidden until intake)

- Page Inventory
- Block Inventory
- Sitemap
- Wireframes
- WordPress architecture design
- ACF architecture design
- Design decisions

### Future intake candidates (held — no start evidence)

- SHPIGOVSKY-INTAKE-FUT-01 — WP automation agents
- SHPIGOVSKY-INTAKE-FUT-02 — Extended SEO program

---

## 6. SAFE UNKNOWN

| Item | Note |
|------|------|
| Delivery phase precision | EV-SHPIG-OP-01 — not attested |
| Contract / acceptance dates | SU-SHPIG-PRJ-01, SU-SHPIG-PRJ-02 |
| ACF / custom programming scope | SU-SHPIG-PRJ-09 |
| Site IA / pages / blocks | Awaiting design materials |
| ORG-0008 → DOM-SHPIG-01 OWNS | Registrar evidence absent |
| Legal Entity Card | CC folder absent |
| CLIENT_OF commercial edge | Wave 6 |
| Person ↔ Project edges | Wave 3 out of scope |

---

## 7. Public business facts (E2 — informational)

From live site capture — **not** project scope proof:

| ID | Fact |
|----|------|
| BF-SHPIG-01 | Центр профилактики зависимостей **Шпиговский Дом** |
| BF-SHPIG-02 | Профилактика и лечение зависимостей |
| BF-SHPIG-03 | Немедицинское социально-психологическое учреждение |
| BF-SHPIG-04 | ООО «Сознание» — privacy policy operator signal |

**Evidence:** EV-SHPIG-WEB-01, EV-SHPIG-WEB-02  

---

*Passport — foundation document. Not manifest (MOC-*). Not registry card (ROC-*).*
