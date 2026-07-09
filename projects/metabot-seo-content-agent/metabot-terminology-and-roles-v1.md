# MetaBOT — Terminology and Roles v1

**Status:** **documented** — working terminology foundation pack.  
**Version:** v1 (Foundation Pack)  
**Classification key:** every term uses one or more of: **REPO_EVIDENCED** · **OPERATOR_CLARIFICATION** · **PLANNED** · **CONCEPTUAL** · **HISTORICAL** · **SAFE UNKNOWN**

**Honesty note:** The repository today treats **MetaBOT** mostly as **MetaBOT — SEO Content Agent**. The operator intends **MetaBOT** as a broader external automation/bot contour. This file documents that working frame **without** claiming the broader umbrella is fully implemented.

---

## Terms

### MetaBOT

| Field | Value |
|-------|-------|
| **Definition** | Working name for an **external automation / bot contour** around n8n workflows, Telegram bots, API bots, webhook automations, cloud actions, external provider calls, and human-supervised operational workflows. |
| **Status** | **OPERATOR_CLARIFICATION** (broader contour) + **REPO_EVIDENCED** (currently documented primarily as SEO Content Agent) |
| **Owner / boundary** | External operators and n8n-hosted workflows; MARS holds documentation and sanitized artifacts only. |
| **What it is not** | MARS autonomous runtime; MARS orchestrator; hidden agent fleet; self-deploying system; replacement for n8n; replacement for MIG / ORCA / OPS / ATLAS. |
| **Evidence** | [README.md](README.md), [integration-boundary.md](integration-boundary.md), [governance/external-system-boundaries.md](../../governance/external-system-boundaries.md) |
| **SAFE UNKNOWN** | Whether future non-SEO MetaBOT products will share one n8n project, one credential store, or one governance row. |

---

### MetaBOT Layer / contour

| Field | Value |
|-------|-------|
| **Definition** | Architectural label for the **ecosystem slice** where external bot/automation products live — adjacent to but separate from MARS core runtime, MIG acquisition, ORCA interpretation, and OPS back-office. |
| **Status** | **OPERATOR_CLARIFICATION** + **CONCEPTUAL** |
| **Owner / boundary** | Cross-cutting documentation boundary; execution stays in external systems. |
| **What it is not** | A deployable MARS module; a registry engine; a single n8n folder name requirement. |
| **Evidence** | This foundation pack; [governance/external-systems-relationship-map-v0.md](../../governance/external-systems-relationship-map-v0.md) |
| **SAFE UNKNOWN** | Formal registry entry for “MetaBOT layer” separate from `metabot-seo-content-agent`. |

---

### MetaBOT Product

| Field | Value |
|-------|-------|
| **Definition** | A concrete external operational product under the MetaBOT contour — e.g. a Telegram-facing SEO writer with its own workflow family and operator runbooks. |
| **Status** | **REPO_EVIDENCED** (one current product) + **PLANNED** (future candidates) |
| **Owner / boundary** | Product operators; live graphs and credentials in n8n / provider consoles. |
| **What it is not** | Every n8n workflow in the ecosystem (MIG has its own product boundary). |
| **Evidence** | [registry/project-registry.md](../../registry/project-registry.md) row `metabot-seo-content-agent` |
| **SAFE UNKNOWN** | Full inventory of live MetaBOT-compatible products outside SEO Agent. |

---

### MetaBOT SEO Agent

| Field | Value |
|-------|-------|
| **Definition** | The **current concrete MetaBOT product**: multi-workflow SEO content system (Intake / Worker / Admin; File Export planned) for SEO briefs, ТЗ, articles, landing text, QA, and factcheck. |
| **Status** | **REPO_EVIDENCED** (documentation) + **OPERATOR_CLARIFICATION** (production usage, Telegram handle) |
| **Owner / boundary** | External n8n runtime; canonical docs in `projects/metabot-seo-content-agent/`. |
| **What it is not** | MARS-in-repo executable; single-webhook “tool”; MIG or ORCA replacement. |
| **Evidence** | [README.md](README.md), [mega-map.md](mega-map.md), [workflow-map.md](workflow-map.md) |
| **SAFE UNKNOWN** | Live deployment topology; exact model list in OpenRouter nodes. |

**Canonical `project_id`:** `metabot-seo-content-agent` — **do not rename**.

---

### SEO Content Agent (legacy / current naming)

| Field | Value |
|-------|-------|
| **Definition** | **Historical and current** product name variant: **MetaBOT — SEO Content Agent**. Same product as MetaBOT SEO Agent; used in registry, governance, and most repo docs. |
| **Status** | **REPO_EVIDENCED** + **HISTORICAL** (folder `seo-content-agent` legacy pack) |
| **Owner / boundary** | Canonical narrative: this folder. Legacy pack: `projects/seo-content-agent/` — **do not extend**. |
| **What it is not** | A separate active product ID; a reason to fork documentation. |
| **Evidence** | [README.md](README.md) §Canonical project folder; [governance/external-system-boundaries.md](../../governance/external-system-boundaries.md) |
| **SAFE UNKNOWN** | Operator preference timeline for display name “SEO Agent” vs “SEO Content Agent”. |

---

### MetaBOT Developer

| Field | Value |
|-------|-------|
| **Definition** | **Planned / conceptual** engineering role or sub-contour: MARS-assisted, human-supervised design of n8n workflow schemes for MetaBOT products and related automation. |
| **Status** | **PLANNED** / **CONCEPTUAL** |
| **Owner / boundary** | Human operator + MARS documentation sessions; **no** autonomous runtime. |
| **What it is not** | Autonomous developer; unattended deployer; production orchestrator; credential owner; direct executor without approval. |
| **Evidence** | [metabot-developer-concept-v1.md](metabot-developer-concept-v1.md) |
| **SAFE UNKNOWN** | Whether it becomes a named agent card, skill, or remains prose-only discipline. |

---

### MetaBOT-compatible workflow

| Field | Value |
|-------|-------|
| **Definition** | An n8n workflow (or workflow family) that fits MetaBOT product patterns: external trigger (often Telegram), optional Sheets state, webhook handoff between Intake/Worker/Admin-style layers, human-supervised ops, credentials outside MARS repo. |
| **Status** | **REPO_EVIDENCED** (pattern description) + **CONCEPTUAL** (compatibility label) |
| **Owner / boundary** | n8n operators; pattern reference from SEO Agent and MIG design study. |
| **What it is not** | Any workflow hosted on n8n regardless of domain; MIG research workflows (separate namespaced paths). |
| **Evidence** | [workflow-map.md](workflow-map.md); [projects/mig/reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../mig/reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) |
| **SAFE UNKNOWN** | Formal checklist/certification for “compatible”. |

---

### MetaBOT n8n Project

| Field | Value |
|-------|-------|
| **Definition** | Operational grouping in a **live n8n instance** for MetaBOT product workflows (graphs, credentials, webhooks) — distinct from MIG `mig/*` paths per MIG design. |
| **Status** | **OPERATOR_CLARIFICATION** + **SAFE UNKNOWN** |
| **Owner / boundary** | n8n operator; not MARS repo. |
| **What it is not** | A folder in `X:\AI MARS` that executes workflows. |
| **Evidence** | MIG design report (shared host, separate webhook namespaces) |
| **SAFE UNKNOWN** | Exact n8n project/workspace name; host URL; workflow IDs. |

---

### MetaBOT Bridge

| Field | Value |
|-------|-------|
| **Definition** | Documentation-level or snippet-level **handoff** between MARS-facing contracts and MetaBOT entrypoints (e.g. webhook payload shaping, bridge Code node). |
| **Status** | **REPO_EVIDENCED** (snippet) + **CONCEPTUAL** (future bridges) |
| **Owner / boundary** | Adapter/bridge semantics in MARS docs; execution in n8n. |
| **What it is not** | MARS orchestrator; proof of full bidirectional integration. |
| **Evidence** | [integrations/n8n-mars-bridge-map-code.txt](integrations/n8n-mars-bridge-map-code.txt); [governance/adapter-and-bridge-boundaries.md](../../governance/adapter-and-bridge-boundaries.md) |
| **SAFE UNKNOWN** | Production use of MARS webhook bridge vs Telegram-only intake. |

---

### MetaBOT Evidence Pack

| Field | Value |
|-------|-------|
| **Definition** | Operator-reviewed bundle after workflow/doc changes: what changed, test results, sanitized export references, rollback notes, parity statement vs live n8n. |
| **Status** | **PLANNED** discipline — partially reflected in existing MIG/MetaBOT practice |
| **Owner / boundary** | Human operator; may live in repo reports or Storage — not auto-generated by MARS runtime. |
| **What it is not** | Git commit by itself; raw credential export. |
| **Evidence** | [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md) |
| **SAFE UNKNOWN** | Standard path template under `projects/metabot-seo-content-agent/`. |

---

### n8n runtime

| Field | Value |
|-------|-------|
| **Definition** | Self-hosted (or otherwise operated) **n8n** instance that executes workflow graphs, stores credentials, and owns live orchestration for MetaBOT products. |
| **Status** | **REPO_EVIDENCED** |
| **Owner / boundary** | External execution owner — **not** MARS. |
| **What it is not** | MARS `mars-runtime/`; documentation in this repo. |
| **Evidence** | [integration-boundary.md](integration-boundary.md) |
| **SAFE UNKNOWN** | Production URL, version, HA setup. |

---

### MARS role

| Field | Value |
|-------|-------|
| **Definition** | In MetaBOT context: **architecture, contracts, knowledge** — documentation packs, terminology, sanitized maps, integration boundaries, human-supervised design assistance. |
| **Status** | **REPO_EVIDENCED** |
| **Owner / boundary** | `X:\AI MARS` documentation; selective staging discipline. |
| **What it is not** | Runtime owner; credential store; autonomous deployer. |
| **Evidence** | [AGENTS.md](../../AGENTS.md), [integration-boundary.md](integration-boundary.md) |
| **SAFE UNKNOWN** | Future observability webhooks — design not evidenced. |

---

### MIG role

| Field | Value |
|-------|-------|
| **Definition** | **Market Intelligence Groundtruth** — R1 acquisition lane: SERP, competitors, keywords (capture-time), evidence, Research Pack. |
| **Status** | **REPO_EVIDENCED** |
| **Owner / boundary** | `projects/mig/`; **MIG acquires reality**. |
| **What it is not** | SEO writer runtime; MetaBOT internal graph; ORCA. |
| **Evidence** | [projects/mig/README.md](../mig/README.md); [shared/contracts/groundtruth-ownership-rule-v1.md](../../shared/contracts/groundtruth-ownership-rule-v1.md) |
| **SAFE UNKNOWN** | Production timing of SEO Agent research-layer fed by MIG outputs. |

**SEO Agent evolution note:** Use MIG experience and patterns; do **not** copy whole MARS brain into n8n. Lightweight research/source-prep layer — **PLANNED**, after studying current 3 workflows and external market tools.

---

### ORCA role

| Field | Value |
|-------|-------|
| **Definition** | **Interpretation owner (R2)** — PPC/strategy review, semantic intelligence, human-operated checklists. |
| **Status** | **REPO_EVIDENCED** |
| **Owner / boundary** | `projects/orca/`; human PPC operator. |
| **What it is not** | Default-required engine inside SEO writer; groundtruth acquirer. |
| **Evidence** | [projects/orca/OPERATIONAL-INDEX.md](../orca/OPERATIONAL-INDEX.md); groundtruth rule |
| **SAFE UNKNOWN** | Any future ORCA handoff into SEO Agent content strategy steps. |

---

### ATLAS role

| Field | Value |
|-------|-------|
| **Definition** | Business Reality Registry — organizations, projects, agreements (documentation layer). |
| **Status** | **REPO_EVIDENCED** — foundation complete; **no runtime** |
| **Owner / boundary** | `projects/atlas/` |
| **What it is not** | MetaBOT state store; automation trigger. |
| **Evidence** | [projects/atlas/OPERATIONAL-INDEX.md](../atlas/OPERATIONAL-INDEX.md) |
| **SAFE UNKNOWN** | Binding between ATLAS entities and MetaBOT task IDs. |

---

### OPS role

| Field | Value |
|-------|-------|
| **Definition** | Business Operations domain — reporting, documents, approvals, deadlines (documentation-first). |
| **Status** | **REPO_EVIDENCED** — registered **planned**; foundation done; **no runtime** |
| **Owner / boundary** | `projects/ops/` |
| **What it is not** | MetaBOT executor; collapsed into MetaBOT contour. |
| **Evidence** | [projects/ops/README.md](../ops/README.md), [projects/ops/foundation/OPS-SYSTEM-POSITIONING-v1.md](../ops/foundation/OPS-SYSTEM-POSITIONING-v1.md) |
| **SAFE UNKNOWN** | Live OPS automation timeline. |

---

### OPS Secretary candidate

| Field | Value |
|-------|-------|
| **Definition** | **Future** conceptual OPS-facing assistant that **might** use n8n / Telegram / API patterns compatible with MetaBOT — **not** a current repo product. |
| **Status** | **PLANNED** / **CONCEPTUAL** |
| **Owner / boundary** | OPS domain if chartered; MetaBOT Developer may help design n8n side **only** with approval. |
| **What it is not** | Current MetaBOT product; shipped bot. |
| **Evidence** | Operator frame; [projects/ops/foundation/OPS-AGENT-DECOMPOSITION-v1.md](../ops/foundation/OPS-AGENT-DECOMPOSITION-v1.md) (conceptual roles) |
| **SAFE UNKNOWN** | Name, scope, and implementation charter. |

---

### HomeGateway display role

| Field | Value |
|-------|-------|
| **Definition** | **Planned** private cockpit UI — may **display** signals from MetaBOT / OPS / n8n; links, deadlines, quick actions. |
| **Status** | **REPO_EVIDENCED** (display intent) + **PLANNED** (integration) |
| **Owner / boundary** | `projects/homegateway-v4-ai/` — UI prototype / docs; **not** runtime owner. |
| **What it is not** | Control plane for MetaBOT; n8n workflow engine; replacement for MARS/ORCA/MetaBOT. |
| **Evidence** | [projects/homegateway-v4-ai/README.md](../homegateway-v4-ai/README.md), [registry/project-registry.md](../../registry/project-registry.md) |
| **SAFE UNKNOWN** | Signal API format and freshness model. |

---

## Naming guidance (quick reference)

| Use this | When |
|----------|------|
| **MetaBOT SEO Agent** / **MetaBOT — SEO Content Agent** | Current product, registry, user-facing docs |
| **MetaBOT** | Broader contour or multi-product architecture discussion — clarify it is **working terminology** |
| **MetaBOT Developer** | Only with **planned/conceptual** qualifier |
| **`metabot-seo-content-agent`** | Registry `project_id`, paths, commits |
| **seo-content-agent** | Legacy folder only — **HISTORICAL** |

---

## Contradictions preserved (intentional)

1. **Repo default:** MetaBOT ≈ SEO Content Agent single product pack.  
2. **Operator intent:** MetaBOT = broader external bot/automation layer.  
3. **Resolution:** Broader layer is **documented**, not **implemented** as separate registry product unless future charter adds rows.

---

*Foundation Pack v1 · see [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)*
