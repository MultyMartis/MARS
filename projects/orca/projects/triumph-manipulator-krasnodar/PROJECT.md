# Triumph Manipulator — Краснодар

**Canonical project container v0** — navigation, identity, approvals, registry, bridge.  
**Not** Search-pack SoT. **Not** runtime.

---

## Project identity

| Field | Value |
|-------|--------|
| **project_id** | `triumph-manipulator-krasnodar` |
| **brand** | Триумф (Triumph Manipulator) |
| **geo** | Краснодар, Краснодарский край |
| **primary service** | Аренда / заказ манипулятора с КМУ (5 т борт / 3 т стрела — capability-фокус; use-case и B2B маршруты в Search Full Cycle) |
| **industry** | Local equipment rental / heavy haul |
| **domain (declared)** | `https://manipulator-triumph.ru` |
| **current status** | `factory` → `launch-prep` (Search export ready; launch gates open) |
| **validated Search-pack reference** | [`projects/orca/ppc/triumph-manipulator/`](../../ppc/triumph-manipulator/) — **active, validated, operational**; not migrated |
| **Website Factory reference** | [`workspaces/triumph-manipulator-landing-v4/`](../../../../workspaces/triumph-manipulator-landing-v4/) |
| **Landing route registry** | [`landing-route-registry.json`](landing-route-registry.json) |

---

## Modes

| Mode | State | Notes |
|------|--------|--------|
| **Search** | **active** | Full Cycle v1.1 — 12 groups, validation passed, export produced |
| **RSYA** | **planned** | Not in current export scope |
| **Retarget** | **future** | Not configured |
| **Brand** | **not configured** | — |
| **Local** | **partial** | Geo copy in pack; no separate Local pack folder |
| **Experimental** | **isolated** | Must not pollute validated Search-pack without explicit charter |

---

## Current operational state

| Milestone | Status |
|-----------|--------|
| Full Cycle v1.1 | Exists — [`runs/full-cycle-v1.1/`](../../ppc/triumph-manipulator/runs/full-cycle-v1.1/) |
| Commander transport | Validated (Region Import Fix v0.6, sheet1-patch, post-export ZIP checks) — **human import not signed off** |
| v5 landing production | Started — workspace v4 |
| ORCA → Website Factory bridge | Validated (handoff + semantic lock MODE 1) |
| Landing page 01 | Implemented in Factory — [`dist/manipulyator-5-tonn/`](../../../../workspaces/triumph-manipulator-landing-v4/dist/manipulyator-5-tonn/) |
| Remaining routes | Registry + blueprints; Factory build **pending** |

---

## Source state

Pointers to validated pack layers (no duplication in this container).

| Layer | Status | Reference |
|-------|--------|-----------|
| Raw pack | Inventied / distributed (historical intake) | Triumph raw pack via pack docs — **SAFE UNKNOWN** for manifest path in this container |
| Normalized intelligence | Partial / operational in pack | [`ppc/triumph-manipulator/`](../../ppc/triumph-manipulator/) schema, prompts, validation rules |
| Research | Snapshot-complete for Search architecture | Landing architecture + SERP methodology in pack |
| Evidence | Graded in validation rules | Commercial / symbol / landing continuity rules |
| Competitors | Present in pack research lane | **SAFE UNKNOWN** — single index path not consolidated here |
| Landing briefs | Approved blueprints in pack | [`landing-pages/`](../../ppc/triumph-manipulator/landing-pages/) |

---

## Artifact state

| Artifact | Status | Location (validated pack) |
|----------|--------|---------------------------|
| Keyword pack | **approved** (export_allowed) | `triumph-s-tier-draft-v1.json` + Full Cycle v1.1 |
| Strategy | **approved** (S-tier + groups 11–12) | Campaign structure v1.1 |
| Commander export | **production-ready** (transport) | `triumph-sheet1-patch-full-cycle-v1.1.xlsx` |
| Landing handoff | **production** (page 01) | [`handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md`](../../ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md) |
| v5 landing implementation | **in_progress** (1/12 routes built) | `workspaces/triumph-manipulator-landing-v4/` |

---

## Approval gates

Summary mirrors [`approvals/approval-state-v0.md`](approvals/approval-state-v0.md). **Human authority only.**

| Gate | Value |
|------|--------|
| `approved_for_research_use` | yes (pack operational) |
| `approved_for_strategy` | yes |
| `approved_for_keywords` | yes (validation CLI passed v1.1) |
| `approved_for_factory` | yes (page 01 handoff + MODE 1 build) |
| `approved_for_commander_import` | **human-only** — transport validated; **gate not signed** |
| `approved_for_ads` | **pending QA** — manual browser QA required |
| `approved_for_launch` | **no** |

**Critical:** Commander import transport validated **≠** launch approved.

---

## Website Factory state

| Field | Value |
|-------|--------|
| Landing routes | [`landing-route-registry.json`](landing-route-registry.json) |
| Handoff status | Page 01: production handoff locked |
| Semantic lock mode | **MODE 1** (active for page 01) |
| Page implementation | Page 01: **implemented** (dist exists); routes 02–12: **pending** |
| QA | [`landing-qa/v5-page01-landing-qa-v0.md`](landing-qa/v5-page01-landing-qa-v0.md) — `approved_for_ads` pending |

---

## SAFE UNKNOWN

| Gap | Blocks |
|-----|--------|
| Live deployment | Whether `manipulator-triumph.ru` serves v5 page 01 in production |
| Real conversion data | CPC, CR, call quality — no analytics in repo |
| RSYA | Pack, creative, landing parity |
| Moderation at scale | Platform policy under live spend |
| Real CPC / auction | Post-launch only |
| Live URLs for routes 06, 11, 12 | See registry `SAFE UNKNOWN` per route |
| Homepage PPC fit (group 12) | Master hot on `/` — not verified live |

---

## Decision log links

| Decision / run | Path |
|----------------|------|
| Full Cycle v1.1 summary | [`../../ppc/triumph-manipulator/runs/full-cycle-v1.1/full-cycle-summary-v1.1.md`](../../ppc/triumph-manipulator/runs/full-cycle-v1.1/full-cycle-summary-v1.1.md) |
| Campaign structure v1.1 | [`../../ppc/triumph-manipulator/runs/full-cycle-v1.1/campaign-structure-v1.1.md`](../../ppc/triumph-manipulator/runs/full-cycle-v1.1/campaign-structure-v1.1.md) |
| Page 01 handoff | [`../../ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md`](../../ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md) |
| Exporter output | [`../../ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.1.xlsx`](../../ppc/triumph-manipulator/tools/exporter-cli/output/triumph-sheet1-patch-full-cycle-v1.1.xlsx) |
| Landing workspace | [`../../../../workspaces/triumph-manipulator-landing-v4/`](../../../../workspaces/triumph-manipulator-landing-v4/) |
| Route registry (canonical) | [`landing-route-registry.json`](landing-route-registry.json) |
| Bridge index | [`bridge-links.md`](bridge-links.md) |
| Approval record | [`approvals/approval-state-v0.md`](approvals/approval-state-v0.md) |

---

## Next actions

- [ ] Operator: manual browser QA page 01 → update `landing-qa/` and registry status for `manipulyator-5-tonn`
- [ ] Operator: Commander import smoke test → sign `approved_for_commander_import` if UI clean
- [ ] Operator: live URL check production vs registry
- [ ] Factory: handoff + build routes 02–12 per blueprint priority
- [ ] Do **not** migrate exporter/validation/runs into this container without explicit charter
