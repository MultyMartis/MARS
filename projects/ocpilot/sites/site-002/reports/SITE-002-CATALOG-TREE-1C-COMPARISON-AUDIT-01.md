# REPORT — SITE-002 Catalog Tree 1C Comparison Audit 01

**Operation:** `SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01`  
**OCPilot run:** **4.340**  
**Date:** 2026-08-24  
**Environment:** CATALOG_TREE_1C_COMPARISON_READONLY  
**Production URL:** https://bzpm.ru/  
**Authority worktree:** `X:\AI MARS STORAGE\git-sync-site002-offers-recovery-docs-03\repo`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01\`

**Final verdict:** `SITE-002 CATALOG TREE 1C COMPARISON AUDIT COMPLETE — STRUCTURE ATTENTION REQUIRED BEFORE APPLY`

**Classifications:**

- `SITE_002_CATALOG_TREE_1C_COMPARISON_AUDIT_COMPLETE`
- `SITE_AND_1C_TREES_READY_FOR_REVIEW`
- `SITE_ROOTS_PARTIALLY_MATCH_1C_ROOTS`
- `SITE_ONLY_CATEGORIES_FOUND`
- `ONE_C_ONLY_GROUPS_FOUND`
- `DEMO_LEGACY_SUSPECTS_FOUND`
- `UPAKOVOCHNOE_PRESENT_IN_1C_ABSENT_ON_SITE`
- `PRODUCTION_MUTATION_ZERO`

---

## 1. Scope

Fresh read-only comparison of:

1. Current Production DB catalog tree (verified against export `SITE-002-CATALOG-TREE-CURRENT-EXPORT-01`).
2. Latest natural 1C import group tree from live `import0_1.xml`.
3. Read-only `oc_mars_1c_category_map`.
4. Sitemap/public status as supporting evidence only.

No Production apply, mapping change, import run, baseline refresh, or cleanup.

## 2. Operator request

Operator asked to compare current site root sections with what 1C exports, confirm correspondence, and detect possible demo/legacy sections that may be absent or named differently in 1C. Empty/disabled site categories are acceptable if they still correspond to 1C. Trees must appear **inline in the report** for review with Web-GPT.

## 3. Read-only boundary

Forbidden and not performed: production DB writes, FTP writes, 1C import runs, cache/OCMOD, category/product/mapping/importer/monitor/baseline/runtime/scheduler changes, Client Ops/n8n/Telegram mutation, docs-01/docs-02, dirty main, deletes.

Allowed and performed: Storage evidence; docs/report.

## 4. Authority preflight

| Check | Result |
|-------|--------|
| Volume `X:` / `AI WS` | OK |
| Authority path | `git-sync-site002-offers-recovery-docs-03\repo` |
| Branch | `docs/site002-offers-recovery-healthcheck-03` → `origin/mars/canonical-post-recovery` |
| Start HEAD | `2ba66a22` (**3 behind** origin) |
| Sync | `git fetch` + `git merge --ff-only` → `a9780f58` |
| Status after FF | clean; HEAD = origin |
| Staged | empty |

## 5. Current accepted state

- Catalog export `SITE-002-CATALOG-TREE-CURRENT-EXPORT-01` (`ab4f90a5`) + artifact repair (`2ba66a22`).
- Healthcheck `SITE-002-POST-IMPORT-AND-MONITOR-HEALTHCHECK-01` (`f93eabf8`): import `2026-08-24` SUCCESS; mapping `95`/`364` persistence confirmed; baseline **1887**.
- Fresh DB verify this run: total **226** / active **225** / inactive **1** / roots **10** / max id **380** — matches export; no new category since export.

## 6. Site catalog tree source

- Primary: repo flat CSV + tree from export `4.339`.
- Fresh SSH SELECT confirmation: export totals match live DB.
- Mapping overlay added in inline tree (`map: none` or GUID).

## 7. Latest 1C import files

| File | Result |
|------|--------|
| Latest log | `mars_1c_import_2026-08-24_080010.txt` |
| Run ID | `mars-20260824-080002-509cb9e8` |
| Status | **SUCCESS** (catalog + offers PASS) |
| Fresh FTP `import0_1.xml` | **OK** — 11266103 bytes — sha256=`bf73f5b74171fa37ea6b927a61159510cfd1881fb591dafeecc69ac79ef45af9` |
| Fresh FTP `offers0_1.xml` | **OK** — sha256=`a02a1b19c25d099fcc7a6d49379982c3a229fae925a19f6acd7dbcb627842c14` |
| Import re-run | **not performed** |

Parsed from live catalog XML:

- 1C groups: **111**
- 1C roots: **5**
- Products in catalog XML: **1647**
- Max 1C depth: **4**

## 8. Current Production Site Catalog Tree

Generated: `2026-08-24T08:37:15Z`
Source: SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-FLAT.csv (+ mapping overlay)

- [79] Нейтральное оборудование — status: active — direct/enabled/subtree/enabled-subtree: 0/0/1535/1533 — map: none
  - [360] Кондитерский инвентарь — status: active — direct/enabled/subtree/enabled-subtree: 0/0/10/10 — map: none
    - [361] Формы кондитерские — status: active — direct/enabled/subtree/enabled-subtree: 10/10/10/10 — map: none
  - [322] Подтоварники и подставки — status: active — direct/enabled/subtree/enabled-subtree: 0/0/24/24 — map: none
    - [325] Подставки для печей и пароконвектоматов — status: active — direct/enabled/subtree/enabled-subtree: 8/8/8/8 — map: none
    - [324] Подтоварники ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 8/8/8/8 — map: none
    - [323] Подтоварники СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 8/8/8/8 — map: none
  - [331] Полки настенные и настольные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/160/160 — map: none
    - [343] Полки для гастоемкостей — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
    - [341] Полки для крышек и досок — status: active — direct/enabled/subtree/enabled-subtree: 2/2/2/2 — map: none
    - [340] Полки для посуды — status: active — direct/enabled/subtree/enabled-subtree: 16/16/16/16 — map: none
    - [337] Полки закрытые ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 1/1/18/18 — map: none
      - [339] Полки закрытые ПРЕМИУМ двери купе — status: active — direct/enabled/subtree/enabled-subtree: 9/9/9/9 — map: none
      - [338] Полки закрытые ПРЕМИУМ распашные двери — status: active — direct/enabled/subtree/enabled-subtree: 8/8/8/8 — map: none
    - [342] Полки консольные ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 16/16/16/16 — map: none
    - [344] Полки настольные ПРЕМИУМ 3 — status: active — direct/enabled/subtree/enabled-subtree: 0/0/44/44 — map: none
      - [345] Полки настольные ПРЕМИУМ 3 глуб.300 — status: active — direct/enabled/subtree/enabled-subtree: 22/22/22/22 — map: none
      - [346] Полки настольные ПРЕМИУМ 3 глуб.400 — status: active — direct/enabled/subtree/enabled-subtree: 22/22/22/22 — map: none
    - [332] Полки открытые ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 1/1/56/56 — map: none
      - [334] Полки открытые ПРЕМИУМ глуб.300 — status: active — direct/enabled/subtree/enabled-subtree: 22/22/22/22 — map: none
      - [333] Полки открытые ПРЕМИУМ глуб.400 — status: active — direct/enabled/subtree/enabled-subtree: 22/22/22/22 — map: none
      - [335] Полки открытые ПРЕМИУМ двухярусные — status: active — direct/enabled/subtree/enabled-subtree: 11/11/11/11 — map: none
    - [336] Полки полуоткрытые ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
  - [301] Столы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/522/520 — map: none
    - [304] Кондитерские столы — status: active — direct/enabled/subtree/enabled-subtree: 12/12/12/12 — map: none
    - [303] Столы для сбора отходов — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
    - [312] Столы серии ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 0/0/78/78 — map: none
      - [313] Столы ПРЕМИУМ-600 — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [314] Столы ПРЕМИУМ-700 — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [315] Столы ПРЕМИУМ-800 — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
    - [319] Столы серии ПРЕМИУМ-3 — status: active — direct/enabled/subtree/enabled-subtree: 0/0/78/78 — map: none
      - [320] Столы серии ПРЕМИУМ-3 - 600 — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [321] Столы серии ПРЕМИУМ-3 - 700 — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [328] Столы серии ПРЕМИУМ-3 - 800 — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
    - [305] Столы серии СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 0/0/164/163 — map: none
      - [330] Столы СТАНДАРТ угловые — status: active — direct/enabled/subtree/enabled-subtree: 7/7/7/7 — map: none
      - [306] Столы СТАНДАРТ-600 с полкой-решеткой — status: active — direct/enabled/subtree/enabled-subtree: 27/26/27/26 — map: none
      - [307] Столы СТАНДАРТ-600 со сплошной полкой — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [308] Столы СТАНДАРТ-700 с полкой-решеткой — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [310] Столы СТАНДАРТ-700 со сплошной полкой — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [309] Столы СТАНДАРТ-800 с полкой-решеткой — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
      - [311] Столы СТАНДАРТ-800 со сплошной полкой — status: active — direct/enabled/subtree/enabled-subtree: 26/26/26/26 — map: none
    - [316] Столы-тумбы серии ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 0/0/92/92 — map: none
      - [317] Столы-тумбы без ванн — status: active — direct/enabled/subtree/enabled-subtree: 52/52/52/52 — map: none
      - [327] Столы-тумбы с двумя цельнотянутыми ваннами — status: active — direct/enabled/subtree/enabled-subtree: 13/13/13/13 — map: none
      - [318] Столы-тумбы с одной цельнотянутой ванной — status: active — direct/enabled/subtree/enabled-subtree: 27/27/27/27 — map: none
    - [302] Столы-тумбы серии СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 33/32/72/71 — map: none
      - [329] Столы-тумбы СТАНДАРТ без ванн — status: active — direct/enabled/subtree/enabled-subtree: 39/39/39/39 — map: none
  - [326] Тележки сервировочные — status: active — direct/enabled/subtree/enabled-subtree: 3/3/3/3 — map: none
  - [354] Тележки-шпильки и противни — status: active — direct/enabled/subtree/enabled-subtree: 0/0/13/13 — map: none
    - [355] Противни — status: active — direct/enabled/subtree/enabled-subtree: 7/7/7/7 — map: none
    - [356] Тележки-шпильки — status: active — direct/enabled/subtree/enabled-subtree: 6/6/6/6 — map: none
  - [358] Шкафы и лари — status: active — direct/enabled/subtree/enabled-subtree: 0/0/8/8 — map: none
    - [363] Шкафы для хлеба — status: active — direct/enabled/subtree/enabled-subtree: 2/2/2/2 — map: none
    - [359] Шкафы кухонные — status: active — direct/enabled/subtree/enabled-subtree: 2/2/2/2 — map: none
    - [88] Лари — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
      - [140] Производственные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [141] Складские — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [207] Зонты вытяжные — status: active — direct/enabled/subtree/enabled-subtree: 67/67/67/67 — map: none
  - [80] Моечные ванны — status: active — direct/enabled/subtree/enabled-subtree: 0/0/128/128 — map: none
    - [261] Ванны СТАНДАРТ нестандартные — status: active — direct/enabled/subtree/enabled-subtree: 2/2/2/2 — map: none
    - [258] Ванны моечные для яиц — status: active — direct/enabled/subtree/enabled-subtree: 10/10/10/10 — map: none
      - [298] Корзины для сан.обработки яиц — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [299] Корзины для сан.обработки яиц НЕСТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [273] Ванны с рабочей поверхностью ЛЮКС — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [272] Ванны с рабочей поверхностью ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 18/18/18/18 — map: none
    - [280] Ванны с рабочей поверхностью ПРЕМИУМ нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [278] Ванны с рабочей поверхностью ПРЕМИУМ-2 — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: none
    - [283] Ванны с рабочей поверхностью ПРЕМИУМ-2 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [290] Ванны с рабочей поверхностью ПРЕМИУМ-3 — status: active — direct/enabled/subtree/enabled-subtree: 16/16/16/16 — map: none
      - [291] Ванна с рабочей поверхностью ПРЕМИУМ-3 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [293] Ванны с рабочей поверхностью ПРЕМИУМ-3 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [271] Ванны с рабочей поверхностью СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 18/18/18/18 — map: none
    - [276] Ванны с рабочей поверхностью СТАНДАРТ нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [266] Ванны сварные ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 15/15/15/15 — map: none
    - [260] Ванны сварные ПРЕМИУМ НЕСТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [264] Ванны сварные ПРЕМИУМ-2 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [294] Ванны сварные ПРЕМИУМ-3 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [259] Ванны сварные ПРЕМИУМ-В — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [265] Ванны сварные СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 15/15/15/15 — map: none
    - [270] Ванны цельнотянутые ЛЮКС — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
    - [269] Ванны цельнотянутые ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
    - [288] Ванны цельнотянутые ПРЕМИУМ нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [277] Ванны цельнотянутые ПРЕМИУМ-2 — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [281] Ванны цельнотянутые ПРЕМИУМ-2 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [295] Ванны цельнотянутые ПРЕМИУМ-3 — status: active — direct/enabled/subtree/enabled-subtree: 10/10/10/10 — map: none
    - [289] Ванны цельнотянутые Премиум-3 Нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [268] Ванны цельнотянутые СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
    - [279] Ванны цельнотянутые СТАНДАРТ нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [243] Вставка перфорированная — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [287] Комплектующие для ванн/рукомойников — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [285] Котломойки ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
    - [296] Котломойки ПРЕМИУМ нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [262] Котломойки ПРЕМИУМ-2 — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [263] Котломойки ПРЕМИУМ-2 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [300] Котломойки ПРЕМИУМ-3 — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [292] Котломойки ПРЕМИУМ-3 нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [267] Котломойки СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 4/4/4/4 — map: none
    - [275] Котломойки СТАНДАРТ нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [282] Моповые ванны — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [286] Моповые ванны нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [284] Нестандартные/специализированные ванны — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [274] Рукомойники — status: active — direct/enabled/subtree/enabled-subtree: 3/3/3/3 — map: none
    - [297] рукомойники нестандарт — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [97] Односекционные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [100] С бортом — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [101] Без борта — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [98] Двухсекционные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [102] С бортом — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [103] С полкой — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [99] Трёхсекционные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [104] Для производств — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [105] Для столовых — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [87] Столы производственные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [106] С бортом — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [109] С полкой — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [110] Усиленные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [107] Без борта — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [111] Стандартные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [112] С нижней полкой — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [108] Специальные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [113] Разделочные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [114] Для оборудования — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [86] Стеллажи — status: active — direct/enabled/subtree/enabled-subtree: 0/0/600/600 — map: none
    - [347] Специализированные стеллажи — status: active — direct/enabled/subtree/enabled-subtree: 3/3/3/3 — map: none
    - [350] Стеллажи ПРЕМИУМ — status: active — direct/enabled/subtree/enabled-subtree: 0/0/207/207 — map: none
      - [366] Стеллажи ПРЕМИУМ высота 1600 — status: active — direct/enabled/subtree/enabled-subtree: 104/104/104/104 — map: none
      - [351] Стеллажи ПРЕМИУМ высота 1800 — status: active — direct/enabled/subtree/enabled-subtree: 103/103/103/103 — map: none
    - [352] Стеллажи ПРЕМИУМ-3 — status: active — direct/enabled/subtree/enabled-subtree: 0/0/156/156 — map: none
      - [367] Стеллажи ПРЕМИУМ-3 высота 1600 — status: active — direct/enabled/subtree/enabled-subtree: 78/78/78/78 — map: none
      - [353] Стеллажи ПРЕМИУМ-3 высота 1800 — status: active — direct/enabled/subtree/enabled-subtree: 78/78/78/78 — map: none
    - [348] Стеллажи СТАНДАРТ — status: active — direct/enabled/subtree/enabled-subtree: 0/0/222/222 — map: none
      - [365] Стеллажи СТАНДАРТ высота 1600 — status: active — direct/enabled/subtree/enabled-subtree: 104/104/104/104 — map: none
      - [377] Стеллажи СТАНДАРТ высота 1600 (решетчатые полки) — status: active — direct/enabled/subtree/enabled-subtree: 15/15/15/15 — map: none
      - [349] Стеллажи СТАНДАРТ высота 1800 — status: active — direct/enabled/subtree/enabled-subtree: 103/103/103/103 — map: none
    - [357] Стеллажи для посуды — status: active — direct/enabled/subtree/enabled-subtree: 12/12/12/12 — map: none
    - [115] Разборные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [117] Лёгкие — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [118] Усиленные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [116] Стационарные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [119] Для складов — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [120] Для кухни — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [83] Полки — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [121] Настенные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [123] Открытые — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [124] Закрытые — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [122] Угловые — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [125] Для кухни — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [126] Для моечных зон — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [82] Подтоварники — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [127] Стандартные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [128] Усиленные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [129] Под оборудование — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [89] Шкафы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [130] Производственные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [132] Закрытые — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [133] С полками — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [131] Для хранения — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [134] Инвентарь — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
      - [135] Посуда — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [85] Тележки — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [136] Платформенные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [137] Сервировочные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [138] Для гастроёмкостей — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
    - [139] Для подносов — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
- [362] Технологическое оборудование — status: active — direct/enabled/subtree/enabled-subtree: 0/0/21/21 — map: active GUID=e0fd5c42-a3b8-11ea-8152-a85e4515c4f4
  - [373] Мясоперерабатывающее — status: active — direct/enabled/subtree/enabled-subtree: 0/0/4/4 — map: active GUID=2adc2489-7c1a-11f1-aecc-581122cf362c
    - [376] Слайсеры для мяса — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: active GUID=e0b6bb6d-7c1a-11f1-aecc-581122cf362c
    - [378] Мясорубки — status: active — direct/enabled/subtree/enabled-subtree: 2/2/2/2 — map: active GUID=7e43262d-7c1a-11f1-aecc-581122cf362c
    - [379] Пилы для мяса — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: active GUID=95003163-7c1a-11f1-aecc-581122cf362c
  - [364] Посуда и инвентарь — status: active — direct/enabled/subtree/enabled-subtree: 6/6/6/6 — map: active GUID=9b37b1f1-7c19-11f1-aecc-581122cf362c
  - [369] Тепловое — status: active — direct/enabled/subtree/enabled-subtree: 0/0/9/9 — map: none
    - [370] Водонагреватели — status: active — direct/enabled/subtree/enabled-subtree: 5/5/5/5 — map: none
    - [371] Грили контактные — status: active — direct/enabled/subtree/enabled-subtree: 3/3/3/3 — map: none
    - [372] Рисоварки — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: none
  - [368] Хлебопекарное — status: active — direct/enabled/subtree/enabled-subtree: 0/0/1/1 — map: none
    - [374] Тестораскатки — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: none
  - [375] Электромеханическое — status: active — direct/enabled/subtree/enabled-subtree: 0/0/1/1 — map: active GUID=bac3dc26-7c19-11f1-aecc-581122cf362c
    - [380] Хлеборезки — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: active GUID=41a86281-7c1b-11f1-aecc-581122cf362c
- [90] Тепловое оборудование — status: active — direct/enabled/subtree/enabled-subtree: 0/0/4/4 — map: none
  - [144] Плиты — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: none
  - [145] Жарочные шкафы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [146] Пароконвектоматы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [147] Фритюрницы — status: active — direct/enabled/subtree/enabled-subtree: 3/3/3/3 — map: none
- [95] Холодильное оборудование — status: active — direct/enabled/subtree/enabled-subtree: 1/1/1/1 — map: active GUID=95bfa611-898d-11f1-aece-581122cf362c
  - [148] Холодильные шкафы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [149] Морозильные шкафы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [150] Камеры — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
- [93] Инвентарь — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [151] Гастроёмкости — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [152] Кухонный инвентарь — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
- [96] Запчасти — status: inactive — direct/enabled/subtree/enabled-subtree: 76/76/76/76 — map: none
- [171] Барное оборудование — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [172] Льдогенераторы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [173] Блендеры — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [174] Мороженое и коктейли — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [175] Миксеры для молочных коктейлей — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [176] Сокоохладители — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [177] Барные комбайны — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [178] Измельчители льда — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [179] Барные станции — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [180] Граниторы - Слаш — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [181] Аппараты для горячего шоколада — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [182] Кегераторы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [183] Аппараты для охлаждения бокалов — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [184] Системы питьевого водоснабжения — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [185] Аппараты для взбитых сливок — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
- [186] Хлебопекарное оборудование — status: active — direct/enabled/subtree/enabled-subtree: 0/0/12/12 — map: none
  - [187] Подовые печи — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [188] Миксеры планетарные — status: active — direct/enabled/subtree/enabled-subtree: 5/5/5/5 — map: none
  - [189] Тестомесы — status: active — direct/enabled/subtree/enabled-subtree: 7/7/7/7 — map: none
  - [190] Шкафы и столы расстоечные — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [191] Ротационные печи — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [192] Прессы для приготовления пасты — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [193] Тестораскатки, тестозакатки — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [194] Тестоделители и тестоокруглители — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [195] Прессы для пиццы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [196] Мукопросеиватели — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [197] Ферментаторы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [198] Оборудование для декорирования — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [199] Бисквиторезки — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [200] Центрифуги для яиц — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [201] Дозаторы — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
  - [202] Измельчители — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
- [205] Посудомоечные машины — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none
- [206] Вентиляционное оборудование — status: active — direct/enabled/subtree/enabled-subtree: 0/0/0/0 — map: none

## 9. Latest 1C Import Group Tree

Generated: `2026-08-24T08:37:15Z`
Source: live FTP `public_html/1c_incoming/webdata/import0_1.xml`

- [НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ] GUID=`25a2ee03-cec7-11e9-95c9-60a44cac3e7c` — depth:1 — direct_products:0 — subtree_products:1608 — site_cat: none
  - [Ванны моечные] GUID=`b8a919ed-ceff-11e9-95c9-60a44cac3e7c` — depth:2 — direct_products:0 — subtree_products:128 — site_cat: none
    - [Ванны моечные для яиц] GUID=`4afc83a3-f0f1-11f0-aebe-581122cf362c` — depth:3 — direct_products:10 — subtree_products:10 — site_cat: none
    - [Ванны с рабочей поверхностью ПРЕМИУМ] GUID=`74355991-3b8e-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:18 — subtree_products:18 — site_cat: none
    - [Ванны с рабочей поверхностью ПРЕМИУМ-2] GUID=`4f1a9de4-5de6-11ea-a867-60a44cac3e7c` — depth:3 — direct_products:1 — subtree_products:1 — site_cat: none
    - [Ванны с рабочей поверхностью ПРЕМИУМ-3] GUID=`aa652ed8-24d5-11f0-aea9-581122cf362c` — depth:3 — direct_products:16 — subtree_products:16 — site_cat: none
    - [Ванны с рабочей поверхностью СТАНДАРТ] GUID=`695627dd-3b8e-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:18 — subtree_products:18 — site_cat: none
    - [Ванны сварные ПРЕМИУМ] GUID=`172927d4-3b60-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:15 — subtree_products:15 — site_cat: none
    - [Ванны сварные СТАНДАРТ] GUID=`6fac5c74-3b50-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:15 — subtree_products:15 — site_cat: none
    - [Ванны СТАНДАРТ нестандартные] GUID=`b9cf3747-95ca-11ea-8f48-60a44cac3e7c` — depth:3 — direct_products:2 — subtree_products:2 — site_cat: none
    - [Ванны цельнотянутые ЛЮКС] GUID=`8e4d4109-3b88-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
    - [Ванны цельнотянутые ПРЕМИУМ] GUID=`84f71764-3b88-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
    - [Ванны цельнотянутые ПРЕМИУМ-3] GUID=`5c4d42a5-27bb-11ef-b00f-a85e4515c4f4` — depth:3 — direct_products:10 — subtree_products:10 — site_cat: none
    - [Ванны цельнотянутые СТАНДАРТ] GUID=`7ae5f1fb-3b88-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
    - [Котломойки ПРЕМИУМ] GUID=`5b0208eb-fe50-11ea-a988-a85e4515c4f4` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
    - [Котломойки СТАНДАРТ] GUID=`cce5cfd2-3b86-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
    - [Рукомойники] GUID=`0c44c21a-3b9c-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:3 — subtree_products:3 — site_cat: none
  - [Зонты вытяжные] GUID=`1e79028a-4182-11ea-aaed-60a44cac3e7c` — depth:2 — direct_products:67 — subtree_products:67 — site_cat: none
  - [Кондитерский инвентарь] GUID=`5f6302bc-1274-11eb-a988-a85e4515c4f4` — depth:2 — direct_products:0 — subtree_products:10 — site_cat: none
    - [Формы кондитерские] GUID=`60f583cc-852d-11ea-8f48-60a44cac3e7c` — depth:3 — direct_products:10 — subtree_products:10 — site_cat: none
  - [Подтоварники и подставки] GUID=`0d37c252-3ba0-11ea-95c9-60a44cac3e7c` — depth:2 — direct_products:0 — subtree_products:24 — site_cat: none
    - [Подставки для печей и пароконвектоматов] GUID=`dac04194-3ba2-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:8 — subtree_products:8 — site_cat: none
    - [Подтоварники ПРЕМИУМ] GUID=`27cf1aa5-3ba0-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:8 — subtree_products:8 — site_cat: none
    - [Подтоварники СТАНДАРТ] GUID=`1c3c68d2-3ba0-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:8 — subtree_products:8 — site_cat: none
  - [Полки настенные и настольные] GUID=`c155fdcd-ceff-11e9-95c9-60a44cac3e7c` — depth:2 — direct_products:0 — subtree_products:160 — site_cat: none
    - [Полки для гастроемкостей] GUID=`d6757ea0-f600-11ec-b988-a85e4515c4f4` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
    - [Полки для крышек и досок] GUID=`28c2de08-e5bb-11ea-a988-a85e4515c4f4` — depth:3 — direct_products:2 — subtree_products:2 — site_cat: none
    - [Полки для посуды] GUID=`2053dee7-e5bb-11ea-a988-a85e4515c4f4` — depth:3 — direct_products:16 — subtree_products:16 — site_cat: none
    - [Полки закрытые ПРЕМИУМ] GUID=`af72998d-3bf1-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:1 — subtree_products:18 — site_cat: none
      - [Полки закрытые ПРЕМИУМ двери купе] GUID=`321d5886-eb50-11ea-a988-a85e4515c4f4` — depth:4 — direct_products:9 — subtree_products:9 — site_cat: none
      - [Полки закрытые ПРЕМИУМ распашные двери] GUID=`942e935f-98c7-11ea-8f48-60a44cac3e7c` — depth:4 — direct_products:8 — subtree_products:8 — site_cat: none
    - [Полки консольные ПРЕМИУМ] GUID=`c218f342-f066-11f0-aebe-581122cf362c` — depth:3 — direct_products:16 — subtree_products:16 — site_cat: none
    - [Полки настольные ПРЕМИУМ 3] GUID=`3918015d-e486-11f0-aebe-581122cf362c` — depth:3 — direct_products:0 — subtree_products:44 — site_cat: none
      - [Полки настольные ПРЕМИУМ 3 глуб.300] GUID=`9c41e283-e486-11f0-aebe-581122cf362c` — depth:4 — direct_products:22 — subtree_products:22 — site_cat: none
      - [Полки настольные ПРЕМИУМ 3 глуб.400] GUID=`cd1508d2-e48c-11f0-aebe-581122cf362c` — depth:4 — direct_products:22 — subtree_products:22 — site_cat: none
    - [Полки открытые ПРЕМИУМ] GUID=`80ce809e-3bf1-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:1 — subtree_products:56 — site_cat: none
      - [Полки открытые ПРЕМИУМ глуб.300] GUID=`65645454-eb50-11ea-a988-a85e4515c4f4` — depth:4 — direct_products:22 — subtree_products:22 — site_cat: none
      - [Полки открытые ПРЕМИУМ глуб.400] GUID=`e49c09b7-e35d-11ea-a988-a85e4515c4f4` — depth:4 — direct_products:22 — subtree_products:22 — site_cat: none
      - [Полки открытые ПРЕМИУМ двухярусные] GUID=`694f56a2-9c10-11ea-b308-a85e4515c4f4` — depth:4 — direct_products:11 — subtree_products:11 — site_cat: none
    - [Полки полуоткрытые ПРЕМИУМ] GUID=`9f4d6146-3bf1-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
  - [Стеллажи] GUID=`50fa44b9-3c05-11ea-95c9-60a44cac3e7c` — depth:2 — direct_products:0 — subtree_products:675 — site_cat: none
    - [Специализированные стеллажи] GUID=`2968ebb5-9542-11f1-aed0-581122cf362c` — depth:3 — direct_products:3 — subtree_products:3 — site_cat: none
    - [Стеллажи для посуды] GUID=`5a1a6c66-e5c0-11ea-a988-a85e4515c4f4` — depth:3 — direct_products:12 — subtree_products:12 — site_cat: none
    - [Стеллажи ПРЕМИУМ] GUID=`66e1310a-3c05-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:0 — subtree_products:237 — site_cat: none
      - [Стеллажи ПРЕМИУМ высота 1600] GUID=`1f41d72e-e367-11ea-a988-a85e4515c4f4` — depth:4 — direct_products:104 — subtree_products:104 — site_cat: none
      - [Стеллажи ПРЕМИУМ высота 1600 (решетчатые полки)] GUID=`19ef9190-4473-11f1-aec7-581122cf362c` — depth:4 — direct_products:15 — subtree_products:15 — site_cat: none
      - [Стеллажи ПРЕМИУМ высота 1800] GUID=`1f41d72f-e367-11ea-a988-a85e4515c4f4` — depth:4 — direct_products:103 — subtree_products:103 — site_cat: none
      - [Стеллажи ПРЕМИУМ высота 1800 (решетчатые полки)] GUID=`fdd8ec00-4764-11f1-aec7-581122cf362c` — depth:4 — direct_products:15 — subtree_products:15 — site_cat: none
    - [Стеллажи ПРЕМИУМ-3] GUID=`c4211260-27bb-11ef-b00f-a85e4515c4f4` — depth:3 — direct_products:0 — subtree_products:186 — site_cat: none
      - [Стеллажи ПРЕМИУМ-3 высота 1600] GUID=`0ebc3df6-3aa9-11ef-b00f-a85e4515c4f4` — depth:4 — direct_products:78 — subtree_products:78 — site_cat: none
      - [Стеллажи ПРЕМИУМ-3 высота 1600 (решетчатые полки)] GUID=`3e04e665-4785-11f1-aec7-581122cf362c` — depth:4 — direct_products:15 — subtree_products:15 — site_cat: none
      - [Стеллажи ПРЕМИУМ-3 высота 1800] GUID=`e97d21d8-3aa8-11ef-b00f-a85e4515c4f4` — depth:4 — direct_products:78 — subtree_products:78 — site_cat: none
      - [Стеллажи ПРЕМИУМ-3 высота 1800 (решетчатые полки)] GUID=`7114272f-478e-11f1-aec7-581122cf362c` — depth:4 — direct_products:15 — subtree_products:15 — site_cat: none
    - [Стеллажи СТАНДАРТ] GUID=`5f7f2c71-3c05-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:0 — subtree_products:237 — site_cat: none
      - [Стеллажи СТАНДАРТ высота 1600] GUID=`9d423fdd-e367-11ea-a988-a85e4515c4f4` — depth:4 — direct_products:104 — subtree_products:104 — site_cat: none
      - [Стеллажи СТАНДАРТ высота 1600 (решетчатые полки)] GUID=`abe516a5-445e-11f1-aec7-581122cf362c` — depth:4 — direct_products:15 — subtree_products:15 — site_cat: none
      - [Стеллажи СТАНДАРТ высота 1800] GUID=`9d423fdc-e367-11ea-a988-a85e4515c4f4` — depth:4 — direct_products:103 — subtree_products:103 — site_cat: none
      - [Стеллажи СТАНДАРТ высота 1800 (решетчатые полки)] GUID=`50a5dc8a-4466-11f1-aec7-581122cf362c` — depth:4 — direct_products:15 — subtree_products:15 — site_cat: none
  - [Столы] GUID=`abfa44f8-ceff-11e9-95c9-60a44cac3e7c` — depth:2 — direct_products:0 — subtree_products:520 — site_cat: none
    - [Кондитерские столы] GUID=`798fce9c-4174-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:12 — subtree_products:12 — site_cat: none
    - [Столы для сбора отходов] GUID=`6d8ebe1c-4174-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:26 — subtree_products:26 — site_cat: none
    - [Столы серии ПРЕМИУМ] GUID=`4c60245a-3de1-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:0 — subtree_products:78 — site_cat: none
      - [Столы ПРЕМИУМ-600] GUID=`7267c45e-3de1-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы ПРЕМИУМ-700] GUID=`82747af3-3de1-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы ПРЕМИУМ-800] GUID=`8ce09bd1-3de1-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
    - [Столы серии ПРЕМИУМ-3] GUID=`e13a5c55-27ba-11ef-b00f-a85e4515c4f4` — depth:3 — direct_products:0 — subtree_products:78 — site_cat: none
      - [Столы серии ПРЕМИУМ-3 - 600] GUID=`cdc59f2b-39e2-11ef-b00f-a85e4515c4f4` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы серии ПРЕМИУМ-3 - 700] GUID=`d847cc03-39e2-11ef-b00f-a85e4515c4f4` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы серии ПРЕМИУМ-3 - 800] GUID=`2bd67bd8-296b-11f0-aea9-581122cf362c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
    - [Столы серии СТАНДАРТ] GUID=`56c7a695-3cc8-11ea-95c9-60a44cac3e7c` — depth:3 — direct_products:0 — subtree_products:163 — site_cat: none
      - [Столы СТАНДАРТ угловые] GUID=`9eed6320-3cc8-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:7 — subtree_products:7 — site_cat: none
      - [Столы СТАНДАРТ-600 с полкой-решеткой] GUID=`6aa97148-3cc8-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы СТАНДАРТ-600 со сплошной полкой] GUID=`82616d60-3cc8-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы СТАНДАРТ-700 с полкой-решеткой] GUID=`82616d61-3cc8-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы СТАНДАРТ-700 со сплошной полкой] GUID=`8b3f8eca-3cc8-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы СТАНДАРТ-800 с полкой-решеткой] GUID=`8b3f8ec9-3cc8-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
      - [Столы СТАНДАРТ-800 со сплошной полкой] GUID=`94023a35-3cc8-11ea-95c9-60a44cac3e7c` — depth:4 — direct_products:26 — subtree_products:26 — site_cat: none
    - [Столы-тумбы серии ПРЕМИУМ] GUID=`68705cc8-40c8-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:0 — subtree_products:92 — site_cat: none
      - [Столы-тумбы без ванн] GUID=`7555f164-40c8-11ea-aaed-60a44cac3e7c` — depth:4 — direct_products:52 — subtree_products:52 — site_cat: none
      - [Столы-тумбы с двумя цельнотянутыми ваннами] GUID=`8d1ef161-40c8-11ea-aaed-60a44cac3e7c` — depth:4 — direct_products:13 — subtree_products:13 — site_cat: none
      - [Столы-тумбы с одной цельнотянутой ванной] GUID=`7fc71ab8-40c8-11ea-aaed-60a44cac3e7c` — depth:4 — direct_products:27 — subtree_products:27 — site_cat: none
    - [Столы-тумбы серии СТАНДАРТ] GUID=`869a32ef-2a1a-11eb-a988-a85e4515c4f4` — depth:3 — direct_products:32 — subtree_products:71 — site_cat: none
      - [Столы-тумбы СТАНДАРТ без ванн] GUID=`a84ba1d5-2a20-11eb-a988-a85e4515c4f4` — depth:4 — direct_products:39 — subtree_products:39 — site_cat: none
  - [Тележки сервировочные] GUID=`2534432c-4182-11ea-aaed-60a44cac3e7c` — depth:2 — direct_products:3 — subtree_products:3 — site_cat: none
  - [Тележки-шпильки и противни] GUID=`5217152a-417a-11ea-aaed-60a44cac3e7c` — depth:2 — direct_products:0 — subtree_products:13 — site_cat: none
    - [Противни] GUID=`724c9da6-417a-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:7 — subtree_products:7 — site_cat: none
    - [Тележки-шпильки] GUID=`79697bb4-417a-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:6 — subtree_products:6 — site_cat: none
  - [Шкафы и лари] GUID=`073be2e6-417f-11ea-aaed-60a44cac3e7c` — depth:2 — direct_products:0 — subtree_products:8 — site_cat: none
    - [Лари] GUID=`313e5e2f-417f-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:4 — subtree_products:4 — site_cat: none
    - [Шкафы для хлеба] GUID=`2472f8b6-417f-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:2 — subtree_products:2 — site_cat: none
    - [Шкафы кухонные] GUID=`2b1b51fa-417f-11ea-aaed-60a44cac3e7c` — depth:3 — direct_products:2 — subtree_products:2 — site_cat: none
- [ПОСУДА И ИНВЕНТАРЬ] GUID=`9b37b1f1-7c19-11f1-aecc-581122cf362c` — depth:1 — direct_products:6 — subtree_products:6 — site_cat=364 (Посуда и инвентарь)
- [ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ] GUID=`e0fd5c42-a3b8-11ea-8152-a85e4515c4f4` — depth:1 — direct_products:0 — subtree_products:31 — site_cat=362 (Технологическое оборудование)
  - [Мясоперерабатывающее] GUID=`2adc2489-7c1a-11f1-aecc-581122cf362c` — depth:2 — direct_products:0 — subtree_products:4 — site_cat=373 (Мясоперерабатывающее)
    - [Мясорубки] GUID=`7e43262d-7c1a-11f1-aecc-581122cf362c` — depth:3 — direct_products:2 — subtree_products:2 — site_cat=378 (Мясорубки)
    - [Пилы для мяса] GUID=`95003163-7c1a-11f1-aecc-581122cf362c` — depth:3 — direct_products:1 — subtree_products:1 — site_cat=379 (Пилы для мяса)
    - [Слайсеры для мяса] GUID=`e0b6bb6d-7c1a-11f1-aecc-581122cf362c` — depth:3 — direct_products:1 — subtree_products:1 — site_cat=376 (Слайсеры для мяса)
  - [Тепловое] GUID=`65f72e7d-7c19-11f1-aecc-581122cf362c` — depth:2 — direct_products:0 — subtree_products:13 — site_cat: none
    - [Водонагреватели] GUID=`ea4e83f6-7c19-11f1-aecc-581122cf362c` — depth:3 — direct_products:5 — subtree_products:5 — site_cat: none
    - [Грили контактные] GUID=`0381869b-7c1a-11f1-aecc-581122cf362c` — depth:3 — direct_products:3 — subtree_products:3 — site_cat: none
    - [Плиты] GUID=`b2e666b2-7c1a-11f1-aecc-581122cf362c` — depth:3 — direct_products:1 — subtree_products:1 — site_cat: none
    - [Рисоварки] GUID=`ca343957-7c1a-11f1-aecc-581122cf362c` — depth:3 — direct_products:1 — subtree_products:1 — site_cat: none
    - [Фритюрницы] GUID=`34e45023-7c1b-11f1-aecc-581122cf362c` — depth:3 — direct_products:3 — subtree_products:3 — site_cat: none
  - [Хлебопекарное] GUID=`5430c2fe-7c19-11f1-aecc-581122cf362c` — depth:2 — direct_products:0 — subtree_products:13 — site_cat: none
    - [Миксеры планетарные] GUID=`4ebf35ee-7c1a-11f1-aecc-581122cf362c` — depth:3 — direct_products:5 — subtree_products:5 — site_cat: none
    - [Тестомесы] GUID=`0d63ee1a-7c1b-11f1-aecc-581122cf362c` — depth:3 — direct_products:7 — subtree_products:7 — site_cat: none
    - [Тестораскатки] GUID=`210b8785-7c1b-11f1-aecc-581122cf362c` — depth:3 — direct_products:1 — subtree_products:1 — site_cat: none
  - [Электромеханическое] GUID=`bac3dc26-7c19-11f1-aecc-581122cf362c` — depth:2 — direct_products:0 — subtree_products:1 — site_cat=375 (Электромеханическое)
    - [Хлеборезки] GUID=`41a86281-7c1b-11f1-aecc-581122cf362c` — depth:3 — direct_products:1 — subtree_products:1 — site_cat=380 (Хлеборезки)
- [УПАКОВОЧНОЕ ОБОРУДОВАНИЕ] GUID=`5bc6a012-7c19-11f1-aecc-581122cf362c` — depth:1 — direct_products:1 — subtree_products:1 — site_cat: none
- [ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ] GUID=`95bfa611-898d-11f1-aece-581122cf362c` — depth:1 — direct_products:1 — subtree_products:1 — site_cat=95 (Холодильное оборудование)

### 9.1 Tech subtree (expanded for operator)

# 1C Технологическое subtree

- ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ | sub=31 | map=362 | GUID=`e0fd5c42-a3b8-11ea-8152-a85e4515c4f4`
  - Хлебопекарное | sub=13 | map=none | GUID=`5430c2fe-7c19-11f1-aecc-581122cf362c`
    - Миксеры планетарные | sub=5 | map=none | GUID=`4ebf35ee-7c1a-11f1-aecc-581122cf362c`
    - Тестомесы | sub=7 | map=none | GUID=`0d63ee1a-7c1b-11f1-aecc-581122cf362c`
    - Тестораскатки | sub=1 | map=none | GUID=`210b8785-7c1b-11f1-aecc-581122cf362c`
  - Тепловое | sub=13 | map=none | GUID=`65f72e7d-7c19-11f1-aecc-581122cf362c`
    - Водонагреватели | sub=5 | map=none | GUID=`ea4e83f6-7c19-11f1-aecc-581122cf362c`
    - Грили контактные | sub=3 | map=none | GUID=`0381869b-7c1a-11f1-aecc-581122cf362c`
    - Плиты | sub=1 | map=none | GUID=`b2e666b2-7c1a-11f1-aecc-581122cf362c`
    - Рисоварки | sub=1 | map=none | GUID=`ca343957-7c1a-11f1-aecc-581122cf362c`
    - Фритюрницы | sub=3 | map=none | GUID=`34e45023-7c1b-11f1-aecc-581122cf362c`
  - Электромеханическое | sub=1 | map=375 | GUID=`bac3dc26-7c19-11f1-aecc-581122cf362c`
    - Хлеборезки | sub=1 | map=380 | GUID=`41a86281-7c1b-11f1-aecc-581122cf362c`
  - Мясоперерабатывающее | sub=4 | map=373 | GUID=`2adc2489-7c1a-11f1-aecc-581122cf362c`
    - Мясорубки | sub=2 | map=378 | GUID=`7e43262d-7c1a-11f1-aecc-581122cf362c`
    - Пилы для мяса | sub=1 | map=379 | GUID=`95003163-7c1a-11f1-aecc-581122cf362c`
    - Слайсеры для мяса | sub=1 | map=376 | GUID=`e0b6bb6d-7c1a-11f1-aecc-581122cf362c`


## 10. Mapping table summary

Rows in `oc_mars_1c_category_map`: **9** (all `active`).

| map_id | category_id | name | GUID | path | confidence | status |
|---:|---:|---|---|---|---|---|
| 1 | 362 | Технологическое оборудование | `e0fd5c42-a3b8-11ea-8152-a85e4515c4f4` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ | HIGH_GUID_AND_PATH | active |
| 2 | 373 | Мясоперерабатывающее | `2adc2489-7c1a-11f1-aecc-581122cf362c` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Мясоперерабатывающее | HIGH_GUID_AND_PATH | active |
| 3 | 375 | Электромеханическое | `bac3dc26-7c19-11f1-aecc-581122cf362c` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Электромеханическое | HIGH_GUID_AND_PATH | active |
| 4 | 376 | Слайсеры для мяса | `e0b6bb6d-7c1a-11f1-aecc-581122cf362c` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Мясоперерабатывающее > Слайсеры для мяса | HIGH_GUID_AND_PATH | active |
| 5 | 378 | Мясорубки | `7e43262d-7c1a-11f1-aecc-581122cf362c` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Мясоперерабатывающее > Мясорубки | HIGH_GUID_AND_PATH | active |
| 6 | 379 | Пилы для мяса | `95003163-7c1a-11f1-aecc-581122cf362c` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Мясоперерабатывающее > Пилы для мяса | HIGH_GUID_AND_PATH | active |
| 7 | 380 | Хлеборезки | `41a86281-7c1b-11f1-aecc-581122cf362c` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ > Электромеханическое > Хлеборезки | HIGH_GUID_AND_PATH | active |
| 8 | 95 | Холодильное оборудование | `95bfa611-898d-11f1-aece-581122cf362c` | ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ | HIGH_GUID_AND_PATH | active |
| 9 | 364 | Посуда и инвентарь | `9b37b1f1-7c19-11f1-aecc-581122cf362c` | ПОСУДА И ИНВЕНТАРЬ | HIGH_GUID_AND_PATH | active |

Focus:

- Roots with GUID map: `95`, `362` (+ tech leaves `373/375/376/378/379/380`).
- `364` Посуда и инвентарь mapped to 1C **root** GUID, but site places it under Tech `362`.
- Roots **without** map rows: `79` (path-matched), `90`, `93`, `96`, `171`, `186`, `205`, `206`.

## 11. Site roots vs 1C roots comparison

### 1C roots (authoritative export)

1. `НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ`
2. `ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ`
3. `ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ`
4. `ПОСУДА И ИНВЕНТАРЬ`
5. `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`

### Site roots (Production DB)

10 roots: `79`, `90`, `93`, `95`, `96`, `171`, `186`, `205`, `206`, `362`.

### Roots matrix

| Site ID | Site root / note | Status | Enabled subtree | Class | 1C name | 1C GUID | Notes |
|---:|---|---:|---:|---|---|---|---|
| 79 | Нейтральное оборудование | 1 | 1533 | `MATCH_PATH` | НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ | `25a2ee03-cec7-11e9-95c9-60a44cac3e7c` |  |
| 90 | Тепловое оборудование | 1 | 4 | `SITE_ROOT_VS_1C_NESTED_CANDIDATE` | — | `—` | No 1C root; 1C has nested ТЕХНОЛОГИЧЕСКОЕ > Тепловое |
| 93 | Инвентарь | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` | — | `—` |  |
| 95 | Холодильное оборудование | 1 | 1 | `MATCH_GUID` | ХОЛОДИЛЬНОЕ ОБОРУДОВАНИЕ | `95bfa611-898d-11f1-aece-581122cf362c` | map_id=8 |
| 96 | Запчасти | 0 | 76 | `SITE_ONLY_NO_1C_MATCH` | — | `—` |  |
| 171 | Барное оборудование | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` | — | `—` |  |
| 186 | Хлебопекарное оборудование | 1 | 12 | `SITE_ROOT_VS_1C_NESTED_CANDIDATE` | — | `—` | No 1C root; 1C has nested ТЕХНОЛОГИЧЕСКОЕ > Хлебопекарное; overlaps site 368; Wave B deferred |
| 205 | Посудомоечные машины | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` | — | `—` |  |
| 206 | Вентиляционное оборудование | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` | — | `—` |  |
| 362 | Технологическое оборудование | 1 | 21 | `MATCH_GUID` | ТЕХНОЛОГИЧЕСКОЕ ОБОРУДОВАНИЕ | `e0fd5c42-a3b8-11ea-8152-a85e4515c4f4` | map_id=1 |
| — | *(1C-only / nested)* | — | — | `ONE_C_ONLY_NO_SITE_MATCH` | УПАКОВОЧНОЕ ОБОРУДОВАНИЕ | `5bc6a012-7c19-11f1-aecc-581122cf362c` | 1C root present; no site category; known open item upakovochnoe |
| 364 | Посуда и инвентарь | 1 | 6 | `MATCH_GUID_BUT_SITE_NESTED_NOT_ROOT` | ПОСУДА И ИНВЕНТАРЬ | `9b37b1f1-7c19-11f1-aecc-581122cf362c` | 1C root mapped to site category 364 under Tech 362 (hierarchy differs) |

**Root verdict:** site roots only **partially** match 1C roots. Exact root correspondence exists for Neutral / Holodilnoe / Tech. Posuda is mapped but **not** a site root. Upakovochnoe is 1C-only. Several site roots have no 1C root counterpart.

## 12. Full mismatch summary

### Match class counts (all 226 site categories)

| Class | Count |
|---|---:|
| `MATCH_GUID` | 9 |
| `MATCH_PATH` | 75 |
| `MATCH_NAME` | 19 |
| `LIKELY_RENAMED_MATCH` | 32 |
| `SITE_ONLY_NO_1C_MATCH` | 91 |

### Site-only roots (no 1C root / no direct GUID)

| ID | Name | Status | Enabled subtree | Class |
|---:|---|---:|---:|---|
| 90 | Тепловое оборудование | 1 | 4 | `SITE_ONLY_NO_1C_MATCH` |
| 93 | Инвентарь | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` |
| 96 | Запчасти | 0 | 76 | `SITE_ONLY_NO_1C_MATCH` |
| 171 | Барное оборудование | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` |
| 186 | Хлебопекарное оборудование | 1 | 12 | `SITE_ONLY_NO_1C_MATCH` |
| 205 | Посудомоечные машины | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` |
| 206 | Вентиляционное оборудование | 1 | 0 | `SITE_ONLY_NO_1C_MATCH` |

Non-empty site-only roots requiring attention:

- `[96] Запчасти` inactive, **76** products — **no 1C group** named Запчасти.
- `[186] Хлебопекарное оборудование` **12** products — 1C has nested `ТЕХНОЛОГИЧЕСКОЕ > Хлебопекарное` (also overlaps site `368`).
- `[90] Тепловое оборудование` **4** products — 1C has nested `ТЕХНОЛОГИЧЕСКОЕ > Тепловое`.

Empty active site-only roots (possible placeholders / demo leftovers / intentional stubs):

- `[93] Инвентарь` (0)
- `[171] Барное оборудование` (0)
- `[205] Посудомоечные машины` (0)
- `[206] Вентиляционное оборудование` (0)

### 1C-only groups (no site counterpart by GUID/path/name)

| GUID | Name | Path | Depth | Direct / subtree products |
|---|---|---|---:|---:|
| `5bc6a012-7c19-11f1-aecc-581122cf362c` | УПАКОВОЧНОЕ ОБОРУДОВАНИЕ | УПАКОВОЧНОЕ ОБОРУДОВАНИЕ | 1 | 1 / 1 |
| `50a5dc8a-4466-11f1-aec7-581122cf362c` | Стеллажи СТАНДАРТ высота 1800 (решетчатые полки) | НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ > Стеллажи > Стеллажи СТАНДАРТ > Стеллажи СТАНДАРТ высота 1800 (решетчатые полки) | 4 | 15 / 15 |
| `19ef9190-4473-11f1-aec7-581122cf362c` | Стеллажи ПРЕМИУМ высота 1600 (решетчатые полки) | НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ > Стеллажи > Стеллажи ПРЕМИУМ > Стеллажи ПРЕМИУМ высота 1600 (решетчатые полки) | 4 | 15 / 15 |
| `fdd8ec00-4764-11f1-aec7-581122cf362c` | Стеллажи ПРЕМИУМ высота 1800 (решетчатые полки) | НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ > Стеллажи > Стеллажи ПРЕМИУМ > Стеллажи ПРЕМИУМ высота 1800 (решетчатые полки) | 4 | 15 / 15 |
| `3e04e665-4785-11f1-aec7-581122cf362c` | Стеллажи ПРЕМИУМ-3 высота 1600 (решетчатые полки) | НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ > Стеллажи > Стеллажи ПРЕМИУМ-3 > Стеллажи ПРЕМИУМ-3 высота 1600 (решетчатые полки) | 4 | 15 / 15 |
| `7114272f-478e-11f1-aec7-581122cf362c` | Стеллажи ПРЕМИУМ-3 высота 1800 (решетчатые полки) | НЕЙТРАЛЬНОЕ ОБОРУДОВАНИЕ > Стеллажи > Стеллажи ПРЕМИУМ-3 > Стеллажи ПРЕМИУМ-3 высота 1800 (решетчатые полки) | 4 | 15 / 15 |

Notes:

- `УПАКОВОЧНОЕ ОБОРУДОВАНИЕ` is the only **true 1C root** missing on site.
- Five stellazhi «решетчатые полки» leaves are 1C-only at leaf level (site has related non-grid variants under Neutral стеллажи).
- `ПОСУДА И ИНВЕНТАРЬ` is **not** site-missing as a category (mapped to `364`), but is a **hierarchy mismatch** (1C root vs site nested under Tech).

### Likely renames / name differences

32 categories classified `LIKELY_RENAMED_MATCH` (token/name ambiguity). Examples include spelling variants (`гастоемкостей` vs `гастроемкостей`) and overlapping section names. Full list: Storage `comparison/likely-renames-or-name-differences.csv`.

## 13. Demo / legacy suspect check

| Question | Answer |
|---|---|
| Any current root not present in 1C? | **Yes** — `90`, `93`, `96`, `171`, `186`, `205`, `206` lack 1C **root** counterparts |
| Likely old demo/manual placeholders? | **Suspects:** empty `[93] Инвентарь`, `[171] Барное`, `[205] Посудомоечные`, `[206] Вентиляционное`; inactive `[96] Запчасти` |
| Empty active sections justified by 1C? | Many Neutral empty leaves/parents are path-matched to 1C and are acceptable structure placeholders |
| `[96] Запчасти` backed by 1C? | **No 1C group hit** → legacy/manual suspect (inactive public 404) |
| `upakovochnoe` in 1C but absent on site? | **Yes** — 1C root present, site absent (known open item) |
| Different naming same semantics? | Yes — e.g. site root `Хлебопекарное оборудование` vs 1C nested `Хлебопекарное`; site `Инвентарь` vs 1C root `ПОСУДА И ИНВЕНТАРЬ` |
| Prior sync already intentional? | Partially — demo Group A `154–170` deleted earlier; Wave B1 mapped only `95`/`364`; `186`/`171`/`upakovochnoe` intentionally deferred |

**Classification:** `DEMO_LEGACY_SUSPECTS_FOUND` (roots listed above). Prior cleanup removed old demo branch `153+`; these remaining roots are a **new operator decision set**, not proof they were already deleted.

## 14. Empty / disabled but 1C-backed sections

Empty/inactive site categories that still match 1C by GUID/path/name are acceptable for structure parity (operator statement). Full list: Storage `comparison/disabled-empty-but-1c-backed.csv`.

Key acceptable pattern: many Neutral empty nestandart / комплектующие leaves remain path-matched to 1C.

Not acceptable as “1C-backed”: empty site-only roots `93/171/205/206` and inactive `96` (no 1C counterpart).

## 15. Public/sitemap support

From current export (supporting only):

- Active categories in sitemap: **225/225**
- Baseline/live sitemap: **1887**
- `[96] Запчасти`: not in sitemap, HTTP **404**
- `/upakovochnoe-oborudovanie`: absent, HTTP **404**
- Matched roots `79/95/362` and empty public roots `93/171/205/206`: sitemap yes / HTTP 200 (empty pages allowed by Launch Mode)

## 16. Decisions needed before any apply

Operator decisions required (no apply in this run):

1. **Keep vs hide/disable vs delete** empty site-only roots: `93`, `171`, `205`, `206`.
2. **Resolve `[96] Запчасти`**: keep inactive + products, remap, or cleanup charter.
3. **Hierarchy for `ПОСУДА И ИНВЕНТАРЬ`**: keep nested under `362` (current) vs promote to site root to mirror 1C.
4. **`УПАКОВОЧНОЕ ОБОРУДОВАНИЕ`**: create site category + map, or keep blocked while auto-create disabled.
5. **`186` Хлебопекарное` vs Tech nested `Хлебопекарное` / site `368`**: choose canonical home (Wave B already flagged collision).
6. **`90` Тепловое` vs Tech nested `Тепловое`**: choose root vs nested canonical.
7. Whether Neutral path-matched empties stay as intentional 1C structure mirrors.

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

Allowed: Storage evidence + this docs/report.

## 18. Git/worktree summary

- Authority worktree used for docs/report only.
- Dirty main `X:\AI MARS` not touched.
- Commit/push: report + OCPilot docs only (exact paths).

## 19. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-CATALOG-TREE-1C-COMPARISON-AUDIT-01\`

Key folders: `preflight/`, `reports-read/`, `site-tree/`, `import-files/` (includes live XML), `one-c-tree/`, `mapping-readonly/`, `comparison/`, `demo-legacy-check/`, `public-sitemap-support/`, `regression/`, `manifests/`, `logs/`.

## 20. SAFE UNKNOWN / blockers

- Exact product-count parity site↔1C for every leaf: approximate via XML product→group links; offers-side stock not used.
- Whether empty site-only roots were intentionally pre-seeded for future 1C groups vs leftover demos: **operator decision** (evidence supports suspect, not proof of origin).
- Whether 1C will later promote nested Тепловое/Хлебопекарное/Барное to roots: **SAFE UNKNOWN**.
- No blocker to operator review; blocker to apply remains intentional until decisions above.

## 21. Final verdict

`SITE-002 CATALOG TREE 1C COMPARISON AUDIT COMPLETE — STRUCTURE ATTENTION REQUIRED BEFORE APPLY`

Site and 1C trees are ready for operator/Web-GPT review. Root structure is only a **partial** match: three shared roots (Neutral / Holodilnoe / Tech), one hierarchy mismatch (Posuda), one 1C-only root (Upakovochnoe), and several site-only roots including demo/legacy suspects.

## 22. Next recommendation

1. Operator reviews inline trees in §§8–9 and roots matrix in §11 with Web-GPT.
2. Produce a bounded **HITL decision sheet** for the seven decision items in §16 (no apply yet).
3. Only after decisions: separate charters for (a) empty-root cleanup/disable, (b) upakovochnoe create/map, (c) хлебопекарное/тепловое canonical placement, (d) optional posuda root promotion.
4. Keep baseline **1887** untouched until an explicit refresh charter after structural apply.

---

**Changed files (this wave):** this report + OCPilot state/index/knowledge touch-ups.  
**Git:** commit/push docs only after staging exact allowlisted paths.
