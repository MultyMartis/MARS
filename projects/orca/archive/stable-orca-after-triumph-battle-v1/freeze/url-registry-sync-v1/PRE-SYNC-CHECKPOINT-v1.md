# PRE-SYNC CHECKPOINT v1

**Label:** `orca-url-registry-sync-preflight-v1`  
**Date:** 2026-05-29  
**Operator lane:** B — ORCA URL Registry Synchronization  
**Project:** Triumph Manipulator (`triumph-manipulator-krasnodar`)

---

## Git state (preflight)

| Field | Value |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` |
| Commit hash | `dc05c479eedd50233442009413fc90dbf314428f` |
| Commit date | 2026-05-29 10:34:42 +0700 |
| Uncommitted changes | **Yes** — many modified and untracked files repo-wide (not limited to ORCA) |
| Push | **Not performed** (per task charter) |
| Commit | **Not performed** (per task charter) |

---

## Sync goal

Align ORCA **route metadata** (registry, pack `canonical_url` / `url` fields, `PACK-STATUS` route URLs) with **production canonical URLs** on `https://manipulator-triumph.ru/`, replacing legacy slug-style paths (e.g. `/perevozka-bytovok/`, `/manipulyator-5-tonn/`) with `.html` canonical paths.

**Out of scope for this checkpoint:** marketing copy, H1, FAQ, CTA, PPC ad text, Commander `.xlsx` export regeneration, live HTTP verification.

---

## Canonical URL set (target)

| # | Path |
|---|------|
| 1 | `/` |
| 2 | `/5-tonn.html` |
| 3 | `/armatura.html` |
| 4 | `/bytovki.html` |
| 5 | `/fbs-zhbi.html` |
| 6 | `/kirpich-bloki.html` |
| 7 | `/konteynery.html` |
| 8 | `/kray.html` |
| 9 | `/oborudovanie.html` |
| 10 | `/stroymaterialy.html` |
| 11 | `/vezdehod.html` |
| 12 | `/yurlic.html` |

**Domain:** `https://manipulator-triumph.ru/`

---

## Registry snapshot (pre-sync)

Source: `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json`

All 12 routes used **legacy slug URLs** (trailing-slash paths) except master hot `/` which was already canonical.

---

## Artifacts to produce (post-sync)

- `URL-INTEGRITY-AUDIT-v1.md`
- `URL-COMMANDER-MAPPING-v1.md`
- `URL-SYNCHRONIZATION-REPORT-v1.md`

---

## SAFE UNKNOWN (preflight)

| Item | Status |
|------|--------|
| Live production URL HTTP check | **Not performed** |
| Commander `.xlsx` on disk vs canonical | **Not reconciled in this preflight** |
| `triumph-s-tier-draft-v1.json` PPC instance | **Legacy URLs present pre-sync** — separate export pass required |
