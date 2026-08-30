# i-SEO Report Hub — Report 5 Target Empty Draft UX v0.1

**Wave:** Report 5 Draft Path Cleanup Charter 01  
**Date:** 2026-08-21  
**Decision:** Option A + light demotion — [I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-DECISION-v0.1.md](I-SEO-REPORT-HUB-REPORT-5-DRAFT-PATH-DECISION-v0.1.md)

---

## Detection (display-only)

Treat a monthly report as **empty draft** for UX when **all** hold:

- status is draft / not finalized  
- report blocks count = **0**  
- work entries count = **0**  

Do **not** invent DB flags. Prefer counts already available to the view/controller.

Also continue using existing `UiTextSanitizer` / `ClientReportDocument` fallbacks for junk/empty section bodies (P0).

---

## `/monthly-reports/5` (and any empty-draft monthly detail)

### Top card (first impression)

Should communicate:

- Heading / badge framing: **`Пустой черновик отчета`** (in addition to status **Черновик**)  
- Period / client / project / site (sanitized labels)  
- Status: **Черновик**  
- Operator message:

> В этом отчете пока нет работ и блоков. Добавьте работы за месяц или создайте блоки отчета.

### Primary actions (GET)

Prefer empty-draft-relevant CTAs near the top:

- **Добавить работу** (or equivalent deep-link into work-entries create / `#work-entries`)  
- **Блоки отчета**  
- **К периоду**  

Assembly / preview may remain available, with expectation note:

> Предпросмотр покажет пустые разделы, пока нет работ и блоков.

### Finalization diagnostics

- Remain **collapsed** (P1 policy stands)  
- Collapsed summary must clearly say:

> Отчет пока не готов к финализации.

- Do **not** make a long red checklist the first impression of an empty draft.

### Content / delivery indicators

- Content filled/empty summary may show all empty — calm, not alarming  
- PDF / active link “not ready” is expected; phrase as readiness, not failure drama  
- No PDF/export/share mutation actions as part of this empty-draft framing

### Must not show as “broken test”

- No raw `LOCAL_FIXTURE_ONLY` / numeric junk in normal-visible UI  
- No implication that the route is half-deleted or invalid  

---

## `/monthly-reports/5/preview`

Should show:

- Client document layout (existing `ClientReportDocument`)  
- Title / period / client / project / site  
- Status badge: **Черновик**  
- Calm empty states for all six report sections (existing section fallbacks OK)  
- Clear note:

> Черновик. Это рабочая версия, ещё не выданный клиенту файл.

- Local demo environment honesty line OK  
- **No** PDF / export / share actions on this surface for the wave  

P0 after-shot already approximates this; implementation should preserve and align wording with manager empty-draft framing.

---

## Reporting periods surfaces

### `/reporting-periods` (period list)

Period `2026-08` stays listed (archived). Do **not** delete or SQL-hide. Optional light copy if period title still reads as placeholder after sanitize — prefer existing sanitizer.

### `/reporting-periods/{id}` monthly report card (primary demotion point)

When linked monthly report is empty draft:

- Show status/label so it is unmistakable: **`Пустой черновик`** or **`Черновик без работ`**  
- Keep Open / Preview GET links  
- Avoid presenting it as the primary “full demo report”

### Primary demo narrative

Operator demo path remains:

1. Period `2026-07` / report **1**  
2. Report 5 only when rehearsing **empty draft**  

---

## Copy constraints

- Russian operator-facing copy  
- No English router/debug lecture text  
- No secrets / share tokens  
- No inventing fake filled metrics  

---

## Non-goals for this target UX

- Seeding content so sections look “full”  
- Hiding report 5 entirely from the app  
- Changing finalization rules in the backend  
- Regenerating PDF/export/share artifacts  
