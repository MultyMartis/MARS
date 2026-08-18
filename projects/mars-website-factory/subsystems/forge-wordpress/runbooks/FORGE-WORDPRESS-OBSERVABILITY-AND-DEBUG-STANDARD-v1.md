# Forge WordPress — Observability and debug standard v1

**ID:** FW-RB-11  
**Status:** ACTIVE — OPERATIONS STANDARD  
**Date:** 2026-08-18  

**Not** a monitoring platform. Bounded signals only.

---

## 1. Production signals (optional but named)

| Signal | Where |
|--------|--------|
| PHP fatals | host error log (not public webroot) |
| Failed AJAX / REST | form/search handlers; Activity Log counts |
| Form errors vs mail | [FORMS-UX](../standards/FORGE-WORDPRESS-FORMS-UX-STANDARD-v1.md) |
| Scheduled tasks | cron list / host cron |
| WPilot health | Dashboard; write false |
| Module health | registry vs Dashboard |
| Activity Log | editor actions |
| Deployment / version | [FW-S-41](../standards/FORGE-WORDPRESS-CHANGE-RELEASE-MANAGEMENT-STANDARD-v1.md) |

---

## 2. Debug policy

**Production: `WP_DEBUG` off.** No persistent public `debug.log` as operating standard.

Temporary debug:

1. **Enable** — capability-locked; time-boxed; flag in [ENVIRONMENT-FLAGS](../templates/FORGE-WORDPRESS-ENVIRONMENT-FLAGS-REGISTER-TEMPLATE-v1.md)  
2. **Collect** — copy log **out** of webroot  
3. **Disable** — same day unless WAD  
4. **Archive** — Storage/incident folder, not `public_html`  

---

*FW-RB-11 v1.*
