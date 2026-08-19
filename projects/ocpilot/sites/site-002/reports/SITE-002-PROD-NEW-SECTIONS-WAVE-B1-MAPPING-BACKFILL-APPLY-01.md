# REPORT — SITE-002 New Sections Wave B1 Mapping Backfill Apply 01

## 1. Scope

Operation: `SITE-002-PROD-NEW-SECTIONS-WAVE-B1-MAPPING-BACKFILL-APPLY-01`  
Mode: bounded production mapping backfill apply  
Target site: SITE-002 / ЗПМ Production  
Authority worktree: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`

Allowed production mutation:

- `oc_mars_1c_category_map` rows only for:
  - `95` `holodilnoe-oborudovanie`
  - `364` `posuda-i-inventar`

Forbidden and not performed:

- category create/move/delete
- product changes
- importer/source changes
- baseline refresh
- FTP writes
- import runs
- Client Ops / n8n / Telegram

## 2. Operator approval

Operator approval recorded as:

`Ок, утверждаю. Жду промт.`

Interpretation honored:

- proceed with bounded Wave B1 mapping backfill;
- apply only `95` and `364`;
- do not map `186`, `171`, or `upakovochnoe`;
- do not refresh baseline.

## 3. Client Ops boundary

Untouched:

- Client Ops: `0`
- n8n: `0`
- Telegram: `0`
- unrelated MARS dirty main: `0`
- `docs-01` / `docs-02`: `0`

## 4. Preflight

Re-checked in authority worktree:

- path: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`
- volume label: `AI WS`
- branch: `docs/site002-offers-recovery-healthcheck-03`
- `git status --short`: clean
- `HEAD`: `57d2d53c6c7905d887855bf8206a67cfa71074fa` (Wave B charter commit)
- `origin/mars/canonical-post-recovery`: `c62b89d74764e05cc4f7ea1ba0a47356d2b1baa2` (1 unrelated commit ahead — FP-0002; no conflict for docs push after pull/rebase)

Saved:

- `preflight/git-state.txt`
- `preflight/origin-state.txt`

## 5. Charter basis

Upstream charter:

- `SITE-002-PROD-NEW-SECTIONS-WAVE-B-MAPPING-CHARTER-01`
- commit: `57d2d53c6c7905d887855bf8206a67cfa71074fa`

Wave B decision preserved:

- B1 = GUID map backfill for `95` and `364` only
- `186` deferred (nested Tech `Хлебопекарное` / overlap with `368`)
- `171` unmapped (no XML proof)
- `upakovochnoe` blocked (no DB target; auto-create off)
- baseline remains blocked

## 6. XML parse

Source: Wave B charter `import0_1.xml` (read-only re-parse).

| Category | XML group | GUID | Path | Top-level | Products |
|----------|-----------|------|------|-----------|----------|
| `95` | ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ | `95bfa611-898d-11f1-aece-581122cf362c` | `ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ` | yes | 1 |
| `364` | ПОСУДА И ИНВЕНТАРЬ | `9b37b1f1-7c19-11f1-aecc-581122cf362c` | `ПОСУДА И ИНВЕНТАРЬ` | yes | 6 |

Gate: **PASS** — both targets confirmed.

Saved:

- `xml-parse/wave-b1-target-xml-groups.csv`
- `xml-parse/xml-target-summary.md`

## 7. DB before

### Target categories

| category_id | name | parent_id | status | keyword | direct products |
|-------------|------|-----------|--------|---------|-----------------|
| `95` | Холодильное оборудование | `0` | `1` | `holodilnoe-oborudovanie` | `1` |
| `364` | Посуда и инвентарь | `362` | `1` | `posuda-i-inventar` | `6` |

### Excluded categories (read-only)

- `79`, `362`, `171`, `186`, `368` — present and unchanged; no B1 writes planned or performed.

Gate: **PASS**

Saved:

- `db-before/target-categories-before.csv`
- `db-before/excluded-categories-before.csv`
- `db-before/db-before-summary.md`

## 8. Mapping before

`oc_mars_1c_category_map` before apply:

- table existed with **7** prior rows (tech/canonical leaf scope from Run 4.296)
- **no** existing rows for categories `95` or `364`
- **no** GUID collision for target XML GUIDs

Gate: **PASS**

Saved:

- `mapping-before/target-mapping-before.csv` (empty for targets)
- `mapping-before/guid-collision-check.csv`
- `mapping-before/excluded-mapping-before.csv`
- `mapping-before/mapping-before-summary.md`

## 9. Rollback prep

Rollback covers insert-only case (no prior rows for `95`/`364`):

```sql
DELETE FROM `oc_mars_1c_category_map`
WHERE `source_group_id` IN (
  '95bfa611-898d-11f1-aece-581122cf362c',
  '9b37b1f1-7c19-11f1-aecc-581122cf362c'
);
```

Saved:

- `rollback/mapping-before-rows.sql`
- `rollback/rollback-plan.md`

## 10. Apply plan

Exact SQL: 2 upsert rows into `oc_mars_1c_category_map` with:

- `confidence`: `HIGH_GUID_AND_PATH`
- `status`: `active`
- computed `source_full_path_hash`

Saved:

- `apply-plan/wave-b1-apply.sql`
- `apply-plan/apply-plan-summary.md`

## 11. DB apply

Executed bounded SQL at `2026-08-19T16:26:42Z` (UTC).

Result:

- **2** new mapping rows inserted
- table total: **7 → 9**
- no errors

Saved:

- `db-apply/db-apply-console.txt`
- `db-apply/db-apply-summary.md`
- `db-apply/applied.sql`

## 12. Mapping after verification

| map_id | category_id | source_group_id | source_name | source_full_path | status |
|--------|-------------|-----------------|-------------|------------------|--------|
| `8` | `95` | `95bfa611-898d-11f1-aece-581122cf362c` | ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ | ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ | active |
| `9` | `364` | `9b37b1f1-7c19-11f1-aecc-581122cf362c` | ПОСУДА И ИНВЕНТАРЬ | ПОСУДА И ИНВЕНТАРЬ | active |

Verified:

- both target rows active and GUID-correct
- excluded category map rows unchanged
- no GUID collision
- category `364` still `parent_id=362` (no placement move)

Gate: **PASS**

Saved:

- `mapping-after/target-mapping-after.csv`
- `mapping-after/excluded-mapping-after.csv`
- `mapping-after/mapping-after-summary.md`

## 13. Public HTTP / sitemap smoke

| URL | Status | Notes |
|-----|--------|-------|
| `/holodilnoe-oborudovanie` | `200` | unchanged |
| `/posuda-i-inventar` | `200` | unchanged |
| `/hlebopekarnoe-oborudovanie` | `200` | unchanged |
| `/barnoe-oborudovanie` | `200` | unchanged, not promoted |
| `/upakovochnoe-oborudovanie` | `404` | expected — still absent |
| `/sitemap.xml` | `200` | unchanged |

Gate: **PASS**

Saved:

- `public-http/public-smoke.csv`
- `public-http/public-http-summary.md`
- `sitemap/sitemap-after-summary.md`

## 14. Regression / mutation summary

| Mutation class | Count |
|----------------|-------|
| categories created | `0` |
| parent moves | `0` |
| product changes | `0` |
| importer changes | `0` |
| mapping rows for excluded categories | `0` |
| mapping rows added (approved) | `2` |
| FTP writes | `0` |
| import runs | `0` |
| cache clear | `0` |
| baseline refresh | `0` |
| monitor changes | `0` |
| Client Ops / n8n / Telegram | `0` |
| dirty main changes | `0` |
| docs-01/docs-02 touched | `0` |

Gate: **PASS**

Saved:

- `regression/mutation-summary.csv`
- `regression/regression-summary.md`

## 15. Git/worktree summary

- authority worktree clean before docs mutation
- production apply performed from Storage deployment script (not committed to repo)
- docs/report commit handled separately
- origin was 1 commit ahead (unrelated FP-0002) — sync before push required

## 16. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-WAVE-B1-MAPPING-BACKFILL-APPLY-01\`

Key outputs:

- `manifests/operation.json`
- `xml-parse/wave-b1-target-xml-groups.csv`
- `db-before/target-categories-before.csv`
- `mapping-before/mapping-before-summary.md`
- `rollback/mapping-before-rows.sql`
- `apply-plan/wave-b1-apply.sql`
- `mapping-after/target-mapping-after.csv`
- `public-http/public-smoke.csv`
- `decision/decision.md`

## 17. SAFE UNKNOWN / blockers

- Post-B1 import persistence not yet validated on next natural 1C run — expected stable but not proven in this run.
- Monitor artifact semantic inconsistency from Run 4.325 remains unresolved — Wave C diagnostic still required.
- `upakovochnoe` create/map remains a separate operator decision.
- `186` root vs nested `368` identity remains unresolved.

## 18. Final verdict

**SITE-002 NEW SECTIONS WAVE B1 MAPPING BACKFILL COMPLETE — 95 AND 364 MAPPED, BASELINE STILL BLOCKED**

Classifications:

- `WAVE_B1_MAPPING_BACKFILL_COMPLETE`
- `BASELINE_REFRESH_STILL_BLOCKED`
- `READY_FOR_WAVE_C_MONITOR_DIAGNOSTIC`
- `UPAKOVOCHNOE_REMAINS_SEPARATE`

## 19. Next recommendation

1. `READY_FOR_WAVE_C_MONITOR_DIAGNOSTIC`
2. `DO_NOT_REFRESH_BASELINE_YET`
3. Observe next natural 1C import for GUID resolution on categories `95` and `364`
4. Keep `186` / `171` / `upakovochnoe` out of mapping until separate charter/approval
