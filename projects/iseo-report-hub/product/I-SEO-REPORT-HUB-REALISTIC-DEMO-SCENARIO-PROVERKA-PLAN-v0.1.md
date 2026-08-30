# I-SEO Report Hub — Realistic Demo Scenario «ПРОВЕРКА.рa» Plan v0.1

**Status:** planning only — **no client/project/report creation in this wave**  
**Date:** 2026-08-21  
**Operator “today”:** `2026-08-21`  
**Wave:** Pre-hosting Demo Scenario and Field Help Charter 01

---

## Project name — literal + mixed-script warning

| Item | Value |
|------|-------|
| **Operator literal (display)** | `ПРОВЕРКА.рa` |
| **Preserve** | Exact operator spelling for human-facing labels |

### Unicode check (charter preflight)

String inspected as operator-provided `ПРОВЕРКА.рa`:

| Position | Char | Code point | Script |
|----------|------|------------|--------|
| `ПРОВЕРКА` | Cyrillic capitals | U+041F…U+0410 | Cyrillic |
| `.` | `.` | U+002E | punctuation |
| `р` | Cyrillic small er | **U+0440** | **Cyrillic** |
| `a` | Latin small a | **U+0061** | **Latin** |

**Finding:** mixed-script suffix `р` + `a` (Cyrillic + Latin).  
**Product rule:** keep the literal for demo authenticity; document the mix so team/hosting do not “normalize” silently; slug generation must use a **safe ASCII slug** (see below), not the mixed-script string as unique key.

Recommended slug (implementation): `proverka-ra-demo` (or similar ASCII), unique under new client.

---

## Narrative (team demo story)

SEO specialist **Тест Проверочнов** ведёт проект **второй месяц**.

- Работы стартуют **с 1-го числа** каждого месяца.
- **Месяц 1 (июль 2026):** полный цикл закрыт — отчёт заполнен, статусно «готово / финализирован» (или максимально близко к show-ready finalized без PDF/share).
- **Месяц 2 (август 2026):** текущий незавершённый месяц — сегодня **21.08.2026**; часть работ done / in progress / planned; отчёт **не** final.

Цель демки: команда видит, **как** SEO заполняет работы, блоки, тексты отчёта и что получается в client preview.

---

## Distinguish from existing local Demo Client path

Current local fixture (read-only probe):

| Entity | Existing |
|--------|----------|
| Client | `Demo Client` (`demo-client`) |
| Project | `Demo SEO Project` |
| Periods | `2026-07` (draft period) + `2026-08` (archived) |
| Monthly | Report **1** finalized (July show-ready preview path); Report **5** empty draft August |

**New demo must be a separate client + project**, not overwrite report 1 / report 5.

Suggested names:

| Entity | Proposed |
|--------|----------|
| Client name | `ПРОВЕРКА.рa` (same literal) |
| Client slug | `proverka-ra-demo` |
| Project name | `ПРОВЕРКА.рa` |
| Project slug | `proverka-ra-demo` |
| Project type | `service_corporate` (neutral B2B service) |
| Site URL | `https://proverka.example` |
| Site label | `ПРОВЕРКА.рa` (primary) |

Marker in titles/notes: `TEAM_DEMO_PROVERKA_2026_08` so it is greppable and safe to exclude from host upload if needed.

---

## Periods and monthly reports

| Month | `period_key` | Dates | Period status (target) | Monthly status (target) | Story |
|-------|--------------|-------|------------------------|-------------------------|-------|
| Month 1 | `2026-07` | 2026-07-01 … 2026-07-31 | `closed` or product-consistent closed/active-complete | `finalized` (or `reviewed` if finalize blocked for demo safety) | Full report |
| Month 2 | `2026-08` | 2026-08-01 … 2026-08-31 | `active` / in progress | `in_progress` (not finalized) | Partial through day 21 |

Owner: user `Тест Проверочнов` (`seo_specialist`).  
Reviewer: optional Local Admin or leave empty for specialist-led demo.

**Note:** existing Demo Client already uses `2026-07` / `2026-08` period keys on **project_id=1**. New periods are per-project — keys can repeat across projects. Implementation must create periods under the **new** project id.

---

## Content direction — Month 1 (July, complete)

Human Russian copy; fictional but realistic SEO metrics **as narrative numbers inside text/blocks**, not fake live Topvisor claims.

Themes to cover:

1. Technical audit (crawl, status codes, basic CWV notes)
2. Indexation (coverage, exclusions, sitemap)
3. Semantic grouping / clustering
4. Meta tags (title/description gaps)
5. Commercial factors (contacts, trust, conversion pages)
6. Content plan
7. Risks / blockers
8. Next month plan (feeds August)

Suggested monthly text fields (schema keys):

| Key | RU label | Direction |
|-----|----------|-----------|
| `executive_summary` | Краткое резюме | 4–6 sentences for client |
| `work_completed` | Что сделали | Bullet-style paragraphs of completed work |
| `results_summary` | Результаты | Indexation/meta progress with invented but calm numbers |
| `key_findings` | Ключевые выводы | 3–5 findings |
| `risks_and_blockers` | Риски и блокеры | 1–2 calm blockers needing client input |
| `next_month_plan` | План на следующий месяц | August priorities |
| `client_notes` | Заметки для клиента | Soft coordination notes |
| `internal_notes` | Внутренние заметки | Team-only technical breadcrumbs |

Work entries (illustrative count): **8–12** with mix of catalogue + manual; mostly `period_role=done`, `status=done`, `client_visibility=client`.

Report blocks: mirror key themes (`block_key` snake_case); fill `title` / `summary` / `body`. Optional `source_metric_refs` with **clearly fictional** refs labeled as demo.

Weekly checkpoints W1–W4: optional but desirable for realism; can be seeded lightly then referenced.

---

## Content direction — Month 2 (August, incomplete through 2026-08-21)

| Work state | Approx share | Examples |
|------------|--------------|----------|
| Done | ~40% | Meta fixes on priority URLs; sitemap resubmit; 2 content briefs published |
| In progress | ~35% | Commercial factor checklist; cluster expansion for service pages |
| Planned | ~25% | Link/internal cross-links pass; August closing report assembly |

Monthly status: `in_progress`.  
Do **not** finalize.  
Preview should look like a living draft (honest incomplete sections OK).

Work entries: **6–10**; roles include `done`, `planned_next`, `risk`, `note`.

---

## Pseudo-metrics policy

- Prefer numbers **inside prose** (“проиндексировано 142 из 160 приоритетных URL”) rather than claiming live API integration.
- If using `source_metric_refs` / `data_json`, mark `"demo": true` and invented sources.
- Do **not** invent Topvisor account IDs or real client credentials.
- Do **not** present fictional KPIs as production analytics.

---

## Hybrid seed vs browser fill

| Layer | Method |
|-------|--------|
| User `seo_specialist` | Controlled seed (CLI) after backup |
| Client / project / site | Controlled seed — **no UI CRUD routes** for clients/projects today |
| Periods + empty monthly shells | Seed **or** UI period/monthly create if project selectable — verify in seed charter; if period UI requires existing project FK, seed project first |
| Weekly checkpoints | Prefer UI or light seed |
| Work entries, block bodies, monthly text | **Prefer browser fill** as `test` user |
| Finalization month 1 | UI only if demo needs finalized; otherwise `reviewed` / full content without PDF |
| PDF / export / share | **Frozen** unless explicitly approved later |

---

## Host upload safety for this demo

- Demo password `test` must **not** ship to production as-is
- Mixed-script name is fine in UTF-8 MySQL if charset is utf8mb4
- Tag demo rows for optional exclusion from first host dump
- Keep Demo Client report 1 path intact for prior show-ready acceptance

---

## Out of scope this charter

No inserts, no UI POSTs, no runtime sync, no PDF/share.
