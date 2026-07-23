# REPORT — SITE-002 1C Category Identity Fix Charter 01

**Operation:** `SITE-002-PROD-1C-CATEGORY-IDENTITY-FIX-CHARTER-01`  
**OCPilot run:** **4.292**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_1C_CATEGORY_IDENTITY_FIX_CHARTER_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CATEGORY-IDENTITY-FIX-CHARTER-01\`

**Final verdict:** `SITE-002 1C CATEGORY IDENTITY FIX CHARTER COMPLETE — IMPLEMENTATION PLAN READY`

**Classifications:**
- Importer: `IMPORTER_LEAF_NAME_COLLISION_CONFIRMED`
- 1C source: `ONE_C_GUID_STRATEGY_AVAILABLE` (+ full path available)
- DB: `DB_CATEGORY_EXTERNAL_ID_ABSENT` + `DB_PRODUCT_XML_ID_PRESENT`
- Strategy: `RECOMMEND_HYBRID_GUID_OR_PATH`
- Persistence after next import: still **not proven** (from Run 4.291)

---

## 1. Scope

Documentary charter / technical plan for a future controlled fix so the next 1C import does not reassign products into legacy same-name categories (154/159/165 under 153) after Run 4.290 reparent.

No production mutation. No importer code change. No migration apply. Dry-run SQL examples only.

## 2. Operator approval

Operator approved the next step after Run 4.291: prepare charter / technical plan for 1C importer category identity / full-path matching fix. Production must not change in this run.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD (start) | `c3a0c790` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `c3a0c790` | yes (fetch performed) |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact report/docs commit |

Evidence: Storage `preflight/`.

## 4. Evidence base from Runs 4.289–4.291

| Run | Verdict | Durable fact |
|-----|---------|--------------|
| **4.289** Forensic | 1C MAPPING REVIEW REQUIRED | JG 210A 1C path under Мясоперерабатывающее; DB was legacy 159; leaf-name collision pattern |
| **4.290** Reparent | PRODUCTS MOVED | 4707/4708/4710→373; 4712→375; 4709 already 376 |
| **4.291** Postcheck | PERSISTENCE NOT YET PROVEN | Relations still hold; latest import `080010` predates reparent; legacy leaves empty |

Known collision leaves still exist as name-match targets: **154 / 159 / 165**.

Evidence: Storage `reports-read/evidence-base.md`, `evidence-matrix.csv`.

## 5. Importer source discovery

### Entrypoints

- Cron: `common/cronjob` → `1c` / `1c_offers`
- Includes: `import_1C.php`, `import_1C_process.php`, `import_1C_offers.php`
- MARS wrapper: `/storage/mars-tools/cron/mars_1c_import_wrapper.php`
- Reports: `mars_1c_import_YYYY-MM-DD_HHMMSS.txt`

### Category matching (confirmed)

Captured Production source builds a **global leaf-name index**:

`mb_strtolower(category_description.name) → category_id`

Then maps each 1C group `<Ид>` to that OC id. Parent path is used only when **creating** a missing category — not when a same-name row already exists.

### Product relations (confirmed)

Each product update: `DELETE` all `product_to_category` rows → `INSERT` from XML group IDs via the runtime GUID→OC map. First category gets `main_category=1`.

### Classifications

| Class | Result |
|-------|--------|
| `IMPORTER_MATCHES_CATEGORY_BY_LEAF_NAME` | **CONFIRMED** |
| `IMPORTER_MATCHES_CATEGORY_BY_FULL_PATH` | ABSENT |
| `IMPORTER_MATCHES_CATEGORY_BY_EXTERNAL_ID` | ABSENT (GUID ephemeral only) |
| Relation removal | **FULL REPLACE** |
| Phase 11 importer class | `IMPORTER_LEAF_NAME_COLLISION_CONFIRMED` |

Evidence: Storage `importer-source/`; repo captures under `reports/m9.8.9-06c-audit-data/`.

SAFE UNKNOWN: live FTP bytes not re-pulled this run; classification uses captured Production source from prior SITE-002 ops (same path as Lari discovery).

## 6. 1C source identity discovery

CommerceML classifier groups include stable `<Ид>` GUIDs and nested structure.

Examples:

| Group | GUID | Notes |
|-------|------|-------|
| ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ | `e0fd5c42-a3b8-11ea-8152-a85e4515c4f4` | → OC 362 |
| Мясоперерабатывающее | `2adc2489-7c1a-11f1-aecc-581122cf362c` | → OC 373 |
| Пилы для мяса | `95003163-7c1a-11f1-aecc-581122cf362c` | no OC leaf yet |
| Мясорубки | `7e43262d-7c1a-11f1-aecc-581122cf362c` | no OC leaf yet |
| Слайсеры для мяса | `e0b6bb6d-7c1a-11f1-aecc-581122cf362c` | → OC 376 |
| Электромеханическое | `bac3dc26-7c19-11f1-aecc-581122cf362c` | → OC 375 |
| Хлеборезки | `41a86281-7c1b-11f1-aecc-581122cf362c` | no OC leaf yet |

Products reference groups by GUID; product `Ид` maps to `oc_product.xml_id`.

| Class | Result |
|-------|--------|
| `ONE_C_CATEGORY_GUIDS_AVAILABLE` | **YES** |
| `ONE_C_CATEGORY_FULL_PATH_AVAILABLE` | **YES** |
| Phase 11 | `ONE_C_GUID_STRATEGY_AVAILABLE` |

Evidence: Storage `one-c-source/` + forensic `1c-artifacts/` from Run 4.289.

## 7. DB identity discovery

From Run 4.289 schema dumps (reused read-only; no DB write this run):

| Item | Result |
|------|--------|
| `oc_category` GUID/xml_id | **ABSENT** |
| Category mapping table | **ABSENT** |
| `oc_product.xml_id` | **PRESENT** |
| `oc_product_to_category` metadata | product_id / category_id / main_category only |

Classifications: `DB_CATEGORY_EXTERNAL_ID_ABSENT`, `DB_PRODUCT_XML_ID_PRESENT`.

Evidence: Storage `db-readonly/`.

## 8. Identity strategy options

| Option | Summary | Role |
|--------|---------|------|
| A | Column `xml_id` on `oc_category` | Optional later |
| B | Dedicated mapping table | **Primary** |
| C | Full-path matching | Fallback |
| D | Explicit collision map | Guard only |
| E | Hybrid B+C+D | **Selected** |

Evidence: Storage `identity-options/`.

## 9. Recommended strategy

**`RECOMMEND_HYBRID_GUID_OR_PATH`**

1. Persist 1C group GUID → OC `category_id` in `oc_mars_1c_category_map` (name HITL-final).
2. Full-path fallback when GUID unseen.
3. Collision guard: never leaf-name-resolve into legacy **154/159/165** when source path is under tech root GUID.
4. Do not delete/disable legacy categories until post-fix import persistence is proven.
5. Optional later: native column on `oc_category` if team wants product-like identity on core table.

Interim mapping may point leaf GUIDs (Пилы/Мясорубки/Хлеборезки) at hubs **373/375** until canonical leaves are created in a separate wave.

## 10. Implementation charter

Six phases (future apply):

1. Read-only harness (parse XML → proposed map)
2. Mapping table + backfill (no product moves)
3. Importer matching change (GUID → path → create; collision guard)
4. Dry-run import simulation
5. Controlled production apply + persistence verify
6. Legacy cleanup — **separate** approval

Evidence: Storage `implementation-plan/`.

## 11. Migration / backfill plan

Dry-run only SQL examples:

- `migration-plan/dry-run-schema.sql`
- `migration-plan/dry-run-backfill.sql`
- `migration-plan/dry-run-rollback.sql`

Also mirrored under repo:

`projects/ocpilot/sites/site-002/reports/artifacts/SITE-002-PROD-1C-CATEGORY-IDENTITY-FIX-CHARTER-01/`

**DO NOT APPLY** in this run.

## 12. Validation plan

Before / during / after checks centered on products **4707/4708/4709/4710/4712**, legacy leaves empty, import SUCCESS, public PDP OK, sitemap sane, monitor not worsened.

Evidence: Storage `validation-plan/`.

## 13. Risks

- Wrong map + full relation replace can move many products
- Path fallback fragile on renames (GUID primary mitigates)
- Possible live vs captured importer drift — re-verify FTP before deploy
- Monitor baseline 1737 vs live 1817 + artifact conflict still open
- Legacy cleanup before persistence proof is dangerous

Evidence: Storage `risks/risks.md`.

## 14. HITL gates

1. Operator approves hybrid strategy  
2. Алексей/1C confirms GUID stability (or path canonicality)  
3. Exact category/product allowlist approved  
4. Full backup before apply  
5. Dry-run simulation reviewed  
6. Rollback approved  
7. Post-import persistence check required  
8. Legacy cleanup separate approval  

Evidence: Storage `risks/hitl-gates.md`.

## 15. Production mutation summary

| Item | Value |
|------|-------|
| FTP writes | **0** |
| DB writes | **0** |
| Admin saves | **0** |
| Import runs | **0** |
| Scheduler changes | **0** |
| Monitor baseline changes | **0** |
| Category deletes/disables | **0** |
| Product/category relation changes | **0** |
| Source deploys | **0** |
| Cache clears | **0** |
| OCMOD refresh | **0** |
| Dirty main changes | **0** |

## 16. Git/worktree summary

| Item | Value |
|------|--------|
| Authority branch | `site-002-git-authority-realign-after-wave-e` @ pre-commit `c3a0c790` |
| Dirty main | inspected read-only only |
| This commit | report + docs + dry-run planning artifacts only |
| Storage artifacts | **not** committed |

## 17. Storage artifacts

Root: `...\deployments\SITE-002-PROD-1C-CATEGORY-IDENTITY-FIX-CHARTER-01\`

Populated: `preflight`, `reports-read`, `importer-source`, `one-c-source`, `db-readonly`, `identity-options`, `implementation-plan`, `migration-plan`, `validation-plan`, `risks`, `reports`, `manifests`, `logs`.

## 18. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Live importer byte-identity vs captured source | SAFE UNKNOWN — re-fetch before deploy |
| Exact Beget backup ID for future apply | N/A this run |
| GUID long-term stability in 1C | HITL confirm with Алексей (evidence already shows GUIDs present) |
| Whether next scheduled import already ran after reparent | Not re-probed this charter; Run 4.291 said `080010` was latest and predated reparent — re-check before apply wave |
| Creating missing tech leaves | Out of scope; optional follow-on |

No blocker for charter completeness.

## 19. Final verdict

**SITE-002 1C CATEGORY IDENTITY FIX CHARTER COMPLETE — IMPLEMENTATION PLAN READY**

Importer leaf-name collision is confirmed in source. 1C group GUIDs and full paths are available. DB lacks category external IDs. Recommended hybrid: mapping table + path fallback + legacy collision guard. Implementation phases and HITL gates are documented. Production unchanged.

## 20. Next recommendation

1. Operator + Алексей HITL on hybrid strategy / GUID stability.  
2. Implementation wave: read-only harness → mapping table → importer patch → dry-run → controlled apply.  
3. After persistence proven: separate legacy disable/redirect charter for 154/159/165.  
4. Do **not** refresh monitor baseline or clean legacy until post-fix import proof.  
5. Optional: create canonical leaves under 373/375 for path fidelity, then remappoint leaf GUIDs from hubs.
