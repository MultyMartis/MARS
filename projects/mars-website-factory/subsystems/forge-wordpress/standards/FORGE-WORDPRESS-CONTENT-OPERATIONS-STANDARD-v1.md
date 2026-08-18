# Forge WordPress — Content operations and editor safety standard v1

**ID:** FW-S-43  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Extends:** [EDITOR-UX](FORGE-WORDPRESS-EDITOR-UX-STANDARD-v1.md) · [ADMIN-IA](FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-STANDARD-v1.md)

**Required outcome:** NORMAL POST-LAUNCH CONTENT WORK DOES NOT REQUIRE A PROGRAMMER.

Custom roles remain **SECOND-SITE VALIDATION**; capability filters are enough for site #1 evidence.

---

## 1. Role model (capability / readiness)

| Role | May | Must not |
|------|-----|----------|
| **Client editor** | business content: pages, CPT objects, posts, media (policy), Site Settings **business** tabs | raw integration code, environment, indexing, plugin internals, migration tools, raw CSS |
| **Site admin** | broader WP configuration (users at agreed level, permalinks if chartered, plugins **if** operator policy) | production debug, MU edits, Git deploy |
| **Technical operator** | integrations, system state, WPilot, SMTP, cache, cutover flags | silent content rewrites without intake |

Dangerous settings must not be visible merely because they technically exist (AP-006).

---

## 2. Client editing safety (architecture principle)

A client editor must not accidentally be able to:

- edit raw integration / advanced head code (unless a gated Admin field with capability)  
- change environment (`WP_ENVIRONMENT_TYPE`, debug)  
- expose indexing on staging (`blog_public`)  
- modify critical plugin internals  
- execute migration / importer tools (or those tools are capability-locked + temporary-tool register)  
- break layout through raw CSS / unfiltered HTML  

---

## 3. Editor vs code vs settings vs infrastructure

| Change type | Path |
|-------------|------|
| CONTENT | WP Admin |
| DESIGN / COMPONENT | source code (theme/plugin) |
| BUSINESS GLOBAL (phone, social, hours) | Site Settings |
| INFRASTRUCTURE (SMTP, cache, DNS) | technical operator |

Do not edit template PHP to change ordinary business content.

---

## 4. Post-launch workflows (each has EDITOR PATH / EXPECTED RESULT / QA)

| Workflow | Editor path | Expected result | QA |
|----------|-------------|-----------------|----|
| Add article | Posts → add; draft; SEO fields; featured image | Appears on blog when published; sitemap when public | [EDITOR-WORKFLOW-ACCEPTANCE](../templates/FORGE-WORDPRESS-EDITOR-WORKFLOW-ACCEPTANCE-CHECKLIST-v1.md) |
| Add service | Services CPT (or project equivalent) | Hub list + single URL | empty optional blocks hidden |
| Add specialist / team | People CPT | Hub + single; search group name stable | |
| Change contact | Site Settings contacts | Header, footer, contacts page, tel: links | |
| Change social | Site Settings social registry | Visible only where toggled | |
| Update SEO | entity SEO fields | view-source title/description | one owner |
| Reorder collection | menu order / list table | hub order | |
| Disable optional section | toggle / empty field | section not rendered | no demo leftover |

If a workflow still needs a programmer, the P1b pack is incomplete.

---

*FW-S-43 v1.*
