# Known Open Items v1

**Freeze:** ORCA Route Family Freeze v1 · 2026-05-28  
**Purpose:** Explicit register of **not-done** work — prevents false «family launched» claims

---

## Launch and approvals

| ID | Item | Status | Owner |
|----|------|--------|-------|
| L1 | `approved_for_factory` — all routes | Open (zakaz **false**; others pending human) | Operator |
| L2 | `approved_for_ads` | Open | Operator |
| L3 | `approved_for_launch` | Open | Operator |
| L4 | `approved_for_commander_import` | Open | Operator |
| L5 | `intent_continuity_ack` in PPC instance (zakaz) | **false** | Operator |

---

## Live QA and URLs

| ID | Item | Status | Notes |
|----|------|--------|-------|
| Q1 | Live QA pending | Open | No repo evidence of production SERP/URL verification |
| Q2 | Live URLs / deploy state | **SAFE UNKNOWN** | Registry flags on multiple routes |
| Q3 | Homepage `/` vs master-hot charter | **SAFE UNKNOWN** | Rollout plan notes ambiguity |
| Q4 | Pack vs live `dist/` parity (zakaz) | **SAFE UNKNOWN** | Requires operator deploy check |

---

## Mobile and Factory

| ID | Item | Status | Notes |
|----|------|--------|-------|
| M1 | Mobile overflow unknowns | Open | Post-implementation; armatura typography risk flagged |
| M2 | Mobile QA after implementation | Open | All routes except partial zakaz device QA |
| M3 | Route rollout pending (V6 HTML) | Open | 11/12 scaffolds only |
| M4 | V6 build closure for siblings | Open | Only `index.html` in build closure |
| M5 | Registry `website_factory_page` v4 paths | Open | Sync to V6 truth — operator |

---

## Semantic / PPC

| ID | Item | Status | Notes |
|----|------|--------|-------|
| S1 | D2 H1 multi-ad (zakaz): «Аренда» vs «Заказать» | Open | `triumph-manipulyator-zakaz-pack-v1` |
| S2 | D1 qualification visibility (zakaz hero notice) | Open | Verify in QA — as-built may differ from G2 notes |
| S3 | Dedicated zakaz handoff MD | Open | Mirror 5-tonn pattern |
| S4 | PPC continuity sign-off (5-tonn pack) | Open | `APPROVALS.md` |
| S5 | Profile B packs — visual-semantics folders | Partial | Copy locked; full YAML bundle optional |
| S6 | konteynery registry blueprint path | Incomplete | `landing-route-registry.json` — folder-only pointer |

---

## Commercial / legal

| ID | Item | Status | Notes |
|----|------|--------|-------|
| C1 | Docs/bank confirmation unknowns | **SAFE UNKNOWN** | B2B yurlic route — operator commercial sign-off |
| C2 | Operator pricing sign-off (bytovki et al.) | Open | Per PACK-STATUS |
| C3 | Legal/payment wording check (5-tonn) | Open | `APPROVALS.md` |

---

## Tooling / export

| ID | Item | Status | Notes |
|----|------|--------|-------|
| T1 | DOCX exporter run for full family | Open | Pilot structure only |
| T2 | Content pack for zakaz in registry semantic-lock trail | Partial | `semantic-lock-state-v1.md` noted gaps — superseded by pack v1 but operator should reconcile |

---

## Explicitly deferred (not open for this freeze)

| Item | Reason |
|------|--------|
| New calibration loops | Task DO NOT |
| New route generation | Task DO NOT |
| Governance expansion | Task DO NOT |
| Workspace edits | Task DO NOT |
| Rollout execution | Task DO NOT |

---

## Review cadence

Update this file when:

- A route completes Factory pilot + operator QA
- An approval gate flips to true (with operator initial + date)
- A SAFE UNKNOWN resolves with evidence link (report path, not assumption)
