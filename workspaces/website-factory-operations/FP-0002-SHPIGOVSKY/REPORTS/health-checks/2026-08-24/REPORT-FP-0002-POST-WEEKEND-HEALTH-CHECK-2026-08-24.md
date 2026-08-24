# REPORT — FP-0002 Post-Weekend Health Check — 2026-08-24

**Режим:** READ-ONLY health check → bounded production maintenance closeout
**Проект:** FP-0002 / shpigovsky.ru
**Evidence:** `REPORTS/health-checks/2026-08-24/`

## Verdict

**PASS**

Исходная read-only проверка зафиксировала **ATTENTION**: физический `/robots.txt` расходился с каноническим Olya-asset. В отдельной bounded maintenance-волне текущий physical файл сохранён в timestamped rollback backup, затем восстановлен точными байтами из текущего canonical Olya source. Post-apply validation прошла.

**ATTENTION RESOLVED — PHYSICAL ROBOTS RESTORED TO OLYA-APPROVED POLICY**

## Public

| Проверка | Результат |
|----------|-----------|
| Канонический хост | `https://shpigovsky.ru/` |
| HTTP→HTTPS / www→apex | OK, без петель |
| Homepage | HTTP 200, WordPress (не Craftum) |
| TLS | Let's Encrypt, valid до Nov 2026 |
| Ключевые маршруты | Все проверенные — HTTP 200 |
| Staging/legacy leak | Не обнаружено (`beget.tech`, Craftum) |

Проверенные URL: `/`, `/uslugi/`, service detail, `/specyalisty/`, `/specyalisty/kostyuk/`, `/blog/`, `/kontakty/`, legal pages.

## Indexing

**INDEXING OPEN — HUMAN APPROVED**

| Сигнал | Значение |
|--------|----------|
| `blog_public` | `1` |
| Effective state | `OPEN` |
| Human decision | `OPEN` (2026-08-20, admin_ui) |
| P18G guard | ACTIVE (класс `IndexingControl` на проде) |
| Watchdog | `fp02_indexing_watchdog_check` — **hourly** |
| Homepage meta robots | `max-image-preview:large` |
| X-Robots-Tag | не установлен |
| Инциденты с 2026-08-21 | **0** в Activity Log |

Synthetic close / QA job не обнаружен.

## Robots

**OLYA-APPROVED ROBOTS POLICY — RESTORED / VERIFIED**

| Поверхность | SHA256 | vs canonical |
|-------------|--------|--------------|
| Канонический asset `robots-seo-policy.txt` | `2594093919…` | MATCH |
| `IndexingControl::robots_body(true)` | `2594093919…` | MATCH |
| Live HTTP + physical `/robots.txt` — detected | `49e52465c97f…` | **DRIFT** |
| Live HTTP + physical `/robots.txt` — corrected | `2594093919d…` | **MATCH** |

- Detection: live/physical содержал четыре неканонических `Disallow: /wp-json/` и отличия только в пустых разделителях групп; глобального `Disallow: /` не было.
- Backup: `/home/s/shpigovsky/shpigovsky.ru/public_html/robots.txt.fp0002-pre-restore-20260824T071539Z.bak`.
- Restore: physical `/robots.txt` записан exact canonical bytes (LF, no BOM, 2826 bytes).
- Verification: HTTP 200 `text/plain`; live = physical = canonical SHA `2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e`.
- Sitemap production-only; Yandex / GoogleBot / Bingbot / `*` / Googlebot-Image groups intact; global closure absent.
- Evidence: `robots-closeout/`.

## Sitemap

- `https://shpigovsky.ru/wp-sitemap.xml` — HTTP 200, валидный index
- Только production host, staging URL не найдены
- robots.txt ссылается на корректный sitemap

## WordPress

| Параметр | Значение |
|----------|----------|
| WP | 7.1 |
| PHP | 8.3.20 |
| Theme | Shpigovsky `0.3.0-d7a-shell` |
| shpigovsky-core | **0.3.25-olya-robots** (active) |
| WPilot | 0.3.2, `write_enabled=false` |
| Maintenance mode | нет |

## Server / PHP Errors

**SAFE UNKNOWN** — доступные пути error log на Beget через SSH не найдены (Aug 21–24). CRITICAL count: не определён.

## Cron

- `fp02_indexing_watchdog_check` — hourly ✓
- Obsolete P18G QA job — не обнаружен
- Подозрительных задач, мутирующих indexing/robots — не обнаружено

## Forms / SMTP

**FORM / SMTP PIPELINE STRUCTURALLY HEALTHY** — без реальной отправки

| Проверка | Результат |
|----------|-----------|
| ConsultationHandler | loaded |
| AntiSpam v1 | loaded (`company_url` honeypot, `fp02_fs` timing) |
| AJAX action | `fp02_lead_submit` |
| SMTP | **VERIFIED / ACTIVE** (`verified=1`, `delivery_active=1`) |
| Transport | `smtp.beget.com:465` ssl |
| Sender | `noreply@shpigovsky.ru` |
| Recipients | **3** configured |
| Lead table `fp02_form_leads` | accessible, total **4**, recent 7d **4**, errorish **0** |

## Privacy / Metrika

- Cookie consent UI — present (browser smoke)
- Metrika **не** загружается до consent (undecided state)
- Unconditional legacy Metrika — не обнаружено

## Frontend

| Viewport | Home / Service | JS errors | Asset failures | Overflow |
|----------|----------------|-----------|----------------|----------|
| Desktop 1440 | 200 | 0 | 0 | нет |
| Mobile 390 | 200 | 0 | 0 | нет |

Screenshots: `screenshots/desktop-home.png`, `desktop-service.png`, `mobile-home.png`, `mobile-service.png`

## Staging / Legacy

Публичный HTML sampled — **NO ACTIVE PUBLIC STAGING/LEGACY HOST LEAK**

## Dashboard

Client-facing widget truthful:
- «Индексация сайта: открыта» — ✓
- «Разработка: Overseo» — ✓
- Stale launch warnings (NS/Craftum) — отсутствуют
- Статус проекта «поддержка / сопровождение» — штатная формулировка виджета

## Drift

| Область | Классификация |
|---------|---------------|
| Critical owner files (6) | **MATCH** |
| shpigovsky-core version | **MATCH** (`0.3.25-olya-robots`) |
| Physical `robots.txt` | **UNEXPECTED DRIFT** |

## Findings

1. **RESOLVED — robots physical drift:** detected live `/robots.txt` ≠ canonical Olya asset; restored exact current canonical policy and verified SHA parity.
2. **SAFE UNKNOWN — server logs:** error logs недоступны для review Aug 21–24.

## Maintenance Closeout

- Current Olya-approved canonical source: `WORDPRESS/plugins/shpigovsky-core/assets/robots-seo-policy.txt`.
- Canonical/review SHA: `2594093919d01f067bcd3776d50d973cfa20a1faf4a6d63fc23f21367d08529e`.
- `IndexingControl::robots_body(true)` equals canonical Olya policy.
- Watchdog remains observation/alert only; no robots rewrite path exists in `IndexingWatchdog`.
- No generic OPEN template owner found in the active owner path.

**OPEN-STATE ROBOTS OWNER PRESERVES OLYA POLICY**

Post-write indexability remained:
- `blog_public=1`;
- effective `OPEN`;
- human decision `OPEN`;
- P18G guard ACTIVE;
- watchdog ACTIVE / hourly;
- homepage and representative service have no `noindex`;
- no global `X-Robots-Tag`.

**INDEXING OPEN — HUMAN APPROVED**

Bounded public regression: homepage, representative service and contacts all HTTP 200. No form/SMTP submission. No synthetic close. Editorial DB untouched.

## Final State

**PRODUCTION / MAINTENANCE — STABLE**

---
*History preserved: detected → corrected → verified. Original broad health check was read-only; bounded follow-up mutated only the physical robots file and its timestamped rollback backup.*
