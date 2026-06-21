# OPS — Business Operations Domain

**Status:** **FOUNDATION**  
**Classification:** **Business Operations Domain**  
**Purpose:** Human-supervised operational back-office support  
**Date:** 2026-06-04  
**Is not:** runtime, agents (implemented), automation, CRM, ERP, accounting system, legal authority, registry implementation, orchestration platform.

**Session navigation:** [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) — open **Core Run** first.

**Registration status:** **REGISTERED** (2026-06-05) — MARS `project_id` **ops**; registry row **planned** band.  
**Registry reference:** [../../registry/project-registry.md](../../registry/project-registry.md) (`ops` row + OPS boundaries note).  
**Lifecycle reference:** [../../logs/lifecycle-log.md](../../logs/lifecycle-log.md) — `evt-2026-0022`.  
**Registration evidence:** [../../logs/ops/ops-registration-v1.md](../../logs/ops/ops-registration-v1.md).

---

## What OPS is

**OPS** (Business Operations) is a **documentation-first**, **human-supervised** domain inside MARS focused on **operational back-office work**: reminders, deadlines, reporting workflows, document workflows, approval workflows, and operational tracking.

OPS exists to give operators a **clear operational model** for recurring business-office tasks without pretending to be a product runtime or a second business registry.

| Property | Description |
|----------|-------------|
| **Documentation-first** | Normative contracts, workflows, and role decomposition live in `projects/ops/` before any future implementation |
| **Human-supervised** | Every client-facing output, approval, and delivery requires explicit human review |
| **ATLAS-consuming** | Business identity and structural facts are **read** from ATLAS (when available); OPS does not own canonical reality |
| **Operationally focused** | Back-office rhythm: reporting cycles, document prep, missing-data review, completion recording |

---

## What OPS is not

OPS is **explicitly not**:

| Anti-role | Rationale |
|-----------|-----------|
| Autonomous business operator | No unsupervised decisions on clients, money, or legal facts |
| Accountant | No ledger, tax filing, or payment confirmation authority |
| Lawyer | No legal interpretation or contract authority |
| CRM | No pipeline, deals, or canonical client SoT |
| ERP | No inventory, procurement, or enterprise resource planning |
| Runtime system | No in-repo execution engine for OPS in Foundation v1 |
| Orchestration platform | No n8n/MARS workflow ownership claimed in this pack |

---

## Ecosystem relationships

### ATLAS — Business Reality Registry

**ATLAS** maintains **who exists, what exists, and how things are related** (canonical business identity and structure).

**OPS** performs **human-supervised operational work** on top of that reality: reporting cycles, document operations, reminders — **without duplicating** ATLAS as source of truth.

See [foundation/OPS-ATLAS-RELATIONSHIP-v1.md](foundation/OPS-ATLAS-RELATIONSHIP-v1.md).

### HomeGateway — Personal Operational Cockpit

**HomeGateway** is a **display and navigation surface** (cockpit UI) for the studio operator — links, clients, projects, deadlines, signals.

**OPS** is the **documented back-office domain** for how reporting and operational workflows should run; HomeGateway may **surface** OPS-related signals in the future but **does not own** OPS workflows or approvals.

**Boundary:** HomeGateway = cockpit layer · OPS = business operations methodology and workflow contracts.

### NOVA — Mobile Application Factory

**NOVA** is a **documentation-first production methodology** for mobile/PWA/business apps (RBM vocabulary, design-before-runtime).

**OPS** has **no production-line ownership** over NOVA deliverables. OPS may reference NOVA **projects** via ATLAS identity when reporting to clients — **SAFE UNKNOWN** until ATLAS consumer contracts are implemented.

### MetaBOT — SEO Content Agent (external)

**MetaBOT** is an **external** multi-workflow SEO content system (n8n, Telegram, Sheets) documented under `projects/metabot-seo-content-agent/`.

**OPS** does **not** execute MetaBOT workflows. OPS may track **operational reporting** about content production (e.g. monthly client summaries) using evidence supplied by humans — not by claiming live MetaBOT integration.

### ORCA — PPC Operational Toolkit

**ORCA** owns **PPC review, campaign preparation, and evidence-aware PPC operational work** (human-supervised).

**OPS** may include **PPC activity summaries** in client reporting when an operator attaches ORCA evidence — OPS does **not** own SERP, bids, or campaign architecture.

### MIG — Market Intelligence / Research

**MIG** **acquires market reality** (research sessions, evidence packs).

**OPS** may reference MIG outputs in client reports as **operator-attested attachments** — OPS does **not** own research methodology or SERP acquisition.

### WPilot — WordPress-oriented operations

**WPilot** (documented under `projects/wpilot/`) covers **WordPress site operations** in the MARS ecosystem.

**OPS** may track **site-related operational tasks** (e.g. maintenance windows in a monthly report) using ATLAS **website** references — OPS does **not** own CMS deploy or WP runtime.

### OCPilot — OpenCart-oriented operations

**OCPilot** (documented under `projects/ocpilot/`) covers **OpenCart storefront operations**.

Same boundary as WPilot: OPS may **report** on operational facts the operator confirms; OCPilot owns storefront ops domain.

---

## Foundation pack (v1)

| Document | Purpose |
|----------|---------|
| [foundation/OPS-BOUNDARIES-v1.md](foundation/OPS-BOUNDARIES-v1.md) | Ownership tables — what OPS owns vs excludes |
| [foundation/OPS-ATLAS-RELATIONSHIP-v1.md](foundation/OPS-ATLAS-RELATIONSHIP-v1.md) | Consumer contract and anti-duplication rules |
| [foundation/OPS-AGENT-DECOMPOSITION-v1.md](foundation/OPS-AGENT-DECOMPOSITION-v1.md) | Conceptual operational roles (not runtime agents) |
| [foundation/OPS-MVP-SCOPE-v1.md](foundation/OPS-MVP-SCOPE-v1.md) | Approved MVP: Monthly Client Reporting Control |
| [workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md](workflows/OPS-MONTHLY-REPORTING-WORKFLOW-v1.md) | Ten-stage monthly reporting workflow |
| [reports/REPORT-ops-business-operations-foundation-v1.md](reports/REPORT-ops-business-operations-foundation-v1.md) | Foundation pass record |

---

## Honesty statement

This pack is **documentation only**. No OPS runtime, agents, automations, or databases exist in-repo. **Registry registration** (2026-06-05) records OPS as a documented MARS program — **not** shipped product. Any future implementation requires a separate charter and explicit human approval.

---

*OPS — Business Operations Domain · Foundation v1.*
