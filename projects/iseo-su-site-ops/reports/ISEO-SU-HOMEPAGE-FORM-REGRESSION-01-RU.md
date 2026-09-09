# ОТЧЁТ — Регрессия форм главной i-seo.su (HOMEPAGE-FORM-REGRESSION-01)

**Дата:** 2026-09-09  
**Статус:** ЗАВЕРШЕНО — причина доказана, приём заявок с главной восстановлен, security сохранён

## Что сломалось

На https://i-seo.su/ оператор увидел: поле «Адрес сайта» вело себя как обязательное; после отправки страница перезагружалась; success не показывался; письмо не приходило. То же в модальной форме.

## Причина (доказано)

1. В `common.js` функция `checkEmptyFields` ошибочно требовала заполнения любого `*_site`, хотя в HTML и PHP поле опционально.  
2. Обработчики `#page__FORM_send` и `#callback__FORM_send` не вызывали `preventDefault`, поэтому при ошибке валидации браузер делал обычный submit на `action=""` → reload без AJAX и без почты.

Исправление endpoint для SEO-форм (`#page__FORM_send_seo`) на это **не влияло**.

## Что сделано

Минимальный патч только `js/common.js`:

- `preventDefault` + `return false` на главной и в модалке;  
- «Адрес сайта» обязателен в JS только если у input есть HTML `required`.

Live и source выровнены (SHA-256 `5894E145…`). Тестовые письма — в `test_mode` на `im.work@mail.ru`; затем `test_mode` OFF. Recipient production: `nikel007i33@yandex.ru`. HMAC / honeypot / min-fill / rate / duplicate / consent — ACTIVE.

## Проверка

После фикса: отправка с пустым и заполненным сайтом для обеих форм — AJAX, HTTP 200, `true`, success UI, без reload. Негатив: без согласия / honeypot — отказ. Дым webinar/restaurant/city/niche — без регрессии endpoint.

## Не менялось

Дизайн, SEO (title/description/H1/canonical/robots), меню, sitemap, PHP-контракты полей, ослабление anti-spam — нет.
