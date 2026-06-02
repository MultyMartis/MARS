# EAR Acquisition Modes v1

**Purpose:** Operational modes for **how** evidence is collected during the **Acquire** stage of [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md).  
**Status:** architecture specification — **no** implementation.  
**Phase:** 2B  

**Alignment:** Mode numbers `0`–`3` match [EAR-MODES-v1.md](EAR-MODES-v1.md). This document adds Phase 2B naming, quality expectations, and risk framing for acquisition workflow only.

---

## Mode overview

| Mode | Phase 2B name | EAR-MODES-v1 name | v1 status |
|------|---------------|-------------------|-----------|
| **0** | Manual Evidence | Manual | Supported semantics |
| **1** | Guided Evidence | Assisted | Supported semantics |
| **2** | Connected Read Only | Connected Read Only | **Design target** — not implemented |
| **3** | Connected Read Write | Connected Read Write | **Forbidden in v1** |

---

## Mode 0 — Manual Evidence

**Definition:** Operator supplies files and exports without EAR-driven collection automation. EAR (or operator with EAR checklist) wraps evidence into a candidate Snapshot Package at Validate.

### Advantages

- Works when no connector exists (SITE-001 default today)
- Air-gapped or low-trust environments
- Operator controls every byte transferred
- No credential flow through future EAR tooling

### Limitations

- Highest operator burden and inconsistency risk
- Manifests may be incomplete or non-standard layout
- Screenshots without machine-readable evidence
- Slow repeat audits

### Risks

| Risk | Mitigation (process) |
|------|----------------------|
| Incomplete sections | Guided checklist at Request; `safe-unknown` honesty |
| Wrong site folder copied | Request records path scope; operator verification |
| Stale exports | `created_at` and acquisition-log timestamps |
| Accidental write during collection | Operator discipline; charter forbids Mode 3 |

### Expected snapshot quality

| Typical outcome | Notes |
|-----------------|-------|
| Level 0–1 | Common for first pilot packages |
| Level 2–3 | Possible if operator delivers comprehensive exports — **not** guaranteed |
| Honesty | Gaps **must** appear in `safe-unknown`; no quality inflation |

---

## Mode 1 — Guided Evidence

**Definition:** EAR provides an **exact artifact request list** (runbook / DATA-REQUEST pattern); operator fulfills via any approved channel; operator delivers files for assembly.

### Advantages

- Reduces “what do you need?” friction (OCPilot Run 5 pattern generalized)
- Repeatable requests per quality level and platform spec
- Aligns with [external-access-patterns](../external-access-patterns/README.md) per-channel gates
- Still no connector implementation required

### Limitations

- Still human-executed on every channel
- Request drift if SITE changes mid-collection
- Partial fulfillment common — quality may stay below target

### Risks

| Risk | Mitigation (process) |
|------|----------------------|
| Skipped checklist items | Validate fails or downgrades quality; `safe-unknown` entries |
| Outdated request list | Re-Request with new scope |
| Operator interprets request as write permission | Request template states read-only only |

### Expected snapshot quality

| Typical outcome | Notes |
|-----------------|-------|
| Level 1–2 | Achievable when request list matches OpenCart spec sections |
| Level 3 | Requires disciplined full checklist completion — rare in first cycle |
| Partial cycles | Normal — new `snapshot_id` for `p2`, `p3` sequences |

---

## Mode 2 — Connected Read Only

**Definition:** Approved read-only connector (future) collects evidence under operator HITL; EAR assembles candidate package from connector output.

### Advantages

- Repeatable path lists and hashes
- Structured `acquisition-log` with channel and scope
- Lower operator toil for repeat audits
- v1 **design target** per [EAR-MODES-v1.md](EAR-MODES-v1.md)

### Limitations

- **Not implemented** at Phase 2B freeze — documentation only
- Requires connector charter, scope limits, and credential handling outside git
- Platform-specific (OpenCart first in Phase 2C roadmap)

### Risks

| Risk | Mitigation (process) |
|------|----------------------|
| Wrong host/path configured | HITL approval of target; access-log records scope |
| Over-collection (PII, full DB rows) | Charter scope limits; Validate rejects policy violations |
| Credential exposure in logs | [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md) |
| False sense of “live truth” | Snapshot remains point-in-time |

### Expected snapshot quality

| Typical outcome | Notes |
|-----------------|-------|
| Level 2–3 | **Expected** when connector scoped correctly — still not guaranteed |
| Level 1 | Valid fallback if connector scope intentionally narrow |
| Validate | Still mandatory; connector output is candidate only |

---

## Mode 3 — Connected Read Write

**Definition:** Connector could modify the external SITE.

### Advantages

- **None in v1 acquisition workflow** — out of scope

### Limitations

- **Forbidden** — not available for Request, Acquire, Validate, Publish, or Consume under EAR v1

### Risks

| Risk | EAR behavior |
|------|----------------|
| Any write request | **Stop** at Request — reject charter |
| Accidental write during Mode 2 impl | Operator escalation; invalidate candidate; incident per mars-survivability patterns |

### Expected snapshot quality

- **N/A** — Mode 3 does not produce EAR v1 snapshots

**Future:** Separate human charter, rollback plan, risk class — Phase 5 evaluation only per [EAR-MODES-v1.md](EAR-MODES-v1.md).

---

## Mode selection (workflow)

| Situation | Recommended mode |
|-----------|------------------|
| No EAR connector | **0** or **1** |
| SITE-001 Run 5 before Phase 2C | **0** or **1** |
| Repeat read-only audits, chartered connector | **2** (when implemented) |
| Deploy, fix, migration | **Not EAR** — separate change process |

Recorded in snapshot metadata as `ear_mode`: `0`, `1`, or `2` only for published v1 packages.

---

## Mode vs lifecycle stage

| Stage | Mode 0 | Mode 1 | Mode 2 (future) |
|-------|--------|--------|-----------------|
| Request | Operator picks mode 0 | Operator picks mode 1 | Operator picks mode 2 + channel |
| Acquire | Operator collects all | Operator fulfills EAR list | Connector reads; EAR assembles |
| Validate+ | Same for all modes | Same | Same |

---

## Cross-references

| Document | Use |
|----------|-----|
| [EAR-ACQUISITION-WORKFLOW-v1.md](EAR-ACQUISITION-WORKFLOW-v1.md) | Full lifecycle |
| [EAR-MODES-v1.md](EAR-MODES-v1.md) | Foundation mode definitions |
| [EAR-CONNECTION-TYPES-v1.md](EAR-CONNECTION-TYPES-v1.md) | Channel families (future) |

---

## SAFE UNKNOWN

- Whether Mode 1 requests are markdown-only or generated by a future helper — not chosen.
- Multi-site concurrent acquisition — undefined.
