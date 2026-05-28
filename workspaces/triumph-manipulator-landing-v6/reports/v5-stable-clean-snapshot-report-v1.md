# REPORT — V5 Stable Clean Snapshot

**Date:** 2026-05-24  
**Task:** Full survivability snapshot of stable V5 after typography, hover rollback, pricing center, contact-cta cleanup  
**Scope:** `workspaces/triumph-manipulator-landing-v5/` → `workspaces/_snapshots/`  
**Source modified:** No (copy-only; this report file created post-copy)  
**Commit / push:** Not performed

---

## Snapshot path

| Field | Value |
|-------|--------|
| **Snapshot ID** | `snap-20260524-193656-triumph-v5-stable-clean` |
| **Relative** | `workspaces/_snapshots/snap-20260524-193656-triumph-v5-stable-clean/` |
| **Full path** | `C:\AI MARS\workspaces\_snapshots\snap-20260524-193656-triumph-v5-stable-clean\` |
| **Manifest** | `workspaces/_snapshots/snap-20260524-193656-triumph-v5-stable-clean/SNAPSHOT-MANIFEST.md` |

---

## Snapshot contents

| Path | Count / note |
|------|----------------|
| `src/` | 195 files |
| `dist/` | 46 files (post-build, captured after `npm run build`) |
| `reports/` | 13 markdown reports (includes this report, synced post-copy) |
| `package.json` | Yes |
| `package-lock.json` | Yes |
| `gulpfile.js` | Yes |
| `README.md` | Yes |
| `SNAPSHOT-MANIFEST.md` | Created in snapshot root |

**Excluded:** `node_modules/`, `.git/`, `tmp/`, `cache/`, `logs/` — verified absent in snapshot.

---

## Manifest created

**Yes** — `SNAPSHOT-MANIFEST.md` in snapshot root includes:

- Snapshot ID, timestamp, baseline commit, branch
- Build status
- Typography / hover rollback / contact CTA / pricing alignment status
- Stable characteristics checklist
- Verification summary and restore notes

---

## Verification results

| Check | Live V5 | Snapshot | Result |
|-------|---------|----------|--------|
| `dist/index.html` | Present | Present | **PASS** |
| `dist/assets/css/style.css` | Present | Present | **PASS** |
| `dist/assets/img/hero/hero-bg-final.jpg` | Present | Present | **PASS** |
| `dist/assets/img/v5/second-screen/second-screen-index-baseline.jpg` | Present | Present | **PASS** |
| `src/` file count | 195 | 195 | **PASS** |
| `dist/` file count | 46 | 46 | **PASS** |
| `src/` SHA256 parity | — | 0 missing, 0 mismatch | **PASS** |
| `dist/` SHA256 parity | — | 0 missing, 0 mismatch | **PASS** |
| Contact CTA truck in CSS | 0 refs | 0 refs | **PASS** |
| `node_modules/` in snapshot | — | Absent | **PASS** |

---

## Build status

| Step | Result |
|------|--------|
| Workspace exists | **PASS** |
| `dist/index.html` (pre-build) | **PASS** |
| `npm run build` | **PASS** (exit 0, ~1.11s) |
| HEAD commit recorded | `6a2c89d08d66b1041107a69941c921044f74ed0f` |
| Branch | `mars/post-cycle8-live-tests` |

---

## Stable state summary

Checkpoint captures V5 after:

1. **Typography stabilization** — Pass 2/3: no mid-word splits, `text-wrap: balance` on headings, `_typography-protection.scss`, zakaz HTML nbsp ties.
2. **Forensic hover rollback** — transport cards no longer use unauthorized `hover-lift` / `translateY` (see `v5-pass-3-forensic-hover-regression-report-v1.md`).
3. **Pricing intro center fix** — `.pricing-factors .section-heading--center .section-lead` centered.
4. **Contact CTA background cleanup** — gradient + `#090c27` only; no truck image in CSS.

**Hero / second-screen:** baseline images present in src and dist; PPC transport stack at 1440px.

---

## SAFE UNKNOWN

- **Live browser QA** on snapshot preview not run in this session.
- **Git commit:** snapshot is filesystem-only; V5 has uncommitted changes vs `6a2c89d`; restore does not imply `git checkout`.
- **Orphan asset:** `v1-04-contact-truck.png` may still exist under `dist/assets/img/reconstruction/` (gulp copies all images) but is **not referenced** by CSS.
- **This report file** was written after initial snapshot copy and then synced into snapshot `reports/` (13 files total).
- **PPC multi-page builds:** default gulp output is `dist/index.html` (zakaz); other PPC pages **UNKNOWN** in default build target.

---

## Exact preview path

**Primary (snapshot):**

`C:\AI MARS\workspaces\_snapshots\snap-20260524-193656-triumph-v5-stable-clean\dist\index.html`

**Relative:**

`workspaces/_snapshots/snap-20260524-193656-triumph-v5-stable-clean/dist/index.html`

**Live equivalent (same build):**

`workspaces/triumph-manipulator-landing-v5/dist/index.html`

---

## Git

No commit. No push.
