# I-SEO Report Hub — Role and Permission Model v0.1

**Status:** PLANNING — product architecture Layer 02 companion  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED**

---

## 1. Status

Defines **who may do what** in Report Hub. Platform-neutral: applies whether MVP is WordPress, custom PHP+MySQL, or hybrid.

No runtime roles exist yet. This is documentation only.

---

## 2. Roles

### 2.1 Admin / Owner

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Full system configuration, user management, policy overrides, dictionary/templates |
| **Typical users** | Nikita / i-SEO leadership; product owner as needed |

| Capability | Allowed |
|------------|---------|
| Create/edit/delete clients | Yes |
| Create/edit projects | Yes |
| Create/edit periods | Yes |
| Fill weekly checkpoints | Yes (override; not primary workflow) |
| Fill monthly reports | Yes (override; not primary workflow) |
| Upload/add evidence | Yes |
| See internal notes | Yes |
| Send to review | Yes |
| Approve | Yes |
| Publish | Yes |
| Unpublish | Yes |
| View published reports | Yes |
| Comment | Yes |
| Manage templates | Yes |
| Manage users | Yes |

### 2.2 SEO Lead / Reviewer

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Quality gate: review queue, approve/revision, team-scoped visibility |
| **Typical users** | Senior SEO / team lead |

| Capability | Allowed |
|------------|---------|
| Create/edit/delete clients | No (create/edit: optional later; delete: No) |
| Create/edit projects | Edit scoped metadata: optional; create: No by default |
| Create/edit periods | View all in scope; create: if assigned lead — **SAFE UNKNOWN** default No |
| Fill weekly checkpoints | View; limited edit only if also specialist on project |
| Fill monthly reports | View; limited edit only if also specialist |
| Upload/add evidence | View; add only if editing as specialist |
| See internal notes | Yes |
| Send to review | No (receives submissions) |
| Approve | Yes |
| Publish | Yes (if policy allows lead publish) |
| Unpublish | Prefer Admin; Lead: optional with audit — MVP: Yes with audit |
| View published reports | Yes |
| Comment | Yes (reviewer comments) |
| Manage templates | No (recommend only) |
| Manage users | No |

### 2.3 SEO Specialist

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Primary author of weekly checkpoints and monthly drafts for assigned projects |
| **Typical users** | Denis, Ilya, and i-SEO SEO team |

| Capability | Allowed |
|------------|---------|
| Create/edit/delete clients | No |
| Create/edit projects | No (view assigned only) |
| Create/edit periods | Create/edit for assigned projects (within policy) |
| Fill weekly checkpoints | Yes (assigned) |
| Fill monthly reports | Yes (assigned) |
| Upload/add evidence | Yes (assigned) |
| See internal notes | Yes (own projects) |
| Send to review | Yes |
| Approve | No |
| Publish | No |
| Unpublish | No |
| View published reports | Yes (assigned projects) |
| Comment | Yes (author replies / notes) |
| Manage templates | No |
| Manage users | No |

### 2.4 Account / Client Manager

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Client delivery liaison: view readiness, share links, light comments |
| **Typical users** | Account / client managers |

| Capability | Allowed |
|------------|---------|
| Create/edit/delete clients | Edit contact fields: optional; delete: No |
| Create/edit projects | View; limited commercial fields: optional |
| Create/edit periods | View only |
| Fill weekly checkpoints | No |
| Fill monthly reports | No |
| Upload/add evidence | No |
| See internal notes | No (client-safe summaries only) |
| Send to review | No |
| Approve | No |
| Publish | No (may flag “sent to client” after published) |
| Unpublish | No |
| View published reports | Yes |
| Comment | Yes (delivery / client feedback notes — client-safe) |
| Manage templates | No |
| Manage users | No |

### 2.5 Read-only Internal Viewer

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Internal observation without mutation (training, oversight, audit) |
| **Typical users** | Observing leads, product, trusted staff |

| Capability | Allowed |
|------------|---------|
| Create/edit/delete clients | No |
| Create/edit projects | No |
| Create/edit periods | No |
| Fill weekly checkpoints | No |
| Fill monthly reports | No |
| Upload/add evidence | No |
| See internal notes | Yes (if granted “internal viewer” scope) |
| Send to review | No |
| Approve | No |
| Publish | No |
| Unpublish | No |
| View published reports | Yes |
| Comment | No |
| Manage templates | No |
| Manage users | No |

### 2.6 Client Viewer

| Dimension | Detail |
|-----------|--------|
| **Purpose** | Consume approved published snapshot only |
| **Typical users** | Client stakeholders via controlled link (MVP: no login portal) |

| Capability | Allowed |
|------------|---------|
| Create/edit/delete clients | No |
| Create/edit projects | No |
| Create/edit periods | No |
| Fill weekly checkpoints | No |
| Fill monthly reports | No |
| Upload/add evidence | No |
| See internal notes | No |
| Send to review | No |
| Approve | No |
| Publish | No |
| Unpublish | No |
| View published reports | Yes — **published snapshot only** |
| Comment | No in MVP (later optional) |
| Manage templates | No |
| Manage users | No |

---

## 3. Permission Matrix

Legend: **Y** = yes · **N** = no · **S** = scoped (assigned projects / team) · **O** = optional / policy · **—** = N/A

| Permission | Admin | Lead | Specialist | Account | Internal RO | Client |
|------------|-------|------|------------|---------|-------------|--------|
| Create/edit clients | Y | N/O | N | O | N | N |
| Delete clients | Y | N | N | N | N | N |
| Create/edit projects | Y | O | N | O | N | N |
| Create/edit periods | Y | O | S | N | N | N |
| Fill weekly | Y | S* | S | N | N | N |
| Fill monthly | Y | S* | S | N | N | N |
| Add evidence | Y | S* | S | N | N | N |
| See internal notes | Y | Y | S | N | Y | N |
| Send to review | Y | N | S | N | N | N |
| Approve | Y | Y | N | N | N | N |
| Publish | Y | O | N | N | N | N |
| Unpublish | Y | O | N | N | N | N |
| View published | Y | Y | S | Y | Y | Y† |
| Comment | Y | Y | S | O | N | N‡ |
| Manage templates | Y | N | N | N | N | N |
| Manage users | Y | N | N | N | N | N |

\* Lead fills only if also specialist on that project.  
† Client: via controlled URL / future portal to published snapshot only.  
‡ Client comments: post-MVP if needed.

---

## 4. MVP Roles vs Future Roles

| Role | MVP | Future |
|------|-----|--------|
| Admin / Owner | **Required** | Required |
| SEO Lead / Reviewer | **Required** (may be same person as Admin early) | Required |
| SEO Specialist | **Required** | Required |
| Account / Client Manager | **Optional** — may defer | Likely |
| Read-only Internal Viewer | Optional / thin | Useful for audit |
| Client Viewer | **Delivery role** via link — not a full login user in MVP | Portal login optional later |

---

## 5. Client Access Boundary

- Client Viewer **never** sees drafts, weekly raw checkpoints (unless later product decision makes weeklies client-visible), internal notes, reviewer comments, raw source dumps, or secrets.
- Client access is to **published snapshots** only.
- Sharing a client URL must not grant admin workspace access.
- Revoke / unpublish must invalidate or soft-block the client view.

---

## 6. Audit Log Needs

MVP should plan to record (implementation later):

| Event | Why |
|-------|-----|
| Role/user changes | Accountability |
| Submit for review | Workflow evidence |
| Approve / revision requested | Gate history |
| Publish / unpublish | Client delivery audit |
| Snapshot create / supersede | Version integrity |
| Template/profile changes | Content integrity |
| Evidence add/remove on published-bound items | Moderation trail |

Exact retention and storage: **SAFE UNKNOWN**.

---

## 7. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Whether Lead may publish without Admin | **UNKNOWN** — policy |
| Whether Account Manager is required day one | **UNKNOWN** |
| Team-scoped vs all-project Lead visibility | **UNKNOWN** |
| Multi-specialist per project | **UNKNOWN** |
| Client comment feature | **UNKNOWN** business need |

---

## Document control

- **Created:** 2026-07-24  
- **Does not claim:** any auth system or roles implemented  
- **Upstream:** Admin UX Flow v0.1 roles; Product Architecture Layer 02
