# INTLSEO FIRST-CONTACT STANDARD v1

**Phase:** 3G.1 (+ text/number hygiene **3G.2**)  
**Status:** approved standard + offline harness PASS; live seed 3G.1.1; profile numbers 3G.2  
**Versions:**
- `reply_standard_version` = `iseo-first-contact-v1.0`
- `reply_template_version` = `iseo-template-set-v1.0`
- `reply_policy_version` = `iseo-sales-policy-v1.0`
- `recipient_personalization_version` = `iseo-recipient-name-v1.1` (3G.2)
- Legacy stamp retained for rollback only: `sm-reply-v2.1`

## Purpose

Единый стандарт первого контакта INTLSEO для менеджерских карточек: детерминированный выбор одного из пяти утверждённых шаблонов, персонализация имени отправителя на уровне получателя карточки, отдельная подсказка менеджеру. Клиентский текст **никогда** не отправляется автоматически.

## Hard rules

1. **No auto-send** — черновик только для ручного копирования менеджером.
2. **AI OFF** по умолчанию; constrained AI assist contract существует, но глобально не включён.
3. Компания в клиентском тексте: **INTLSEO** (если не задано иное валидное company snapshot).
4. Приветствие: `Добрый день!`
5. Представление: `Меня зовут <approved_first_name>, компания INTLSEO.`
6. Никнейм **Мопс** никогда не попадает в клиентский текст; для этого получателя — **Михаил**.
7. Без гарантий позиций/сроков/роста; без тариф-first; без выдуманного аудита сайта.
8. Precedence маршрутизации: **T5 > T4 > T3 > T1 > T2** (безопасный fallback — T2).

## Approved template IDs

| ID | Meaning | Typical CTA |
|----|---------|-------------|
| `T1_EXISTING_SITE_GROWTH` | Сайт указан, SEO/рост | согласие на аудит + видео-презентация |
| `T2_SITE_MISSING` | Сайт отсутствует / невалидное поле | уточнить наличие сайта |
| `T3_MEANINGFUL_TASK` | Описана осмысленная задача | аудит с controlled task_summary |
| `T4_NEW_SITE_DEVELOPMENT` | Новый сайт / разработка | уточнить стадию; без audit CTA |
| `T5_SPECIAL_PROJECT` | Спец/legal/материалы | запросить материалы; без audit CTA |

## Separation of surfaces

| Surface | Contents |
|---------|----------|
| Customer copy (`<pre>`) | Только утверждённый клиентский текст |
| Manager guidance | Подсказка вне copy-блока; без internal codes |
| Shared LEADS metadata | template id, versions, mode — без имени получателя |
| Recipient draft storage | персональный текст + snapshot имени |

## Runtime libraries (MARS package)

- `implementation/runtime-libs/approved-template-router-v1.mjs`
- `implementation/runtime-libs/approved-template-renderer-v1.mjs`
- `implementation/runtime-libs/reply-profile-lib.mjs`
- `implementation/runtime-libs/ai-assist-validator-v1.mjs`
- `implementation/runtime-libs/reply-profile-commands-v1.mjs`
- Harness: `implementation/harness/phase3g1-harness.mjs` → **100/100 PASS**

## Contour note (current)

- Ops: active, **45** nodes (`xSnXPy8cEHoZw6xG`); Admin: active, **~84+** after 3G.2 patch (`wLrLp4WQHm1VJmxz`); Sales-Manager-v2 inactive; AI OFF; reminders OFF.
- Authoritative: Parser 3.3 · `LEADS` · `LEAD_EVENTS` · stats epoch 05.08.2026 Europe/Moscow.
- Sender name only from `reply_sender_name`; profiles numbered 1–4 (see [REPLY-PROFILE-NUMBERING-v1.md](REPLY-PROFILE-NUMBERING-v1.md)).
- Operator-facing wording: [TELEGRAM-TEXT-CONTRACT-v2.md](TELEGRAM-TEXT-CONTRACT-v2.md).

## Related

- [RECIPIENT-PERSONALIZED-REPLIES-v1.md](RECIPIENT-PERSONALIZED-REPLIES-v1.md)
- [AI-MANAGER-ASSIST-v1.md](AI-MANAGER-ASSIST-v1.md)
- [REPLY-PROFILE-CONTRACT-v1.md](REPLY-PROFILE-CONTRACT-v1.md)
- Evidence: `evidence/phase3g1/` · `evidence/phase3g1-1/` · `evidence/phase3g2/`
