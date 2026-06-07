# MOC-12 — External References & ATLAS Refs

**Class:** MOC-12  
**Manifest Charter category:** Category 7 — Topology target locators  
**Factory Project:** FP-0001  
**Convention:** RC-01 — refs are **pointers**, not identity restatement  

---

## ATLAS canonical references

Populated per [WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md](../../../../website-factory-reference-v1/WEBSITE-FACTORY-ATLAS-ADOPTION-STATEMENT-v1.md) when active attested canonical exists in population documentation.

| Field | Value | Population source |
|-------|-------|-------------------|
| atlas_client_org_ref | **ORG-0004** | Триумф — active (Wave 1) |
| atlas_project_ref | **PRJ-0008** | Манипулятор — active |
| atlas_website_ref | **WEB-0009** | manipulator-triumph.ru — active |
| atlas_domain_ref | **DOM-0004** | manipulator-triumph.ru — active |
| atlas_person_ref | *absent* | Not required at enrollment |
| atlas_relationship_ref | REL-0025, REL-0031, REL-0035 | COMMISSIONED_BY, BELONGS_TO, OWNS |

---

## Relationship refs (informational)

| Ref | Semantics |
|-----|-----------|
| REL-0025 | PRJ-0008 → ORG-0004 **COMMISSIONED_BY** |
| REL-0026 | ORG-0001 → PRJ-0008 **EXECUTES** |
| REL-0031 | WEB-0009 → PRJ-0008 **BELONGS_TO** |
| REL-0035 | ORG-0004 → WEB-0009 **OWNS** |

---

## External workspace locators

| Role | Locator |
|------|---------|
| delivery_workspace | `projects/triumph-manipulator-landing/` |
| live_url | `https://manipulator-triumph.ru` |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Live attestation on runtime ATLAS service | **SAFE UNKNOWN** — documentation-level refs only |
| Blueprint / generation_id binding | **SAFE UNKNOWN** at Wave 1 bind |

---

## Ref discipline

- Factory Project **FP-0001** remains distinct from `atlas_project_ref` PRJ-0008.
- No org legal facts (INN, legal name) copied into Factory records — ATLAS owns canonical identity.

---

*Category 7 locators. Closure ref to POC-08 optional — not present at Wave 1.*
