# ORCA Upgrade Backlog v1

**Source:** Battle Pilot Triumph Search PPC — post-battle analysis  
**Date:** 2026-05-30  
**Status:** Human-maintained backlog — **not** automated tracker

---

## P0 — Must fix before next battle cycle

| ID | Item | Battle evidence | Target artifact |
|----|------|-----------------|-----------------|
| P0-01 | **Final Website Copy Pack gate before Factory** | Semantic pack ≠ deployed copy; ad↔landing drift risk | New pack type + approval gate in content-packs workflow |
| P0-02 | **Commander Export no-duplicate transport model** | F1: keyword×ad bug produced 108 duplicate rows | Permanent architecture doc + transport matrix validator |
| P0-03 | **Commander-safe negative syntax** | F3: 12/12 groups failed v1.3 wildcard import | `commander_negative_syntax_pass` promoted to all export versions |
| P0-04 | **Post-import campaign settings checklist** | F5: bids invisible until UI strategy setup | [CAMPAIGN-SETTINGS-LAYER-v1.md](CAMPAIGN-SETTINGS-LAYER-v1.md) → formal gate |
| P0-05 | **URL registry/export sync gate** | F2: 164 URL replacements needed manually | Automated 3-layer sync check (registry + JSON + exporter) |

---

## P1 — High value, next evolution wave

| ID | Item | Rationale |
|----|------|-----------|
| P1-01 | **Automated cross-negative matrix builder** | Manual matrix maintenance doesn't scale to new routes |
| P1-02 | **Bid priority model** | Intent tier S/A/B should map to bid weight, not flat 400–600 |
| P1-03 | **Commander hygiene scanner** | Catch gruzotaxi tails, stale negatives, legacy URLs pre-export |
| P1-04 | **Export readiness dashboard** | Single view: validation + transport QA + URL + bids + negatives |
| P1-05 | **Launch readiness checklist** | Separate from export READY — conversion, analytics, moderation, sign-off |

---

## P2 — Future research / expansion

| ID | Item | Notes |
|----|------|-------|
| P2-01 | **DOCX/XLSX human artifacts** | Operator-facing reports beyond JSON/XLSX transport |
| P2-02 | **Future RSYA mode** | Separate template + transport model — not Search v1 |
| P2-03 | **Future Direct API research** | Evaluate API vs Commander XLSX — no commitment |
| P2-04 | **Multi-project ORCA template** | Generalize Triumph learnings to ORCA universal PPC pack |

---

## Priority rationale

**P0 items directly caused battle failures or near-misses.** Each maps to a documented failure in [FAILURES-AND-FIXES-v1.md](FAILURES-AND-FIXES-v1.md).

**P1 items reduce operator load** for the next campaign or route addition.

**P2 items are exploratory** — no battle urgency, no runtime commitment.

---

## Sequencing recommendation

```
Phase 1 (next chat): P0-01 through P0-05 — architecture + gates
Phase 2: P1-03, P1-04 — tooling helpers
Phase 3: P1-01, P1-02, P1-05 — optimization layer
Phase 4: P2 — research only
```

---

## Boundaries

- Backlog items are **documentation/tooling targets** — not runtime products  
- No item implies autonomous campaign management  
- Priority may change with human charter — this is v1 snapshot at battle freeze
