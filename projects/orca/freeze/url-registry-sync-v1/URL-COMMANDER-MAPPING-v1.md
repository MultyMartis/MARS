# URL COMMANDER MAPPING v1

**Project:** Triumph Manipulator  
**Date:** 2026-05-29  
**Purpose:** Commander import preparation — canonical landing URLs vs current PPC JSON export.

**PPC instance reference:** `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json`  
**Commander template:** `projects/orca/ppc/triumph-manipulator/assets/direct-commander-template/` — **not opened in this pass (SAFE UNKNOWN for column literals).**

---

## Mapping table (12 routes)

| Route ID | Campaign group | Canonical URL | Expected Commander URL | Current export URL (JSON) | Status |
|----------|----------------|---------------|------------------------|---------------------------|--------|
| `zakazat-manipulyator` | 12 | `https://manipulator-triumph.ru/` | `https://manipulator-triumph.ru/` | `https://manipulator-triumph.ru/` | **OK** |
| `manipulyator-5-tonn` | 01 | `https://manipulator-triumph.ru/5-tonn.html` | `https://manipulator-triumph.ru/5-tonn.html` | `…/manipulyator-5-tonn/` | **MISMATCH** |
| `perevozka-bytovok` | 02 | `https://manipulator-triumph.ru/bytovki.html` | `https://manipulator-triumph.ru/bytovki.html` | `…/perevozka-bytovok/` | **MISMATCH** |
| `dostavka-stroymaterialov` | 03 | `https://manipulator-triumph.ru/stroymaterialy.html` | `https://manipulator-triumph.ru/stroymaterialy.html` | `…/dostavka-stroymaterialov/` | **MISMATCH** |
| `manipulyator-dlya-yurlic` | 04 | `https://manipulator-triumph.ru/yurlic.html` | `https://manipulator-triumph.ru/yurlic.html` | `…/manipulyator-dlya-yurlic/` | **MISMATCH** |
| `manipulyator-vezdehod` | 05 | `https://manipulator-triumph.ru/vezdehod.html` | `https://manipulator-triumph.ru/vezdehod.html` | `…/manipulyator-vezdehod/` | **MISMATCH** |
| `perevozka-oborudovaniya` | 06 | `https://manipulator-triumph.ru/oborudovanie.html` | `https://manipulator-triumph.ru/oborudovanie.html` | `…/perevozka-oborudovaniya/` | **MISMATCH** |
| `perevozka-konteynerov` | 07 | `https://manipulator-triumph.ru/konteynery.html` | `https://manipulator-triumph.ru/konteynery.html` | `…/perevozka-konteynerov/` | **MISMATCH** |
| `perevozka-armatury` | 08 | `https://manipulator-triumph.ru/armatura.html` | `https://manipulator-triumph.ru/armatura.html` | `…/perevozka-armatury/` | **MISMATCH** |
| `dostavka-kirpicha-blokov` | 09 | `https://manipulator-triumph.ru/kirpich-bloki.html` | `https://manipulator-triumph.ru/kirpich-bloki.html` | `…/dostavka-kirpicha-blokov/` | **MISMATCH** |
| `fbs-zhbi` | 10 | `https://manipulator-triumph.ru/fbs-zhbi.html` | `https://manipulator-triumph.ru/fbs-zhbi.html` | `…/perevozka-fbs-zhbi/` | **MISMATCH** |
| `manipulyator-krasnodarskiy-kray` | 11 | `https://manipulator-triumph.ru/kray.html` | `https://manipulator-triumph.ru/kray.html` | `…/manipulyator-krasnodarskiy-kray/` | **MISMATCH** |

**Expected Commander URL** = target state after registry sync (same as canonical).  
**Current export URL** = values present in `triumph-s-tier-draft-v1.json` at audit time — **not modified** in this sync pass.

---

## Display path (Commander visible path — unchanged)

| Route ID | `display_path` in registry |
|----------|----------------------------|
| `manipulyator-5-tonn` | `manip-5-tonn` |
| `perevozka-bytovok` | `bytovki` |
| `dostavka-stroymaterialov` | `stroymaterialy` |
| `manipulyator-dlya-yurlic` | `dlya-yurlic` |
| `manipulyator-vezdehod` | `vezdehod-6x6` |
| `perevozka-oborudovaniya` | `oborudovanie` |
| `perevozka-konteynerov` | `konteynery` |
| `perevozka-armatury` | `armatura` |
| `dostavka-kirpicha-blokov` | `kirpich-bloki` |
| `fbs-zhbi` | `fbs-zhbi` |
| `manipulyator-krasnodarskiy-kray` | `kray` |
| `zakazat-manipulyator` | `zakaz-manip` |

Display paths are **not** substituted into final URL per registry operator note.

---

## Commander export file status

| Artifact | Status |
|----------|--------|
| `triumph-s-tier-draft-v1.json` | Found — legacy URLs |
| `triumph-sheet1-patch-full-cycle-v1.1.xlsx` | **UNKNOWN** — not validated in this pass |
| Regenerated export after canonical sync | **UNKNOWN** — not produced |

---

## Recommended follow-up (human-operated)

1. Update `triumph-s-tier-draft-v1.json` group `landing_route.final_url` + ad `landing_url` + fastlink URLs to canonical `.html` paths.
2. Re-run exporter CLI → new Commander `.xlsx`.
3. HITL spot-check per `commander-import-checklist-v1.1.md` with updated landing URLs.
4. Live URL HTTP check on production before import.
