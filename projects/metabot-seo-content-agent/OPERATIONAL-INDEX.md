# MetaBOT — Operational Index

**Status:** **ACTIVE** — canonical documentation pack for MetaBOT SEO Content Agent; **MetaBOT Foundation Pack v1** adds broader working terminology.  
**Maturity:** **External operational product (documentation-level)** — live execution in **n8n**; MARS holds knowledge, contracts, and sanitized artifacts only.  
**Classification:** External Systems lane · `project_id`: **metabot-seo-content-agent**  
**Domain root:** [README.md](README.md)

**Not:** MARS autonomous runtime, MARS orchestrator, hidden agent fleet, self-deploying system, n8n replacement, or owner of MIG / ORCA / OPS / ATLAS.

---

## Current Identity

| Field | Value |
|-------|-------|
| **Canonical `project_id`** | `metabot-seo-content-agent` — **do not rename** |
| **Current concrete product** | **MetaBOT SEO Agent** (also documented as **MetaBOT — SEO Content Agent**) |
| **Broader working contour** | **MetaBOT** — external automation / bot layer (n8n, Telegram, API bots, webhooks, cloud actions) — **OPERATOR_CLARIFICATION**; not fully implemented as a separate umbrella product in repo |
| **Telegram bot** | `@seo_content_agent_bot` — **OPERATOR_CLARIFICATION** (external fact; not verified from this repo) |
| **Primary users** | i-SEO SEO specialists — **OPERATOR_CLARIFICATION** + partial repo evidence (workflow export label `i-SEO`) |
| **Registry** | [registry/project-registry.md](../../registry/project-registry.md) — row `metabot-seo-content-agent` **active** |

---

## Execution Boundary

| Layer | Role |
|-------|------|
| **n8n** | **Execution runtime** — Intake / Worker / Admin graphs, credentials, retries, live orchestration |
| **MetaBOT (external)** | **Product system** — multi-workflow SEO content pipeline, Telegram UX, Sheets-backed state |
| **MARS (`X:\AI MARS`)** | **Architecture / contracts / knowledge** — documentation, sanitized exports, integration boundaries. **Does not execute MetaBOT workflows.** |
| **MetaBOT Developer** | **PLANNED / CONCEPTUAL** engineering sub-contour — see [metabot-developer-concept-v1.md](metabot-developer-concept-v1.md). **Not** running software. |

Normative boundary: [integration-boundary.md](integration-boundary.md) · Governance: [governance/external-system-boundaries.md](../../governance/external-system-boundaries.md)

---

## Current Product: MetaBOT SEO Agent

**Purpose (REPO_EVIDENCED + OPERATOR_CLARIFICATION):** Create SEO briefs, ТЗ, SEO articles, SEO landing/page text, QA and factcheck for SEO specialists.

**Runtime surfaces:** Telegram · OpenRouter · Google Sheets · n8n workflows.

**Worker reference:** v13 stable — **SAFE UNKNOWN** whether other variants run in parallel; confirm in live n8n.

### Current workflows (REPO_EVIDENCED)

| Workflow | Status | Role |
|----------|--------|------|
| **Intake** | **Current** | Telegram gateway, validation, routing, lock initiation |
| **Worker** | **Current** | Main content pipeline — generation, locks, QA/factcheck, Sheets |
| **Admin** | **Current** | Ops layer — locks, health, recovery, `/stop-all-flow` |
| **File Export** | **PLANNED** | Documented future 4th workflow — **not** evidenced as implemented |

**Sanitized repo export:** legacy single-workflow snapshot only — [exports/workflow-sanitized-legacy.json](exports/workflow-sanitized-legacy.json). **Does not** replace live Intake/Worker/Admin truth.

**Research / niche / competitor / keyword workflow:** **PLANNED** evolution candidate — **not** current repo truth. See Active Work Lines.

---

## Planned / Conceptual: MetaBOT Developer

Engineering role for MARS-assisted, human-supervised design of n8n workflow schemes.

| Attribute | Value |
|-----------|-------|
| **Status** | **PLANNED / CONCEPTUAL** |
| **Purpose** | Design, document, test-plan, and prepare importable workflow JSON for MetaBOT products |
| **Not** | Autonomous developer, unattended deployer, credential owner, production orchestrator |

Full definition: [metabot-developer-concept-v1.md](metabot-developer-concept-v1.md)  
Development discipline: [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md)

---

## Related Systems

| System | Relationship to MetaBOT |
|--------|-------------------------|
| **MIG** | Groundtruth / acquisition lane (R1). Use patterns and experience; **do not** copy whole MARS brain into n8n. Future lightweight research/source-prep layer for SEO Agent — **PLANNED**. Wordstat / Yandex keyword API — **SAFE UNKNOWN** unless evidenced. |
| **ORCA** | Interpretation lane (R2). **Optional / not default** for SEO writer evolution until charter requires it. |
| **OPS** | Business operations domain. **Not** a MetaBOT product. OPS Secretary — **future candidate** only if it later uses n8n/Telegram/API. |
| **ATLAS** | Business reality registry — documentation only; no MetaBOT runtime ownership. |
| **HomeGateway** | Display-only cockpit surface — may show MetaBOT signals in future; **not** control plane or runtime owner. |
| **Legacy `seo-content-agent`** | Early spec / bridge pack — **do not extend**; canonical docs live here. |

Ecosystem map: [governance/external-systems-relationship-map-v0.md](../../governance/external-systems-relationship-map-v0.md)  
MIG pattern study: [projects/mig/reports/REPORT-mig-runtime-design-metabot-patterns-v1.md](../mig/reports/REPORT-mig-runtime-design-metabot-patterns-v1.md)  
Groundtruth rule: [shared/contracts/groundtruth-ownership-rule-v1.md](../../shared/contracts/groundtruth-ownership-rule-v1.md)

---

## Current Evidence Map

| Evidence type | Path | Classification |
|---------------|------|----------------|
| Canonical doc pack | `projects/metabot-seo-content-agent/` | **REPO_EVIDENCED** |
| Runtime mega-map v13 | [mega-map.md](mega-map.md) | **REPO_EVIDENCED** |
| Workflow map | [workflow-map.md](workflow-map.md) | **REPO_EVIDENCED** |
| Integration boundary | [integration-boundary.md](integration-boundary.md) | **REPO_EVIDENCED** |
| Sanitized legacy export | [exports/workflow-sanitized-legacy.json](exports/workflow-sanitized-legacy.json) | **REPO_EVIDENCED** (partial; legacy shape) |
| n8n bridge snippet | [integrations/n8n-mars-bridge-map-code.txt](integrations/n8n-mars-bridge-map-code.txt) | **REPO_EVIDENCED** |
| Governance boundaries | [governance/external-system-boundaries.md](../../governance/external-system-boundaries.md) | **REPO_EVIDENCED** |
| Live n8n graphs | External — `n8n` instance | **SAFE UNKNOWN** from repo alone |
| Telegram bot handle | `@seo_content_agent_bot` | **OPERATOR_CLARIFICATION** |
| Full Intake/Worker/Admin JSON in repo | Not present as current sanitized set | **SAFE UNKNOWN** / gap |

---

## Active Work Lines

**Marking:** items below are **not started** in this foundation pack unless noted.

| # | Work line | Status |
|---|-----------|--------|
| 1 | Study current 3 SEO Agent n8n workflows again for Web-GPT / MARS sessions | **Not started** |
| 2 | Collect SEO team evidence pack (prompts, examples, good/bad outputs, ТЗ structures, QA criteria, factcheck cases, specialist requests) | **Not started** |
| 3 | External deep research (SEO AI writers, brief generators, SERP parsers, keyword tools, competitor→brief pipelines, QA/factcheck tools, n8n best practices) | **Not started** |
| 4 | Build SEO Agent evolution plan (SERP parse, niche research, competitors, keywords, ТЗ, writer quality, QA/factcheck) | **Not started** |
| 5 | Design MetaBOT Developer workflow discipline for future n8n scheme creation | **Documented** — [metabot-developer-concept-v1.md](metabot-developer-concept-v1.md), [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md) |
| 6 | Implement n8n workflow changes | **Forbidden without evidence + operator approval** |
| — | Stabilization buckets (runtime, quality, storage) | **REPO_EVIDENCED** planning — [roadmap.md](roadmap.md), [known-issues.md](known-issues.md) |
| — | File Export workflow | **PLANNED** — [workflow-map.md](workflow-map.md) |
| — | Research / keyword / competitor layer (MIG-informed) | **PLANNED** — not current product |

---

## SAFE UNKNOWN

- Exact live n8n graph parity with documentation (node order, error branches, credential scopes).
- Whether Worker variants besides v13 run in production.
- Intake → Worker handoff mechanism (queue vs synchronous vs sheet polling).
- Admin trigger model (same bot vs separate webhook).
- Wordstat / Yandex keyword API integration status for SEO Agent.
- Full sanitized export set for Intake / Worker / Admin in repo.
- Webhook shapes for future MARS ↔ MetaBOT observation bridges.
- OPS Secretary product shape and MetaBOT compatibility timing.
- HomeGateway signal format for MetaBOT status display.

---

## Session Start Checklist

1. Read this index and [metabot-terminology-and-roles-v1.md](metabot-terminology-and-roles-v1.md).
2. Confirm task scope: **docs** vs **live n8n change** — live changes require operator charter and [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md).
3. Open product truth: [mega-map.md](mega-map.md) → [workflow-map.md](workflow-map.md) → task-specific doc.
4. Check boundaries: [integration-boundary.md](integration-boundary.md); do not claim MARS runtime ownership.
5. For cross-system work: MIG = acquisition · ORCA = interpretation · OPS ≠ MetaBOT.
6. Reconcile execution claims against **live n8n** — repo markdown is not execution proof.
7. Mark gaps **SAFE UNKNOWN**; do not invent credentials, bot tokens, or workflow IDs.

---

## Do Not Claim

- MARS executes or orchestrates MetaBOT workflows.
- MetaBOT Developer is live autonomous software.
- Broader MetaBOT umbrella is fully implemented beyond SEO Content Agent documentation.
- File Export or research/keyword workflows exist in production without evidence.
- Wordstat / Yandex keyword APIs are integrated and complete.
- ORCA is required for SEO writer by default.
- OPS Secretary is a current MetaBOT product.
- HomeGateway controls MetaBOT or n8n.
- Sanitized legacy JSON equals current Intake/Worker/Admin live graphs.
- Registry row or doc pack proves deployed runtime health.

---

## Current Next Step

**v14 patch status (2026-07-13):**

| Item | Status |
|------|--------|
| PC-07 | `PC07_PRODUCTION_APPLIED_VERIFIED` |
| PC-14 | `PC14_PRODUCTION_APPLIED_VERIFIED_WITH_FOLLOWUP_STRICT_BACKLOG` |
| PC14-FU-01 | **COMPLETE** — `PC14_FU01_CLOSED_NEXT_SELECTED` |
| PC14-FU-02 audit | **COMPLETE** — `PC14_FU02_READY_FOR_SANDBOX_PATCH_PROPOSAL` |
| PC14-FU-02 sandbox proposal | **COMPLETE** — `PC14_FU02_READY_FOR_SANDBOX_IMPLEMENTATION` |
| Production Worker | `p4mqb4VuPcemIDlC` active · Strict Cleanup `v15-strict-cleanup-pc14-fu01-r1` |
| Selected path | **FU-02A / Option B** — Strategy A insert `TZ Strict Cleanup` after `Run Extract Outline` (+ companion `$()` retargets); final SEO Text / Strict Cleanup / Format unchanged |
| Next backlog | `PC14_FU02_SANDBOX_PATCH_IMPLEMENTATION` |

FU-02 sandbox proposal: [reports/REPORT-metabot-seo-agent-v14-pc14-fu02-sandbox-patch-proposal.md](reports/REPORT-metabot-seo-agent-v14-pc14-fu02-sandbox-patch-proposal.md)  
FU-02 audit: [reports/REPORT-metabot-seo-agent-v14-pc14-fu02-tz-strict-residual-cleanup-audit-proposal.md](reports/REPORT-metabot-seo-agent-v14-pc14-fu02-tz-strict-residual-cleanup-audit-proposal.md)  
FU-01 closeout: [reports/REPORT-metabot-seo-agent-v14-pc14-fu01-closeout-next-backlog-selection.md](reports/REPORT-metabot-seo-agent-v14-pc14-fu01-closeout-next-backlog-selection.md)

Foundation pack review remains available:

- [metabot-terminology-and-roles-v1.md](metabot-terminology-and-roles-v1.md)
- [metabot-developer-concept-v1.md](metabot-developer-concept-v1.md)
- [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md)

Then (after FU-02 sandbox/production wave, when capacity allows): **work line 1** — re-study live 3-workflow SEO Agent graphs with operator — before unrelated workflow evolution.

---

## Foundation Pack v1 (navigation)

| File | Purpose |
|------|---------|
| [metabot-terminology-and-roles-v1.md](metabot-terminology-and-roles-v1.md) | Working names, roles, boundaries |
| [metabot-developer-concept-v1.md](metabot-developer-concept-v1.md) | Planned engineering sub-contour |
| [n8n-project-development-rules-v1.md](n8n-project-development-rules-v1.md) | Safe MARS-assisted n8n workflow discipline |

*See also existing pack: [README.md](README.md) documentation table.*
