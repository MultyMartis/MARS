# I-SEO Report Hub — Target Report Information Architecture v0.1

**Status:** CHARTER / TARGET IA — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Nikita Report Template Data Model Charter 01  
**Depends on:** Current Data Model Baseline v0.1 · Nikita Taxonomy v0.1 · Report Content Architecture v0.1 (planning legacy)

---

## 1. Design principle

Separate four layers that the current MVP conflates into free-text:

1. **Work catalogue** — reusable Nikita taxonomy (what *can* be done).  
2. **Weekly checkpoint** — short operational notes for the week.  
3. **Internal SEO workspace** — structured work entries + internal fields for the month.  
4. **Client-facing monthly report** — curated summaries assembled for snapshot/export/share.

Do **not** force Nikita catalogue rows 1:1 onto PDF sections.

---

## 2. Internal SEO workspace

**Users:** `seo_specialist`, `seo_lead_reviewer`, `admin_owner`, optionally `account_client_manager` (read/coord).

| Need | Target object | Notes |
|------|---------------|-------|
| Done work | `monthly_report_work_entries` (planned) | Status done/partial; category from catalogue |
| Planned work | same table + next-period plan entries | Or `next_action` on entry |
| Blockers | entry type/flag or risks section | Client-safe vs internal text |
| Metrics | later `report_metrics` | Day-1 optional; keep external Topvisor links |
| Evidence | later `report_evidence_links` | URL/file ref; visibility flag |
| Comments | `internal_note` on entry + monthly `internal_notes` | Never auto-publish |
| Approval | entry status + existing monthly/block review | Reuse finalization gates |
| AI draft | nullable `ai_draft_*` later | Human accept before client |
| Weekly sources | link entry ↔ weekly checkpoint ids | Soft FK / JSON initially OK |

**Specialist primary UX (target):** pick catalogue item → mark status → write what/result → optional evidence → optional client summary. Macro 6 sections become **review/assembly**, not the only place to type work.

---

## 3. Client-facing monthly report

**Users:** client via share/PDF; managers previewing client mode.

| Section | Source | Must be client-safe |
|---------|--------|---------------------|
| Short summary | `executive_summary` block/column (kept) | Yes |
| What was done | assembled from work entries +/or `work_completed` | Yes |
| Results / metrics | `results_summary` (+ later metrics) | Yes |
| Important changes / findings | `key_findings` (possible rename later) | Yes |
| Issues / risks | `risks_and_blockers` client wording | Yes |
| Next plan | `next_month_plan` from planned entries | Yes |
| Optional appendix | evidence subset marked client-facing | Optional |

**Out of client report:** internal notes, raw access/credentials, unfiltered technical dumps, unapproved AI drafts, reviewer comments.

---

## 4. Weekly checkpoint

Keep existing entity; enrich later without removing free-text MVP fields.

| Capture | Day-1 target | Later |
|---------|--------------|-------|
| Work done | keep `work_done` TEXT | optional weekly work entries |
| Issues | keep `risks` / `findings` | typed blockers |
| Open decisions | in `findings` / `next_steps` | explicit field |
| Metrics changes | free text | metric rows |
| Artifacts | free text links | evidence table |

Weekly remains **internal-first**. Monthly assembly may cite weekly IDs (already supported via JSON refs).

---

## 5. Work catalogue

### 5.1 Catalogue record shape

| Field | Purpose |
|-------|---------|
| category_code / title | Nikita top-level |
| item_code / title | Atomic work |
| site_type_applicability | `service` / `ecommerce` / `both` |
| cadence | one-time / weekly / monthly / recurring / as-needed |
| default_visibility | internal / client-safe / client-facing |
| default_fill_mode | manual / ai_assisted / computed |
| evidence_required | bool |
| active | bool |
| sort_order | display |

### 5.2 Storage decision: **hybrid (recommended)**

| Approach | Pros | Cons |
|----------|------|------|
| Static PHP/JSON config only | Fast, easy review in git | Harder admin edits; no per-tenant overrides |
| DB tables only | Queryable; admin CRUD later | Needs migration + seed discipline |
| **Hybrid** | Seed from Nikita into DB; versioned seed files in git; runtime reads DB | Slightly more moving parts |

**Recommendation:** hybrid — versioned seed SQL/JSON in `app-source` + tables `seo_work_categories` / `seo_work_items`. Config file alone is acceptable only as interim prototype; target is DB-backed catalogue for Option B.

---

## 6. Report types (product)

| Type | Exists today? | Target |
|------|---------------|--------|
| Weekly checkpoint | Yes | Keep; optional work-entry link later |
| Monthly internal workspace | Partial (flat+blocks) | Work entries + summaries |
| Monthly client report | Via snapshot/export/share | Same pipeline; richer assembly input |
| 12-month work plan view | No | Later (catalogue + planned quotas); not day-1 |
| Access/credential handoff | No (correctly) | Stay out of Report Hub content |

---

## 7. Compatibility with current MVP flow

Preserve path:

`period → weekly → monthly → blocks(6) → finalize → snapshot → export → share`

Evolution rule: **additive workspace under monthly**; do not delete required block keys until dual-write/assembly proven. Preview/finalization continue to key off the six (five required + risks optional) shells until a later gated cutover.

---

## 8. SAFE UNKNOWN

- Exact client appendix policy (always / on request).  
- Whether weekly structured entries are needed before first client-template wave.  
- Admin CRUD for catalogue in MVP+ vs seed-only catalogue.
