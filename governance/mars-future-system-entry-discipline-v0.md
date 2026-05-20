# MARS — Future system entry discipline

**Status:** **documented** — minimal onboarding gate for new **major** systems.  
**Date:** 2026-05-19.  
**Context:** Post-freeze scaling limits ([mars-governance-baseline-freeze-v0.md](mars-governance-baseline-freeze-v0.md) §6).

**Definition:** **Major system** = new pack, external bridge programme, or registered operational lane with its own README and delivery identity.

**Is:** a **checklist** — seven items, human-operated.  
**Is not:** onboarding bureaucracy, automated gate, certification, or ontology work.

---

## 1. Minimum onboarding requirements

Complete **all seven** before treating the system as ecosystem-visible:

| # | Requirement | Where |
|---|-------------|--------|
| **1** | **Topology row** | [ecosystem-topology-index.md](ecosystem-topology-index.md) — one row: what it is / is not, status, canonical path, relationship role |
| **2** | **Reality row** | [mars-reality-index-v0.md](mars-reality-index-v0.md) — correct bucket (operational / conceptual / experimental / external / …) |
| **3** | **Canonical entrypoint** | Pack README = **identity**; session SoT = **OPERATIONAL-INDEX** (or lane-equivalent FAST PATH) if corpus is large |
| **4** | **OPERATIONAL-INDEX** | Core Run ≤10 concern rows for large packs; Extended on-demand; STOP/FAST PATH where live ops apply (ORCA pattern) |
| **5** | **Lifecycle append** | `logs/lifecycle-log.md` line when **status** or implementation claim changes |
| **6** | **Lane assignment** | Path letter B–E or explicit lane in [survivability-onboarding-strategy-v0.md](survivability-onboarding-strategy-v0.md) — **no** new Tier 1 “start here” |
| **7** | **Registry row** | [registry/project-registry.md](../registry/project-registry.md) and/or [agents/registry.md](../agents/registry.md) per [registry-entry-minimal-standard.md](registry-entry-minimal-standard.md) |

**Optional (same pass, not substitute):** [external-system-boundaries.md](external-system-boundaries.md) row if external runtime.

---

## 2. Pre-entry gate (30-second check)

| Question | If “no” |
|----------|---------|
| Is there a **scoped charter** (who, lane, failure without system)? | Defer — IdeaBox or REPORT only |
| Is this **major** (not a single doc fix)? | Edit authoritative file; skip checklist |
| Will this stay within **+3** scaling discipline? | If +5 cluster forming → compression charter first |
| Does a system with same **role** already exist? | Extend existing pack — no duplicate lane |

---

## 3. Lane assignment rules

| System type | Lane pattern |
|-------------|--------------|
| **In-repo pack** (Factory-class) | Path B + OPERATIONAL-INDEX Core/Extended |
| **Live ops corpus** (ORCA-class) | Path C + FAST PATH + STOP |
| **External bridge** (MetaBOT, WPilot) | Path D/E + external map row — **external** implementation status |
| **Reference / delivery case** (Triumph-class) | Reference model — **not** production runtime proof |
| **Experimental code** | `mars-runtime/` or experimental scope — R1 qualifiers |

**Forbidden:** new Tier 1 router; new meta-governance triad before OPERATIONAL-INDEX row exists.

---

## 4. OPERATIONAL-INDEX minimum (large packs)

```text
Core Run (session default)
  - identity + honesty boundary (link README)
  - FAST PATH or Core Run table (≤10 rows)
  - STOP — minimum reads before depth

Extended (on-demand)
  - governance / taxonomy links by concern
  - banner: not session default
```

**WPilot / MetaBOT:** if no pack folder, use **external map + Factory bridge docs**; add OPERATIONAL-INDEX only when in-repo corpus justifies it.

---

## 5. What this checklist prevents

| Risk | Prevention |
|------|------------|
| **Entropy explosion** | No invisible system — always topology + reality |
| **Shadow SoT** | README vs INDEX split enforced |
| **Registry drift** | Row in same pass as public id |
| **Onboarding collapse** | Path letter instead of new global router |
| **Mythology** | Reality bucket + AGENTS three-way split |
| **Governance wave** | No triad until INDEX row proves operational need |

---

## 6. Post-entry maintenance

After entry, system owner (human) maintains:

- Core Run row accuracy when operational behaviour changes  
- Registry status when implementation posture changes  
- **No** automatic sync — event-driven per [mars-lightweight-maintenance-mode-v0.md](mars-lightweight-maintenance-mode-v0.md)

---

## 7. SAFE UNKNOWN

If any of the seven items cannot be completed:

- State **SAFE UNKNOWN** in REPORT  
- Do **not** advertise system as ecosystem-canonical  
- Complete missing items before cross-lane references in governance prose

---

*Entry discipline — minimal, practical, non-bureaucratic.*
