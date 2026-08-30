# I-SEO Report Hub — Report Finalization Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Finalization Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORT-FINALIZATION-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORT-PREVIEW-RENDER-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый internal finalization / approval / locking слой** monthly report после:

- Auth persistence + local admin bootstrap;
- Reporting Period CRUD;
- Weekly Checkpoints CRUD;
- Monthly Report Content CRUD (DB-05);
- Report Blocks migration (DB-06) + Report Blocks CRUD;
- Report Preview / Render Implementation (internal preview + optional print route).

Цель charter:

1. Описать product model **finalization** (internal complete + lock), отдельно от public publish / PDF / client approval.
2. Зафиксировать readiness gates перед `finalized`.
3. Определить lock rules для `monthly_report_contents` и `report_blocks`.
4. Зафиксировать finalize / reopen (unfinalize) policy и role access.
5. Определить audit events и UI/status surface для следующей implementation wave.
6. Подготовить smoke/validation plan (включая текущий fixture, где readiness должна FAIL).
7. Не менять app-source / runtime / DB в этой волне.

Эта волна — **documentation / policy only**. Finalization **не** кодируется здесь.

---

## 2. Current Baseline

### Report Preview / Render implementation

| Item | Value |
|------|-------|
| Primary commit | `4334b4a853faa208f7334cc37925d3954d3bfd14` — `feat(iseo-report-hub): add report preview render` |
| Hash-record | `52bd58a9929c5c8de25d4a2d0041bac3f67e4947` — `docs(iseo-report-hub): record report preview render commit hash` |
| Clarify | `11a4f232b167d0d1512b1804fcf66c3d7c0a4b68` — `docs(iseo-report-hub): clarify report preview render commit hash record` |
| Smoke | **22/22 PASS** (per implementation closeout) |
| DB | **unchanged** by preview wave |
| Push | **no** |

### Upstream baselines (unchanged authority)

| Layer | Primary / hash-record |
|-------|------------------------|
| Auth | `d4b3b2e2…` / `0cd2cfb7…` |
| Reporting Period CRUD | `392258fc…` / `f1d8a17e…` |
| Weekly Checkpoints CRUD | `911db07d…` / `64c42cbe…` |
| Monthly Report Content CRUD | `65f64124…` / `17553a55…` (+ clarify `eb00b3f4…`) |
| DB-06 Report Blocks migration | `1b71a021…` / `7393d7c1…` (+ clarify `86338d66…`) |
| Report Blocks CRUD | `135da213…` / `5c65ac88…` |
| Report Preview / Render Charter | `f9604d4b…` / `34e7d9d0…` (+ clarify `65ab3a97…`) |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migrations | **5** |
| Tables | **13** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |
| report_blocks | **6** |

### Parent monthly report content

| Field | Value |
|-------|-------|
| Id | **1** |
| Parent period | id **1** / `2026-07` |
| Status | `in_progress` |
| Title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` (W1–W4) |
| `finalized_at` | **null** |
| Flat DB-05 fields | contain `LOCAL_FIXTURE_ONLY` |
| created_by / updated_by | **1** / **1** |

### Current report blocks (ordered)

| id | block_key | status | sort_order |
|----|-----------|--------|------------|
| 1 | `executive_summary` | `in_progress` | 15 |
| 2 | `work_completed` | `draft` | 20 |
| 3 | `results_summary` | `draft` | 30 |
| 9 | `risks_and_blockers` | `draft` | 35 |
| 4 | `key_findings` | `draft` | 40 |
| 5 | `next_month_plan` | `draft` | 50 |

All retain `LOCAL_FIXTURE_ONLY` markers / sources as applicable.

### Current preview

| Item | Value |
|------|-------|
| `GET /monthly-reports/1/preview` | auth **200** |
| `GET /monthly-reports/1/preview/print` | auth **200** |
| Render mode | `blocks_primary` |
| Block order | executive_summary → work_completed → results_summary → risks_and_blockers → key_findings → next_month_plan |

### Schema already available (no new migration for MVP)

- `monthly_report_contents.status`
- `monthly_report_contents.finalized_at`
- `report_blocks.status`
- `report_blocks.approved_at`
- audit log table from prior waves

Partial status transition / lock notes already exist in Monthly Report Content CRUD; **readiness gates, explicit finalize/reopen actions, parent→block lock enforcement, and finalization UI checklist are not a complete product workflow yet.**

---

## 3. Problem

Система умеет:

- редактировать monthly report content;
- редактировать report blocks;
- собирать internal preview/print.

Но **нет** контролируемого finalization / locking workflow:

- нет явных finalize / submit-review / mark-reviewed / reopen actions как product surface;
- нет readiness gates (required blocks, block statuses, source weekly resolve, preview render mode);
- нет enforced lock после `finalized` для block create/edit как parent-child policy;
- нет finalization readiness UI checklist;
- нет dedicated finalization audit events как product contract;
- нет immutable snapshot / client approval / public share (и они **не** входят в MVP finalization).

Итог: preview показывает черновик, но нельзя формально «закрыть» период как internal finalized report.

---

## 4. Scope

### In scope

- Internal monthly report finalization policy;
- Readiness gates;
- Lock rules for monthly content + report blocks;
- Status transitions (`draft` → … → `finalized`, reopen, archive);
- Role access for transitions;
- Audit events;
- Future implementation + smoke/validation plan;
- Docs-only Active Brain updates listed in this charter wave.

### Out of scope

- Public publishing / token URLs;
- PDF / export packages;
- Client portal / client approval / e-signature;
- Immutable snapshot table / version history;
- Email sending;
- Topvisor imports / charts / external metrics;
- Production deployment;
- Schema migrations;
- App-source / runtime / DB mutation **in this charter wave**.

---

## 5. Product Rules

1. **Finalization = internal complete + lock**, not publish.
2. Finalization is **not** PDF/export, **not** client approval, **not** public sharing.
3. Finalization is **not** an immutable snapshot unless a later snapshot layer is chartered.
4. Use existing DB-05 monthly status allowlist: `draft`, `in_progress`, `ready_for_review`, `reviewed`, `finalized`, `archived`.
5. Prefer **staged lifecycle** over direct jump to `finalized` (no casual admin shortcut unless explicitly logged override is implemented later).
6. Recommended lifecycle:
   - `draft` → `in_progress`
   - `in_progress` → `ready_for_review`
   - `ready_for_review` → `reviewed`
   - `reviewed` → `finalized`
   - any non-finalized → `archived`
   - `finalized` → `reviewed` / `in_progress` **only** via privileged reopen
7. After `finalized`: monthly edit + block create/edit locked for normal users; preview/print remain readable.
8. No hard DELETE.
9. Local fixture only (`LOCAL_FIXTURE_ONLY`); no real client data.
10. No new DB migration required for MVP finalization.

---

## 6. Readiness Gates

Before monthly can become `finalized`:

| Gate | Rule |
|------|------|
| Monthly exists | Target `monthly_report_contents` row exists |
| Parent period exists | Parent `reporting_periods` resolves |
| Title | Non-empty title |
| Preview | Preview composition succeeds; render mode is `blocks_primary` **or** valid `flat_fallback` |
| Blocks present | ≥1 non-archived report block |
| Required blocks | Canonical required keys exist (non-archived): `executive_summary`, `work_completed`, `results_summary`, `key_findings`, `next_month_plan` |
| Block statuses | All non-archived blocks must **not** be `draft` or `in_progress`; stricter MVP: required blocks at least `reviewed` (or `approved` if used) |
| Optional blocks | `risks_and_blockers`, `client_notes`, `internal_notes`, `custom_text`, `metric_snapshot`, `weekly_summary` — if present and non-archived, same non-draft/non-in_progress rule |
| Archived blocks | Ignored for readiness |
| Source weekly | All `source_weekly_checkpoint_ids` resolve; no missing ids |
| Admin override | **Not** default; only if explicitly implemented later with warning + audit |

**Current fixture readiness:** **FAIL** — `executive_summary` is `in_progress`; several required blocks are `draft`; `risks_and_blockers` is `draft`. Documented intentionally for failure-first smoke in Implementation 01.

---

## 7. Locking Rules

When monthly status is `finalized`:

- Monthly content normal edit blocked (except privileged reopen flow);
- Report block create / edit / status update blocked for normal users;
- Preview + print remain readable;
- Reporting period detail may still link to finalized report;
- Show `finalized_at`; actor via audit if no `finalized_by` column;
- Enforcement is **app-level** status checks (no schema change).

---

## 8. Reopen Policy

| Item | MVP policy |
|------|------------|
| Casual unfinalize button | **No** |
| Route | `POST /monthly-reports/{id}/reopen` |
| Who | **`admin_owner` only** |
| Effect | `finalized` → `reviewed` (preferred) or `in_progress` |
| `finalized_at` | **Preserve** as historical timestamp; reopen recorded in audit (no finalization history table in MVP) |
| Blocks | Reopen does **not** auto-change block statuses |
| `seo_lead_reviewer` reopen | **No** in MVP (can finalize; cannot reopen) |

---

## 9. Safety Boundary

- Docs-only this wave.
- No app-source / runtime / DB / SQL / migration edits.
- No secrets in docs.
- Foreign WIP preserved.
- Exact-path docs commit only; **push no**.
- Implementation wave may mutate **local fixture only** rows marked `LOCAL_FIXTURE_ONLY` (+ audit inserts); no production / no real client data.

---

## 10. Next Implementation Wave

**I-SEO Report Hub — Report Finalization Implementation 01**

Deliverables (future wave, not this charter):

- `ReportFinalizationService` + explicit transition routes;
- readiness checklist UI on monthly show (+ preview status cues);
- lock integration in monthly + block services;
- audit events;
- smoke: readiness FAIL → fixture prep → submit → review → finalize → lock → reopen → leave **finalized** as preferred end state for later export/snapshot work.

See design, implementation plan, and validation plan companions.
