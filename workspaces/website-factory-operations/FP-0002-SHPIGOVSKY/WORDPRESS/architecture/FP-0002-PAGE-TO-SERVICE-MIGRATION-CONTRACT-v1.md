# FP-0002 Page-to-Service Migration Contract v1

**Task:** V9-06A.1 | **Date:** 2026-07-03  
**Status:** DEFINED — no migration executed

---

## 1. Scope

Three foundation Pages migrate to `service` CPT parent records:

| # | Foundation Page slug | Target service_id | Canonical URL |
|---|---------------------|-------------------|---------------|
| 1 | `zavisimosti` | SVC-ZAVISIMOSTI | `/uslugi/zavisimosti/` |
| 2 | `psihicheskoe-zdorovie` | SVC-PSYCH | `/uslugi/psihicheskoe-zdorovie/` |
| 3 | `rasstroystva-pischevogo-povedeniya` | SVC-RPP | `/uslugi/rasstroystva-pischevogo-povedeniya/` |

All other services (12) are **CREATE_SERVICE** only — no Page predecessor.

---

## 2. Recommended method

**CREATE_NEW_SERVICE → VALIDATE → SWITCH_REFERENCES → RETIRE_OLD_PAGE**

**Do not** use in-place `post_type` conversion unless proven advantage with rollback contract — **not recommended** for FP-0002.

---

## 3. Per-candidate contract

### 3.1 Zavisimosti

| Field | Value |
|-------|-------|
| Current Page identity | Foundation Page `zavisimosti` under parent `uslugi` |
| Target Service | SVC-ZAVISIMOSTI |
| Desired canonical URL | `/uslugi/zavisimosti/` |
| Method | CREATE_NEW_SERVICE |
| Content transfer | Map Page title, excerpt if any; ACF/bounded fields from V9 fixture at V9-08 |
| Metadata transfer | `fp02_service_layout=subdivision`; menu_order from foundation if set |
| Child relationships | Set `post_parent=0`; children created separately with `post_parent` = new service ID |
| Menu updates | Primary + footer_services items pointing to Page → repoint to Service URL |
| Old object retirement | Draft → trash after URL 200 + menu switch + backup |
| Redirect requirement | 301 only if old Page URL differed from target (slug preserved → likely none) |
| Rollback | Restore Page from trash; delete Service; restore menu refs from ID map JSON |
| Idempotency | Check service slug `zavisimosti` exists before create; skip if map records completion |
| Collision handling | Reject if Service slug taken; reject if Page still published when Service live |

### 3.2 Psihicheskoe zdorovie

| Field | Value |
|-------|-------|
| Current Page identity | Foundation Page `psihicheskoe-zdorovie` |
| Target Service | SVC-PSYCH |
| Desired canonical URL | `/uslugi/psihicheskoe-zdorovie/` |
| Method | CREATE_NEW_SERVICE |
| Content transfer | Placeholder content from V9 dist at V9-08 |
| Metadata transfer | `fp02_service_layout=subdivision`; placeholder flag |
| Child relationships | 6 leaf services created with `post_parent` = new service ID |
| Menu updates | footer_services, home_accordion refs |
| Old object retirement | Same as §3.1 |
| Redirect requirement | Slug preserved |
| Rollback | Same pattern |
| Idempotency | Same pattern |
| Collision handling | Same pattern |

### 3.3 Rasstroystva pishchevogo povedeniya

| Field | Value |
|-------|-------|
| Current Page identity | Foundation Page `rasstroystva-pischevogo-povedeniya` |
| Target Service | SVC-RPP |
| Desired canonical URL | `/uslugi/rasstroystva-pischevogo-povedeniya/` |
| Method | CREATE_NEW_SERVICE |
| Content transfer | Placeholder from V9 |
| Metadata transfer | `fp02_service_layout=subdivision` |
| Child relationships | 3 leaf services under parent |
| Menu updates | footer_services, home_accordion |
| Old object retirement | Same as §3.1 |
| Redirect requirement | Slug preserved |
| Rollback | Same pattern |
| Idempotency | Same pattern |
| Collision handling | Same pattern |

---

## 4. Migration procedure (ordered)

1. **Pre-migration snapshot** — WPilot backup + object ID map export.
2. **Create Service** — title, slug, `post_parent=0`, layout meta, publish.
3. **Verify permalink** — GET canonical URL → 200; template `single-service.php`.
4. **Create children** — for each leaf under this parent (if not already in separate batch).
5. **Switch menu references** — update menu item object IDs/types.
6. **Switch internal links** — audit hardcoded links in content (minimal in foundation).
7. **Retire Page** — set draft → trash; do not delete permanently until retention window.
8. **Flush rewrites** — once per batch.
9. **Record completion** — update migration map JSON in `delivery/fixtures/`.

---

## 5. Redirect matrix (migration-specific)

| From | To | When |
|------|-----|------|
| Old Page permalink (if drift) | New Service permalink | 301 at retirement |
| `/uslugi/zavisimosti/` Page ID URL | `/uslugi/zavisimosti/` Service | Only if WordPress emitted different URL pre-migration |

Slug preservation means **zero redirect** expected when slugs match.

---

## 6. Rollback contract

| Step | Rollback action |
|------|-----------------|
| Service created | Trash/delete Service posts (children first) |
| Page trashed | Restore Page from trash |
| Menus updated | Restore menu JSON from snapshot |
| Rewrites flushed | Flush again post-rollback |

---

## 7. Execution phase

Migration execution authorized in **V9-06D** (object skeleton) — not V9-06A.1, not V9-06B.

---

*Planning authority only.*
