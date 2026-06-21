# XLSX REGENERATION QA v1

**Operation:** ORCA Commander XLSX Regeneration after URL-sync  
**Label:** `orca-commander-xlsx-regeneration-qa-v1`  
**Date:** 2026-05-29  
**Lane:** B  
**Source instance:** `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json`

---

## Validation result

| Field | Value |
|-------|--------|
| CLI | `tools/validation-cli` (Hardening v0.1) |
| Command | `node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json` |
| Working directory | `projects/orca/ppc/triumph-manipulator/tools/validation-cli` |
| Exit code | **0** |
| `validation_status` | **passed** |
| `export_allowed` | **true** |
| Blocking errors | **0** |
| Warnings | **0** |
| Rule evaluations | **345 pass** |
| Report path | `projects/orca/ppc/triumph-manipulator/tools/validation-cli/output/validation-report.output.json` |
| Report timestamp | `2026-05-29T07:14:13.729Z` |

**Verdict:** **PASS**

---

## Export result

| Field | Value |
|-------|--------|
| CLI | `tools/exporter-cli` — sheet1 ZIP patch v0.6 (full-cycle v1.1) |
| Command | `npm run export:sheet1-patch:full-cycle-v1.1` |
| Working directory | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli` |
| Exit code | **0** |
| Mode | `sheet1-zip-patch` |
| Rows patched | **108** |
| Last export row | **123** |
| Stale rows removed | **10** (rows 124–133) |
| Integrity check | **INTEGRITY_OK** (workbook reopened; mapped columns readable) |
| ZIP preserve check | **PASS** (no sharedStrings introduced) |
| Transport post-check | `node _validate-full-cycle-v1.1.js` — **PASS** |

**Verdict:** **PASS**

---

## Generated XLSX path

```
projects/orca/ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.1.xlsx
```

Absolute: `C:\AI MARS\projects\orca\ppc\triumph-manipulator\tools\exporter-cli\output\triumph-sheet1-patch-full-cycle-v1.1.xlsx`

**Note:** Path is gitignored (local transport artifact). File exists on disk after this run.

---

## Entity counts (source JSON)

| Entity | Expected (v1.1) | Actual | Match |
|--------|-----------------|--------|-------|
| Groups | 12 | **12** | yes |
| Ads | 20 | **20** | yes |
| Keywords | 64 | **64** | yes |
| Commander fill rows | 108 | **108** (rows 16–123) | yes |

---

## URL QA (programmatic — sheet1.xml)

**Method:** Read `xl/worksheets/sheet1.xml` from generated ZIP (same transport layer as `_validate-full-cycle-v1.1.js`). Scan data rows **16–123**.

| Column | Header (logical) | Role |
|--------|------------------|------|
| 48 | Ссылка | Landing / final URL |
| 49 | Отображаемая ссылка | Display path (short; no full URL) |
| 60 | Адреса быстрых ссылок | Fastlink URLs (`\|\|` joined) |

### Landing URLs (col 48)

- **12 unique** landing URLs in export matrix — all match canonical set
- Homepage route present: `https://manipulator-triumph.ru/` — **yes** (group 12 / master hot)
- Non-canonical landing URLs: **0**
- Legacy slug URLs (`manipulyator-`, `perevozka-`, `dostavka-`, non-`.html` paths): **0**

### Display paths (col 49)

- **12 unique** short display paths (e.g. `manip-5-tonn`, `bytovki`, `zakaz-manip`)
- No full `https://` URLs in display column — **PASS**
- Legacy slug paths in display column: **0**

### Fastlink URLs (col 60)

- **12 unique** fastlink URL tokens (canonical reuse across rows) — all in canonical set
- Non-canonical fastlink URLs: **0**
- Legacy fastlink URLs: **0**

### Canonical URL set verified

All landing and fastlink URLs ⊆ operator canonical list:

- `https://manipulator-triumph.ru/`
- `https://manipulator-triumph.ru/5-tonn.html`
- `https://manipulator-triumph.ru/armatura.html`
- `https://manipulator-triumph.ru/bytovki.html`
- `https://manipulator-triumph.ru/fbs-zhbi.html`
- `https://manipulator-triumph.ru/kirpich-bloki.html`
- `https://manipulator-triumph.ru/konteynery.html`
- `https://manipulator-triumph.ru/kray.html`
- `https://manipulator-triumph.ru/oborudovanie.html`
- `https://manipulator-triumph.ru/stroymaterialy.html`
- `https://manipulator-triumph.ru/vezdehod.html`
- `https://manipulator-triumph.ru/yurlic.html`

**URL QA verdict:** **PASS**

---

## Legacy URL scan

| Pattern | Hits in XLSX URL columns |
|---------|--------------------------|
| `manipulyator-*` path slugs | **0** |
| `perevozka-*` path slugs | **0** |
| `dostavka-*` path slugs | **0** |
| `manipulator-triumph.ru/<slug>/` (non-`.html`) | **0** |

**Legacy scan verdict:** **PASS** (no legacy URLs found)

---

## Commander readiness

| Gate | State |
|------|--------|
| validation-cli PASS | **yes** |
| `export_allowed: true` | **yes** |
| exporter-cli PASS | **yes** |
| XLSX opens (ZIP + integrity) | **yes** |
| URL QA PASS | **yes** |
| No legacy URL in XLSX | **yes** |

**Commander readiness:** **READY** (transport + URL layer — **not** import approval)

**Still blocked (by design):**

- Commander import — **not performed** (human HITL)
- `human_review.approved_for_commander_import` — unchanged / human-only
- Campaign launch — **not performed**

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Commander UI import acceptance | **UNKNOWN** — requires human smoke test in Yandex Direct |
| Excel desktop open (GUI) | **UNKNOWN** — validated via ZIP/XML + exporter integrity reopen only |
| Live HTTP 200 on `.html` URLs | **UNKNOWN** — not probed in this pass |
| Display path ↔ live site path parity | **UNKNOWN** — display paths are short Commander fields, not landing URLs |
| Commander schema / template drift vs live Direct | **UNKNOWN** |
| Prior on-disk XLSX before this run | **UNKNOWN** — overwritten by regeneration |

---

## Recommended human follow-up

1. Open `triumph-sheet1-patch-full-cycle-v1.1.xlsx` in Excel — spot-check col 48 (Ссылка) for 2–3 groups.
2. Run `commander-import-checklist-v1.1.md` — HITL import smoke test (no launch).
3. HTTP-check canonical `.html` URLs on production before launch.
4. Set `human_review.approved_for_commander_import` only after import smoke passes.

---

## Not performed (per charter)

- Commander import
- Ad launch / Direct API
- Git commit / push
- Changes to ad copy, keywords, fastlink titles, bids, or negatives
