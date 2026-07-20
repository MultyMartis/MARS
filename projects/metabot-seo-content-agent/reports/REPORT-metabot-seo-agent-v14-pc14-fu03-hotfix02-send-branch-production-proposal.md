# REPORT — MetaBOT SEO Agent PC14-FU03 HOTFIX02 Send Branch Production Proposal

**Date:** 2026-07-20  
**Classification:** Production proposal only — GET-only production + sandbox baseline · **no live mutation**  
**Scope:** MetaBOT SEO Content Agent v14 (`@seo_content_agent_bot`) — PC14-FU03 HOTFIX02 send-branch plain-safe + memory-first fan-out  
**Lane:** B — MetaBOT / MetaBOT SEO Agent / MetaBOT Developer · SEO Content Agent only  

| Label | Value |
|-------|-------|
| **Proposal** | `PC14_FU03_HOTFIX02_PRODUCTION_PROPOSAL` |
| **Based on sandbox implementation** | `PC14_FU03_HOTFIX02_SANDBOX_APPLIED_HARNESS_VERIFIED` |
| **Based on design** | `PC14_FU03_HOTFIX02_SEND_BRANCH_DESIGN_READY_FOR_SANDBOX` |
| **Based on diagnostics** | `PC14_FU03_HOTFIX01_SMOKE_DIAGNOSED_TELEGRAM_API_FAILURE` |
| **Production HOTFIX01 apply commit** | `67ecdc7c` |
| **Production Worker** | `p4mqb4VuPcemIDlC` |
| **Sandbox source** | `TMhJbxtk6uUPDpEb` |
| **Failed Worker execution fixture** | `3364` |
| **Failed task_id fixture** | `seo202607201222012uqhz9` |
| **Decision** | `PC14_FU03_HOTFIX02_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next** | `PC14_FU03_HOTFIX02_PRODUCTION_PROPOSAL_PERSIST` |
| **After persist** | `PC14_FU03_HOTFIX02_PRODUCTION_APPLY` |
| **Final status** | `COMPLETE — PC14-FU03 HOTFIX02 production proposal ready` |
| **Secret scan** | `PASS_WITH_REVIEW_LABELS` |

**Current statuses preserved / context:**

| Item | Status |
|------|--------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` |
| PC14-FU-01 | `PC14_FU01_CLOSED_NEXT_SELECTED` |
| PC14-FU-02 production apply | `PC14_FU02_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU02 HOTFIX01 production apply | `PC14_FU02_HOTFIX01_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU03 production apply | `PC14_FU03_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU03 HOTFIX01 production apply | `PC14_FU03_HOTFIX01_PRODUCTION_APPLIED_HARNESS_VERIFIED` |
| PC14-FU03 HOTFIX01 operator smoke | `PC14_FU03_HOTFIX01_SMOKE_DIAGNOSED_TELEGRAM_API_FAILURE` |
| PC14-FU03 HOTFIX02 sandbox | `PC14_FU03_HOTFIX02_SANDBOX_APPLIED_HARNESS_VERIFIED` |
| **This task** | `PC14_FU03_HOTFIX02_PRODUCTION_PROPOSAL` → ready for approval |

**Constraints honored:** Production Worker **not** patched. Sandbox **not** mutated. No Telegram / OpenRouter / Sheets. No `/run` / `/health` / `/locks`. No lock/memory cleanup. No Intake/Admin mutation. No stage / commit / push / pull. Foreign WIP preserved.

---

## 1. Executive Summary

PC14-FU03 HOTFIX02 is **ready for operator-approved production apply**. Fresh GET confirms:

1. Production Worker `p4mqb4VuPcemIDlC` still has HOTFIX01 applied and **does not** contain HOTFIX02.
2. Inactive sandbox `TMhJbxtk6uUPDpEb` still carries the harness-verified HOTFIX02 delta (reject plain-safe + Parse Mode plain-safe + memory-first fan-out).
3. Proposed production delta is exactly the approved sandbox allowlist: **2** `jsCode` replaces + **1** connection reorder · node delta **0**.

Automated preflight gates **all PASS**. Blockers: **none**.

| Field | Value |
|-------|-------|
| **Production Worker** | `SEO Content Agent Beta.v14 - Worker` (`p4mqb4VuPcemIDlC`) |
| **Active** | `true` |
| **Node count** | `101` |
| **FU03 nodes** | `9` |
| **updatedAt** | `2026-07-20T11:03:34.279Z` (matches HOTFIX01 apply) |
| **`Run Strict Surface Repair`** | enabled (`disabled=false`) |
| **HOTFIX01 restores** | intact (1112 / 1123) |
| **HOTFIX02 on production** | **absent** |
| **Reject fan-out (prod)** | `Take First Item` → `Prepare Memory Row Run` |
| **Proposed patch** | 2 code nodes + 1 fan-out reorder · node delta **0** |
| **Sandbox harness** | HF02 10/10 PASS (offline) |
| **Do not** | retry `/run` before production HOTFIX02 apply |

**Decision:** `PC14_FU03_HOTFIX02_READY_FOR_PRODUCTION_APPROVAL`  
**Next:** `PC14_FU03_HOTFIX02_PRODUCTION_PROPOSAL_PERSIST` → then `PC14_FU03_HOTFIX02_PRODUCTION_APPLY`

---

## 2. Background

HOTFIX01 production apply (`67ecdc7c`) fixed reject-path restore + lock closure. Operator smoke (execution `3364`, task `seo202607201222012uqhz9`) still failed at `Send Telegram Run` with Telegram HTTP 400 entity-parse because reject excerpts retained raw `*` while `Parse Mode` did not neutralize asterisks. Memory append was skipped when send failed because reject fan-out listed `Take First Item` before `Prepare Memory Row Run`.

HOTFIX02 design selected `HOTFIX02_DESIGN_COMBINED_B_C_MINIMAL`. Sandbox implementation applied that patch to inactive `TMhJbxtk6uUPDpEb` and verified HF02 10/10 offline. This task proposes transplanting the same allowlisted delta onto production — **proposal only**.

---

## 3. Preflight

| Check | Result |
|-------|--------|
| Working directory | `X:\AI MARS` — **PASS** |
| Volume `X:` label | `AI WS` — **PASS** |
| Git branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD / checkpoint | `67ecdc7c` — HOTFIX01 production apply present — **PASS** |
| Staged index | Empty — **PASS** |
| `origin/mars/canonical-post-recovery` | Local ahead / behind noted — **no pull / no push** |
| Foreign WIP | Preserved (Website Factory / FP-0002 / OCPilot / `.recovery-temp`) — **PASS** |
| Credentials | `local/tokens/n8n-api.env` present (values not printed) — **PASS** |

**Authority / evidence read:** `AGENTS.md`, `.cursorrules`, `OPERATIONAL-INDEX.md`, `safe-workflow-patch-protocol-v1.md`, `n8n-import-safe-generation-rules-v1.md`, `n8n-workflow-json-grammar-v1.md`, HOTFIX02 design + sandbox implementation packs, HOTFIX01 production apply/proposal/diagnostics, design gates/rollback, sandbox diffs/harness/preservation checks.

**=== MARS AGENT GUARDRAILS v1 ===**  
Lane: B · Phase: production proposal · Repo root: `X:\AI MARS` · Volume: AI WS (X:)  
SCOPE LOCK: `projects/metabot-seo-content-agent/` + `local/pc14-fu03-hotfix02-send-branch-production-proposal-2026-07-20/` · Allowed: n8n GET production/sandbox (read-only), sanitized proposal evidence write · Forbidden: production/sandbox PUT/activate, Telegram, OpenRouter, Sheets write, `/run`, git stage/commit/push/pull/clean/reset.

---

## 4. Production Preproposal Baseline

**Method:** `GET_ONLY` via n8n API for `p4mqb4VuPcemIDlC`. Compared to HOTFIX01 after-apply / pre-HOTFIX02 sanitized baseline.

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `p4mqb4VuPcemIDlC` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker` | same | **PASS** |
| active | `true` | `true` | **PASS** |
| node count | `101` | `101` | **PASS** |
| FU03 nodes | `9` | `9` | **PASS** |
| updatedAt | `2026-07-20T11:03:34.279Z` | HOTFIX01 apply timestamp | **PASS** |
| `Run Strict Surface Repair` | enabled | enabled | **PASS** |
| HOTFIX01 restores | intact | intact | **PASS** |
| HOTFIX02 already applied | **false** | false | **PASS** |
| `Format Strict Reject Message` length | `1951` | pre-HOTFIX02 | **PASS** |
| `Parse Mode` length | `405` | pre-HOTFIX02 | **PASS** |
| Reject fan-out | `Take First Item`, `Prepare Memory Row Run` | old order | **PASS** |
| `Send Telegram Run` | `={{ $json.telegram_text_safe }}` | unchanged | **PASS** |
| PC-07 Close Lock | `={{ $('Route Command').first().json.task_id }}` | same | **PASS** |
| TZ HOTFIX01 | structuredClone=0, clonePlain present, version intact | same | **PASS** |
| Non-target drift vs HOTFIX01 after-apply | none | none | **PASS** |
| Credentials | redacted in sanitized export | redacted | **PASS** |

**Drift decision:** no unexpected drift. Production remains HOTFIX01-applied / HOTFIX02-absent — **apply-ready for HOTFIX02 only**.

---

## 5. Sandbox HOTFIX02 Source Verification

**Method:** live GET of `TMhJbxtk6uUPDpEb` + sandbox after evidence.

| Field | Observed | Expected | Result |
|-------|----------|----------|--------|
| ID | `TMhJbxtk6uUPDpEb` | same | **PASS** |
| Name | `SEO Content Agent Beta.v14 - Worker.sandbox-pc14-fu03-hotfix02-send` | same | **PASS** |
| active | `false` | `false` | **PASS** |
| node count | `101` | `101` | **PASS** |
| FU03 nodes | `9` | `9` | **PASS** |
| `Run Strict Surface Repair` | disabled | disabled (sandbox) | **PASS** |
| Reject HOTFIX02 marker | `v1-pc14-fu03-hotfix02-format-strict-reject-plain` | present | **PASS** |
| Parse HOTFIX02 marker | `v1-pc14-fu03-hotfix02-parse-mode-plain` | present | **PASS** |
| Reject length | `2821` | HOTFIX02 | **PASS** |
| Parse length | `768` | HOTFIX02 | **PASS** |
| Fan-out | `Prepare Memory Row Run`, `Take First Item` | memory-first | **PASS** |
| Helper mirror | matches exported patch constants | true | **PASS** |
| Live jsCode vs committed after | match | match | **PASS** |
| HOTFIX01 restores | intact | intact | **PASS** |
| `Send Telegram Run` expr | unchanged | unchanged | **PASS** |
| PC-07 / TZ | intact | intact | **PASS** |
| Harness | 10/10 PASS | 10/10 | **PASS** |

Sandbox remains inactive. Do **not** copy sandbox disabled side-effect states into production. Do **not** disable `Run Strict Surface Repair` on production.

---

## 6. Proposed Production Delta

| Item | Detail |
|------|--------|
| Target | `p4mqb4VuPcemIDlC` |
| Patch nodes | `Format Strict Reject Message`, `Parse Mode` |
| Patch type | `jsCode` replace + one connection reorder |
| Source | sandbox HOTFIX02 after export (`TMhJbxtk6uUPDpEb`) |
| Node delta | **0** |
| Connection changes | **yes** — key `Format Strict Reject Message` only |
| Entire-workflow copy | **forbidden** |

**Connection reorder:**

| Before (production now) | After (proposed) |
|-------------------------|------------------|
| `Take First Item` → `Prepare Memory Row Run` | `Prepare Memory Row Run` → `Take First Item` |

**Preserve on production:** active `true`, id/name/webhook, credentials, Telegram/OpenRouter/Sheets enabled states, `Run Strict Surface Repair` **enabled**, HOTFIX01 restores, PC-07 Close Lock mapping, TZ HOTFIX01, `Send Telegram Run` expression, Status Complete/Final, Intake/Admin untouched.

**Do not modify:** Send Telegram Run expression, Status Complete/Final, restore nodes, repair enabled state, FU03 repair loop bodies (except allowlisted reject formatter), PC-07, TZ, Intake, Admin, credentials, side-effect enabled states.

---

## 7. Target Node / Connection Diff

| Node | Prod length | Sandbox length | Prod HOTFIX02 | Sandbox HOTFIX02 | Would change |
|------|-------------|----------------|---------------|------------------|--------------|
| Format Strict Reject Message | 1951 | 2821 | false | true | **yes** |
| Parse Mode | 405 | 768 | false | true | **yes** |

| Connection | Prod fan-out | Sandbox fan-out | Would change |
|------------|--------------|-----------------|--------------|
| Format Strict Reject Message | Take First Item → Prepare Memory Row Run | Prepare Memory Row Run → Take First Item | **yes** |

Version markers to land on production after apply:

- `v1-pc14-fu03-hotfix02-format-strict-reject-plain`
- `v1-pc14-fu03-hotfix02-parse-mode-plain`

Expected after apply: node count `101 → 101`, FU03 `9`, code targets `2`, connection targets `1`.

---

## 8. Production Apply Plan

Plan only — **not executed** in this task. Full steps in `pc14-fu03-hotfix02-send-branch-production-proposal-apply-plan.json`.

1. GET production raw before apply.  
2. Save rollback: `local/pc14-fu03-hotfix02-send-branch-production-apply-2026-07-20/rollback/worker-before-hotfix02.raw.json`.  
3. Sanitize before export.  
4. GET sandbox HOTFIX02 source.  
5. Extract only the two target `jsCode` values.  
6. Replace only those two `parameters.jsCode` on production copy.  
7. Reorder only `Format Strict Reject Message` fan-out to memory-first.  
8. Preserve id/name/active/webhook/credentials/non-targets/side-effects/PC-07/TZ/HOTFIX01 restores/repair enabled/Send Telegram expr.  
9. Validate structurally (101 / 9 FU03 / node delta 0 / allowlisted-only).  
10. PUT production **only** after automated gates + operator approval.  
11. Re-GET production.  
12. Verify HOTFIX02 markers, memory-first fan-out, HOTFIX01 intact, repair enabled, PC-07/TZ/side-effects/credentials intact.  
13. Offline production-transformed harness HF02 **10/10** (no live side effects / no `/run`).  
14. Do **not** run operator smoke inside the apply task unless separately asked.

---

## 9. Rollback Plan

| Item | Detail |
|------|--------|
| Primary | Re-PUT production from raw before-hotfix02 backup |
| Path | `local/pc14-fu03-hotfix02-send-branch-production-apply-2026-07-20/rollback/worker-before-hotfix02.raw.json` |
| Alternate | Revert exact allowlisted changes: reject jsCode + Parse Mode jsCode + fan-out to Take First Item → Prepare Memory Row Run |
| Notes | Do not copy sandbox disabled side-effects; do not deactivate unless charter says so; do not roll back HOTFIX01/FU03/PC-07/TZ; pending lock cleanup remains separate |

---

## 10. Harness Plan

| Item | Detail |
|------|--------|
| Method | Offline local only — no Telegram / OpenRouter / Sheets / `/run` |
| When | After production transform (apply task), before claiming harness-verified |
| Cases | HF02-H01 … HF02-H10 (reject asterisk/underscore/brackets, long chunking, memory-first, clean-path regression, HOTFIX01 intact, exec3364 fixture, secret scan) |
| Expected | **10/10 PASS** |
| Reference | sandbox harness results under `pc14-fu03-hotfix02-send-branch-sandbox-implementation/2026-07-20/` |

---

## 11. Operator Smoke Plan

**Do not execute now. Do not retry `/run` before production HOTFIX02 apply.**

Bait (same reject-path command family as HOTFIX01 smoke / exec `3364`):

```
/run тестовая проверка PC14-FU03 HOTFIX02 после production apply: короткий SEO-план на 3 пункта для страницы услуги ремонта кофемашин. Обязательно сделай SEO ТЗ с таблицей и укажи причину таблицы. В причине таблицы специально используй формулировку: для удобства восприятия. Не используй слова: аккуратное, удобства, удобно, позволяет, обеспечение, контроль, безопасность, специализированные, надежность, наглядность.
```

**Acceptable:** STRICT QA REJECT diagnostic **sent** (no Telegram 400) + lock closes + memory `blocked_dirty`; **or** repair-clean materials + lock closes + memory `repair_attempted_clean` (or equivalent).

**Not acceptable:** `Send Telegram Run` HTTP 400 entity parse; false complete preface only; pending lock left active; restore-node regression; memory append skipped while send fails; banned markers in public output; raw Strategy JSON dump.

Pending old smoke lock cleanup remains **separate**, operator-approved only.

Full charter: `pc14-fu03-hotfix02-send-branch-production-proposal-smoke-charter.md`.

---

## 12. Risk Matrix

| ID | Risk | Mitigation | Residual |
|----|------|------------|----------|
| R1 | Unexpected non-target drift at apply time | Preflight non-target/target-vs-baseline gates → DRIFT_BLOCKED | low if gates hold |
| R2 | Copying sandbox disabled side-effects / disabling repair | jsCode + one reorder only; keep repair enabled | low |
| R3 | Telegram still 400 despite neutralization (parse_mode default UNKNOWN) | Neutralize `*`/`_`/`` ` ``/`[]`; smoke verifies delivery | medium (SAFE UNKNOWN) |
| R4 | False complete preface UX on reject | Deferred HOTFIX03; smoke still requires materials/diagnostic + lock close | medium (UX) |
| R5 | Apply without offline HF02 harness | Mandatory HF02 10/10 after transform | low |
| R6 | `/run` before hotfix creates another failed send | Charter forbids `/run` until apply | medium (ops) |
| R7 | Sandbox source drift between proposal and apply | Fresh GET at apply; SOURCE_DRIFT_BLOCKED if mismatch | low |

---

## 13. Evidence Files Created

Under `projects/metabot-seo-content-agent/exports/pc14-fu03-hotfix02-send-branch-production-proposal/2026-07-20/`:

- `PC14-FU03-HOTFIX02-SEND-BRANCH-PRODUCTION-PROPOSAL-MANIFEST.md`
- `run-pc14-fu03-hotfix02-production-preproposal.mjs`
- `SEO-Content-Agent-Beta-v14-Worker.production-preproposal-hotfix02.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Worker.sandbox-hotfix02-source.sanitized.json`
- `SEO-Content-Agent-Beta-v14-Worker.production-hotfix02.transformed-preview.sanitized.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-delta.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-target-node-diff.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-connection-diff.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-preflight-gates.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-apply-plan.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-rollback-plan.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-harness-plan.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-smoke-charter.md`
- `pc14-fu03-hotfix02-send-branch-production-proposal-risk-matrix.json`
- `pc14-fu03-hotfix02-send-branch-production-proposal-secret-scan.json`
- code-node-index / side-effect-baseline / structural-validation / transform-preview-meta

Raw local (not for commit): `local/pc14-fu03-hotfix02-send-branch-production-proposal-2026-07-20/`  
(includes `worker-preproposal.raw.json`, `sandbox-hotfix02-source.raw.json`, `production-transform-preview.not-applied.raw.json`, `preproposal-result.json`)

---

## 14. Out-of-Scope Preserved

Foreign WIP from Website Factory / FP-0002 / OCPilot / `.recovery-temp` left untouched. No stage/commit/push/pull. Intake/Admin untouched. Preface gating deferred to `PC14_FU03_HOTFIX03_PREFACE_GATING`. Production and sandbox workflows were **not** mutated.

---

## 15. SAFE UNKNOWN

- Exact n8n Telegram `sendMessage` default when `parse_mode` omitted (entity parse still observed on HOTFIX01 smoke; neutralization is the mitigation).
- Exact Sheets memory row for smoke task_id (not read in this proposal).
- Live Telegram UX after HOTFIX02 — not operator-smoked yet (do not `/run` until apply wave completes).

---

## 16. Final Status

| Field | Value |
|-------|-------|
| **Decision** | `PC14_FU03_HOTFIX02_READY_FOR_PRODUCTION_APPROVAL` |
| **Recommended next** | `PC14_FU03_HOTFIX02_PRODUCTION_PROPOSAL_PERSIST` |
| **After persist** | `PC14_FU03_HOTFIX02_PRODUCTION_APPLY` |
| **Final status** | `COMPLETE — PC14-FU03 HOTFIX02 production proposal ready` |
| **Blockers** | none |
| **Automated gates** | all PASS |
| **Production mutated** | **No** |
| **Sandbox mutated** | **No** |

Awaiting operator review / persist authorization. **Do not** retry Telegram `/run` yet.
