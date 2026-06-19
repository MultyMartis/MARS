# AUTO Catalog Vertical Profile v1

**Profile ID:** AUTO  
**Subprogram:** WF-R01.3.4 — Catalog & Vertical Profile References  
**Wave:** C7 — Vertical Profile Binding  
**Version:** v1  
**Date:** 2026-06-20  
**Status:** **P2 PARTIAL**

**Honesty boundary:** Documentation-only binding layer. **Prototype-informed** — **not** validated against a complete production automotive catalog. **Not** a Registry row, **not** a site type, **not** runtime, **not** dealer CMS schema.

---

## 1. Status

| Field | Value |
|-------|-------|
| **Profile status** | **P2 PARTIAL** |
| **Evidence basis** | SRC-SIBCAR-001 — approved prototype + local structural evidence |
| **Live OpenCart catalog** | **UNVERIFIED** for Factory binding |
| **Binding publication** | Wave C7 — documentation only |
| **Implementation** | **NOT STARTED** |
| **Registry ID** | **None** — `AUTO` = profile document identity only |

**Forbidden status claims:** AUTO P1 READY · production validated · complete automotive profile · dealer runtime supported.

---

## 2. Identity

| Field | Value |
|-------|-------|
| **Canonical working identity** | **AUTO** |
| **Registry site_type_code** | **Does not exist** — binds to `CATALOG` site type + dealer/commerce notes per charter §13 |
| **Scope** | Vehicle inventory catalogues · dealer listing sites · automotive PLP/PDP patterns |
| **Evidence proxy** | SRC-SIBCAR-001 (`workspaces/site-001-wf-v3/`) |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| WF-R01.3.4 Charter | `projects/mars-website-factory/wf-r01-3-4-catalog-vertical-profile-references-charter-v1.md` | Vertical Profile Policy §13 · AUTO P2 note |
| Catalog Reference Inventory | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` | AUTO evidence §17 |
| Wave C1 REPORT | `reports/wf-r01-3-4-wave-c1-catalog-reference-inventory-v1.md` | P2 PARTIAL §15 |
| Universal references | Waves C2–C6 published partials and scaffolds | Secondary structural alignment only |
| Block Registry | `workspaces/website-factory-reference-v1/block-registry/BLOCK-REGISTRY-v1.md` | Canonical identities only |

---

## 4. Evidence Level

| Class | State |
|-------|-------|
| **Approved prototypes** | SRC-SIBCAR-001 — inventory card · catalog filters · catalog layout · PDP hero zones |
| **Verified local execution evidence** | Prototype HTML/CSS in monorepo — **PARTIAL** |
| **Live production catalog** | **SAFE UNKNOWN** — not verified for Factory binding |
| **Published universal references** | Used as contract baseline — AUTO fields remain profile-specific overlays |

**Core honesty statement:**

```text
AUTO profile is prototype-informed.
It is not validated against a complete production automotive catalog.
```

---

## 5. Applicability

AUTO profile applies when a project targets vehicle inventory presentation with:

- Make/model/year-led taxonomy
- Mileage and configuration on cards
- Price-forward commercial presentation
- Dealer trust and contact/enquiry paths

AUTO profile **must not** elevate prototype-only fields to universal PRODUCT_CARD or FILTERS requirements.

---

## 6. Universal Contract Inheritance

Same universal catalog contract as MANUFACTURER:

```text
FILTERS · SEARCH · CATEGORIES · CATEGORY_GRID · PRODUCT_GRID · PRODUCT_CARD
CATEGORY_PAGE · PRODUCT_PAGE
```

AUTO-specific fields (make · mileage · VIN) are **profile adaptations** — forbidden as universal layer requirements.

---

## 7. CATEGORY_PAGE Binding

| Zone / block | Universal role | AUTO adaptation (where evidenced) |
|--------------|----------------|--------------------------------|
| **FILTERS** | PLP REQ | Vehicle facets — see §9 |
| **PRODUCT_GRID** | PLP REQ | Inventory listing |
| **PRODUCT_CARD** | PLP REQ | Make/model · year · mileage · price — see §10 |
| **SEARCH** | Discovery | Header search — universal |
| **BREADCRUMBS** | PLP REQ | Make/model hierarchy when present |
| **PAGINATION** | PLP REQ | Standard |

**Not declared mandatory without evidence:** credit filters · trade-in · monthly payment · dealer programme · reservation controls.

---

## 8. PRODUCT_PAGE Binding

### Minimum expected zones (structural — prototype-informed)

| Zone | Verification |
|------|--------------|
| vehicle identity | **VERIFIED** (prototype PDP hero) |
| media | **PARTIAL** — hero image pattern; no gallery block_id |
| price / commercial state | **VERIFIED** (prototype) |
| year / mileage / configuration | **VERIFIED** (prototype card/hero) |
| availability | **PARTIAL** |
| description | **PARTIAL** |
| contact or enquiry | **VERIFIED** — maps to `LEAD_FORM` policy |
| dealer trust | **PARTIAL** — `TRUST` zone |

### Classified extensions (not universal requirements)

| Feature | Classification |
|---------|----------------|
| credit | **SAFE UNKNOWN** — not verified in Factory reference |
| trade-in | **SAFE UNKNOWN** |
| reservation | **DEFERRED** |
| finance calculator | **DEFERRED** |
| VIN / history | **SAFE UNKNOWN** |
| equipment list | **PARTIAL** — prototype may show options list |
| comparison | **DEFERRED** — no Registry block |

---

## 9. FILTERS Priorities

| Field / facet | Classification | Notes |
|---------------|----------------|-------|
| make | **VERIFIED** | Prototype filter groups |
| model | **VERIFIED** | |
| year | **VERIFIED** | |
| price | **VERIFIED** | Range facet pattern |
| mileage | **VERIFIED** | |
| body type | **PARTIAL** | Common automotive facet |
| transmission | **PARTIAL** | |
| drive type | **PARTIAL** | |
| engine | **PARTIAL** | |
| availability | **PARTIAL** | In stock / sold — presentation only |
| credit | **SAFE UNKNOWN** | Not mandatory |
| trade-in | **SAFE UNKNOWN** | |
| monthly payment | **SAFE UNKNOWN** | |
| dealer programme | **SAFE UNKNOWN** | |
| reservation | **SAFE UNKNOWN** | |

---

## 10. PRODUCT_CARD Priorities

| Field | Classification | Universal? |
|-------|----------------|------------|
| vehicle make/model | **VERIFIED** | **No** — AUTO profile only |
| year | **VERIFIED** | **No** |
| mileage | **VERIFIED** | **No** |
| price | **VERIFIED** | Commercial emphasis — not universal spec slot |
| key configuration | **PARTIAL** | Trim · engine summary |
| availability | **PARTIAL** | |
| primary detail action | **VERIFIED** | Universal pattern |
| thumbnail | **VERIFIED** | Universal minimum |

AUTO-specific additions **do not** become universal `PRODUCT_CARD` fields.

---

## 11. Attribute Policy

| Attribute class | AUTO use | Verification |
|-----------------|----------|--------------|
| identity attributes | make · model · trim · stock id | **VERIFIED** (prototype) |
| condition attributes | new · used · mileage | **VERIFIED** / **PARTIAL** |
| configuration attributes | engine · transmission · drive · body | **PARTIAL** |
| usage attributes | mileage · owners · service history | **PARTIAL** / **SAFE UNKNOWN** for history |
| commercial attributes | price · discount · payment hints | **PARTIAL** |
| availability attributes | in stock · reserved · sold | **PARTIAL** |
| dealer-programme attributes | credit · trade-in · loyalty | **SAFE UNKNOWN** |

**Attribute Registry:** possible future system — **not created in WF-R01.3.4 C7**.

---

## 12. Commercial State Policy

| State | AUTO | Verification |
|-------|------|--------------|
| fixed price | **Supported** (presentation) | **VERIFIED** prototype |
| available | **Supported** | **PARTIAL** |
| sold / unavailable | **Supported** | **PARTIAL** |
| on request | **OPT** | **SAFE UNKNOWN** |
| request price | **N/A typical** | MANUFACTURER path — not AUTO default |
| made to order | **N/A typical** | |
| production lead time | **N/A typical** | |
| credit / finance advertised | **SAFE UNKNOWN** | Not binding without evidence |
| trade-in advertised | **SAFE UNKNOWN** | |
| reservation deposit | **DEFERRED** | |

---

## 13. Media Policy

| Priority | Classification | Notes |
|----------|----------------|-------|
| hero / primary photo | **VERIFIED** | Prototype PDP |
| gallery depth | **PARTIAL** | No Registry gallery block |
| interior / exterior sets | **SAFE UNKNOWN** | |
| 360 / video | **DEFERRED** | |
| document preview | **N/A typical** | |

Profile does not implement gallery runtime or create media block_id.

---

## 14. Trust and Dealer Policy

| Signal | Identity | Classification |
|--------|----------|----------------|
| dealer name / location | `TRUST` | **PARTIAL** — sanitize in reference |
| stock guarantee | `TRUST` | **SAFE UNKNOWN** |
| inspection / certification | `CERTIFICATES` | **SAFE UNKNOWN** |
| reviews | `TRUST` / social proof | **DEFERRED** |
| manufacturer warranty | `TRUST` | **PARTIAL** for new vehicles |

Use `TRUST` · `CERTIFICATES` only — no new block IDs.

---

## 15. CTA and Enquiry Policy

| CTA | Classification | Block |
|-----|----------------|-------|
| Call / message dealer | **VERIFIED** (prototype patterns) | `LEAD_FORM` or tel link — project choice |
| Request test drive | **SAFE UNKNOWN** | |
| Reserve vehicle | **DEFERRED** | |
| Credit application | **SAFE UNKNOWN** | |
| Trade-in enquiry | **SAFE UNKNOWN** | |

Primary path in prototype: **contact / enquiry** — not checkout.

---

## 16. Block Binding Matrix

| Canonical block | Binding status | Profile adaptation | Evidence state | Notes |
|-----------------|----------------|--------------------|----------------|-------|
| `FILTERS` | **BOUND (partial)** | Vehicle facets | **PARTIAL** | Prototype only |
| `SEARCH` | **BOUND** | Universal discovery | **VERIFIED** (universal C3) | |
| `CATEGORIES` | **OPTIONAL** | Make/model hubs | **PARTIAL** | IA-dependent |
| `CATEGORY_GRID` | **OPTIONAL** | Hub navigation | **PARTIAL** | |
| `PRODUCT_GRID` | **BOUND** | Inventory listing | **PARTIAL** | |
| `PRODUCT_CARD` | **BOUND (partial)** | Make · year · mileage · price | **PARTIAL** | Secondary source in C4B |
| `BREADCRUMBS` | **BOUND** | Hierarchy when used | **VERIFIED** (universal) | |
| `PAGINATION` | **BOUND** | Standard | **VERIFIED** (universal) | |
| `LEAD_FORM` | **BOUND** | Enquiry | **VERIFIED** (universal partial) | |
| `TRUST` | **OPTIONAL** | Dealer trust | **PARTIAL** | Sanitize PII |

---

## 17. Page-Type Binding Matrix

| Page type | Binding | Priority | Notes |
|-----------|---------|----------|-------|
| `CATEGORY_PAGE` | **PRIMARY (partial)** | **P2** | Prototype-informed PLP |
| `PRODUCT_PAGE` | **PRIMARY (partial)** | **P2** | Prototype PDP hero — gaps remain |
| `HOME_PAGE` | **CONTEXTUAL** | Handoff | Inventory entry |
| `SERVICE_PAGE` | **CONTEXTUAL** | Handoff | Service centre pages |
| `CONTACT_PAGE` | **CONTEXTUAL** | Handoff | Dealer contact |

---

## 18. Verified / Partial / SAFE UNKNOWN

| Concern | VERIFIED | PARTIAL | SAFE UNKNOWN | DEFERRED |
|---------|----------|---------|--------------|----------|
| make/model/year filters | ✓ | | | |
| price · mileage on card | ✓ | | | |
| body · transmission · drive | | ✓ | | |
| availability badges | | ✓ | | |
| dealer trust strip | | ✓ | | |
| credit · trade-in · finance | | | ✓ | |
| reservation · deposit | | | | ✓ |
| VIN / history | | | ✓ | |
| live OC catalog behavior | | | ✓ | |
| comparison widget | | | | ✓ |

---

## 19. Runtime Exclusions

AUTO profile binding **does not** authorize:

- Live OpenCart inventory APIs
- Credit/finance calculator backends
- VIN decoder integrations
- Reservation payment flows
- Dealer DMS coupling
- Production automotive catalog claims

---

## 20. Evidence Limitations

1. Evidence derives primarily from **static Gulp prototype** — not full dealer production site.
2. **Live OpenCart** catalog for SITE-001 remains **UNVERIFIED** for Factory enrollment.
3. Secondary SIBCAR patterns informed C4B PRODUCT_CARD notes only — universal minimum preserved.
4. P2 status is **intentional** — publication of honest partial binding is authorized by charter.
5. No new project audit was run in C7 — C1/C4 evidence reused.

---

## 21. Reuse Rules

Same guardrails as MANUFACTURER profile:

**Allowed:** field planning · QA checklists · source evaluation · future composition notes.

**Forbidden:** production-ready claim · universal field promotion · automatic generator · G2 proof · P1 upgrade without new verified evidence.

---

## 22. Evidence Paths

| Class | Path |
|-------|------|
| Primary prototype | `workspaces/site-001-wf-v3/` (SRC-SIBCAR-001) |
| OCPilot reports | `projects/ocpilot/sites/site-001/reports/` |
| Storage mirror (read-only) | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001/` |
| Inventory §17 | `projects/mars-website-factory/wf-r01-3-4-catalog-reference-inventory-v1.md` |
| Universal reference partials | `workspaces/website-factory-reference-v1/src/partials/` |
| C4B secondary card evidence | `reports/wf-r01-3-4-wave-c4b-product-grid-card-v1.md` |

**Sanitization mandatory:** remove dealer PII · brand assets · client URLs from any future extract.

---

## 23. Decision

**AUTO Catalog Vertical Profile v1 — PUBLISHED at P2 PARTIAL.**

Prototype-informed binding is sufficient for documentation handoff. Profile **must not** be treated as production-validated or promoted to P1 without new verified evidence.

**Next consumer:** Wave C8 — Exit and G2 Readiness Evaluation.
