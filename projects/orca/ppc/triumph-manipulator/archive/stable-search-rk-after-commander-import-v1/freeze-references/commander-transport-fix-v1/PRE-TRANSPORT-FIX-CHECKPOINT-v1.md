# PRE-TRANSPORT-FIX CHECKPOINT v1

**Label:** `orca-commander-transport-fix-v1-pre-checkpoint`  
**Date:** 2026-05-29  
**Lane:** B — ORCA Commander Export Transport Fix  
**Mode:** Checkpoint only — no Commander import, no launch

---

## Git state

| Field | Value |
|-------|-------|
| Commit | `c337e27d56960683347800e00c64508a689459ea` |
| Branch | `mars/post-cycle8-live-tests` |

---

## Current problem

`mapTemplateFillRows()` in `exporter-cli/mapping.js` builds a **Cartesian product** `ad × keyword` per group. Direct Commander treats each populated text row as a separate ad, so **108 transport rows** become **108 ads** in UI instead of **20 ads + 64 keyword phrases**.

**Root cause:** Source C in [DUPLICATE-ADS-AUDIT-v1.md](../commander-url-sync-v1/DUPLICATE-ADS-AUDIT-v1.md) — not JSON duplication.

---

## Current XLSX (pre-fix)

| Artifact | Path | Data rows |
|----------|------|-----------|
| Full cycle v1.1 (broken transport) | `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.1.xlsx` | 108 |
| Full cycle v1 (older keyword set) | `…/output/triumph-sheet1-patch-full-cycle-v1.xlsx` | 82 |

**Source JSON:** `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json`

| Entity | Count |
|--------|-------|
| Groups | 12 |
| Ads | 20 |
| Keywords | 64 |

---

## Affected files (planned)

| File | Change |
|------|--------|
| `tools/exporter-cli/mapping.js` | Split `mapTemplateFillRows()` → ad rows + keyword rows |
| `tools/exporter-cli/sheet1-xml-builder.js` | Row-type field routing (no ad text on keyword rows) |
| `tools/exporter-cli/commander-header-map-v0.json` | Col 1 «Доп. объявление группы» mapping |
| `tools/exporter-cli/_validate-no-duplicate-ads-v1.js` | Post-export QA |
| `tools/exporter-cli/package.json` | `export:sheet1-patch:full-cycle-v1.2` |
| `projects/orca/freeze/commander-transport-fix-v1/*` | Design + QA docs |

**Not changed:** JSON instance semantics, keywords, ad copy, URLs, campaign structure.

---

## Fix goal

| Metric | Before | After (target) |
|--------|--------|----------------|
| Commander ads (transport) | 108 (duplicated) | 20 |
| Keyword phrase rows | merged into ad rows | 64 |
| Groups | 12 | 12 |
| Sheet1 data rows | 108 | 84 (20 + 64) |
| Duplicate ad signatures | 20 groups affected | 0 |
| Canonical `.html` URLs | preserved | preserved |
| Fastlinks / display paths / region | preserved | preserved |

---

## Human actions deferred

- Commander import test (explicitly out of scope)
- Launch / push (explicitly out of scope)
- Git commit (explicitly out of scope)
