# ATLAS Boundaries v1

**Status:** **documented** — Phase 1 normative boundary contract.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) · [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md)  
**Is not:** enforcement code, linter rules, or automated policy engine.

---

## 1. Purpose of this document

Define **what ATLAS must never become** and **what it must always remain**, so cross-cutting registry work does not absorb CRM, ERP, finance, sales, project management, or marketing execution — even under pressure from consumers wanting “one place for everything.”

---

## 2. Explicit inclusions

ATLAS **includes** (conceptual ownership):

| # | Inclusion | Description |
|---|-----------|-------------|
| **I-01** | Canonical identity | Stable ids for MVP entities once implemented |
| **I-02** | Organizations | Business units as registry entities |
| **I-03** | People | Natural persons, multi-org participation |
| **I-04** | Projects | Structural work containers (not PM) |
| **I-05** | Websites | Web property identity |
| **I-06** | Domains | Hostname / domain identity anchors |
| **I-07** | Relationships | Structural edges between entities |
| **I-08** | Human attestation model | Canonical promotion requires human review (design) |
| **I-09** | Consumer reference contract | Downstream systems may **read** canonical reality |
| **I-10** | Deprecation / tombstones | Explicit retirement of entities (design principle) |
| **I-11** | SAFE UNKNOWN handling | Documented ambiguity — no silent invention |
| **I-12** | Cross-cutting registry role | Single business-reality SoT **intent** for MARS ecosystem |

---

## 3. Explicit exclusions

ATLAS **excludes** (must not own, store as canonical core, or operate):

### 3.1 Operational and execution domains

| # | Exclusion | Rationale |
|---|-----------|-----------|
| **E-01** | Tasks, subtasks, assignees | Task manager / PM territory |
| **E-02** | Sprints, boards, burndown | Agile tooling |
| **E-03** | Campaigns, ad groups, creatives | ORCA / ads platforms |
| **E-04** | Content calendars, articles, copy | CMS / content ops |
| **E-05** | SEO audits, keyword lists, rankings | MIG / SEO tools |
| **E-06** | PPC bids, budgets, performance metrics | ORCA / ads |
| **E-07** | Analytics sessions, conversions, funnels | Analytics products |
| **E-08** | Deploy pipelines, build ids, release trains | CI/CD and ops |
| **E-09** | CMS posts, products, orders | WPilot / OCPilot / storefront |
| **E-10** | Market SERP evidence packs | MIG acquisition artifacts |

### 3.2 Commercial and financial domains

| # | Exclusion | Rationale |
|---|-----------|-----------|
| **E-11** | Invoices, payments, ledgers | Accounting / ERP |
| **E-12** | Contracts, clauses, signatures | Contract lifecycle tools (future doc gen **consumes** ATLAS) |
| **E-13** | Quotes, proposals, deal values | Sales CRM |
| **E-14** | Pipeline stages, win probability | CRM |
| **E-15** | Tax IDs as financial system of record | ERP — optional **attested attribute** later, not ledger |
| **E-16** | Payroll, timesheets | HR / finance |

### 3.3 Platform and MARS meta domains

| # | Exclusion | Rationale |
|---|-----------|-----------|
| **E-17** | MARS `project_id` registry rows | `registry/project-registry.md` — program packs |
| **E-18** | Agent cards, orchestration graphs | MARS agent / automation layers |
| **E-19** | Autonomous runtime, workflows, n8n | Execution infrastructure |
| **E-20** | RAG corpora, embeddings | Knowledge products — not business graph |
| **E-21** | Infrastructure hosts, NAS paths | `governance/mars-infrastructure-reality-v1.md` |
| **E-22** | Environment (staging/prod) as entity | Deployment topology — rejected Phase 1 |

### 3.4 Phase 1 forbidden entity classes

| # | Exclusion | Status |
|---|-----------|--------|
| **E-23** | Business Scope as entity | Future metadata only |
| **E-24** | Cluster, Portfolio, Business Unit, Division | **NOT APPROVED FOR PHASE 1** |
| **E-25** | Standalone Asset entity | Phase 2+ relationship consideration |
| **E-26** | CRM Account / Contact mirror | Use Organization / Person — not CRM clone |

---

## 4. Boundary matrix — ATLAS vs drift targets

| Drift target | What attackers want | ATLAS allowed response | Forbidden response |
|--------------|---------------------|------------------------|-------------------|
| **CRM** | Deals, leads, pipeline on Organization | Org identity + link to external CRM id (optional, future) | Pipeline stage fields |
| **ERP** | GL accounts, cost centers | Org identity only | Posting, balances |
| **Accounting** | Invoices linked to org | Org id for reference export | Invoice storage |
| **Finance** | Revenue attribution | **SAFE UNKNOWN** or consumer-local | Canonical revenue |
| **Sales** | Opportunity tracking | Project name as **structural** label only | Win/loss state |
| **Project management** | Tasks under Project | Project container | Task lists in ATLAS |
| **Marketing** | Campaign membership | **Relationship** to external campaign id — only if expansion approves | Campaign execution |
| **Analytics** | Traffic by website | Website id handoff | Session metrics in ATLAS |
| **Hosting** | DNS, SSL, env | Domain/Website **identity** | DNS console |
| **MIG** | Competitor truth | Consumer reads org/site ids | SERP packs in ATLAS |
| **ORCA** | Ad structure | Consumer reads site/project ids | Ad groups in ATLAS |

---

## 5. Anti-drift rules

Normative rules for humans and future implementers. Violation = **boundary defect**, not “tech debt.”

### 5.1 Feature admission

| Rule ID | Rule |
|---------|------|
| **AD-01** | New field on MVP entity requires **expansion review** ([ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md)) |
| **AD-02** | If a feature supports **daily operator workflow** (due dates, assignments), it is **not** ATLAS |
| **AD-03** | If a feature supports **money movement or recognition**, it is **not** ATLAS |
| **AD-04** | If a feature is **updated every minute** from live systems, it is likely **consumer cache**, not canonical |
| **AD-05** | “Just one more table” for convenience triggers **AD-01** — no exceptions without written approval |
| **AD-06** | Consumer-specific blobs (ORCA export settings) stay in consumer — **reference** ATLAS ids only |
| **AD-07** | Reporting aggregates are **derived** — not stored as canonical truth in ATLAS |
| **AD-08** | Sync from external CRM **imports proposals** — human promotion to canonical (future impl) |

### 5.2 Language and documentation drift

| Rule ID | Rule |
|---------|------|
| **AD-10** | Do not describe ATLAS as “the CRM” or “master ERP” in docs or UI |
| **AD-11** | Do not claim “ATLAS runtime” until evidenced implementation exists |
| **AD-12** | Prefix ambiguous “registry” with **Business Reality** or **ATLAS** |
| **AD-13** | Pilot data in MIG/ORCA folders is **not** automatic ATLAS canonical |

### 5.3 Organizational pressure patterns

| Pressure | Correct response |
|----------|------------------|
| “Store tasks here so we have one tool” | Reject — link Project id in task tool |
| “Track deal stage on Organization” | Reject — CRM owns pipeline |
| “Put MIG SERP JSON on Website” | Reject — MIG session evidence |
| “Add staging Environment entity” | Reject Phase 1 — ops local |
| “Business Scope = top-level org” | Reject — scope is classification metadata, future |

---

## 6. Consumer contract boundaries

Consumers **may**:

- Resolve `organization_id`, `person_id`, `project_id`, `website_id`, `domain_id` for labeling and joins.
- Propose new entities or relationships for human canonicalization (future).
- Cache read-only copies with explicit sync discipline.

Consumers **must not**:

- Treat local cache as canonical when ATLAS disagrees post-reconciliation.
- Require ATLAS to store their execution artifacts.
- Fork duplicate Organization/Person registries without documented exception and merge plan.

| Consumer | Reads from ATLAS (intent) | Must keep local |
|----------|---------------------------|-----------------|
| **MIG** | Org, project, site for session context | SERP evidence, research packs |
| **ORCA** | Site, project, org for pilot scope | Campaigns, semantics, exports |
| **Website Factory** | Site, project, org for pack scope | Build artifacts, QA state |
| **WPilot / OCPilot** | Site, domain, org | CMS content, plugins, orders |
| **HomeGateway** | Surfaces for navigation labels | Cockpit layout, personal UX state |

---

## 7. Relationship to MARS governance

| Surface | Relationship to ATLAS |
|---------|-------------------------|
| `registry/project-registry.md` | MARS **program** ids — orthogonal |
| `governance/mars-infrastructure-reality-v1.md` | Machine paths — not business entities |
| MIG “Reality Layers R1–R4” | Market evidence — not business graph |
| NOVA “Decision Reality” | Mobile product decisions — not ATLAS entities |

No automatic merge of these namespaces.

---

## 8. Phase 1 boundary compliance checklist

Use for reviews before any implementation charter:

- [ ] Change adds only MVP entity types or attested attributes?
- [ ] No task, deal, invoice, or campaign fields?
- [ ] No Environment entity?
- [ ] No Business Scope / Cluster / Portfolio / Division entities?
- [ ] Project remains structural only?
- [ ] Relationship does not imply implemented OWNER/EMPLOYEE enum?
- [ ] Documentation avoids runtime/API/DB claims?
- [ ] Ambiguity path documented as SAFE UNKNOWN?

---

## 9. Escalation

Boundary disputes escalate to **human program owner** (operator), not autonomous agent resolution. Document outcome as amendment to expansion rules or reality model — not silent code change.

---

*ATLAS Boundaries v1 — inclusions, exclusions, anti-drift. Documentation only.*
