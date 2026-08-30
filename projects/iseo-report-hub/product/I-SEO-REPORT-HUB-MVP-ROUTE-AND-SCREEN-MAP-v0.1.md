# I-SEO Report Hub — MVP Route and Screen Map v0.1

**Status:** CONCEPTUAL ROUTE MAP — not implemented  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED**

**Basis:** [PHP + MySQL MVP Technical Brief](I-SEO-REPORT-HUB-PHP-MYSQL-MVP-TECHNICAL-BRIEF-v0.1.md), [Role and Permission Model](I-SEO-REPORT-HUB-ROLE-AND-PERMISSION-MODEL-v0.1.md)

---

## 1. Status

Conceptual PHP application routes for MVP. No router code exists. Path styles are illustrative (`{id}` placeholders).

---

## 2. Route catalog

### `/login`

| Field | Value |
|-------|-------|
| **Purpose** | Authenticate internal user |
| **Primary role** | Anonymous → all internal roles |
| **Read/write** | Write (credentials POST) |
| **Entities** | users, sessions |
| **MVP** | Yes |

### `/logout`

| Field | Value |
|-------|-------|
| **Purpose** | End session |
| **Primary role** | Any authenticated |
| **Read/write** | Write |
| **Entities** | sessions |
| **MVP** | Yes |

### `/`

| Field | Value |
|-------|-------|
| **Purpose** | Dashboard — assigned work, period readiness, review cues |
| **Primary role** | All authenticated (scoped) |
| **Read/write** | Read |
| **Entities** | projects, periods, monthly_reports |
| **MVP** | Yes |

### `/clients`

| Field | Value |
|-------|-------|
| **Purpose** | List clients |
| **Primary role** | Admin (Lead: view if policy allows) |
| **Read/write** | Read |
| **Entities** | clients |
| **MVP** | Yes |

### `/clients/new`

| Field | Value |
|-------|-------|
| **Purpose** | Create client |
| **Primary role** | Admin |
| **Read/write** | Write |
| **Entities** | clients |
| **MVP** | Yes |

### `/clients/{id}`

| Field | Value |
|-------|-------|
| **Purpose** | Client detail + linked projects |
| **Primary role** | Admin |
| **Read/write** | Read / write (edit) |
| **Entities** | clients, projects |
| **MVP** | Yes |

### `/projects`

| Field | Value |
|-------|-------|
| **Purpose** | List projects (scoped by role) |
| **Primary role** | Admin / Lead / Specialist (assigned) |
| **Read/write** | Read |
| **Entities** | projects, clients |
| **MVP** | Yes |

### `/projects/{id}`

| Field | Value |
|-------|-------|
| **Purpose** | Project detail: sites, assignments, periods entry |
| **Primary role** | Admin / assigned Specialist / Lead |
| **Read/write** | Read; write Admin (and limited Lead if policy) |
| **Entities** | projects, sites, users, periods |
| **MVP** | Yes |

### `/projects/{id}/periods`

| Field | Value |
|-------|-------|
| **Purpose** | List / create reporting periods for project |
| **Primary role** | Admin / assigned Specialist |
| **Read/write** | Read / write (create) |
| **Entities** | reporting_periods |
| **MVP** | Yes |

### `/periods/{id}`

| Field | Value |
|-------|-------|
| **Purpose** | Period detail and lifecycle overview |
| **Primary role** | Assigned Specialist / Lead / Admin |
| **Read/write** | Read; limited write for state advances |
| **Entities** | reporting_periods, weekly_checkpoints, monthly_reports |
| **MVP** | Yes |

### `/periods/{id}/workspace`

| Field | Value |
|-------|-------|
| **Purpose** | Specialist workspace for the period |
| **Primary role** | Assigned Specialist |
| **Read/write** | Read / write |
| **Entities** | periods, blocks, work_items, kpi_values, evidence |
| **MVP** | Yes |

### `/periods/{id}/weekly/{week}`

| Field | Value |
|-------|-------|
| **Purpose** | Weekly checkpoint editor (week 1–3) |
| **Primary role** | Assigned Specialist |
| **Read/write** | Read / write |
| **Entities** | weekly_checkpoints, report_blocks, evidence |
| **MVP** | Yes |

### `/periods/{id}/monthly`

| Field | Value |
|-------|-------|
| **Purpose** | Monthly report editor |
| **Primary role** | Assigned Specialist |
| **Read/write** | Read / write (submit) |
| **Entities** | monthly_reports, report_blocks, kpi_values |
| **MVP** | Yes |

### `/reports/{id}/review`

| Field | Value |
|-------|-------|
| **Purpose** | Review queue item — request changes / approve |
| **Primary role** | Lead / Admin |
| **Read/write** | Read / write |
| **Entities** | monthly_reports, reviewer_comments, audit_log |
| **MVP** | Yes |

### `/reports/{id}/preview`

| Field | Value |
|-------|-------|
| **Purpose** | Internal client-safe preview before/after publish |
| **Primary role** | Specialist (assigned) / Lead / Admin |
| **Read/write** | Read |
| **Entities** | monthly_reports or published_snapshots |
| **MVP** | Yes |

### `/p/{token}`

| Field | Value |
|-------|-------|
| **Purpose** | **Public** published client report (token) |
| **Primary role** | Unauthenticated client holder of link |
| **Read/write** | Read only |
| **Entities** | published_snapshots only |
| **MVP** | Yes |

### `/settings/templates`

| Field | Value |
|-------|-------|
| **Purpose** | Block templates / matrix settings |
| **Primary role** | Admin |
| **Read/write** | Read / write |
| **Entities** | project_type_profiles, template definitions |
| **MVP** | Yes |

### `/settings/users`

| Field | Value |
|-------|-------|
| **Purpose** | Users and role assignment |
| **Primary role** | Admin |
| **Read/write** | Read / write |
| **Entities** | users, roles, user_roles |
| **MVP** | Yes |

### `/settings/project-types`

| Field | Value |
|-------|-------|
| **Purpose** | Project type profiles |
| **Primary role** | Admin |
| **Read/write** | Read / write |
| **Entities** | project_type_profiles |
| **MVP** | Yes |

---

## 3. Navigation model

| Area | Typical entry |
|------|----------------|
| Global | Dashboard `/` |
| Structure | Clients → Projects → Periods |
| Authoring | Period → Workspace → Weekly / Monthly |
| Quality | Review queue (Lead) → `/reports/{id}/review` |
| Delivery | Preview → Publish → share `/p/{token}` |
| Admin | Settings (templates, users, project types) |

Specialist navigation is **assignment-scoped**. Admin sees all. Lead sees team/review scope per Role Model.

UX layout may follow static demo v0.4, but routes above are the product map.

---

## 4. Permission checkpoints

On every authenticated route:

1. Session valid
2. Role capability allows action
3. Resource scope (project assignment) for Specialist
4. CSRF on POST/PUT/PATCH/DELETE
5. Server-side validation

On `/p/{token}`:

1. No session required
2. Token entropy + lookup
3. Snapshot `status = live` (or explicit superseded view policy — **SAFE UNKNOWN**)
4. Payload already client-safe (no internal notes)
5. Prefer not to leak existence of invalid tokens (generic 404)

---

## 5. Client public route isolation

| Rule | Detail |
|------|--------|
| Isolation | `/p/{token}` must not share admin layout, internal nav, or draft queries |
| Data source | `published_snapshots` only |
| Auth | Token is the access secret; not WP cookies |
| Logging | Optional access audit — **SAFE UNKNOWN** if required for MVP |

---

## 6. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Exact URL prefix / subdirectory on production host | **SAFE UNKNOWN** |
| Whether review queue uses `/reviews` list route | Optional later |
| Password-protected client URL layer | Optional; not required for MVP token model |
| Account Manager dedicated routes | May reuse preview + project read — exact set TBD |
| HTTP method conventions (REST vs form POST) | TBD in Phase 1 |

---

## 7. Boundaries

- Conceptual only — no router implementation.
- Does not authorize creating PHP files.
- Aligns with Platform Decision: no WordPress admin routes as product SoT.
