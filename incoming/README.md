# MARS — Ecosystem intake zone (`incoming/`)

**Status:** **documented** — ecosystem-level intake policy (Wave 2A; hybrid model Wave 2B, 2026-06-03).  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`incoming/**` excluded from checkpoint by design).

---

## Hybrid placement model (Wave 2B)

| Layer | Location | Contents |
|-------|----------|----------|
| **Active Incoming** | **Active Brain** — repo-root `incoming/` | Operational drops (`incoming/mig/`), active stubs, small pending triage |
| **Historical Bulk** | **Storage Layer** — `C:\MARS Phenix\AI MARS STORAGE\…`, Cold Brain | Retired raw packs, superseded exports, large archives **after** operator triage sign-off |

**No folder moves in Wave 2B** — hybrid model is **documentation only**. See [logs/cleanup/actions/incoming-hybrid-alignment-v1.md](../logs/cleanup/actions/incoming-hybrid-alignment-v1.md).

---

## What `incoming/` is

`incoming/` at the repository root is a **temporary intake zone** for **untrusted external material** and **program-specific transport drops** before human promotion into canonical project packs, workspaces, or governance SoT.

| Property | Meaning |
|----------|---------|
| **Trust** | Contents are **not** authoritative until reviewed, normalized, and promoted |
| **Lifecycle** | Drop → triage → promote → optional retire raw copy |
| **Scope** | Ecosystem-wide staging; complements **program-scoped** zones such as `projects/ocpilot/incoming/` |

**Examples (observed):**

- `incoming/mig/` — operational Task File drop zone ([mig/README.md](mig/README.md))
- `incoming/orca-triumph-raw-pack/` — historical ORCA raw intake (normalized 2026-05-20)
- `incoming/metabot/`, `incoming/mars-bridge/`, `incoming/website-factory-legal-cleanup/` — reference exports, stubs, or pending triage

---

## What `incoming/` is not

| Misread | Correction |
|---------|------------|
| **Long-term storage** | Not Cold Brain, not `archive/`, not Knowledge Center |
| **Archive** | Retired bulk belongs under `archive/` or operator storage **after** triage — not by default in `incoming/` |
| **Registry** | No `project_id` rows; folder names do not register programs |
| **Runtime / pipeline** | No daemon, queue, or autonomous processor at repo root |
| **SoT** | Operational truth lives under `projects/`, `registry/`, `governance/`, and scoped workspaces |

---

## Expected lifecycle

```text
External artefact / operator drop
        → incoming/{subfolder}/     (quarantine — untrusted)
        → human intake / adapter / normalization
        → projects/{program}/ · workspaces/ · governance/   (promoted SoT)
        → optional: archive or remove stale drop (operator-gated)
```

**Discipline:**

1. Prefer **program charters** (ORCA intake architecture, MIG contracts, OCPilot incoming README) for subfolder rules.
2. **Do not** treat checkpoint exclusion as permission to accumulate unbounded stale drops.
3. Material registry or governance changes after promotion may warrant a row in [logs/lifecycle-log.md](../logs/lifecycle-log.md) — same-session append when applicable.

---

## Promote

**Promote** means a human (or human-supervised agent) moves or rewrites content into a **canonical** path with explicit scope:

| Target | When |
|--------|------|
| `projects/{program}/` | Pack docs, contracts, normalized exports |
| `workspaces/` | Build artefacts tied to a registered workspace |
| `governance/` | Cross-cutting policy (rare; operator-gated) |

Promotion requires **evidence**: intake report, normalization log, or task REPORT — not silent copy.

---

## Archive

**Archive** (of intake residue) is **operator-gated** and **out of scope** for default agent cleanup:

- After promotion, raw packs may be copied to `archive/`, Cold Brain storage, or removed from `incoming/` per program policy.
- Stale folders (e.g. post-normalization raw packs) are **archive candidates** — see `logs/cleanup/archive-candidates/` and program triage notes.

`incoming/` itself is **not** an archive tree.

---

## Delete

**Delete** from `incoming/` is **human-only** after triage confirms SoT elsewhere. Agents must **not** delete intake files unless the operator explicitly instructs.

---

## Related surfaces (navigation only)

| Surface | Role |
|---------|------|
| [continuity/](../continuity/README.md) (IdeaBox) | Trusted **session** capture — not external quarantine |
| [logs/lifecycle-log.md](../logs/lifecycle-log.md) | Governance **events** after material registry/policy change |
| [registry/project-registry.md](../registry/project-registry.md) | Current project identity SoT |
| [logs/cleanup/](../logs/cleanup/README.md) | Ecosystem audit evidence — not intake SoT |
| [projects/mars-survivability/](../projects/mars-survivability/README.md) | Survivability / GitGuard advisory — protects zones; does not process drops |

**Evidence:** [logs/cleanup/actions/incoming-readme-v1.md](../logs/cleanup/actions/incoming-readme-v1.md)

---

*Ecosystem intake policy — documentation only; no runtime.*
