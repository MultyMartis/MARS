# Forge WordPress — WPilot Production Standard v1

**ID:** FW-RB-09  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** C  
**Evidence:** FP-0002 P05-FU01; Dashboard P13+

---

## Defaults

- Authenticated **READ** for inspection  
- `write_enabled=false` by default  
- Business writes require an **explicit separate charter**  
- Distinguish operational telemetry (versions, ping) vs content writes  
- Show plugin version + write state on the system Dashboard  
- **Never** assume the stored option version equals runtime file version — verify filesystem/header  

Tokens: gitignored local path; never commit. Upgrade via documented package replace, not ad-hoc overwrite without baseline.

Forge WordPress **does not** own WPilot. Handoff: [FW-C-03](../contracts/FORGE-WORDPRESS-TO-WPILOT-HANDOFF-CONTRACT-v1.md).

---

*FW-RB-09 v1.*
