# MARS — Critical node validation (Cycle 8)

**Status:** **documented** — focused validation of highest document-gravity and routing-risk nodes.  
**Date:** 2026-05-19.  
**Scope:** Task B — survivability, overload resistance, navigation resilience, drift resistance, scaling durability per node.

**Rating key (each dimension):** **Strong** · **Adequate** · **Weak** · **At limit**

---

## Summary matrix

| Node | Survivability | Overload resistance | Navigation resilience | Drift resistance | Scaling durability |
|------|---------------|---------------------|----------------------|------------------|-------------------|
| **Factory Extended** | Adequate | **Weak** | Adequate (if Core-only) | Adequate | **At limit** |
| **ORCA document gravity** | **Strong** (live) | **Weak** (corpus) | **Strong** (INDEX) | Adequate | **At limit** |
| **governance/README** | Adequate | **Weak** | **Strong** (one-row) | Adequate | Weak |
| **Topology + reality indexes** | **Strong** | Adequate | **Strong** | Adequate | Adequate (+3), Weak (+10) |
| **Forge checklist catalog** | Adequate | Weak | Adequate | **Strong** (transition doc) | Weak |
| **Registry / lifecycle parity** | Adequate | **Strong** | **Strong** | **Weak** (log lag) | Adequate |
| **web-gpt-sources legacy** | Weak (if first-read) | Weak | Weak | Weak | N/A (frozen lane) |

---

## 1. Factory Extended (`OPERATIONAL-INDEX` Extended + meta-governance triads)

| Dimension | Assessment |
|-----------|------------|
| **Survivability** | **Adequate** — Core Run (8 concerns + Frontend block once) is session-viable; Extended is correctly labeled Tier 3 with STOP cue |
| **Overload resistance** | **Weak** — default sink for new `*-governance.md`; ~258 pack files; domain tables span semantics → meta-governance |
| **Navigation resilience** | **Adequate** when operators stay on one Core row; **fails** if Extended opened without citation |
| **Drift resistance** | **Adequate** — INDEX-first discipline documented; triad sprawl still permeable |
| **Scaling durability** | **At limit** — +3 entities manageable via row discipline; +5 without compression → unmaintainable Extended |

**Collapse mode:** Extended treated as mandatory syllabus; fourth sibling taxonomy doc without Core row.

**Mitigations (existing):** Core/Extended split, entropy rules, compression strategy doc — **no new fix required in Cycle 8**.

---

## 2. ORCA document gravity (~473 md)

| Dimension | Assessment |
|-----------|------------|
| **Survivability** | **Strong** for live PPC — FAST PATH, STOP NOW, max depth 1+1, 10–20 min target |
| **Overload resistance** | **Weak** at corpus level — volume unbounded; “one more checklist” loop |
| **Navigation resilience** | **Strong** — OPERATIONAL-INDEX live-first; operator-entrypoints banner redirects live sessions |
| **Drift resistance** | **Adequate** — STOP cues; secondary entry docs partially duplicate INDEX |
| **Scaling durability** | **At limit** — new subsystem without starter-core row → gravity amplifies |

**Collapse mode:** Starter Core menu exhaustion; project-shaped entry in live session.

---

## 3. governance/README (~88+ linked rows in addenda table)

| Dimension | Assessment |
|-----------|------------|
| **Survivability** | **Adequate** as **router** (one row); **Weak** if full table scan |
| **Overload resistance** | **Weak** — S0–S7 + Phase 3–7 + reality audit rows accumulate |
| **Navigation resilience** | **Strong** with Tier 1 one-row rule; fragile under “read all governance” |
| **Drift resistance** | **Adequate** — new phase = new row (entropy rules apply) |
| **Scaling durability** | **Weak** at +5 new governance programs without compression |

**Collapse mode:** Encyclopedia read during onboarding; new Phase 8+ row without editorial pass.

---

## 4. Topology + reality indexes

| Dimension | Assessment |
|-----------|------------|
| **Survivability** | **Strong** today — compact, pick-one, cross-linked to entrypoint model |
| **Overload resistance** | **Adequate** — linear row growth |
| **Navigation resilience** | **Strong** — not contradictory when used as routers |
| **Drift resistance** | **Adequate** — human-maintained; no auto-sync |
| **Scaling durability** | **Adequate** at +3; **Weak** at +10 without row-cap policy |

**Collapse mode:** Sixth Tier 1 “start here”; both indexes + governance README in one session.

---

## 5. Forge checklist catalog (42 md under `agents/mars-forge/`)

| Dimension | Assessment |
|-----------|------------|
| **Survivability** | **Adequate** — AGENT.md + qa-checklist.md entry; operational modes model |
| **Overload resistance** | **Weak** — README catalog scroll opens Tier 3 as Tier 2 |
| **Navigation resilience** | **Adequate** — foundation map + transition stabilization |
| **Drift resistance** | **Strong** — “not second Gulp SoT” repeated across governance |
| **Scaling durability** | **Weak** — each new QA domain = file + README row |

**Collapse mode:** Checklist enumeration loop; overlay perceived as parallel SoT.

---

## 6. Registry / lifecycle parity

| Dimension | Assessment |
|-----------|------------|
| **Survivability** | **Adequate** — registry-source-of-truth clear |
| **Overload resistance** | **Strong** — small tables |
| **Navigation resilience** | **Strong** — single project-registry, agents/registry |
| **Drift resistance** | **Weak** — lifecycle log **0016** last; ORCA/WPilot/MetaBOT/Phase 1 backlog **0017–0021** not backfilled |
| **Scaling durability** | **Adequate** if “registry change → lifecycle append same session” enforced |

**Collapse mode:** Registry row updated without lifecycle event → claim/evidence gap for auditors.

---

## 7. web-gpt-sources legacy surfaces

| Dimension | Assessment |
|-----------|------------|
| **Survivability** | **Weak** if used as Tier 0 |
| **Overload resistance** | **Weak** — numbered pack, no OPERATIONAL-INDEX |
| **Navigation resilience** | **Weak** — depth-first tree |
| **Drift resistance** | **Weak** — vocabulary may predate governance |
| **Scaling durability** | **N/A** — lane should shrink or stay frozen, not grow |

**Collapse mode:** First-read before AGENTS; chat-migration snapshot as live state.

---

## Critical-node verdict

**PASS with hotspots** — no single node breaks the global spine; **Factory Extended**, **ORCA volume**, and **lifecycle lag** are the highest operational risks. Hardening from Phase 6–7 is **effective at Tier 0–2**; **volume layers** remain stress-sensitive.

---

## Related (Cycle 8)

- [mars-document-gravity-hardening-review-v0.md](mars-document-gravity-hardening-review-v0.md)  
- [mars-global-ecosystem-validation-cycle-8-topology-v0.md](mars-global-ecosystem-validation-cycle-8-topology-v0.md)

---

*Cycle 8 Task B — critical nodes only; no commits implied.*
