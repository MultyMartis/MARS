# I-SEO Report Hub — Work Entry Editor Scope v0.1

**Status:** CHARTER / SCOPE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Work Entry Editor Charter 01  
**Depends on:** Work Entry UI Implementation 01 · Nikita Catalogue Seed and Work Entry Model Implementation 01 · Option B (Catalogue + monthly work entries)

This wave does **not** implement the editor. It freezes MVP product decisions for Implementation 01.

---

## 1. Goal

Give an internal specialist a **safe MVP editor** for `monthly_report_work_entries` on an existing monthly report, using the already-seeded Nikita catalogue as a picker and allowing a manual custom entry when no catalogue item fits.

The editor is the specialist workspace. It must **not** assemble the 6 client shells, regenerate PDF, or mutate shares/exports.

---

## 2. Decisions (MVP)

| # | Question | Decision |
|---|----------|----------|
| 1 | Where does the editor live? | **Embedded controls** on `/monthly-reports/{id}` section «Работы за месяц»; **separate create/edit form pages** for writes |
| 2 | Inline quick actions vs full form? | **Full form** for create and edit. **No** inline POST status buttons in Implementation 01 |
| 3 | Create / edit / delete? | **Create + edit only.** Physical **delete is forbidden** in the first editor |
| 4 | How to remove from active work? | Set `status` = `cancelled` or `deferred`, and/or `client_visibility` = `internal` |
| 5 | Are seeded fixture entries editable? | **Yes.** They are local fixture rows, not production client data. UI must still show catalogue origin when `work_item_id` is set |
| 6 | Catalogue-linked title? | **Editable override.** If title is empty on save and a work item is selected, default title from `seo_work_items.name` |
| 7 | Manual custom entry without catalogue? | **Yes.** `work_item_id` may be NULL. Title required |
| 8 | Internal-only entries? | **Yes.** `client_visibility` = `internal` is a first-class choice |
| 9 | Client-facing entries? | **Yes, explicit.** `client_facing` is a distinct value; do not infer it from status |
| 10 | Two add buttons? | **No.** One CTA «Добавить работу». The create form covers catalogue pick **and** manual entry |
| 11 | Edit catalogue / items? | **No.** Categories and work items are read-only selectors |
| 12 | Finalized monthly report lock? | **Do not inherit the 6-block lock.** Work entries remain editable on a finalized report in this MVP, with a visible warning that client PDF/snapshot does **not** update automatically. Do **not** reopen report 1 for editor smoke |
| 13 | Duplicate catalogue item on one report? | **Allowed.** Same item may appear as done this month and planned next |
| 14 | Dedicated show page? | **No.** List card + edit form is enough |
| 15 | JS category→item filter? | **No JS required.** Group work items in `<optgroup>` by category; optional GET `?category_id=` filter is allowed |

---

## 3. In scope (Implementation 01)

- Add / edit monthly work entries for an existing monthly report.
- Pick an active catalogue category and/or work item.
- Create a manual entry with title (and optional category).
- Edit: title, description, status, period_role, client_visibility, client_summary, internal_note, evidence_note, sort_order, category_id, work_item_id.
- Preserve `monthly_report_id` and `created_by_user_id` on update; set `updated_by_user_id` from the current user when available.
- Russian labels already present in `UiLabels` (status / period_role / visibility).
- CSRF + internal auth.
- List on `/monthly-reports/{id}` gains «Добавить работу» and per-card «Изменить».
- Show cancelled/deferred entries in the list (dimmed), so they can be revived via edit.

---

## 4. Out of scope

- Physical DELETE route or UI.
- Summary assembly into `work_completed` / `next_month_plan` / risks.
- Client report / PDF template alignment.
- Export, share, snapshot, finalize, reopen mutations.
- Catalogue CRUD (create/edit categories or items).
- Weekly checkpoint structured work entries.
- Screenshot QA / operator visual redesign.
- Production.
- Reopening finalized report 1.

---

## 5. Seeded entries policy

Local report id **1** currently has **7** fixture entries from `nikita_catalogue_v1`.

| Rule | Detail |
|------|--------|
| Editable | Yes — fixture, not a production freeze |
| Origin visible | If `work_item_id` is set, show catalogue name/slug in card details and as read-only hint on the edit form |
| Relink | Allowed: change or clear `work_item_id` |
| Do not “protect” seed rows | No special DB flag in this MVP. Safety is backup + no DELETE route |
| Do not mass-edit seeds in smoke | Implementation smoke must use a **new test entry**, not rewrite the 7 fixtures |

---

## 6. Add-from-catalogue vs manual

### Catalogue-linked

1. User selects category (optional filter) then work item.  
2. On save, `work_item_id` is set; `category_id` is **derived from the work item** (posted category is ignored if it disagrees).  
3. Empty title → copy `seo_work_items.name` (truncate to 240).  
4. Default `client_visibility` may copy the item’s `visibility` on **create** only; user can override.

### Manual custom

1. User leaves work item empty.  
2. Category optional.  
3. Title **required**.  
4. `work_item_id` stays NULL.

One create form, one POST. No second route for “from catalogue”.

---

## 7. Status / role / visibility

These three fields are independent required enums (DB-11 CHECKs). The editor must not auto-rewrite one from another.

**Hide from future client assembly (later wave)** by:

- `status` ∈ {`cancelled`, `deferred`}, **or**
- `client_visibility` = `internal`

MVP does not hide cancelled rows from the specialist list.

---

## 8. Lock / authorization

| Actor | MVP |
|-------|-----|
| Unauthenticated / no internal role | Redirect login / deny |
| Internal role (`seo_specialist`, `seo_lead_reviewer`, `admin_owner`, and other internal roles already used by monthly CRUD) | Create + edit |
| Client / public / share token | **No** editor routes; **no** token links on these pages |
| Finalized monthly report | Editor **allowed** with warning |
| Parent period archived | Follow existing monthly CRUD `canMutateAgainstParent` if the same helper is reused; do not invent a new lock matrix in this wave |

Rationale for ignoring the block lock: Option B treats work entries as specialist SoT and the 6 shells as a later assembly. Blocking the only fixture report (id 1, **finalized**) would force a `reopen` mutation of `monthly_report_contents`, which this editor wave must not do.

A later assembly/finalize charter may lock entries after finalize.

---

## 9. Success criteria for the next implementation wave

1. Specialist can add a catalogue-linked entry and a manual entry.  
2. Specialist can edit fields including status / period_role / visibility.  
3. No DELETE control or route exists.  
4. Seeded 7 entries remain unless the operator explicitly keeps a test row (see Safety Policy).  
5. Six client blocks, exports, shares, and PDF checksums unchanged.  
6. Russian UI; CSRF; auth.

---

## 10. SAFE UNKNOWN

- Whether operators will later want a default list filter that hides `cancelled`.  
- Whether post-assembly waves should lock entries when the monthly report is finalized.  
- Exact internal-role matrix beyond “same as other internal monthly CRUD” if a dedicated permission table is added later.
