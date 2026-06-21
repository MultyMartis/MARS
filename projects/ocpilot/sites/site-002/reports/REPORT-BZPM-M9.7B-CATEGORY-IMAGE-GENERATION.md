# REPORT — BZPM M9.7B Category Image Generation

**Режим:** TEST only · local generation · **без deploy** · **без изменения БД** · **без привязки к `oc_category.image`**  
**Authority:** [REPORT — BZPM M9.7A Category Image Reference Audit](c6aca349-50c3-409b-aee7-90cc3560cdd0) (единственный источник Style Contract и Prompt Blueprint)  
**Эталон:** `nejtralnoe-oborudovanie-2.webp` · `teplovoe-oborudovanie-2.webp` · `kholodilno-oborudovanie.webp` (live TEST + локальная копия в `.recovery-temp/m9.7a-audit/`)  
**Статус:** ожидает **ручного визуального утверждения оператора**

---

## 1. Scope

Сгенерированы и подготовлены локально **5 master WebP** для веток neutral hub:

| category_id | Категория | Итоговый файл |
|---:|---|---|
| 301 | Столы | `stoly.webp` |
| 80 | Моечные ванны | `moechnye-vanny.webp` |
| 322 | Подтоварники и подставки | `podtovarniki-i-podstavki.webp` |
| 207 | Зонты вытяжные | `zonty-vytyazhnye.webp` |
| 326 | Тележки сервировочные | `telezhki-servirovochnye.webp` |

**Не выполнено (по заданию):** deploy на TEST, обновление `oc_category.image`, изменение live storefront.

---

## 2. Генератор

| Параметр | Значение |
|---|---|
| Запрошено | **Nano Banana Pro** |
| Фактически использовано | **Cursor `GenerateImage`** с reference images из M9.7A audit cache |
| Причина | В workspace **нет** конфигурации/интеграции «Nano Banana Pro» (grep по `C:\AI MARS` — 0 совпадений). Генерация выполнена доступным image-generation инструментом с промптами и negative-ограничениями из M9.7A Style Contract. |

**UNKNOWN:** эквивалентность вывода Cursor GenerateImage vs Nano Banana Pro на 100% — **не подтверждена**. Оператору рекомендуется сравнить side-by-side с live эталоном на 300×300.

---

## 3. Процесс

1. Повторно скачаны reference masters с `https://zpm.new-site.space/image/catalog/Category-image/`.
2. Визуально изучены эталоны (PNG-превью из M9.7A + повторный просмотр перед генерацией).
3. Для каждой категории сгенерировано **3 варианта** (всего 15).
4. Выбран лучший вариант по критериям: ракурс, освещение, стиль, плотность кластера, обработка металла, соответствие M9.7A Style Contract.
5. Master обработан: resize **H=1800×1200** (aspect 1.5), фон запечён в белый (#FFFFFF), экспорт **WebP quality=90**.
6. Созданы storefront-превью **300×300** (`object-fit: contain` simulation) для QA.

---

## 4. Итоговые файлы (master)

**Путь:** `image/catalog/Category-image/`

| Файл | Выбранный вариант | Canvas | Размер |
|---|---|---:|---:|
| `stoly.webp` | `stoly-v1` | 1800×1200 | 65 KB |
| `moechnye-vanny.webp` | `moechnye-vanny-v1` | 1800×1200 | 83 KB |
| `podtovarniki-i-podstavki.webp` | `podtovarniki-v1` | 1800×1200 | 59 KB |
| `zonty-vytyazhnye.webp` | `zonty-vytyazhnye-v1` | 1800×1200 | 113 KB |
| `telezhki-servirovochnye.webp` | `telezhki-v2` | 1800×1200 | 107 KB |

**Сравнение с эталонными masters (live TEST):**

| Эталон | Canvas | Размер |
|---|---:|---:|
| `nejtralnoe-oborudovanie-2.webp` | 1745×1200 | 710 KB |
| `teplovoe-oborudovanie-2.webp` | 1436×1200 | 687 KB |
| `kholodilno-oborudovanie.webp` | 1295×1200 | 807 KB |

**QA-заметка:** новые masters **корректны по геометрии canvas (H=1200)**, но **значительно легче по весу**, чем оригинальные 3D renders. Перед deploy оператору стоит проверить детализацию металла и отсутствие «AI sheen» на реальном 300×300 resize.

---

## 5. Превью 300×300 (как на hub/megamenu)

Превью для операторского QA:

| Категория | Превью |
|---|---|
| Эталон | `.recovery-temp/m9.7b-generation/previews/reference-nejtralnoe-300x300.png` |
| Столы | `.recovery-temp/m9.7b-generation/previews/stoly-300x300.png` |
| Моечные ванны | `.recovery-temp/m9.7b-generation/previews/moechnye-vanny-300x300.png` |
| Подтоварники | `.recovery-temp/m9.7b-generation/previews/podtovarniki-i-podstavki-300x300.png` |
| Зонты | `.recovery-temp/m9.7b-generation/previews/zonty-vytyazhnye-300x300.png` |
| Тележки | `.recovery-temp/m9.7b-generation/previews/telezhki-servirovochnye-300x300.png` |

Все варианты (15 PNG) сохранены в: `.recovery-temp/m9.7b-generation/variants/`

---

## 6. Выбор вариантов и обоснование

### 6.1 Столы → `stoly-v1`

| Вариант | Вердикт | Причина |
|---|---|---|
| **v1 ✅** | **Выбран** | Чистый кластер из 2 столов; белый фон; high-angle 3/4; satin steel; contact shadows. Соответствует столу из `nejtralnoe-oborudovanie-2.webp`. |
| v2 | Отклонён | Смешанная композиция (стол + ванна + стеллаж) — нарушает category purity. |
| v3 | Резерв | Близок к v1, но чуть менее выразительная глубина кластера. |

**Сравнение с эталоном:** ракурс и освещение совпадают; плотность ниже эталона (2 vs 4 объекта) — **допустимо** для branch card.

---

### 6.2 Моечные ванны → `moechnye-vanny-v1`

| Вариант | Вердикт | Причина |
|---|---|---|
| **v1 ✅** | **Выбран** | Двухчашечная + одночашечная ванна; drainboard; белый фон; минимальные краны; тот же типаж, что в neutral root cluster. |
| v2 | Резерв | Хорош, но чуть более «плоская» композиция. |
| v3 | Отклонён | Sliding doors менее типичны для ZPM line vs открытая/закрытая тумба v1. |

**Сравнение с эталоном:** металл и студийный свет в семействе; на 300×300 читаются чаши и backsplash.

---

### 6.3 Подтоварники и подставки → `podtovarniki-v1`

| Вариант | Вердикт | Причина |
|---|---|---|
| **v1 ✅** | **Выбран** | Только **низкие напольные подставки** и low platform — **без overshelf / tabletop shelf**. 3 типа в кластере. |
| v2 | Резерв | Корректные floor stands, но менее разнообразный набор. |
| v3 | Отклонён | Слишком однотипные low trays; слабее category storytelling. |

**Спец-ограничение M9.7B соблюдено:** нет настольных надстроек и overshelf.

---

### 6.4 Зонты вытяжные → `zonty-vytyazhnye-v1`

| Вариант | Вердикт | Причина |
|---|---|---|
| **v1 ✅** | **Выбран** | High-angle 3/4 (не low-angle outlier вентиляции); 2 ширины; видны baffle filters и duct stub; белый фон. |
| v2 | Отклонён | LED-акценты на внутренней кромке — Style Contract для neutral **избегает** цветных LED. |
| v3 | Резерв | Хороший кластер, но меньше «grounding» и глубины vs v1. |

**Сравнение с эталоном:** сознательно **не** копируется low-angle `ventilyacionnoe-oborudovanie.webp` (M9.7A outlier rule).

---

### 6.5 Тележки сервировочные → `telezhki-v2`

| Вариант | Вердикт | Причина |
|---|---|---|
| v1 | Резерв | Корректные 2-tier + 3-tier, но плоское side-by-side размещение. |
| **v2 ✅** | **Выбран** | Foreground/background overlap — ближе к тележке в `nejtralnoe-oborudovanie-2.webp`; raised edges; casters + brakes. |
| v3 | Отклонён | Менее естественная кластерная глубина. |

**Сравнение с эталоном:** типаж тележки из root neutral cluster узнаваем; satin steel и contact shadows совпадают.

---

## 7. Сводное сравнение с `nejtralnoe-oborudovanie-2.webp`

| Критерий | Эталон | 5 итоговых | Оценка |
|---|---|---|---|
| Ракурс | High-angle 3/4 front-right | High-angle 3/4 | ✅ |
| Освещение | Soft diffuse studio, top-front-left | Soft diffuse studio | ✅ |
| Стиль | Commercial 3D product viz | Commercial 3D product viz | ✅ (pending operator) |
| Плотность кластера | 4 объекта, ~85% кадра | 2–3 объекта, ~75–85% | ⚠️ чуть ниже плотность |
| Обработка металла | Satin brushed SS | Satin brushed SS | ✅ (pending 300×300 QA) |
| Фон | Белый / светло-нейтральный | Белый #FFFFFF | ✅ |
| Тени | Soft contact shadows | Soft contact shadows | ✅ |
| Запреты | Нет интерьера/людей/еды | Соблюдены | ✅ |

**Общий вердикт:** визуально **в одном семействе** с эталоном; требуется **human HITL** на читаемость 300×300 и отсутствие AI-артефактов.

---

## 8. Готовность к deploy

| Шаг | Статус |
|---|---|
| Master WebP локально в `image/catalog/Category-image/` | ✅ готово |
| Naming по M9.5 / M9.7A (`{seo-slug}.webp`) | ✅ |
| Canvas H=1200 | ✅ |
| Upload на TEST FTP | ⏸ **не выполнялось** |
| `oc_category.image` update (301, 80, 322, 207, 326) | ⏸ **не выполнялось** |
| Image cache flush | ⏸ **не выполнялось** |
| Hub/megamenu visual QA на TEST | ⏸ после deploy |

**Deploy checklist (для следующего этапа после approval):**

1. Upload 5 WebP → `/image/catalog/Category-image/` на TEST.
2. SQL update `oc_category.image` для cat 301, 80, 322, 207, 326.
3. Flush OpenCart image cache / thumb cache.
4. QA URLs: `/katalog/nejtralnoe-oborudovanie` hub + megamenu.
5. Side-by-side 300×300 с `nejtralnoe-oborudovanie-2-300x300.webp`.

---

## 9. Changed files

| Путь | Действие |
|---|---|
| `image/catalog/Category-image/stoly.webp` | **created** |
| `image/catalog/Category-image/moechnye-vanny.webp` | **created** |
| `image/catalog/Category-image/podtovarniki-i-podstavki.webp` | **created** |
| `image/catalog/Category-image/zonty-vytyazhnye.webp` | **created** |
| `image/catalog/Category-image/telezhki-servirovochnye.webp` | **created** |
| `projects/ocpilot/sites/site-002/reports/REPORT-BZPM-M9.7B-CATEGORY-IMAGE-GENERATION.md` | **created** |
| `.recovery-temp/m9.7b-generation/` (variants + previews) | **created** (QA cache, не deliverable) |
| `.recovery-temp/m9.7a-audit/` | refreshed reference download |

**Не изменялись:** TEST site, DB, `oc_category`, templates, deploy scripts.

---

## 10. Git status

Локальные новые файлы в `image/catalog/Category-image/` и отчёт — **untracked/uncommitted**. Commit **не создавался** (default policy).

---

## 11. UNKNOWN / SECURITY RISK

**UNKNOWN:**

- Эквивалентность генерации через Cursor GenerateImage vs запрошенный **Nano Banana Pro**.
- Достаточна ли детализация masters при resize 300×300 vs оригинальные ~700 KB renders (вес новых файлов 59–113 KB).
- Нужен ли re-gen через Nano Banana Pro после operator feedback.

**SECURITY RISK:** нет.

---

## 12. Следующий шаг

**Остановка.** Ожидается ручное визуальное утверждение оператора:

- `approved` — можно переходить к deploy milestone (upload + DB, отдельная задача)
- `fix <category>` — перегенерация конкретной ветки
- `regen all via Nano Banana Pro` — если оператор предоставит доступ/интеграцию
