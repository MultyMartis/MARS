# SITE-002 MVP Intake

**Status:** DOCUMENTATION INTAKE ASSUMPTIONS / PHASE 0A  
**Site:** SITE-002 · ЗПМ · `bzpm.ru`  
**Production mutation by this pack:** none  
**Live sitemap refetch during Phase 0A:** none

---

## 1. Purpose

Capture SITE-002-specific evidence and assumptions for the shared Client Ops Reporting Bridge contract. Generic envelope semantics live in [REPORT-CONTRACT-V1.md](REPORT-CONTRACT-V1.md); this file holds site facts.

---

## 2. Current known monitor / artifact model

| Item | Evidence |
|------|----------|
| Monitor tool | `projects/ocpilot/sites/site-002/tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py` |
| Runner | `projects/ocpilot/sites/site-002/tools/site-002-post-1c-monitor-runner.ps1` |
| Runbook | `projects/ocpilot/sites/site-002/runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md` |
| Hardening report | `projects/ocpilot/sites/site-002/reports/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md` |
| Hardening baseline note | `projects/ocpilot/sites/site-002/baselines/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md` |
| Tools contract notes | `projects/ocpilot/sites/site-002/tools/README.md` (classification + artifact list) |
| Scheduled output root (Storage) | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\scheduled-monitors\post-1c\` |

Monitor is **read-only** relative to SITE-002 production website (no FTP/admin/DB mutation by design in runbook).

Hardened per-run artifacts include: `added-urls.*`, `removed-urls.*`, `sitemap-baseline.xml`, `sitemap-current.xml`, `hygiene-flags.*`, `monitor-classification.*`, `changed-summary.*`, UTF-8 `run.log` / `run.stderr.log`, `run-summary` with duration/classification/next_action.

Source classification vocabulary includes: `NO_ACTION_REQUIRED` \| `HYGIENE_REVIEW_REQUIRED` \| `ONBOARDING_REQUIRED` \| `FAILURE_REVIEW_REQUIRED`.

---

## 3. Accepted baseline checkpoint wording

| Field | Value |
|-------|-------|
| Accepted checkpoint | `SITE-002-STABLE-PROD-POST-1C-MONITOR-BASELINE-1737-04` |
| Accepted baseline count | **1737** |
| Operation evidence | `SITE-002-MONITOR-BASELINE-REFRESH-04` (OCPilot run 4.288) |
| Storage evidence (prose path) | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-MONITOR-BASELINE-REFRESH-04\baseline-after\stable-checkpoint.md` |

**Wording rules:**

- 1737 is an **accepted baseline checkpoint count**.
- 1737 must **not** be described as necessarily current live sitemap count.
- Forbidden: `Sitemap: 1737` as current-live shorthand.
- Required pattern:

```text
Baseline: 1737
Current observed: 1817
Delta: +80 / -0
```

---

## 4. Latest inspected current observed count

| Field | Value |
|-------|-------|
| Scheduled run id | `2026-07-23_12-30-03` |
| Current observed count | **1817** (`changed-summary.json` → `current_url_count`) |
| Baseline count in that run | **1737** (`baseline_url_count`) |
| Added / removed | **80 / 0** |
| Live sitemap re-fetched in Phase 0A / intake docs task | **No** |

Do not claim live current site state beyond this accepted evidence window.

---

## 5. Artifact conflict (latest inspected)

Run: `.../scheduled-monitors/post-1c/2026-07-23_12-30-03`

| Artifact | Fact |
|----------|------|
| `monitor-classification.json` | `ONBOARDING_REQUIRED` |
| `run.log` | contains `ONBOARDING_REQUIRED` (debug) |
| `run-summary.json` | `classification: NO_ACTION_REQUIRED` |
| Same `run-summary.json` metrics | `added_count: 80`, `onboarding_needs_count: 4` |
| `changed-summary.json` | baseline 1737, current 1817, added 80, removed 0; `CATEGORY_PLP: 4` among added page types |

Normalization implication: see [ARTIFACT-AUTHORITY-AND-PRECEDENCE.md](ARTIFACT-AUTHORITY-AND-PRECEDENCE.md) — fail closed to BLOCKED / `SOURCE_ARTIFACT_CONFLICT` when trustworthy reconciliation is impossible; `run-summary.json.classification` is not sole authority.

---

## 6. Required source files for future exporter (SITE-002 MVP)

Primary:

1. `monitor-classification.json`
2. `changed-summary.json`
3. `run-summary.json`

Evidence/debug:

4. `run.log` (and stderr if present)

Companions for completeness (hardening contract): added/removed URL artifacts, hygiene flags, sitemap snapshots.

**Envelope must not include absolute paths** to these files.

---

## 7. Assumptions

- Preferred MVP intake: scheduled monitor folder → separate future read-only exporter → sanitized atomic JSON → future n8n.
- Alternative if n8n cannot read Storage: authenticated webhook POST from local exporter.
- Phase 1 routing: internal-only until separate approval.
- SITE-002 is the first MVP site evidence; multi-client templates are later phases.

---

## 8. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Whether n8n host can read `X:\AI MARS STORAGE` | SAFE UNKNOWN (operator blocker) |
| Root cause of `run-summary.json` vs `monitor-classification.json` mismatch | SAFE UNKNOWN (monitor bug vs merge logic — not diagnosed in Phase 0A) |
| Exact live sitemap count at report time after 2026-07-23_12-30-03 | SAFE UNKNOWN (no refetch) |
| Dedicated vs existing Telegram bot for Client Ops | SAFE UNKNOWN |
| Hub Gateway readiness to consume envelope | SAFE UNKNOWN / planned only |
| Whether Git authority worktree and runtime-checkout SHAs match for monitor script | SAFE UNKNOWN from this pack alone (paths observed in run metadata; not verified here) |

---

## 9. Future exporter responsibilities (not implemented)

- Read scheduled artifacts read-only
- Validate completeness/freshness
- Apply precedence and severity rules
- Emit sanitized `mars.client_ops.report` v1
- Never write production site; never refresh baseline; never trigger 1C import
- Never embed secrets or absolute paths

---

## 10. Preservation rule

Phase 0A and future bridge work must preserve unless separately chartered:

- SITE-002 monitor code behavior (no drive-by fixes in bridge tasks)
- Monitor scheduler registration
- Baseline `SITE-002-STABLE-PROD-POST-1C-MONITOR-BASELINE-1737-04` contents

**Note:** Some SITE-002 tool files are dirty foreign WIP in the Active Brain worktree; Phase 0A must not modify them.
