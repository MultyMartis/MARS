# REPORT — METALLKA SITE OPS PHASE 3A CHANGE 0001 PREPARATION

**Programme:** METALLKA-RU-SITE-OPS  
**Stage:** PHASE 3A — BOUNDED SITE OPS TASK PREPARATION  
**Date:** 2026-07-26  
**Production:** `https://metallka.ru/`  
**Result:** **COMPLETE — CHANGE 0001 PREPARED / NOT AUTHORIZED**

---

## Status

| Field | Value |
|-------|-------|
| Phase 3A | **COMPLETE** |
| CHANGE-REQUEST-0001 | **PREPARED — AWAITING OPERATOR CONTENT + EXECUTION APPROVAL** |
| CHANGE-0001 execution charter | **PREPARED / NOT AUTHORIZED** |
| Production mutation | **NONE** |
| Next | Operator supplies exact text + `APPROVE METALLKA CHANGE 0001 — ABOUT PAGE TEXT EDIT` → then Phase 3B (does not auto-start) |

---

## Environment

| Check | Result |
|-------|--------|
| cwd | `X:\AI MARS` |
| Volume X: label | **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `7ae0ba79e3f18b9bd1ea8994812a304f15cc1b8d` |
| Staged index | **Empty** (unchanged by this task) |
| Foreign WIP | **Untouched** |

---

## Target

| Field | Value |
|-------|-------|
| Task class | SMALL TEXT CONTENT CHANGE |
| Page ID | **52** |
| URL | `https://metallka.ru/about/` |
| Title (Phase 2B) | `О нас` |
| Slug | `about` |
| Block | One existing non-global `vc_column_text` |

---

## Ownership Verification

Re-verified from Phase 2B artefacts + sanitized Storage evidence — **no new production access**.

| Check | Result |
|-------|--------|
| ID / URL / type / status | 52 / `/about/` / page / publish |
| Template | `default` |
| WPBakery | Yes |
| `vc_column_text` | **1** |
| `vc_raw_html` | **0** |
| Forms / `dt_*` / Shortcoder in content | **0** |
| Global/shared text ownership | **Not evidenced** |
| The7 global options as body owner | **No** (chrome/meta only) |
| Verdict | **CLEAR** for charter prep; re-check live before Phase 3B save |

Note: Phase 2B metric `vc_column: 2` with `vc_column_text: 1` — re-confirm visual structure in WPBakery UI at execution; mutation boundary remains text-only.

---

## Authoring Surface

**Canonical:** WordPress Admin → page 52 → WPBakery editor → Update once.  

**Rejected for this task:** DB, WP-CLI, SQL, SFTP, theme files, bulk `post_content` replace, WPilot.

---

## Mutation Boundary

Allowed (future): textual content inside the single mapped `vc_column_text` on page 52 only.  

Forbidden: layout, rows/columns, attributes unrelated to text, `vc_raw_html`, template/title/slug, The7 globals, menu/header/footer, CSS/JS/PHP, plugin/theme updates, cache purge, WPilot, other pages.

---

## Backup Requirement

- Confirm Beget backup/restore still available before execution.  
- Mandatory page-level before snapshot (content + hash if practical + screenshot + timestamp).  
- WP revisions: **not verified** — do not rely exclusively.  
- Fresh full hosting backup: not solely required for this text edit if existing backup is current enough and page snapshot exists; otherwise mark as pre-execution requirement.  
- **No backup created in Phase 3A.**

---

## Validation Plan / Rollback / STOP

Documented in CHANGE-REQUEST-0001 (frontend desktop+mobile, shared smoke, admin, no auto purge; primary rollback = restore before text via WP Admin; STOP before/after save per charter).

---

## Required Operator Input

1. Exact old/current text **or** exact target block/substring.  
2. Exact replacement / new text.  
3. Backup posture confirmation (or fresh backup if inadequate).  

**No fabricated old/new text was prepared.**

---

## Execution Approval

```text
APPROVE METALLKA CHANGE 0001 — ABOUT PAGE TEXT EDIT
```

Authorizes only the bounded page-52 WPBakery text edit + validation/rollback. Does **not** authorize other pages, filesystem, updates, cache purge, or WPilot.

---

## Files Created

| Path |
|------|
| `projects/metallka-ru-site-ops/METALLKA-CHANGE-REQUEST-0001-ABOUT-TEXT-v1.md` |
| `projects/metallka-ru-site-ops/METALLKA-CHANGE-0001-EXECUTION-CHARTER-v1.md` |
| `projects/metallka-ru-site-ops/reports/REPORT-METALLKA-SITE-OPS-PHASE-3A-CHANGE-0001-PREPARATION.md` |

---

## Files Modified

| Path |
|------|
| `projects/metallka-ru-site-ops/OPERATIONAL-INDEX.md` |
| `projects/metallka-ru-site-ops/METALLKA-ARTIFACT-REGISTER-v1.md` |

---

## Production Mutations

**NONE.**

No WP Admin save, SSH/FTP write, cache purge, backup trigger, or WPilot operation.

---

## Git Operations

**NONE** (no commit, no push, no staging).

---

## Next Phase

```text
PHASE 3B — CHANGE 0001 PRODUCTION EXECUTION
```

Starts only after operator content + approval string. **Does not auto-start.**

---

## Stop Condition

**STOP after this REPORT.** Phase 3A preparation complete; execution remains **NOT AUTHORIZED**.
