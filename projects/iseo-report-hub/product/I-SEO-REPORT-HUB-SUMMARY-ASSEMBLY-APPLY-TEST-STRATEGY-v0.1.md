# I-SEO Report Hub — Summary Assembly Apply Test Strategy v0.1

**Status:** CHARTER / TEST STRATEGY — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01

Report id **1** is finalized and issued. Implementation 01 must not damage it.

---

## 1. Live DB snapshot (read-only probe, this charter)

Probed 2026-08-17 against local `iseo_report_hub_dev` (SELECT only):

| Item | Value |
|------|--------|
| `monthly_report_contents` | **2** |
| id 1 | `finalized`; blocks **6** all `reviewed`; work entries **7** |
| id 5 | `draft`; blocks **0**; work entries **0**; period id 3 |
| `report_exports` | **4** |
| `report_export_shares` | **7** (active **1**, revoked **6**) |
| `report_snapshots` | **1** (monthly 1, active) |

**No** non-finalized monthly report currently has the three auto blocks.

Report **5** is **not** a safe apply target: apply Implementation 01 does not INSERT missing shells, and id 5 has no entries to assemble.

Do **not** seed report 5 in Apply Implementation 01 unless a **separate explicit fixture charter** is issued.

---

## 2. Options considered

| Option | Meaning | Verdict |
|--------|---------|---------|
| **A** Disabled apply only | POST route exists but smoke never writes (report 1 blocked; no other target) | **Fallback** |
| **B** Seed a new non-finalized report + blocks + entries | Extra DB mutation / cleanup | **Not** in Implementation 01 |
| **C** Temporarily reopen report 1 and rollback | Desync risk vs PDF/share; too risky | **Forbidden** |
| **D** Use existing non-finalized report with blocks and no exports/shares | Best write-proof | **Preferred if discovered at impl time** |

---

## 3. Locked recommendation

**Implementation 01 = discovery then D-or-A.**

### 3.1 Preferred write-proof path (Option D)

At the start of Implementation 01, SELECT:

- monthly `status NOT IN ('finalized','archived')`
- has existing rows for at least one auto key (`work_completed` / `next_month_plan` / `risks_and_blockers`)
- **no** `report_exports` tied to snapshots of that monthly
- **no** `report_export_shares` (active or revoked) for those exports
- preferably has some work entries so the draft is non-empty

If found: dump DB, POST apply **one** selected block only, capture old/new body in STORAGE evidence, assert other blocks unchanged, assert exports/shares/PDF on report 1 unchanged.

### 3.2 Fallback (Option A) — **expected on current DB**

If no such report exists (current state):

1. Still implement GET UI disabled state + POST handler that refuses finalized.
2. Smoke report 1: GET preview 200; POST apply **refuses** (4xx/redirect+flash); **zero** `report_blocks` mutation on id 1.
3. **Do not** POST a successful write.
4. **Do not** reopen id 1.
5. **Do not** INSERT blocks on id 5.
6. Closeout verdict: `PASS_WITH_LIMITED_WRITE_PROOF` (or charter-equivalent wording in the implementation report).

Acceptance remains **clear**: disabled apply on finalized report 1 is the proven safety property; write-path unit/logic can be reviewed in code; live UPDATE is **not** proven until a safe fixture exists.

---

## 4. Forbidden test path

- Reopen report 1 “just to see apply”.
- Apply then restore from backup as the **planned** happy path (backup is emergency rollback only).
- Mutate export 4 / share `test-first-link`.
- Generate PDF.

---

## 5. Evidence requirements (Implementation 01)

STORAGE (not git), suggested folder:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\summary-assembly-apply-implementation-01\`

Must include:

- before/after counts: entries_r1, blocks_r1, exports, shares active/revoked, checksum prefix export 4
- HTTP results for GET preview and POST refuse on report 1
- if Option D ran: old body, new body, target monthly id, selected key
- dump path / filename if a dump was taken (dump itself not committed)

No share tokens, no `.env`, no passwords.

---

## 6. Cleanup

| Path | Cleanup |
|------|---------|
| Option A only | None (no writes) |
| Option D | Keep the fixture report unless the impl charter says restore that one block from captured old body |
| Option B (future fixture charter) | Document keep vs delete; no `git clean`; no recursive delete of runtime |

---

## 7. Expected counts after Implementation 01 (fallback A)

Unchanged vs this charter probe, unless an unrelated operator change happens:

- entries_r1 **7**
- blocks_r1 **6**
- exports **4**
- shares **7** / active **1** / revoked **6**
- export 4 checksum prefix `a8c4d61c6216e8d70b19`
- monthly id 1 still `finalized`
- monthly id 5 still `draft` with **0** blocks (do not “fix” it here)

---

## 8. SAFE UNKNOWN

- Origin/purpose of monthly id **5** (not documented in OPERATIONAL-INDEX as a second monthly; treat as foreign local smoke residue — **do not delete**).  
- Whether the operator will later authorize a dedicated apply-fixture seed wave to upgrade from limited write proof.
