# I-SEO Report Hub — Summary Assembly Block Text Contract v0.1

**Status:** CHARTER / CONTRACT — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01

Defines **exactly** what apply writes into `report_blocks.body`.  
Preview cards may stay more technical; **applied body must be client-facing**.

---

## 1. Storage format

`report_blocks.body` is **plain text** (MEDIUMTEXT). Preview/PDF render with `nl2br(e($body))` / `ReportPreviewService::safeMultiline`. There is **no** Markdown/HTML renderer.

Therefore apply must write:

- UTF-8 plain text
- intro sentence
- blank line
- lines starting with `- ` for bullets
- `\n` newlines (no HTML tags, no `<ul>`)

Do **not** write raw JSON. Do **not** write source ids. Do **not** write category badges. Do **not** write `internal_note` / `evidence_note`.

Max length: existing `ReportBlockService` body cap **50000**.

---

## 2. Item text source priority

For each included work entry, the bullet text is:

1. `client_summary` if non-empty after trim  
2. else `title` + truncated `description` (max **280**, ellipsis) if description non-empty  
3. else `title` only  

If the resulting line does not already end with `.` `!` or `?`, append `.`

Never use catalogue slugs, user emails, or entry ids in the body.

Do **not** add extra marketing verbs if `client_summary` already is a complete client sentence (fixture examples already are).

---

## 3. `work_completed`

**Intro (locked):**

```
В течение месяца выполнены основные SEO-работы:
```

Then a blank line, then one bullet per included entry, in work-entry list order (`sort_order ASC`, `id ASC`).

**No category group headings** in the applied body.

**Example (fixture-shaped):**

```
В течение месяца выполнены основные SEO-работы:

- Выполнен технический мониторинг сайта.
- Проверена индексация ключевых страниц.
- Актуализирована семантика по приоритетным группам.
- Подготовлены рекомендации по коммерческим факторам.
```

Empty list: **do not write** this block even if selected (see Apply Scope). Preview empty copy stays preview-only.

---

## 4. `next_month_plan`

**Intro (locked):**

```
В следующем периоде запланированы работы:
```

Then bullets from included plan entries, same order rules, no category headings.

**Example (fixture-shaped):**

```
В следующем периоде запланированы работы:

- Запланирована доработка мета-тегов.
- Запланирована подготовка новых текстов.
```

Use live `client_summary` / fallback; do not rewrite “Запланирована…” into a different verb unless the source text itself differs.

Empty list: **do not write**.

---

## 5. `risks_and_blockers`

**Intro when there is at least one included risk/blocker:**

```
На текущий момент требуют внимания:
```

Then bullets, same order rules, no category headings.

**Example (fixture-shaped):**

```
На текущий момент требуют внимания:

- Требуется согласование приоритетных страниц.
```

### Empty state (locked)

If the block is **selected** and the generated list is empty, write **exactly**:

```
Существенных рисков и блокеров на текущий момент не зафиксировано.
```

No intro line in that empty state. No dash.

If the block is **not** selected, write nothing (leave current body).

Rationale: `risks_and_blockers` is optional for finalize; an explicit apply of an empty risk draft is a valid client statement. Auto-writing empty completed/plan sections is not — those would destroy useful manual text for no content.

---

## 6. Forbidden in body

| Forbidden | Why |
|-----------|-----|
| Work entry ids | Internal |
| `block_key` / status / visibility enums | Internal |
| Category names / badges | Technical grouping |
| `internal_note` / `evidence_note` | Internal |
| Preview `<details>` source dump | Debug |
| KPI / traffic / ranking claims | No metrics model |
| Concatenation into `executive_summary` | Manual-only |

---

## 7. `summary` field

Implementation 01: **do not change** `summary`.

If current summary is non-empty, apply UX must say that «Кратко» will stay as-is. Operator uses block editor to fix a stale teaser.

---

## 8. Preview vs apply text

| Surface | Format |
|---------|--------|
| Preview cards | May group by category; may show source `<details>` (future: hide in normal mode) |
| Applied `body` | Intro + flat bullets only |

Apply payload is built from the same classified items as preview, then **formatted** by this contract. Do not persist the HTML of the preview page.

---

## 9. SAFE UNKNOWN

- Whether operators will later want category subheadings in client body (rejected for Implementation 01).  
- Whether empty completed/plan should ever write a neutral “no work” sentence (rejected for Implementation 01).
