# REPORT — I-SEO REPORT HUB WORDPRESS DATA MODEL ADMIN UX PLANNING 01

**Task:** WordPress data model / admin UX planning (documentation-first)  
**Date:** 2026-07-10  
**Lane:** B — product formation and architecture  
**Branch:** `mars/canonical-post-recovery`  
**Commit:** None (per task charter)

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| **Repository root** | `X:\AI MARS` — confirmed |
| **Drive** | `X:` — confirmed |
| **Volume label** | `AI WS` — confirmed |
| **Branch** | `mars/canonical-post-recovery` — confirmed |
| **Staged changes** | Empty — confirmed |
| **Foreign WIP** | Present (unrelated modified/untracked files under `projects/mars-website-factory/`, `projects/ocpilot/`, `workspaces/`, `.recovery-temp/`, etc.) — **preserved, not touched** |
| **Read scope** | AGENTS.md, .cursorrules, i-SEO programme docs, Website Factory / Forge WordPress / MLI indexes, registry row — read |
| **Write scope** | `projects/iseo-report-hub/**` only — confirmed |

Preflight: **PASS** — no STOP tokens.

---

## 2. Scope

### Planned (done)

- WordPress domain entity model (20 entities) with fields, relationships, storage candidates, statuses, security
- Admin UX flows for specialist, reviewer, admin
- Weekly checkpoint and monthly report screen field inventories
- Client web report page structure and block types
- Implementation brief for future Anton / WordPress work
- Website Factory prototype candidate list (documentation only)
- n8n/AI boundary reaffirmation (external helper, draft-only AI, events not SoT)
- OPERATIONAL-INDEX update

### Not done (explicit)

- No WordPress code, PHP, JS, CSS, HTML
- No plugin scaffolding or database migrations
- No wp-admin or remote hosting access
- No n8n workflow changes
- No API integration
- No Website Factory workspace creation
- No registry update
- No git add / commit / push

---

## 3. Files Created

| Path |
|------|
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md` |
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md` |
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md` |
| `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md` |
| `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-wordpress-data-model-admin-ux-planning-01.md` |

---

## 4. Files Modified

| Path |
|------|
| `projects/iseo-report-hub/OPERATIONAL-INDEX.md` |

---

## 5. Summary of Planning Decisions

### Data model

- **20 domain entities** defined: Client through User/Role Assignment
- **Hybrid WordPress storage** recommended at product level: CPTs for major navigable objects (client, project, cycle, monthly); **custom tables** for block instances, metrics, completed works, reviews, events, published versions
- **Status vocabularies** defined for reporting cycle, weekly checkpoint, monthly final, review, published version
- **Data source modes** preserved from report model: manual, template, dictionary, external link, screenshot; later API and AI draft

### Admin UX

- **Five roles** scoped: Admin, SEO Lead/Reviewer, SEO Specialist, optional Account/Manager, client read-only later
- **16 admin areas** proposed (dashboard through settings)
- **13-step specialist monthly flow** from login through publish
- **Reviewer flow** via review queue with approve/revision
- **Validation rules** at product level (e.g. no publish without approval, executive summary required for monthly submit)

### Web report structure

- **Monthly client page** skeleton: header → meta → executive summary → KPI cards → traffic/positions/leads → works → optional weekly rollup → profile blocks → risks → plan → evidence → Topvisor card → footer
- **Weekly client page** defined for optional client-visible policy; internal-only assumed as MVP default
- **10 block render types** for client-facing output
- **URL strategy:** controlled private links; opaque token path candidate; final security **deferred**

### Implementation brief

- **12 MVP modules** listed for Anton handoff
- **10 pre-build gates** before implementation authorization
- Risks documented (WP complexity, access model, URL security, dictionary sanitization)

### Website Factory prototype candidates

High priority: client web report page, monthly editor, specialist dashboard. Medium: weekly editor, review queue, project detail, block layouts. **No workspace created.**

### n8n / AI boundaries

- n8n: reminders, completeness checks, notifications, delivery hooks — **events only**; WP remains SoT
- AI: draft assistance only; **no autonomous publication**
- Notification Event entity logs events for future consumption

---

## 6. MVP Boundary

### In

- Project/client management with profiles and assignments
- Monthly cycle + 3 weeklies + monthly final
- Work dictionary selection, manual metrics, evidence, Topvisor link
- Review/approval and published web report
- Basic notification event logging

### Out

- Client portal login
- API auto-import
- AI auto-publish
- Full n8n automation
- BI warehouse
- Required Topvisor iframe
- PDF primary delivery

---

## 7. Security Notes

- **Secrets excluded** from all report entities and documentation
- Nikita XLSX credential sheet class remains excluded from dictionary corpus
- **Private link mechanism deferred** — product requirements stated, implementation not chosen
- **Project-scoped access** required for specialists
- Integration credentials in **separate secure layer** — not in report tables
- Internal notes stripped from published snapshots

---

## 8. SAFE UNKNOWN

| Topic |
|-------|
| Final CPT vs custom table mapping per entity |
| Plugin packaging on i-seo.su (hosting constraints) |
| Admin UI: native wp-admin vs custom shell |
| Weekly checkpoint review requirement and client visibility policy |
| Private URL token format, expiry, revocation |
| Chart library selection |
| Immutable snapshot format (JSON vs normalized copy) |
| Work dictionary sanitized content (extraction gate pending) |
| Exact metric catalog per project profile |
| n8n webhook authentication design |
| ATLAS / OPS cross-program binding |
| i-seo.su coexistence with existing proposal generator module |

---

## 9. Recommended Next Action

**Operator review** of planning docs v0.1, then **choose one path:** optional Website Factory prototype charter **OR** implementation specification pass (leading to HITL charter for Anton).

---

## 10. Files Changed

**Created:**

- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-WEB-REPORT-STRUCTURE-v0.1.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-wordpress-data-model-admin-ux-planning-01.md`

**Modified:**

- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

**Not changed:** `registry/project-registry.md` or any path outside `projects/iseo-report-hub/**`

---

## 11. Git Actions

| Action | Status |
|--------|--------|
| git add | **No** |
| git commit | **No** |
| git push | **No** |
| git checkout | **No** |
| git reset | **No** |
| git clean | **No** |

---

## Validation checklist

| Check | Result |
|-------|--------|
| Changes only under `projects/iseo-report-hub/**` | Pass |
| No registry changes | Pass |
| No code files created | Pass |
| No Website Factory workspace | Pass |
| No secrets/credentials printed | Pass |
| No deprecated C:/D:/E: paths as current targets | Pass |
| Docs do not claim implementation exists | Pass |
| n8n remains external helper, not SoT | Pass |
| Website Factory remains prototype lane | Pass |
