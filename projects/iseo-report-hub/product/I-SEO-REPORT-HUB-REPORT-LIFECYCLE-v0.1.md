# I-SEO Report Hub — Report Lifecycle v0.1

**Status:** PLANNING — product architecture Layer 02 companion  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-24  
**Implementation:** **NOT STARTED**

---

## 1. Status

Defines lifecycle states for **reporting periods**, **weekly checkpoints**, **monthly reports**, and **report blocks**. Aligns with Demo Report States v0.1 (demo scenarios) but is product-level, not demo-only.

---

## 2. Reporting Period States

| State | Meaning |
|-------|---------|
| `planned` | Period created; work not started |
| `active_week_1` | Week 1 checkpoint in progress |
| `active_week_2` | Week 2 checkpoint in progress |
| `active_week_3` | Week 3 checkpoint in progress |
| `monthly_draft` | Month-close report being composed |
| `review` | Monthly (or period) under review |
| `revision_requested` | Reviewer sent back for changes |
| `approved` | Monthly approved; not yet published (or publish pending) |
| `published` | Client snapshot live |
| `archived` | Closed historical period |

### Period transitions (happy path)

```
planned → active_week_1 → active_week_2 → active_week_3 → monthly_draft
  → review → approved → published → archived
```

Revision branch: `review → revision_requested → monthly_draft|review` (after specialist edits).

### Who can move period states

| Transition | Typical actor |
|------------|---------------|
| planned → active_week_* | Specialist / system when W1 opens |
| week advances | Specialist completing prior week **or** Admin override |
| → monthly_draft | Specialist / automatic when W3 rolled |
| → review | Specialist (submit monthly) |
| → revision_requested | Lead / Admin |
| → approved | Lead / Admin |
| → published | Lead / Admin (per policy) |
| → archived | Admin (or Lead with policy) |

---

## 3. Weekly Checkpoint States

| State | Meaning |
|-------|---------|
| `not_started` | Shell exists; empty |
| `draft` | Specialist editing |
| `ready_for_review` | Submitted for optional weekly review |
| `reviewed` | Lead acknowledged / reviewed |
| `rolled_into_monthly` | Content synthesized into monthly |

### Weekly transitions

```
not_started → draft → ready_for_review → reviewed → rolled_into_monthly
```

Skip path (MVP): `draft → rolled_into_monthly` if weekly formal review is optional.

### Who can move weekly states

| Action | Actor |
|--------|-------|
| Create/edit draft | Specialist (assigned) |
| Submit ready_for_review | Specialist |
| Mark reviewed | Lead / Admin |
| Roll into monthly | Specialist during monthly synthesis / system assist |

---

## 4. Monthly Report States

| State | Meaning |
|-------|---------|
| `shell` | Created from period; blocks empty |
| `draft` | Specialist composing |
| `ready_for_review` | Submitted |
| `revision_requested` | Returned |
| `approved` | Cleared for publish |
| `published` | Snapshot published |
| `superseded` | Newer published version exists |
| `archived` | Historical; not active |

### Monthly transitions

```
shell → draft → ready_for_review → approved → published
                      ↓
              revision_requested → draft
published → superseded (when new version published)
published|superseded → archived
```

---

## 5. Report Block States

| State | Meaning |
|-------|---------|
| `empty` | Required or optional block with no content |
| `draft` | Partially filled |
| `needs_evidence` | Claims lack evidence |
| `needs_client_text` | Client-facing copy incomplete |
| `ready_for_review` | Block complete for review |
| `approved` | Block cleared |
| `hidden_internal` | Internal-only; never client |
| `published` | Included in live snapshot (client-visible subset) |

### Block transitions

```
empty → draft → needs_evidence|needs_client_text → ready_for_review → approved → published
draft → hidden_internal (if internal-only block)
```

Hidden/internal blocks never enter client snapshot payload.

---

## 6. Validation Gates

### Before weekly `ready_for_review` (if used)

- Required weekly fields not empty (per profile)
- No secrets in free text (policy check — product rule)

### Before monthly `ready_for_review`

- Required blocks per Block Matrix ≠ `empty`
- KPI snapshot present for required KPIs
- Evidence attached where blocks require it
- Client-facing summaries present (no internal-only leakage flagged)

### Before `approved`

- Lead checklist complete
- Internal notes reviewed for accidental client exposure

### Before `published`

- Monthly state = `approved`
- Snapshot built excluding excluded fields (see Publishing model)
- Access token / URL policy applied

### Client report availability

Client URL resolves **only** when a `published_snapshots` row is `live`. Drafts and weeklies do not unlock client page by default.

---

## 7. Edit After Publish

| Approach | Behavior |
|----------|----------|
| **Recommended** | Edits go to a new draft / revision; republish creates **new snapshot**; old snapshot → `superseded` |
| **Forbidden for MVP** | Silently mutating the live snapshot without version bump |
| Unpublish | Snapshot → revoked/unavailable; period may return to `approved` or stay `published` with revoked flag — policy TBD |

---

## 8. MVP Simplification

MVP may:

- Treat weekly formal review as **optional** (`draft → rolled_into_monthly`)
- Collapse period states to fewer UI labels while keeping finer states in data
- Allow Admin to force transitions with **audit**
- Defer `superseded` UI until second publish exists

MVP must **not** skip: monthly review before publish; snapshot separation from draft.

---

## 9. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Are weeklies ever client-visible in MVP? | **UNKNOWN** — default No |
| Automatic week advance vs manual | **UNKNOWN** |
| Exact timeout/SLA for review | **UNKNOWN** |
| Whether approved implies auto-publish | **UNKNOWN** — default separate publish action |

---

## Document control

- **Created:** 2026-07-24  
- **Does not claim:** workflow engine or state machine implemented
