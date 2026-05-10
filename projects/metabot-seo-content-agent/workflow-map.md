# Workflow map — MetaBOT SEO Content Agent

**Status:** documentation — communication paths described at **workflow** level. **Optional** sanitized n8n JSON may appear under [`exports/`](exports/) (legacy snapshot); it **does not** replace live graphs in n8n.

**Главный архитектурный обзор runtime:** [mega-map.md](mega-map.md) (SEO Content Agent v13 как **multi-workflow production runtime**, не «просто бот»).

---

## Workflow set

| Workflow | Role |
|----------|------|
| **Intake** | Entry from Telegram (and possibly other triggers **SAFE UNKNOWN**); validation, normalization, handoff to processing. |
| **Worker** | Main content pipeline: chunking, generation, locks, QA/factcheck triggers, Sheets updates — **v13 stable**. |
| **Admin** | **Ops layer:** locks, health, recovery, **`/stop-all-flow`**; admin-only маршруты — частичное пересечение с Worker без live graph (**SAFE UNKNOWN** детали узлов). |
| **File Export** (future) | Export artifacts to files or external storage — **not** evidenced as implemented in this repository. |

**Canonical workflows (current product line, documentation-level):** **Intake**, **Worker**, **Admin**, and **File Export** (future). Operational detail and graph truth remain in **n8n** — see [integration-boundary.md](integration-boundary.md).

**Sanitized exports in this repository:** a **legacy** single-workflow-style sanitized JSON may exist under [`exports/`](exports/) (e.g. `workflow-sanitized-legacy.json`) for reference; it **does not** replace the three-layer Intake / Worker / Admin model described above. **Raw** workflow dumps (if any) stay **local** and **gitignored** under `projects/metabot-seo-content-agent/raw/`.

**Legacy / bridge artifacts:** early spec and single-tool bridge material may remain under [`../seo-content-agent/`](../seo-content-agent/) **pending migration**; **do not** extend that folder as the canonical doc set — see [README.md](README.md) §Canonical project folder.

---

## Communication paths (logical)

```
Telegram user
    │
    ▼
┌─────────────┐
│   Intake    │  ← commands, payloads, metadata (user_id, username, …)
└──────┬──────┘
       │  SAFE UNKNOWN: internal call pattern (sub-workflow, queue, HTTP)
       ▼
┌─────────────┐
│   Worker    │  ← OpenRouter, chunking, locks, seo_active_jobs, memory
└──────┬──────┘
       │
       ├──────────► Google Sheets (memory, seo_active_jobs, …)
       └──────────► OpenRouter (generation, QA, cleanup rewrite, …)

┌─────────────┐
│    Admin     │  ← may read Sheets, Telegram admin routes
└─────────────┘
       ▲
       │  SAFE UNKNOWN: whether Admin is always invoked via Intake or separate trigger
```

---

## External systems

| System | Direction | Notes |
|--------|-----------|--------|
| **Telegram** | Inbound commands / outbound replies | Bot API — credentials in n8n. |
| **OpenRouter** | Outbound API | Model calls from Worker (**SAFE UNKNOWN**: which nodes). |
| **Google Sheets** | Read/write | **Главный bottleneck** (квоты, задержки, неатомарность); см. [mega-map.md](mega-map.md) §8, [known-issues.md](known-issues.md). |

---

## Route types (Intake → Worker)

Реальные типы маршрутизации v13 (логические; реализация в n8n):

| Route type | Назначение |
|------------|------------|
| **local** | Облегчённая/локальная ветка без полного длинного пайплайна. |
| **single** | Один целевой шаг или короткая цепочка: outline, text, seoqa, factcheck. |
| **run** | Полный production pipeline (outline → … → final format) — см. ниже. |
| **get** | Выдача по `task_id` (`/get`); известны тихие сбои — [known-issues.md](known-issues.md). |
| **reuse** | Повторное использование артефакта/контекста (`from:task_id`, ветки QA и др.) — [memory-and-task-reuse.md](memory-and-task-reuse.md). |

---

## Single vs run

- **Single** — узкие ветки: **outline**, **text**, **seoqa**, **factcheck** (каждая со своим набором слоёв качества по конфигурации).
- **Run** — полный проход: **outline → strategy → text → cleanup → repair → score → seoqa → factcheck → final format**.

Strict QA не «наследуется» автоматически на все пути; канон — явные команды — [seoqa-and-factcheck.md](seoqa-and-factcheck.md). Подробнее: [mega-map.md](mega-map.md) §4.

---

## Reuse branch

- Синтаксис **`from:task_id`** (и варианты `--from` в парсере) связывает команду с prior task.
- Канонический strict: `/seoqa --strict from:task_id`, `/factcheck --strict from:task_id`.
- Потоки **memory append** и чтения для reuse — [memory-and-task-reuse.md](memory-and-task-reuse.md), [storage-layer.md](storage-layer.md).

---

## Admin ops layer

- **Locks:** пользовательский `/locks` + админские действия (**SAFE UNKNOWN** ACL).
- **Health:** пробы, часто бьют по Sheets — риск rate limit.
- **Recovery:** ручное снятие залипших lock, разбор **pending** в `seo_active_jobs`.
- **`/stop-all-flow`:** логическая остановка сценария; **нет physical cancellation** — [mega-map.md](mega-map.md) §5, [known-issues.md](known-issues.md).

---

## Lock lifecycle (сводка)

- Таблица **`seo_active_jobs`**: жизненный цикл задачи; поле **`pending`** может рассинхронизироваться с **active lock**.
- **Active lock**, **`expires_at`** (семантика TTL — **SAFE UNKNOWN** в схеме репозитория), **Finish Lock**, политика **Close Single Lock Before Sending**.
- **Текущие ограничения:** нет надёжной physical cancellation, нет единого running status, нет задокументированного в репозитории **expired cleanup** — детали [mega-map.md](mega-map.md) §5, [lock-system.md](lock-system.md).

---

## Memory flows

- **Memory table** (Sheets): append после значимых шагов в ветках **local / single / run**.
- **`/get`:** выдача сохранённого состояния/артефакта; возможны **silent failures**.
- **reuse / `from:`:** чтение stored input/output и согласование с задачей.
- См. [memory-and-task-reuse.md](memory-and-task-reuse.md), [mega-map.md](mega-map.md) §6.

---

## SAFE UNKNOWN

- **Exact** handoff mechanism between Intake and Worker (named queue vs synchronous execute vs shared sheet row polling).
- Whether **Admin** is a separate Telegram bot, same bot with role check, or separate webhook — **not** documented in-repo.
- **Retry** and **dead-letter** behavior per workflow.
- **Future File Export Workflow** attachment point (post-Worker vs parallel).

---

*Related: [intake-workflow.md](intake-workflow.md), [worker-workflow.md](worker-workflow.md), [admin-workflow.md](admin-workflow.md), [integration-boundary.md](integration-boundary.md).*
