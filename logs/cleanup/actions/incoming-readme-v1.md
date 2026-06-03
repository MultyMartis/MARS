# Incoming README Action v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2A  
**Upstream:** [incoming-deep-review-v2.md](../discoveries/incoming-deep-review-v2.md), Wave 2 Discovery W2-A02  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`incoming/**` excluded from checkpoint)

---

## Action

| Item | Status |
|------|--------|
| Author ecosystem-level `incoming/README.md` | **Implemented** |
| Archive / delete / move intake folders | **Not executed** (Wave 2A charter) |

---

## Rationale

Wave 2 Discovery identified **no root intake charter** while multiple programs (MIG, ORCA, OCPilot, Factory) assumed different subfolder contracts. A single ecosystem README clarifies:

- `incoming/` = temporary quarantine / transport
- `incoming/` ≠ storage, archive, registry, runtime
- promote / archive / delete = human-gated

---

## Content summary (deliverable)

| Section | Purpose |
|---------|---------|
| What it is / is not | Trust and misread corrections |
| Expected lifecycle | Drop → triage → promote → optional retire |
| Promote / Archive / Delete | Operator boundaries |
| Related surfaces | IdeaBox, lifecycle, registry, cleanup, survivability — **links only** |

---

## Files changed

- **Created:** `incoming/README.md`
- **Created:** this evidence file

---

## Deferred (Wave 3+)

| ID | Action |
|----|--------|
| W2-A03 | Triage `incoming/orca-triumph-raw-pack/` — archive candidate |
| W2-A04 | Resolve `incoming/website-factory-legal-cleanup/` promote vs intake |
| N-01 | Hybrid Cold Brain moves after operator approval |

---

*Incoming README action v1 — Wave 2A evidence.*
