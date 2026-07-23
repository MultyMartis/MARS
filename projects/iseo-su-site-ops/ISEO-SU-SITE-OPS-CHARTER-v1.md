# ISEO-SU-SITE-OPS Charter v1

**Status:** ACCEPTED (Phase 1.5)  
**Decision date:** 2026-07-22  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`  
**Classification key:** CONFIRMED · OPERATOR-CONTEXT · RECOMMENDED · DEFERRED · SAFE UNKNOWN · EXCLUDED

---

## 1. Purpose

Establish a durable MARS programme for **existing production site operations** of `https://i-seo.su/` so that hybrid static + WordPress work, connection planning, safety, and runbooks have a single documentary home — **before** any production connection is authorized.

---

## 2. Scope

| In scope (documentation / planning) | Classification |
|-------------------------------------|----------------|
| Project charter, phase model, registers, reports | CONFIRMED |
| Future site passport, access model, hybrid SoT matrix | PLANNED (CONFIRMED ownership) |
| FTP/static connection planning | PLANNED |
| WPilot preinstall / connection planning (WordPress-only) | PLANNED / OPTIONAL until approved |
| Backup/rollback and protected-zone documentation for this site | PLANNED |
| Smoke plans and operational runbook | PLANNED |
| Cross-programme boundary statements | CONFIRMED |

| Out of scope (this charter) | Classification |
|-----------------------------|----------------|
| Live production mutation | EXCLUDED until Phase 6+ charter |
| Credential storage in Git | EXCLUDED |
| ATLAS mint | DEFERRED |
| Local mirror creation | DEFERRED (default) |
| Report Hub product build | EXCLUDED (sibling programme) |
| Copying FP-0002 architecture as site blueprint | EXCLUDED |
| Claiming verified hosting/architecture facts without evidence | EXCLUDED |

---

## 3. Business context

| Fact | Classification |
|------|----------------|
| Site URL `https://i-seo.su/` | CONFIRMED (operator / programme decision) |
| Organization: i-SEO | CONFIRMED |
| Operator: Andrey | CONFIRMED |
| Existing production site | OPERATOR-CONTEXT |
| Hybrid static HTML + WordPress | OPERATOR-CONTEXT (not verified technical evidence) |

---

## 4. System context

| System | Role | Classification |
|--------|------|----------------|
| This locus | Main SoT for hybrid site operations docs | CONFIRMED |
| WPilot | WordPress pilot methodology + RC5 DEV reference | CONFIRMED (supporting) |
| WPilot Plugin | Future WordPress connection surface only | DEFERRED for production |
| Report Hub | Sibling product on/near i-seo.su ecosystem | CONFIRMED (sibling) |
| Website Factory | Static methodology | CONFIRMED (methodology-only) |
| Forge WordPress | WP engineering safety methodology | CONFIRMED (methodology-only) |
| ATLAS | Identity registry | DEFERRED mint |
| Survivability / GitGuard | Safety patterns | CONFIRMED (supporting) |
| MLI | Optional future local runtime | DEFERRED |
| ROL | Remote-ops discipline | CONFIRMED (supporting; not authorization) |
| Firefox Browser Workstation | Future QA workstation | APPROVED DIRECTION / IMPLEMENTATION DEFERRED |

---

## 5. In-scope surfaces (when later authorized)

- Public site surfaces (read evidence, browser QA)
- Static file/docroot surfaces (FTP/static plan)
- WordPress admin / content surfaces (via WPilot or HITL admin — only when chartered)
- Custom tools / forms / calculators as mapped entities (documentary first)
- Backup, rollback, and promote procedures (documentary → controlled execution)

All remain **NOT AUTHORIZED** for live connection at Phase 1.5 closeout.

---

## 6. Out-of-scope surfaces

- Unrelated MARS programmes' foreign WIP
- Report Hub implementation backlog as site-ops work
- Production credential vaulting inside this Git tree
- Autonomous CMS/ops agents
- Broad mirror sync as default workflow

---

## 7. Role model

| Role | Responsibility |
|------|----------------|
| **Operator (Andrey)** | HITL approvals, production identity, acceptance of phase REPORTs |
| **Lane A agent (Cursor)** | Documentation and later chartered scoped ops under this locus |
| **Lane B (read-only support)** | Read governance / sibling methodology; no ownership transfer |
| **WPilot programme** | Plugin contracts and WordPress-only patterns |
| **Sibling programmes** | Boundaries only unless separately chartered |

---

## 8. HITL model

Every phase that risks external access, secrets, mutation, or identity mint requires **explicit operator approval** before execution.

Minimum HITL gates:

1. Accept Phase REPORT before next phase starts.
2. Approve any connection charter (FTP, WPilot, panel, SSH).
3. Approve any write/smoke/promote.
4. Approve ATLAS mint when no longer deferred.
5. Approve local mirror creation if ever needed.

Default on ambiguity: **STOP**.

---

## 9. Lifecycle

Current: **DOCUMENTARY INTAKE / PRE-CONNECTION**.

Progression requires completed phase artifacts + operator acceptance. Production connection is a late gate (Phase 6), not an early convenience.

---

## 10. Phase model

Normative detail: [ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md](ISEO-SU-SITE-OPS-PHASE-MODEL-v1.md).

Summary: Phase 0–1 COMPLETE → Phase 1.5 COMPLETE after this locus → Phase 2 HOLD pending acceptance → Phases 3–5 planning → Phases 6–7 NOT AUTHORIZED.

---

## 11. Evidence requirements

- Prefer **runtime-first audit** of live non-secret evidence over assuming Git/source truth.
- Chat handoffs are supporting evidence only.
- Do not invent hosting facts.
- Secrets never enter reports or registers.
- Classify claims: CONFIRMED / OPERATOR-CONTEXT / RECOMMENDED / DEFERRED / SAFE UNKNOWN / EXCLUDED.

---

## 12. Mutation prohibition (current)

Until a Phase 6+ connection charter is accepted:

- No production writes
- No plugin install
- No token creation
- No REST calls
- No FTP/SFTP
- No Localhost site creation for this programme
- No ATLAS mutation
- No project-registry mutation without separate charter

---

## 13. Conditions before any production connection

RECOMMENDED gate set (must be satisfied or explicitly waived by operator):

1. Site passport + hybrid ownership map accepted
2. Access model accepted (non-secret)
3. Protected zones + backup/rollback model accepted
4. Connection channel chosen and chartered (FTP and/or WPilot)
5. Smoke plans accepted
6. Operator HITL recorded
7. No secrets in Git locus
8. Rollback method known for intended action class

---

## 14. Closeout criteria (Phase 1.5)

Phase 1.5 is COMPLETE when:

- Canonical locus exists at `projects/iseo-su-site-ops/`
- Required charter/boundary/phase/register/handoff/deferred docs exist
- Phase 0 / 1 / 1.5 REPORTs exist
- No secrets in locus
- No unauthorized mutations outside locus
- Operator can review Phase 1.5 REPORT and authorize Phase 2

---

*Charter v1 · 2026-07-22 · does not claim verified i-seo.su architecture.*
