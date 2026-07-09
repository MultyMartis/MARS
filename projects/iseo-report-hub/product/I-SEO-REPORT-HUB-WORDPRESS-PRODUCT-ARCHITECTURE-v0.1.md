# i-SEO Report Hub — WordPress Product Architecture v0.1

**Status:** DRAFT (approved direction persist 2026-07-10)  
**Platform:** WordPress on i-seo.su  
**Implementation:** **NOT STARTED** — architecture documentation only

---

## 1. High-level architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     i-seo.su (WordPress)                       │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              Report Hub — SOURCE OF TRUTH                    │  │
│  │  Admin/workspace │ Cycles │ Reports │ Dictionary │ Evidence │  │
│  │  Review/Approval │ Publish state │ Web Report Renderer      │  │
│  └───────────────────────────────────────────────────────────┘  │
│         │ client web reports (controlled URLs)                   │
└─────────┼────────────────────────────────────────────────────────┘
          │
          ▼
    Client (read-only web report)

┌─────────────────────────────────────────────────────────────────┐
│              External operator n8n server                        │
│  AI draft assist │ Reminders │ Alerts │ Delivery notifications   │
│  ** NOT source of truth — events/triggers only **                │
└─────────────────────────────────────────────────────────────────┘
          ▲
          │ future webhooks / scheduled checks (read-only or draft)
          │
    WordPress Report Hub

┌─────────────────────────────────────────────────────────────────┐
│              Future external APIs (post-MVP)                     │
│  Topvisor │ Metrika │ GSC │ GA4 │ Yandex Webmaster │ CRM       │
└─────────────────────────────────────────────────────────────────┘
```

**Hosting split:**
- **Programmatic/reporting processes:** i-seo.su WordPress hosting
- **AI/n8n automation:** external user n8n server

---

## 2. Data ownership

**WordPress on i-seo.su owns (source of truth):**

- All report entities and versions
- Reporting cycles and statuses
- Work dictionary (canonical entries)
- Manual metric snapshots
- Evidence metadata (links, files, screenshots)
- External report links (Topvisor, etc.)
- Review/approval state
- Publish/export history
- Client-facing web report rendered content (approved versions)

**WordPress does NOT own (external):**
- Live Topvisor/Metrika/GSC metric APIs (until integrated)
- n8n workflow state
- Credential vaults
- MARS documentation

---

## 3. WP admin/workspace modules

| Module | Function |
|--------|----------|
| **Clients / Projects** | Client records, project profiles, specialist assignment, scoped access |
| **SEO Specialist Dashboard** | Active cycles, pending checkpoints, review queue, deadlines |
| **Reporting Cycles** | Monthly cycle container per project |
| **Weekly Checkpoints** | Week 1–3 preliminary reports |
| **Monthly Final Reports** | Month-close comprehensive report |
| **Block Library** | Reusable report blocks (required/optional/profile-specific) |
| **Work Dictionary** | Canonical work items, client-facing wording, applicability |
| **Metrics** | Manual metric entry, snapshots, chart data from entered/imported values |
| **Evidence** | Links, files, screenshots attached to works or report sections |
| **External Links** | Topvisor report URL, other third-party report links |
| **Review / Approval** | Reviewer workflow, revision requests, approval gates |
| **Publish / Export** | Client-ready state, web report publication, export history |

---

## 4. Roles

| Role | Access | Notes |
|------|--------|-------|
| **Admin / Owner** | Full system config, all projects, dictionary management | Nikita / i-SEO leadership |
| **SEO Lead / Reviewer** | Review queue, approve/reject, all or team-scoped projects | Approval authority |
| **SEO Specialist** | Assigned projects only; create/edit drafts; submit for review | Primary data entry |
| **Account / Manager** | Optional read + comment; may trigger client delivery | **Optional** — MVP TBD |
| **Client read-only** | View approved web report only | **Later optional** — not MVP login portal |

Role-capability matrix detail: **SAFE UNKNOWN** until admin UX planning.

---

## 5. Security

| Rule | Requirement |
|------|-------------|
| **No secrets in reports** | Access credentials, passwords, API keys — **never** in report tables or client exports |
| **Private report links** | Client reports via controlled URL (token/private), not public unrestricted canonical URLs |
| **Project-scoped access** | Specialists see only assigned projects |
| **Approval before publication** | No client-visible report without approved state |
| **Export history** | Audit trail of what was published/sent and when |
| **Credential materials exclusion** | Nikita XLSX Лист2 class content excluded from corpus and system |
| **AI draft boundary** | AI-generated content stays draft until human approval |

Private link mechanism (token length, expiry, auth): **SAFE UNKNOWN** — implementation planning gate.

---

## 6. n8n boundary

**n8n = external helper, NOT source of truth.**

**May later support:**
- AI assistance (draft generation)
- Reminders (checkpoint due, month close)
- Report readiness checks (missing fields)
- Specialist pings
- Missing-field alerts
- Review notifications
- Approved report delivery triggers
- Telegram/bot workflows
- Future API integration glue

**n8n must NOT:**
- Own report data or canonical status
- Auto-publish to clients without human approval gate
- Replace WordPress admin as primary workspace
- Store credentials in report-accessible locations

**Integration pattern:** WordPress emits **events** (webhook or polled); n8n reacts; writes back only via defined WP API/admin actions with human gate where required.

**Current state:** no n8n workflow exists for Report Hub.

---

## 7. AI boundary

| Allowed | Forbidden |
|---------|-----------|
| Draft text for report sections | Autonomous client publication |
| Suggest work dictionary wording | Overwrite approved reports silently |
| Completeness hints (via n8n) | Include credentials in prompts |
| Summarize entered metrics | Replace human specialist interpretation as final authority |

**Rule:** AI assistance = **draft only**; human approval required for review submission and client publication.

---

## 8. Topvisor strategy

**MVP:**
- External online report **link field** (acceptable primary pattern from Ilya-style reports)
- Screenshots/previews attached as evidence (acceptable)
- No required live iframe/embed

**Later (optional):**
- iframe/embed only if technically and legally safe
- Topvisor API import (post-MVP integration phase)

---

## 9. Client web report renderer

**Primary client output:** web pages generated on i-seo.su by WordPress/custom reporting module.

**Characteristics:**
- Rendered from **approved** report version only
- Controlled/private delivery (secure link or controlled URL)
- Not editable by client
- PDF/export may be added later — web report remains primary

**Renderer implementation:** **NOT STARTED** — WordPress theme/module decision deferred to implementation charter.

---

## 10. Relationship to MARS ecosystem

| MARS component | Relationship |
|----------------|--------------|
| **Forge WordPress** | Possible methodology for WP implementation packaging — **not** auto-implementation |
| **WPilot** | Possible future bridge for WP admin operations — **not** architecture owner |
| **MARS Localhost** | Local dev only — production is i-seo.su external hosting |
| **OPS** | Operational process patterns (monthly reporting WF-01) — consumer/reference, not owner |
| **ATLAS** | Business identity — optional future consumer for client/project records |
| **MetaBOT / n8n** | External automation per boundary above |

---

## 11. Website Factory UI / Prototype Boundary

**Production target unchanged:** Report Hub production and client web reports remain **WordPress on i-seo.su** — source of truth, admin workspace, and approved report renderer.

**Website Factory role (MARS documentation + future workspace lane):**
- Preferred methodology for **HTML/static UI demos**, visual/UX exploration, and screen sketches **before** WordPress implementation.
- May prototype: SEO specialist admin UI, client web report page layouts, weekly checkpoint screens, monthly final report screens, report block compositions.
- Uses existing MARS gulp starter / Website Factory build approach when a demo workspace is chartered — **not** automatic factory runtime.

**Explicit exclusions:**
- Website Factory **does not** own Report Hub runtime, production deployment, or WordPress plugin/module implementation.
- Website Factory output is **not** the deployed Report Hub or client-facing production reports.
- **No demo workspace** is created by documentation tasks alone.

**Future workspace:** A Report Hub–scoped Website Factory workspace may be created **only** under a separate operator charter (HITL). This architecture persist task creates **documentation binding only**.

---

## 12. SAFE UNKNOWN

- Custom post types vs custom tables vs hybrid storage on WordPress
- Plugin vs theme-module vs site-specific mu-plugin packaging
- ACF/ACF-like field strategy for report blocks
- Multisite vs single-site assumptions on i-seo.su
- File upload storage quotas and retention policy
- Chart rendering library on WordPress admin and client web report
- Webhook authentication between WP and n8n

---

## Document control

- **Created:** 2026-07-10
- **No code, no plugin, no deployment** claimed or included
