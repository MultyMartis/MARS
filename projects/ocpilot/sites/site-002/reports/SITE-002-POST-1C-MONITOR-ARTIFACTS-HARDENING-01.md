# REPORT — SITE-002 Post-1C Monitor Artifacts Hardening

**Operation:** `SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01`  
**OCPilot run:** 4.228  
**Date:** 2026-07-08  
**Production checkpoint (unchanged):** `SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01`  
**Mode:** Local/repo tooling hardening — **no Production mutation**

---

## 1. Scope

Controlled local implementation to harden SITE-002 post-1C scheduled monitor artifacts after Run 4.227 hygiene review. Goals: machine-readable added/removed URL lists, sitemap snapshots, UTF-8 logs, real duration, context-aware garbage markers, operator classification with `next_action`.

**Not in scope:** catalog changes, production uploads, 1C import, Task Scheduler registration changes.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `b9375afe701357149b6ad05fc5c2e22d6f246caf` |
| Staged before task | **empty** |
| Foreign WIP | Present — **not staged** |

---

## 3. Source discovery

| File | Role |
|------|------|
| `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` | Main read-only monitor |
| `site-002-post-1c-monitor-runner.ps1` | Scheduled/local runner |
| `install-site-002-post-1c-monitor-task.ps1` | Task installer (read-only review) |
| Scheduled output | `scheduled-monitors/post-1c/<timestamp>/` |

Run 4.227 scheduled folder `2026-07-08_12-30-02` had only `run-summary.json` / `.md` — deployment artifacts lived under `deployments/SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-02/`.

---

## 4. Current behavior baseline

From Run 4.227 scheduled artifacts:

- Added URLs **not** saved in scheduled folder
- Sitemap snapshots **not** in scheduled folder
- `duration_seconds` **absent** from run-summary (wall time ~65s from timestamps)
- **31** garbage false positives (`demo` in `/assets/img/demo/`, «Пример эксплуатации»)
- `run.log` not preserved in scheduled folder (encoding SAFE UNKNOWN)

---

## 5. Implementation design

See Storage `manifests/implementation-design.md`. Monitor accepts `--scheduled-run-dir`; runner passes timestamped folder. Strict garbage scan replaces loose `demo`/`пример` full-page markers.

**Import wrapper `Duration: 0 seconds`:** not owned by monitor — separate future charter if operator wants (e.g. `SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`).

---

## 6. Patch summary

| File | Change |
|------|--------|
| `site-002-prod-post-1c-catalog-onboarding-monitor-02.py` | Artifact export, classification, strict markers, duration, fixtures |
| `site-002-post-1c-monitor-runner.ps1` | UTF-8 process I/O, duration merge, `--scheduled-run-dir` |
| `site-002-post-1c-garbage-marker-fixture-test.py` | **new** fixture harness |
| `tools/README.md` | Contract + classification docs |

---

## 7. Local test run after patch

Read-only monitor with `--scheduled-run-dir` → `test-runs/after/2026-07-08-test/`:

| Check | Result |
|-------|--------|
| `run-summary.json` + `.md` | **yes** |
| `added-urls.csv/json/md` | **yes** (31 URLs) |
| `removed-urls.csv/json/md` | **yes** (0 URLs) |
| `sitemap-current.xml` | **yes** (1408 URLs) |
| `sitemap-baseline.xml` | **yes** (1377 URLs) |
| `changed-summary` | **yes** |
| `hygiene-flags` | **yes** (0 flags) |
| `monitor-classification` | **yes** |
| `duration_seconds` | **54.855** |
| `duration_human` | **55 seconds** |
| `classification` | `HYGIENE_REVIEW_REQUIRED` |
| `strict_garbage_hits_count` | **0** (was 31 false positives) |
| `false_positive_suppressed_count` | **31** |

---

## 8. Artifact output contract

Each scheduled run folder now includes at minimum the artifacts listed in `manifests/implementation-design.md`. Operator should open `run-summary.md` then `monitor-classification.md` for next steps.

---

## 9. Garbage marker fixture regression

7/7 fixtures **PASS**:

- `/assets/img/demo/assum_logo.png` — no hit
- «Пример эксплуатации» link — no hit
- `НЕ БРАТЬ`, `тестовый товар`, `ne-brat`, `dummy product` — hit

---

## 10. Live read-only smoke

| URL | HTTP | Notes |
|-----|------|-------|
| `/sitemap.xml` | 200 | loc_count **1408** |
| `/robots.txt` | 200 | OK |
| `/llms.txt` | 200 | 0 **БЗПМ** |
| `/` | 200 | OK |
| `/katalog` | 200 | OK |

---

## 11. Scheduled task impact review

**Classification A** — installer points to repo runner `site-002-post-1c-monitor-runner.ps1` with `WorkingDirectory X:\AI MARS`. **No Task Scheduler registration change required.** Next enabled scheduled run uses hardened tooling automatically.

---

## 12. Production mutation summary

| Category | Count |
|----------|------:|
| Remote uploads | 0 |
| Remote overwrites | 0 |
| Remote deletes | 0 |
| FTP operations | 0 |
| Admin saves | 0 |
| DB direct operations | 0 |
| Mail sends | 0 |
| Form submits | 0 |
| Product/category/PDP changes | 0 |
| JS/CSS production changes | 0 |
| Sitemap/robots/llms changes | 0 |
| Cron/import runs | 0 |
| Windows Task Scheduler registration changes | 0 |
| public БЗПМ introduced | no |

---

## 13. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01\`

---

## 14. Authority updates

- OCPilot Run **4.228** registered
- Baseline: `SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01`
- Production checkpoint unchanged

---

## 15. Git status

Selective commit of scoped repo paths only (no Storage, no foreign WIP).

---

## 16. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Run 4.227 `run.log` encoding | SAFE UNKNOWN — file not in scheduled folder |
| 1C import TXT `Duration: 0 seconds` | Out of scope — not monitor-owned |
| Live Task Scheduler state | Not inspected live — inferred from installer script (Category A) |

---

## 17. Final verdict

**SITE-002 POST-1C MONITOR ARTIFACTS HARDENING COMPLETE — TOOLING READY FOR NEXT SCHEDULED RUN**

---

## 18. Next task recommendation

1. **Optional:** After next daily 1C import + scheduled monitor — operator spot-check new scheduled folder artifact contract.
2. **Optional:** `SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01` if import TXT duration field should be fixed (separate from monitor).
3. **Not required:** `SITE-002-POST-1C-MONITOR-SCHEDULER-UPDATE-01` — scheduler already uses repo runner.

---

*Tools:* [site-002-prod-post-1c-catalog-onboarding-monitor-02.py](../tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py) · [site-002-post-1c-monitor-runner.ps1](../tools/site-002-post-1c-monitor-runner.ps1) · [site-002-post-1c-garbage-marker-fixture-test.py](../tools/site-002-post-1c-garbage-marker-fixture-test.py)
