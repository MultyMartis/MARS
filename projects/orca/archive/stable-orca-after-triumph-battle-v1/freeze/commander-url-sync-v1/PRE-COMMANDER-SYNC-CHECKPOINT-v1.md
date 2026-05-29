# PRE-COMMANDER SYNC CHECKPOINT v1

**Label:** `orca-commander-url-sync-preflight-v1`  
**Date:** 2026-05-29  
**Operator lane:** B — ORCA Commander Export URL Synchronization  
**Project:** Triumph Manipulator (`triumph-manipulator-krasnodar`)

---

## Git state (preflight)

| Field | Value |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` |
| Commit hash | `dc05c479eedd50233442009413fc90dbf314428f` |
| Uncommitted changes | **Yes** — repo-wide modified/untracked files |
| Push | **Not performed** (per task charter) |
| Commit | **Not performed** (per task charter) |

---

## Operation goal

Synchronize **Commander export layer** landing URLs in PPC JSON and exporter route mappings to production **canonical `.html` URLs** on `https://manipulator-triumph.ru/`. Replace legacy trailing-slash slug paths (e.g. `/manipulyator-5-tonn/`, `/perevozka-bytovok/`).

**Out of scope:** Commander import, ad launch, push, keywords/headlines/fastlink titles/minus-words/bids, XLSX regeneration.

---

## Canonical URL set (target)

| # | URL |
|---|-----|
| 1 | `https://manipulator-triumph.ru/` |
| 2 | `https://manipulator-triumph.ru/5-tonn.html` |
| 3 | `https://manipulator-triumph.ru/armatura.html` |
| 4 | `https://manipulator-triumph.ru/bytovki.html` |
| 5 | `https://manipulator-triumph.ru/fbs-zhbi.html` |
| 6 | `https://manipulator-triumph.ru/kirpich-bloki.html` |
| 7 | `https://manipulator-triumph.ru/konteynery.html` |
| 8 | `https://manipulator-triumph.ru/kray.html` |
| 9 | `https://manipulator-triumph.ru/oborudovanie.html` |
| 10 | `https://manipulator-triumph.ru/stroymaterialy.html` |
| 11 | `https://manipulator-triumph.ru/vezdehod.html` |
| 12 | `https://manipulator-triumph.ru/yurlic.html` |

---

## Export artifacts inventory (pre-sync)

| Artifact | Path | Pre-sync SHA-256 | Notes |
|----------|------|------------------|-------|
| PPC instance (primary) | `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | `B48611BD308E736FC91B7D89DE55A60C2344F640FCE29634B512AA8808A7A776` | 12 groups · legacy slug URLs on 11 routes |
| Commander header map | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/commander-header-map-v0.json` | — | Column mapping only · no landing URLs |
| Exporter mapping | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/mapping.js` | — | `PRODUCTION_LANDING_SLUGS` = legacy slug names (5 entries) |
| Landing route schema | `projects/orca/ppc/triumph-manipulator/schema/landing-routing-schema-v1.md` | — | Production table = legacy slugs |
| Export mapping schema | `projects/orca/ppc/triumph-manipulator/schema/export-mapping-schema-v1.md` | — | Field mapping · no literal URLs |
| Commander template (reference) | `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx` | — | **Not modified** · transport shape reference |
| Generated export XLSX | `tools/exporter-cli/output/*.xlsx` | — | **UNKNOWN** — no output files present in tree at preflight |
| Full-cycle draft builder | `projects/orca/ppc/triumph-manipulator/tools/_build-full-cycle-draft.js` | — | Legacy slug constants · not primary instance |

**Registry reference (already canonical):** `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json` — synced in prior `url-registry-sync-v1` pass.

---

## Pre-sync URL state (PPC JSON groups)

| Group ID | Route role | Pre-sync `final_url` |
|----------|------------|----------------------|
| `grp_fc12_zakaz` | Master | `https://manipulator-triumph.ru/` |
| `grp_fc01_5ton` | 5 t | `…/manipulyator-5-tonn/` |
| `grp_fc02_bytovka` | Бытовки | `…/perevozka-bytovok/` |
| `grp_fc03_stroymaterialy` | Стройматериалы | `…/dostavka-stroymaterialov/` |
| `grp_fc04_yurlica` | B2B | `…/manipulyator-dlya-yurlic/` |
| `grp_fc05_6x6` | Вездеход | `…/manipulyator-vezdehod/` |
| `grp_fc06_oborudovanie` | Оборудование | `…/perevozka-oborudovaniya/` |
| `grp_fc07_konteynery` | Контейнеры | `…/perevozka-konteynerov/` |
| `grp_fc08_armatura` | Арматура | `…/perevozka-armatury/` |
| `grp_fc09_kirpich` | Кирпич/блоки | `…/dostavka-kirpicha-blokov/` |
| `grp_fc10_fbs` | ФБС/ЖБИ | `…/perevozka-fbs-zhbi/` |
| `grp_fc11_kray` | Край | `…/manipulyator-krasnodarskiy-kray/` |

---

## SAFE UNKNOWN (preflight)

| Item | Status |
|------|--------|
| Live HTTP check on production `.html` URLs | **Not performed** |
| Commander `.xlsx` cell URLs vs JSON | **Not opened** — template on disk only |
| Regenerated export after sync | **Not produced** in this pass |
