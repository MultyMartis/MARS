# {PROJECT-ID} — Field Ownership Map v1

**Artifact ID:** FIELD-OWNERSHIP-MAP  
**Project:**  
**Date:**  
**Standard:** [GLOBAL SETTINGS OWNERSHIP](../standards/FORGE-WORDPRESS-GLOBAL-SETTINGS-OWNERSHIP-STANDARD-v1.md)

Every editable value has one owner.

---

## Ownership table

| FIELD / ENTITY | STORAGE OWNER (group + field name) | EDITOR (role) | FRONTEND CONSUMERS | FALLBACK (A–E) | VALIDATION |
|----------------|-------------------------------------|---------------|--------------------|----------------|------------|
| Phone (primary) | Site Settings / `phone_primary` | client editor | header, mobile, floating header, footer, contacts | B hide | phone |
| | | | | | |

Fallback classes: A required · B optional hide · C safe global · D programmatic · E demo (forbidden).

---

## Duplicate-risk review

| Business value | Found in (list all proposed fields) | Keep | Delete / never create |
|----------------|-------------------------------------|------|------------------------|
| | | | |

---

## Chrome helper functions (planned)

| Helper | Reads | Used by partials |
|--------|-------|------------------|
| | | |

---

*No second phone field “for the footer” unless it is a different business number.*
