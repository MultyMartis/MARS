# URL INTEGRITY AUDIT v1

**Project:** Triumph Manipulator (`triumph-manipulator-krasnodar`)  
**Date:** 2026-05-29  
**Sync label:** `orca-url-registry-sync-preflight-v1`  
**Canonical domain:** `https://manipulator-triumph.ru/`

---

## Audit scope

| Area | Path | Audited |
|------|------|---------|
| Project registry | `projects/orca/projects/triumph-manipulator-krasnodar/` | Yes |
| Content packs | `projects/orca/content-packs/examples/triumph-*-pack-v1/` | Yes |
| Coordination | `projects/orca/coordination/` | Yes (URL-bearing checklist rows) |
| Calibration | `projects/orca/calibration/triumph-manipulator/` | Yes |
| Intelligence | `projects/orca/intelligence/` | Yes — no Triumph URL metadata found |
| Route registry | `landing-route-registry.json` | Yes |
| PACK-STATUS (all 12 routes) | `**/PACK-STATUS.md` | Yes |

**Not in scope (documented as residual):** PPC JSON instance URLs, Commander `.xlsx`, marketing copy, freeze snapshot `route-family-freeze-v1` (historical).

---

## Status model

| Status | Meaning |
|--------|---------|
| **OK** | Route metadata matches canonical URL |
| **WARNING** | Canonical OK in registry/packs; dependent artifact still legacy |
| **MISMATCH** | Legacy slug URL found in audited route-metadata surface |
| **UNKNOWN** | URL not set or live/Commander not verified |

---

## Route audit matrix (post-sync)

| Route ID | Canonical URL | Registry (pre) | Registry (post) | PACK-STATUS | PACK-METADATA | Overall |
|----------|---------------|----------------|-----------------|-------------|---------------|---------|
| `zakazat-manipulyator` | `https://manipulator-triumph.ru/` | OK | OK | N/A (gates only) | OK | **OK** |
| `manipulyator-5-tonn` | `…/5-tonn.html` | MISMATCH | OK | N/A | OK (synced) | **OK** |
| `perevozka-bytovok` | `…/bytovki.html` | MISMATCH | OK | N/A | OK (synced) | **OK** |
| `dostavka-stroymaterialov` | `…/stroymaterialy.html` | MISMATCH | OK | OK (was UNKNOWN) | N/A | **OK** |
| `manipulyator-dlya-yurlic` | `…/yurlic.html` | MISMATCH | OK | OK | N/A | **OK** |
| `manipulyator-vezdehod` | `…/vezdehod.html` | MISMATCH | OK | OK | N/A | **OK** |
| `perevozka-oborudovaniya` | `…/oborudovanie.html` | MISMATCH | OK | OK | N/A | **OK** |
| `perevozka-konteynerov` | `…/konteynery.html` | MISMATCH | OK | OK | N/A | **OK** |
| `perevozka-armatury` | `…/armatura.html` | MISMATCH | OK | OK (was UNKNOWN) | N/A | **OK** |
| `dostavka-kirpicha-blokov` | `…/kirpich-bloki.html` | MISMATCH | OK | OK (was UNKNOWN) | N/A | **OK** |
| `fbs-zhbi` | `…/fbs-zhbi.html` | MISMATCH | OK | OK | N/A | **OK** |
| `manipulyator-krasnodarskiy-kray` | `…/kray.html` | MISMATCH | OK | OK | N/A | **OK** |

---

## Residual findings (not route-metadata)

| Location | Finding | Status |
|----------|---------|--------|
| `ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | All groups use legacy slug URLs in `final_url` / `landing_url` / fastlinks | **WARNING** — export refresh required |
| `freeze/route-family-freeze-v1/ORCA-ROUTE-FAMILY-FREEZE-v1.md` | Historical slug table | **WARNING** — freeze snapshot; not updated |
| `content-packs/examples/triumph-manipulyator-zakaz-pack-v1/ppc/geo-alignment.md` | Fastlink still references `/manipulyator-krasnodarskiy-kray/` | **WARNING** — PPC continuity doc (out of sync scope) |
| `calibration/triumph-manipulator/ppc-alignment/route-alignment-v1.md` | Master `/` only | **OK** |
| `intelligence/` | No Triumph route URLs | **OK** |
| Live HTTP verification | Not run | **UNKNOWN** |
| Commander `.xlsx` on disk | Not opened in this pass | **UNKNOWN** |

---

## Legacy URL patterns searched

| Pattern | Hits in route metadata (post-sync) |
|---------|-------------------------------------|
| `/perevozka-fbs-zhbi/` | 0 in registry + PACK-STATUS + PACK-METADATA |
| `/manipulyator-krasnodarskiy-kray/` | 0 in route metadata |
| `/zakaz-manipulyatora/` | 0 |
| `/manipulyator-dlya-yurlic/` | 0 in route metadata |
| `/perevozka-stroymaterialov/` / `/dostavka-stroymaterialov/` | 0 in route metadata |
| `/perevozka-bytovok/` | 0 in route metadata |

---

## Summary counts

| Metric | Count |
|--------|------:|
| Routes audited | 12 |
| MISMATCH at audit start (registry) | 11 |
| OK at audit start (registry) | 1 (`/`) |
| Route metadata fixed in sync pass | 11 registry + 9 PACK-STATUS + 3 PACK-METADATA + supporting README/artifact-links |
| Routes OK after sync (registry + packs) | 12 |
| Routes UNKNOWN (live / Commander) | 12 (live); Commander export **WARNING** |
