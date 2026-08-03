# PHASE 3D.4 ACCEPTANCE RECEIPT v1

**Date:** 2026-08-03  
**Verdict:** **PHASE 3D.4 COMPLETE — SEMANTICS DEPLOYED, OLYA LIVE CALLBACK PENDING**

---

## Gates

| Gate | Result |
|------|--------|
| Sales-Manager-v2 inactive | PASS |
| Operational.dev + Admin.dev active | PASS |
| AI OFF | PASS |
| New workflows created | **0** |
| No client auto-messages | PASS |
| No credentials in docs | PASS |

---

## Harness

| Suite | Result |
|-------|--------|
| Manager UX / callback local harness (F-MU01–F-MU30) | **30/30 PASS** |
| Parser semantic extensions (v3.2 supplied form) | PASS |
| Admin regression stubs | PASS |

---

## Live / runtime

| Check | Result |
|-------|--------|
| Live n8n patch applied | **ok** |
| CONFIG enrollment (`manager_action_user_ids`) | **ok** |
| Synthetic Olya callback (processed/spam) | **PASS** |
| Operator Admin commands regression | **PASS** |
| Olya live `/start` (human Telegram) | **PENDING** |
| Olya live `/help` (human Telegram) | **PENDING** |
| Olya live callback on real pending card | **PENDING** |

---

## Version bumps

| Component | From | To |
|-----------|------|-----|
| Parser | sm-parser-v3.1 | **sm-parser-v3.2** |
| Message format | sm-msg-v2 | **sm-msg-v2.1** |

---

## Olya enrollment summary

- Identity resolved: hash **E6714550214106BA** (distinct from operator **3FBE21323E22BFC1**).
- Denied `/start` exec **17177** observed pre-enrollment.
- Enrolled in `manager_action_user_ids` **only** — not admin.
- Synthetic acceptance complete; **human Telegram confirmation pending** for `/start`, `/help`, and first live button tap.

---

## Evidence pack

14 documents under `evidence/phase3d4/` + registry `knowledge/WEBSITE-FORM-FORMATS-v1.md` + updated guides/specs + phase report.

---

## Commit / push

Git commit hash: **TBD**  
Git push hash: **TBD**

---

*Related: REPORT-iseo-sales-manager-bot-phase3d4-manager-enrollment-and-form-semantics-v1.md.*


## Live synthetic acceptance (2026-08-03)

- Harness: 30/30 PASS
- Synthetic Admin harness (Olya identity): **13/13 PASS**
- Olya manager /start /help: PASS (synthetic inject)
- Olya admin-command denial: PASS
- Olya processed/spam callbacks on SYNTHETIC_TEST fixtures: PASS
- Admin /config counts: administrators=1, manager-actions=2
- Unauthorized /start + callback: PASS
- Contour restored: Ops+Admin active, Sales-Manager-v2 inactive
- Human live Telegram confirmation by Olya: still requested (operator ask)

