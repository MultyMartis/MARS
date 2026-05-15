# MARS v2 — Runtime boundary (R1)

**Status:** **BOUNDARY ONLY** · **EXPERIMENTAL** (narrow JS) · **NOT** production runtime

---

## Hard classification

| MARS is | MARS is not |
|---------|-------------|
| Documentation-first program with v0 **contracts** under `mars-runtime/*.md` | Production multi-agent runtime |
| Optional **R1** manual `node` demos (task → bridge → adapter → webhook) | Autonomous orchestration |
| Honesty boundary for future DevOps/Runtime layer | Control plane implementation |
| Evidence of **experiments typed** in-tree | Proof of fleet-wide operational system |

**Uploading `mars-runtime/**/*.js` to Web-GPT as “source pack proof” is forbidden** — this pack states boundaries only.

---

## R1 — what exists (if cited from repo)

| Property | Fact |
|----------|------|
| Entry | Human-invoked scripts only |
| Scope | Narrow handoff to operator-configured external URLs (e.g. n8n webhook) |
| Registry JS | Demo lookup — **not** `tools/registry.md` SoT |
| Missing | Queue, orchestrator, concurrency manager, memory subsystem, model routing, long-running host |

**File exists** ✅ · **Fleet-wide MARS runtime operational** ❌ without separate evidence.

---

## Contracts vs code (mars-runtime/)

| Artefact | Status |
|----------|--------|
| `execution-bridge-v0.md`, queue/orchestrator/context/lifecycle contracts | **CORE** documentation |
| `architecture-map.md` | Folder → layer **glossary**; not implementation inventory |
| `adapters/`, `runtime/*.js` | **EXPERIMENTAL**; boundary context only |

Phase 1: contracts are **primary** in-tree runtime-facing artefacts; R1 does **not** complete planned full runtime.

---

## Execution Bridge

**BOUNDARY ONLY** — conceptual translation between MARS task semantics and runners (Cursor, n8n, future API). Canonical contract: `mars-runtime/execution-bridge-v0.md`. No claim that a bridge **instance** is deployed as MARS product.

---

## Control plane and orchestration

| Component | In-repo today |
|-----------|---------------|
| Control Plane contracts (`control-plane/`) | **Documented** target |
| Workflow engine / scheduler / queue consumer | **Not** shipped MARS |
| Autonomous multi-agent dispatch | **Planned** |

Do not conflate **workflow map narrative** with a running engine.

---

## Registry confusion (prevent illusion)

Three registries — see `01`:

1. Governance markdown registries  
2. R1 JS convenience keys  
3. External live catalogs (n8n, etc.)  

Runtime code **never** silently overrides governance rows.

---

## Related projects (not R1 proof)

| Pack | Runtime owner |
|------|---------------|
| MetaBOT SEO Content Agent | **External** n8n — canonical `projects/metabot-seo-content-agent/` |
| Website Factory | **Human + Cursor** methodology — no in-pack engine |
| Legacy `seo-content-agent/` | **EXCLUDED** — do not extend |

---

## What operators may do (explicit runtime tasks only)

When task charter says **R1 experiment**:

- Run documented manual scripts in controlled environment  
- REPORT with paths, config boundaries, no production claims  
- Keep lane separate from Factory delivery and governance rewrites  

Otherwise treat `mars-runtime/` as **read-only boundary context** for planning.

---

## SAFE UNKNOWN

- Production deployment topology for any future MARS runtime.  
- Whether team's program adopts n8n as standard bridge consumer.  
- Live parity between adapter code and external workflow graphs.
