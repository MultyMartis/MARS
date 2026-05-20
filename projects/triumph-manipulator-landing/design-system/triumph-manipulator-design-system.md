# Triumph Manipulator — Design System

**Статус:** канонический документ для **всех будущих** версий лендинга Triumph Manipulator (включая Landing V2).  
**Источник правды:** этот файл + утверждённые макеты/ассеты репозитория.  
**Область:** визуальная система, CSS-закон, правила для AI design / AI frontend агентов.  
**Не является:** автоматической валидацией, сборкой, кодом рантайма.

**Связь с V1 (только справка):** палитра и часть семантики цветов извлечены из `workspaces/triumph-manipulator-landing/src/scss/utils/_tokens.scss` и `_variables.scss`. Типографика, радиусы, высоты кнопок и трекинг в **этом документе** — **целевой канон для новых версий** и могут **расходиться** с текущей реализацией V1 без изменения V1-кода.

---

## 1. Philosophy

- **Промышленная геометрия:** только прямые углы, явные линии, модульная сетка. Никаких «мягких» облачных форм.
- **Тёмный премиум:** глубокий тёмный фон, контрастный светлый текст на тёмных поверхностях; на светлых секциях — плотный тёмный текст и чёткие границы.
- **Коммерческое тяжёлое оборудование:** визуальный язык B2B / аренда спецтехники: уверенность, массивность, дисциплина, без «стартап-иллюстраций».
- **Один закон для всех агентов:** любой AI-агент обязан сверяться с этим документом до генерации макета или CSS; отклонения только по явному human-approved исключению (должно быть зафиксировано в задаче).

---

## 2. Visual direction

- Тёмные плоскости (`surface`), локальные светлые зоны для контраста (например блок доверия/отзывов на светлом фоне).
- Акцент — **фирменный красный**, используется дозированно: CTA, ключевые заголовочные акценты, индикаторы, правила-разделители.
- Фотография: реальная техника, площадки, рабочий контекст; без стоковых «улыбающихся офисов».
- Композиция: сильный горизонталь/вертикаль, крупные блоки, предсказуемый ритм секций.

---

## 3. Brand feeling

- **Надёжность и ответственность** (сервис, логистика) — через стабильную сетку, сдержанную палитру, отсутствие игривости.
- **Сила и масштаб** — крупная типографика display, плотные блоки, минимум «воздушного SaaS».
- **Профессионализм** — сдержанные тени (если разрешены — см. раздел 30), без декоративного шума.

---

## 4. Allowed / forbidden styles

**Разрешено**

- Плоские заливки, линейные и радиальные градиенты **только** в рамках раздела 35.
- Тонкие обводки `1px` / `2px` для структуры.
- Uppercase для ограниченного числа элементов (eyebrow, редкие подписи) при `letter-spacing: 0` (без разрежения/сжатия).
- Строгие прямоугольные карточки, табличная логика, выравнивание по базовой линии.

**Запрещено**

- Любой `border-radius` **≠ 0** (см. раздел 11).
- Glassmorphism (`backdrop-filter` «матовое стекло»), neumorphism, «мягкий SaaS», стартаповая эстетика (пузыри, скруглённые «карточки приложений», pastel UI).
- Случайные самодельные иконки от AI (см. разделы 19–20, 38).
- Произвольные шрифты вне Roboto / Montserrat для UI текста и заголовков.
- `em` / `rem` / `%` / `clamp()` для **`font-size`** (см. раздел 8 — только `px`).
- Любой `letter-spacing` **≠ 0** (см. раздел 10).

---

## 5. Color system

Ниже — **формализованная палитра Triumph** по текущим семантическим токенам V1 (`_tokens.scss`). Имена сохраняйте в CSS custom properties или препроцессорных переменных 1:1 для предсказуемости.

| Семантика | HEX / значение | Правила использования |
|-----------|----------------|------------------------|
| `--tm-surface` | `#050b16` | Основной фон страницы / тёмные секции. |
| `--tm-surface-2` | `#07111f` | Поднятая тёмная плоскость, полосы, «второй уровень». |
| `--tm-surface-3` | `#0b1628` | Вложенные тёмные блоки, глубина без «стекла». |
| `--tm-text-on-dark` | `#d8dde6` | Основной текст на тёмном фоне (было `$tm-color-ink`). |
| `--tm-text-on-dark-muted` | `rgba(216, 221, 230, 0.78)` | Вторичный текст на тёмном. |
| `--tm-text-on-light` | `#0a1220` | Основной текст на белом/светлом фоне. |
| `--tm-text-on-light-soft` | `rgba(10, 18, 32, 0.82)` | Лид / подстрока на светлом. |
| `--tm-light-section` | `#f6f7f9` | Фон светлых секций (доверие, вспомогательные блоки). |
| `--tm-white` | `#ffffff` | Карточки на светлом, чистые поля форм, инверсия кнопок. |
| `--tm-muted` | `#7b8494` | Подписи, вторичные метки на светлом. |
| `--tm-accent` | `#e30621` | Основной бренд-красный, CTA, акцентные слова в заголовке. |
| `--tm-accent-hover` | `#f01832` | Hover активных красных элементов (фон/бордер/градиентная сторона). |
| `--tm-accent-dark` | `#b90018` | Press / тёмная сторона градиента, «вдавленное» состояние. |
| `--tm-border-on-light` | `#d9dde5` | Разделители и рамки на светлом. |
| `--tm-border-on-dark` | `rgba(255, 255, 255, 0.16)` | Тонкие линии на тёмном без «свечения». |
| `--tm-whatsapp` | `#25d366` | Только иконка/лейбл мессенджера (не перекрашивать в бренд-красный). |
| `--tm-telegram` | `#27a7e7` | То же. |
| `--tm-max` | `#4f55ff` | То же. |

**Дополнительно из фирменного логотипа (SVG):** тёмно-синий `#090c27` и красный `#e1002d` встречаются в экспорте логотипа; для **веб-UI** приоритет — таблица выше (`#0a1220` / `#e30621`). Если нужно пиксель-в-пиксель совпадение с печатным логотипом — согласовать отдельно.

**Пример: корневые токены (CSS)**

```css
:root {
    color-scheme: dark;
    --tm-surface: #050b16;
    --tm-surface-2: #07111f;
    --tm-surface-3: #0b1628;
    --tm-text-on-dark: #d8dde6;
    --tm-text-on-dark-muted: rgba(216, 221, 230, 0.78);
    --tm-text-on-light: #0a1220;
    --tm-text-on-light-soft: rgba(10, 18, 32, 0.82);
    --tm-light-section: #f6f7f9;
    --tm-white: #ffffff;
    --tm-muted: #7b8494;
    --tm-accent: #e30621;
    --tm-accent-hover: #f01832;
    --tm-accent-dark: #b90018;
    --tm-border-on-light: #d9dde5;
    --tm-border-on-dark: rgba(255, 255, 255, 0.16);
    --tm-whatsapp: #25d366;
    --tm-telegram: #27a7e7;
    --tm-max: #4f55ff;
}
```

**Пример: тело страницы на тёмной теме**

```css
body {
    margin: 0;
    background: var(--tm-surface);
    color: var(--tm-text-on-dark);
}
```

**Пример: светлая секция**

```css
.section--light {
    background: var(--tm-light-section);
    color: var(--tm-text-on-light);
}
```

---

## 6. Typography system

- **Body / UI text:** `Roboto`, `Arial`, `sans-serif`.
- **Display / headings / кнопки (подпись):** `Montserrat`, `Arial`, `sans-serif`.
- Все размеры **`font-size` только в `px`** (раздел 8).
- **Никакого произвольного letter-spacing** — всегда `0` (раздел 10).

```css
body {
    font-family: 'Roboto', Arial, sans-serif;
    font-weight: 400;
}

h1,
h2,
h3,
h4,
h5,
h6,
.tm-display {
    font-family: 'Montserrat', Arial, sans-serif;
    font-weight: 500;
    letter-spacing: 0;
}
```

Подключение шрифтов — через утверждённый проектный способ (локально или Google Fonts); в HTML/CSS **не подключать** случайные CDN без ревью.

---

## 7. Font weights

| Роль | Вес | Примечание |
|------|-----|------------|
| Основной текст (body, списки, формы) | **400** | Канон default. |
| Заголовки, подписи кнопок, навигация | **500** | Без искусственного `800/900` unless human-approved. |
| Жирное выделение внутри абзаца | **500** или **400** + цвет/контраст | Предпочтительно не раздувать шкалу весов. |

```css
p,
li,
label,
input,
textarea {
    font-weight: 400;
}

h1,
h2,
h3,
.tm-button {
    font-weight: 500;
}
```

---

## 8. Font sizes

**Закон:** все `font-size` **только в `px`**. Запрещено: `rem`, `em`, `%`, `clamp()` для размера шрифта.

Рекомендуемая шкала (корректируется только решением владельца продукта; AI не «добавляет от себя» ступени):

| Токен | px | Применение |
|-------|-----|------------|
| `--tm-fs-caption` | 12 | Подписи, мелкий legal. |
| `--tm-fs-small` | 14 | Вторичный текст, таблицы. |
| `--tm-fs-body` | 16 | Основной текст. |
| `--tm-fs-lead` | 18 | Лид-абзацы. |
| `--tm-fs-subtitle` | 22 | Крупный подзаголовок. |
| `--tm-fs-h3` | 24 | H3. |
| `--tm-fs-h2` | 32 | H2 / крупные секции. |
| `--tm-fs-h1` | 48 | H1 desktop (см. responsive). |

**Пример**

```css
:root {
    --tm-fs-caption: 12px;
    --tm-fs-small: 14px;
    --tm-fs-body: 16px;
    --tm-fs-lead: 18px;
    --tm-fs-subtitle: 22px;
    --tm-fs-h3: 24px;
    --tm-fs-h2: 32px;
    --tm-fs-h1: 48px;
}

p {
    font-size: var(--tm-fs-body);
}

h1 {
    font-size: var(--tm-fs-h1);
}
```

**Responsive:** менять размер шрифта **ступенчато медиазапросами**, по-прежнему в `px`:

```css
h1 {
    font-size: 40px;
}

@media (min-width: 1024px) {
    h1 {
        font-size: 48px;
    }
}
```

---

## 9. Line-height rules

**Закон:**

- **Текст** (параграфы, списки, лид, подписи полей): `line-height = font-size + 4px` (используйте `calc`).

```css
p {
    font-size: 16px;
    line-height: calc(16px + 4px);
}

.lead {
    font-size: 18px;
    line-height: calc(18px + 4px);
}
```

- **Заголовки и кнопки:** `line-height: 1`.

```css
h1,
h2,
h3,
.tm-button {
    line-height: 1;
}
```

---

## 10. Letter-spacing rules

**Закон:** `letter-spacing: 0` для **всех** элементов. Запрещены отрицательные значения, разрежение в `em`, `uppercase + tracking`.

```css
* {
    letter-spacing: 0;
}
```

(На практике задавайте явно на типовых классах; глобальный селектор — иллюстрация закона.)

---

## 11. Border-radius policy

**Закон:** `border-radius: 0` **всегда** для всех компонентов: кнопки, поля, карточки, модалки, изображения в рамках, чипы, тосты.

```css
.btn,
.card,
.input,
.modal__dialog,
img.tm-framed {
    border-radius: 0;
}
```

---

## 12. Container system

Канон ширины и отступов согласовать с утверждённым макетом. **Ориентир из V1 variables:** максимальная ширина контента **1540px**, горизонтальные паддинги **72px / 32px / 16px** (desktop / tablet / mobile).

```css
:root {
    --tm-container-max: 1540px;
    --tm-container-pad-x-desktop: 72px;
    --tm-container-pad-x-tablet: 32px;
    --tm-container-pad-x-mobile: 16px;
}

.tm-container {
    width: 100%;
    max-width: var(--tm-container-max);
    margin-inline: auto;
    padding-inline: var(--tm-container-pad-x-desktop);
}

@media (max-width: 1024px) {
    .tm-container {
        padding-inline: var(--tm-container-pad-x-tablet);
    }
}

@media (max-width: 768px) {
    .tm-container {
        padding-inline: var(--tm-container-pad-x-mobile);
    }
}
```

---

## 13. Grid system

- **Desktop (≥1200px):** 12 колонок, gap 24px (или 32px по согласованию); выравнивание строго по колонкам.
- **Laptop (1024–1199px):** те же 12 колонок с возможным уменьшением gap до 24px.
- **Tablet (768–1023px):** 8 колонок или 12 с крупнее-минимальными ячейками; не сжимать touch-targets ниже стандартов раздела 27.
- **Mobile (≤767px):** 4 колонки / одна колонка контента; второстепенное уходит под основной поток.
- **Ultra-small (≤360px):** одна колонка; уменьшать **паддинги**, а не ломать законы типографики; при необходимости уменьшать `font-size` **ступенями в px** через медиазапросы.

```css
.tm-grid-12 {
    display: grid;
    grid-template-columns: repeat(12, minmax(0, 1fr));
    gap: 24px;
}

@media (max-width: 1024px) {
    .tm-grid-12 {
        gap: 20px;
    }
}

@media (max-width: 768px) {
    .tm-grid-12 {
        grid-template-columns: 1fr;
        gap: 16px;
    }
}
```

---

## 14. Section spacing system

Вертикальный ритм секций — **в `px`**, кратно **8px** (база 8).

Рекомендуемые ступени:

| Зона | Desktop | Tablet | Mobile |
|------|---------|--------|--------|
| Padding-block секции | 96px | 72px | 56px |
| Разрыв между крупными подблоками | 64px | 48px | 40px |

```css
.section {
    padding-block: 96px;
}

@media (max-width: 1024px) {
    .section {
        padding-block: 72px;
    }
}

@media (max-width: 768px) {
    .section {
        padding-block: 56px;
    }
}
```

---

## 15. Block spacing system

Внутри секций:

- Между заголовком секции и контентом: **24px–32px** (desktop 32px, mobile 24px).
- Между абзацами: **16px**.
- Между элементами формы: **16px** (поле + ошибка — см. раздел 18).

```css
.section__header {
    margin-bottom: 32px;
}

@media (max-width: 768px) {
    .section__header {
        margin-bottom: 24px;
    }
}

.section__body p + p {
    margin-top: 16px;
}
```

---

## 16. Card system

- Фон: `--tm-white` на светлой секции или `--tm-surface-2` на тёмной.
- Обводка: `1px solid var(--tm-border-on-light)` или `var(--tm-border-on-dark)`.
- **Без скруглений.** Тень — только если пройден чеклист раздела 30.

```css
.card {
    background: var(--tm-white);
    color: var(--tm-text-on-light);
    border: 1px solid var(--tm-border-on-light);
    border-radius: 0;
    padding: 24px;
}

.card__title {
    font-family: 'Montserrat', Arial, sans-serif;
    font-size: 18px;
    font-weight: 500;
    line-height: 1;
    letter-spacing: 0;
    margin: 0 0 16px;
}
```

---

## 17. Button system

**Закон:** высота **40px** (фиксированная или `min-height` + выравнивание иконки). Типографика кнопки: Montserrat, **500**, `line-height: 1`, `letter-spacing: 0`, `border-radius: 0`.

```css
.tm-button {
    box-sizing: border-box;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    min-height: 40px;
    padding: 0 20px;
    border-radius: 0;
    border: 1px solid transparent;
    font-family: 'Montserrat', Arial, sans-serif;
    font-size: 14px;
    font-weight: 500;
    line-height: 1;
    letter-spacing: 0;
    text-transform: none; /* по умолчанию; uppercase только если явно в ТЗ секции */
    cursor: pointer;
}

.tm-button--primary {
    color: var(--tm-white);
    background: linear-gradient(135deg, #f01832 0%, #d5001c 100%);
}

.tm-button--outline {
    color: var(--tm-accent);
    background: transparent;
    border-color: var(--tm-accent);
}
```

---

## 18. Form system

- Высота полей **40px**, `border-radius: 0`.
- Шрифт поля: Roboto 400, 16px, `line-height: calc(16px + 4px)`.
- Обводка: `1px solid var(--tm-border-on-light)` на светлом; на тёмном — `var(--tm-border-on-dark)`.
- Фокус: видимое кольцо **без** «свечения стартапа» — контрастное, прямоугольное.

```css
.tm-input {
    box-sizing: border-box;
    height: 40px;
    width: 100%;
    padding: 0 12px;
    border-radius: 0;
    border: 1px solid var(--tm-border-on-light);
    font-family: 'Roboto', Arial, sans-serif;
    font-size: 16px;
    font-weight: 400;
    line-height: calc(16px + 4px);
    letter-spacing: 0;
    color: var(--tm-text-on-light);
    background: var(--tm-white);
}

.tm-input:focus-visible {
    outline: 2px solid var(--tm-accent);
    outline-offset: 0;
}
```

---

## 19. Icon system

- **Единственный разрешённый набор глифов:** **Font Awesome Pro 5.15.4** из репозитория: `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/` (подключение — по решению сборки: CSS+webfont или спрайт; принцип неизменен: **источник глифа — FA Pro 5.15.4**).
- AI **не** генерирует SVG-иконки «с нуля» и **не** импортирует случайные наборы.
- Выравнивание: иконка в кнопке/строке — `inline-flex` + `align-items: center`, отступ **8px** между иконкой и текстом unless плотная таблица (тогда 6px, но фиксированно в рамках компонента).

---

## 20. Font Awesome rules

**Governance:** reusable selection discipline is documented in [`../notes/icon-source-policy.md`](../notes/icon-source-policy.md) and [`../../mars-website-factory/font-awesome-governance-layer.md`](../../mars-website-factory/font-awesome-governance-layer.md). For V2 rebuilds, icon choice is governed by **semantic fidelity first**, then family consistency and optical rhythm.

**Иерархия стилей FA5**

| Префикс / класс | Когда использовать |
|-----------------|-------------------|
| `fal` | Предпочтительно для технических / информационных маркетинговых иконок среднего и крупного размера: trust strip, спецификации, feature rows — если контраст достаточен. |
| `far` | Дополнительный UI и компактные affordance-иконки, где `fal` слишком тонкий, а `fas` слишком тяжёлый. |
| `fas` | Малый / плотный функциональный UI: FAQ plus/minus, check bullets, phone/CTA support, stats; не смешивать с `fal` в одной роли без причины. |
| `fab` | Только бренды (WhatsApp, Telegram, и т.д.). |

**Размеры (все в `px`)**

| Контекст | Размер |
|----------|--------|
| В строке с body 16px | 16px |
| В кнопке 14–16px | 16px |
| Заголовок / промо | 24px |
| Крупный акцент (герой) | 32px (не выше без human-approved) |

```html
<button class="tm-button tm-button--primary" type="button">
    <i class="fas fa-phone" style="font-size: 16px" aria-hidden="true"></i>
    <span>Заказать звонок</span>
</button>
```

```css
.tm-icon--16 {
    width: 16px;
    height: 16px;
    font-size: 16px;
    line-height: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}
```

**Рамки / кольца вокруг иконки:** только прямоугольник или квадрат с `border: 1px solid …`, `border-radius: 0`. Круглые иконки-«пилюли» запрещены.

**Цвет иконки:** `currentColor` по умолчанию; на красной кнопке — `color: var(--tm-white)`; на светлом фоне — `var(--tm-text-on-light)` или `var(--tm-accent)` для акцентных действий.

**Запрещено:** эмодзи как замена иконкам, случайные SVG с Behance/Dribbble, смешение версий FA (6+ с 5), outline от других библиотек.

---

## 21. Hero rules

- Полноширинный фон: фото + **строгий** линейный оверлей слева направо (см. раздел 34), без виньеток «кино».
- Заголовок: Montserrat 500, `line-height: 1`, `letter-spacing: 0`, допустим uppercae только если так в контент-гайде; акцентная строка — `color: var(--tm-accent)`.
- CTA: не более **одного** первичного и **одного** вторичного действия above the fold без согласования.
- Минимальная высота героя задаётся осмысленно (например `min-height: 600px` на desktop), но **не** через типографические костыли.

```css
.hero {
    position: relative;
    background: var(--tm-surface);
    color: var(--tm-text-on-dark);
    min-height: 600px;
    display: flex;
    flex-direction: column;
}

.hero__title {
    font-family: 'Montserrat', Arial, sans-serif;
    font-size: 48px;
    font-weight: 500;
    line-height: 1;
    letter-spacing: 0;
    margin: 0 0 24px;
}
```

---

## 22. CTA rules

- Первичный CTA — заливка/градиент красного диапазона (раздел 35), текст белый.
- Вторичный — outline `1px` accent, фон прозрачный.
- Все CTA высотой **40px**, без скруглений.
- Текст кнопки — короткий глагол + объект («Получить расчёт»), без кликбейта.

---

## 23. Trust block rules

- Светлый фон секции: `background: var(--tm-light-section)`, текст `var(--tm-text-on-light)`.
- Логотипы площадок отзывов — **только** утверждённые SVG/PNG из `projects/triumph-manipulator-landing/design/shared-assets/reviews/` (или обновлённого ассет-пакета), **без** перекраски брендов партнёров.
- Карточки преимуществ: прямоугольник, `border-radius: 0`, внутренние отступы **32px** desktop / **24px** mobile.
- Eyebrow: Montserrat 500, размер **12px** или **14px** только из шкалы; `letter-spacing: 0` (даже при `text-transform: uppercase`).

---

## 24. Equipment card rules

- Секция на белом/светлом: `background: var(--tm-white)` или блок на белом внутри светлой секции.
- Заголовок секции: Montserrat, крупные размеры из шкалы **в px**, `line-height: 1`, `letter-spacing: 0`.
- Подчёркивание-правило под заголовком: прямоугольная полоса **3px** высотой, ширина фиксирована (например `104px`), цвет — градиент красного диапазона или сплошной `var(--tm-accent)` — согласовать один вариант на всю страницу.

```css
.equipment-rule {
    width: 104px;
    height: 3px;
    border-radius: 0;
    background: linear-gradient(90deg, #f01832, #d5001c);
}
```

---

## 25. FAQ rules

- Вопрос: Montserrat 500, `line-height: 1`, размер **16–18px** (фиксировать один для проекта).
- Ответ: Roboto 400, 16px, `line-height: calc(16px + 4px)`.
- Разделитель между вопросами: `1px solid var(--tm-border-on-light)` на светлом или `var(--tm-border-on-dark)` на тёмном.
- Аккордеон без «пружинных» анимаций высоты > 200ms и без изменения трекинга при открытии.

---

## 26. Footer rules

- Фон: `var(--tm-surface-2)` или `var(--tm-surface)`.
- Текст: `var(--tm-text-on-dark-muted)` для вторичного, основной — `var(--tm-text-on-dark)`.
- Ссылки: подчёркивание **однообразно** (либо `text-decoration: underline`, либо только цвет — выбрать один стиль на проект).
- Иконки мессенджеров: **fab** + фирменные цвета раздела 5, размер **16px** или **20px** в ряд.

---

## 27. Mobile rules

- **Touch:** интерактив не уже **40px** по высоте (совпадает с кнопкой/полем).
- **Читаемость:** body не ниже **16px** на mobile.
- **Контейнер:** паддинги **16px**; не выносить критичный CTA ниже второго экрана без причины.
- **Навигация:** бургер — прямоугольная кнопка 40×40px, иконка `fas` из FA.
- **Ultra-small (≤360px):** не уменьшать шрифт ниже 12px для юридически значимого текста; для маркетинга минимум 14px unless иное утверждено.

---

## 28. Animation rules

- Допустимо: **короткие** (150–200ms) переходы `opacity`, `color`, `background-color`, `border-color`.
- Запрещено: чрезмерный `transform: scale`, «пружинные» easing для UI-контролов, параллакс ради декора.
- **Не** анимировать `letter-spacing`, `box-shadow` от неоновых значений.

```css
.tm-button {
    transition: background-color 0.15s ease, color 0.15s ease, border-color 0.15s ease;
}
```

---

## 29. Hover rules

- Кнопка primary: слегка темнее/светлее в пределах палитры акцента, **без** увеличения тени «ореолом».
- Ссылки: смена цвета на `var(--tm-accent)` или подчёркивание — один паттерн на весь сайт.
- **Запрещено:** hover, меняющий `letter-spacing`, `border-radius`, геометрию карточки.

```css
.tm-button--primary:hover {
    filter: brightness(1.05);
}

a:hover {
    color: var(--tm-accent);
}
```

---

## 30. Shadow rules

- По умолчанию **без теней** (плоский индустриальный вид).
- Если тень необходима для CTA на тёмном фоне — только: `box-shadow: 0 14px 30px rgba(227, 6, 33, 0.28);` (из токенов V1) и hover `0 18px 36px rgba(227, 6, 33, 0.36)` — **либо** отказаться полностью на новых версиях. Нельзя смешивать несколько несовместимых теневых языков.

```css
.tm-button--primary {
    box-shadow: 0 14px 30px rgba(227, 6, 33, 0.28);
}

.tm-button--primary:hover {
    box-shadow: 0 18px 36px rgba(227, 6, 33, 0.36);
}
```

---

## 31. Border rules

- Толщина: **1px** по умолчанию; акцентные разделители **2px** или **3px** только горизонтально.
- Цвет: строго из `--tm-border-on-light` / `--tm-border-on-dark`.
- **Никаких** полупрозрачных «светящихся» border на тёмном.

```css
.tm-divider {
    height: 1px;
    background: var(--tm-border-on-dark);
    border: 0;
}
```

---

## 32. Image rules

- `object-fit: cover` для фоновых фото; позиция по art-direction (например `object-position: 72% center` для героя) — фиксируется в задаче на секцию.
- Логотипы и бренды отзывов — без искажения пропорций, без лишних фильтров.
- Рамка вокруг изображения техники — `border: 1px solid var(--tm-border-on-light)`, `border-radius: 0`.

---

## 33. Background rules

- Основной фон страницы: `var(--tm-surface)`.
- Чередование секций: `surface` → `surface-2` → светлая (`light-section` / `white`) по смыслу, а не ради декора.
- **Запрещено:** «мягкие» пятна, размытые blob-backgrounds.

```css
.page {
    background: var(--tm-surface);
}
```

---

## 34. Overlay rules

- Линейный оверлей героя (пример направления из токенов V1, значения зафиксированы как ориентир):

```css
.hero__overlay {
    background: linear-gradient(
        90deg,
        rgba(5, 8, 15, 0.96) 0%,
        rgba(5, 8, 15, 0.88) 28%,
        rgba(5, 8, 15, 0.42) 58%,
        rgba(5, 8, 15, 0.12) 100%
    );
}
```

- Никаких радиальных «световых пятен» поверх фото.

---

## 35. Gradient rules

- Допустим **только** красный рабочий градиент для кнопок/акцентных полос: `linear-gradient(135deg, #f01832 0%, #d5001c 100%)`.
- Тёмный вертикальный градиент секции (опционально): `linear-gradient(180deg, #07111f 0%, #040914 100%)`.
- Запрещены: радужные, пастельные, «голографические» градиенты.

```css
.tm-gradient-accent {
    background: linear-gradient(135deg, #f01832 0%, #d5001c 100%);
}
```

---

## 36. AI frontend agent rules

1. Перед генерацией CSS — прочитать разделы **4–12, 17–18, 27, 38**.
2. Любой новый компонент: **0 radius**, **letter-spacing 0**, **`font-size` в px**, шрифты Roboto/Montserrat только.
3. Не добавлять библиотеки иконок; использовать FA Pro 5.15.4 из репозитория.
4. Не менять цветовые HEX без задачи от владельца бренда.
5. Каждый PR должен пройти **раздел 39** вручную или агентом-ревьюером.

---

## 37. AI design agent rules

1. Макеты должны быть **пиксельно дисциплинированы**: сетка 8px, без «случайных» отступов.
2. **Не** рисовать иконки руками — только плейсхолдеры из FA каталога (указать класс, например `fas fa-wrench`).
3. **Не** предлагать glass/blur/neumorphism — даже как «альтернатива».
4. Все тексты на макете — с реальными размерами в **px**, соответствующими шкале раздела 8.
5. Любой новый цвет → либо из раздела 5, либо отдельное согласование.

---

## 38. Strict prohibitions

- `border-radius` ≠ **0**.
- Glassmorphism / neumorphism / soft SaaS / generic startup look.
- `font-size` в **не-px** единицах.
- `letter-spacing` ≠ **0**.
- Любые иконки не из **Font Awesome Pro 5.15.4** (и самовольные SVG-иконки).
- Скруглённые «пилюли», липкие тултипы с тяжёлым blur, неоновые тени.
- Подключение шрифтов/ассетов с сомнительных CDN без ревью.

---

## 39. QA checklist

**Пиксели и сетка**

- [ ] Все отступы секций соответствуют разделу 14 (или задокументированному исключению в задаче).
- [ ] Контейнер: max-width и паддинги как в разделе 12.

**Типографика**

- [ ] Body: Roboto 400, размеры только **px**, `line-height: calc(font-size + 4px)`.
- [ ] Заголовки/кнопки: Montserrat 500, `line-height: 1`, `letter-spacing: 0`.

**Интервалы**

- [ ] Вертикальные ритмы кратны **8px** (кроме явно зафиксированных 4px для мелких делителей).

**Иконки**

- [ ] Только FA Pro 5.15.4; размеры в **px**; выравнивание `inline-flex`; отступ 8px до текста.
- [ ] Бренды мессенджеров — `fab` и фирменные цвета.

**Адаптив**

- [ ] Проверены **desktop, laptop, tablet, mobile, ultra-small** (разделы 13, 27).
- [ ] Нет горизонтального скролла из-за фиксированных ширин.

**Коммерческая консистентность**

- [ ] Палитра только из раздела 5 (+утверждённые логотипные исключения).
- [ ] Нет «игривых» шрифтов, иллюстраций-«человечков», стартап-UI.

---

## 40. Final implementation principles

1. **Один документ — один закон:** при конфликте макет ↔ этот файл → уточнение у человека; AI не «усредняет».
2. **Жёсткие края и индустриальность** важнее трендов UI.
3. **Минимум сюрпризов:** одинаковые кнопки, одинаковые поля, одинаковые карточки на всём лендинге.
4. **Доступность:** контраст текста к фону соблюдать относительно WCAG для ключевого контента (проверка внешним инструментом).
5. **Версионирование:** изменения в этот документ — только осознанным коммитом с указанием причины (продукт/бренд/юридические требования).

---

**Конец канона.**
