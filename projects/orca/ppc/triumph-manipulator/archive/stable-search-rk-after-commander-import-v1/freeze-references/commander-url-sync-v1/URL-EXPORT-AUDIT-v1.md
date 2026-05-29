# URL EXPORT AUDIT v1

**Label:** `orca-commander-url-sync-preflight-v1`  
**Date:** 2026-05-29  
**Scope:** Commander export layer — `projects/orca/ppc/triumph-manipulator/`  
**Instance:** `schema/instances/triumph-s-tier-draft-v1.json`

---

## Export discovery

| Artifact | Path | Role |
|----------|------|------|
| PPC instance (primary) | `schema/instances/triumph-s-tier-draft-v1.json` | Source of truth for exporter landing URLs |
| Commander header map | `tools/exporter-cli/commander-header-map-v0.json` | Col 48 `ads.landing_url` mapping |
| Exporter mapping | `tools/exporter-cli/mapping.js` | Transport + `PRODUCTION_LANDING_SLUGS` fastlink discipline |
| Landing route schema | `schema/landing-routing-schema-v1.md` | Route → `final_url` contract |
| Export mapping schema | `schema/export-mapping-schema-v1.md` | Entity → Commander column mapping |
| Commander template | `assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx` | Transport reference (**not audited cell-by-cell**) |
| Full-cycle builder | `tools/_build-full-cycle-draft.js` | Regeneration helper (legacy URLs pre-sync) |
| Route registry (external) | `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json` | Canonical `.html` URLs (already synced) |

**Generated XLSX on disk:** **UNKNOWN** — no `tools/exporter-cli/output/*.xlsx` present at audit time.

---

## Route audit (pre-sync)

| Route ID | Group ID | Current export URL (pre-sync) | Canonical URL | Status |
|----------|----------|-------------------------------|---------------|--------|
| `zakazat-manipulyator` | `grp_fc12_zakaz` | `https://manipulator-triumph.ru/` | `https://manipulator-triumph.ru/` | **OK** |
| `manipulyator-5-tonn` | `grp_fc01_5ton` | `https://manipulator-triumph.ru/manipulyator-5-tonn/` | `https://manipulator-triumph.ru/5-tonn.html` | **MISMATCH** |
| `perevozka-bytovok` | `grp_fc02_bytovka` | `https://manipulator-triumph.ru/perevozka-bytovok/` | `https://manipulator-triumph.ru/bytovki.html` | **MISMATCH** |
| `dostavka-stroymaterialov` | `grp_fc03_stroymaterialy` | `https://manipulator-triumph.ru/dostavka-stroymaterialov/` | `https://manipulator-triumph.ru/stroymaterialy.html` | **MISMATCH** |
| `manipulyator-dlya-yurlic` | `grp_fc04_yurlica` | `https://manipulator-triumph.ru/manipulyator-dlya-yurlic/` | `https://manipulator-triumph.ru/yurlic.html` | **MISMATCH** |
| `manipulyator-vezdehod` | `grp_fc05_6x6` | `https://manipulator-triumph.ru/manipulyator-vezdehod/` | `https://manipulator-triumph.ru/vezdehod.html` | **MISMATCH** |
| `perevozka-oborudovaniya` | `grp_fc06_oborudovanie` | `https://manipulator-triumph.ru/perevozka-oborudovaniya/` | `https://manipulator-triumph.ru/oborudovanie.html` | **MISMATCH** |
| `perevozka-konteynerov` | `grp_fc07_konteynery` | `https://manipulator-triumph.ru/perevozka-konteynerov/` | `https://manipulator-triumph.ru/konteynery.html` | **MISMATCH** |
| `perevozka-armatury` | `grp_fc08_armatura` | `https://manipulator-triumph.ru/perevozka-armatury/` | `https://manipulator-triumph.ru/armatura.html` | **MISMATCH** |
| `dostavka-kirpicha-blokov` | `grp_fc09_kirpich` | `https://manipulator-triumph.ru/dostavka-kirpicha-blokov/` | `https://manipulator-triumph.ru/kirpich-bloki.html` | **MISMATCH** |
| `fbs-zhbi` | `grp_fc10_fbs` | `https://manipulator-triumph.ru/perevozka-fbs-zhbi/` | `https://manipulator-triumph.ru/fbs-zhbi.html` | **MISMATCH** |
| `manipulyator-krasnodarskiy-kray` | `grp_fc11_kray` | `https://manipulator-triumph.ru/manipulyator-krasnodarskiy-kray/` | `https://manipulator-triumph.ru/kray.html` | **MISMATCH** |

**Summary:** 12 routes present · **1 OK** · **11 MISMATCH** · **0 UNKNOWN**

---

## Extended URL surface (pre-sync)

| Surface | Count | Notes |
|---------|-------|-------|
| `landing_route.final_url` | 12 | 11 legacy slug paths |
| `ad.landing_url` | 24 | Mirrored group legacy paths |
| `fastlinks[].url` | ~164 slots | Cross-intent sitelinks — all legacy host paths |
| `display_url.path_1` | unchanged | Short paths (`manip-5-tonn`, etc.) — **not** landing URLs |

**Exporter `PRODUCTION_LANDING_SLUGS` (pre-sync):** 5 legacy slug names — fastlink sort priority did not recognize `.html` canonical paths.

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Commander `.xlsx` cell URLs | **UNKNOWN** — template not diffed |
| Live HTTP on canonical `.html` | **UNKNOWN** — not checked |
| Validator re-run after sync | **UNKNOWN** — not executed in this pass |
