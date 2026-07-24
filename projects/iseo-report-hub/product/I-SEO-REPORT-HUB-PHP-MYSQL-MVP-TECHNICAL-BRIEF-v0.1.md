# I-SEO Report Hub — PHP + MySQL MVP Technical Brief v0.1

**Status:** TECHNICAL BRIEF — planning only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED** — no code, no schema deploy

**Authority:** [Platform Decision v0.1](I-SEO-REPORT-HUB-PLATFORM-DECISION-v0.1.md)  
**Basis:** [Product Architecture Layer 02](I-SEO-REPORT-HUB-PRODUCT-ARCHITECTURE-LAYER-02-v0.1.md), roles, data model, lifecycle, publishing/snapshots

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | MVP technical brief |
| Implementation | **Not started** |
| Code | **None** |
| SQL migrations | **None** |
| Based on | Product Architecture Layer 02 + Platform Decision (custom PHP + SQL/MySQL) |

This brief guides a future implementation charter. It does **not** authorize writing application code.

---

## 2. MVP Objective

Deliver a **local-to-production-ready** custom PHP + MySQL reporting application that allows the i-SEO team to:

- create and manage clients, projects, and sites;
- open monthly reporting periods;
- fill **weekly checkpoints** and a **monthly final report**;
- attach **evidence** and **KPI notes**;
- run **review / approve** workflow;
- **publish** versioned **snapshots**;
- share **controlled client token URLs**.

MVP is **internal-first**. Client delivery is a controlled published report link, not a full client login portal.

---

## 3. Recommended Technical Shape

| Choice | Recommendation |
|--------|----------------|
| Language | PHP |
| Database | MySQL or MariaDB |
| App structure | Plain PHP or **light custom MVC** initially |
| Composer | Optional later — not required to start |
| Heavy framework (Laravel/Symfony/etc.) | **Not** unless separately approved |
| Admin UI | Server-rendered HTML |
| JavaScript | Progressive enhancement only where useful |
| UX reference | Static demo v0.4 (`iseo-report-hub-prototype`) |
| WordPress dependency | **None** |
| Local runtime candidate | Laragon (see Laragon Local Runtime Plan) |

Do not claim any of the above as already built.

---

## 4. Core Modules

| Module | Description |
|--------|-------------|
| **auth/session** | Login, logout, session cookie, password verify |
| **users/roles** | User accounts; Admin, Lead, Specialist, Account Manager (per Role Model) |
| **clients** | Customer records |
| **projects/sites** | SEO engagements and site URLs; specialist assignment |
| **reporting periods** | One calendar month cycle per project |
| **weekly checkpoints** | Weeks 1–3 preliminary reports |
| **monthly reports** | Month-close comprehensive report |
| **report blocks** | Structured sections + field values |
| **specialist workspace** | Primary daily fill surface for assigned periods |
| **review workflow** | Submit → review → revision → approve |
| **published snapshots** | Immutable client-facing payload + token |
| **evidence/files** | Links, screenshots, uploads with ACL |
| **KPI values** | Manual metric snapshots + notes |
| **template/block matrix** | Project type profiles and block templates |
| **admin settings** | Templates, project types, system config |
| **audit log** | Publish/unpublish and sensitive actions |

---

## 5. MVP Screens

| Screen | Purpose |
|--------|---------|
| Login | Authenticate internal users |
| Dashboard | Period readiness, assigned work, review cues |
| Clients / projects | List and create clients and projects |
| Project detail | Sites, assignments, periods |
| Reporting period detail | Period state, weekly/monthly entry points |
| Specialist workspace | Daily fill for active period |
| Weekly checkpoint editor | Week 1–3 content |
| Monthly report editor | Month-close composition |
| Review queue | Lead/Admin review actions |
| Client report preview | Internal preview of client-safe view |
| Published report page | Token-based client delivery (`/p/{token}`) |
| Settings / templates | Block matrix / templates |
| Users / roles | User management (Admin) |

---

## 6. MVP Data Flow

1. Admin creates client / project / site.
2. Admin or Lead creates reporting period.
3. Specialist fills weekly checkpoints and block values.
4. Specialist adds evidence and KPI notes.
5. Monthly report aggregates / synthesizes content (author interpretation — not blind copy of weeklies).
6. Specialist submits monthly report to review.
7. Lead reviews and requests changes or approves.
8. Approved report is published as a **snapshot**.
9. Client receives **token URL**.
10. Later edits create a new draft and, if re-published, a new or superseded snapshot — never mutate the live client payload in place without versioning rules.

---

## 7. Security Baseline

| Control | Requirement |
|---------|-------------|
| Password hashing | Modern PHP password API (`password_hash` / `password_verify`) |
| Sessions | Server-side sessions; secure cookie flags in production |
| CSRF | Tokens on state-changing forms |
| Authorization | Role checks on every write/read path |
| Validation | Server-side validation for all inputs |
| Uploads | Type/size allowlist; no executable uploads |
| Upload storage | Private directory **outside** public docroot |
| Client links | High-entropy tokens |
| Secrets | No secrets in repo; `.env.local` gitignored |
| Audit | Log publish / unpublish (and preferably approve / revoke) |

Exact production TLS, host hardening, and backup tooling: **SAFE UNKNOWN** until deployment phase.

---

## 8. Non-MVP

Explicitly out of MVP:

- Topvisor API direct import
- AI generation / auto-draft publication
- Client login portal
- Complex BI / warehouse
- CRM
- Billing / accounting
- Full task manager
- Multi-tenant SaaS packaging
- Automated PDF generation (unless later approved)

n8n remains an **external helper** boundary only — not SoT, not required for MVP runtime.

---

## 9. Implementation Risks

| Risk | Mitigation direction |
|------|----------------------|
| Scope creep | Stick to Layer 02 MVP boundary; phases charter |
| File upload security | Private storage + allowlist + auth gate |
| Snapshot immutability | Separate draft vs snapshot storage; no live-draft client URL |
| Role complexity | Start with Role Model v0.1; avoid early ACL overengineering |
| Template overengineering | Seed from Block Matrix; avoid infinite configurator |
| Production hosting / backups | Dedicated deployment phase before go-live claims |
| Demo → app migration | Treat v0.4 as UX reference; rebuild against schema, not copy static HTML as SoT |

---

## 10. Companion docs in this package

| Doc | Role |
|-----|------|
| [Laragon Local Runtime Plan](I-SEO-REPORT-HUB-LARAGON-LOCAL-RUNTIME-PLAN-v0.1.md) | Local runtime planning |
| [MVP Implementation Phases](I-SEO-REPORT-HUB-MVP-IMPLEMENTATION-PHASES-v0.1.md) | Phased build plan |
| [MVP Schema Draft](I-SEO-REPORT-HUB-MVP-SCHEMA-DRAFT-v0.1.md) | Conceptual tables |
| [MVP Route and Screen Map](I-SEO-REPORT-HUB-MVP-ROUTE-AND-SCREEN-MAP-v0.1.md) | Conceptual routes |

---

## 11. Boundaries

- No claim that PHP app, DB, or Laragon project exists.
- No WordPress plugin path for MVP.
- Next step: operator review → scoped commit of this brief package → separate implementation charter for Phase 0.
