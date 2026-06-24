# AG-WP-001 — WPilot Handoff Contract v1

**Document type:** Handoff boundary contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Aligns with:** FW-C-03 [FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md](../contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md)

---

## 1. Boundary

```text
AG-WP-001:
  builds and validates WordPress implementation (local/dev)

WPilot:
  future controlled WordPress operations bridge (staging/prod ops)
```

---

## 2. Ownership

| Domain | Owner |
|--------|-------|
| Theme/plugin source (brain Git) | Forge / AG-WP-001 delivery |
| Runtime files on host | MLI (local) / hosting (remote) |
| Operational mutations post-handoff | WPilot + operator |
| Rollback after handoff | WPilot policy + operator |

---

## 3. Frozen vs editable zones (post-handoff)

| Zone | Typical state |
|------|---------------|
| Template structure, PHP architecture | **Frozen** without charter |
| Client content fields | **Editable** via curated editor |
| Plugin register | **Change requires** risk review |
| Integration credentials | **Never** in theme; WPilot target registry |

---

## 4. Handoff package requirements

Per Gate J — includes:

- Release manifest
- Plugin register with versions
- Known deviations
- Validation report bundle
- Rollback baseline reference
- WPilot target registry mapping (when chartered)

---

## 5. Current state

| Item | State |
|------|-------|
| WPilot package for FP-0002 | **HOLD** |
| Canonical approved package | **NOT YET CONFIRMED** |
| WPilot install on FP-0002 local | **NOT AUTHORIZED** (FW-07A) |

---

## 6. Production approval

All production exposure remains **prohibited** at AG-WP-001 foundation stage. WPilot DEV reference (`dev.gktriumph.ru`) is **separate** program — not FP-0002 local.

---

*WPilot handoff v1 — build vs operate split.*
