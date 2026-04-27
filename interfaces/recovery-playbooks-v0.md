# MARS — Recovery Playbooks v0

**Status:** documented — approved recovery patterns for MARS governance and contracts (documentation only). No runtime orchestration enforcement, no auto-fix, and no implied tool or filesystem automation in this file.

**Version:** v0. Aligns with [self-heal-v0.md](self-heal-v0.md) (plan-only recovery proposals), [security/approval-gates.md](../security/approval-gates.md) (HITL and gates), [governance/risk-register.md](../governance/risk-register.md), [governance/dependency-map.md](../governance/dependency-map.md) entity `recovery_playbooks`, and [governance/master-build-map.md](../governance/master-build-map.md) Stage 8.5.

---

## 1. Purpose

- Standardise which kinds of recovery (documentation, registry, risk, execution-narrative gaps) are permitted in a MARS Self-Heal or manual maintenance process, and which actions are forbidden or require NEED HUMAN APPROVAL per approval gates.
- Constrain ad hoc “fix everything” plans that skip [risk-register.md](../governance/risk-register.md) rows, [approval-gates.md](../security/approval-gates.md), or [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) when memory or PII is touched.
- Complement (not replace) the v0 recovery type taxonomy in [self-heal-v0.md](self-heal-v0.md) §4 with playbook-level triggers, allowed and forbidden action sets, and canonical system signals (see §2–§3).

**SAFE UNKNOWN:** Exact numeric limits, tool id formats, or runtime event envelope for a given run are not fully specified in-repo for v0 — the plan or maintenance narrative must use playbook discipline plus `SAFE UNKNOWN` (see [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md)) and must append to [risk-register.md](../governance/risk-register.md) or the lifecycle log as needed per [risk-register.md](../governance/risk-register.md) §2.

---

## 2. Relation to Self-Heal (normative)

| Role | Self-Heal v0 | Recovery Playbooks v0 (this file) |
|------|----------------|-----------------------------------|
| **Output** | Proposes an ordered recovery / fix plan (steps, approvals, unknowns); no execution ([self-heal-v0.md](self-heal-v0.md) §1, §3). | Defines playbook types and per-playbook boundaries (allowed and forbidden, approval class, related signals) so Self-Heal steps (or human edits) can be labelled against an approved pattern. |
| **Binding** | Must name a primary recovery type from Self-Heal §4 for each step. | Each playbook in §3 maps naturally to one or more of those types; in doubt, use “risk escalation” and NEED HUMAN APPROVAL (playbook 4). |
| **Honesty** | [AGENTS.md](../AGENTS.md) (no false implementation claim) applies to plans. | Playbooks must not be cited as proof of runtime healing; this is governance and process text only. |

**Summary:** Self-Heal proposes a recovery plan; Recovery Playbooks v0 define approved recovery patterns. A plan is not compliant v0 narrative if it systematically violates the “forbidden actions” of the playbook it claims, unless a human reclassifies the work and updates governance and risk as appropriate.

---

## 3. Playbook types (v0)

### Legend — required approval

- **none** — single-file or trivial doc edits in line with [approval-gates.md](../security/approval-gates.md) (low blast radius; still follow [AGENTS.md](../AGENTS.md) and team norms).
- **governance review** — peer or maintainer read of a small change set (not the same as HITL; product team may still raise to HITL if gates apply).
- **HITL** — at least one condition in [approval-gates.md](../security/approval-gates.md) (filesystem, structure, sensitive, external, PII, et cetera) applies; the plan emits `NEED HUMAN APPROVAL` and does not finalise unapproved effects (design-time and process only in Phase 1).
- **escalation** — routed to [risk-register.md](../governance/risk-register.md) update, [lifecycle log](../logs/lifecycle-log.md), or out-of-band security / compliance; may require HITL in the same pass.

**Related signals** use the vocabulary in [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md) §2.

---

### 1) Documentation inconsistency fix

| Facet | Content |
|--------|---------|
| **Trigger** | Self-Check, Self-Audit, or read-through finds contradictory definitions, stage ordering gaps, or incompatible claims between governance and contracts (excluding registry and path work covered by playbooks 2–3). Use `CONTEXT MIGRATION NEEDED` when the mismatch is broad and may need multi-step work and higher approval. |
| **Allowed actions** | Narrow, single-intent markdown edits; cross-links; terminology alignment; changelog rows in the affected SoT; propose (not execute) a larger restructure if out of playbook scope (emit `STRUCTURE CHANGE` + HITL). |
| **Forbidden actions** | Resolving a contradiction by silently dropping risk register or approval-gate obligations; inventing implementation that does not exist in repo; bulk moves or new top-level areas without HITL per [approval-gates.md](../security/approval-gates.md). |
| **Required approval** | **none** (typical); **HITL** if edits imply structure, external integration, or sensitive/PII paths. |
| **Related signals** | `SAFE UNKNOWN`, `STRUCTURE CHANGE`, `CONTEXT MIGRATION NEEDED`, `NO GIT CHECKPOINT` / `GIT CHECKPOINT NEEDED` per [AGENTS.md](../AGENTS.md) and [web-gpt-sources/04-workflows__git-rules.md](../web-gpt-sources/04-workflows__git-rules.md) (process only). |

**Primary Self-Heal type(s) from** [self-heal-v0.md](self-heal-v0.md) §4: `documentation fix`; `risk mitigation plan` if the register is updated in the same work.

---

### 2) Path / reference correction

| Facet | Content |
|--------|---------|
| **Trigger** | Broken or ambiguous path literals, links, or “SoT” pointers in MARS docs (including default bindings in [introspection-v0.md](introspection-v0.md)); Self-Check or Self-Audit fails with wrong-file evidence. |
| **Allowed actions** | Update markdown links and path literals to repository-root-relative form (or project convention); small line-count fixes; optional maintenance note referencing lifecycle or NO GIT CHECKPOINT. |
| **Forbidden actions** | Widespread moves or renames of governance or registry without HITL; repointing to fictive paths; skipping [risk-register.md](../governance/risk-register.md) or [dependency-map.md](../governance/dependency-map.md) when a path is the public SoT for a risk (see playbook 4). |
| **Required approval** | **none** for small fixes; **governance review** for table-wide or cross-root repairs; **HITL** for moves, new top-level areas, or re-homing SoT. |
| **Related signals** | `UNKNOWN`, `SAFE UNKNOWN`, `STRUCTURE CHANGE`. |

**Primary Self-Heal type(s):** `documentation fix`; `dependency correction` if [dependency-map.md](../governance/dependency-map.md) is edited.

---

### 3) Registry repair

| Facet | Content |
|--------|---------|
| **Trigger** | Missing, stale, or duplicate rows in [project-registry.md](../registry/project-registry.md) or [agents/registry.md](../agents/registry.md) (or equivalent in-scope catalogues per governance); Self-Check or introspection emits `UNKNOWN` or `FAIL` for id binding. |
| **Allowed actions** | Propose (Self-Heal) or apply (human) edits that conform to registry row schema, passport/card rules, and [agent-card-template.md](../agents/agent-card-template.md) (documentation). Append [lifecycle-log.md](../logs/lifecycle-log.md) when the governing file requires. No shadow registries. |
| **Forbidden actions** | Deleting or moving registry *files* without explicit user instruction per [AGENTS.md](../AGENTS.md); bypassing HITL for sensitive PII per [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md); fictional ids or unapproved integration stubs (→ RISK and [risk-register.md](../governance/risk-register.md) §7.3). |
| **Required approval** | **governance review** (typical); **HITL** when agent CRUD-shaped, PII, or integration identity is affected per [approval-gates.md](../security/approval-gates.md). |
| **Related signals** | `UNKNOWN`, `NEED HUMAN APPROVAL`, `STRUCTURE CHANGE` when registry, factory, and orchestrator must co-align. |

**Primary Self-Heal type(s):** `registry update`; `dependency correction` if [dependency-map.md](../governance/dependency-map.md) or cards need edges.

---

### 4) Risk escalation

| Facet | Content |
|--------|---------|
| **Trigger** | New or worsening hazard (integration, runtime, data, governance, security); `SECURITY RISK` or [risk-register.md](../governance/risk-register.md) §2 / §7 (new external integration, runtime implementation claim, et cetera); or Self-Heal cannot converge a plan without a human or compliance decision. |
| **Allowed actions** | Create or update a row in [risk-register.md](../governance/risk-register.md) (fields per §5 there); cross-link [dependency-map.md](../governance/dependency-map.md) and [approval-gates.md](../security/approval-gates.md) as policy requires; propose (not execute) [lifecycle-log.md](../logs/lifecycle-log.md) when [master-build-map.md](../governance/master-build-map.md) authority requires; add `SAFE UNKNOWN` and `NEED HUMAN APPROVAL` in narrative as needed. |
| **Forbidden actions** | Closing or deleting risk rows without rationale, successor `risk_id`, or `obsolete` handling per [risk-register.md](../governance/risk-register.md) §3; bypassing [approval-gates.md](../security/approval-gates.md) or required legal review (e.g. RF / 152-ФЗ and other norms per RISK-V0-0007 — SAFE UNKNOWN for formal legal sign-off in-repo). |
| **Required approval** | **escalation** (always in scope of this playbook); **HITL** for security or compliance posture change; owner may be `TBD` per [risk-register.md](../governance/risk-register.md). |
| **Related signals** | `SECURITY RISK`, `NEED HUMAN APPROVAL`, `SAFE UNKNOWN` (residuals on the hazard). |

**Primary Self-Heal type(s):** `risk mitigation plan`; `escalation` (NEED HUMAN APPROVAL).

---

### 5) Memory write correction

| Facet | Content |
|--------|---------|
| **Trigger** | Durable knowledge / RAG (design) is wrong, forbidden, or infeasible per [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) or RISK-V0-0007 / 0011; or checkpoint / resume and memory narrative are mismatched. |
| **Allowed actions** | Propose (Self-Heal) or author (human) edits to policy, registry (project binding), and dependency-map edges; append governance or lifecycle per memory policy §7; re-run Self-Check or Self-Audit in narrative only. |
| **Forbidden actions** | Claiming that memory enforcement or an implemented store exists (see [AGENTS.md](../AGENTS.md) and RISK-V0-0005); durable PII without HITL per memory policy §3b; silent data wipe (must be governed; logged if required by policy or lifecycle rules). |
| **Required approval** | **HITL** for PII, retention, or schema-affecting durable knowledge per [approval-gates.md](../security/approval-gates.md) and [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md); **governance review** for low-sensitivity narrative only. |
| **Related signals** | `NEED HUMAN APPROVAL`, `CONTEXT MIGRATION NEEDED`, `SECURITY RISK`, `SAFE UNKNOWN` (backend, store, dedup mechanisms). |

**Primary Self-Heal type(s):** `permission correction`, `documentation fix`, `risk mitigation plan` (risk rows), `registry update` (project or agent as applicable).

---

### 6) Execution failure recovery

| Facet | Content |
|--------|---------|
| **Trigger** | Planned (documentation) response to run / bridge / store–shaped issues: inconsistent [runtime-state-store-v0.md](../storage/runtime-state-store-v0.md) narrative; contradiction between [checkpoint-resume-protocol-v0.md](../storage/checkpoint-resume-protocol-v0.md) and [failure-model-v0.md](../workflows/failure-model-v0.md); or resume / idempotency after `errors` on [execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) (design-time and future incident narrative). |
| **Allowed actions** | Reconcile contracts in markdown; clarify `SAFE UNKNOWN` (no implementation backend in repo in Phase 1); propose HITL-gated re-run or park per [state-model.md](../governance/state-model.md) and [task-contract-v0.md](../workflows/task-contract-v0.md) (documentation). Propose (not execute) lifecycle and risk register updates when RISK-V0-0008, 0009, 0010, or new rows warrant. |
| **Forbidden actions** | Implying a live orchestrator without in-repo evidence; unbounded or infinite retries; continuing blindly on `SECURITY RISK` per [failure-model-v0.md](../workflows/failure-model-v0.md) and [governance/system-signals-dictionary.md](../governance/system-signals-dictionary.md); duplicating an irreversible side effect without HITL per [approval-gates.md](../security/approval-gates.md) and the failure model. |
| **Required approval** | **HITL** for gated RAG, PII, or external side effects, and for re-play of suspected duplicate actions; **governance review** for small doc-only surgical fixes. |
| **Related signals** | `SAFE UNKNOWN`, `STRUCTURE CHANGE` (replan after invariant break), `SECURITY RISK` (retry and integrity), `NEED HUMAN APPROVAL` (resume/duplicate suspected). |

**Primary Self-Heal type(s):** `documentation fix`, `dependency correction`, `risk mitigation plan`, `escalation` (NEED HUMAN APPROVAL and retry class).

---

### 7) Security incident escalation

| Facet | Content |
|--------|---------|
| **Trigger** | Confirmed or suspected `SECURITY RISK` (injection, secret in an artefact, unauthorised write, policy bypass, or live credential exposure in a future live incident) — or risk / audit work mandates stopping work until a human and possibly out-of-band response (legal, DPA, RF/152-ФЗ per RISK-V0-0007 and [memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md)). |
| **Allowed actions** | Halt (process-level) new writes that broaden blast radius; document what is `SAFE UNKNOWN` (evidence, scope, timestamps, what was touched); update or create [risk-register.md](../governance/risk-register.md) rows; append [lifecycle-log.md](../logs/lifecycle-log.md) if governance says so; emit `NEED HUMAN APPROVAL` and the security narrative for out-of-band as needed. This repository’s v0 scope is governance and plan text — not a substitute for network isolation, IR tooling, or KMS; org SOPs are SAFE UNKNOWN here. |
| **Forbidden actions** | Pretending the MARS v0 doc pack is a SOC, SIEM, or IR system; continuing automation (when it exists) on the affected track without HITL; deleting audit-relevant lifecycle or risk rows (only `obsolete` with successor per [risk-register.md](../governance/risk-register.md) §3). |
| **Required approval** | **HITL** minimum; escalation to compliance, security, or legal as risk and [approval-gates.md](../security/approval-gates.md) require; exact RACI in-repo is SAFE UNKNOWN. |
| **Related signals** | `SECURITY RISK`, `NEED HUMAN APPROVAL`, `UNKNOWN` (forensics not yet bound), `SAFE UNKNOWN` (external org response). |

**Primary Self-Heal type(s):** `escalation` (NEED HUMAN APPROVAL), `risk mitigation plan`, optional `permission correction` (policy text).

---

## 4. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-27 | Recovery Playbooks v0 — purpose, Self-Heal relation, seven playbook types (trigger, allow/forbid, approval, signals). No enforcement. Does not add or change `tools/` or `models/`. |

---

*End of MARS Recovery Playbooks v0.*
