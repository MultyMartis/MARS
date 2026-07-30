# OPERATIONAL END-TO-END TESTS v1

## Local harness

Pass: **30** · Fail: **0** · Gap: **1**

| Fixture | Mode | Result |
|---------|------|--------|
| STRUCT | structure | **PASS** |
| C01_unnamed_audit_phone | AI OFF local | **PASS** |
| C02_named_seo_site | AI OFF local | **PASS** |
| C03_email_only | AI OFF local | **PASS** |
| C04_telegram_handle | AI OFF local | **PASS** |
| C05_unknown_service | AI OFF local | **PASS** |
| C06_malformed_insufficient | AI OFF local | **PASS** |
| C07_reprocess_same_msg | AI OFF local | **PASS** |
| C08_repeat_phone | AI OFF local | **PASS** |
| C09_same_site_diff_contact | AI OFF local | **PASS** |
| TG_FAIL_POLICY | telegram_fail | **PASS** |
| AI_VALID_JSON | AI ON mocked | **PASS** |
| AI_INVALID_JSON | AI ON mocked | **PASS** |
| AI_EMPTY | AI ON mocked | **PASS** |
| AI_BAD_SERVICE | AI ON mocked | **PASS** |
| AI_UNSAFE_PRICE | AI ON mocked | **PASS** |
| AI_DEADLINE | AI ON mocked | **GAP** |
| AI_GUARANTEE | AI ON mocked | **PASS** |
| AI_FABRICATED | AI ON mocked | **PASS** |
| AI_TIMEOUT_SIM | AI ON mocked | **PASS** |
| TG_SPECIAL_CHARS | telegram_format | **PASS** |
| ADMIN_/help | admin_local | **PASS** |
| ADMIN_/status | admin_local | **PASS** |
| ADMIN_/ai_status | admin_local | **PASS** |
| ADMIN_/health | admin_local | **PASS** |
| ADMIN_/stats | admin_local | **PASS** |
| ADMIN_/last_error | admin_local | **PASS** |
| ADMIN_/config | admin_local | **PASS** |
| ADMIN_/unknown_xyz | admin_local | **PASS** |
| ADMIN_UNAUTH_AI_ON | admin_auth | **PASS** |
| ADMIN_AI_ON_OFF | admin_write | **PASS** |

## Live n8n synthetic executions (Operational.dev)

Method: temporary webhook + flatten (removed after restore). Telegram send remained **disabled**. Gmail mutate remained **disabled**. OpenRouter remained **disabled**. Sheets append nodes left disabled due to stale column-cache error against v2 headers.

| Case | Exec status | OpenRouter | Prepare AI | Format | Error Handler | Copy separator |
|------|-------------|------------|------------|--------|---------------|----------------|
| LIVE_C01 | success | false | false | true | false | true |
| LIVE_C02 | success | false | false | true | false | true |
| LIVE_C08 | success | false | false | true | false | true |
| LIVE_TG_FAIL | success | false | false | true | true | true |
| LIVE_CHARS | success | false | false | true | false | true |

### Sanitized card previews

#### LIVE_C01

```
Повторная обработка

Клиент: —
Контакты: +<REDACTED_NUM> (телефон)
Сайт: —
Услуга: Аудит
Источник: /audit

Кратко: Нужен аудит сайта SYNTHETIC_TEST, срочно

Чего не хватает: имя; сайт
Качество: Нужны уточнения — Нужны уточн
```

#### LIVE_C02

```
Повторная обработка

Клиент: Синтетик Тестов
Контакты: synth.c02@example.test (email)
Сайт: synth-c02.example.test
Услуга: SEO
Источник: —

Кратко: Нужно SEO продвижение SYNTHETIC_TEST

Чего не хватает: текст заявки
Каче
```

#### LIVE_C08

```
Повторная обработка

Клиент: —
Контакты: +<REDACTED_NUM> (телефон)
Сайт: —
Услуга: Другое
Источник: —

Кратко: Другое письмо тот же телефон SYNTHETIC_TEST

Чего не хватает: имя; сайт
Качество: Нужны уточнения — Нужны уточне
```

#### LIVE_TG_FAIL

```
Повторная обработка

Клиент: —
Контакты: +<REDACTED_NUM> (телефон)
Сайт: —
Услуга: Другое
Источник: —

Кратко: Нужна консультация по непонятной услуге SYNTHETIC_TEST

Чего не хватает: имя; сайт
Качество: Нужны уточнения — Н
```

#### LIVE_CHARS

```
Повторная обработка

Клиент: A &lt;B&gt; &amp; C
Контакты: +<REDACTED_NUM> (телефон)
Сайт: —
Услуга: Другое
Источник: —

Кратко: Спецсимволы &lt;tag&gt; &amp; more SYNTHETIC_TEST

Чего не хватает: сайт; текст заявки
Качеств
```


## Notes

- Duplicate headers showing «Повторная обработка» on later live runs are expected after DEDUP_INDEX synthetic keys were written.
- Google Sheets node append path for v2 tabs requires column-list refresh before production enablement.
