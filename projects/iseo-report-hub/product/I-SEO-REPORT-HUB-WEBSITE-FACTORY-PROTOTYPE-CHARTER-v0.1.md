# I-SEO Report Hub — Website Factory Prototype Charter v0.1

**Status:** PLANNING — documentation-first charter only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10  
**Implementation:** **NOT STARTED** — no demo built, no workspace created

---

## 1. Status and Scope

This document is a **documentation-first charter** for a future Website Factory HTML/static prototype of i-SEO Report Hub.

| Fact | State |
|------|-------|
| Static HTML demo | **Does not exist** |
| Website Factory workspace | **Not created** |
| WordPress implementation | **Not started** |
| n8n workflows | **Do not exist** |
| Runtime / plugin / API | **None** |

A clickable or navigable static prototype requires a **separate operator-approved build task** with its own HITL charter. This document defines scope and boundaries only; it does **not** authorize build, deployment, or workspace creation.

**Authority commits for this programme lane (reference only):**
- `56d8e755` — initial programme persist
- `1dbff9c6` — Website Factory binding
- `be3db88f` — WordPress data model / admin UX planning

Commit `49ffdafe` is **non-authority** (accidental foreign commit) — do not rely on it.

---

## 2. Purpose

The prototype will help validate product direction **before** WordPress coding on i-seo.su:

- **Admin UX** — how SEO specialists navigate cycles, checkpoints, and monthly assembly.
- **Report structure** — block hierarchy, field density, weekly vs monthly separation.
- **Client web report presentation** — readability, tone, and block composition for business owners.
- **Implementation handoff** — give Anton and operator a shared visual reference for WP admin and client renderer.

The prototype is a **decision-support artifact**, not a production system or substitute for WordPress source of truth.

---

## 3. Website Factory Boundary

| Layer | Role |
|-------|------|
| **Website Factory** | Methodology + **prototype lane** + future workspace for HTML/static UI demos (gulp starter/build approach when chartered) |
| **WordPress / i-seo.su** | **Production target** — source of truth for reports, admin workspace, approved client web report renderer |
| **n8n** | External helper only — reminders, AI draft assist, delivery hooks; **not** source of truth |
| **MARS (`projects/iseo-report-hub/`)** | Documentation locus — product architecture, charters, reports |

**Website Factory is:**
- Useful for static demos and visual exploration.
- A handoff input for Anton's WordPress implementation.

**Website Factory is NOT:**
- Runtime owner of Report Hub.
- Production engine or deployed Report Hub.
- WordPress implementation owner.
- Automatic factory runtime.

**No demo workspace** is created by this charter alone.

---

## 4. Prototype Goals

1. Make the **monthly reporting workflow visible** end-to-end (dashboard → weekly → monthly → client report → review).
2. **Reduce ambiguity for Anton** — screen inventory, field lists, and navigation patterns before WP build.
3. **Validate weekly/monthly model** — three checkpoints + month close feel operable, not redundant.
4. **Validate client report layout** — executive summary, KPI cards, works, Topvisor card, evidence appendix.
5. **Test information density** — admin may be dense; client report must stay calm and scannable.
6. **Clarify block hierarchy** — required vs optional vs profile-specific blocks in context.
7. **Identify missing fields** before implementation — gaps surfaced in static walkthrough.
8. Give operator a **clickable/static demo** for feedback before MVP implementation charter.

---

## 5. Prototype Non-goals

- No production code on i-seo.su.
- No WordPress plugin or theme module.
- No database or persistent backend.
- No API integrations (Topvisor, Metrika, GSC, etc.).
- No n8n wiring or webhooks.
- No login/security implementation (mock navigation only if needed).
- No real client data, credentials, or secrets.
- No AI integration or autonomous draft publication.
- No claim that prototype output is deployed Report Hub.

---

## 6. Prototype Scope v0.1

### Recommended first prototype screens

| # | Screen | Primary audience |
|---|--------|------------------|
| 1 | **SEO Specialist Dashboard** | Specialist — deadlines, assigned projects, action items |
| 2 | **Project Detail / Reporting Cycle Overview** | Specialist — one project, current month, week status strip |
| 3 | **Weekly Checkpoint Editor** | Specialist — fast weekly fill (weeks 1–3) |
| 4 | **Monthly Report Editor** | Specialist — assemble month-close report |
| 5 | **Client Web Report Page** | Client / operator — approved report presentation |
| 6 | **Review Queue / Reviewer View** | SEO Lead — inbox, approve/revision |

### Optional later screens (post v0.1)

- Work Dictionary manager
- Block Library manager
- Published Reports list
- Settings (profiles, deadlines, publish policy)
- Notification Events log

**Scope discipline:** v0.1 should not expand beyond six core screens unless operator explicitly revises charter.

---

## 7. Data and Content Strategy

**Use fake/demo data only.**

### Suggested demo project (either acceptable)

| Option | Client | Notes |
|--------|--------|-------|
| A | **Demo Industrial Tools** | Primary recommendation in Demo Brief |
| B | Makita Land Demo / Neutral Demo Client | If corpus-aligned naming needed — **mark as demo/sanitized** |

### Demo scenario parameters

| Field | Value |
|-------|-------|
| Project type | e-commerce |
| Period | July 2026 |
| Weekly checkpoints | 3 (Week 1–3) |
| Monthly final | Month Close |
| Topvisor | External link placeholder only |
| Metrics | Manual KPI cards (entered values) |
| Works | Completed work list from dictionary-style labels |
| Evidence | Placeholder URLs only |
| Blockers/risks | Sample narrative |
| Next month plan | Sample forward plan |

**Security:** No real credentials. No sensitive client data. If real-looking names from Storage corpus appear, label explicitly as **demo/sanitized**. Nikita XLSX Лист2 class material remains **excluded**.

---

## 8. Visual Direction

Use **i-SEO-compatible business style**:

- Clean professional B2B admin and client surfaces.
- Clear dashboards with readable tables and cards.
- White/light background; restrained accent color.
- Strong table/card readability in admin.
- **Client-facing report calmer than admin** — less chrome, more narrative flow.
- No flashy SaaS overload or fake AI "wow" effects.

**Do not force final brand decision** in prototype — explore tone; operator approves direction before WP theming.

Corpus-informed blend (from attested planning docs): Denis-style branded clarity for client report; Ilya-style compact metrics + Topvisor link utility — unified block system, not two products.

---

## 9. Prototype Deliverables

For a **future build task** (not this charter):

| Deliverable | Notes |
|-------------|-------|
| Static HTML pages | Six core screens minimum |
| Shared layout/components | Sidebar/topbar, badges, cards, blocks |
| Navigation between screens | Linked demo flow; no backend |
| Responsive behavior | Desktop-first admin; mobile-friendly client report |
| README in workspace | Screen list, demo data summary, build notes |
| Screenshots | Optional **after** build — not required by this charter |
| WordPress runtime | **Explicitly excluded** |

Build may use Website Factory / gulp starter when workspace is chartered — see [I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md](I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md).

---

## 10. Acceptance Criteria

Prototype v0.1 should allow operator to answer:

1. Does the **admin workflow** make sense for a specialist's monthly rhythm?
2. Can SEO fill **weekly checkpoints quickly** without excessive friction?
3. Does the **monthly editor** expose the right blocks for e-commerce profile?
4. Is the **client report readable** for a business owner (not SEO specialist)?
5. Are **too many or too few fields** shown on key screens?
6. What should **Anton implement first** in WordPress MVP?
7. What can be **removed or deferred** from MVP scope?

Prototype passes when operator can make these judgments from static navigation and sample data — not when pixels match final brand.

---

## 11. Risks

| Risk | Mitigation |
|------|------------|
| Over-polishing prototype before process is fixed | Time-box v0.1; focus workflow clarity over visual perfection |
| Confusing static demo with implementation | Label all outputs "prototype"; repeat WP = production in README |
| Too much dashboard noise | Start with six screens; defer dictionary/library managers |
| Too many screens at v0.1 | Strict scope gate; optional screens listed but not built |
| Using real sensitive data | Demo data only; no Storage corpus paste without sanitization |
| Diverging from WordPress constraints | Align fields with [I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-DATA-MODEL-v0.1.md) and [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md) |
| Website Factory scope creep | Prototype lane only; no production deployment claims |

---

## 12. Next Step

**Separate build charter** for Website Factory demo — operator reviews this charter and [I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md](I-SEO-REPORT-HUB-WEBSITE-FACTORY-DEMO-BRIEF-v0.1.md), then authorizes:

1. Workspace creation (candidate path in Demo Brief — **SAFE UNKNOWN** until build charter), **or**
2. Charter revision if screens/scope should change before build.

No workspace creation or HTML build from this document alone.

---

## Document control

- **Upstream:** [I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md](I-SEO-REPORT-HUB-WORDPRESS-PRODUCT-ARCHITECTURE-v0.1.md) §11, [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md) §10, [I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md](I-SEO-REPORT-HUB-IMPLEMENTATION-BRIEF-v0.1.md) §6
- **Does not claim:** any demo, workspace, HTML, or runtime exists
