# REPORT — SITE-002 New Sections Wave B Mapping Charter 01

## 1. Scope

- Operation: `SITE-002-PROD-NEW-SECTIONS-WAVE-B-MAPPING-CHARTER-01`
- Mode: read-only mapping charter and future apply planning
- Target site: `SITE-002` / ЗПМ Production
- Working repo authority: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`
- Production mutation in this run: forbidden and not performed

## 2. Operator approval

Operator approval used:

`Ок, утверждаю. Жду промт.`

Interpretation honored:

- proceed with Wave B mapping charter;
- do not execute mapping apply;
- do not create or move categories;
- do not refresh baseline;
- produce exact future mapping/apply plan only.

## 3. Client Ops boundary

Untouched:

- Client Ops: `0`
- n8n: `0`
- Telegram: `0`
- production DB writes: `0`
- production FTP writes: `0`
- import runs: `0`
- baseline refresh: `0`
- importer/source deploys: `0`
- dirty main mutations: `0`
- `docs-01` / `docs-02`: `0`

## 4. Preflight

Re-checked in current authority worktree:

- path: `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`
- volume label: `AI WS`
- branch: `docs/site002-offers-recovery-healthcheck-03` (task-authorized worktree)
- `git status --short`: clean
- `git status --branch --porcelain=v2`: `branch.ab +0 -0`
- `HEAD`: `b4fda02fa57eccd6c0ff3f99d0be8e51f45516ea`
- `origin/mars/canonical-post-recovery`: `b4fda02fa57eccd6c0ff3f99d0be8e51f45516ea`

Saved:

- `preflight/git-state.txt`
- `preflight/origin-state.txt`

## 5. Current state after Wave A

Upstream basis preserved:

- healthcheck Run `4.325`: offers recovered; sitemap `1887`; baseline `1879`
- placement charter Run `4.326`: safe strategy `KEEP_DB_PLACEMENT_AND_SEPARATE_UI_FROM_STRUCTURE`
- Wave A Run `4.327`: bounded onboarding only for `186.description`, `95.meta_description`, `95.description`

Still true after this review:

- `barnoe-oborudovanie` remains live but empty
- `hlebopekarnoe-oborudovanie` remains live/root with products
- `holodilnoe-oborudovanie` remains live/root with products
- `posuda-i-inventar` remains DB-child under `362`
- `upakovochnoe-oborudovanie` remains absent from DB/site/sitemap
- baseline refresh remains blocked

## 6. Reports read

Reviewed required authority documents and prior reports, including:

- `SITE-002-PROD-POST-1C-OFFERS-RECOVERY-AND-NEW-SECTIONS-HEALTHCHECK-01`
- `SITE-002-PROD-NEW-SECTIONS-ONBOARDING-PLACEMENT-CHARTER-01`
- `SITE-002-PROD-NEW-SECTIONS-WAVE-A-ONBOARDING-APPLY-01`
- `SITE-002-PROD-1C-CATEGORY-IDENTITY-HARNESS-01`
- `SITE-002-PROD-1C-CANONICAL-LEAF-CREATION-CHARTER-01`
- `SITE-002-PROD-1C-CANONICAL-LEAF-APPLY-01`
- `SITE-002-PROD-1C-CATEGORY-MAPPING-BACKFILL-01`
- `SITE-002-PROD-1C-IMPORTER-GUID-PATH-PATCH-01`
- `SITE-002-PROD-1C-POST-IMPORT-PERSISTENCE-CHECK-01`

Saved summaries:

- `reports-read/category-identity-design-summary.md`
- `reports-read/importer-behavior-summary.md`
- `reports-read/current-new-sections-summary.md`

## 7. XML parse

Current live `import0_1.xml` was re-fetched read-only and parsed through the current harness flow.

Confirmed top-level XML groups now are:

1. `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`
2. `ПОСУДА И ИНВЕНТАРЬ`
3. `ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ`
4. `НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ`
5. `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ`

Key Wave B XML facts:

- `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`
  - GUID: `5bc6a012-7c19-11f1-aecc-581122cf362c`
  - top-level: yes
  - subtree products: `1`
- `ПОСУДА И ИНВЕНТАРЬ`
  - GUID: `9b37b1f1-7c19-11f1-aecc-581122cf362c`
  - top-level: yes
  - subtree products: `6`
- `ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ`
  - GUID: `95bfa611-898d-11f1-aece-581122cf362c`
  - top-level: yes
  - subtree products: `1`
- `НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ`
  - GUID: `25a2ee03-cec7-11e9-95c9-60a44cac3e7c`
  - top-level: yes
- `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ`
  - GUID: `e0fd5c42-a3b8-11ea-8152-a85e4515c4f4`
  - top-level: yes
- `БАРНОЕ ОБОРУДОВАНИЕ`
  - no match in current XML parse
- `ХЛЕБОПЕКАРНОЕ ОБОРУДОВАНИЕ`
  - no match in current XML parse
- but current XML does contain nested `Хлебопекарное`
  - GUID: `5430c2fe-7c19-11f1-aecc-581122cf362c`
  - path: `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Хлебопекарное`

Saved:

- `xml-parse/target-xml-groups.csv`
- `xml-parse/xml-top-level-groups.csv`
- `xml-parse/xml-parse-summary.md`

## 8. DB category map

Read-only DB snapshot confirms:

- `79` `Нейтральное оборудование`
  - root
  - subtree products: `1608`
- `362` `Технологическое оборудование`
  - root
  - subtree products: `31`
- `171` `Барное оборудование`
  - root
  - subtree products: `0`
- `186` `Хлебопекарное оборудование`
  - root
  - subtree products: `12`
- `95` `Холодильное оборудование`
  - root
  - subtree products: `1`
- `364` `Посуда и инвентарь`
  - `parent_id=362`
  - direct products: `6`
  - public URL still `https://bzpm.ru/posuda-i-inventar`

`Упаковочное` search result:

- no matching current DB category found
- no current `upakovochnoe-oborudovanie` public category target

Saved:

- `db-readonly/target-db-categories.csv`
- `db-readonly/upakovochnoe-search.csv`
- `db-readonly/db-category-summary.md`

## 9. Mapping table read-only

Current `oc_mars_1c_category_map` state:

- table exists
- current active evidence remains on prior tech/canonical scope
- confirmed current existing mapped root from Wave B target set: `362`
- no current rows found for:
  - `79`
  - `171`
  - `186`
  - `95`
  - `364`
  - `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`

Meaning:

- `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ` is already covered
- the Wave B decision is primarily about whether to backfill `95` and `364`, and whether `171` / `186` should stay unmapped for now

Saved:

- `mapping-table-readonly/current-map-rows.csv`
- `mapping-table-readonly/target-map-status.csv`
- `mapping-table-readonly/mapping-table-summary.md`

## 10. Importer source review

Live importer files were fetched read-only and the current behavior matches the prior patched design:

- category resolution order remains:
  1. GUID map
  2. path hash
  3. normalized DB full path
  4. safe leaf-name only
  5. review
- auto-create is still disabled
- collision guard still blocks unsafe tech legacy matches
- `import_1C_process.php` preserves existing `product_to_category` on update when categories are unresolved

Wave B implications:

- missing mapping does not auto-create a new public category
- unresolved update does not blindly destroy existing category placement
- direct GUID backfill is the safest identity bridge when XML path and DB path differ

Saved:

- `importer-source-review/importer-source-findings.md`
- `importer-source-review/importer-risk-summary.md`

## 11. Group/category match

Final Wave B matching status:

| XML / category target | Status | Decision |
|---|---|---|
| `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ` -> `362` | `KEEP_EXISTING_MAPPING` | already mapped |
| `ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ` -> `95` | `MAP_TO_EXISTING_CATEGORY` | ready for bounded B1 backfill |
| `ПОСУДА И ИНВЕНТАРЬ` -> `364` | `MAP_TO_EXISTING_CATEGORY` | safe to map without parent move |
| `ХЛЕБОПЕКАРНОЕ ОБОРУДОВАНИЕ` -> `186` | `MAPPING_COLLISION_RISK` | do not backfill yet; current XML proves nested `Хлебопекарное` under Tech and overlaps with existing `368` |
| `БАРНОЕ ОБОРУДОВАНИЕ` -> `171` | `DO_NOT_MAP_YET` | current XML does not prove matching bar group |
| `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ` | `DO_NOT_MAP_YET` | XML-only; no DB target; auto-create disabled |
| `НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ` -> `79` | `DO_NOT_MAP_YET` | not a required new Wave B identity correction on current evidence |

Saved:

- `group-category-match/group-category-match.csv`
- `group-category-match/group-category-match-summary.md`

## 12. Collision/risk review

Primary Wave B risks:

1. `posuda-i-inventar`
   - XML is top-level
   - DB category remains child of `362`
   - path-only matching is risky
   - GUID row to `364` is safe if exact GUID is approved
2. `hlebopekarnoe-oborudovanie`
   - root `186` already exists live
   - current XML proves nested `Хлебопекарное` under Tech
   - overlap with existing `368` makes root backfill unsafe without separate identity decision
3. `barnoe-oborudovanie`
   - live root exists
   - no current XML proof of corresponding group
   - mapping now would be speculative
4. `upakovochnoe-oborudovanie`
   - XML product evidence exists
   - importer still cannot materialize it because auto-create is disabled and no DB target exists

Saved:

- `collision-review/collision-risk-matrix.csv`
- `collision-review/collision-risk-summary.md`

## 13. Recommendations

Bounded recommendation set:

- `95` / `ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ`
  - recommended action: `BACKFILL_GUID_MAP_TO_EXISTING_CATEGORY`
- `364` / `ПОСУДА И ИНВЕНТАРЬ`
  - recommended action: `BACKFILL_GUID_MAP_TO_EXISTING_CATEGORY`
  - explicit note: map to existing category while keeping `parent_id=362`
- `186` / `ХЛЕБОПЕКАРНОЕ ОБОРУДОВАНИЕ`
  - recommended action: `DO_NOT_MAP_YET`
  - reason: current XML identity points to nested Tech branch, not proven root twin
- `171` / `БАРНОЕ ОБОРУДОВАНИЕ`
  - recommended action: `DO_NOT_MAP_YET`
  - reason: no current XML proof
- `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`
  - recommended action: `DO_NOT_CREATE_DO_NOT_MAP_YET`
  - note: XML product evidence exists, but create/mapping remain blocked until explicit approval
- `362`
  - keep existing mapping
- `79`
  - no Wave B change on current evidence

Saved:

- `recommendations/mapping-recommendations.csv`
- `recommendations/recommendation-summary.md`

## 14. Future apply plan

### Wave B1

Ready after approval:

- bounded mapping-table backfill only for:
  - `95`
  - `364`
- no parent moves
- no category creation
- no product changes
- no importer change
- no baseline refresh

### Wave B2

Blocked pending operator decision:

- `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`
- separate create-then-map path only if operator explicitly approves a new category target

### Wave B3

Current verdict:

- no new importer patch is required before B1 on current evidence
- existing importer logic already supports GUID-first resolution and preserve-on-unresolved updates
- B3 becomes necessary only if post-B1 validation proves unexpected unresolved behavior

Saved:

- `future-apply-plan/wave-b1-mapping-backfill-apply-plan.md`
- `future-apply-plan/wave-b2-upakovochnoe-plan.md`
- `future-apply-plan/wave-b3-importer-patch-plan.md`
- `future-apply-plan/not-executed.md`

## 15. Docs update

This charter updates canonical documentation status only:

- Wave B mapping charter created
- no production mapping apply performed
- safe B1 scope narrowed to `95` and `364`
- `186` root mapping deferred due XML/DB identity overlap with `368`
- `171` remains unmapped because matching XML proof is absent
- `upakovochnoe` remains blocked from create/map
- baseline remains blocked
- next waves remain B1 apply approval and Wave C monitor diagnostic

## 16. Regression/mutation summary

All forbidden production mutations stayed at `0`:

- DB writes: `0`
- FTP writes: `0`
- import runs: `0`
- cache clear: `0`
- OCMOD refresh: `0`
- mapping table changes: `0`
- importer changes: `0`
- category/product changes: `0`
- baseline refresh: `0`
- Client Ops / n8n / Telegram changes: `0`

Saved:

- `regression/mutation-summary.csv`
- `regression/regression-summary.md`

## 17. Git/worktree summary

- authority worktree remained clean before docs mutation
- dirty main was not touched
- this run is docs/report + Storage-artifact only
- commit/push handled separately after exact doc review

## 18. Storage artifacts

Root:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-WAVE-B-MAPPING-CHARTER-01\`

Key outputs:

- `manifests/operation.json`
- `xml-parse/target-xml-groups.csv`
- `db-readonly/target-db-categories.csv`
- `mapping-table-readonly/current-map-rows.csv`
- `group-category-match/group-category-match.csv`
- `recommendations/mapping-recommendations.csv`
- `future-apply-plan/wave-b1-mapping-backfill-apply-plan.md`

## 19. SAFE UNKNOWN / blockers

- `НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ` root mapping necessity for Wave B is not proven as required on current evidence.
- `БАРНОЕ ОБОРУДОВАНИЕ` matching current 1C GUID/path is `SAFE UNKNOWN` because no current XML group match was found.
- `hlebopekarnoe-oborudovanie` root `186` versus nested Tech `368` requires separate operator/1C identity decision before mapping apply.
- live monitor artifact semantic inconsistency from Run `4.325` remains unresolved at the documentation level; Wave C diagnostic is still required.

## 20. Final verdict

`SITE-002 NEW SECTIONS WAVE B MAPPING CHARTER COMPLETE — BACKFILL PLAN READY, BASELINE STILL BLOCKED`

Classifications:

- `WAVE_B_MAPPING_CHARTER_COMPLETE`
- `WAVE_B1_MAPPING_BACKFILL_READY`
- `WAVE_B2_UPAKOVOCHNOE_BLOCKED_OR_READY`: `BLOCKED`
- `WAVE_B3_IMPORTER_PATCH_NEEDED_OR_NOT`: `NOT_NEEDED_FOR_B1_BASED_ON_CURRENT_EVIDENCE`
- `BASELINE_REFRESH_STILL_BLOCKED`
- `MONITOR_DIAGNOSTIC_STILL_REQUIRED`

## 21. Next recommendation

1. `READY_FOR_WAVE_B1_MAPPING_BACKFILL_APPLY_AFTER_APPROVAL` for bounded rows `95` and `364` only.
2. Keep `186` out of B1 until root-vs-`368` identity is explicitly resolved.
3. Keep `171` unmapped until matching XML proof appears.
4. `READY_FOR_WAVE_C_MONITOR_DIAGNOSTIC`
5. `DO_NOT_REFRESH_BASELINE_YET`
