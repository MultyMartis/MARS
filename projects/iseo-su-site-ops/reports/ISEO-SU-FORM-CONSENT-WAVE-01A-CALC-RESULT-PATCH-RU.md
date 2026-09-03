# ISEO-SU — FORM CONSENT WAVE 01A (калькулятор после «Рассчитать»)

**Task ID:** `ISEO-SU-SITE-OPS-FORM-CONSENT-WAVE-01A-CALC-RESULT-FORM-PATCH`  
**Дата:** 2026-09-03  
**Статус:** **COMPLETE — WAVE 1 FULLY RECONCILED**

---

## Что пропустили в WAVE 1

В WAVE 1 закрыли обычные контактные `<form>`. Остался скрытый кейс: после кнопки **«Рассчитать»** на SEO-калькуляторе появляется блок «Получите персональный план…» с именем/телефоном. Это был не полноценный form surface (поля без `name`, ссылка на `#callback`, мягкая сноска без checkbox). Оператор увидел пробел на `https://i-seo.su/services/seo.html`.

## Почему surface был скрытым

Блок живёт в DOM всегда, но визуально относится к **результату расчёта** (JS снимает `hidden` с результата). Сканеры WAVE 1 ориентировались на классические формы, а не на `.tariff-calc-request`.

## Source authority

Единый шаблон:

`wp-content/themes/iseoblog/template-parts/tarif-calc.php`  
(канон в репо: `production-source/theme/iseoblog/template-parts/tarif-calc.php`)

Дублей разметки нет: все страницы с этим калькулятором берут один include. Live подтверждено: `/services/seo.html`, `/tariff-calc`. Home / glossary / blog этот блок не показывают.

## Что исправлено

1. Блок превращён в форму `callback__FORM_tariff_calc` с полями `cf_*` и обязательным `personal_data_consent=1`.
2. В `common.js` — отправка на существующий `callback__FORM.php` через тот же `checkEmptyFields()`.
3. Стили для consent / button в `main.css` и theme `style.css`.
4. Серверный guard WAVE 1 **не дублировали** — POST идёт в уже защищённый `callback`.

## Проверки

- UI: checkbox перед кнопкой, ссылка на `/privacy-policy.html`, без precheck.
- Direct POST без согласия / `0` / `false` / мусор → `false`, писем 0.
- Positive под временным `test_mode` → `true`, затем `test_mode` OFF; прод-получатель только `nikel007i33@yandex.ru`.
- HMAC / antispam / secret не менялись.

## Итог

WAVE 1 по consent **полностью согласован (RECONCILED)**. WAVE 2 / WAVE 3 не запускались.
