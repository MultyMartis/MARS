# Known issues — MetaBOT SEO Content Agent

Grouped per user briefing. **Status** reflects operations narrative, not automated tests in this repo.

---

## Runtime issues

| Issue | Notes |
|-------|--------|
| **`/get task_id` sometimes does not respond** | Intermittent; causes **SAFE UNKNOWN** (timeout, Sheets, lock, Telegram API). |
| **`/get` silent failures** | Пользователь не получает ответа; воспринимается как «бот игнорирует» — см. также UX. |
| **`/run` lock vs `seo_active_jobs`** | Lock may **close** while job row stays **pending** — treat tables as potentially **out of sync**. |
| **`task_id` may stay pending** | Строка job может оставаться **pending** после снятия lock или без явного terminal state. |
| **Stale active locks / rows** | **Нет** задокументированного в репозитории надёжного **expired cleanup**; возможны залипшие активные lock и «мёртвые» pending без фоновой уборки. |
| **No physical cancellation** | Длительные LLM/HTTP вызовы нельзя гарантированно оборвать из Telegram; `/stop-all-flow` — логический уровень ops. |
| **Distributed strict-policy enforcement** | Строгие правила и forbidden patterns размазаны по промптам/веткам (**single** vs **run** могут расходиться без централизации). |

---

## Quality issues

| Issue | Notes |
|-------|--------|
| **Strict layer still improving** | Undesired phrases may appear: *order now*, *professional*, *improvement*, *helps*, *affects*, *visibility*. |
| **Cleanup rewrite ≠ full QA** | Editorial pass helps; **canonical strict** remains `/seoqa --strict` / `/factcheck --strict` with `from:task_id`. |
| **Text Repair may reintroduce forbidden wording** | После cleanup/strict слой **Text Repair** может вернуть ранее снятые шаблонные или запрещённые формулировки. |

---

## Infrastructure issues

| Issue | Notes |
|-------|--------|
| **`/health` vs Google Sheets** | May hit rate limits: *“The service is receiving too many requests from you”*. |
| **Google Sheets rate limit (general)** | **Главный bottleneck** системы: любые частые чтения/записи (health, memory, jobs) усугубляют квоты — см. [mega-map.md](mega-map.md) §8. |
| **Sheets as state store** | No transactions; races possible under concurrency — see [storage-layer.md](storage-layer.md). |

---

## UX issues

| Issue | Notes |
|-------|--------|
| **`/get` silence** | User perception: “bot ignored me” — see runtime issues. |
| **Strict inheritance** | Users might assume `/run` implies strict QA — **not** current requirement; document clearly — [seoqa-and-factcheck.md](seoqa-and-factcheck.md). |

---

## SAFE UNKNOWN

- Frequency metrics for each issue.
- Whether fixes are deployed uniformly across Intake/Worker/Admin.

---

*See [roadmap.md](roadmap.md).*
