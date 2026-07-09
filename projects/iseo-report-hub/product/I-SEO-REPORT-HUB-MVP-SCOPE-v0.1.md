# i-SEO Report Hub — MVP Scope v0.1

**Status:** APPROVED scope persist 2026-07-10  
**Implementation:** **NOT STARTED**

---

## 1. MVP intent

Deliver a **WordPress internal Report Hub** on i-seo.su that allows i-SEO specialists to run monthly reporting cycles (3 weekly checkpoints + 1 monthly final), compose reports from blocks and work dictionary, attach evidence, pass review/approval, and publish **controlled client web reports**.

MVP is **internal-first**. Client delivery is via controlled web report links, not a full client portal.

---

## 2. In MVP

| # | Capability | Notes |
|---|------------|-------|
| 1 | **WordPress internal Report Hub admin/workspace** | Custom module on i-seo.su — implementation not started |
| 2 | **SEO specialist roles and scoped project access** | Specialist sees assigned projects only |
| 3 | **Client/project records** | Basic project profile |
| 4 | **Project type profile** | service / e-commerce / local / B2B / content / technical / custom |
| 5 | **Monthly reporting cycle** | One cycle per project per month |
| 6 | **Three weekly checkpoints** | Weeks 1–3 preliminary reports |
| 7 | **Monthly final report** | Month-close comprehensive report |
| 8 | **Report block library** | Required/optional/profile blocks |
| 9 | **Work dictionary** | Canonical work items with client-facing wording |
| 10 | **Manual metric entry** | Specialist-entered values; charts from entered data |
| 11 | **Evidence links/screenshots/files** | Attach to works and report sections |
| 12 | **Topvisor external report link field** | URL + optional preview — no required iframe |
| 13 | **Web report renderer on i-seo.su** | Client-facing approved report pages |
| 14 | **Review/approval workflow** | Submit → review → revision → approve |
| 15 | **Publish/export state** | Track client-ready and published/sent |
| 16 | **Basic notification event model** | Event definitions for future n8n (no live automation required in MVP) |

---

## 3. Out of MVP

| # | Excluded capability | Reason / deferral |
|---|---------------------|-------------------|
| 1 | **Full client portal with login** | Controlled links sufficient for MVP |
| 2 | **Automatic API integrations** | Manual entry + external links first |
| 3 | **Automatic AI publication** | AI draft only when added; never auto-publish |
| 4 | **Complete BI warehouse** | Report Hub ≠ analytics platform |
| 5 | **Live iframe dependency** | Topvisor link/screenshot sufficient |
| 6 | **Secrets management inside report tables** | Security policy exclusion |
| 7 | **Autonomous n8n orchestration** | Events defined; automation later |
| 8 | **PDF export as primary delivery** | Web report primary; PDF optional later |
| 9 | **Public unrestricted report URLs** | Private/controlled delivery only |
| 10 | **Multi-language client reports** | **SAFE UNKNOWN** need — default single language |
| 11 | **ATLAS live consumer integration** | Optional later |
| 12 | **OPS runtime binding** | Documentation alignment only at this stage |

---

## 4. MVP acceptance boundaries (draft)

MVP is **accepted** when (implementation phase — criteria for future charter):

1. Specialist can create monthly cycle for assigned project.
2. Specialist can complete 3 weekly checkpoints and 1 monthly final.
3. Work dictionary entries selectable in completed works blocks.
4. Manual metrics enterable and visible in report render.
5. Evidence (link + screenshot) attachable and visible in report.
6. Topvisor external link storable and displayed on client web report.
7. Reviewer can approve or request revision.
8. Approved monthly report renders as client web page on i-seo.su.
9. Published state recorded with timestamp/history.
10. No credentials/secrets storable in report fields (enforced by design).
11. Notification event hooks documented for n8n (even if not wired).

Exact test plan: **SAFE UNKNOWN** — defined in implementation charter.

---

## 5. Later phases

### Phase 2 — Integrations (post-MVP)

| Integration | Purpose |
|-------------|---------|
| **Topvisor API** | Metric import |
| **Yandex Metrika** | Traffic/conversion import |
| **Yandex Webmaster** | Indexation/search data |
| **Google Search Console** | Search performance |
| **GA4** | Analytics cross-check |
| **CRM / calls** | Lead attribution |

### Phase 3 — Automation & AI

| Capability | Boundary |
|------------|----------|
| **n8n bot reminders** | Checkpoint due, month close |
| **AI drafts** | Section drafts — human approval required |
| **Automated completeness checks** | Missing field alerts via n8n |
| **Approved report delivery** | Telegram/email triggers after human approval |

### Phase 4 — Client experience (if proven needed)

| Capability | Notes |
|------------|-------|
| **Client portal with login** | Only if controlled links insufficient |
| **PDF export** | Secondary format |
| **iframe/embed Topvisor** | Only if technically and legally safe |
| **Client comment/reaction** | **SAFE UNKNOWN** business need |

---

## 6. Dependencies before implementation

1. Operator approval of architecture v0.1
2. WordPress data model design
3. Work dictionary sanitized extraction
4. Private report URL security design
5. Explicit implementation charter (HITL) for i-seo.su deployment
6. Hosting review for custom WP module constraints

---

## 7. SAFE UNKNOWN

- MVP timeline and resource allocation
- Whether weekly checkpoints are client-visible in MVP
- Exact chart types in MVP renderer
- File upload size limits
- Number of concurrent projects supported day one
- Migration path for historical PDF reports from corpus

---

## Document control

- **Created:** 2026-07-10
- **No implementation code** in this document or programme folder yet
