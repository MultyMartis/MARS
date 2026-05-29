# URL EXPORT VALIDATION v1

**Date:** 2026-05-29 (post-sync)  
**Instance:** `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json`  
**Post-sync SHA-256:** `7264707fd557c9b64d2f8811040a3ce4237927b2741cfe05e0be0f3685029281`

---

## Validation checks

| Check | Result | Evidence |
|-------|--------|----------|
| All 12 routes present (`campaign.groups`) | **PASS** | `groupCount: 12` |
| Each group `landing_route.final_url` matches canonical | **PASS** | 12/12 canonical match |
| No legacy slug URLs in JSON URL fields | **PASS** | 0 hits on `manipulyator-` / `perevozka-` / `dostavka-` paths |
| No empty `landing_url` / `final_url` | **PASS** | 0 empty URL fields in audit walk |
| Non-canonical `https://manipulator-triumph.ru/*` landing URLs | **PASS** | 0 — only canonical set + host-only `display_url.domain` |
| Duplicate **route** URLs (per-group `final_url`) | **PASS** | 12 unique group finals |
| Fastlink URL reuse across ads | **EXPECTED** | Same canonical URL may appear in multiple fastlink slots (cross-intent) — not a route defect |

---

## Per-route `final_url` (post-sync)

| Group ID | `final_url` | Canonical match |
|----------|-------------|-----------------|
| `grp_fc01_5ton` | `https://manipulator-triumph.ru/5-tonn.html` | yes |
| `grp_fc02_bytovka` | `https://manipulator-triumph.ru/bytovki.html` | yes |
| `grp_fc03_stroymaterialy` | `https://manipulator-triumph.ru/stroymaterialy.html` | yes |
| `grp_fc04_yurlica` | `https://manipulator-triumph.ru/yurlic.html` | yes |
| `grp_fc05_6x6` | `https://manipulator-triumph.ru/vezdehod.html` | yes |
| `grp_fc06_oborudovanie` | `https://manipulator-triumph.ru/oborudovanie.html` | yes |
| `grp_fc07_konteynery` | `https://manipulator-triumph.ru/konteynery.html` | yes |
| `grp_fc08_armatura` | `https://manipulator-triumph.ru/armatura.html` | yes |
| `grp_fc09_kirpich` | `https://manipulator-triumph.ru/kirpich-bloki.html` | yes |
| `grp_fc10_fbs` | `https://manipulator-triumph.ru/fbs-zhbi.html` | yes |
| `grp_fc11_kray` | `https://manipulator-triumph.ru/kray.html` | yes |
| `grp_fc12_zakaz` | `https://manipulator-triumph.ru/` | yes |

---

## Exporter mapping validation

| File | Change verified |
|------|-----------------|
| `tools/exporter-cli/mapping.js` | `PRODUCTION_LANDING_SLUGS` → 11 `.html` slug filenames |
| `schema/landing-routing-schema-v1.md` | Production URL table → canonical `.html` paths (12 routes) |
| `tools/_build-full-cycle-draft.js` | `url()` + `FL.*.slug` → canonical `.html` paths |

---

## Not validated (SAFE UNKNOWN)

| Item | Status |
|------|--------|
| Regenerated Commander `.xlsx` | **UNKNOWN** — exporter CLI not run |
| `validation-cli` report / `export_allowed` | **UNKNOWN** |
| Commander import acceptance | **UNKNOWN** — human session required |
| Live production HTTP 200 on `.html` URLs | **UNKNOWN** |

---

## Verdict

**Export JSON layer:** ready for Commander export **regeneration** (human-operated `exporter-cli` run).  
**Commander import:** **not performed** — per task charter.
