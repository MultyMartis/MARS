# COMMANDER URL SYNC REPORT v1

**Operation:** ORCA Commander Export URL Synchronization  
**Label:** `orca-commander-url-sync-preflight-v1`  
**Date:** 2026-05-29  
**Lane:** B

---

## Summary

Synchronized Triumph Manipulator **Commander export layer** from legacy trailing-slash slug URLs to operator-confirmed **canonical `.html` URLs** on `https://manipulator-triumph.ru/`. Updated primary PPC JSON instance, exporter fastlink slug table, landing-route schema production table, and full-cycle draft builder.

**Not performed:** Commander import, ad launch, git commit, git push, XLSX regeneration.

---

## Backup / checkpoint

| Item | Value |
|------|--------|
| Checkpoint file | `PRE-COMMANDER-SYNC-CHECKPOINT-v1.md` |
| Branch | `mars/post-cycle8-live-tests` |
| Commit (preflight) | `dc05c479eedd50233442009413fc90dbf314428f` |
| Pre-sync JSON SHA-256 | `B48611BD308E736FC91B7D89DE55A60C2344F640FCE29634B512AA8808A7A776` |
| Post-sync JSON SHA-256 | `7264707fd557c9b64d2f8811040a3ce4237927b2741cfe05e0be0f3685029281` |

---

## Files changed

| File | Change |
|------|--------|
| `projects/orca/ppc/triumph-manipulator/schema/instances/triumph-s-tier-draft-v1.json` | 164 legacy URL string replacements (`final_url`, `landing_url`, `fastlinks[].url`) |
| `projects/orca/ppc/triumph-manipulator/tools/exporter-cli/mapping.js` | `PRODUCTION_LANDING_SLUGS` → 11 canonical `.html` slugs |
| `projects/orca/ppc/triumph-manipulator/schema/landing-routing-schema-v1.md` | Production URL table → 12 canonical routes |
| `projects/orca/ppc/triumph-manipulator/tools/_build-full-cycle-draft.js` | Canonical `.html` URL builder + `FL` slug map |

**Freeze artifacts created:** `projects/orca/freeze/commander-url-sync-v1/` (this report + audit + validation + mapping + checkpoint).

---

## Audit results (pre-sync)

- **12/12** routes present in PPC instance  
- **11 MISMATCH** (legacy slugs) · **1 OK** (homepage)  
- See `URL-EXPORT-AUDIT-v1.md`

---

## Sync results

- **11** route URL families updated to `.html` canonical paths  
- **1** route unchanged (homepage `/`)  
- Keywords, headlines, descriptions, callouts, display paths, negatives, bids — **not modified**

---

## Validation (post-sync)

- All 12 group `final_url` values match canonical set — **PASS**  
- No legacy slug paths in URL fields — **PASS**  
- No empty landing URLs — **PASS**  
- See `URL-EXPORT-VALIDATION-v1.md`

---

## Commander readiness

| Gate | State |
|------|--------|
| Export JSON URLs | **Ready** |
| Route mapping doc | `COMMANDER-URL-MAPPING-v1.md` |
| Regenerated XLSX | **UNKNOWN** — run `exporter-cli` before import |
| Commander import | **Blocked** — human-only; not executed |

---

## SAFE UNKNOWN

| Item | Notes |
|------|-------|
| Commander `.xlsx` on disk vs JSON | Template not regenerated in this pass |
| `validation-cli` / `export_allowed` | Not re-run |
| Live HTTP on `.html` URLs | Not verified |
| Commander schema drift | Not compared to live Direct UI |

---

## Recommended human follow-up

1. `cd projects/orca/ppc/triumph-manipulator/tools/exporter-cli` → validate + export (per `OPERATIONAL-INDEX.md` Route C).  
2. Spot-check col 48 landing URLs in generated XLSX.  
3. `commander-import-checklist-v1.1.md` — HITL before import.  
4. HTTP-check canonical URLs on production before launch.
