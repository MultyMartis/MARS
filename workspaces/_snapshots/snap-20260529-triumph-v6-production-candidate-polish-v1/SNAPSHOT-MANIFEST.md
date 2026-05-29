# Snapshot Manifest

**Standard:** `projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md`

---

## Identity

| Field | Value |
|-------|-------|
| **snapshot id** | `snap-20260529-triumph-v6-production-candidate-polish-v1` |
| **workspace** | `C:\AI MARS\workspaces\triumph-manipulator-landing-v6` |
| **timestamp** | `2026-05-29T14:16:00+03:00` (approx., post-build) |
| **operator** | Cursor agent (human-chartered checkpoint) |

---

## Context

| Field | Value |
|-------|-------|
| **reason** | Final scoped git checkpoint for accepted V6 production-candidate polish (contacts, messengers, footer nav, image mapping, hero cargo/proof typography, Open Sans normalization) |
| **risk class** | `MEDIUM` |
| **task / chat reference** | V6 production candidate polish checkpoint |
| **linked incident** | none |

---

## Pre-operation state

- **Branch:** `mars/post-cycle8-live-tests`
- **HEAD (at snapshot):** `f235bf13945008cea6dc4949a69370744cb56b44`
- **Working tree:** dirty — V6 polish under `workspaces/triumph-manipulator-landing-v6/` and Triumph project docs; unrelated repo changes **not** included in this commit scope
- **Build:** `npm run build` **PASS** in workspace before manifest write

---

## Git state

| Field | Value |
|-------|-------|
| **branch** | `mars/post-cycle8-live-tests` |
| **HEAD** | `f235bf13945008cea6dc4949a69370744cb56b44` (pre-commit baseline) |
| **working tree** | dirty — V6 polish paths only staged for commit |
| **untracked included in snapshot** | partial — full source tree copy; git commit stages manifest + report only from snapshot path |

---

## Restore instructions

1. Stop AGENT session on `workspaces/triumph-manipulator-landing-v6`.
2. Verify snapshot id and paths match this manifest.
3. Copy selective paths from snapshot → workspace (`src/`, `backend/`, root package files as needed).
4. Run `npm run build` and dist verification (12 routes, contacts, mailer path).
5. Log restore in `logs/rollback-history/` if human-operated rollback occurs.

**Primary restore source paths:**

- `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-polish-v1/src/` → `workspaces/triumph-manipulator-landing-v6/src/`
- `.../backend/` → `workspaces/triumph-manipulator-landing-v6/backend/`
- `.../package.json`, `package-lock.json`, `gulpfile.js`, `README.md` → workspace root

---

## Forbidden operations after snapshot

Until restore is verified **or** polish checkpoint is confirmed on remote:

- [ ] No recursive delete on `workspaces/triumph-manipulator-landing-v6/`
- [ ] No `git reset --hard` without human charter
- [ ] No mass search-replace across Triumph workspaces without new snapshot
- [ ] Do not edit `workspaces/triumph-manipulator-landing-v5/` (protected)

---

## Snapshot inventory

**Included:** `src/`, `backend/`, `docs/`, `reports/`, `tools/`, `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`

**Excluded:** `node_modules/`, `dist/`, `.cache/`, `logs/`, `tmp/`, `temp/`, `*.log`, `_backup/`, `_snapshots/`

| Path | Files (approx.) |
|------|----------------:|
| `src/` | 208 |
| `backend/` | 11 |
| `docs/` | 11 |
| `reports/` | 107 (includes QA screenshot artifacts in snapshot tree only) |
| `tools/` | 6 |

Excluded directories verified absent at snapshot root (`node_modules`, `dist`, etc.).

---

## Polish scope captured (accepted state)

| Track | Notes |
|-------|--------|
| Global phone/email | `+7 (918) 991-2-991`, `info@manipulator-triumph.ru` |
| Messenger links | MAX, Telegram, WhatsApp canonical URLs |
| Footer nav | clean-scroll via `header-menu.js` |
| Image mapping v1 | per-route hero/second-screen + micro-correction |
| Hero cargo cleanup | readability + `1025–1510px` cargo card rule |
| Typography | Open Sans normalization; Montserrat/Roboto removed from stack |
| Hero proof label | `761px+` micro-fix in `_v5-hero-extensions.scss` |

**Out of commit payload:** snapshot file tree (except this manifest + linked report).

---

## Verification summary (dist, post-build)

| Check | Result |
|-------|--------|
| 12 routes in `dist/` | **PASS** |
| `dist/backend/send-lead.php` | **PASS** |
| `dist/backend/api/forms/send.php` | **absent — PASS** |
| One `id="contacts"` per route | **PASS** |
| No `.hero__notice` | **PASS** |
| No `data-form-handler="mock"` | **PASS** |
| No `backend/api/forms/send.php` refs | **PASS** |
| Canonical contacts/messengers | **PASS** |
| Compiled CSS: Open Sans yes; Montserrat/Roboto no | **PASS** |
| Hero proof `761px+` rule in source | **PASS** |
| Hero cargo `1025–1510px` rule in source | **PASS** |

Detail: `reports/v6-production-candidate-polish-v1-snapshot-report.md`

---

## Related artifacts

| Artifact | Path |
|----------|------|
| Production candidate state doc | `projects/triumph-manipulator-landing/V6-PRODUCTION-CANDIDATE-STATE.md` |
| Image mapping pass doc | `projects/triumph-manipulator-landing/V6-IMAGE-MAPPING-PASS.md` |
| Prior candidate snapshot | `workspaces/_snapshots/snap-20260529-triumph-v6-production-candidate-v1/` (if present on disk) |

---

*Human-operated snapshot. Not automated enforcement.*
