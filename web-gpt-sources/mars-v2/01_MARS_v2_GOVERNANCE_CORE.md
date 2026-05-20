# MARS v2 — Governance core

**Status:** **CORE** — summarized from `governance/`; full text remains **REPO-ONLY**.

**Post–Cycle 8:** governance baseline **frozen**; this file is for **maintenance / boundary** tasks — **not** the default first load for delivery chats. Start operational: `00` + `03` + `05` → pack OPERATIONAL-INDEX.

---

## What governance is

Human-maintained **documentation discipline** for boundaries, execution semantics, registries, survivability, tooling limits, operationalization, experiments, and reality audits. **Not** automated enforcement, **not** a policy engine, **not** runtime code.

---

## S0–S7 stack (overview)

| Phase | Focus | Status |
|-------|--------|--------|
| **S0** | Master boundaries, execution model, system boundaries | **CORE** |
| **S1** | Enforcement **cues** (`governance/enforcement/`) — forbidden claims, check catalog | **OPERATIONAL** (human review) |
| **S2** | Registry architecture, **source-of-truth**, identity/naming, external system boundaries | **CORE** |
| **S3** | Operational survivability, onboarding, entropy, operator load, continuity | **OPERATIONAL** |
| **S4** | Execution contracts — task envelope, phases, validation chain, artifact lifecycle | **OPERATIONAL** |
| **S5** | Operational tooling boundaries — helpers assist humans only | **BOUNDARY ONLY** |
| **S6** | Controlled operationalization — maturity levels, interoperability semantics | **PARTIALLY OPERATIONAL** |
| **S7** | Operational experiments — classification, evidence, isolation, lessons | **EXPERIMENTAL** |

**Cross-cutting:** Reality audit framework (qualitative, human-led) — links S1–S7 for drift and usefulness review.

---

## Governance stack purpose

- Keep **claims** aligned with **evidence** in-repo.
- Separate **design vocabulary** from **running systems** (IDE, n8n, cloud, etc.).
- Reduce **registry illusion** (markdown row ≠ deployed tool).
- Support **onboarding** without architecture shock (minimum read set in `onboarding-survivability.md`).

---

## Source-of-truth discipline

**Precedence (in-repo design claims, highest first):**

1. Explicit **governance / contract** for the topic  
2. Specialized **boundary** doc (e.g. MetaBOT integration)  
3. Pack **index** / operational index (navigation; fix conflicts deliberately)  
4. **Legacy imported** `web-gpt-sources/` — input only; reconcile with governance  
5. **Experimental runtime** JS — lowest; illustrative only  

**May be canonical:** `registry/project-registry.md`, `agents/registry.md`, `tools/registry.md`, normative `workflows/*`, designated `*-v0.md` packs — **after human review**.

**Must not silently override governance:** runtime JS, external live configs, casual README lag, chat/tickets, lifecycle log alone.

**Execution truth** for external systems (n8n, SaaS) = **that system’s live config**, not a MARS row by itself.

---

## Registry truth rules (summary)

| Registry kind | Location | Role |
|---------------|----------|------|
| Governance | `agents/registry.md`, `tools/registry.md`, `registry/project-registry.md` | Human-maintained design vocabulary |
| R1 experimental | `mars-runtime/runtime/tool-registry.js` etc. | Demo keys — **not** governance SoT |
| External catalogs | n8n, consoles, MCP | Authoritative **for that system** only |

**Rules:** No auto-sync between JS and markdown registries. MetaBOT ≠ single tool row. Code proves what was typed; it does **not** retroactively change governance rows.

---

## Naming / identity (summary)

- Stable **project_id** in registry rows (e.g. `mars-website-factory`, `metabot-seo-content-agent`).
- **Legacy** packs (e.g. `seo-content-agent/`) — do not extend; use **canonical** MetaBOT pack.
- External entities referenced in docs; **no** implied runtime identity product in-repo.

---

## Anti-drift rules

- Pair high-risk claims with [forbidden-runtime-claims.md](../../governance/enforcement/forbidden-runtime-claims.md) review cues.
- Prefer **documented / planned / experimental R1 / human-operated** over prestige language.
- Stabilize one SoT path before adding parallel normative docs.
- Lifecycle log records **events** — not automatic implementation truth.

---

## Artifact lifecycle (summary)

| Label family | Meaning |
|--------------|---------|
| Draft → review → approved → frozen | Human-operated publication semantics (Factory + governance) |
| Supersede / revision / rollback | Lineage discipline; **no** silent replacement |
| Deprecation | Per `deprecation-and-pruning-semantics.md` — human decision |

Execution contracts (S4) define **task envelope**, **REPORT**, **validation meaning**, and **artifact state** — **semantics only**, not enforced by MARS daemon.

---

## Phase 1 repo posture

- **Documented** — markdown contracts normative for **documentation**, not proof of runnable product.
- **Planned** — full runtime, services, enforcement engines unless path cited.
- **Experimental R1** — narrow `mars-runtime/` demos; see `05_MARS_v2_RUNTIME_BOUNDARY.md`.

*Authoritative detail: `governance/README.md`, `governance/master-build-map.md`, `logs/lifecycle-log.md`.*
