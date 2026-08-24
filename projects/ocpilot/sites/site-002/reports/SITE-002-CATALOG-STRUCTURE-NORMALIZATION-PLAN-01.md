# REPORT — SITE-002 Catalog Structure Normalization Plan 01

**Operation:** `SITE-002-CATALOG-STRUCTURE-NORMALIZATION-PLAN-01`  
**OCPilot run:** **4.341**  
**Date:** 2026-08-24  
**Environment:** `CATALOG_STRUCTURE_NORMALIZATION_PLAN_DOCS_ONLY`  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-STRUCTURE-NORMALIZATION-PLAN-01\`

**Final verdict:** `SITE-002 CATALOG STRUCTURE NORMALIZATION PLAN COMPLETE — OPERATOR DECISIONS REQUIRED BEFORE APPLY`

**Classifications:**

- `SITE_002_CATALOG_STRUCTURE_NORMALIZATION_PLAN_COMPLETE`
- `PLAN_ONLY_PRODUCTION_MUTATION_ZERO`
- `STRUCTURE_ATTENTION_CONFIRMED`
- `STRICT_1C_MODEL_OPTION_READY`
- `SEO_UI_EXCEPTION_MODEL_OPTION_READY`
- `HYBRID_RECOMMENDED_MODEL_READY`
- `OPERATOR_DECISIONS_REQUIRED_BEFORE_APPLY`
- `ZAPCHASTI_DRILLDOWN_REQUIRED`
- `CLEANUP_DEFERRED`
- `SAFE_UNKNOWN` (limited — see §20)

---

## 1. Scope

Create a safe operator decision plan for aligning the SITE-002 Production catalog tree with the latest 1C group tree after comparison audit `SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01` (`4e5442cd`).

This wave produces diagnosis, target options, decision matrix, SEO/mapping/UI plans, Zapchasti drilldown plan, and bounded future apply phases. **No apply.**

## 2. Operator approval

Operator approved planning after the comparison audit with: `ок, давай`.

Context: fresh read-only comparison concluded **STRUCTURE ATTENTION REQUIRED BEFORE APPLY**. Operator wants to compare site root sections with latest 1C groups and decide how to clean/normalize — **plan first**.

## 3. Read-only / plan-only boundary

**Forbidden and not performed:** production DB writes; FTP writes; 1C import runs; cache clear; OCMOD refresh; category/product changes; mapping table changes; importer/monitor/baseline/runtime/scheduler changes; Client Ops/n8n/Telegram; cleanup/delete; docs-01/docs-02; dirty main mutation; broad git staging.

**Allowed and performed:** Storage evidence; docs/plan/report; minimal OCPilot index/state/knowledge updates.

## 4. Authority preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority path | `git-sync-site002-offers-recovery-docs-03\repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` → `origin/mars/canonical-post-recovery` |
| Start HEAD | `4e5442cd` (**2 behind** origin) |
| Sync | `git fetch` + `git merge --ff-only` → `b4e6daea` |
| Behind commits | ISEO-only (`0d117722`, `b4e6daea`) — safe FF |
| Status after FF | clean; HEAD = origin |
| Staged | empty |

Evidence: Storage `preflight/authority-git-state.txt`, `preflight/authority-origin-state.txt`.

## 5. Current accepted evidence

| Artifact | Commit / fact |
|---|---|
| Catalog export | `SITE-002-CATALOG-TREE-CURRENT-EXPORT-01` (`ab4f90a5`) |
| Artifact repair | `SITE-002-CATALOG-TREE-ARTIFACT-REPAIR-01` (`2ba66a22`) |
| Comparison audit | `SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01` (`4e5442cd`) |
| Healthcheck | `SITE-002-POST-IMPORT-AND-MONITOR-HEALTHCHECK-01` (`f93eabf8`) |
| Site DB | 226 cats / 225 active / 1 inactive / 10 roots / depth 3 |
| Sitemap | 1887 / 1887; active cats 225/225 |
| 1C latest import | `2026-08-24` SUCCESS; 111 groups; 5 roots; 1647 products |
| Mapping | 9 active rows; `95`/`364` persistence confirmed |
| Prior waves | B1 mapped `95`/`364`; `186`/`171`/`upakovochnoe` deferred |

## 6. Structure diagnosis

### Matches 1C

- `[79]` Neutral — path-matched root (~1533 enabled)
- `[95]` Holodilnoe — GUID-mapped root
- `[362]` Tech — GUID-mapped root + mapped Tech leaves

### Nested differently

- `[364]` Posuda — GUID = 1C **root**, site parent = Tech
- `[90]` Teplovoe root vs 1C Tech→Тепловое (also site `[369]`)
- `[186]` Hlebo root vs 1C Tech→Хлебопекарное (also site `[368]`)

### Site-only

- Empty active: `93`, `171`, `205`, `206`
- Non-empty active: `90` (4), `186` (12)
- Inactive with products: `96` Запчасти (76), public 404

### 1C-only

- Root `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ` (1 product) — site absent, URL 404
- Five stellazhi «решетчатые полки» leaves (lower priority)

### URL risks

- Posuda nested canonical in sitemap; flat `/posuda-i-inventar` live alias without redirect
- `/brands/assum` generic vs `/assum` canonical
- Root→nested moves for Teplovoe/Hlebo need 301 plans

Full write-up: Storage `diagnosis/structure-diagnosis.md`.

## 7. Target model options

### Option A — Strict 1C hierarchy

Public roots = 5× 1C roots; Teplovoe/Hlebo under Tech; hide empty site-only; create Upakovochnoe. **Pros:** single SoT. **Cons:** highest SEO churn. **Ready** as long-term ideal.

### Option B — Preserve SEO/UI roots with documented exceptions

Keep Teplovoe/Hlebo (and possibly nested Posuda) as public exceptions. **Pros:** low short-term SEO risk. **Cons:** permanent dual taxonomy / mapping collisions. **Ready** only with explicit client approval of exceptions.

### Option C — Hybrid (recommended)

1C preferred for existence/hierarchy; preserve old SEO URLs via 301; create Upakovochnoe; hide empties after checks; Zapchasti only after drilldown; mapping/category moves in separate bounded applies; baseline refresh last.

| Option | Recommendation |
|---|---|
| A | Ready — long-term |
| B | Ready — temporary/exception path |
| **C** | **Recommended default** |

Details: Storage `target-models/target-model-options.md`.

## 8. Recommended target model

**Hybrid Option C.**

Public roots (target): Neutral, Holodilnoe, Tech, Posuda (promoted unless exception approved), Upakovochnoe (created).  
Tech children: Хлебопекарное / Тепловое / Электромеханическое / Мясоперерабатывающее with product consolidation from legacy roots `186`/`90` when operator chooses nest/merge.  
Empty site-only roots: disable/hide, do not delete first.  
`[96]`: drilldown before any action.

## 9. Per-category decision matrix

Recommended default = Hybrid C.

| Category / group | Site state | 1C state | Enabled subtree | Sitemap / public | Issue | Recommended decision | Later apply | SEO / redirect | Mapping | Rollback | Operator decision? |
|---|---|---|---:|---|---|---|---|---|---|---|---|
| `[79] Нейтральное` | Root active | Root path-match | 1533 | yes / 200 | — | Keep root | optional GUID map | none | optional | N/A | No |
| `[95] Холодильное` | Root GUID map | Root | 1 | yes / 200 | — | Keep | none | none | preserve map_id 8 | restore map | No |
| `[362] Технологическое` | Root GUID map | Root | 21 | yes / 200 | hosts Posuda + Tech children | Keep | none at root | none | preserve map_id 1 | restore map | No |
| `[364] Посуда` | Nested under 362; GUID = 1C root | 1C root | 6 | nested in sitemap; flat alias 200 | hierarchy mismatch | Promote to root **or** approved nested exception | parent move or exception doc | nested↔flat redirect plan | preserve GUID | revert parent | **Yes** |
| `УПАКОВОЧНОЕ` | Absent | 1C root (1 prod) | 1 | 404 | missing site cat | Create + map | create+map | create URL + sitemap | new GUID map | disable+unmap | **Yes** |
| `[90] Тепловое` | Site root | 1C nested under Tech | 4 | yes / 200 | vs `[369]` | Nest/merge into Tech **or** SEO exception | move+merge+map | 301 if moved | map nested GUID | revert | **Yes** |
| `[186] Хлебопекарное` | Site root | 1C nested under Tech | 12 | yes / 200 | vs `[368]` | Nest/merge into Tech **or** SEO exception | move+merge+map | 301 if moved | map nested GUID | revert | **Yes** |
| `[368]` Tech Хлебопекарное | Nested under 362 | 1C nested candidate | 1 | yes nested | overlap 186 | Prefer 1C home after merge | map+absorb | may be redirect target | map `5430c2fe` | unmap | **Yes** (w/ 186) |
| `[369]` Tech Тепловое | Nested under 362 | 1C nested candidate | 9 | yes nested | overlap 90 | Prefer 1C home after merge | map+absorb | may be redirect target | map `65f72e7d` | unmap | **Yes** (w/ 90) |
| `[93] Инвентарь` | Empty root | none | 0 | yes / 200 empty | site-only suspect | Hide/disable (not delete) | status | menu/sitemap impact | none | re-enable | **Yes** |
| `[171] Барное` | Empty root | no current XML proof | 0 | yes / 200 empty | site-only suspect | Hide/disable or keep stub | status | menu/sitemap | none | re-enable | **Yes** |
| `[205] Посудомоечные` | Empty root | none | 0 | yes / 200 empty | site-only suspect | Hide/disable | status | menu/sitemap | none | re-enable | **Yes** |
| `[206] Вентиляционное` | Empty root | none | 0 | yes / 200 empty | site-only suspect | Hide/disable | status | menu/sitemap | none | re-enable | **Yes** |
| `[96] Запчасти` | Inactive + 76 products | none | 76 | no / 404 | products without 1C group | Drilldown first | Apply 06 after drilldown | TBD | none now | restore | **Yes after drilldown** |
| `/brands/assum` | Generic 200 | N/A | — | `/assum` canonical | brand route noise | Separate SEO task | out of tree plan | optional redirect | none | N/A | **Yes (separate)** |
| flat `/posuda-i-inventar` | Alias 200 | N/A | 6 | not in sitemap | no redirect | 301 to canonical or promote flat | with Posuda | required | preserve map | remove redirect | **Yes (w/ 364)** |

CSV twin: Storage `decision-matrix/catalog-normalization-decision-matrix.csv`.

## 10. SEO / URL plan

- Root→nested moves for `/teplovoe-oborudovanie` and `/hlebopekarnoe-oborudovanie` require **301** to nested Tech paths if Hybrid nest/merge is chosen.
- Posuda: fix flat alias (301) or promote and invert canonical.
- Create `/upakovochnoe-oborudovanie` when Apply 02 runs.
- Empty roots: prefer disable; expect sitemap shrinkage; baseline refresh only after charter.
- `/brands/assum`: out of catalog-tree scope.

Full: Storage `seo-url-plan/seo-url-normalization-plan.md`.

## 11. Mapping / import implications

- **Protect** existing 9 map rows (especially `95`, `364`, Tech leaves).
- **Later create** Upakovochnoe map (`5bc6a012-…`); map Teplovoe (`65f72e7d-…`) and Hlebo (`5430c2fe-…`) to **one** chosen site category each — no dual maps.
- Posuda: keep GUID map even if parent changes.
- **Default: no importer code patch**; keep auto-create disabled.
- Validate on next **natural** import: SUCCESS log, map persistence, no surprise categories, URL smoke.

Full: Storage `mapping-import-plan/mapping-import-implications.md`.

## 12. UI / menu / sitemap implications

- Homepage tiles / `/katalog/` / mega menu should follow approved roots; remove empty stubs after disable.
- Tech submenu should expose nested Teplovoe/Hlebo after merge.
- Sitemap/monitor: expect deltas after disable/create/moves; **no baseline refresh in plan wave**.

Full: Storage `ui-menu-sitemap-plan/ui-menu-sitemap-plan.md`.

## 13. Zapchasti drilldown plan

Separate future read-only task: list 76 products (status, SKU, price, qty, URLs), cross-check latest XML for 1C IDs, smoke PDPs, then client chooses keep-private / relocate / delete charter. **No cleanup now.**

Full: Storage `zapchasti-drilldown-plan/zapchasti-drilldown-plan.md`.

## 14. Future apply phases

| Phase | Goal | Mutation |
|---|---|---|
| Apply 01 | Freeze operator decisions | docs only |
| Apply 02 | Create+map Upakovochnoe | bounded DB |
| Apply 03 | Posuda root/nested + alias | parent/SEO/redirect |
| Apply 04 | Teplovoe / Hlebo resolve | move/merge/map/redirect |
| Apply 05 | Hide empty site-only roots | status only (no delete) |
| Apply 06 | Zapchasti action | only after drilldown |
| Apply 07 | Sitemap/monitor + optional baseline refresh | baseline charter |

Do **not** execute these phases in this wave. Full: Storage `apply-phases/future-apply-phases.md`.

## 15. Cleanup later note

No MARS/ZPM cleanup now. After catalog work, separate dry-run for docs-01/docs-02 and SITE-002 backup/tail paths — exact paths, dry-run, approval required. Storage `cleanup-later-note/cleanup-later-note.md`.

## 16. Decisions needed from operator

1. Approve Hybrid C, or choose Strict A / Exception B?
2. Posuda: promote `[364]` to root, or keep nested exception?
3. Flat `/posuda-i-inventar`: 301 vs promote-as-canonical?
4. Create Upakovochnoe (Apply 02) — yes/no?
5. Teplovoe: nest/merge with 301, or keep SEO root exception?
6. Hlebopekarnoe: nest/merge with 301, or keep SEO root exception?
7. Empty roots `93/171/205/206`: disable all, or keep any (e.g. Barnoe stub)?
8. Authorize Zapchasti read-only drilldown next?
9. `/brands/assum` redirect — now or later (separate)?
10. After applies: authorize baseline refresh when URL set stable?

Packet: Storage `decision/operator-decision-packet.md`.

## 17. Regression / mutation summary

| Forbidden action | Count |
|---|---:|
| Production DB writes | 0 |
| FTP writes | 0 |
| 1C import run | 0 |
| Cache clear / OCMOD | 0 |
| Category/product changes | 0 |
| Mapping table changes | 0 |
| Importer/monitor/baseline/runtime/scheduler | 0 |
| Client Ops / n8n / Telegram | 0 |
| Cleanup/delete | 0 |
| docs-01 / docs-02 | 0 |

Allowed: Storage evidence + this docs/plan.

## 18. Git/worktree summary

- Authority worktree used for docs/report only.
- Dirty main `X:\AI MARS` not mutated by this task.
- Commit/push: exact allowlisted report + OCPilot docs only.

## 19. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-STRUCTURE-NORMALIZATION-PLAN-01\`

Folders: `preflight/`, `reports-read/`, `diagnosis/`, `target-models/`, `decision-matrix/`, `seo-url-plan/`, `mapping-import-plan/`, `ui-menu-sitemap-plan/`, `zapchasti-drilldown-plan/`, `apply-phases/`, `cleanup-later-note/`, `decision/`, `regression/`, `reports/`, `manifests/`, `logs/`.

## 20. SAFE UNKNOWN / blockers

- Whether empty site-only roots were intentional future stubs vs leftover demos — **operator decision** (evidence = suspect, not origin proof).
- Whether 1C will later promote Teplovoe/Hlebo/Barnoe to roots — unknown.
- Exact product-level consolidate plan for `90`↔`369` and `186`↔`368` needs Apply-04 preflight inventory (counts known; SKU-level mapping not re-audited here).
- Stellazhi «решетчатые полки» 1C-only leaves — deferred; not blocking root plan.
- **No blocker to planning.** **Blocker to apply:** operator answers in §16 / Apply 01 freeze.

## 21. Final verdict

`SITE-002 CATALOG STRUCTURE NORMALIZATION PLAN COMPLETE — OPERATOR DECISIONS REQUIRED BEFORE APPLY`

Structure attention from comparison audit is confirmed. Three target models are ready; Hybrid C is recommended. Per-category matrix, SEO/mapping/UI implications, Zapchasti drilldown, and bounded future apply phases are documented. Production mutation in this wave: **0**.

## 22. Next recommendation

1. Operator (+ client/Web-GPT) answers §16 against the matrix.
2. Commit Apply 01 decision freeze (docs only).
3. Then sequence Apply 02–05 as approved; start Zapchasti drilldown on a parallel track.
4. Apply 07 baseline refresh only after URL set is stable and smoke-verified.
5. Keep cleanup of docs-01/docs-02/tails as a **separate** later dry-run.

---

**Changed files (this wave):** this report + minimal OCPilot state/index/knowledge touch-ups.  
**Git:** commit/push docs only after staging exact allowlisted paths.
