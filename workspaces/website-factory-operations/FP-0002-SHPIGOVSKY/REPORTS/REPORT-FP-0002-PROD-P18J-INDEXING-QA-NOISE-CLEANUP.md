# REPORT — FP-0002 PROD-P18J Indexing Guard QA Noise Cleanup

**Wave:** PROD-P18J  
**Site:** https://shpigovsky.ru/  
**Date:** 2026-08-20  
**Status:** **PASS**

---

## 1. Status

**PASS** — synthetic P18G guard QA is separated from production incident channels; indexing remains OPEN; guard and watchdog active; production deployed `0.3.22-p18j` with source/production parity.

---

## 2. Current State

**P18J CURRENT INDEXING SAFETY STATE VERIFIED**

| Signal | Value |
|--------|-------|
| `blog_public` | 1 |
| Effective indexability | **OPEN** |
| Human authority | OPEN — Olya (`p18g_bootstrap`) |
| P18G guard | **ACTIVE** |
| Watchdog | **ACTIVE** (hourly observation) |
| Core version (post-deploy) | `0.3.22-p18j` |
| Project phase | **PRODUCTION / MAINTENANCE** |

Evidence: `REPORTS/evidence/prod-p18j-indexing-qa-noise/00-summary.json`, `04-post-intake.json`

---

## 3. Four Event Forensics

**ALL FOUR P18G_QA_GUARD_TEST EVENTS ATTRIBUTED**

| Timestamp | ID | Source | Caller | State change | Email |
|-----------|-----|--------|--------|--------------|-------|
| 2026-08-19 20:23:07 | 155 | `p18g_qa_guard_test` | P18G `_p18g_runtime.py` → `wp_eval` | **None** | **No critical alert** |
| 2026-08-19 20:23:54 | 156 | same | P18G QA re-run | **None** | **No** |
| 2026-08-19 20:29:33 | 157 | same | P18G push-wave QA | **None** | **No** |
| 2026-08-19 21:09:12 | 158 | same | P18G push-wave QA | **None** | **No** |

Entry point: `IndexingControl::request_state( false, [ 'source' => 'p18g_qa_guard_test' ] )` from deploy QA harness — **not** cron, watchdog, Admin UI, or WPilot.

Detail: `REPORTS/evidence/prod-p18j-indexing-qa-noise/05-four-event-forensics.md`

---

## 4. Production Safety

**SYNTHETIC GUARD TESTS DID NOT CLOSE PRODUCTION INDEXING**

All four events: guard blocked close; `blog_public` remained 1; robots permissive; effective OPEN before and after.

---

## 5. Scheduler / Cron

**NO SYNTHETIC P18G GUARD TEST REMAINS SCHEDULED IN PRODUCTION**

Only relevant scheduled hook: `fp02_indexing_watchdog_tick` (observe-only). No `p18g_qa_guard_test` in cron.

Detail: `06-cron-scheduler-audit.md`

---

## 6. Email Forensics

**SYNTHETIC QA EMAIL BEHAVIOR VERIFIED**

- Historical four blocked-close rows: **no critical alert attempted** (classification A).
- P18G/P18J intentional mail proof uses **TEST — INDEXING SAFETY ALERT** subject via `send_test_alert()`.

Detail: `08-email-forensics.md`

---

## 7. Alert Policy

**SYNTHETIC QA CANNOT TRIGGER REAL CRITICAL ADMIN ALERTS**

Authorized QA blocked-close → QA evidence sink; no production incident stream; no critical blocked-close email.

**QA SUPPRESSION NEVER HIDES A REAL CLOSED OR INCONSISTENT STATE**

`IndexingAlerts::should_suppress_for_qa_context()` suppresses only when QA is explicitly authorized **and** effective state remains OPEN.

---

## 8. Activity Log

**SYNTHETIC INDEXING QA IS VISUALLY DISTINCT FROM REAL PRODUCTION INCIDENTS**

- New authorized QA: bounded option `fp02_indexing_qa_evidence` only (no repeated «Закрытие индексации заблокировано» rows).
- Historical rows 155–158: presentation normalization → «QA: защита индексации проверена — PASS» (raw data preserved).

**REAL INDEXING INCIDENT LOGGING REMAINS UNCHANGED OR STRONGER**

Unauthorized close without QA authorization still writes `indexing_close_blocked` (proven by spoof test in `03-post-deploy-qa.json`).

---

## 9. Historical Rows

**HISTORICAL ACTIVITY LOG IS NOT DESTRUCTIVELY CLEANED**

Rows 155–158 retained; classified as synthetic P18G QA in evidence and Admin display layer.

---

## 10. Watchdog

**WATCHDOG MONITORS STATE WITHOUT GENERATING SYNTHETIC CLOSE ATTEMPTS**

Post-deploy snapshot: OPEN, no close simulation.

---

## 11. QA Context Security

**QA TEST CONTEXT CANNOT BE SPOOFED FROM PUBLIC REQUESTS**

Requires server-side `FP02_INDEXING_QA_MODE_AUTHORIZED` constant plus validated QA context. Spoof marker without constant → real incident log row (+1 delta in post-deploy test).

---

## 12. QA Matrix

| Case | Result |
|------|--------|
| A — Synthetic authorized close | **PASS** |
| B — Real alert path (TEST subject) | **PASS** |
| C — Watchdog OPEN | **PASS** |
| D — Inconsistent-state QA | **SAFE UNKNOWN** (no mutating prod test) |
| E — Spoof resistance | **PASS** |

Detail: `07-qa-matrix.md`

---

## 13. Dashboard

- Indexing: **OPEN — HUMAN APPROVED**
- Guard: **ACTIVE**
- Watchdog: **ACTIVE · OPEN**
- Incident counter: synthetic QA excluded from new noise (historical four rows display as QA)

---

## 14. Regression

**P18J REGRESSION PASS — INDEXING REMAINS OPEN**

Post-deploy: `parity_ok: true`, `indexing_open_ok: true`, `qa_no_activity_noise: true`.

---

## 15. Olya Safety

**P18J PRESERVES CURRENT EDITORIAL PRODUCTION TRUTH**

Scope limited to indexing guard observability plugin files; no content, SEO, forms, cookie, or menu changes.

---

## 16. Source / Production Parity

**P18J SOURCE / PRODUCTION PARITY PASS**

8 files deployed; hashes matched (`02-deploy-manifest.json`).

Changed runtime files:

- `shpigovsky-core.php` → `0.3.22-p18j`
- `src/Admin/IndexingQaContext.php` (new)
- `src/Admin/IndexingControl.php`
- `src/Admin/IndexingAlerts.php`
- `src/Admin/ActivityLog.php`
- `src/Admin/SystemDashboard.php`

---

## 17. WP Forge Knowledge

Added to anti-pattern registry and indexing standard:

- **INDEX-008** — Synthetic guard tests indistinguishable from real incidents
- **INDEX-009** — QA suppression hides real CLOSED state
- **INDEX-010** — Watchdog generates synthetic close requests
- **OBSERVABILITY-001** — Synthetic QA pollutes operator channels
- **OBSERVABILITY-002** — Destructive audit cleanup for noisy rows

---

## 18. Git

- Worktree: `X:\AI MARS\worktrees\fp-0002-p18j`
- Branch: `fp-0002/prod-p18j-indexing-qa-noise`
- Commits: `a17a4231` (FP-0002 P18J), `d50ae4c0` (WP Forge)
- Remote HEAD: `d50ae4c0` on `origin/mars/canonical-post-recovery`
- Dirty main: **untouched**
- Secret scan: evidence contains no credentials; recipient counts only

---

## 19. Current Project State

**PRODUCTION / MAINTENANCE**

---

## 20. Remaining Work

Non-blocking operator items unchanged (GSC/Yandex sitemap submission, legal sign-off, optional lead retention). CASE D inconsistent-state QA harness — optional future bounded wave.

---

## 21. Acceptance

**FP-0002 P18J COMPLETE** — THE FOUR INDEXING-GUARD EVENTS VISIBLE IN THE PRODUCTION ACTIVITY LOG WERE FORENSICALLY CLASSIFIED — SYNTHETIC QA IS NOW SEPARATED FROM REAL PRODUCTION INCIDENTS — SYNTHETIC GUARD TESTS CANNOT TRIGGER REAL CRITICAL ADMIN ALERTS — REAL UNAUTHORIZED CLOSE AND REAL GLOBAL INDEXABILITY INCIDENTS REMAIN FULLY LOGGED AND ALERTED — THE WATCHDOG MONITORS STATE WITHOUT GENERATING SYNTHETIC CLOSE REQUESTS — QA SUPPRESSION CANNOT BE PUBLICLY SPOOFED AND CANNOT HIDE A REAL CLOSED/INCONSISTENT STATE — HISTORICAL AUDIT ROWS WERE NOT DESTRUCTIVELY REMOVED — INDEXING REMAINS OPEN AND HUMAN-OWNED — P18G GUARD AND WATCHDOG REMAIN ACTIVE — CURRENT EDITORIAL TRUTH IS PRESERVED — SOURCE/PRODUCTION PARITY PASSES — CANONICAL REMOTE IS UPDATED — FP-0002 REMAINS IN NORMAL PRODUCTION / MAINTENANCE

---

*Evidence pack: `REPORTS/evidence/prod-p18j-indexing-qa-noise/`*
