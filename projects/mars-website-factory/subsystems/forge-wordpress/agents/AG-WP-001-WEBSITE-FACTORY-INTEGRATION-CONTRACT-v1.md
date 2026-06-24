# AG-WP-001 — Website Factory Integration Contract v1

**Document type:** Upstream/downstream integration contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Aligns with:** FW-C-01 [WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md](../contracts/WEBSITE-FACTORY-TO-FORGE-WORDPRESS-HANDOFF-CONTRACT-v1.md)

---

## 1. Upstream sources (Website Factory)

| Source | Consumed by AG-WP-001 |
|--------|----------------------|
| Website Factory project intake | Project context, constraints |
| Approved frontend (`src/` authority) | Implementation reference |
| Page inventory | Template map |
| Block registry | Block-to-WP mapping |
| Design tokens / frontend rules | Styling parity |
| Production Pass | Gate A authority |
| Frontend Handoff Contract | Structural contract |

---

## 2. Downstream outputs (to Factory ecosystem)

| Output | Destination |
|--------|-------------|
| WordPress implementation | Project `WORDPRESS/` tree |
| Editor model | Content model docs + ACF JSON |
| Theme/plugin source | Git-tracked artifacts |
| QA package | Validation reports |
| Handoff package | Operator + future WPilot |

---

## 3. Forbidden cross-boundary actions

AG-WP-001 **must not** alter Website Factory canonical frontend directly (`workspaces/fp-*/src/`, factory reference trees).

---

## 4. Frontend Change Request (FCR)

When WordPress cannot safely compensate for a frontend defect:

```text
FRONTEND CHANGE REQUEST
```

Required fields:

| Field | Description |
|-------|-------------|
| exact issue | What fails parity or integration |
| evidence | Screenshots, diff, route |
| affected files/components | Paths in frontend repo |
| reason WP cannot compensate | Technical boundary |
| operator decision required | Yes |

FCR returns work to **Gulp Frontend Agent** / operator — not silent WP hacks.

---

## 5. Workflow position

```text
Website Factory Stages 10–11 (frontend)
  → Production Pass
  → Forge WordPress FW-06B
  → AG-WP-001 execution workflow
```

---

*Website Factory integration v1 — frontend SoT stays upstream.*
