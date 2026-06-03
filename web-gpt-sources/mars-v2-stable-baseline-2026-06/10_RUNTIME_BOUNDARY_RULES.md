# MARS — Runtime boundary rules (Stable Baseline 2026-06)

**Status:** **CORE** · **BOUNDARY ONLY**  
**Repo SoT:** `mars-runtime/README.md`, `governance/enforcement/forbidden-runtime-claims.md`, `governance/runtime-registry-boundaries.md`

---

## Hard line

| MARS is | MARS is not |
|---------|-------------|
| v0 **contracts** under `mars-runtime/*.md` | Production multi-agent runtime |
| Optional **R1** human-invoked `node` demos | Autonomous orchestration |
| Honesty boundary for future integration | Deployed control plane or fleet narrative |
| EAR R1 **skeleton** under `projects/ear-runtime/` | Live SFTP connector or production acquisition |

**Do not upload `mars-runtime/**/*.js` to Web-GPT** as implementation proof.

---

## Forbidden claims (unless path proof in session)

- MARS runs 24/7 as orchestrator  
- Queues, schedulers, worker pools as **shipped MARS**  
- Registry JavaScript demo keys = production tool registry  
- Execution Bridge = deployed bridge **instance**  
- MetaBOT / Factory / ORCA automated by MARS core  
- File exists → fleet operational  

---

## R1 experimental scope

| Fact | Status |
|------|--------|
| Entry | Human-invoked scripts only |
| Typical use | Narrow handoff (e.g. n8n webhook adapter) |
| Registry JS | Demo/lab keys — `tools/registry.md` remains SoT for tool rows |
| Missing | Queue consumer, orchestrator host, concurrency product |

**Lane:** Runtime — explicit charter; REPORT with paths; no production claims.

---

## Contracts vs code

| Artefact | Classification |
|----------|----------------|
| `execution-bridge-v0.md`, queue/orchestrator/lifecycle contracts | **Conceptual / documented** |
| `adapters/`, `runtime/*.js` | **Experimental** — boundary context only |
| Control plane / workflow engine product | **Future** — not evidenced as shipped |

---

## External systems boundary

| System | Execution truth |
|--------|-----------------|
| MetaBOT | Live **n8n** (external) |
| WordPress / Beget | **WPilot** external lane |
| OpenCart sites | **OCPilot** external lane |
| MIG v0.1 n8n export | In-repo export ≠ production deployment proof |

MARS holds **contracts and operator discipline** — not external SLAs or live graph ownership.

---

## EAR Runtime vs EAR Architecture

| Layer | Path | Role |
|-------|------|------|
| **EAR Architecture** (frozen) | `shared/external-access-runtime/` | Normative patterns |
| **EAR Runtime** (engineering) | `projects/ear-runtime/` | Implements chartered helpers — skeleton at baseline |

Runtime code **must not** silently amend architecture.

---

## When touching runtime paths

Only if **all** apply:

1. Lane = **Runtime** (or explicit task charter)  
2. Operator approved scope  
3. REPORT lists exact paths touched  
4. No uplift to governance SoT or registry deployment fiction  

Otherwise route work through **operational packs** and human execution loop.

---

## Web-GPT discipline

- Cite `mars-runtime/*.md` for **boundaries**, not `.js` as proof  
- State **SAFE UNKNOWN** for adapter parity with external workflows  
- Separate **planned-implementation** language from **operationally verified** human repo work  

---

*Runtime boundary — Stable Baseline 2026-06 — mythology-pressure zone; honesty mandatory.*
