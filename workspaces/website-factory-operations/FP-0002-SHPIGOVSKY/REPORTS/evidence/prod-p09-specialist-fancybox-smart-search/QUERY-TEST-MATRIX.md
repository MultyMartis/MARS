# PROD-P09 — Query Test Matrix

| Query | Expectation | Result |
|-------|-------------|--------|
| 2 chars (`ab`) | no useful results; empty payload; frontend: **0** REST calls | **PASS** (REST empty; Playwright `below3_requests=0`) |
| `алк` (3+) | Услуги present | **PASS** (services ≥1; UI group present) |
| `Кост` / `Костюк` | Специалисты | **PASS** (Kostyuk #1033) |
| article fragment | Статьи | **PASS** (mixed `леч` articles=5) |
| `конта` | Страницы (Контакты) | **PASS** |
| multi-type (`леч`) | multiple groups | **PASS** (services+articles+pages) |
| `zzzqqqxyz` | «Ничего не найдено» | **PASS** |
| title vs body | title matches rank above body-only | **PASS** (deterministic score tiers; specialist title hit score 60+ for contains) |

Evidence: `LIVE-VALIDATION.json`, `PLAYWRIGHT-QA.json`, `PLAYWRIGHT-QA-SUPPLEMENT.json`, `PHP-LINT-AND-RELEVANCE.json`.
