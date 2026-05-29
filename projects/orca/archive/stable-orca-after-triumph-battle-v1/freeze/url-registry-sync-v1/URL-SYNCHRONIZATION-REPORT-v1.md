# URL SYNCHRONIZATION REPORT v1

**Label:** `orca-url-registry-sync-preflight-v1`  
**Date:** 2026-05-29  
**Project:** Triumph Manipulator

---

## Phase 0 — Backup / checkpoint

| Item | Result |
|------|--------|
| Checkpoint label | `orca-url-registry-sync-preflight-v1` |
| PRE-SYNC doc | `PRE-SYNC-CHECKPOINT-v1.md` |
| Commit at checkpoint | `dc05c479eedd50233442009413fc90dbf314428f` |
| Branch | `mars/post-cycle8-live-tests` |
| Uncommitted changes | Yes (repo-wide) |
| Git commit | **Not performed** |
| Git push | **Not performed** |

---

## Phase 1 — Audit

See `URL-INTEGRITY-AUDIT-v1.md`.

- **12** routes audited against canonical list.
- **11** registry MISMATCH at start; **1** OK (`/`).
- PPC JSON instance: **WARNING** (legacy URLs throughout).
- Live URLs: **UNKNOWN** (not HTTP-checked).

---

## Phase 2 — Synchronization

### Files updated (route metadata only)

| File | Change |
|------|--------|
| `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json` | All 12 routes: `slug` + `url` → canonical `.html` paths; `registry_version` → `v1` |
| `content-packs/examples/triumph-*-pack-v1/PACK-STATUS.md` (9 packs) | `url:` field synced |
| `triumph-manipulyator-5-tonn-pack-v1/PACK-METADATA.md` | `route_slug`, `canonical_url` |
| `triumph-bytovki-pack-v1/PACK-METADATA.md` | `route_slug`, `canonical_url` |
| `triumph-manipulyator-5-tonn-pack-v0.md` | frontmatter `route_slug`, `canonical_url` |
| `triumph-manipulyator-5-tonn-pack-v1/README.md` | route URL row |
| `triumph-bytovki-pack-v1/README.md` | route URL row |
| `triumph-bytovki-pack-v1/exports/artifact-links.md` | Route URL |
| `projects/.../landing-qa/v5-page01-landing-qa-v0.md` | QA URL header |
| `coordination/production-pack-readiness-checklist-v1.md` | canonical check criterion |

### Not changed (per charter)

- Marketing copy, H1, FAQ, CTA
- `triumph-s-tier-draft-v1.json` (PPC instance — separate export pass)
- Commander `.xlsx` files
- Freeze snapshot `route-family-freeze-v1`

### Mismatch fix counts

| Category | Fixed |
|----------|------:|
| Registry URL fields | 11 |
| PACK-STATUS `url:` | 9 |
| PACK-METADATA canonical | 2 |
| Supporting route URL rows | 4 |

---

## Phase 3 — Commander preparation

See `URL-COMMANDER-MAPPING-v1.md`.

| Commander alignment | Count |
|---------------------|------:|
| OK (homepage only) | 1 |
| MISMATCH (JSON vs canonical) | 11 |
| UNKNOWN (xlsx not opened) | export file on disk |

---

## Post-sync route status

| Status | Routes |
|--------|-------:|
| **OK** (registry + pack route metadata) | 12 |
| **WARNING** (PPC JSON / freeze / geo-alignment residual) | see audit |
| **UNKNOWN** (live HTTP, Commander xlsx) | 12 live; 1 xlsx |

---

## Files created (freeze folder)

```
projects/orca/freeze/url-registry-sync-v1/
├── PRE-SYNC-CHECKPOINT-v1.md
├── URL-INTEGRITY-AUDIT-v1.md
├── URL-COMMANDER-MAPPING-v1.md
└── URL-SYNCHRONIZATION-REPORT-v1.md
```

---

## SAFE UNKNOWN

| Item | Note |
|------|------|
| Live production URLs | Not HTTP-verified |
| Commander `.xlsx` contents | Not opened; mapping derived from JSON instance |
| `website_factory_page` dist paths | Still reference v4 slug folders where set |
| Factory V6 HTML output paths vs `.html` canonical | Not verified in repo |

---

## Git status (post-task)

New/modified under ORCA sync scope (representative):

- `projects/orca/freeze/url-registry-sync-v1/` (new)
- `projects/orca/projects/triumph-manipulator-krasnodar/landing-route-registry.json`
- Multiple `content-packs/examples/triumph-*/` route metadata files
- `projects/orca/coordination/production-pack-readiness-checklist-v1.md`

**Commit:** not performed · **Push:** not performed
