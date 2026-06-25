# AG-WP-001 — Approved Frontend Input Contract v1

**Document type:** Input contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24  
**Consumes:** Website Factory frontend handoff; **aligns with** [FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md](../projects/fp-0002/FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md)

**Field classification:** REQUIRED · OPTIONAL · CONDITIONAL · SAFE UNKNOWN ALLOWED · BLOCKING UNKNOWN

---

## 1. Purpose

Define the **minimum authoritative input** before AG-WP-001 may propose or implement WordPress artifacts.

---

## 2. Input fields

| Field | Classification | Notes |
|-------|----------------|-------|
| **project_id** | REQUIRED | e.g. `FP-0002` |
| **approved_frontend_git_commit** | REQUIRED | Immutable SHA; not branch tip alone |
| **production_pass** | REQUIRED | Issued Frontend Production Pass artifact |
| **page_inventory** | REQUIRED | Pages with routes and template intent |
| **block_inventory** | REQUIRED | Blocks/sections with stable IDs |
| **shared_component_inventory** | REQUIRED | Header, footer, modals, forms shell |
| **responsive_rules** | REQUIRED | Breakpoints and evidence (not assumptions) |
| **forms_map** | REQUIRED | Endpoints, validation, captcha, success states |
| **modal_map** | CONDITIONAL | Required if modals exist in approved frontend |
| **navigation_map** | REQUIRED | Menus, mobile nav, anchors |
| **assets_manifest** | REQUIRED | Images, SVG, icons — provenance |
| **font_manifest** | REQUIRED | WOFF2 paths, weights, fallbacks |
| **js_behaviour_map** | REQUIRED | Modules, `data-*` hooks, dependencies |
| **legal_pages** | CONDITIONAL | Required for sites with legal IA |
| **content_ownership** | REQUIRED | Who owns copy vs system fields |
| **editable_region_requirements** | REQUIRED | Client-edit boundaries |
| **known_deviations** | OPTIONAL | Documented waivers from Production Pass |
| **operator_visual_approval** | REQUIRED | Recorded sign-off |
| **wordpress_environment_profile** | REQUIRED | Runtime ID, URL, PHP version |
| **plugin_constraints** | REQUIRED | Allowed/forbidden plugins register |
| **hosting_constraints** | CONDITIONAL | Required before staging handoff |
| **seo_implementation_requirements** | CONDITIONAL | Implement given spec only |
| **analytics_requirements** | CONDITIONAL | Tags, consent, suppression rules |
| **security_requirements** | REQUIRED | Least privilege, no secrets in theme |

---

## 3. Explicit rejections

AG-WP-001 **must reject** intake when:

| Condition | Result |
|-----------|--------|
| Uncommitted frontend | **BLOCK** |
| `dist/` without `src/` authority | **BLOCK** |
| Screenshots as sole implementation source | **BLOCK** |
| Unapproved visual changes since Production Pass | **BLOCK** |
| Missing responsive evidence | **BLOCK** |
| Missing forms behaviour specification | **BLOCK** |
| Missing asset provenance | **BLOCK** |
| Production target without explicit charter | **BLOCK** |
| FW-06B not authorized | **BLOCK** (integration phase) |

---

## 4. FW-06B alignment

FW-06B produces the **handoff manifest** referenced here. This contract is the **agent-level** intake gate; FW-06B remains the **phase charter** for FP-0002 integration.

| FW-06B artifact | Maps to input field |
|-----------------|---------------------|
| Handoff manifest | page/block inventories, assets, JS |
| Approved commit/hash | `approved_frontend_git_commit` |
| Production Pass | `production_pass` |
| Theme integration plan outline | downstream — not substitute for this contract |

---

## 5. SAFE UNKNOWN handling

| Field type | Behaviour |
|------------|-----------|
| SAFE UNKNOWN ALLOWED | Document unknown; proceed only on non-blocking paths with operator ack |
| BLOCKING UNKNOWN | Stop; no architecture commitment |

---

## 6. Authority chain

```text
Frontend Production Pass
  → approved Git commit
  → FW-06B intake (when authorized)
  → AG-WP-001 input validation (Gate A)
```

---

*Input contract v1 — no implementation without approved handoff.*
