# COMMANDER URL MAPPING v1

**Project:** Triumph Manipulator  
**Date:** 2026-05-29  
**Purpose:** Commander import preparation — legacy export URLs → canonical production URLs.

**PPC instance:** `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json`  
**Commander template:** `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/` — column literals **SAFE UNKNOWN** (not opened in this pass).

---

## Mapping table (12 routes)

| Route | Old URL (pre-sync export) | New URL (canonical / post-sync) | Status |
|-------|---------------------------|----------------------------------|--------|
| Master / заказ | `https://manipulator-triumph.ru/` | `https://manipulator-triumph.ru/` | **OK** (unchanged) |
| 5 тонн | `https://manipulator-triumph.ru/manipulyator-5-tonn/` | `https://manipulator-triumph.ru/5-tonn.html` | **SYNCED** |
| Бытовки | `https://manipulator-triumph.ru/perevozka-bytovok/` | `https://manipulator-triumph.ru/bytovki.html` | **SYNCED** |
| Стройматериалы | `https://manipulator-triumph.ru/dostavka-stroymaterialov/` | `https://manipulator-triumph.ru/stroymaterialy.html` | **SYNCED** |
| Юрлица | `https://manipulator-triumph.ru/manipulyator-dlya-yurlic/` | `https://manipulator-triumph.ru/yurlic.html` | **SYNCED** |
| Вездеход 6×6 | `https://manipulator-triumph.ru/manipulyator-vezdehod/` | `https://manipulator-triumph.ru/vezdehod.html` | **SYNCED** |
| Оборудование | `https://manipulator-triumph.ru/perevozka-oborudovaniya/` | `https://manipulator-triumph.ru/oborudovanie.html` | **SYNCED** |
| Контейнеры | `https://manipulator-triumph.ru/perevozka-konteynerov/` | `https://manipulator-triumph.ru/konteynery.html` | **SYNCED** |
| Арматура | `https://manipulator-triumph.ru/perevozka-armatury/` | `https://manipulator-triumph.ru/armatura.html` | **SYNCED** |
| Кирпич/блоки | `https://manipulator-triumph.ru/dostavka-kirpicha-blokov/` | `https://manipulator-triumph.ru/kirpich-bloki.html` | **SYNCED** |
| ФБС / ЖБИ | `https://manipulator-triumph.ru/perevozka-fbs-zhbi/` | `https://manipulator-triumph.ru/fbs-zhbi.html` | **SYNCED** |
| Краснодарский край | `https://manipulator-triumph.ru/manipulyator-krasnodarskiy-kray/` | `https://manipulator-triumph.ru/kray.html` | **SYNCED** |

---

## Group ID cross-reference

| Route (registry `route_id`) | Group ID |
|-----------------------------|----------|
| `manipulyator-5-tonn` | `grp_fc01_5ton` |
| `perevozka-bytovok` | `grp_fc02_bytovka` |
| `dostavka-stroymaterialov` | `grp_fc03_stroymaterialy` |
| `manipulyator-dlya-yurlic` | `grp_fc04_yurlica` |
| `manipulyator-vezdehod` | `grp_fc05_6x6` |
| `perevozka-oborudovaniya` | `grp_fc06_oborudovanie` |
| `perevozka-konteynerov` | `grp_fc07_konteynery` |
| `perevozka-armatury` | `grp_fc08_armatura` |
| `dostavka-kirpicha-blokov` | `grp_fc09_kirpich` |
| `fbs-zhbi` | `grp_fc10_fbs` |
| `manipulyator-krasnodarskiy-kray` | `grp_fc11_kray` |
| `zakazat-manipulyator` | `grp_fc12_zakaz` |

---

## Display path (unchanged — not landing URL)

| Route | `display_path` (Commander col 49) |
|-------|-----------------------------------|
| 5 тонн | `manip-5-tonn` |
| Бытовки | `bytovki` |
| Стройматериалы | `stroymaterialy` |
| Юрлица | `dlya-yurlic` |
| Вездеход | `vezdehod-6x6` |
| Оборудование | `oborudovanie` |
| Контейнеры | `konteynery` |
| Арматура | `armatura` |
| Кирпич/блоки | `kirpich-bloki` |
| ФБС/ЖБИ | `fbs-zhbi` |
| Край | `kray` |
| Master | `zakaz-manip` |

---

## Commander readiness

| Step | Status |
|------|--------|
| JSON landing URLs canonical | **Done** |
| Exporter slug table updated | **Done** |
| Regenerate `.xlsx` via `exporter-cli` | **Pending** — human-operated |
| Commander import | **Not performed** |
| Ad launch | **Not performed** |
