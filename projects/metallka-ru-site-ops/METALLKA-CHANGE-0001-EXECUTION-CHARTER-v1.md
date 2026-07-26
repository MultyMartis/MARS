# METALLKA — CHANGE 0001 Execution Charter v1

**Programme:** METALLKA-RU-SITE-OPS  
**Change ID:** CHANGE-0001  
**Linked request:** [METALLKA-CHANGE-REQUEST-0001-ABOUT-TEXT-v1.md](METALLKA-CHANGE-REQUEST-0001-ABOUT-TEXT-v1.md)  
**Status:** **COMPLETE — EXECUTED AND PRODUCTION VALIDATED**  
**Date prepared:** 2026-07-26  
**Date first execution attempted:** 2026-07-26 — **BLOCKED** (WP Admin auth)  
**Date R1 execution completed:** 2026-07-26  

```text
State: AUTHORIZED by exact approval string
First attempt: BLOCKED before first Update (invalid password) — mutations 0
Operator credential correction + manual login confirmation
R1: authenticated; one authorized content mutation; production validated
```

---

## 1. Approval gate

### Required approval string (exact)

```text
APPROVE METALLKA CHANGE 0001 — ABOUT PAGE TEXT EDIT
```

**Status:** **RECEIVED** and **REMAINS VALID** for R1. Backup posture: operator **CONFIRMED READY**.

### Authorized scope (only)

| Authorized | Scope |
|------------|-------|
| One bounded content edit | Page **ID 52** only |
| Target block | Mapped non-global **`vc_column_text`** on `/about/` |
| Content | Exact operator-supplied text change only |
| Method | Normal **WP Admin / WPBakery** edit + Update |
| Contingency | Rollback via WP Admin if validation fails |

### Not authorized (compliance)

No other pages; no filesystem/SSH/FTP/DB/WPilot; no plugin/theme/core updates; no cache purge; no header/footer/menus/The7 globals; no title/slug/template/layout changes.

---

## 2. Preconditions — R1 outcome

| # | Precondition | R1 |
|---|--------------|----|
| 1 | Change request allows execution | **YES** |
| 2 | Exact approval string | **YES** |
| 3 | Backup posture adequate | **YES** (operator) |
| 4 | Page-level before snapshot | **YES** (authenticated) |
| 5 | Live ID/URL/ownership re-check | **YES** |
| 6 | No concurrent editor conflict | **YES** (not evidenced) |
| 7 | No layout/CSS/template required | **YES** |
| 8 | WP Admin credentials authenticate | **YES** (after operator correction) |

---

## 3. Authoring surface (canonical)

```text
WordPress Admin → page 52 → WPBakery / content → edit only the mapped vc_column_text → Update
```

---

## 4. Exact mutation (authorized content)

OLD:

```text
«МЕТАЛЛКА» — это надежный партнер в области металлообработки и ремонта узлов спецтехники.
```

NEW:

```text
Компания «МЕТАЛЛКА» — это надежный партнер в области металлообработки и ремонта узлов спецтехники.
```

---

## 5. Execution record

### 5.1 First attempt (Phase 3B)

| Item | Result |
|------|--------|
| WP Admin login | **FAILED** |
| Update saves | **0** |
| Rollback | **NO** |
| REPORT | [reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-CHANGE-0001-PRODUCTION-EXECUTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-CHANGE-0001-PRODUCTION-EXECUTION.md) |

### 5.2 Retry (Phase 3B-R1)

| Item | Result |
|------|--------|
| WP Admin login | **SUCCESS** |
| Effective OLD→NEW saves | **1** |
| Pages mutated | **1** |
| Rollback required for success | **NO** |
| Rollback attempted (automation flake) | YES — **did not persist** |
| Final production state | Authorized **NEW** |
| Evidence | [METALLKA-CHANGE-0001-EXECUTION-EVIDENCE-v1.md](METALLKA-CHANGE-0001-EXECUTION-EVIDENCE-v1.md) |
| REPORT | [reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-R1-CHANGE-0001-PRODUCTION-EXECUTION.md](reports/REPORT-METALLKA-SITE-OPS-PHASE-3B-R1-CHANGE-0001-PRODUCTION-EXECUTION.md) |

---

## 6. Explicit claims / non-claims

**Claimed:** CHANGE 0001 production-validated; bounded WP Admin / WPBakery page-local text write workflow for this change class is **PROVEN**.

**Not claimed:** filesystem write, SSH/FTP mutation, DB mutation, The7 globals, forms, header/footer, plugin/theme updates, cache purge, WPilot install/REST/writes.

---

*CHANGE-0001 Execution Charter v1 · COMPLETE — EXECUTED AND PRODUCTION VALIDATED.*
