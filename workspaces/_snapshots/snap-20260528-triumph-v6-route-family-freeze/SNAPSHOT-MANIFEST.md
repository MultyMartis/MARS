# Snapshot Manifest

**Standard:** [projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md](../../../projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md)

---

## Identity

| Field | Value |
|-------|-------|
| **snapshot id** | `snap-20260528-triumph-v6-route-family-freeze` |
| **workspace** | `C:\AI MARS\workspaces\triumph-manipulator-landing-v6` |
| **timestamp** | `2026-05-29T10:21:00+03:00` |
| **operator** | Cursor agent (V6 route family freeze task) |

---

## Context

| Field | Value |
|-------|-------|
| **reason** | Full stable snapshot at V6 route family freeze — all 12 accepted routes built and verified; QA phase next |
| **risk class** | `LOW RISK` |
| **task / chat reference** | V6 Route Family Freeze (2026-05-29) |
| **linked incident** | none |

---

## Pre-operation state

- Branch: `mars/post-cycle8-live-tests`
- HEAD: `be0409e72feb1f43b44de8ed91188eb89a47126a`
- V6 workspace: 12 route pages in `src/pages/`; `npm run build` exit 0 (~1.5s)
- All 12 routes PASS dist verification (contacts, split FAQ, canonical markers, no mock/legacy endpoints)
- Route creation phase closed; no new routes in this freeze

---

## Git state

| Field | Value |
|-------|-------|
| **branch** | `mars/post-cycle8-live-tests` |
| **HEAD** | `be0409e72feb1f43b44de8ed91188eb89a47126a` |
| **working tree** | dirty — repo-wide changes outside V6 freeze scope |
| **untracked included in snapshot** | partial — snapshot tree is new; workspace V6 files copied as-is |

---

## Included / excluded

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

| Path | Source files | Snapshot files | Parity |
|------|-------------:|---------------:|--------|
| `src/` | 208 | 208 | PASS |
| `backend/` | 11 | 11 | PASS |
| `docs/` | 11 | 11 | PASS |
| `reports/` | 20 | 20 | PASS (at copy; freeze report added post-copy) |
| `tools/` | 6 | 6 | PASS |
| Root files | 4 | 4 | PASS |

Excluded directories verified absent in snapshot root.

---

## Restore instructions

1. Stop AGENT session on target workspace.
2. Verify this manifest — snapshot id and workspace paths.
3. Copy selected paths from snapshot to `workspaces/triumph-manipulator-landing-v6/`.
4. Run `npm install` if needed, then `npm run build`.
5. Verify all 12 routes in `dist/` per `V6-ROUTE-FAMILY-FREEZE.md`.
6. Log restore in `logs/rollback-history/` if used for recovery.

**Primary restore source paths:**

- `snap-20260528-triumph-v6-route-family-freeze/src/` → `workspaces/triumph-manipulator-landing-v6/src/`
- `snap-20260528-triumph-v6-route-family-freeze/backend/` → `workspaces/triumph-manipulator-landing-v6/backend/`
- Root build files (`package.json`, `gulpfile.js`, etc.) → workspace root

---

## Forbidden operations after snapshot

Until restore is verified **or** QA phase completes and snapshot is retired:

- [ ] No new route pages or partial scaffolds without explicit charter
- [ ] No edits to accepted route content listed in `V6-ROUTE-FAMILY-FREEZE.md` Section A
- [ ] No modification of `src/pages/index.html` during QA unless HITL override
- [ ] No recursive delete on V6 workspace
- [ ] No workspace delete-and-recreate

---

## Retention

| Tier | Value |
|------|-------|
| **retention tier** | `Reference` |
| **review date** | `2026-06-28` |

---

## SAFE UNKNOWN

| Item | Status |
|------|--------|
| Production deploy parity | SAFE UNKNOWN — not verified at snapshot time |
| Browser visual QA (mobile/desktop) | SAFE UNKNOWN — automated dist checks only |
| Live mailer SMTP delivery | SAFE UNKNOWN — endpoint presence verified only |
| MAX/Telegram production URLs | SAFE UNKNOWN — placeholder links remain in tree |

---

## Sign-off

| Field | Value |
|-------|-------|
| **manifest completed** | `2026-05-29` |
| **operator sign-off** | Cursor agent |
