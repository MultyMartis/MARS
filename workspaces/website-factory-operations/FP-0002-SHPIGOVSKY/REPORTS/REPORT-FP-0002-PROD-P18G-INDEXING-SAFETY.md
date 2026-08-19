# REPORT — FP-0002 PROD-P18G Indexing Safety Guard + Critical Admin Alerts

**Date:** 2026-08-20  
**Status:** **PASS**  
**Core deployed:** `0.3.17-p18g`  
**Evidence:** `REPORTS/evidence/prod-p18g-indexing-safety/`

---

## 1. Status

**PASS** — guard live, production indexing remains OPEN, 8/8 source↔production match.

---

## 2. Current Truth

**P18G CURRENT INDEXABILITY TRUTH VERIFIED**

| Surface | Value |
|---------|-------|
| `blog_public` | **1** |
| Effective state | **OPEN** |
| Physical `robots.txt` | Present at docroot; **no global `Disallow: /`** |
| HTTP `/robots.txt` | 200 |
| Homepage meta | `max-image-preview:large` — **no sitewide noindex** |
| X-Robots-Tag | None (sampled) |
| Human authority | OPEN · Olya (bootstrapped from confirmed operator state) |

---

## 3. Incident Root Cause

**2026-08-19 13:13:25 INDEXING CLOSURE ROOT CAUSE PROVEN**

**Classification A** — `IndexingControl` mutation via P18D-FU01 closeout script.

Chain: fresh intake `blog_public=1` (admin opened 11:16) → FU01 `close_indexing()` → `IndexingControl::set_site_indexability(false)` via wp_eval → Activity Log id **135** @ 13:13:25, user_id **0** → UI «Система». Human reopen id **139** @ 19:18:26 (admin).

Detail: `REPORTS/evidence/prod-p18g-indexing-safety/INCIDENT-2026-08-19-131325.md`

---

## 4. Robots Ownership

**ALL GLOBAL ROBOTS OWNERS IDENTIFIED**

| Owner | Role |
|-------|------|
| Physical `/robots.txt` | **Primary** — host-managed multi-agent rules (Beget-style) |
| WordPress virtual robots | Fallback if physical absent |
| IndexingControl | Sync only for known simple open/closed templates or clearing global disallow |
| Theme / SEO plugin | Page-level rules only |
| P18D-FU01 script | Historical — wrote simple closed robots during FU01 (superseded by human reopen) |

**ROBOTS.TXT PRECEDENCE AND SINGLE OWNER PROVEN**

Physical file serves HTTP 200. No global `Disallow: /` while OPEN. IndexingControl will not destroy complex host robots on OPEN (P18G sync safety).

---

## 5. Mutation Paths

**ALL KNOWN INDEXING MUTATION PATHS INVENTORIED**

| Path | P18G |
|------|------|
| Admin IndexingControl POST | Allowed with human confirm |
| `IndexingControl::request_state()` | Guarded |
| `IndexingControl::set_site_indexability()` | Close blocked without auth |
| Direct `update_option('blog_public',0)` | Blocked by filter |
| P18D-FU01 `close_indexing()` | **Would block now** |
| P18B QA scripts | Historical — must not re-run close on production |
| WP core Reading settings | Blocked on close via filter |
| WP-CLI `option update blog_public 0` | Blocked via filter |

---

## 6. Dangerous Legacy Logic

**NO TECHNICAL CLOSEOUT PATH CAN SILENTLY RESTORE CLOSED**

FU01 closeout logic neutralized by server-side guard. Current docs updated — no remaining charter tells waves to re-close.

---

## 7. Human Authority

**HUMAN-OPEN INDEXING STATE OVERRIDES HISTORICAL CLOSED BASELINES**

Option `fp02_indexing_human_authority` records decision OPEN, actor, timestamp, source.

---

## 8. Effective State

**INDEXABILITY STATE IS COMPUTED FROM MULTIPLE REAL SURFACES**

`IndexingState::snapshot()` → OPEN | CLOSED | INCONSISTENT from blog_public + robots global disallow + global meta.

---

## 9. Guard

**NON-HUMAN OPEN → CLOSED MUTATION IS BLOCKED BY DEFAULT**

QA: `guard_held_open: true` in `03-post-deploy-qa.json`.

---

## 10. Robots Safety

**ROBOTS GLOBAL BLOCK CANNOT DRIFT FROM HUMAN INDEXING STATE**

Watchdog alerts on human OPEN + effective != OPEN. Complex host robots preserved on OPEN.

---

## 11. Current Open State

**CURRENT HUMAN-APPROVED OPEN STATE IS CONSISTENT ACROSS GLOBAL SURFACES**

No reconcile mutation required.

---

## 12. Administrator Alerts

**INDEXING ALERT RECIPIENTS ARE WP ADMINISTRATORS, NOT FORM LEAD RECIPIENTS**

4 administrators resolved (redacted in evidence).

**GLOBAL INDEXING BLOCK ALERTS DO NOT DEPEND ONLY ON BLOG_PUBLIC TRANSITION**

Alerts on inconsistency and human-open-but-blocked paths.

---

## 13. Alert QA

**WP ADMIN ALERT RECIPIENT RESOLUTION PASS** — count 4.

**ALERT PIPELINE TESTED WITHOUT CLOSING PRODUCTION INDEXING** — `TEST — INDEXING SAFETY ALERT` sent (`test_alert.sent: true`).

---

## 14. Watchdog

**INDEXING WATCHDOG ALERTS BUT DOES NOT FIGHT HUMAN STATE AUTOMATICALLY**

Hourly cron scheduled; first check OPEN.

---

## 15. Dashboard

Shows effective OPEN, human decision, robots owner, watchdog line.

---

## 16. Activity Log

New actions: `indexing_close_blocked`, `indexing_inconsistency_detected`, `indexing_alert_sent`, `indexing_recovered`. Source suffix on system events. Historical «Система» = user_id 0 programmatic calls (proven FU01).

---

## 17. Documentation

**CURRENT DOCUMENTATION NO LONGER TELLS FUTURE WAVES TO RE-CLOSE INDEXING**

Updated: PROJECT-STATUS, OPEN-ITEMS-P18G, P18 runbook indexing row, P18G baseline, FW-S-32 §6, INDEX-001…007.

---

## 18. Global vs Page-Level

**GLOBAL INDEXING SAFETY DOES NOT ERASE VALID PAGE-LEVEL SEO RULES**

Host robots retains per-path Disallow (search, legal pages, etc.).

---

## 19. Privacy Regression

P18E intact — cookie consent, Metrika gating, form goal gating unchanged (pre-intake dashboard meta confirmed).

---

## 20. Olya Safety

**OLYA CURRENT EDITORIAL STATE PRESERVED THROUGH P18G**

Plugin-only deploy; no editorial DB writes except human-authority bootstrap metadata.

---

## 21. QA

**P18G QA NEVER CLOSES CURRENT PRODUCTION INDEXING**

Post-deploy `blog_public=1`, effective OPEN.

---

## 22. Parity

**CODE PARITY PASS / HUMAN INDEXING STATE PRESERVED**

8/8 files MATCH.

---

## 23. WP Forge Knowledge

INDEX-001…INDEX-007 registered. Operator-owned indexability rule in FW-S-32 §6.

---

## 24. Git

Two commits (FP-0002 + WP Forge). Secret scan: no credentials in committed artifacts. Dirty main foreign WIP untouched.

---

## 25. Current Production State

**INDEXING OPEN — HUMAN APPROVED**

---

## 26. Remaining Work

- Sitemap submissions  
- Final crawl  
- Final Cookie Policy operator review  

---

## 27. Acceptance

**FP-0002 P18G COMPLETE** per charter acceptance block.
