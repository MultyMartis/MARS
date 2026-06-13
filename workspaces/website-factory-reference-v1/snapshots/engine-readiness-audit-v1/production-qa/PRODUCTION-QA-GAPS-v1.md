# Website Factory — Production QA Gaps v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** future work register — **documentation only**  
**Связь:** [PRODUCTION-QA-ROADMAP-v1.md](PRODUCTION-QA-ROADMAP-v1.md), [WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md](../WEBSITE-FACTORY-NEXT-PRIORITIES-v1.md)

---

## Назначение

Gaps v1 регистрирует work **вне scope** Production QA Architecture v1. **Никакая** запись ниже не означает реализацию, одобрение charter, или runtime existence.

---

## Gap register

| ID | Gap | Why out of v1 | Future charter |
|----|-----|---------------|----------------|
| PQA-G01 | **QA automation** — scripted contract validation | v1 human-operated only | Factory automation charter |
| PQA-G02 | **Playwright** / browser E2E | Not architectural QA | Frontend QA charter |
| PQA-G03 | **Visual QA** — screenshot diff, Percy, etc. | Not pattern architecture | Design ops charter |
| PQA-G04 | **Frontend QA** — component tests, Storybook QA | Implementation layer | Frontend factory charter |
| PQA-G05 | **Code QA** — lint, static analysis, SAST | Source code not in v1 scope | Engineering standards charter |
| PQA-G06 | **Performance QA** — Lighthouse, load tests | Runtime metrics | Performance charter |
| PQA-G07 | **Accessibility QA** — axe, WCAG audit automation | Runtime/DOM | A11y charter |
| PQA-G08 | **Runtime QA** — staging smoke, API health | Post-implementation | Runtime ops charter |
| PQA-G09 | **Production deployment QA** — deploy gates, infra checks | Deploy ≠ architecture handoff | DevOps charter |
| PQA-G10 | **Content copy QA** — linguistics, tone, fact-check bots | Content Validation = signals only | Editorial charter |
| PQA-G11 | **Legal fact verification runtime** | Human legal review outside v1 | Legal ops charter |
| PQA-G12 | **CI matrix executor** — auto-run checklist from repo | No CI product in MARS v1 | Tooling charter |
| PQA-G13 | **Extended site type matrix** | SAAS / WEB_APPLICATION / MARKETPLACE | Extended Types charter |
| PQA-G14 | **Per-block micro-QA matrix** | Page-level sufficient for v1 | Matrix v2 charter |
| PQA-G15 | **MIG/ORCA integration** | External orchestration | Bridge charter |
| PQA-G16 | **JSON Schema for PRODUCTION-QA-CONTRACT** | Fields documented in prose v1 | Contract tooling v2 |

---

## Explicit non-goals (reinforcement)

Production QA v1 **will not** become:

- Playwright project
- Visual regression suite
- Deploy approval bot
- Lighthouse gate
- Code review bot
- New architecture layer (taxonomy, blocks, pages)

---

## Dependencies on other gaps

| Gap | Related upstream gap |
|-----|---------------------|
| PQA-G01 | [generation-contracts/GENERATION-GAPS-v1.md](../generation-contracts/GENERATION-GAPS-v1.md) GG-* |
| PQA-G02–G04 | Frontend Layer (not started) |
| PQA-G08–G09 | Factory Runtime Architecture (not queued) |

---

## SAFE UNKNOWN

- Priority order among PQA-G01–G16 — **not scheduled**.
- Whether Production QA automation merges with Generation automation — **UNKNOWN**.
- Operator tooling (CLI vs web) — **UNKNOWN**.

---

*Production QA Gaps v1 — register only; no implementation claimed.*
