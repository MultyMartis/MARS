# EAR Acquisition Tracks v1

**Purpose:** Formalize the **two-track** EAR acquisition model — **Offline** and **Connected** — as permanent, co-equal acquisition families.  
**Status:** architecture specification — **no** implementation, runtime, connectors, or scripts.  
**Phase:** 2E  
**Parent:** [EAR-ARCHITECTURE-v1.md](EAR-ARCHITECTURE-v1.md)  
**Relation:** Complements [EAR-MODES-v1.md](EAR-MODES-v1.md) (how evidence is collected) and [EAR-ACQUISITION-MODES-v1.md](EAR-ACQUISITION-MODES-v1.md) (Mode 0–3 operational detail). Phase 2D defined the **connector layer** for Connected acquisition; Phase 2E names the **families** both tracks belong to.

---

## Why two tracks exist

EAR serves **heterogeneous operational reality**, not a single access pattern.

| Discovery source | Insight |
|------------------|---------|
| OCPilot **SITE-001** | Active managed project with SFTP, SSH, phpMyAdmin, and Admin channels — **Connected** is required for recurring, governed read-only acquisition. |
| Legacy / client / audit work | Many engagements deliver **archives only** — no live channel, no credentials, or policy forbids connection. **Offline** is required and must remain first-class. |
| MARS consumer roadmap | OCPilot, WPilot, Website Factory, and future CMS pilots share one snapshot contract but **different** acquisition preferences per project lifecycle. |

A single-track model (Connected-only or Offline-only) would force consumers to bypass EAR or invent parallel acquisition — both are **forbidden** by Phase 2E design decisions.

---

## Track overview

| Track | Model | Primary inputs | Primary EAR modes | v1 implementation |
|-------|-------|----------------|---------------------|-------------------|
| **A** | **Offline Acquisition** | Site archive, database archive (operator-delivered) | Mode 0 (Manual), Mode 1 (Guided) | Semantics supported; no EAR automation required |
| **B** | **Connected Acquisition** | Approved read-only channels (SFTP, SSH, PMA metadata, Admin read paths, …) | Mode 2 (Connected Read Only) | **Architecture only** — connectors per Phase 2D, runtime Phase 3+ |

Both tracks produce the same **consumer-facing artifact**: a governed **Snapshot Package** after Validate and Publish. Tracks differ in **how evidence enters EAR**, not in consumer analysis role.

---

## Offline Acquisition

**Definition:** Operator supplies **archives and exports** (or equivalent file drops). EAR validates, assembles, and publishes a Snapshot. No live connector session is required for the Acquire leg.

**Philosophy:** **Archive First** — treat delivered packages as authoritative evidence for a point in time; corroborate with manifests and `safe-unknown` honesty, not live re-fetch.

**Detail:** [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md), [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md)

### When to use

| Situation | Fit |
|-----------|-----|
| Legacy or archived project | **Strong** |
| Client-provided ZIP + DB dump | **Strong** |
| No-access audit (evidence package only) | **Strong** |
| One-off audit with no recurring charter | **Strong** |
| Air-gapped or credential-free engagement | **Strong** |
| Initial baseline before Connected channels are approved | **Strong** (often Hybrid prelude) |

### When not to use

| Situation | Reason |
|-----------|--------|
| Recurring snapshots on active host without operator re-export | Connected or Hybrid preferred |
| Need fresh `acquisition-log` from live channel for compliance | Offline is stale by definition |
| Operator expects EAR to pull deltas automatically | Requires Connected track (future Mode 2) |

---

## Connected Acquisition

**Definition:** EAR (future connectors under operator HITL) acquires read-only evidence from **approved systems** on an active project. Evidence passes through **Evidence Package** → Validate → Snapshot per Phase 2D.

**Philosophy:** **Managed Project** — long-lived operational sites with chartered channels, repeatable scope, and structured provenance in `acquisition-log` / `access-log`.

**Detail:** [EAR-CONNECTED-ACQUISITION-v1.md](EAR-CONNECTED-ACQUISITION-v1.md), [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md), [EAR-CONNECTOR-ARCHITECTURE-v1.md](EAR-CONNECTOR-ARCHITECTURE-v1.md)

### When to use

| Situation | Fit |
|-----------|-----|
| SITE-001, BZPM, dealership support projects | **Strong** |
| Recurring read-only audits | **Strong** |
| Active maintenance with chartered SFTP/SSH/PMA/Admin | **Strong** |
| Target Snapshot Level 2–3 with repeatable manifests | **Strong** (when channels confirmed) |

### When not to use

| Situation | Reason |
|-----------|--------|
| No credentials and no charter for external access | Use Offline |
| One-time archive-only engagement | Connected adds risk without benefit |
| Write access required | **Not EAR v1** — Mode 3 forbidden; separate change process |
| Connector runtime not chartered | Mode 0/1 Offline path until Phase 3+ pilot |

---

## Hybrid (cross-track)

**Hybrid** is not a third permanent family — it is a **lifecycle pattern** combining Offline and Connected acquisitions under one `site_id` with distinct `snapshot_id` values.

| Pattern | Example |
|---------|---------|
| Offline baseline → Connected refresh | Initial ZIP+DB (Offline), later SFTP+PMA (Connected) for Run 5 extension pass |
| Connected partial → Offline gap fill | Connector timeout on DB metadata; operator delivers PMA export (Offline leg) |
| Multi-snapshot compare | Level 1 archive snapshot vs Level 2 connected snapshot — consumer diff policy |

Selection rules: [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md)

---

## Track vs EAR mode (mapping)

| Acquisition track | Typical EAR modes | Acquire mechanism |
|-------------------|-------------------|-------------------|
| **Offline** | 0, 1 | Operator files → EAR Validate |
| **Connected** | 2 | Connector → Evidence Package → EAR Validate |
| **Hybrid** | 0/1 + 2 across snapshots | Per-leg mode recorded in metadata |

Metadata SHOULD record `acquisition_track`: `offline` | `connected` | `hybrid` (per snapshot) in addition to `ear_mode` when published — **field name frozen at architecture level**; serialization **SAFE UNKNOWN** until Phase 3 schema charter.

---

## Consumer invariant (both tracks)

```
Operator → EAR → Snapshot Package → Consumer
```

Consumers **never** bypass EAR for acquisition. Whether evidence arrived as archive or connector output, the **published snapshot** is the only consumer input. See [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md), [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md).

---

## Phase 2E document map

| Document | Role |
|----------|------|
| [EAR-OFFLINE-ACQUISITION-v1.md](EAR-OFFLINE-ACQUISITION-v1.md) | Offline mission, I/O, strengths/weaknesses |
| [EAR-CONNECTED-ACQUISITION-v1.md](EAR-CONNECTED-ACQUISITION-v1.md) | Connected mission, I/O, managed-project philosophy |
| [EAR-ACQUISITION-SELECTION-GUIDE-v1.md](EAR-ACQUISITION-SELECTION-GUIDE-v1.md) | Decision questions → track choice |
| [EAR-OFFLINE-PATHS-v1.md](EAR-OFFLINE-PATHS-v1.md) | Canonical offline paths → snapshot levels |
| [EAR-CONNECTED-PATHS-v1.md](EAR-CONNECTED-PATHS-v1.md) | Canonical connected paths → snapshot levels |
| [EAR-OCPILOT-INTEGRATION-v1.md](EAR-OCPILOT-INTEGRATION-v1.md) | OCPilot consumption by track |
| [EAR-FUTURE-CONSUMERS-v1.md](EAR-FUTURE-CONSUMERS-v1.md) | Expected consumers and preferences |
| [EAR-PHASE-2E-DESIGN-DECISIONS-v1.md](EAR-PHASE-2E-DESIGN-DECISIONS-v1.md) | Approved decisions DD-2E-* |

---

## SAFE UNKNOWN

- Whether `acquisition_track` is mandatory in OpenCart snapshot metadata v1.1 — Phase 3 schema charter.
- Unified track selector CLI — not specified.
- Cross-track snapshot merge into single `snapshot_id` — policy undefined; default is separate snapshots.

---

## Non-goals (Phase 2E)

- Code, runtime, connectors, scripts, automation
- Live SITE-001 or any host access
- Replacing Phase 2C channel paths or Phase 2D connector contracts — they nest **under** Connected track
