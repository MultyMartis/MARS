# Survivability Checkpoint v1

**Freeze:** ORCA Route Family Freeze v1 · 2026-05-28  
**Lane:** B — ORCA Freeze + Survivability  
**Type:** Human-operated documentation checkpoint — **not** automated backup, **not** runtime

---

## Current operational milestone

**Milestone:** Triumph Manipulator — **ORCA production semantic route family complete (12/12)** with stabilized differentiation and ORCA ↔ Website Factory coordination — **pre-implementation rollout**.

| Prior milestone | Current milestone | Next (out of freeze scope) |
|-----------------|-------------------|----------------------------|
| Single-route calibration (zakaz / 5-tonn) | Full family semantic freeze | Factory V6 pilot wave (e.g. 5-tonn → bytovki) |

---

## Why freeze performed

1. **Semantic surface area closed** — all 12 PPC routes have v1 production packs; further copy churn risks drift without Factory consumption.
2. **Differentiation discipline** — logistics batch + per-route H1 locks must not regress during implementation.
3. **Survivability** — operator needs a recoverable baseline before workspace rollout edits and git noise.
4. **Boundary honesty** — freeze separates **documented semantic baseline** from **false launch/runtime claims**.

---

## What is stabilized

| Stabilized | Location |
|------------|----------|
| 12-route family map | [ORCA-ROUTE-FAMILY-FREEZE-v1.md](ORCA-ROUTE-FAMILY-FREEZE-v1.md) |
| Per-route index | [ROUTE-FAMILY-INDEX-v1.md](ROUTE-FAMILY-INDEX-v1.md) |
| READY/PENDING rollup | [ROLLUP-STATUS-v1.md](ROLLUP-STATUS-v1.md) |
| Factory handoff roles | [FACTORY-HANDOFF-STATE-v1.md](FACTORY-HANDOFF-STATE-v1.md) |
| Open items register | [KNOWN-OPEN-ITEMS-v1.md](KNOWN-OPEN-ITEMS-v1.md) |
| Production pack format (A/B) | `content-packs/content-pack-system-v0.md` |
| Coordination protocol | `coordination/orca-factory-coordination-protocol-v1.md` |

---

## What remains human-operated

| Activity | Owner |
|----------|--------|
| `approved_for_factory` / launch gates | Operator |
| Factory HTML/SCSS implementation | Website Factory lane (human build) |
| Mobile QA after build | Operator QA |
| Commander import / ads | Operator |
| Registry drift sync | Operator |
| Git commit / push / deploy | Operator (explicit request only) |
| Survivability backup archive | Operator |

**No agent** may auto-approve packs, resolve destructive drift, or claim live deployment.

---

## Recommended git checkpoint label

```
orca-route-family-freeze-v1
```

**Suggested commit message (when operator requests commit):**

```
docs(orca): freeze Triumph 12-route semantic family v1

Document production semantic baseline, ORCA↔Factory split, and
survivability checkpoint before V6 implementation rollout.
```

**This session:** commit **not** performed per task instruction.

---

## Backup scope (critical directories)

Human-operated archive recommended **before** large Factory rollout edits:

| Priority | Path | Rationale |
|----------|------|-----------|
| P0 | `projects/orca/` | Semantic SoT: packs, coordination, calibration, PPC |
| P0 | `projects/orca/content-packs/examples/triumph-*-pack-v1/` | Frozen copy artifacts |
| P0 | `projects/orca/freeze/route-family-freeze-v1/` | This checkpoint |
| P1 | `projects/orca/calibration/triumph-manipulator/` | Calibration lessons |
| P1 | `projects/orca/coordination/` | Factory protocol + matrices |
| P1 | `projects/orca/visual-semantics/` | Cross-route contracts |
| P2 | `workspaces/triumph-manipulator-landing-v5/` | Prior as-built reference |
| P2 | `workspaces/triumph-manipulator-landing-v6/` | V6 baseline (exists) |
| P2 | `projects/orca/projects/triumph-manipulator-krasnodar/` | Route registry |

**Not required for semantic freeze:** `governance/*`, `mars-runtime/*` (explicitly out of scope).

---

## Runtime / autonomy claim check

Freeze artifacts reviewed for prohibited claims:

| Claim type | Present in freeze docs? |
|------------|-------------------------|
| Autonomous orchestration | **No** |
| Runtime / bidding / auto-launch | **No** |
| Automated validation enforcement | **No** |
| Live production proof | **No** — SAFE UNKNOWN where applicable |

---

## Recovery pointer

If semantic drift occurs post-rollout:

1. Restore from checkpoint label `orca-route-family-freeze-v1`.
2. Diff pack vs Factory report — use `calibration/triumph-manipulator/drift-analysis/`.
3. Re-read [FACTORY-HANDOFF-STATE-v1.md](FACTORY-HANDOFF-STATE-v1.md) before accepting Factory copy changes.
