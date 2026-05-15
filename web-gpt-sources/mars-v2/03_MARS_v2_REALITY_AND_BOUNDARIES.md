# MARS v2 — Reality and boundaries

**Status:** **CORE**

---

## Reality audit framework (summary)

**Human-operated** review pass asking whether docs, helpers, and habits still match **actual work** and **maintenance cost**.

| Evaluates | Does not |
|-----------|----------|
| Operational reality, usefulness, friction, drift | Governance certification |
| Human feedback, REPORT traces, registry edits | Runtime validation / telemetry |
| Helper value vs noise (S5/S6) | Automated audit engine |

**Starting artifacts (REPO-ONLY):** `reality-audit-questions.md`, `governance-usefulness-review.md`.

---

## Mythology warnings

**Mythology** = narrative drift: titles and maps that sound like **running systems** without proportional evidence.

| Warning pattern | Corrective action |
|-----------------|-------------------|
| Pilots described as capabilities | Rename: pilot / draft / experimental |
| Concepts named as systems | Add boundaries; cite paths or downgrade |
| Registry row = deployed tool | Link runtime-registry-boundaries |
| Helpers = enforcers | Restate S5 manual posture |
| Governance inflation | Merge, deprecate, narrow SoT |
| Architecture for its own sake | Stabilize before expanding |

**Stabilization-before-expansion:** fix one SoT path before new normative layers.

---

## Forbidden runtime claims (high-risk triggers)

Rewrite if appearing **without** evidence and AGENTS-aligned qualifiers:

- Fully **autonomous** agents/runtime/factory
- **Production orchestrator** / orchestrates production (in-repo)
- **Automatic agent coordination**
- **Self-managing** / **self-healing production** (as factual now)
- **Enforces policy across the repository**
- **Always-on** / **24/7** MARS core
- **Single source of truth (runtime)** erasing governance vs JS vs external split
- **Implements the full control plane** without path proof
- **Daemon** / **worker pool** / **queue consumer** as **shipped MARS**
- **End-to-end verified by MARS** (README “operationally verified” = **human-controlled** work)

**Medium-risk — qualify:** orchestration, registry sync, runtime-ready, validated.

**Allowed when accurate:** documented, contract v0, planned implementation, experimental R1, narrow demo, human-in-the-loop, Web-GPT → Cursor path.

---

## What counts as evidence

| Strong | Weak / not sufficient |
|--------|------------------------|
| Cited file paths and behavior in-repo | Chat agreement alone |
| User-pasted `git status`, command output | Filenames implying runtime |
| Human REPORT with scope | Lifecycle log without map alignment |
| External system's live config (operator-verified) | Sanitized export without freshness note |
| R1 JS for **narrow** demo scope | R1 JS as full product proof |

**Three-way split always applies** when interpreting evidence.

---

## SAFE UNKNOWN (required discipline)

Structured admission:

- **Unknown:** what is not known  
- **Why:** missing file, no command output, stale map  
- **Verify:** paste status, open path, operator check live n8n, etc.  
- **Risk if wrong:** lane mix, false deploy, license commit, etc.

**UNKNOWN** alone is weak for operations; prefer **SAFE UNKNOWN**.

**Must mark SAFE UNKNOWN when:**

- Git state not provided in chat  
- Live integration match to adapter code  
- Validator PASS without human evidence  
- License/commit intent for vendor trees  
- Deployment URLs, secrets, CI names without files  

---

## What must not be promoted to MARS core

| Item | Classification |
|------|----------------|
| Triumph V2 landing workspace (`workspaces/.../src/**`) | **REPO-ONLY** project delivery |
| Website Factory reference case narratives | **OPERATIONAL** example, not production proof |
| MetaBOT n8n graphs | **BOUNDARY ONLY** external system |
| `tools/` pilot scripts | **EXPERIMENTAL** hints |
| Font Awesome Pro vendor tree | **EXCLUDED** from packs; local licensed asset |
| Legacy `seo-content-agent/` | **EXCLUDED** from canonical work |
| Old numbered `web-gpt-sources/` topics | **REPO-ONLY** legacy import |

---

## System boundaries (inside vs outside)

**Inside MARS program/repo:** documentation, contracts, governance, layout placeholders, human operational discipline.

**Outside:** Web-GPT UI, Cursor IDE, model providers, cloud infra, customer data, live n8n — MARS **relates** via integration points; does not own vendor SLAs.

**MARS is NOT:** production runtime, autonomous orchestration, governance enforcement engine.
