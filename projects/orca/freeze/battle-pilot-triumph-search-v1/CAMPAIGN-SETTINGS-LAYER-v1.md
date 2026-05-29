# Campaign Settings Layer v1

**Purpose:** Document what the Commander XLSX transport layer can and cannot carry for Triumph Search PPC.  
**Date:** 2026-05-30  
**Source:** Battle pilot Commander import findings

---

## Core principle

**XLSX = dumb transport.** Campaign strategy, budget, and schedule are **not** a full transport layer in Commander Template v1. They require **post-import human setup** in Direct Commander UI.

This is **not a bug** — it is an architectural boundary that must be documented and gated.

---

## Transport matrix

| Setting | XLSX (template v1) | Exporter v1.4 | Post-import UI | Battle result |
|---------|-------------------|---------------|----------------|---------------|
| Campaign type | R7C5 | Patched | Confirm | PASS |
| Placement (Search) | R7C8 | Patched | Confirm | PASS |
| Currency RUB | R8C8 | Patched | Confirm | PASS |
| Campaign negatives | R9C5 | Patched | Confirm | PASS |
| Optimize text | R10C5 | Patched | Confirm | PASS |
| Promotion URL (root) | R11C5 | Patched | Confirm | PASS |
| Group structure | Sheet1 rows | Transport split | Confirm counts | PASS |
| Ads (text + URLs) | Sheet1 rows | Transport split | Spot-check | PASS |
| Keywords + match types | Sheet1 rows | Transport split | Spot-check | PASS |
| Keyword bids (values) | Col 54 | v1.3+ bid-assignment | **Requires strategy activation** | PASS after UI |
| Autobid flag | Col 53 (`-`) | Exported | **Requires strategy activation** | PASS after UI |
| Group negatives | Col 68 | v1.4 cross-negative | Confirm no rejection | PASS |
| Fastlinks / callouts | Sheet1 cols | Exported | Spot-check | PASS |
| **Weekly budget** | **Not in template** | N/A | **Set manually** | Pending |
| **Daily budget cap** | **Not in template** | N/A | **Set manually** | Pending |
| **Ad schedule** | **Not in template** | N/A | **Set manually** | Pending |
| **Smart bidding strategy** | **Out of scope** | N/A | N/A | N/A |

---

## Post-import campaign settings checklist (mandatory)

Use this checklist **after every Commander import** before treating a campaign as launch-ready:

### Strategy layer

- [ ] Open campaign settings in Direct Commander  
- [ ] Confirm «Единая перфоманс-кампания» + Search placement  
- [ ] Activate **ручное управление ставками** (manual bid management)  
- [ ] Verify bids visible on all 64 keyword phrases (400–600 ₽)  
- [ ] Confirm no zero bids on active phrases  

### Budget layer

- [ ] Set weekly or daily budget intentionally  
- [ ] Confirm budget aligns with operator plan (not default/test value)  
- [ ] Document chosen budget in operator log  

### Schedule layer

- [ ] Set ad schedule if required (hours/days)  
- [ ] Confirm schedule matches business hours intent  

### Final gates

- [ ] Promotion URL = `https://manipulator-triumph.ru/`  
- [ ] No duplicate ads per group  
- [ ] Group negatives active — no syntax errors  
- [ ] Operator sign-off recorded  
- [ ] Launch **not** enabled until explicit approval  

---

## Why bids need UI activation

Exporter v1.3+ writes bid values to col 54 and sets col 53 (autobid) to `-`. Commander stores these values in the XLSX, but the UI **does not display bids** until the campaign strategy layer is explicitly configured.

**Battle observation:** Import succeeded, bid values present in transport, but UI showed no bids until operator manually selected manual bid strategy.

**ORCA obligation:** Export READY gate passes; post-import checklist is **separate mandatory step**.

---

## Future upgrade (backlog)

See [ORCA-UPGRADE-BACKLOG-v1.md](ORCA-UPGRADE-BACKLOG-v1.md) — P0: Post-import campaign settings checklist (this doc becomes gate artifact).

---

## Boundaries

- Does **not** define live budget amounts — operator decision  
- Does **not** automate Commander UI setup  
- Does **not** claim Direct API integration (P2 research item)
