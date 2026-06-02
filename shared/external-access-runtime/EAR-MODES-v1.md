# EAR Modes v1

Operational maturity levels for access acquisition. Higher modes increase structure and repeatability; they do **not** imply autonomy.

---

## Mode overview

| Mode | Name | Operator role | EAR role | v1 status |
|------|------|---------------|----------|-----------|
| **0** | Manual | Provides complete files | Validates / wraps snapshot only (conceptual) | Supported semantics |
| **1** | Assisted | Executes collection; EAR guides | Requests **exact** artifacts; checklist-driven | Supported semantics |
| **2** | Connected Read Only | Approves connection | Collects via approved read-only channel (future impl) | **v1 design target** |
| **3** | Connected Read Write | Approves write charter | Would mutate external system | **NOT ALLOWED IN V1** |

---

## Mode 0 — Manual

**Definition:** Operator acquires artifacts outside EAR tooling and delivers files for packaging.

**Flow:**

```
Operator → (WinSCP, panel download, screenshots, exports) → files → EAR or Consumer intake → Snapshot
```

**Characteristics:**

- Lowest automation; highest operator burden
- Valid for SITE-001 until Mode 2 exists
- EAR (or consumer) still applies [EAR-SNAPSHOT-CONTRACT-v1.md](EAR-SNAPSHOT-CONTRACT-v1.md) at wrap time

**Risks:**

- Incomplete manifests
- Inconsistent folder layout
- Screenshots without machine-readable evidence

**Read-only:** Operator discipline — EAR does not grant write capability.

---

## Mode 1 — Assisted

**Definition:** EAR (future helper or runbook) emits a **structured request list**; operator fulfills via any channel.

**Flow:**

```
EAR request manifest → Operator collects → Operator delivers → EAR assembles Snapshot
```

**Characteristics:**

- Reduces “what do you need?” friction (Run 5 DATA-REQUEST pattern generalized)
- Still human-executed per channel
- Aligns with [external-access-patterns](../external-access-patterns/README.md) gates before each channel use

**Risks:**

- Operator skips checklist items → `safe-unknown` grows
- Stale requests if site changes mid-collection

**Read-only:** Explicit in request template — no write steps in v1 assisted packs.

---

## Mode 2 — Connected Read Only (v1 target)

**Definition:** Approved connector performs **read-only** acquisition under operator supervision (HITL).

**Flow:**

```
Operator approves target + channel + scope
  → EAR connector (future) reads
  → EAR assembles Snapshot
  → Operator approves publish
  → Consumer ingests
```

**Characteristics:**

- Repeatable manifests and hashes
- `access-log` records channel and approval
- Designed for OpenCart first (Phase 2 roadmap)

**Risks:**

- Misconfigured connector path (wrong site folder)
- Over-collection (PII, full DB) — scope limits required in charter
- Credential exposure if helper logs secrets — mitigated by security model

**Read-only expectations:**

- No PUT/POST to admin that changes state
- No SQL writes
- No file upload to host
- Stop on any write prompt — operator escalation

**v1 foundation:** Mode 2 is **specified**, not **implemented**.

---

## Mode 3 — Connected Read Write

**Definition:** Connector could modify external system.

**v1 status:** **NOT ALLOWED IN V1**

**Future (Phase 5 evaluation only):**

- Requires separate human charter
- Rollback plan mandatory per [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md)
- Risk class MEDIUM+ or HIGH per mars-survivability patterns
- Never default; never autonomous

---

## Mode selection guide

| Situation | Recommended mode |
|-----------|------------------|
| EAR not implemented yet | **0** or **1** |
| SITE-001 Run 5 resume before Phase 2 | **0** or **1** |
| Repeat audits, same host | **2** (when chartered) |
| Deploy / fix / migration | **Not EAR v1** — consumer change run, not acquisition |

---

## EAR v1 target (explicit)

> **EAR v1 design target: Mode 2 — Connected Read Only.**

Documentation and Phase 2 charter aim at read-only connectors. Modes 0–1 remain valid fallback forever for air-gapped or low-trust environments.

---

## SAFE UNKNOWN

- Whether Mode 1 is a markdown runbook only or a future CLI — implementation not chosen.
- Connector concurrency (multiple sites) — undefined.
