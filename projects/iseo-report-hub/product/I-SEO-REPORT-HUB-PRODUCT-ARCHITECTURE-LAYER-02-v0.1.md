# I-SEO Report Hub — Product Architecture Layer 02 v0.1

**Status:** PLANNING — product architecture layer after static demo v0.4  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED** — documentation only

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Product architecture (Layer 02) |
| After | Static demo v0.4 (commit `66d651a2`) |
| After (content) | Report content architecture (commit `6c496b57`) |
| Before | Implementation; SEO feedback charter; platform MVP build |
| Purpose | Define next product architecture layer beyond demo and content model |

**State summary:**
- documentation-only;
- after static demo v0.4;
- before implementation;
- before SEO feedback charter;
- defines next product architecture layer.

---

## 2. Current Accepted Baseline

| Baseline | Status |
|----------|--------|
| Static demo v0.4 | **Accepted** as a useful **raw** prototype (operator decision 2026-07-24) |
| Specialist workspace | Exists in demo (`specialist-workspace.html`); treated as likely core UX |
| Report content architecture | Exists (v0.1) — philosophy, objects, block matrix, staged states |
| Visual direction | i-seo.su / INTLSEO-inspired style accepted as direction for demos |
| SEO specialist feedback | **Deferred** — collection still premature |
| Informal demo viewing | Several people looked; no meaningful notes captured |
| Implementation | **Not started** — no plugin, app, DB, API, n8n |

Operator position: v0.4 is obviously still a demo; some panels will later be removed and others added. Next work is **product architecture**, not demo polishing. Demo corrections discovered here go to the **v0.5 backlog**, not into live demo edits.

---

## 3. Product Layers

Ordered from current reality toward long-term product maturity:

| # | Layer | Role | Current state |
|---|-------|------|---------------|
| 1 | **Demo / UX prototype** | Static HTML workspace to explore flows and visual direction | v0.4 exists; accepted raw baseline |
| 2 | **Report content model** | What a credible weekly/monthly report contains; block matrix; visibility | Documented (content architecture + block matrix) |
| 3 | **Product architecture** | Modules, MVP boundary, roles, lifecycle, publishing | **This layer (02)** |
| 4 | **Data model** | Conceptual entities and relations (platform-neutral) | Layer 02 companion: data model v0.1 |
| 5 | **Runtime / platform implementation** | WordPress module and/or custom PHP+MySQL (and hybrid) | **Not started**; decision frame only |
| 6 | **Automation / API / imports** | Topvisor and other imports; n8n events; AI drafts | Post-MVP |
| 7 | **Client publishing** | Controlled client web report delivery from snapshots | Spec in Layer 02; no runtime |
| 8 | **Long-term analytics / history** | Cross-period history, BI-style views | Explicitly out of MVP |

Layers 1–2 inform Layer 3. Layers 5–8 must not be claimed as existing.

---

## 4. Product Modules

Logical product modules (not implementation packages):

| Module | Purpose |
|--------|---------|
| **Authentication / users** | Identity, sessions, role assignment |
| **Clients** | Customer records and commercial context |
| **Projects / sites** | SEO engagements and site URLs |
| **Project type profile** | Block set and validation defaults by site type |
| **Reporting periods** | Monthly cycle container per project |
| **Weekly checkpoints** | Week 1–3 preliminary reports |
| **Monthly reports** | Month-close comprehensive report |
| **Report blocks** | Structured sections with status and visibility |
| **Work dictionary** | Canonical work items and client-facing wording |
| **KPI values** | Manual (later imported) metric snapshots |
| **Evidence / screenshots / files** | Links, files, and attachments supporting claims |
| **Review workflow** | Submit, revise, approve gates |
| **Published client reports** | Snapshot-backed client-facing delivery |
| **Comments / revisions** | Reviewer and internal commentary |
| **Templates / block matrix** | Profiles, block templates, inclusion rules |
| **Notifications / reminders** | Event model for future n8n (not live automation in MVP) |
| **Imports / integrations** | External source references and future API imports |

---

## 5. MVP Product Boundary

### In MVP

- Manual / semi-manual report creation
- User roles (see Role and Permission Model)
- Project and period management
- Specialist workspace (daily filling surface)
- Monthly report editor (and weekly checkpoint editors)
- Review / publish workflow
- Client public/private report link (controlled access — not full portal)
- Evidence attachments as references or files
- Version snapshots for published client views

### Out of MVP

- Full Topvisor API automation
- AI-generated full reports without human approval
- Client portal with login
- Billing / accounting
- CRM
- Complex BI dashboards
- Full task management system

MVP remains **internal-first**. Client delivery is controlled report links from **approved published snapshots**, not live drafts.

---

## 6. Key Product Decisions Needed Later

| Decision | Why it matters |
|----------|----------------|
| **Platform choice** | WP module vs custom PHP+MySQL vs hybrid — see Implementation Options Decision Frame |
| **File storage strategy** | Local disk, object storage, WP media — evidence volume and backups |
| **User auth model** | WP users vs app auth vs SSO later |
| **Published report access model** | Unlisted token / password / portal — security gate |
| **API / import scope** | What is manual vs automated in phase 2 |
| **Immutable snapshot strictness** | Soft vs strict immutability after publish |
| **Screenshot / evidence moderation** | What may appear on client snapshot |
| **Template customization rules** | Who may alter profiles/block matrix per project |

These are **decision gates**, not claims that solutions exist.

---

## 7. Relation to Demo v0.4

- Demo v0.4 remains the primary **UX reference** for specialist workspace, monthly/client flows, and visual direction.
- **Not all demo UI must survive** into the product.
- Specialist workspace is **likely core**.
- Monthly and client report flows are **likely core**.
- Some visual/extra/explanatory panels may be removed or reframed.
- **Architecture docs now take priority** over further demo polishing.
- Corrections discovered during architecture work are recorded in [I-SEO-REPORT-HUB-V0.5-DEMO-CORRECTIONS-BACKLOG-v0.1.md](I-SEO-REPORT-HUB-V0.5-DEMO-CORRECTIONS-BACKLOG-v0.1.md) — demo is **not** edited in this task.

---

## 8. Next Product Work

Immediate Layer 02 companions (same wave):

1. Role and permission model
2. Conceptual data model
3. Report lifecycle model
4. Publishing and snapshot model
5. Implementation options decision frame
6. v0.5 demo corrections backlog

After operator review of Layer 02:

- Scoped **commit** of architecture docs (operator-chartered)
- Then choose: **v0.5 demo corrections** **or** **MVP technical brief**

SEO feedback charter remains **deferred** until operator decides the product/demo is ready for specialist review.

---

## 9. Companion documents

| Document | Role |
|----------|------|
| [I-SEO-REPORT-HUB-ROLE-AND-PERMISSION-MODEL-v0.1.md](I-SEO-REPORT-HUB-ROLE-AND-PERMISSION-MODEL-v0.1.md) | Roles and matrix |
| [I-SEO-REPORT-HUB-DATA-MODEL-v0.1.md](I-SEO-REPORT-HUB-DATA-MODEL-v0.1.md) | Conceptual entities |
| [I-SEO-REPORT-HUB-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORT-LIFECYCLE-v0.1.md) | States and transitions |
| [I-SEO-REPORT-HUB-PUBLISHING-AND-SNAPSHOT-MODEL-v0.1.md](I-SEO-REPORT-HUB-PUBLISHING-AND-SNAPSHOT-MODEL-v0.1.md) | Client delivery snapshots |
| [I-SEO-REPORT-HUB-IMPLEMENTATION-OPTIONS-DECISION-FRAME-v0.1.md](I-SEO-REPORT-HUB-IMPLEMENTATION-OPTIONS-DECISION-FRAME-v0.1.md) | Platform options |
| [I-SEO-REPORT-HUB-V0.5-DEMO-CORRECTIONS-BACKLOG-v0.1.md](I-SEO-REPORT-HUB-V0.5-DEMO-CORRECTIONS-BACKLOG-v0.1.md) | Future demo fixes only |

Upstream: Product Charter, MVP Scope, Platform Options, Report Content Architecture, Admin UX Flow, Web Report Structure, WordPress architecture/data model (Option A artifacts).

---

## 10. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Final platform for MVP build | **UNKNOWN** — decision frame only |
| Exact hosting constraints on i-seo.su | **UNKNOWN** |
| Whether Account Manager is MVP-required | **UNKNOWN** — role defined; inclusion TBD |
| Exact client URL security mechanism | **UNKNOWN** — options documented |
| When SEO feedback charter opens | **UNKNOWN** — operator gate |

---

## Document control

- **Created:** 2026-07-24 (Product Architecture Layer 02)
- **Does not claim:** runtime, plugin, app, DB, API, or n8n workflow exists
- **Authority:** operator decision — v0.4 accepted as raw demo; proceed to product architecture; feedback deferred
