# Roadmap — MetaBOT SEO Content Agent

Documentation-only planning buckets. **No** implementation commitment in MARS repo.

**Runtime architecture (v13):** [mega-map.md](mega-map.md).

---

## Runtime stability

- **Robust `/get`** — устранение или диагностика **silent failures**, таймауты, явные ошибки пользователю.
- **Robust reuse** — предсказуемое поведение `from:` / `--from` и согласованность с memory.
- **Stale lock cleanup** — автоматическая или полуавтоматическая уборка просроченных lock и «мёртвых» pending (**сейчас не задокументировано** как надёжный механизм в репозитории).
- **Update lock with real `task_id`** — связка lock ↔ реальный идентификатор задачи в Sheets для снижения рассинхрона с `seo_active_jobs`.

---

## Quality

- **Centralized forbidden patterns** — единый каталог запрещённых формулировок для промптов и пост-проверок.
- **Final enforcement after Text Repair** — жёсткая проверка после repair, чтобы не реинтродукция запрета.
- **Synchronized single/run strict behavior** — одинаковая семантика strict между **single** и **run** ветками.

---

## Storage

- **Future storage adapter abstraction** — слой абстракции над Sheets для смены бэкенда без переписывания всех workflow-контрактов.
- **Possible PostgreSQL migration later** — потенциальный перенос операционного state/memory/jobs в Postgres (**план**, не обязательство).

---

## Near-term stabilization

- Fix or mitigate **`/get`** non-responses (timeouts, error visibility).
- Align **`seo_active_jobs`** terminal state with **lock** lifecycle after `/run`.
- Reduce **`/health`** Sheets chatter or add backoff / caching to avoid quota errors.

---

## Production hardening

- Stronger **strict QA** prompts and checks without adding **niche-only validators**.
- Expand **cleanup rewrite** coverage where it helps universal editorial quality.
- Operational runbooks for **stuck pending** rows and **lock** cleanup — [admin-operations.md](admin-operations.md).

---

## Future multi-workflow orchestration

- Clarify **Intake → Worker → Admin** contracts in **sanitized** maps (still **no** secrets in MARS).
- Optional: formal **event** or **task id** correlation across workflows — **SAFE UNKNOWN** design.

---

## Future file export workflow

- **File Export Workflow** (artifacts to drive, CMS, or handoff packages) — **planned**; not evidenced in-repo.
- Attachment point likely **post-Worker** — [workflow-map.md](workflow-map.md).

---

## Future MARS integration

- If MARS later **orchestrates** or **observes** MetaBOT, respect [integration-boundary.md](integration-boundary.md): credentials in n8n; MARS holds **knowledge** and possibly **sanitized** telemetry contracts only.
- **SAFE UNKNOWN:** webhook shapes, auth, and whether MetaBOT remains primary SoT for task state.

---

*See [known-issues.md](known-issues.md), [lessons-learned.md](lessons-learned.md).*
