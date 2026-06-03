# Incoming Deep Review v2

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2 Discovery  
**Mode:** Investigation + classification only (**no moves**, **no deletes**, **no archive**)  
**Baseline:** MARS v2 Stable Baseline 2026-06 (`45518bb` — `incoming/**` **excluded** from checkpoint)  
**Prior evidence:** Census AC-10, A-011/A-012/A-030; Wave 1 W1-023/W1-024

---

## Executive determination

| Question | Answer |
|----------|--------|
| Actual usage | **Multi-program intake staging** — MIG operational drop zone; ORCA/MetaBOT/Factory **historical or pending triage** drops |
| Intended usage | **Quarantine / transport** — external material ≠ trusted SoT until promoted |
| Placement recommendation | **C) Hybrid model** — keep **lane-specific intake contracts** in Active Brain; move **stale bulk** to Storage/Cold Brain after triage (operator-gated, not executed here) |

**Not:** a registered program, registry row, or autonomous pipeline.

---

## 1. Current contents (verified 2026-06-03)

| Subfolder | Files | Role |
|-----------|-------|------|
| `incoming/mig/` | 11 | **Operational** — Task File intake + registry (`request-index.json`) |
| `incoming/orca-triumph-raw-pack/` | 17 | **Historical intake** — normalized into `projects/orca/ppc/triumph-manipulator/` (2026-05-20) |
| `incoming/metabot/seo-writer-workflows/` | 3 | **Reference export** — n8n JSON (Beta v14 Admin/Intake/Worker) |
| `incoming/mars-bridge/` | 1 | **Stub** — `mars-bridge-workflow.json` (`mode: bridge_stub`) |
| `incoming/website-factory-legal-cleanup/` | 8 | **Pending triage** — docx + extracted txt (Triumph legal pilot) |

**Total:** ~40 files under repo-root `incoming/` (excluding `projects/ocpilot/incoming/` — separate scoped zone).

### 1.1 MIG drop zone detail

| Path | State |
|------|-------|
| `requests/` | Example + `.gitkeep` |
| `processing/`, `failed/`, `archive/` | Structure + `.gitkeep` |
| `completed/` | Smoke test artefacts (`req-20260601-smoke01*`) |
| `registry/request-index.json` | Request ↔ session linkage |

**Processor:** `projects/mig/tools/run-task-file-adapter.ps1` — human-invoked, documented in `incoming/mig/README.md`.

### 1.2 Parallel: `projects/ocpilot/incoming/`

| Property | Value |
|----------|-------|
| Scope | OCPilot-only quarantine (`baselines/`, `project-sites/`) |
| Pattern | Same **Incoming ≠ Trusted** principle |
| Baseline ZIPs | Often gitignored bulk — external storage registry |

**Important:** Root `incoming/` is **ecosystem-wide staging**; OCPilot incoming is **program-scoped** — do not collapse paths in policy.

---

## 2. Intended usage (documented)

| Program / doc | Intended pattern |
|---------------|------------------|
| ORCA `orca-universal-intake-architecture-v0.md` | `incoming/orca/<project-id>-raw-pack/` → normalize to pack |
| ORCA principles | `incoming/` + `raw-inventory/` = traceability, not truth |
| MIG contracts | `incoming/mig/` = primary Task File transport |
| OCPilot `incoming/README.md` | Quarantine until intake report |
| Stable baseline release | `incoming/**` = **staging materials**, excluded from checkpoint |
| Active Brain doc | Git-tracked working intelligence includes narrow experimental paths |

**Lifecycle (conceptual):**

```text
External / operator drop
        → incoming/{program-subfolder}/  (untrusted)
        → human intake / adapter / normalization
        → projects/{program}/ or workspaces/  (operational SoT)
        → optional: archive raw pack to Cold Brain after promotion
```

---

## 3. Actual usage vs intent

| Subfolder | Intent match | Notes |
|-----------|--------------|-------|
| `mig/` | **High** | Active structure; smoke completed; registry in use |
| `orca-triumph-raw-pack/` | **Stale** | Normalized copy exists in ORCA pack; raw pack **retained** — archive candidate AC-10 |
| `metabot/` | **Uncertain** | Live n8n may differ — export freshness **SAFE UNKNOWN** |
| `mars-bridge/` | **Stub only** | No production bridge; MIG cites future transport |
| `website-factory-legal-cleanup/` | **Pending** | Referenced from Triumph legal pilot; promote vs keep intake — A-030 |

**Drift:** Root `incoming/` lacks a **single governance README** at `incoming/README.md` (unlike `incoming/mig/README.md` and OCPilot incoming). Topology index does not list `incoming/` as first-class node.

---

## 4. Placement options analysis

### A) Remain inside Active Brain (`C:\AI MARS`)

| Pros | Cons |
|------|------|
| Git-visible staging for agents and operators | Clutters working tree; baseline **excludes** incoming from checkpoint |
| Co-located with `projects/mig` adapter paths | Conflicts with “Active Brain = SoT” mental model for **untrusted** blobs |
| Proven for MIG operational MVP | Large raw packs (legal docx, xlsx) inflate repo |

### B) Move toward Storage Layer (`C:\AI MARS STORAGE\...`)

| Pros | Cons |
|------|------|
| Aligns with Cold Brain / bulk semantics | Breaks relative paths in contracts (`incoming/mig/...`) |
| Keeps Active Brain lean | Requires path migration + doc sweep — **not done in Wave 2** |
| Good for retired raw packs (orca-triumph) | Active MIG drop zone needs **low-friction** local path for adapter |

### C) Hybrid model (recommended)

| Layer | What stays | What moves (future, operator) |
|-------|------------|-------------------------------|
| **Active Brain** | `incoming/mig/` (operational), `incoming/mars-bridge/` (stub), **small** active drops | — |
| **Active Brain → program scope** | Promoted material only in `projects/*` | — |
| **Storage / Cold Brain** | Retired raw packs, superseded exports, large legal ZIPs after promotion | `orca-triumph-raw-pack/`, stale metabot exports **after** triage sign-off |
| **Documentation** | Add `incoming/README.md` ecosystem charter | — |

---

## 5. Overlap with other systems

| System | Overlap |
|--------|---------|
| **Archive** (`archive/`, `projects/*/archive/`) | Incoming = **pre-promotion** quarantine; archive = **post-decision** historical |
| **IdeaBox** | No — Incoming is **external artefacts**, not session ideas |
| **Registry** | Incoming drops are **not** `project_id` rows |
| **Knowledge Center** | No git mirror of incoming; KC may **link** to intake SOP |
| **Lifecycle log** | No events for intake promotions — **gap** optional for operator |
| **GitGuard** | Protected zones — destructive cleanup of `incoming/` requires human policy |

---

## 6. Recommended classification (Wave 2 — no execution)

| Action | Detail |
|--------|--------|
| **KEEP** | `incoming/mig/` operational drop zone in Active Brain |
| **KEEP** | `incoming/mars-bridge/` stub until charter supersedes |
| **INVESTIGATE** | Per-subfolder triage SOP (promote / archive / delete) |
| **ARCHIVE CANDIDATE** (identification) | `orca-triumph-raw-pack/` after operator confirms ORCA pack SoT |
| **INVESTIGATE** | `website-factory-legal-cleanup/` → Factory legal registry vs intake-only |
| **INVESTIGATE** | `metabot/` export sync vs live n8n |
| **REDEFINE** | Author root `incoming/README.md` + link from ecosystem-topology-index |
| **Do not** | Move folders in Wave 2 Discovery |

---

## 7. Proposed operator decisions (deferred)

| ID | Question |
|----|----------|
| N-01 | Adopt hybrid placement policy? |
| N-02 | Triage orca-triumph-raw-pack to Cold Brain? |
| N-03 | Promote legal-cleanup to `projects/mars-website-factory/` legal registry? |
| N-04 | Single ecosystem incoming README — who maintains? |

---

## 8. SAFE UNKNOWN

| Topic | Note |
|-------|------|
| Live n8n workflow parity with `incoming/metabot/*.json` | Requires n8n UI |
| Git tracking status of docx/xlsx (LFS vs plain) | Not audited |
| Operator copies of incoming on other drives | Out of repo |
| Whether smoke MIG requests should remain in `completed/` or archive | Policy TBD |

---

*Incoming Deep Review v2 — Wave 2 Discovery evidence only.*
