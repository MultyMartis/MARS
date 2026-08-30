# I-SEO Report Hub — Summary Assembly Apply UX v0.1

**Status:** CHARTER / UX — documentation only  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Summary Assembly Apply Charter 01

Page: existing `GET /monthly-reports/{id}/assembly-preview`.  
Write action: `POST /monthly-reports/{id}/assembly-apply` (not implemented in this wave).

---

## 1. Page choice

**Same preview page** contains apply controls. No separate confirmation route in Implementation 01.

Rationale: operator already compared drafts on this page; a second hop would duplicate the three auto cards. Confirmation is the checkbox + selected keys, not another URL.

---

## 2. Auto-block card (apply-ready)

For each of `work_completed`, `next_month_plan`, `risks_and_blockers`:

1. **Черновик для клиента** — the **apply-formatted** body (intro + bullets), not the technical grouped cards as the primary text. Technical grouping / source ids stay in collapsed `<details>` (operator note: hide source details in normal mode later).
2. **Сейчас в отчете** — current `body` (and `summary` if non-empty). Default **open** when current body is non-empty; otherwise collapsed or “пусто”.
3. Checkbox **Включить в применение** (`block_keys[]`), enabled only if apply is allowed for this report.
4. If current body is non-empty: warning `Текущий текст блока будет перезаписан.`
5. If current body differs from generated apply text: simple **before / after** (two stacked preformatted blocks). Line-level diff is optional later; Implementation 01 does not need a diff library.

Manual-only cards stay as today: no apply checkbox.

«Сейчас в отчете» on auto cards is an **apply-stage** comparison (operator request). Keep it on this page.

---

## 3. Apply panel (footer)

### 3.1 Report not finalized and user may apply

Form `method="post"` `action=".../assembly-apply"`:

- hidden CSRF
- checkboxes from §2
- confirm:

```
Подтверждаю перезапись выбранных блоков черновиком.
```

- submit: **Применить выбранные блоки**
- hint: PDF, снимки и публичные ссылки этим действием **не** обновляются

Submit is **disabled** until:

- at least one auto block is selected, and
- confirm is checked, and
- report is not finalized/archived

Server re-checks all three. HTML `required` on confirm is allowed. Small JS to toggle submit disabled state is allowed if kept scoped to this form; no new framework.

### 3.2 Report finalized (report id 1)

- **No** working POST form (do not emit `action` that can write).
- Disabled checkbox lookalikes **or** no checkboxes.
- Disabled button **Применить выбранные блоки**.
- Visible explanation from Finalized Report Policy:

```
Отчет финализирован. Чтобы применить черновик, сначала нужен отдельный безопасный reopen/update/finalize/export процесс.
```

### 3.3 User cannot apply (specialist / viewer)

Show preview as today. Footer: no POST form; hint that применение доступно руководителю / владельцу.

---

## 4. After successful apply

Redirect: `GET /monthly-reports/{id}`  
Flash success listing updated keys in Russian labels, e.g.:

```
Черновик записан в блоки: Что сделали.
```

If some selected keys were skipped (empty completed/plan, missing row): flash warn with those keys.

Do not redirect to PDF, share, or snapshot pages.

---

## 5. After refused apply

Stay on preview (or redirect back to preview) with flash warn:

| Cause | Copy (RU) |
|-------|-----------|
| Finalized | Same finalized sentence as §3.2 |
| No selection | `Выберите хотя бы один раздел.` |
| Confirm missing | `Подтвердите перезапись выбранных блоков.` |
| CSRF | Existing session/CSRF warn pattern |
| Forbidden key | `Этот раздел нельзя заполнить автосборкой.` |
| Empty completed/plan selected | `Пустой черновик раздела не записан.` |

---

## 6. Overwrite warnings

| Current body | Generated | UI |
|--------------|-----------|-----|
| empty | non-empty | Checkbox; no overwrite banner required (still confirm globally) |
| non-empty | different | Overwrite banner + before/after |
| non-empty | identical | Checkbox; note `Текст совпадает с черновиком — запись будет пропущена.` |
| non-empty summary, any body | — | Note `Краткое описание блока не меняется.` |

---

## 7. Technical source details

Operator accepted preview as “somewhat technical, good enough”, with a future UX improvement: hide source ids in **normal mode**.

Implementation 01 apply UI:

- default: client draft primary; source `<details>` collapsed
- do not put ids in the text that will be written

A dedicated “simple vs technical” toggle is **not** required in Implementation 01.

---

## 8. SAFE UNKNOWN

- Exact CSS for before/after columns vs stacked blocks (stacked is enough).  
- Whether confirm copy uses “Я понимаю…” vs “Подтверждаю…” — both are accepted; pick one string and keep it on the server too.
