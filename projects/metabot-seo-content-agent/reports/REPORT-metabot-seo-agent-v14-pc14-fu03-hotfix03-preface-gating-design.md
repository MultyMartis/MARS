# REPORT — MetaBOT SEO Agent PC14-FU03 HOTFIX03 Preface Gating Design

**Date:** 2026-07-21  
**Classification:** Design-only · sanitized evidence · no live mutation  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — Worker status/preface UX gating after HOTFIX02  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer · SEO Content Agent only  

| Label | Value |
|-------|-------|
| **Design** | `PC14_FU03_HOTFIX03_PREFACE_GATING_DESIGN` |
| **Based on** | `PC14_FU03_HOTFIX02_OPERATOR_SMOKE_PASS` |
| **HOTFIX02 operator smoke commit** | `1343b676` |
| **HOTFIX02 production apply commit** | `65642ef2` |
| **Production Worker** | `p4mqb4VuPcemIDlC` |
| **Smoke task_id** | `seo20260720182937io0c5y` |
| **Open issue** | `PC14_FU03_HOTFIX03_PREFACE_GATING` |
| **Decision** | `PC14_FU03_HOTFIX03_PREFACE_GATING_DESIGN_READY_FOR_SANDBOX` |
| **Recommended next** | `PC14_FU03_HOTFIX03_PREFACE_GATING_SANDBOX_IMPLEMENTATION` |
| **Final status** | `COMPLETE — PC14-FU03 HOTFIX03 preface gating design ready` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |

**Constraints honored:** No n8n API. No Telegram / OpenRouter / Sheets. No workflow patch. No sandbox create. No lock clear. No `/run` retry. No raw/local/helper/runner staging. No foreign WIP staging. No `git add .` / `-A`. No push. No pull.

---

## 1. Executive Summary

HOTFIX02 fixed plain-safe STRICT QA REJECT delivery and passed operator smoke (`seo20260720182937io0c5y`). The remaining UX defect is a **false success preface** from `Status Complete` (`✅ Задача завершена` / `Результат готов. Отправляю материалы...`) that still fires before the final clean vs reject outcome is communicated.

This design selects **Option D — outcome-gated `Status Complete` wording** with **node delta 0**, keeping the node as the Restore → Close Lock sequencing bridge. Success wording only for clean / repair-clean; blocked-dirty / reject get blocked wording only; errors get error wording. **Option C (suppress success preface)** is the documented fallback if fresh production field predicates are unsafe.

**Decision:** `PC14_FU03_HOTFIX03_PREFACE_GATING_DESIGN_READY_FOR_SANDBOX`  
**Next:** `PC14_FU03_HOTFIX03_PREFACE_GATING_SANDBOX_IMPLEMENTATION`

---

## 2. Background

| Checkpoint | Subject |
|------------|---------|
| `1343b676` | HOTFIX02 operator smoke |
| `65642ef2` | HOTFIX02 production apply |
| `36012d8b` | HOTFIX02 production proposal |
| `67ecdc7c` | HOTFIX01 production apply |

HOTFIX02 intentionally deferred preface gating. Production Worker `p4mqb4VuPcemIDlC` currently contains HOTFIX02 send-branch fixes; Intake `x8EbTGKNdlBprLvk` and Admin `AR6QxGt8ZKH0xG2T` are out of scope. HOTFIX02 sandbox `TMhJbxtk6uUPDpEb` must not be mutated in this design task.

---

## 3. Problem Statement

On reject/blocked-dirty runs, the bot announces completion and outgoing materials, then later sends STRICT QA REJECT. That preface is logically wrong and misleading. Full statement: `exports/pc14-fu03-hotfix03-preface-gating-design/2026-07-21/pc14-fu03-hotfix03-preface-gating-design-problem-statement.md`.

---

## 4. Evidence From HOTFIX02 Smoke

| Field | Observed |
|-------|----------|
| Command window | 2026-07-21 01:29 local |
| Task ID | `seo20260720182937io0c5y` |
| Preface | Status Complete success preface **sent** |
| Reject | STRICT QA REJECT delivered 01:31; status `blocked-dirty` |
| Raw `*` | 0 |
| Telegram 400 | not observed |
| Content materials | blocked |
| `/locks` / `/health` | OK (operator evidence in smoke pack) |
| Decision | `PC14_FU03_HOTFIX02_OPERATOR_SMOKE_PASS` |
| Deferred | `PC14_FU03_HOTFIX03_PREFACE_GATING` |

Actual smoke evidence paths (committed):

- `exports/pc14-fu03-hotfix02-operator-smoke/2026-07-21/PC14-FU03-HOTFIX02-OPERATOR-SMOKE-MANIFEST.md`
- `.../pc14-fu03-hotfix02-operator-smoke-summary.json`
- `.../pc14-fu03-hotfix02-operator-smoke-telegram-transcript.sanitized.json`
- `.../pc14-fu03-hotfix02-operator-smoke-pass-checks.json`
- `.../pc14-fu03-hotfix02-operator-smoke-timeline.json`
- `.../pc14-fu03-hotfix02-operator-smoke-hotfix01-comparison.json`
- `.../pc14-fu03-hotfix02-operator-smoke-secret-scan.json`

**Note:** Task-listed names `pc14-fu03-hotfix02-operator-smoke-transcript.md`, `...-classification.json`, `...-locks-health.json`, `...-expected-vs-observed.json`, `...-open-items.json` were **not** present; equivalent content lives in the files above.

---

## 5. Current Behavior

Shared final chain (clean + reject), from committed HOTFIX02 design evidence:

`Format* → Take First Item → Status Complete → Restore → Close Lock → Restore After Lock → Parse Mode → Send Telegram Run`

| Node | Behavior |
|------|----------|
| `Status Complete` | Static HTML success preface — **false on reject** |
| `Status Final` | Progress: preparing final result — not the false-success claim |
| `Format Strict Reject Message` | Builds reject payload; emits `memory_status=blocked_dirty`, `blocked_diagnostic` |
| `Parse Mode` / `Send Telegram Run` | HOTFIX02 plain-safe final send (intact) |

Reject path **does** reach `Status Complete` before final diagnostic send.

---

## 6. Desired Behavior

- No success-preface before final outcome is known.
- Reject/blocked-dirty: blocked/reject wording only (or suppress).
- Clean/repair-clean: success wording allowed only after that branch is selected.
- Lock close, memory append, task_id, HOTFIX02/HOTFIX01/PC-07/TZ preserved.

---

## 7. Design Options

| Option | Verdict |
|--------|---------|
| A — Move success preface downstream | Secondary — connection/lock risk |
| B — Neutral processing text for all | Partial — can still mislead on reject |
| C — Suppress success preface | **Fallback** |
| D — Outcome-gated Status Complete wording | **SELECTED** |

Details: `pc14-fu03-hotfix03-preface-gating-design-options.json`.

---

## 8. Selected Design

**`HOTFIX03_DESIGN_D_OUTCOME_GATED_STATUS_COMPLETE`**

1. Keep `Status Complete` position and connections (sequencing bridge).
2. Replace static success text with outcome-aware wording using fields already present after `Format*` / `Take First` (especially `memory_status` / `blocked_diagnostic` on reject).
3. Policy: clean/repair-clean → success OK; blocked-dirty → blocked wording only; error → error wording only.
4. Leave `Status Final` unchanged unless fresh read proves false success.
5. Do not change HOTFIX02 sanitizer/send, HOTFIX01 restores, Close Lock, memory fan-out, generation/scanner/repair.
6. Node delta **0**.
7. Fallback **Option C** if predicates unsafe after fresh production read.

---

## 9. Scope Guard

In scope: design + sandbox plan only.  
Out of scope: live APIs, production apply, Intake/Admin, scanner/repair/generation, foreign WIP, broad git staging.  
See `pc14-fu03-hotfix03-preface-gating-design-scope-guard.json`.

---

## 10. Risk Matrix

Key risks: losing Close Lock sequencing if node deleted; HOTFIX02 reject regression; wrong clean/reject predicate; sandbox disabled states leaking to production. Mitigations: expression-only edit; regression guards; harness fixtures; production apply gates. Full matrix: `pc14-fu03-hotfix03-preface-gating-design-risk-matrix.json`.

---

## 11. Sandbox Implementation Plan

Next task: **`PC14_FU03_HOTFIX03_PREFACE_GATING_SANDBOX_IMPLEMENTATION`**

1. Fresh production read of `p4mqb4VuPcemIDlC`.
2. Clone inactive sandbox: `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03-hotfix03-preface`.
3. Disable side-effects; keep `Run Strict Surface Repair` disabled unless mocked.
4. Apply Option D (or C fallback) to `Status Complete` only.
5. Offline harness; no live Telegram/Sheets/OpenRouter.
6. Persist sanitized sandbox evidence; no production apply in that task.

See `pc14-fu03-hotfix03-preface-gating-design-sandbox-plan.json`.

---

## 12. Harness Plan

Fixtures: clean, repair-clean, blocked-dirty, error.  
Checks HF03-01…12: no premature success on reject; success only on clean paths if retained; lock/memory reachable; HOTFIX02 `*` safety; PC-07; TZ; restores; credentials/side-effects documented; node delta 0; structural chain intact; HTML-safe status text.  
See `pc14-fu03-hotfix03-preface-gating-design-harness-plan.json`.

---

## 13. Production Apply Gates

Production apply is **not** this task. Later gates must include:

- Sandbox harness PASS
- HOTFIX02 regression guards PASS
- Fresh production baseline vs sandbox delta allowlist = Status Complete (or documented C)
- Node count unchanged (delta 0)
- Side-effect enabled states restored from production baseline (not sandbox disables)
- Credentials unchanged
- Intake/Admin untouched
- Operator approval
- Rollback plan + raw pre-apply backup under `local/` (not committed)

---

## 14. Out-of-Scope Preserved

HOTFIX02 send safety · HOTFIX01 restores · PC-07 Close Lock · TZ HOTFIX01 · memory-first fan-out · strict scan/repair/generation · Intake/Admin · credentials · foreign WIP · HOTFIX02 sandbox `TMhJbxtk6uUPDpEb` (not mutated here).

---

## 15. SAFE UNKNOWN

- Exact live post-HOTFIX02 Worker JSON without fresh GET (design used committed sanitized topology).
- Exact clean-path `memory_status` / equivalent field names on `Format Run Pipeline` items.
- Whether `Status Complete` text is currently literal vs expression in live JSON.
- Parallel edits to the same Telegram `message_id`.
- n8n execution IDs for smoke task `seo20260720182937io0c5y`.
- Sheets lock/memory row proof for that smoke (Telegram-only evidence).

Sandbox implementation must validate topology/predicates on a fresh production export before patching.

---

## 16. Final Status

| Field | Value |
|-------|-------|
| **Decision** | `PC14_FU03_HOTFIX03_PREFACE_GATING_DESIGN_READY_FOR_SANDBOX` |
| **Recommended next** | `PC14_FU03_HOTFIX03_PREFACE_GATING_SANDBOX_IMPLEMENTATION` |
| **Final status** | `COMPLETE — PC14-FU03 HOTFIX03 preface gating design ready` |

Evidence directory: `projects/metabot-seo-content-agent/exports/pc14-fu03-hotfix03-preface-gating-design/2026-07-21/`
