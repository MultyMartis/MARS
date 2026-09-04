# ISEO-SU — Роллаут низкой высоты первого экрана на 14 новых SEO-лендингах (RU)

**Задача:** ISEO-SU-SITE-OPS-NEW-SEO-LANDINGS-SMALL-HEIGHT-OVERLAP-ROLLOUT-01  
**Дата:** 2026-09-04  
**Итог:** COMPLETE — 14 страниц безопасны / пилот обобщён

## В чём был дефект

Общее CSS-правило .page_scene_inner { height: 100vh } жёстко ограничивало высоту первого экрана. При длинном вводном тексте контент выходил за пределы блока, а секция #SecondScreen начиналась в обычном потоке документа сразу после фиксированных 100vh — визуально наезжала на переполненный первый экран.

## Почему проявлялся при небольшой высоте

На высоких мониторах (например 1080p) длинный intro ещё помещался в 100vh. На низких десктопных высотах (650–720px) intro превышал viewport → overflow + overlap.

## Почему оригиналы могли выглядеть нормально

Исходные шаблоны (-regionakh, авто-ниша, zarubezhnye) имеют более короткий первый экран или иной контент; они оставлены контрольной группой без изменений. Новые 14 лендингов получили более длинные approved intro.

## Что показал пилот Новосибирска

Operator визуально одобрил пилот: height: auto + min-height: 100vh устраняет overlap. Пилот был изолирован классом city-seo-novosibirsk-height-pilot и отдельным CSS.

## Как обобщили fix

**MODEL A:** один общий body-класс 
ew-seo-landing-flex-first-screen и один CSS production-source/css/new-seo-landing-flex-first-screen.css на все 14 новых лендингов. Пилотные класс и CSS удалены. Legacy/control не трогали.

## Сколько страниц проверено

14/14 (5 city + 7 niche + 2 international) на матрице viewport, включая 1440×600 / 1366×650 и mobile 390×844 / 360×800. Post-rollout overlaps: **0**.

## Какие страницы получили final layout safety

Все 14 новых SEO-лендингов из контура rollout.

## SEO / content / forms

Title, description, H1, intro, canonical, sitemap (139), кросс-ссылки городов, hub-ссылки ниш, статус меню/sitemap USA/UAE, формы/consent/калькулятор — **без изменений**.

## Итог

Роллаут завершён. Пилот Новосибирска сохранён по поведению и обобщён. Production/source aligned. Документация и Git sync — в основном REPORT.
