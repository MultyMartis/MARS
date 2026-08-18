# Forge WordPress — Redirect Standard v1

**ID:** FW-RB-06  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** D  
**Evidence:** FP-0002 P17 CONT1 `.htaccess` fragment

---

## Rules

- Exact legacy path mapping (manifest)  
- Rules **before** WordPress front-controller block  
- Exact-path match; optional trailing slash variant  
- Query string preservation  
- **No prefix overreach** (`/yoga` must not steal `/yoga-example`)  
- Path-relative targets on temporary host **pre-cutover**  
- Temporary-host → final-domain host-conditional 301 **only after** final domain works (AP-016)

Do not copy client paths. Copy the **matching rules**.

Template: [REDIRECT-MANIFEST](../templates/FORGE-WORDPRESS-REDIRECT-MANIFEST-TEMPLATE-v1.md).

---

*FW-RB-06 v1.*
