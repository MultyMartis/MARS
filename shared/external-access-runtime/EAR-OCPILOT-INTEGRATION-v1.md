# EAR OCPilot Integration v1

**Purpose:** Document how **OCPilot** consumes EAR output across **Offline** and **Connected** acquisition tracks — audit vs operations layers, and implications for future development.  
**Status:** architecture / consumer contract — **no** OCPilot or EAR implementation claimed.  
**Phase:** 2E  
**Extends:** [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md) (Phase 2A intake rules)

---

## Integration invariant

```
Operator → EAR (Offline and/or Connected) → Published Snapshot → OCPilot
```

OCPilot **never** acquires evidence from live sites when a snapshot path is chartered. OCPilot **never** invokes connectors. Re-acquisition requires a **new EAR cycle** (operator + EAR), not a consumer-side live pull.

---

## OCPilot layers vs EAR tracks

| OCPilot layer | Role | EAR track interaction |
|---------------|------|------------------------|
| **Audit Layer** | Read-only analysis, diff vs baseline, reports (e.g. Run 5) | Consumes **published snapshots** only; agnostic to track if quality level sufficient |
| **Operations Layer** | Future: change runs, deployment, remediation | **Out of EAR v1** — not snapshot consumption; must not bypass EAR for evidence refresh |

Phase 2E clarifies that **acquisition track** affects how evidence arrives, not how OCPilot grades findings. Gating remains **quality level** + `safe-unknown` per [EAR-OPENCART-CONSUMER-GUIDE-v1.md](EAR-OPENCART-CONSUMER-GUIDE-v1.md).

---

## Offline OCPilot workflows

| Workflow | EAR path | OCPilot behavior |
|----------|----------|------------------|
| **Run 5 resume (archive-first)** | OFF-L1-A/B, Mode 0/1 | Intake Level 1+; halt phases needing `file-manifest` if missing |
| **Legacy site audit** | OFF-L0–L2 | Gate phases by level; heavy `safe-unknown` expected |
| **Client package one-off** | OFF-L1-B | Point-in-time; no live re-fetch |
| **Freeze / bridge alignment** | Matches [projects/ocpilot/freeze/site-001-pre-runtime-bridge/](../../projects/ocpilot/freeze/site-001-pre-runtime-bridge/) | Documentation-only bridge until snapshot published |

**Operator pattern:** WinSCP / panel download → files → EAR Validate → Publish → OCPilot intake (today’s practical path for SITE-001 before Mode 2 runtime).

**OCPilot assumptions (offline):**

- `ear_mode` 0 or 1 in metadata — noisier packages possible.
- `acquisition-log` may list manual channels only.
- Staleness must be read from log dates — consumer must not assume freshness.

---

## Connected OCPilot workflows

| Workflow | EAR path | OCPilot behavior |
|----------|----------|------------------|
| **SITE-001 managed audit** | CON-L2-A – CON-L3-B (when runtime chartered) | Expect structured manifest + acquisition-log |
| **Extension inventory refresh** | CON-S1 scoped partial | New `snapshot_id`; compare to prior if chartered |
| **Recurring support (BZPM, dealership)** | CON-S3 recurring | Explicit snapshot lineage in reports |
| **Level 3 comprehensive** | CON-L3-B | Enable Level 3-gated audit phases |

**OCPilot assumptions (connected):**

- `ear_mode` 2 when runtime used.
- Richer `acquisition-log` — channel, scope, connector class references (no secrets).
- Still **point-in-time** — no silent live sync during audit.

**Pre-runtime SITE-001:** Connected workflows are **documented target**; execution remains **SAFE UNKNOWN** until Phase 3 Connected Acquisition Pilot Charter.

---

## Hybrid OCPilot workflows

| Pattern | EAR | OCPilot |
|---------|-----|---------|
| Offline L1 baseline → Connected L2 extension | OFF-L1 then CON-S1 | Two snapshots; Run 5 may resume after first publish, extend after second |
| Connected partial → Offline gap | CON partial + OFF-S3 | Consumer uses published snapshot; operator may need to reconcile two publishes |
| Compare stale backup vs fresh connected | OFF-S1 + CON-L3-B | Diff charter must name **both** `snapshot_id` values |

OCPilot reports **must** cite `snapshot_id` per finding. Cross-snapshot conclusions require explicit analysis charter.

---

## Audit Layer (detail)

**Purpose:** Structural and configuration audit (OpenCart / ocStore), baseline diff, extension risk indicators.

| Input from EAR | Audit use |
|----------------|-----------|
| `file-manifest` | Core diff vs `ocstore-3038-rs2` |
| `extension-inventory` | Level 2+ phases |
| `database-metadata` | Schema indicators — not business data |
| `safe-unknown` | Phase halts |
| `package_quality_level` | Phase gating |

**Track-agnostic rule:** If Level 1+ is published honestly, audit proceeds regardless of Offline vs Connected. If only Level 0, audit phases that need files **halt**.

**SITE-001 Run 5 (documented minimum):** Level **1+** with `file-manifest` before structural audit resume — see freeze docs and [EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md](EAR-SITE-001-WORKFLOW-EXAMPLE-v1.md).

---

## Operations Layer (boundary)

| Activity | EAR / OCPilot split |
|----------|---------------------|
| Deploy, fix, migration | **Not EAR acquisition** — separate change process |
| “Refresh audit during deploy” | New EAR Request — Connected or Offline per guide |
| Consumer write to live site | **Forbidden** in v1 read-only stack |
| Future Mode 3 | **Not in v1** — would not be OCPilot audit layer default |

Operations Layer must **not** embed SFTP/SSH clients for evidence — any refresh goes through EAR.

---

## Implications for future development

| Area | Implication |
|------|-------------|
| **OCPilot Run 5 resume** | Charter must name track + path; offline viable before connector runtime |
| **OCPilot registry** | Store `snapshot_id`, quality level, optional `acquisition_track` metadata |
| **Diff tooling** | Support multi-snapshot compare for Hybrid — not assumed v1 |
| **Reporting** | Display acquisition track for operator transparency — optional UI |
| **Phase 3 EAR pilot** | OCPilot remains consumer-only; pilot validates CON-L1/L3 paths against Run 5 gates |
| **Operations features** | Any live host action ≠ EAR; do not merge Operations Layer into connector layer |

---

## Cross-references

| Document | Use |
|----------|-----|
| [projects/ocpilot/OPERATIONAL-INDEX.md](../../projects/ocpilot/OPERATIONAL-INDEX.md) | Run 5 pause |
| [EAR-SITE-001-ACQUISITION-OPTIONS-v1.md](EAR-SITE-001-ACQUISITION-OPTIONS-v1.md) | SITE-001 options |
| [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md) | Sibling consumers |

---

## SAFE UNKNOWN

- OCPilot UI for track selection — not specified.
- Automatic “latest snapshot” pointer per site — registry policy TBD.
- Whether Operations Layer ever shares EAR credential store — **forbidden** by default security model.
