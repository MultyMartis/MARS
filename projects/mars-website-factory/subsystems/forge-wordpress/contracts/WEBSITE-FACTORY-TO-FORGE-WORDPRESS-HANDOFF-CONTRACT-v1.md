# Website Factory → Forge WordPress Handoff Contract v1

**Document type:** Boundary contract (B1)  
**Version:** v1  
**Date:** 2026-06-22  
**Stage:** FW-02  
**Authority:** Forge WordPress subsystem — human-operated intake gate

**Extends:** [frontend-handoff-contract-v0.md](../../../frontend-handoff-contract-v0.md) · [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](../FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md)

**Honesty:** Documentation contract only — **not** runtime validation, **not** automated intake.

---

## 1. Purpose

Define the **mandatory input package** Website Factory must deliver before Forge WordPress may begin **FWP-01 Project Intake**. This contract formalizes boundary **B1**.

---

## 2. Intake gate (blocking)

Forge WordPress intake is **forbidden** without all three:

```text
Website Factory PRODUCTION PASS
+
operator approval
+
complete handoff manifest
```

| Gate element | Evidence |
|--------------|----------|
| **PRODUCTION PASS** | Factory lifecycle `PRODUCTION PASS`; VL0–VL6 complete per [website-factory-validation-architecture-charter-v1.md](../../../website-factory-validation-architecture-charter-v1.md) (or documented waiver) |
| **Operator approval** | Signed acknowledgment in handoff manifest; G1 gate per [FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md](../FORGE-WORDPRESS-PROJECT-LIFECYCLE-v1.md) |
| **Complete handoff manifest** | `FRONTEND-HANDOFF` artifact using [FORGE-WORDPRESS-FRONTEND-HANDOFF-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-FRONTEND-HANDOFF-TEMPLATE-v1.md) |

---

## 3. Project identity (required)

| Field | Required | Notes |
|-------|----------|-------|
| **project_id** / execution-case ID | Yes | e.g. `FP-0002-SHPIGOVSKY` |
| **LOC-ZONE path** | Yes | Canonical project root under `workspaces/website-factory-operations/` |
| **ATLAS bindings** | If exist | Registry / passport cross-refs — **SAFE UNKNOWN** if not created |
| **project owner** | Yes | Operator or accountable role |
| **approved production_mode** | Yes | `PIXEL_PERFECT` \| `TEMPLATE_ART` per [website-factory-production-modes-charter-v1.md](../../../website-factory-production-modes-charter-v1.md) |
| **target WordPress mode** | If known | Mode A/B/C/D intent — may be **SAFE UNKNOWN** at handoff; resolved at intake |

---

## 4. Frontend authority (required)

| Field | Required | Notes |
|-------|----------|-------|
| **canonical frontend workspace** | Yes | Repo path or LOC-ZONE subpath |
| **approved commit or package version** | Yes | Git SHA, tag, or release label |
| **source directories** | Yes | `src/` tree; partials, SCSS, JS roots |
| **build command** | Yes | e.g. `npm run build` — must be reproducible |
| **`src` / `dist` boundary** | Yes | Source-first; **no** hand-edited `dist` as authority |
| **assets** | Yes | Raster paths, lazy rules, picture/srcset intent |
| **fonts** | Yes | Paths, formats, licensing note if external |
| **SVG** | Yes | Sprite or inline policy |
| **JavaScript dependencies** | Yes | CDN vs bundled; critical globals (Swiper, Fancybox, etc.) |

Factory retains ownership of design source, frontend code changes post-handoff (via change-control), Gulp discipline, and VL semantics — see [FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md](../FORGE-WORDPRESS-HANDOFF-BOUNDARIES-v1.md) §2.

---

## 5. Frontend readiness (required)

| Field | Required | Notes |
|-------|----------|-------|
| **desktop approval** | Yes | Operator visual approval where `PIXEL_PERFECT` |
| **mobile approval** | Yes | Per production mode matrix |
| **responsive rules** | Yes | Breakpoints, mobile-first notes |
| **frontend QA** | Yes | VL reports or consolidated QA summary |
| **visual approval** | Yes for PIXEL_PERFECT | [operator-visual-approval-law-v1.md](../../../operator-visual-approval-law-v1.md) |
| **known deviations** | Yes | List or explicit `none` |
| **browser support** | Yes | Target browsers / minimum versions |
| **accessibility notes** | Yes | Known gaps, landmarks, form labels |

---

## 6. Page and block inventory (required)

| Field | Required | Notes |
|-------|----------|-------|
| **page inventory** | Yes | All pages with slugs, types, H1 policy |
| **block inventory** | Yes | `block_id` alignment with Factory registry where applicable |
| **shared components** | Yes | Header, footer, nav, forms shell |
| **unique components** | Yes | Page-specific sections |
| **forms** | Yes | Client behavior, endpoints (**SAFE UNKNOWN** if not wired) |
| **modals** | If present | Triggers, a11y, JS hooks |
| **global elements** | Yes | Cookie banner, CTAs, legal links |
| **legal pages** | If applicable | Privacy, terms, etc. |

---

## 7. Content signals (required)

Signals inform Forge WordPress content modeling — **not** final WordPress schema.

| Field | Required | Notes |
|-------|----------|-------|
| **fixed content** | Yes | Copy that must not be editor-editable |
| **editable content candidates** | Yes | Regions likely needing CMS fields |
| **repeated entities** | Yes | Cards, news, team, catalog-like patterns |
| **global data** | Yes | Phone, address, social, site-wide options |
| **content dependencies** | Yes | Cross-page references, shared snippets |
| **content still SAFE UNKNOWN** | Yes | Explicit gaps — do not invent at intake |

---

## 8. Handoff manifest structure

Minimum artifact: **`FRONTEND-HANDOFF`** — use template. Cross-reference Factory [frontend-handoff-contract-v0.md](../../../frontend-handoff-contract-v0.md) fields where applicable.

Additional required annexes in manifest:

- Link to `PROJECT-INTAKE` (Forge WordPress)
- VL6 / PRODUCTION PASS evidence paths
- Operator sign-off block (name, date, scope)

---

## 9. Rejection conditions

| Condition | Outcome |
|-----------|---------|
| Missing PRODUCTION PASS | **REJECT** — return to Factory VL chain |
| Missing operator approval | **REJECT** — hold at G1 |
| Incomplete manifest | **REJECT** — WV0 blocks |
| Non-reproducible build | **REJECT** — Factory must fix build |
| Undeclared `production_mode` | **REJECT** |
| Hand-edited `dist` as source of truth | **REJECT** |
| Missing page/block inventory | **REJECT** |
| Material visual failures undocumented | **REJECT** for PIXEL_PERFECT |

---

## 10. Return to Website Factory

When rejected, Forge WordPress returns a **return packet**:

| Element | Content |
|---------|---------|
| **return_reason** | Specific missing or failed gate |
| **required_remediation** | Actionable Factory tasks |
| **blocking_WV** | WV0 (always) |
| **operator_contact** | Project owner |

Factory addresses remediation; **new handoff version** required (manifest version bump).

---

## 11. Lifecycle mapping

| Stage | Contract role |
|-------|---------------|
| FWP-01 | This contract is prerequisite |
| WV0 | Validates manifest completeness |
| G1 | Operator intake approval |

---

## Related documents

- [FORGE-WORDPRESS-PROJECT-INTAKE-CONTRACT-v1.md](FORGE-WORDPRESS-PROJECT-INTAKE-CONTRACT-v1.md)
- [templates/FORGE-WORDPRESS-FRONTEND-HANDOFF-TEMPLATE-v1.md](../templates/FORGE-WORDPRESS-FRONTEND-HANDOFF-TEMPLATE-v1.md)
- [website-factory-validation-architecture-charter-v1.md](../../../website-factory-validation-architecture-charter-v1.md)

---

*Handoff contract v1 — B1 formalized; not runtime.*
