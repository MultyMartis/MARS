# FP-0002 FW-07C-2 Mutation Charter v1

**Status:** `BOUNDED — FW-07C-2B PROVEN`  
**Project:** FP-0002 — Шпиговский  
**Date:** 2026-07-02 (updated after FW-07C-2B proof PASS)  
**Task:** FW-07C-2A — enforcement reconciliation and charter design  
**Authority:** Operator authorization FP-0002-FW-07C-2B (2026-07-02); V9-05C read-only admission PASS

> **Layer authorization is sequential.** FW-07C-2B local WPilot write proof is **COMPLETE**. FW-07C-2C, FW-07C-2D, and V9-06 remain **NOT AUTHORIZED** until separately chartered.

---

## 1. Scope

Controlled mutation programme for FP-0002 local WordPress foundation reconciliation and subsequent V9 integration. Applies only to:

| Surface | Path |
|---------|------|
| Runtime site root | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` |
| Domain | `http://shpigovsky.test/` |
| site_id | `fp-0002-shpigovsky` |
| Database | `mars_wp_fp0002` |
| Checkpoint baseline | `foundation-002-v9-pre-implementation` |

**Out of scope until separately chartered:** production hosting, remote deploy, DNS, secrets rotation, Laragon core, WordPress core updates.

---

## 2. Programme layers

| Layer | ID | Purpose | Mutation type | Current status |
|-------|-----|---------|---------------|----------------|
| Enforcement reconciliation + charter design | **FW-07C-2A** | Fix enforcement taxonomy; design mutation boundaries | Documentation only | **COMPLETE** (this task) |
| WPilot harmless write proof | **FW-07C-2B** | Prove scoped replace + backup + rollback on disposable target | WPilot write (bounded) | **COMPLETE** ([receipt](FP-0002-FW-07C-2B-WPILOT-LOCAL-WRITE-PROOF-RECEIPT-v1.md)) |
| Filesystem delivery capability | **FW-07C-2C** | Theme / plugin / acf-json package delivery | Filesystem (allowlisted) | **NOT AUTHORIZED** |
| WordPress object reconciliation | **FW-07C-2D** | Pages, menus, options, ACF values per route register | WP-CLI / WPilot / manual | **NOT AUTHORIZED** |
| Foundation reconciliation | **V9-06** | Execute approved route + object plan | Mixed bounded ops | **NOT STARTED** |
| Template/content integration | **V9-07+** | Visual parity, content migration, media | Mixed | **NOT STARTED** |

Layers are **sequential gates**. Each layer requires operator authorization referencing this charter (or layer-specific addendum) before execution.

---

## 3. Allowed roots (future — not active)

When FW-07C-2C is authorized, filesystem writes may target **only** these subtrees under the admitted site root:

```text
wp-content\themes\shpigovsky\
wp-content\plugins\shpigovsky-core\
wp-content\acf-json\
```

Delivery requires: X volume `AI WS` verification; runtime identity match; source manifest; pre-write checkpoint; file allowlist; dry-run diff; unknown-file detection; post-write hashes; rollback package.

---

## 4. Denied roots and surfaces (always)

Unless separately chartered:

```text
wp-admin\
wp-includes\
wp-content\plugins\metacode-wpilot\
wp-content\mu-plugins\
wp-content\uploads\
wp-config.php
.htaccess
database files
Laragon runtime
X:\MARS-Localhost\          (parent — protected)
X:\AI MARS\                   (repo — not runtime write target)
C:\ D:\ E:\ legacy MARS roots
sibling project sandboxes
```

Path validator precedence: **`FW_PATH_PROTECTED_ROOT` > `FW_PATH_OUTSIDE_ALLOWED_ROOT`** when both apply (FW-07C-2A reconciliation).

---

## 5. Allowed operation families (by layer — not active until authorized)

| Family | Layer | Mechanism |
|--------|-------|-----------|
| WPilot scoped `post_content` replace | 2B, 2D | WPilot REST |
| WPilot backup / rollback | 2B, 2D | WPilot REST |
| Theme file delivery | 2C | Forge filesystem adapter |
| Project-plugin file delivery | 2C | Forge filesystem adapter |
| ACF JSON schema delivery | 2C | Filesystem → theme `acf-json/` |
| Page create/update (bounded) | 2D, V9-06 | WP-CLI / manual |
| Menu reconciliation | 2D, V9-06 | WP-CLI / manual |
| Site options (front page, posts page) | 2D, V9-06 | WP-CLI / manual |
| Media import | V9-06+ | WP admin / WP-CLI |
| Object retirement | 2D, V9-06 | WP-CLI / manual with backup |

---

## 6. Denied operations (default)

- Generic SQL mutation
- Bulk mirror/purge of runtime tree
- WPilot writes without prior 2B proof
- Page creation via WPilot (not implemented)
- ACF registration via WPilot (not implemented)
- Menu mutation via WPilot (not implemented)
- Plugin/theme installation via WPilot
- MU-plugin modification
- User/credential changes except separately chartered local proof fixtures
- Production deploy
- `write_enabled: true` without explicit operator gate

---

## 7. WPilot boundary

**Supported today (v0.3.0-rc5):**

- Read-only inspection endpoints (admitted in V9-05C)
- Page `post_content` exact scoped replace
- Page backup
- Rollback

**Not supported today:**

- Page creation, posts, menus, ACF, users, media, options, parent/template assignment, plugin/theme installation

**Policy:** Use WPilot only where implemented **and** proven in FW-07C-2B. Do not duplicate WPilot capabilities in ad-hoc scripts.

---

## 8. WP-CLI boundary

Permitted for bounded operations **not** covered by proven WPilot paths, only when:

1. Layer gate authorized
2. Pre-checkpoint exists
3. Operation allowlisted in layer task
4. Dry-run or `--dry-run` where available
5. Audit receipt produced

Prohibited: raw SQL, unscoped `wp post delete`, option bulk replace without manifest.

---

## 9. Filesystem boundary

Forge filesystem delivery (FW-07C-2C) is the **only** authorized path for theme/plugin/acf-json bulk updates. Requirements:

| Control | Requirement |
|---------|-------------|
| Source authority | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/` (prescribed; not yet created) |
| Package | Clean manifest with SHA-256 per file |
| Checkpoint | Named checkpoint under `X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\` |
| Dry-run | Diff against runtime; operator review |
| Unknown files | Fail closed — no silent additions outside manifest |
| Rollback | Restore checkpoint package |

---

## 10. Project-plugin boundary

`shpigovsky-core` owns: bootstrap, modal hooks, form hooks, ACF registration helpers. ACF JSON **source of truth** lives in **theme** `acf-json/` per intake policy; plugin loads via theme wiring.

---

## 11. Backup model

| Trigger | Backup type |
|---------|-------------|
| Any WPilot write | WPilot page backup (required) |
| Filesystem delivery | Full subtree checkpoint (zip + manifest) |
| WP-CLI object batch | `wp db export` micro-dump or checkpoint reference |
| Pre-layer gate | Reference `foundation-002-v9-pre-implementation` minimum |

---

## 12. Dry-run model

- **WPilot:** dry-run flag on replace endpoint where supported; validate diff before apply
- **Filesystem:** manifest diff only; no writes until operator approves diff receipt
- **WP-CLI:** `--dry-run` or SQL preview scripts; no apply without approval reference

---

## 13. Approval model

```text
Operator task charter (explicit)
  → layer gate (2B / 2C / 2D / V9-06)
    → dry-run receipt
      → operator APPROVE
        → bounded execution
          → validation receipt
            → rollback proof (where required)
```

Authorization reference must cite: charter version, layer ID, checkpoint name, allowed operation list.

---

## 14. Rollback model

| Mechanism | Rollback path |
|-----------|---------------|
| WPilot replace | WPilot rollback endpoint |
| Filesystem delivery | Restore pre-delivery checkpoint package |
| WP-CLI create | Delete created object from backup identity map |
| WP-CLI update | Restore from checkpoint DB or object export |

Final state must be proven equivalent to pre-mutation baseline for proof tasks (FW-07C-2B).

---

## 15. Audit model

Each authorized operation produces:

- `operation_id`, `site_id`, `timestamp`, `layer`, `mechanism`
- before/after checksums or WPilot receipt IDs
- checkpoint reference
- `mutations_count`, `rollback_available`

Store under `runtime/reports/fp0002-fw07c2/` (path TBD at layer authorization).

---

## 16. Stop conditions

Stop immediately if:

- Volume label ≠ `AI WS`
- `write_enabled` toggled without authorization
- Path validator returns any denial
- Unknown file in delivery manifest
- WPilot backup fails
- Rollback does not restore equivalence
- Operator revokes layer authorization

---

## 17. Production exclusions

No layer in this charter applies to production. Production requires separate programme, credentials charter, and DNS/hosting gate.

---

## 18. Required tests (per layer)

| Layer | Tests |
|-------|-------|
| 2A | `run-all-enforcement-tests.mjs` — FULL PASS |
| 2B | WPilot proof script + admission preflight + mutation baseline diff |
| 2C | Filesystem delivery harness + path validator + hash verification |
| 2D | Route manifest conformance + object identity checks |
| V9-06 | Intake validator + route register zero-unresolved gate |

---

## 19. Authorization gate

```text
FW-07C-2 MUTATION CHARTER: DRAFT — NOT AUTHORIZED

Required for first write:
  1. Operator review of this charter
  2. Explicit AUTHORIZE FW-07C-2B (or layer) instruction
  3. Checkpoint confirmation
  4. No foreign WIP in commit scope
```

---

## 20. WPilot local write proof (FW-07C-2B — COMPLETE)

**Executed:** 2026-07-02 — **PASS**  
**Receipt:** [FP-0002-FW-07C-2B-WPILOT-LOCAL-WRITE-PROOF-RECEIPT-v1.md](FP-0002-FW-07C-2B-WPILOT-LOCAL-WRITE-PROOF-RECEIPT-v1.md)  
**Evidence:** `runtime/reports/fp0002-fw07c2b-proof/`

| Step | Result |
|------|--------|
| Disposable fixture | Created and retired (`mars-wpilot-proof-fw07c2b`) |
| Dry-run | `match_count: 1`, safe zone, no mutation |
| Backup | `backup_id: 1` |
| Scoped replace | `replacement_count: 1` |
| Rollback | Pre-apply state restored |
| Final equivalence | `FINAL_STATE_EQUALS_INITIAL_STATE` |
| Write gate | `false → true → false` verified |

**Safe to execute next (2C):** **NO** — requires separate FW-07C-2C operator authorization.

---

## 21. Canonical WordPress source surface

| Role | Path | Status |
|------|------|--------|
| Prescribed canonical source | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/` | **NOT YET CREATED** |
| V9 static authority | `workspaces/fp-0002-shpigovsky-v9/src/` + `dist/` | **FROZEN baseline** |
| Intake authority | `workspaces/fp-0002-shpigovsky-v9/forge-intake/` | **COMPLETE** |
| Runtime deployment target | `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` | **READ_ONLY admitted** |

**Deployment model:** V9 `dist/` → WordPress templates/assets via implementation pipeline (V9-07+). Theme/plugin PHP authored in canonical WORDPRESS surface when created. Git tracks source; runtime is deploy target only.

**Created in FW-07C-2A:** NO — creation awaits operator authorization in FW-07C-2C or V9-06 gate.

---

## 22. Route reconciliation input (authority: V9-05A register)

| Action | Count | Notes |
|--------|------:|-------|
| **KEEP** | 17 | 31 V9 routes − 14 missing |
| **CREATE** | 14 | Missing pages/post + template gaps per register |
| **UPDATE** | 6 | 4 legal + blog archive + front-page template assignment |
| **RETIRE** | 4 | Extra foundation-only routes |
| **REDIRECT** | 0 | None mandated; `specyalisty` may become redirect after review |
| **MANUAL REVIEW** | 5 | `glavnaya` slug, dual `specialistam`, 3 retire-or-review extras |

**Forbidden invariant:** `/uslugi/genotipirovanie/` — MUST NOT publish (included in RETIRE set).

**Unresolved:** REDIRECT vs RETIRE for `/specyalisty/`, `/o-centre/intervyu-i-smi/`, `/pravovaya-informaciya-pilzovatelyu/` — operator decision before V9-06.

---

## 23. ACF / content-model input

| Item | Value |
|------|-------|
| Field groups | **13** documented (`FP-0002-V9-FORGE-FIELDS-v1.json`) |
| Ownership | Theme `acf-json/` source of truth; `inc/acf-json.php` registration |
| Registration | JSON sync + theme bootstrap (not runtime UI creation in implementation) |
| ACF Free compatibility | Architecture supports Free; **repeaters** may require Pro or code registration (OD-ACF-PRO open) |
| Runtime sync | Export JSON to theme before commit; load on deploy |
| Rollback | Restore acf-json checkpoint + DB field values from layer checkpoint |

---

## 24. Readiness matrix

| Mutation family | Mechanism | Implemented today | Proven | Next task | Authorized |
| --------------- | --------- | ----------------: | -----: | --------- | ---------: |
| WPilot scoped replace | WPilot REST | Yes | No (local) | FW-07C-2B | No |
| WPilot backup | WPilot REST | Yes | No (local) | FW-07C-2B | No |
| WPilot rollback | WPilot REST | Yes | No (local) | FW-07C-2B | No |
| Theme delivery | Forge filesystem | No | No | FW-07C-2C | No |
| Project-plugin delivery | Forge filesystem | No | No | FW-07C-2C | No |
| ACF schema delivery | Filesystem + theme | Wiring only | No | FW-07C-2C | No |
| Page creation | WP-CLI / manual | N/A | No | FW-07C-2D | No |
| Page update (content) | WPilot / manual | WPilot partial | No | FW-07C-2D | No |
| Hierarchy/template assignment | WP-CLI / manual | N/A | No | FW-07C-2D | No |
| Menus | WP-CLI / manual | N/A | No | FW-07C-2D | No |
| Posts/blog | WP-CLI / manual | N/A | No | V9-06 | No |
| Media | WP admin / WP-CLI | N/A | No | V9-06+ | No |
| Options | WP-CLI / manual | N/A | No | FW-07C-2D | No |
| Rewrites/permalinks | WP-CLI / manual | N/A | No | V9-06 | No |
| Retirement | WP-CLI / manual | N/A | No | FW-07C-2D | No |
| Forms | Project plugin | Partial hooks | No | V9-07+ | No |
| Production secrets | N/A | N/A | N/A | DEFERRED | No |

---

## 25. Mutation needs inventory (summary)

| Mutation | Required | Mechanism | Risk | Backup | Rollback |
| -------- | -------: | --------- | ---- | ------ | -------- |
| Theme filesystem delivery | Yes | FORGE_FILESYSTEM_DELIVERY | Medium | Subtree checkpoint | Package restore |
| Plugin filesystem delivery | Yes | FORGE_FILESYSTEM_DELIVERY | Medium | Subtree checkpoint | Package restore |
| ACF group registration | Yes | FORGE_FILESYSTEM_DELIVERY + PROJECT_PLUGIN_CODE | Medium | acf-json + DB | Checkpoint |
| ACF field values | Yes | WP_CLI / WORDPRESS_ADMIN_MANUAL | Medium | WPilot/DB | Object restore |
| Page creation (14 routes) | Yes | WP_CLI_CONTROLLED_OPERATION | Medium | DB checkpoint | Delete created |
| Page updates (legal, full) | Yes | WPILOT_SUPPORTED (content) / WP_CLI | Low–Med | WPilot backup | Rollback |
| Parent/template assignment | Yes | WP_CLI_CONTROLLED_OPERATION | Medium | DB checkpoint | Restore |
| Post creation (blog fixture) | Yes | WP_CLI_CONTROLLED_OPERATION | Low | DB checkpoint | Delete |
| Blog setup | Yes | WP_CLI_CONTROLLED_OPERATION | Low | Options export | Restore options |
| Menu create/update | Yes | WP_CLI / WORDPRESS_ADMIN_MANUAL | Medium | Menu export | Restore |
| Front page/posts page options | Yes | WP_CLI_CONTROLLED_OPERATION | Low | Options export | Restore |
| Media import | Yes | WP_CLI / WORDPRESS_ADMIN_MANUAL | Medium | Uploads checkpoint | Remove imports |
| Site options | Yes | WP_CLI_CONTROLLED_OPERATION | Med–High | DB checkpoint | Restore |
| Permalink/rewrite | Yes | WP_CLI_CONTROLLED_OPERATION | Med–High | Rewrite rules export | Restore |
| Retire obsolete objects (4+) | Yes | WP_CLI_CONTROLLED_OPERATION | High | Object export | Recreate from backup |
| Form configuration | Yes | PROJECT_PLUGIN_CODE | Low | Plugin checkpoint | Restore |
| Cookie consent | Yes | PROJECT_PLUGIN_CODE / theme | Low | File checkpoint | Restore |
| Legal DEMO markers | Yes | WPILOT / manual | Low | WPilot backup | Rollback |
| WPilot preservation | Yes | NOT_REQUIRED (preserve) | N/A | N/A | N/A |

---

*FP-0002 FW-07C-2 Mutation Charter v1 — DRAFT — NOT AUTHORIZED*
