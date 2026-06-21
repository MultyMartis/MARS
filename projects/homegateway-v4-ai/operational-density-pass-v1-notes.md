# HomeGateway v4.ai — operational density pass v1 notes

**Статус:** DRAFT  
**Назначение:** зафиксировать, что именно было усилено в MVP v1 без редизайна shell и без ухода в декоративную стилизацию.

---

## 1. Что изменилось

- Усилен scale system для иконок:
  - utility controls приведены к более читаемому operational size;
  - sidebar navigation icons получили больший визуальный вес;
  - telemetry icons переведены из micro-mark состояния в рабочий tactical размер;
  - monitor/status icons выровнены под плотность правой колонки;
  - favorites icons сделаны немного тяжелее sidebar icon layer, но без доминирования.
- Telemetry indicators переведены из схемы `icon + tiny number` в компактные operational capsules.
- Topbar получил weight pass без роста высоты: активный tab стал лучше читаться, utility layer и profile block стали заметнее.
- Favorites слой получил более собранную кнопку, более явную иерархию icon/text/action и вторичный external action.
- Monitor cards, status module и left sidebar получили более плотную внутреннюю структуру и более читаемую иерархию.
- Усилен micro-contrast через opacity hierarchy существующей палитры без добавления новых цветов.

---

## 2. Density philosophy

Operational density в этом проходе трактуется не как “добавить больше элементов”, а как:

1. уменьшить ощущение визуальной пустоты;
2. поднять мгновенную читаемость рабочих сигналов;
3. перераспределить visual mass между topbar, left rail, favorites, monitor и status area;
4. сохранить calm tactical discipline без glow, blur, glassmorphism и ornamental FX.

Ключевой принцип: **сделать интерфейс плотнее, не делая его тяжелым или шумным**.

---

## 3. Tactical UI reasoning

- Topbar не должен расширяться по высоте: law `50px` сохранен, поэтому усиление сделано через underline, border contrast, selected surface и profile separation.
- Left sidebar не должен расширяться по ширине: law `370px` сохранен, поэтому баланс достигался через row readability, icon weight и telemetry grouping.
- Favorites остаются utility layer, а не primary dashboard strip: основной CTA — весь button surface, secondary CTA — только external action zone.
- Right sidebar должен ощущаться как operational awareness rail, а не как демонстрационный dashboard. Поэтому monitor и status blocks сделаны плотнее, но без “fake analytics” языка.

---

## 4. Telemetry readability logic

Telemetry capsules были собраны вокруг четырех требований:

- компактность;
- стабильная ширина;
- читаемость трехзначных значений;
- моментальное различение problem / active / completed semantics.

Принятые решения:

- fixed numeric rhythm через tabular numerals;
- capsule height и padding снижены до компактного tactical формата;
- сохранен `border-radius: 4px`;
- введена отдельная contrast hierarchy по типам telemetry, но только внутри существующей палитры;
- `0` у problems специально деградирует в muted state, чтобы не создавать ложную тревогу.

---

## 5. Hierarchy balancing decisions

### Topbar

Активный tab усилен, но не превращен в glowing primary CTA. Utility buttons и profile block получили собственную surface mass, чтобы topbar перестал быть визуально “тонкой линией”.

### Favorites

Favorites buttons стали плотнее и лучше читаются сканированием слева направо: icon -> text -> secondary external affordance.

### Monitor

Signal cards получили более собранную body/indicator композицию, чтобы карточки читались как operational units, а не как разреженные placeholders.

### Status module

A4 area подтянута к metrics через alignment, более ясный value anchor и менее декоративный chart language.

### Sidebar

List rows получили более устойчивую icon/text/telemetry связь. Это повышает scanability без изменения структуры и без роста panel width.

---

## 6. Non-goals preserved

- Не добавлялись новые цвета.
- Не добавлялись blur/fog/glass/giant shadows/neon glow.
- Не добавлялись uppercase и letter-spacing.
- Не менялась shell geometry.
- `#main_area` не трогался.
- Радиус оставлен в логике `4px`.

---

## 7. Проверка смысла прохода

Проход считается удачным, если интерфейс:

- стал читаться плотнее на первом взгляде;
- перестал выглядеть “слишком тонким”;
- не превратился в cinematic/cyberpunk concept;
- сохранил clean tactical operational character;
- не сломал ритм shell, control law и viewport discipline.
