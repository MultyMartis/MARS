# REPORT — SITE-002 1C Category Identity Harness 01

**Operation:** `SITE-002-PROD-1C-CATEGORY-IDENTITY-HARNESS-01`  
**OCPilot run:** **4.293**  
**Date:** 2026-07-23  
**Environment:** PRODUCTION_1C_CATEGORY_IDENTITY_HARNESS_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-e01\repo`  
**Dirty main:** `X:\AI MARS` (read-only inspect only)  
**Runtime checkout:** `X:\AI MARS STORAGE\runtime-checkouts\site-002-monitor\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CATEGORY-IDENTITY-HARNESS-01\`

**Final verdict:** `SITE-002 1C CATEGORY IDENTITY HARNESS COMPLETE — LEAF CREATION NEEDED BEFORE BACKFILL`

**Classifications:**
- Harness: `HARNESS_COMPLETE_LEAF_CREATION_NEEDED`
- Critical products: `CRITICAL_PRODUCTS_CREATE_LEAF_REQUIRED`
- Next phase: `READY_FOR_LEAF_CREATION_CHARTER` (hubs also ready for interim mapping-table backfill in parallel)
- Previous charter: Run **4.292** / commit `36518f07`

---

## 1. Scope

Phase 1 only: read-only harness proving how a future importer should map 1C category identity (GUID + full path) to OpenCart `category_id` and proposed `product_to_category` assignments.

No production mutation. No importer code change. No mapping-table apply. No product moves.

## 2. Operator approval

Operator approved the next step after Run 4.292: create a read-only harness for 1C category identity mapping using live XML/DB evidence. Production must not change.

## 3. Preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority toplevel | `X:/AI MARS STORAGE/git-sync-e01/repo` |
| Authority branch | `site-002-git-authority-realign-after-wave-e` |
| Authority HEAD | `36518f07` (= `origin/mars/canonical-post-recovery`) |
| Origin includes `36518f07` | yes (fetch performed) |
| Staged | empty |
| Untracked tools (authority) | 3 foreign verification `.py` — **not committed** |
| Dirty main | foreign WIP — **read-only**; **0 mutations** |
| Authority commit safety | **SAFE** for exact harness tool/report/docs commit |

Evidence: Storage `preflight/`.

## 4. Evidence base

From Runs **4.289–4.292**:

| Fact | Status |
|------|--------|
| Leaf-name collision | **CONFIRMED** |
| 1C group GUIDs | **AVAILABLE** |
| Nested full paths | **AVAILABLE** |
| DB category external id | **ABSENT** |
| Product `xml_id` | **PRESENT** |
| Reparent (4.290) | **DONE** |
| Persistence after next import | **NOT PROVEN** |

Evidence: Storage `reports-read/`.

## 5. Source/XML input discovery

| Field | Value |
|-------|--------|
| Live source | `public_html/1c_incoming/webdata/import0_1.xml` |
| Access | FTP RETR read-only |
| Bytes | 10637418 |
| SHA-256 | `b7d4343d968a9b14…` (full in Storage meta) |
| Parse | **104** groups, **1562** products |
| Group tree | YES |
| Product↔group refs | YES |
| Stale local copy | Lari `import0_1.xml` (2026-07-09, ~7.9MB) — **not** used as primary |

Evidence: Storage `source-discovery/`, `xml-input/` (raw XML **not** committed).

## 6. DB readonly snapshot

SSH `mysql` SELECT only (6 queries). Snapshot under Storage `db-readonly/`:

| Artifact | Content |
|----------|---------|
| `categories-snapshot.csv` | 241 categories + paths + direct/subtree counts |
| `products-critical-snapshot.csv` | 4707/4708/4709/4710/4712 |
| `product-category-relations-snapshot.csv` | focus + tech/legacy relation rows |
| `leaf-name-collisions-db.csv` | DB duplicate leaf names |

DB writes: **0**. Credentials: not included.

## 7. Harness implementation

Tool (authority repo):

`projects/ocpilot/sites/site-002/tools/site-002-1c-category-identity-harness.py`

Capabilities:

- Parse CommerceML groups (`<Ид>`, name, parent, full path, leaf)
- Parse products (XML id, name, group GUID refs, resolved paths)
- Snapshot-mode analysis (`--xml` + `--db-snapshot-dir`)
- Optional `--fetch-live` (FTP XML + SSH SELECT → Storage, then analyze)
- Outputs: `source-groups.json`, `source-products.json`, `db-category-index.json`, `proposed-category-map.csv`, `proposed-product-map.csv`, `leaf-collisions.csv`, `critical-products.csv`, `summary.json` / `summary.md`

No production writes.

## 8. Harness run

| Field | Value |
|-------|--------|
| Command | Storage `harness/harness-command.txt` |
| Exit code | **0** |
| Log | `harness/harness-run.log` |
| Output dir | Storage `harness-output/` |
| Verdict from tool | Leaf creation needed before backfill |

## 9. Critical product validation

Classification: `CRITICAL_PRODUCTS_CREATE_LEAF_REQUIRED`

| ID | Name | 1C path | Current DB | Proposed interim | Old importer risk | Action |
|----|------|---------|------------|------------------|-------------------|--------|
| 4707 | Мясорубка TC-12 | … > Мясорубки | **373** | **373** | **154** | WOULD_REVERT_TO_LEGACY_UNDER_OLD_IMPORTER |
| 4708 | Мясорубка TC-22 | … > Мясорубки | **373** | **373** | **154** | WOULD_REVERT_TO_LEGACY_UNDER_OLD_IMPORTER |
| 4709 | Слайсер ТТ-М29С | … > Слайсеры для мяса | **376** | **376** | 376 | **KEEP** |
| 4710 | Пила JG 210A | … > Пилы для мяса | **373** | **373** | **159** | WOULD_REVERT_TO_LEGACY_UNDER_OLD_IMPORTER |
| 4712 | Хлеборезка ТТ-D7C | … > Хлеборезки | **375** | **375** | **165** | WOULD_REVERT_TO_LEGACY_UNDER_OLD_IMPORTER |

Run 4.290 relations still hold. Canonical tech leaves for Мясорубки / Пилы для мяса / Хлеборезки are **missing** in OC.

Evidence: Storage `critical-products/`.

## 10. Collision analysis

Focus:

| Leaf | Source GUID | Old importer target | Proposed safe (interim) | Create leaf? |
|------|-------------|---------------------|-------------------------|--------------|
| Мясорубки | `7e43262d-…` | 154 | 373 | **YES** |
| Пилы для мяса | `95003163-…` | 159 | 373 | **YES** |
| Хлеборезки | `41a86281-…` | 165 | 375 | **YES** |
| Слайсеры для мяса | `e0b6bb6d-…` | 376 | 376 | NO |

DB duplicate leaf-name count: **9** (see `leaf-collisions.csv`).

Evidence: Storage `collision-analysis/`.

## 11. Proposed map for future backfill

Dry-run only — **not applied**.

| Action | Count (approx) |
|--------|----------------|
| BACKFILL_MAPPING | 100 |
| CREATE_CATEGORY_THEN_MAP | 4 |
| IGNORE_LEGACY | 153/154/159/165 |

Hubs already backfill-ready: **362 / 373 / 375 / 376**.

Leaf GUIDs requiring create-then-map (or interim hub map + later rebind):

- `7e43262d-…` Мясорубки → interim 373
- `95003163-…` Пилы для мяса → interim 373
- `41a86281-…` Хлеборезки → interim 375

Evidence: Storage `proposed-map/`.

## 12. Phase 2 readiness

| Question | Answer |
|----------|--------|
| XML parsed? | **YES** |
| GUIDs stable? | **YES** |
| Critical products resolved? | **PARTIAL** (hubs yes; leaves no) |
| Collisions identified? | **YES** |
| Canonical leaves missing? | **YES** |
| Safe mapping backfill without product moves? | **YES for hubs**; leaves need create or interim hub rows |
| HITL needed? | **YES** — leaf creation charter vs interim-hub-only map |

Next phase classification: `READY_FOR_LEAF_CREATION_CHARTER`.

Evidence: Storage `validation/`.

## 13. Production mutation summary

- FTP writes: **0** (RETR only)
- DB writes: **0**
- Admin saves: **0**
- Import runs: **0**
- Scheduler changes: **0**
- Monitor baseline changes: **0**
- Category deletes/disables: **0**
- Product/category relation changes: **0**
- Source deploys: **0**
- Cache clears: **0**
- OCMOD refresh: **0**
- Dirty main changes: **0**

## 14. Git/worktree summary

| Item | Value |
|------|--------|
| Authority | `X:\AI MARS STORAGE\git-sync-e01\repo` |
| Branch | `site-002-git-authority-realign-after-wave-e` |
| Base HEAD | `36518f07` |
| Dirty main | inspected read-only only |
| Commit scope | harness tool + report + docs only |
| Not committed | Storage artifacts, raw XML, DB snapshots, foreign untracked tools |

## 15. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-CATEGORY-IDENTITY-HARNESS-01\`

Subfolders populated: `preflight`, `reports-read`, `source-discovery`, `xml-input`, `db-readonly`, `harness`, `harness-output`, `critical-products`, `collision-analysis`, `proposed-map`, `validation`, `reports`, `manifests`, `logs`.

## 16. SAFE UNKNOWN / blockers

- Live importer FTP bytes not re-diffed this run (classification still uses Run 4.292 charter capture).
- Exact PHP leaf-index collision order (first vs last wins) remains implementation-detail; risk to legacy 154/159/165 is confirmed either way.
- One additional `CREATE_REQUIRED` group beyond the three focus leaves exists in harness output — review in leaf-creation charter.
- Persistence after next scheduled import still **not proven**.

No hard blocker for harness completeness.

## 17. Final verdict

**`SITE-002 1C CATEGORY IDENTITY HARNESS COMPLETE — LEAF CREATION NEEDED BEFORE BACKFILL`**

## 18. Next recommendation

1. Operator HITL: approve **leaf creation charter** for tech leaves Мясорубки / Пилы для мяса / Хлеборезки (parents 373 / 375), **or** approve interim hub GUID→373/375 mapping rows plus collision guard.
2. Phase 2: create mapping table + backfill **without product moves**.
3. Phase 3: importer GUID → path → create; never leaf-match into 154/159/165 under tech source tree.
4. Dry-run simulation → controlled apply → persistence check after next import.
5. Legacy cleanup remains separate HITL.
