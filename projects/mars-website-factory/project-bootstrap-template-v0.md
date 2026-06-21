# Operational template — Project bootstrap (v0)

**Status:** **documentation-only** checklist for **starting** a new Website Factory project in supervised execution. **Not** project generator software, **not** repo scaffolding automation.

**Normative references:** [reference-project-model-v0.md](reference-project-model-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [first-operational-runbook-v0.md](first-operational-runbook-v0.md), [cursor-execution-standard-v0.md](cursor-execution-standard-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md).

---

## 1. Bootstrap trigger

- [ ] New client / new site request
- [ ] Migration from legacy content
- [ ] Reference / demo project

**project_id** (proposed):  
**Target folder / repo path** (if known):

---

## 2. Intake minimums

Before strategy work, capture **at minimum**:

| Topic | Status (known / SAFE UNKNOWN) |
|-------|--------------------------------|
| **Production mode** (`PIXEL_PERFECT` \| `TEMPLATE_ART`) | **Mandatory** — undeclared → **STOP** per [website-factory-production-modes-charter-v1.md](website-factory-production-modes-charter-v1.md) |
| Business model & offer | |
| Audience / geography | |
| Compliance constraints (claims, industries) | |
| Brand assets & voice | |
| Success definition (non-ranking where possible) | |
| Technical constraints (CMS, static only, etc.) | |

---

## 3. Required artifacts (first slice)

Per [reference-project-artifact-tree-v0.md](reference-project-artifact-tree-v0.md):

1. Intake memo  
2. Site classification (`site_type_id`)  
3. Initial assumptions + **SAFE UNKNOWN** list  

Optional but recommended: single-page **project charter** paragraph (scope / non-goals).

---

## 4. Initial assumptions (explicit)

| Assumption | Risk if wrong | Validation owner |
|------------|---------------|------------------|
| | | |

---

## 5. Escalation triggers

Escalate early when:

- **Legal / regulated** claims appear without source.
- **STRUCTURE CHANGE** — site type or page count materially shifts ([system-signals-dictionary.md](../../governance/system-signals-dictionary.md)).
- **SECURITY RISK** — forms, PII, third-party scripts.
- **NEED HUMAN APPROVAL** — budget, timeline, or brand boundary crossed.

---

## 6. Operator expectations

- Work inside agreed **target folder** ([cursor-execution-standard-v0.md](cursor-execution-standard-v0.md)).
- **AGENT** vs **ASK** mode per project rules — **not** autonomous execution.
- Produce **REPORT** blocks per [reporting-standard-v0.md](reporting-standard-v0.md) after material steps.

---

## 7. Choose templates

Map `site_type_id` + scope to operational templates ([operational-template-overview-v0.md](operational-template-overview-v0.md)):

| Template | Use (Y/N) |
|----------|-----------|
| [service-landing-template-v0.md](service-landing-template-v0.md) | |
| [geo-landing-template-v0.md](geo-landing-template-v0.md) | |
| [catalog-project-template-v0.md](catalog-project-template-v0.md) | |
| [multi-page-site-template-v0.md](multi-page-site-template-v0.md) | |
| Others | |

---

## 8. First checkpoint alignment

Map to [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md) **C01** (or earliest applicable).

---

*Template v0 — disciplined project start.*
