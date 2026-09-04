# ISEO-SU — WAVE 04: семь нишевых SEO-посадочных (закрытие)

**Задача:** `ISEO-SU-SITE-OPS-NICHE-PAGES-WAVE-04`  
**Дата:** 2026-09-04  
**Статус:** **COMPLETE** — 7 лендингов live, хаб услуг обновлён, sitemap 132→139

---

## Семь URL

1. https://i-seo.su/services/seo/prodvizhenie-sajta-pitomnika.html  
2. https://i-seo.su/services/seo/prodvizhenie-sajta-smi.html  
3. https://i-seo.su/services/seo/prodvizhenie-sajta-restorana.html  
4. https://i-seo.su/services/seo/prodvizhenie-internet-magazina-zapchastej.html  
5. https://i-seo.su/services/seo/prodvizhenie-sajta-internet-provajdera.html  
6. https://i-seo.su/services/seo/prodvizhenie-internet-magazina-kosmetiki.html  
7. https://i-seo.su/services/seo/prodvizhenie-internet-magazina-czvetov.html  

---

## Источник

Клон с актуального канонического файла `prodvizhenie-avtomobilnogo-sajta.html` (структура HTML + PHP includes; не live-HTML без consent).

---

## Что изменено

На каждой странице только: `<title>` и meta description, H1, первый intro после H1, последний уровень хлебных крошек, self-canonical (на источнике canonical не было).

На хабе `services/seo.html`: **+7** ссылок в нишевом списке (31 → 38).

Sitemap: инвентарь + генератор → **139** URL.

Исключение «Питомник»: кейс Drive Avenue заменён на **Maltipoo Honey Club** (`/cases/maltipoo-honey-club.html`, HTTP 200 подтверждён до деплоя).

---

## Что не трогали

Метрики компании, тарифы, этапы, «что входит», калькулятор, акции, команда, отзывы, FAQ (все 4), бесплатный аудит, другие услуги. На 6 из 7 страниц блок кейсов без изменений. HMAC / антиспам / получатель `nikel007i33@yandex.ru` без изменений. Глобальный `robots.txt` без изменений. Бэклог SEO-review не открывали.

---

## Consent

Базовый consent форм и consent результата калькулятора сохранены (через общие PHP includes). Live: 7/7 страниц с consent; регрессии форм нет.

---

## Self-canonical / индексация

7/7: HTTP 200, indexable (`index, follow`), self-canonical = URL страницы.

---

## Sitemap

До: 132. После: 139. Новые URL 7/7 в `sitemap-static.xml`. Дубликаты 0. Completeness PASS. Корневой `sitemap.xml` здоров (static + WP).

---

## Валидация

Live QA всех 7 страниц, хаба и sitemap — PASS. Smoke регрессии (главная, хаб, авто-источник, регионы, США/ОАЭ, tariff-calc, sitemaps) — все HTTP 200.

Полные доказательства: `ISEO-SU-NICHE-PAGES-WAVE-04-EVIDENCE-v1.md`.
