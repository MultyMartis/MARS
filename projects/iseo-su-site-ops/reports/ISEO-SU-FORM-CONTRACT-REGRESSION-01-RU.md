# ISEO-SU — регрессия контракта форм (`pf_contact` / `pf_phone`)

**Задача:** `ISEO-SU-SITE-OPS-FORM-CONTRACT-REGRESSION-01`  
**Дата:** 2026-09-09  
**Статус:** **COMPLETE** — все доказанные дефекты `pf_contact` как видимый телефон закрыты.

---

## Что было сломано

После фикса вебинара тот же контрактный дефект искали по всему live-сайту i-seo.su.

Сломанный шаблон:

- видимое поле телефона: `name="pf_contact"`
- нет `name="pf_phone"`
- отправка на `/page__FORM.php`
- обработчик отвечает HTTP 200 и телом `false`

Правильный контракт:

- скрытый `pf_contact=<метод>` (на этом семействе — `WhatsApp`)
- видимый телефон: `name="pf_phone"`
- согласие `personal_data_consent=1`

---

## Масштаб

| Показатель | Значение |
|------------|----------|
| Живых поверхностей `/page__FORM.php` | 137 |
| Сломанных до фикса | **90** |
| После GET-рескана | **0** |
| Файлов-источников на проде | **18** (1 общий include + 17 inline) |
| Страниц, которые наследуют общий SEO-include | 75 |

Страница ресторана `https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html`: **BROKEN → HEALTHY**.

Городские и нишевые SEO-страницы (СПб, Казань, питомник, СМИ, ресторан и т.д.) чинились **один раз** в `content-form-seo.php`, не постранично.

---

## Что не трогали

- обработчик `/page__FORM.php` и `common.js`
- HMAC, honeypot, min-fill, rate limit, duplicate, серверный consent
- title / description / H1 / canonical / sitemap / меню / контент / дизайн
- чужой WIP в основном индексе git

`blog.html`: контракт полей исправлен; чекбокс согласия по-прежнему отсутствует (остаток WAVE 01 — UI не выдумывали).

---

## Безопасность (финальное состояние)

HMAC, honeypot, min-fill, rate limit, duplicate, consent guard — **ACTIVE**.  
Получатель: `nikel007i33@yandex.ru`.  
`test_mode`: **OFF**.

Незатронутые формы (главная, вебинар): **регрессии нет**.
