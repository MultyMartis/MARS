# FP-0002 Operations Evidence Register v1

**Factory Project:** FP-0002 — Shpigovsky.ru  
**Ops workspace:** `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/`  
**Register version:** v1  
**Inventory snapshot:** 2026-07-05 (MASTER-16G shallow read-only)

---

## 0. Scope banner

This document is an **evidence register only**.

- Created under **MASTER-16G** from MASTER-16F design.
- **Does not** establish runtime delivery, production deployment, or go-live.
- **Does not** move, copy, or mutate assets.
- **Does not** replace **V9** as current product/source authority.
- **Does not** authorize cleanup, Git restore, Storage migration, or Localhost changes.
- **Does not** commit, stage, or classify foreign WIP.

---

## 1. Current authority pointers

| Item | Value |
|------|-------|
| Active frontend authority | **V9** static frontend (`workspaces/fp-0002-shpigovsky-v9/`) |
| V9-03 Stable Baseline | commit `a51376872fbfefb7d5f68a58b440c726d6cf3de3`; tag `fp-0002-v9-operator-approved-static-frontend-stable-01` |
| V9-04 Forge WordPress Intake Pack | commit `de1169cf`; tag `fp-0002-v9-forge-wordpress-intake-pack-01` |
| Git root / branch | `X:\AI MARS` · `mars/canonical-post-recovery` |
| V7 / V8 | Historical / superseded predecessor WIP — **not active authority**; V8 dirty cluster must not be commit/restored/cleaned automatically |
| Website Factory ops zone | `website-factory-operations/FP-0002-SHPIGOVSKY/` — operational records/evidence only, **not production runtime** |

---

## 2. INCOMING assets inventory and policy

**Policy baseline:** INCOMING assets are **protected**. Git vs Storage persistence for large binaries = **SAFE UNKNOWN**. Large binaries are **Storage policy candidates** only.

| Path/group | Type | Current persistence | Classification | Recommended policy | Notes |
|---|---|---|---|---|---|
| `INCOMING/README.md` | index doc | tracked-in-git | SOURCE_REFERENCE_ASSET | preserve in ops | Intake zone README |
| `INCOMING/01_DESIGN/` tracked PDFs/JPG/PNG | design exports | tracked-in-git | PROTECTED_CLIENT_ASSET | no move without charter | ~27 tracked design PDFs/JPG/PNG observed via `git ls-files` |
| `INCOMING/01_DESIGN/Spig_v1.2.fig` | Figma source | untracked-local | PROTECTED_CLIENT_ASSET | storage-candidate | Present on disk; not in `git ls-files`. **PROTECTED — NO_MOVE NO_COMMIT_WITHOUT_OPERATOR_CHARTER** |
| `INCOMING/01_DESIGN/Шпиговский.fig` | Figma source | gitignored-local | PROTECTED_CLIENT_ASSET | storage-candidate | `.gitignore` entry observed. **PROTECTED — NO_MOVE NO_COMMIT_WITHOUT_OPERATOR_CHARTER** |
| `INCOMING/01_DESIGN/26.06.2026/` | PNG export set | untracked-local | PROTECTED_CLIENT_ASSET | storage-candidate | Desktop/mobile page PNGs; not tracked. **PROTECTED — NO_MOVE NO_COMMIT_WITHOUT_OPERATOR_CHARTER** |
| `INCOMING/01_DESIGN/services-hub/SERVICES-HUB-DESKTOP.png` | PNG mockup | untracked-local | PROTECTED_CLIENT_ASSET | storage-candidate | MOBILE PNG tracked; DESKTOP untracked = **mixed** group. **PROTECTED — NO_MOVE NO_COMMIT_WITHOUT_OPERATOR_CHARTER** |
| `INCOMING/02_CONTENT/*.xlsx` | content spreadsheet | tracked-in-git | PROTECTED_CLIENT_ASSET | preserve in ops | 1 xlsx tracked |
| `INCOMING/02_CONTENT/video/` | video assets | untracked-local | PROTECTED_CLIENT_ASSET | storage-candidate | MP4 present; not tracked. **PROTECTED — NO_MOVE NO_COMMIT_WITHOUT_OPERATOR_CHARTER** |
| `INCOMING/03_BRANDING/*.svg` | brand SVGs | tracked-in-git | PROTECTED_CLIENT_ASSET | preserve in ops | logo + social icons tracked |
| `INCOMING/04_ACCESS/` … `INCOMING/09_ARCHIVE/` | placeholder README dirs | tracked-in-git (README only) | SAFE_UNKNOWN | preserve; no auto-populate | Access/hosting/WP/notes/client/archive slots — README stubs only observed |

---

## 3. WORDPRESS validation chain

Validation evidence is an **audit/validation chain**, not proof of production deployment.

| Phase | Suite / path | Verdict | Runtime writes | Classification | Delivery claim allowed? | Notes |
|---|---|---|---|---|---|---|
| Pre-D | `v9-06b2-acf-admission` | PASS (`collection-summary.json`; scan REVIEW_REQUIRED) | 0 | admission audit | NO | Source/admission only; no `final-verdict.json` |
| Pre-D | `v9-06c-content-model` | PASS (`generation-result.json`) | 0 | source generation | NO | Deterministic source generation; planning/source-only |
| Pre-D | `v9-06c1-source-activation-gate` | PASS | 0 | source gate | NO | Gate resolved; D.1 rerun ready |
| D.1 | `v9-06d1-runtime-delivery` | **BLOCKED** | NOT PERFORMED | negative evidence | **NO** | Skeleton gate blocker; `runtime_delivery: NOT PERFORMED` |
| D.1 rerun | `v9-06d1-runtime-delivery-rerun` | PASS / COMPLETE | bounded local activation | bounded runtime evidence | **NO** | Bounded local activation only — not final product delivery |
| D.2 | `v9-06d2-object-skeleton` | PASS / COMPLETE | performed (skeleton) | bounded runtime evidence | NO | Object skeleton; content migration NOT PERFORMED |
| D.3 | `v9-06d3-content-migration-planning` | PASS | 0 | planning | NO | Planning/source-only |
| D.4 | `v9-06d4-minimal-content-seed` | **BLOCKED** | NOT COMPLETE | negative evidence | **NO** | Initial seed blocked |
| D.4 rerun | `v9-06d4-minimal-content-seed-rerun` | PARTIAL PASS | partial | bounded partial evidence | **NO** | Partial seed only |
| Micro | `rewrite-flush-micro-gate` | PARTIAL PASS | partial flush | micro gate | NO | Partial rewrite flush evidence |
| Micro | `route-ownership-investigation` | PASS (d5-readiness BLOCKED in sub-suite) | 0 | diagnostic | NO | Investigation pass ≠ route delivery |
| Micro | `rewrite-rule-repair` | PASS | repair performed | bounded repair | NO | Route repair evidence; not go-live |
| D.5 | `v9-06d5-visual-route-qa` | PARTIAL PASS | validation reads | QA evidence | **NO** | Visual QA partial; no-runtime-mutation suites PASS |
| D.6 | `v9-06d6-template-integration-planning` | PASS | 0 | planning | NO | Template integration **planning** complete |
| D.7-A | `v9-06d7a-global-shell-asset-source` | PASS (`global_shell_asset_source: COMPLETE`) | **NOT PERFORMED** | source-only | **NO** | `runtime_delivery: NOT_PERFORMED` — source packaging only |
| D.7-B | `v9-06d7b-home-template-source` + `v9-06d7b-runtime-delivery` | PASS | YES — local theme files only; prior evidence-recorded action | VALIDATION_EVIDENCE_LOCAL_RUNTIME | **NO** | `home_template_source: COMPLETE` @ `c006edeb`; `runtime_delivery: PERFORMED` @ `3d42853a`; target `X:\MARS-Localhost\...\wp-content\themes\shpigovsky\`; apply 1 ADD / 11 MODIFY / 442 SAME / 0 DELETE; hash 454/454 PASS; routes smoke PASS; DB/content/ACF writes **0**; forbidden roots unchanged; checkpoint recorded; operator approval **SAFE UNKNOWN** |

**Delivery claim rules encoded:** BLOCKED = NO; PARTIAL PASS = NO; PASS planning/source-only = NO; D.1 rerun COMPLETE = NO; D.7-A = NO (`runtime_delivery NOT_PERFORMED`); D.7-B = NO (local bounded theme delivery evidence only; not production / not go-live / not remote CMS).

*Observed verdicts from `final-verdict.json` / suite summaries where present; Pre-D b2/c rows from collection/generation artifacts.*

---

## 4. Forge 05C admission receipts

| Field | Value |
|-------|-------|
| Receipt doc | `projects/mars-website-factory/subsystems/forge-wordpress/projects/fp-0002/FP-0002-V9-05C-READ-ONLY-PROJECT-ADMISSION-RECEIPT-v1.md` |
| Runtime reports path | `projects/mars-website-factory/subsystems/forge-wordpress/runtime/reports/fp0002-v9-05c-admission/` |
| Classification | **E3 dirty/local** (modified receipt JSON cluster in working tree) |
| Decision | **LEAVE_DIRTY_LOCAL** |
| Mode | `READ_ONLY` / `NO_MUTATION` / `write_authorized: false` |
| 17:18 re-inspect metadata | Preflight/receipts timestamped **2026-07-02T17:18:17Z–17:18:44Z** (`fp0002-admission-preflight-summary.json`, `wp-inspect-*` receipts) |
| Action now | **No restore / no commit / no automatic cleanup** |

---

## 5. REPORTS / temp / noise

Generated forensic/temp outputs — **index only**; not promoted to authority; **no cleanup without cleanup charter**.

| Path/group | Classification | Repo policy | Cleanup policy | Notes |
|---|---|---|---|---|
| `REPORTS/_fig_parse_temp/` | generated noise/evidence | mixed local | defer — charter required | Figma parse temp dir |
| `REPORTS/_fig_logo_extract/` | generated noise/evidence | mixed local | defer — charter required | Logo extract temp |
| `REPORTS/_fig_forensic_temp/` | generated noise/evidence | mixed local | defer — charter required | Forensic temp |
| `REPORTS/_fig_audit_page_sections_v2.json` | forensic output | tracked/mixed | defer — charter required | ~59 KB JSON |
| `REPORTS/_audit_extract_output.json` | forensic output | tracked/mixed | defer — charter required | ~306 KB JSON |
| `REPORTS/__pycache__/` | local Python cache | untracked-local | defer — charter required | Observed under REPORTS tools run |

---

## 6. phase-07b staged diff review

- File: `phase-07b-staged-diff-review.md` — **preserved ops review note**.
- Role: meaningful **boundary evidence** for staged FP-0002 ops / WF index promotion (2026-07-01; parent `eb47ebb…`; gate PASS).
- Standalone commit status: **SAFE UNKNOWN** (review references intended commit message; not verified committed here).
- Referenced in this register only — **no action now**.

---

## 7. Do-not-touch list

Protected clusters — no agent/operator mutation without explicit charter:

- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/theme/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/plugins/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/validation/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/architecture/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/WORDPRESS/reports/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_parse_temp/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_logo_extract/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/REPORTS/_fig_forensic_temp/**`
- `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/phase-07b-staged-diff-review.md`
- `workspaces/fp-0002-shpigovsky-v7/**`
- `workspaces/fp-0002-shpigovsky-v8/**`
- `workspaces/fp-0002-shpigovsky-v9/**`
- `projects/mars-website-factory/subsystems/forge-wordpress/runtime/reports/fp0002-v9-05c-admission/**`
- `X:\MARS-Localhost\**`
- `X:\AI MARS STORAGE\**`

---

## 8. Explicit non-claims

This register **does not** establish or imply:

- Runtime delivery success or final product delivery
- Production WordPress deployment or client-facing go-live
- Remote/live CMS operational status
- Autonomous Forge runtime or WPilot ownership transfer
- FW-07C-2 mutation charter authorization
- V7/V8 as current authority
- BLOCKED or PARTIAL PASS as success
- D7-A global-shell **runtime delivery** (source task explicitly `NOT_PERFORMED`)
- D7-B **production** WordPress deployment, client-facing go-live, or remote/live CMS status (local theme evidence only @ `3d42853a`)
- D7-B autonomous Forge runtime execution or WPilot ownership transfer
- D7-B Storage or INCOMING mutation
- D7-B DB/content/ACF writes (evidence-recorded: **0** @ `3d42853a`)
- D7-B Localhost activity as **prior evidence-recorded** action; **this register update performs no Localhost mutation**
- Storage policy resolution for INCOMING large binaries
- Cleanup authorization for temp/noise clusters
- Validity or exposure of secrets/credentials in INCOMING access slots

---

## 9. Future actions

Possible future operator waves only — **not executed by this register**:

1. INCOMING Storage policy charter (Git vs Storage for fig/video/large binaries)
2. Evidence register review / standalone commit decision (MASTER-16H candidate)
3. Forge 05C dirty receipt cluster — remain **LEAVE_DIRTY_LOCAL** unless separately chartered
4. Cleanup charter for `REPORTS/_fig_*` temp/noise after operator policy
5. Runtime delivery as a **separate operator-approved wave** (distinct from source/planning PASS)
6. Formal D7-B operator approval closure remains optional/future because parent context classified approval status as **SAFE UNKNOWN** while accepting `3d42853a` content as E4 evidence

---

## 10. Revision log

| Date | Wave | Change |
|---|---|---|
| 2026-07-05 | MASTER-16G | Initial evidence register created from MASTER-16F design; no runtime/storage/git claims. |
| 2026-07-05 | MASTER-16L | Added D7-B local home template runtime evidence row after `3d42853a`; preserved no-production/no-go-live/non-remote claims and approval SAFE UNKNOWN. |
