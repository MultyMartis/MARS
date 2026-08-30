# I-SEO Report Hub — Block / Field Mapping v0.1

**Status:** CHARTER / MAPPING — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Nikita Report Template Data Model Charter 01

---

## 1. Mapping of current 6 MVP blocks

| Current key | Current RU label | Target role | Decision | Nikita source | Client-facing | Internal workspace | AI-assisted | DB impact |
|-------------|------------------|-------------|----------|---------------|---------------|--------------------|-------------|-----------|
| `executive_summary` | Краткое резюме | Client macro summary | **Keep** | Not named in plans; needed for client narrative | Yes | Review/edit | Yes (draft later) | Keep column/block; optional gen from entries |
| `work_completed` | Что сделали | Client rollup of done work | **Keep + split backing** | Strong match to all work categories | Yes | Backed by work entries | Partial (rollup draft) | Keep shell; add entries table |
| `results_summary` | Результаты | Outcomes / metrics narrative | **Keep**; later split positions/traffic/leads | Analytics + monitoring outcomes | Yes | Yes | Yes (from metrics later) | Keep; metrics table later |
| `key_findings` | Ключевые выводы | Changes / insights | **Keep**; optional **rename** UI → «Что изменилось» | Точки роста / competitor insights | Yes | Yes | Yes (draft) | Label-only rename safe; key keep |
| `risks_and_blockers` | Риски и блокеры | Issues (client-safe) | **Keep**; consider add to REQUIRED later | Tech/content/client blockers implied | Yes (safe wording) | Yes (+ internal severity) | Low | Keep; policy decision on required gate |
| `next_month_plan` | План на следующий месяц | Forward plan | **Keep + split backing** | Plan актуализация + month columns | Yes | Backed by planned entries | Partial | Keep shell; planned entries |

**Macro decision:** keep the six keys as **client-facing assembly sections**. Do **not** replace keys in day-1 migration. Specialist primary entry moves to **work entries**; shells become generated and/or manually polished.

---

## 2. Additional sections (not new required keys on day 1)

| Candidate | Role | When |
|-----------|------|------|
| KPI / metric snapshot | Structured results | After metrics table; may use existing `metric_snapshot` block_type |
| Work by category appendix | Client optional detail | After work entries stable |
| Technical SEO detail | Client or internal | Prefer work entries under `tech_monitoring` first |
| Semantics/content detail | Same | Catalogue-backed |
| Links/authority | Optional client | Catalogue-backed |
| Evidence appendix | Client subset | Evidence table later |
| Internal-only notes | Already `internal_notes` | Keep |

---

## 3. Target work-entry field set

| Field | Required day-1? | Notes |
|-------|-----------------|-------|
| work item category | Yes | FK / code from catalogue |
| work item title | Yes | From catalogue or custom override |
| work item status | Yes | planned / in_progress / done / blocked / skipped |
| description | Yes | What was done / planned |
| result_effect | Optional | Outcome |
| evidence_link / file ref | Optional | Day-1 URL text OK |
| metric_reference | Optional | Later |
| client_summary | Optional | Client-safe short text |
| internal_note | Optional | Never auto-client |
| next_action | Optional | Feeds plan |
| owner_user_id | Optional | Default specialist |
| reviewer_user_id | Optional | |
| reporting_period_id / monthly_report_content_id | Yes | Scope |
| weekly_checkpoint_id | Optional | |
| site_type / project_type filter | Via project | Catalogue applicability |
| importance / priority | Optional | |
| visibility | Yes | internal / client-safe / client-facing |
| catalogue_item_id | Yes if from catalogue | Null = custom |
| sort_order | Yes | |

---

## 4. How assembly should work (target)

```
catalogue item → monthly work entry (specialist)
                    ↓
        optional weekly checkpoint link
                    ↓
   generate/edit macro blocks (6 keys)
                    ↓
     existing finalize → snapshot → export → share
```

Rules:

1. Empty catalogue month still allows manual shell editing (MVP compatibility).  
2. Generation is **assistive**, not mandatory overwrite — specialist can edit shells.  
3. Only `visibility=client-facing` (or approved client_summary) enters client assembly by default.  
4. Access/credential catalogue items never assemble.

---

## 5. Weekly field mapping

| Weekly field today | Target |
|--------------------|--------|
| `work_done` | Keep; optionally summarize linked weekly entries |
| `findings` | Keep |
| `next_steps` | Keep |
| `risks` | Keep |
| `summary` | Keep |

No forced rename in day-1.

---

## 6. Rename / split / replace summary

| Action | Items |
|--------|-------|
| Keep keys | All 6 machine keys |
| Rename (UI only) | `key_findings` → «Что изменилось» (candidate) |
| Split (backing data) | `work_completed`, `next_month_plan` (+ later `results_summary`) |
| Replace | **None** on day-1 |
| Add (data) | Catalogue + monthly work entries |
| Add (blocks) | Deferred; use existing optional types first |

---

## 7. DB impact summary

| Change | Impact |
|--------|--------|
| New catalogue + entries tables | Migration required |
| Keep `report_blocks` / monthly columns | No breaking change |
| Expand CHECK `block_type` | Only if new types required — avoid day-1 |
| Finalization REQUIRED keys | Unchanged day-1 |
| Seed Nikita items | New seed/fixture update |
| PDF checksum | Unchanged until content/assembly/export regen |

---

## 8. SAFE UNKNOWN

- Final Russian label for `key_findings` after operator review.  
- Whether `risks_and_blockers` should join REQUIRED_BLOCK_KEYS.  
- Whether custom (non-catalogue) entries need a quota/limit.
