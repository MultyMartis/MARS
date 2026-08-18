# Forge WordPress — Second-site bootstrap v1

**ID:** FW-S-47  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  

**Goal:** Site #2 does not feel like “the first production case from zero.” Bespoke pages start **after** this shell exists.

---

## 1. Code (before bespoke page work)

| Piece | Notes |
|-------|--------|
| Theme skeleton | FW-S-03 structure; enqueue; template-parts folders; tokens file |
| Functionality plugin skeleton | bootstrap, autoload or includes, text domain |
| Module registry | [FW-S-33](FORGE-WORDPRESS-MODULE-LIFECYCLE-STANDARD-v1.md) — even if a simple array |
| i18n | [FW-S-18](FORGE-WORDPRESS-I18N-STANDARD-v1.md) from first string |
| Settings foundation | options page stub + SoT helpers |
| SEO foundation | one owner; empty-safe output |
| Sitemap | native extension hook stub |
| Dashboard | one ops widget stub |
| Typography owner | render-time pipeline **or** explicit “not needed” WAD |
| Navigation foundation | `register_nav_menus` + walker/CSS hooks |

Do **not** copy clinical CPTs or brand CSS. Copy **structure**.

---

## 2. Docs (project pack)

- project profile / passport  
- [CONTENT-ENTITY-MAP](../templates/FORGE-WORDPRESS-CONTENT-ENTITY-MAP-TEMPLATE-v1.md)  
- [FIELD-OWNERSHIP-MAP](../templates/FORGE-WORDPRESS-FIELD-OWNERSHIP-MAP-TEMPLATE-v1.md)  
- [ADMIN-IA](../templates/FORGE-WORDPRESS-ADMIN-INFORMATION-ARCHITECTURE-TEMPLATE-v1.md)  
- [COMPONENT-INVENTORY](../templates/FORGE-WORDPRESS-COMPONENT-INVENTORY-TEMPLATE-v1.md)  
- [DESIGN-SYSTEM-MAP](../templates/FORGE-WORDPRESS-DESIGN-SYSTEM-MAP-TEMPLATE-v1.md)  
- [DEPENDENCY-REGISTER](../templates/FORGE-WORDPRESS-DEPENDENCY-REGISTER-TEMPLATE-v1.md)  
- access/authority ([FW-RB-01](../runbooks/FORGE-WORDPRESS-SOURCE-RUNTIME-AUTHORITY-STANDARD-v1.md))  
- environment profile + [ENVIRONMENT-FLAGS](../templates/FORGE-WORDPRESS-ENVIRONMENT-FLAGS-REGISTER-TEMPLATE-v1.md)  
- [DEPLOY SOP](../runbooks/FORGE-WORDPRESS-PRODUCTION-DEPLOYMENT-SOP-v1.md) applied  
- [QA matrix](../templates/FORGE-WORDPRESS-QA-MATRIX-v1.md) + [REGRESSION-PACK](FORGE-WORDPRESS-REGRESSION-PACK-v1.md)  

P1b CMS pack is a **gate** before frontend WordPress implementation ([CMS-ARCHITECTURE](FORGE-WORDPRESS-CMS-ARCHITECTURE-STANDARD-v1.md)).

---

## 3. Ops

- Git scope: clean worktree, exact paths ([FW-RB-04](../runbooks/FORGE-WORDPRESS-GIT-SOP-v1.md))  
- Backup model ([FW-RB-03](../runbooks/FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md))  
- Runtime/source authority  
- Production connection gate (real docroot, WPilot READ, write false)  
- Temporary-tool register empty or dated  

---

## 4. Stop

Do not start unique landing sections until §1–3 exist **or** a WAD waives a named item.

---

*FW-S-47 v1.*
