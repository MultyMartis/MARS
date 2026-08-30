# I-SEO Report Hub — Summary Assembly Apply Scope v0.1

**Status:** CHARTER / SCOPE — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01  
**Depends on:** Summary Assembly Charter 01; Summary Assembly Preview Implementation 01  
**Mode:** Option B MVP — selected-block apply, no PDF/export/share mutation

This wave does **not** implement apply. No app-source, runtime, DB, share, or PDF mutation.

---

## 1. Product goal

Turn the existing GET preview (`/monthly-reports/{id}/assembly-preview`) into a **safe apply** that can overwrite **selected** client shells in `report_blocks` with **readable client-facing draft text**.

Apply writes polished block prose. It does **not** copy the technical preview cards (source ids, category badges, internal notes, debug grouping).

---

## 2. Writable blocks (Implementation 01)

| `block_key` | RU | Apply? |
|-------------|----|--------|
| `work_completed` | Что сделали | **Yes** — if selected and draft non-empty |
| `next_month_plan` | План на следующий месяц | **Yes** — if selected and draft non-empty |
| `risks_and_blockers` | Риски и блокеры | **Yes** — if selected; empty draft may write the locked empty-state phrase |

Only these three keys may appear as apply checkboxes.

---

## 3. Manual-only blocks (never writable by assembly)

| `block_key` | RU | Apply? |
|-------------|----|--------|
| `executive_summary` | Краткое резюме | **No** |
| `results_summary` | Результаты | **No** |
| `key_findings` | Ключевые выводы | **No** |

If POST includes any of these keys → reject that key (or the whole request). Do not write them.

---

## 4. Selection model

**Per-block checkboxes, not all-or-nothing.**

- Zero selected → POST refused; no writes.
- One, two, or three auto keys may be selected.
- Unselected auto blocks are **untouched**, even if their generated draft differs from current body.
- Global confirm checkbox is **required** in addition to selection:

```
Я понимаю, что выбранные блоки отчета будут перезаписаны черновиком.
```

Equivalent confirm copy for the control label is allowed:

```
Подтверждаю перезапись выбранных блоков черновиком.
```

Both mean the same gate. Implementation 01 should use **one** visible checkbox; server field `confirm_overwrite=1`.

---

## 5. Finalized / archived parent

| Parent status | Apply |
|---------------|--------|
| `finalized` | **Forbidden** |
| `archived` | **Forbidden** |
| `draft` / `in_progress` / `ready_for_review` / `reviewed` | Allowed if other gates pass |

Report id **1** is finalized. Implementation 01 must show a **disabled** apply state there and must **not** reopen it.

Apply does **not** call reopen. Reopen remains the existing `admin_owner` monthly-report action, out of this scope.

---

## 6. `body` vs `summary`

Canonical table: `report_blocks`.

| Column | Implementation 01 |
|--------|-------------------|
| `body` | **Written** with the generated client draft (plain text, bullets) |
| `summary` | **Unchanged** |
| `title` | **Unchanged** |
| `block_key` / `block_type` / `sort_order` | **Unchanged** |
| `source_weekly_checkpoint_ids` | **Unchanged** |
| Flat `monthly_report_contents.*` text columns | **Not written** |

Preview/PDF renderers show `summary` («Кратко») **if non-empty**, then `body`. Stale fixture summary may remain visible above new body. That is an accepted MVP limitation: operator can edit summary in the existing block editor. A later wave may add an optional «обновить краткое описание» checkbox.

Renderer does **not** require `summary`; body-only is valid.

---

## 7. Existing text preservation

Before any UPDATE of a selected row:

1. Capture previous `body` and `summary` (and `status`) into implementation evidence (STORAGE, not git).
2. Capture generated new `body`.
3. Write an `audit_log` event (hashes/lengths + keys; not full client prose if long).

There is **no** schema flag for “manual lock”. Process protection = selection + confirm + finalized lock + backup (implementation wave).

---

## 8. Auth / HTTP

| Rule | Decision |
|------|----------|
| Method | **POST only** |
| Route | `POST /monthly-reports/{id}/assembly-apply` |
| Auth | Internal; apply roles = `admin_owner` and `seo_lead_reviewer` |
| CSRF | Required (`_csrf`) |
| Specialist | Preview yes; apply **no** in Implementation 01 (matches full block-edit privilege, avoids applying over `reviewed` rows the specialist cannot currently edit) |
| GET apply | **No** write; GET on the apply path should 405 |

---

## 9. Preview confirmation screen

**Same page as preview** (`GET .../assembly-preview`). No separate confirmation route in Implementation 01.

- Finalized: controls disabled; explanation shown; **no** working POST form.
- Not finalized: form on the same page with selection, confirm, submit.

---

## 10. Empty drafts

| Block | Selected + empty generated list |
|-------|----------------------------------|
| `work_completed` | **Skip write**; flash that empty draft was not applied |
| `next_month_plan` | **Skip write**; flash that empty draft was not applied |
| `risks_and_blockers` | **Write** locked empty-state phrase if selected (see Block Text Contract) |

Missing `report_blocks` row for a selected key: **skip / refuse that key**; do **not** INSERT a new shell in Implementation 01.

Archived selected block: refuse that key.

---

## 11. What apply is not

- Not PDF regeneration
- Not snapshot create/update
- Not export/share create/revoke
- Not work-entry mutation
- Not finalize/reopen
- Not auto-apply on preview GET
- Not metrics / executive auto-prose

---

## 12. SAFE UNKNOWN

- Whether a later wave should let `seo_specialist` apply to `draft` / `in_progress` blocks only.  
- Whether `summary` should be cleared or rewritten once operators see stale «Кратко» on preview.  
- Live title strings of fixture blocks (English vs RU) — title is out of apply scope.
