# Mega-map — SEO Content Agent v13 (MetaBOT)

**Назначение:** единый **архитектурный runtime-документ** мульти-workflow системы.  
**Уровень детализации:** workflow- и продуктовая семантика v13; **не** замена JSON n8n и **не** схема таблиц Google Sheets (конкретные узлы/колонки — **SAFE UNKNOWN**, если не экспортированы в репозиторий).

**Source of truth для документации и канонических контрактов:** каталог [`projects/metabot-seo-content-agent/`](README.md) (см. README §Canonical project folder).  
**Legacy-пак** (ранний spec / bridge): [`projects/seo-content-agent/`](../seo-content-agent/) — **не удалять** без отдельного решения; **не** добавлять туда новую документацию; расхождения сверять с **живым n8n**. Санитизированные копии и мост — в [`exports/`](exports/), [`integrations/`](integrations/), [`integration-contract-legacy.md`](integration-contract-legacy.md).

---

## 1. System role

**SEO Content Agent v13** — это **multi-workflow AI production runtime** (Intake → Worker → Admin, внешние сервисы), а **не** «просто Telegram-чатбот». Telegram — **шлюз и UX**; исполнение, состояние, качество и блокировки живут в **оркестрации workflow** и **хранилище состояния** (в операциях — преимущественно Google Sheets + n8n).

---

## 2. Workflows (три слоя)

### Intake

- **Telegram gateway** — приём команд и тел сообщений, разбор аргументов (`from:task_id`, `--strict` и т.д.).
- **Lock creation** — инициирование/согласование блокировок там, где продукт требует исключить гонки (см. §5).
- **Routing** — маршрутизация в Worker по **типу маршрута** (`local`, `single`, `run`, `get`, `reuse` — см. §3).
- **Admin routing** — отдельные админ-команды и операции (locks, health, recovery, stop-all-flow) в **ops-слой** (см. Admin).

### Worker

- **Execution runtime** — основной контент-пайплайн v13: генерация, слои качества, запись в Sheets, ответы в Telegram.
- **single / run / get / reuse** — разные **режимы выполнения** одного Worker-контура (см. §3–4).
- **Layered quality pipeline** — Auto Polish, Cleanup, Hard Cleanup, Text Repair, Content Score, SEO QA, Factcheck, Postcheck Strict Claims (см. §7).
- **Memory append** — дозапись в **memory table** после значимых шагов (см. §6).
- **Lock close** — освобождение блокировки по завершении или по политике «закрыть single-lock перед отправкой» (см. §5).

### Admin

- **Ops layer** — операции без основного контент-пайплайна или с ограниченным пересечением с Worker.
- **Locks** — обзор и вмешательство при залипших блокировках (`/locks` у пользователя; расширенные действия — **SAFE UNKNOWN** по точному ACL).
- **Health** — пробы зависимостей (в т.ч. обращения к Sheets); риск **квот** Google.
- **Recovery** — ручное разруливание расхождений lock ↔ `seo_active_jobs`, зависших pending.
- **stop-all-flow** — команда уровня **остановки сценариев** / сброса активности (**нет физической отмены** исполняющихся узлов — см. §5, ограничения).

---

## 3. Route types (реальные типы маршрутизации)

| Route type | Смысл (runtime) |
|------------|------------------|
| **local** | Локальная/облегчённая обработка без полного прохода длинного пайплайна (интерпретация на уровне n8n; детали узлов — **SAFE UNKNOWN**). |
| **single** | Один **целевой** шаг или короткая цепочка: outline, text, seoqa, factcheck — см. §5. |
| **run** | Полный production **run** — см. §5. |
| **get** | Выдача артефакта/состояния по `task_id` (`/get`) — известны **тихие сбои** (см. §10). |
| **reuse** | Повторное использование контекста/артефакта (`from:task_id`, ветки повторного запуска QA и т.д.) — см. §7. |

---

## 4. Single vs Run

### Single

Типичные **single**-ветки (по продуктовой фиксации v13):

- **outline**
- **text**
- **seoqa**
- **factcheck**

Каждая — относительно **узкий** проход: один доминирующий результат (структура, текст, SEO-ревью, фактчек) плюс сопутствующие слои качества **по конфигурации** этой ветки.

### Run

**Run** — **полный пайплайн** (последовательность этапов по v13):

1. outline  
2. strategy  
3. text  
4. cleanup  
5. repair  
6. score  
7. seoqa  
8. factcheck  
9. final format  

**Важно:** strict QA / factcheck «наследуются» не автоматически для всех путей; канонический strict — явные команды с `--strict` и `from:` — [seoqa-and-factcheck.md](seoqa-and-factcheck.md).

---

## 5. Lock system

### Артефакты и поля

- **`seo_active_jobs`** — таблица жизненного цикла задач (pending / processing / completed / failed — концептуально; точные колонки — **SAFE UNKNOWN**).
- **Active lock** — текущая блокировка, мешающая параллельным конфликтующим операциям.
- **Pending `task_id`** — задача может оставаться в **pending** в `seo_active_jobs`, пока lock уже снят или наоборот — **известное рассогласование**.
- **`expires_at`** — логическое поле/семантика истечения блокировки (**SAFE UNKNOWN**: где хранится и обновляется ли автоматически).
- **Finish Lock** — нормальное завершение: снятие блокировки после успешного или контролируемого завершения пайплайна.
- **Close Single Lock Before Sending** — политика: для **single**-маршрутов закрыть lock **до** отправки ответа пользователю, чтобы снизить окно гонок (детали реализации — в n8n).
- **`/stop-all-flow`** — админ/ops остановка сценария на уровне оркестрации; **не** гарантирует мгновенную остановку уже запущенных HTTP/OpenRouter вызовов.

### Текущие ограничения (зафиксировать явно)

| Ограничение | Описание |
|-------------|----------|
| **Нет physical cancellation** | Нет надёжной «убийственной» отмены уже идущего LLM/HTTP запроса из Telegram; возможны только логические отказы и ops-действия. |
| **Нет running status** | Пользователю/оператору не гарантируется явный, консистентный **running**-статус в UX или в Sheets для всех путей. |
| **Нет expired cleanup** | Автоматическая уборка **просроченных** lock / pending строк **не задокументирована** как надёжный механизм в репозитории — возможны «залипшие» состояния без фонового cleaner’а. |

Подробнее о взаимодействии с задачами: [task-lifecycle.md](task-lifecycle.md), [lock-system.md](lock-system.md).

---

## 6. Memory system

- **Memory table** — таблица в Google Sheets для долговременного контекста между задачами ([storage-layer.md](storage-layer.md)).
- **Append по веткам** — после значимых шагов **local / single / run** выполняется **append** в memory (точные триггеры шагов — **SAFE UNKNOWN** на уровне узлов).
- **`/get`** — чтение/выдача по `task_id`; может **молчать** (см. §9).
- **reuse** — повторное использование: `from:task_id`, согласование с memory и артефактами задачи.
- **`--from`** / **`from:`** — синтаксис привязки к prior task (как реализовано парсером Telegram → workflow).
- **Stored input/output** — в memory и/или связанных таблицах могут храниться сырой ввод и ключевые выходы для продолжения сессии (**SAFE UNKNOWN**: полная схема полей).

Дополнительно: [memory-and-task-reuse.md](memory-and-task-reuse.md).

---

## 7. Quality layer

| Слой | Роль |
|------|------|
| **Auto Polish** | Лёгкая пост-обработка / сглаживание стиля до или после основного текста (**SAFE UNKNOWN**: точная позиция в графе). |
| **Cleanup** | Редакторский проход снятия шаблонности и слабой лексики ([cleanup-rewrite-layer.md](cleanup-rewrite-layer.md)). |
| **Hard Cleanup** | Более агрессивная чистка при необходимости (**SAFE UNKNOWN**: критерии включения). |
| **Text Repair** | Починка текста после проверок; **риск реинтродукции** запрещённых формулировок (см. §9). |
| **Content Score** | Оценка качества контента (шкала/модель — **SAFE UNKNOWN**). |
| **SEO QA** | SEO-ревью, отдельно от фактчека ([seoqa-and-factcheck.md](seoqa-and-factcheck.md)). |
| **Factcheck** | Проверка фактов отдельным контуром. |
| **Postcheck Strict Claims** | Дополнительная строгая проверка утверждений после основных слоёв (**SAFE UNKNOWN**: полный список правил в промптах). |

### LLM validation vs JS enforcement

- **LLM validation** — правила, «понимание» и классификация нарушений через модель (промпты, многошаговые вызовы).
- **JS enforcement** — детерминированные проверки в Code-узлах n8n: токены блокировок, идемпотентность записей, простые инварианты маршрутизации, формат полей. Цель — **runtime consistency** без тотальной перестройки графа.

---

## 8. Bottlenecks

**Главный bottleneck:** **Google Sheets** — квоты, задержки чтения/записи, отсутствие транзакций; любые частые пробы (`/health`) и массовые апдейты усугубляют лимиты. См. [known-issues.md](known-issues.md), [storage-layer.md](storage-layer.md).

---

## 9. Known risks (сводка)

См. расширенный список в [known-issues.md](known-issues.md):

- `/get` **иногда молчит** (нет ответа пользователю).
- **`task_id` может оставаться pending** в `seo_active_jobs` при уже снятом lock.
- **Stale active locks** — залипшие активные блокировки без автоматического expired cleanup.
- **Нет physical cancellation** длительных вызовов.
- **Text Repair** может **вернуть** запрещённые формулировки, снятые ранее слоями cleanup/strict.
- **Distributed strict-policy logic** — строгие правила размазаны по промптам/веткам; риск расхождения поведения **single** vs **run** без централизации паттернов.

---

## 10. Source of truth (paths)

| Роль | Path |
|------|------|
| **Canonical project (документация и интеграционные контракты)** | `projects/metabot-seo-content-agent/` |
| **Sanitized workflow exports (репозиторий)** | `projects/metabot-seo-content-agent/exports/` — JSON без секретов; может включать **legacy** снимок (`workflow-sanitized-legacy.json`). |
| **Raw workflow dumps (локально, не коммитить)** | `projects/metabot-seo-content-agent/raw/` — **gitignored**; полные выгрузки из n8n держать только локально или вне репозитория. |
| **Legacy documentation / bridge pack** | `projects/seo-content-agent/` — ранний spec и артефакты моста; **не** считать каноном; миграция в канонический каталог по мере готовности. |

Исполняемая правда графов workflow остаётся в **n8n**; MARS держит **санитизированные** описания — [integration-boundary.md](integration-boundary.md).

---

## 11. Навигация по пакету

- Карта workflow: [workflow-map.md](workflow-map.md)  
- Команды: [telegram-commands.md](telegram-commands.md)  
- Полный run: [full-run-pipeline.md](full-run-pipeline.md)  
- Проблемы и roadmap: [known-issues.md](known-issues.md), [roadmap.md](roadmap.md)

---

*Версия документа: синхронизация с продуктовой фиксацией v13 (документация MARS, май 2026).*
