# Forge WordPress — Definition of Done v1

**ID:** FW-S-19  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** C  

A WP Forge site is **not done** because the frontend “looks ready”.

---

## Checklist

| Domain | Done means |
|--------|------------|
| Admin UX | Localized, curated fields, Site Settings SoT, no global debug notices, Dashboard widget |
| **CMS / editor workflows** | P1b maps exist; [EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md) PASS (change phone globally, add entity, hide section, internal CTA) |
| Frontend | Templates match approved design; empty Admin data does not show demo leftovers |
| Responsive | Desktop/tablet/mobile per design breakpoints |
| Real devices | Physical QA for device-specific features ([FW-S-17](FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md)) |
| Accessibility basics | [FW-S-37](FORGE-WORDPRESS-ACCESSIBILITY-BASELINE-v1.md) — not WCAG certification |
| Frontend acceptance | [FW-S-46](FORGE-WORDPRESS-FRONTEND-ACCEPTANCE-STANDARD-v1.md) — not screenshot parity only |
| Client editor workflows | [FW-S-43](FORGE-WORDPRESS-CONTENT-OPERATIONS-STANDARD-v1.md) — no programmer for normal content |
| SEO | Title/description owner; canonical; no duplicate SEO plugins |
| Sitemap | Native sitemap on **final** host after cutover |
| Forms | Handler + nonce + anti-spam |
| SMTP | Proven delivery on final domain |
| Redirects | Manifest PASS; no loops; query preserved |
| Users | No leftover bootstrap/`@localhost` admins; roles correct |
| System status | Dashboard current; WPilot write state known |
| Source/prod parity | Exact-file hashes MATCH for product code |
| Backup | Named full backup at last freeze/cutover |
| Git | Canonical checkpoint; secrets absent |
| Environment | `WP_ENVIRONMENT_TYPE` correct; debug off in prod |
| Webroot hygiene | [FW-S-20](FORGE-WORDPRESS-PUBLIC-WEBROOT-HYGIENE-GATE-v1.md) PASS |
| DNS | Intended A/NS; **mail zone intact** |
| SSL | Valid on canonical host |
| Indexing | Open only after indexing gate |
| Final crawl | 2xx/redirects as designed; no `.test`/`localhost` in HTML |

Use [QA matrix](../templates/FORGE-WORDPRESS-QA-MATRIX-v1.md) to evidence the rows.

---

*FW-S-19 v1.*
