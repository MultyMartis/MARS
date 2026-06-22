# MARS Localhost MLI-03 — WordPress Plugin & Theme Baseline v1

**Document type:** WordPress plugin and theme baseline validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Scope

Establish a **synthetic baseline** for the FWS-0001 WordPress runtime: core install with default bundled assets sufficient for Forge handoff smoke paths. No production themes, no client deliverables, no FP-0002 content.

---

## Target

| Field | Value |
|-------|-------|
| Site | `fws-0001` |
| Path | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| WordPress version | **7.0** |

---

## Baseline results

| Check | Result |
|-------|--------|
| WordPress core present | **PROVEN** |
| Active theme renders front-end | **PROVEN** — HTTP 200 on front-end via Host header |
| Admin theme stack loadable | **PROVEN** — `wp-login.php` HTTP 200 |
| Additional synthetic plugins beyond core bundle | **NOT PROVEN** — not separately installed or audited in this pass |
| Custom Forge consumer theme | **OUT OF SCOPE** — MLI-03 synthetic baseline only |

---

## Assessment

MLI-03 plugin/theme baseline is **PROVEN WITH LIMITATIONS**:

- **PROVEN:** Fresh WordPress 7.0 core install with default bundled themes/plugins sufficient for front-end, admin login, and REST smoke checks.
- **LIMITATION:** No dedicated synthetic plugin pack was validated; no per-plugin inventory command output captured in this report pass.
- **LIMITATION:** Theme/plugin activation matrix for Forge consumer workflows remains **FW-05R** scope after MLI-03 profile acceptance.

---

## Related

- [MARS-LOCALHOST-MLI-03-WORDPRESS-HEALTH-v1.md](MARS-LOCALHOST-MLI-03-WORDPRESS-HEALTH-v1.md)
- [MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md](MARS-LOCALHOST-MLI-03-FORGE-WORDPRESS-RUNTIME-HANDOFF-v1.md)

---

*WordPress plugin and theme baseline report v1 — MLI-03.*
