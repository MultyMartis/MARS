# Forge WordPress — Security ownership baseline v1

**ID:** FW-S-44  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Extends:** [CODING-AND-SECURITY](FORGE-WORDPRESS-CODING-AND-SECURITY-STANDARD-v1.md) · [HYGIENE](FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md)  
**Not:** an enterprise GRC product.

---

## Practical baseline

| Rule | Owner |
|------|--------|
| Secrets outside Git | tokens, SMTP passwords, WPilot secrets in ignored local/host config |
| No credentials in source | including sample `wp-config` in reports |
| No private backups in webroot | backups live outside `public_html` |
| Least privilege | client editor ≠ administrator where practical |
| Remove temp tools | [MODULE-LIFECYCLE](FORGE-WORDPRESS-MODULE-LIFECYCLE-STANDARD-v1.md) |
| Known admin accounts | inventory; no leftover `@localhost` |
| WPilot `write_enabled=false` by default | [FW-RB-09](../runbooks/FORGE-WORDPRESS-WPILOT-PRODUCTION-STANDARD-v1.md) |
| Plugin/update hygiene | [PLUGIN-GOVERNANCE](FORGE-WORDPRESS-PLUGIN-GOVERNANCE-STANDARD-v1.md) · [UPDATE SOP](../runbooks/FORGE-WORDPRESS-PRODUCTION-UPDATE-SOP-v1.md) |
| Controlled SVG / raw code | [MEDIA](FORGE-WORDPRESS-MEDIA-ARCHITECTURE-STANDARD-v1.md) · [CONTENT-OPERATIONS](FORGE-WORDPRESS-CONTENT-OPERATIONS-STANDARD-v1.md) |
| `WP_DEBUG` off in production | [OBSERVABILITY-DEBUG](../runbooks/FORGE-WORDPRESS-OBSERVABILITY-AND-DEBUG-STANDARD-v1.md) |

---

*FW-S-44 v1.*
