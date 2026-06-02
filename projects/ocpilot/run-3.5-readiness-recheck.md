# OCPilot Run 3.5 — Baseline Readiness Recheck

**Date:** 2026-05-30  
**Checklist:** [baseline-readiness-checklist.md](../baseline-readiness-checklist.md)  
**Promotion:** Run 3.5 — files populated from canonical ZIPs

---

## ocstore-3038-rs2

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | Passport exists | **PASS** | `passports/ocstore-3038-rs2-passport-v1.md` |
| 2 | Files exist (sanitized vendor tree) | **PASS** | `files/` — 4055 files; OpenCart root at `files/admin`, `files/catalog`, … |
| 3 | Manifest exists | **PASS** | `manifest/baseline-manifest-v1.md` |
| 4 | DB metadata (optional) | **PASS** | `database/database-metadata-v1.md` |
| 5 | Comparison notes (optional) | **PARTIAL** | Cross-version note in `comparison-notes/3038-vs-3039-structured-review-v1.md`; baseline-local `comparison-notes/` still placeholder |

### Status: **READY**

**Reason:** All three **required** checklist items pass after Run 3.5 promotion. Sanitization review PASS. Optional DB metadata present. Optional per-baseline comparison notes not yet populated in `baselines/ocstore-3038-rs2/comparison-notes/` — does not block file-level comparison.

---

## ocstore-3039-rs1

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | Passport exists | **PASS** | `passports/ocstore-3039-rs1-passport-v1.md` |
| 2 | Files exist | **PASS** | `files/` — 3553 files; correct OpenCart root layout |
| 3 | Manifest exists | **PASS** | `manifest/baseline-manifest-v1.md` |
| 4 | DB metadata (optional) | **PASS** | `database/database-metadata-v1.md` |
| 5 | Comparison notes (optional) | **PARTIAL** | Shared structured review in `projects/ocpilot/comparison-notes/`; local folder placeholder |

### Status: **READY**

**Reason:** Required gate satisfied. Same optional gap as 3038-rs2 for baseline-local `comparison-notes/`.

---

## Readiness summary block

```
Baseline readiness: READY
Path: baselines/ocstore-3038-rs2/
Passport: yes
Files: yes
Manifest: yes
DB metadata: yes (optional)
Comparison notes: partial (optional)
Blockers: none for file-level comparison
```

```
Baseline readiness: READY
Path: baselines/ocstore-3039-rs1/
Passport: yes
Files: yes
Manifest: yes
DB metadata: yes (optional)
Comparison notes: partial (optional)
Blockers: none for file-level comparison
```

---

## Post-promotion passport alignment

Passports updated in Run 3.5 to reflect `Files Present = yes` and `Database Metadata Present = yes`.

---

## SAFE UNKNOWN

- Operator sign-off on sanitization — documented review only; formal HITL approval not recorded in repo.
