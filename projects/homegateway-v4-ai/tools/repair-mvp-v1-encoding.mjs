#!/usr/bin/env node
/**
 * HomeGateway v4.ai MVP v1 — UTF-8 encoding repair
 * Writes HTML partials with correct Cyrillic (avoids PowerShell 5.1 script encoding drift).
 */
import { writeFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const V1 = join(__dirname, '../../../workspaces/homegateway-v4-ai/v1');

function w(relPath, content) {
  const full = join(V1, relPath);
  mkdirSync(dirname(full), { recursive: true });
  writeFileSync(full, content.replace(/^\n/, ''), 'utf8');
}

w('src/partials/shell/head.html', `
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="HomeGateway v4.ai — operational cockpit MVP v1">
  <title>HomeGateway v4.ai — MVP v1</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Exo+2:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/main.css">
</head>
`);

w('src/partials/shell/scripts.html', `
  <script src="assets/js/hooks/theme.js" defer></script>
  <script src="assets/js/hooks/favorites.js" defer></script>
  <script src="assets/js/main.js" defer></script>
`);

w('src/pages/index.html', `
@@include("partials/shell/head.html")
<body class="hg-app-body" data-hg-version="v1">
  <a class="hg-skip-link" href="#main_area">Перейти к рабочей области</a>
  <div class="hg-viewport-stage" data-component="viewport-stage">
    <div class="hg-device-shell" data-component="device-shell">
      @@include("partials/sections/app-shell.html")
    </div>
  </div>
  @@include("partials/shell/scripts.html")
</body>
</html>
`);

w('src/partials/sections/app-shell.html', `
<div class="hg-app" data-component="app-shell">
  @@include("partials/sections/topbar.html")
  <div class="hg-app__workspace">
    @@include("partials/sections/left-sidebar.html")
    <div class="hg-app__center">
      @@include("partials/sections/favorites-row.html")
      @@include("partials/sections/main-area.html")
    </div>
    @@include("partials/sections/right-sidebar.html")
  </div>
</div>
`);

w('src/partials/sections/topbar.html', `
<header class="hg-topbar" data-component="topbar">
  <nav class="hg-topbar__nav" aria-label="Режимы интерфейса">
    <ul class="hg-topbar__tabs" role="tablist">
      <li role="presentation"><button type="button" class="hg-tab hg-tab--active" role="tab" aria-selected="true" data-hook="nav-tab" data-tab="general">Общий</button></li>
      <li role="presentation"><button type="button" class="hg-tab" role="tab" aria-selected="false" data-hook="nav-tab" data-tab="systems">Системы</button></li>
      <li role="presentation"><button type="button" class="hg-tab" role="tab" aria-selected="false" data-hook="nav-tab" data-tab="focus">Фокус</button></li>
      <li role="presentation"><button type="button" class="hg-tab" role="tab" aria-selected="false" data-hook="nav-tab" data-tab="signals">Сигналы</button></li>
    </ul>
  </nav>
  <div class="hg-topbar__utilities">
    <button type="button" class="hg-utility-btn" data-hook="utility" data-utility="01" aria-label="Утилита 01">01</button>
    <button type="button" class="hg-utility-btn" data-hook="utility" data-utility="02" aria-label="Утилита 02">02</button>
    <button type="button" class="hg-utility-btn" data-hook="utility" data-utility="03" aria-label="Утилита 03">03</button>
    <button type="button" class="hg-theme-switch" data-hook="theme-toggle" aria-label="Переключить тему">
      <span class="hg-theme-switch__track"><span class="hg-theme-switch__thumb"></span></span>
      <span class="hg-theme-switch__label">Тема</span>
    </button>
  </div>
  <div class="hg-topbar__profile hg-profile" data-component="profile">
    <div class="hg-profile__meta">
      <span class="hg-profile__status">Авторизован</span>
      <span class="hg-profile__name">Multy Martis</span>
    </div>
    <div class="hg-profile__avatar" aria-hidden="true">MM</div>
  </div>
</header>
`);

w('src/partials/sections/left-sidebar.html', `
<aside class="hg-sidebar hg-sidebar--left" data-component="sidebar-left">
  <div class="hg-sidebar__logo hg-logo">
    <a href="/" class="hg-logo__link">
      <img class="hg-logo__img" src="assets/img/logo/logo-dark.svg" width="200" height="38" alt="Hub Gateway">
    </a>
  </div>

  <section class="hg-panel hg-panel--projects" data-component="projects-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Проекты</h2>
      <div class="hg-panel__counters">
        @@include("partials/components/counter-pill.html", {"value":"9"})
        @@include("partials/components/counter-pill.html", {"value":"10"})
      </div>
    </header>
    <ul class="hg-list">
      @@include("partials/components/list-row.html", {"title":"Полигон [WSP]","count":"5","stars":"3","icon":"project"})
      @@include("partials/components/list-row.html", {"title":"Метакод [MCA]","count":"12","stars":"3","icon":"project"})
      @@include("partials/components/list-row.html", {"title":"Песочница","count":"999","stars":"3","icon":"project"})
    </ul>
  </section>

  <section class="hg-panel hg-panel--tools" data-component="tools-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Инструменты</h2>
    </header>
    <ul class="hg-list">
      @@include("partials/components/list-row.html", {"title":"Системы","count":"4","stars":"4","icon":"tool"})
      @@include("partials/components/list-row.html", {"title":"Процессы","count":"18","stars":"4","icon":"tool"})
      @@include("partials/components/list-row.html", {"title":"Роботы","count":"7","stars":"4","icon":"tool"})
      @@include("partials/components/list-row.html", {"title":"Вики","count":"124","stars":"4","icon":"tool"})
    </ul>
  </section>

  <section class="hg-panel hg-panel--quick" data-component="quick-access-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Быстрый доступ</h2>
    </header>
    <button type="button" class="hg-quick-link" data-hook="quick-access-open">Открыть список</button>
  </section>
</aside>
`);

w('src/partials/components/counter-pill.html', `
<span class="hg-counter" data-component="counter">@@value</span>
`);

w('src/partials/components/list-row.html', `
<li class="hg-list__item">
  <button type="button" class="hg-list__row" data-hook="list-row" data-icon="@@icon">
    <span class="hg-list__icon" aria-hidden="true"></span>
    <span class="hg-list__title">@@title</span>
    @@include("partials/components/counter-pill.html", {"value":"@@count"})
    <span class="hg-list__affordances" aria-hidden="true">
      <span class="hg-star"></span><span class="hg-star"></span><span class="hg-star"></span>
    </span>
  </button>
</li>
`);

w('src/partials/sections/favorites-row.html', `
<div class="hg-favorites" data-component="favorites-row">
  <div class="hg-favorites__track" data-hook="favorites-track">
    <a class="hg-fav-btn" href="https://yandex.ru" target="_blank" rel="noopener noreferrer" data-hook="fav-link">Яндекс</a>
    <a class="hg-fav-btn" href="https://google.com" target="_blank" rel="noopener noreferrer" data-hook="fav-link">Google</a>
    <a class="hg-fav-btn" href="https://youtube.com" target="_blank" rel="noopener noreferrer" data-hook="fav-link">YouTube</a>
    <a class="hg-fav-btn" href="https://mail.ru" target="_blank" rel="noopener noreferrer" data-hook="fav-link">Mail</a>
    <a class="hg-fav-btn" href="https://vk.com" target="_blank" rel="noopener noreferrer" data-hook="fav-link">VK</a>
  </div>
  <button type="button" class="hg-favorites__slide" data-hook="favorites-slide" aria-label="Сменить набор избранного (#01)">#01</button>
</div>
`);

w('src/partials/sections/main-area.html', `
<main id="main_area" class="hg-main-area" data-component="main-area" aria-label="Рабочая область">
  <div class="hg-main-area__canvas">
    <span class="hg-main-area__label">#main_area</span>
    <p class="hg-main-area__hint">Операционная зона — контент подключается динамически</p>
  </div>
</main>
`);

w('src/partials/sections/right-sidebar.html', `
<aside class="hg-sidebar hg-sidebar--right" data-component="sidebar-right">
  <section class="hg-panel hg-panel--monitor" data-component="monitor-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Монитор</h2>
    </header>
    <div class="hg-signals">
      @@include("partials/components/signal-card.html", {"type":"A1","title":"Название сигнала","desc":"Описание сигнала — операционный placeholder.","status":"OK","statusLabel":"В норме"})
      @@include("partials/components/signal-card.html", {"type":"A2","title":"Название уведомления","desc":"Описание уведомления — операционный placeholder.","status":"WARN","statusLabel":"Внимание"})
      @@include("partials/components/signal-card.html", {"type":"A3","title":"Название события","desc":"Описание события — операционный placeholder.","status":"ALERT","statusLabel":"Отклонение"})
    </div>
    <footer class="hg-panel__foot">
      <a href="#" class="hg-link" data-hook="monitor-log">Смотреть весь лог →</a>
    </footer>
  </section>

  <section class="hg-panel hg-panel--status" data-component="system-status-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Статус системы</h2>
    </header>
    <div class="hg-status-grid">
      <ul class="hg-metrics">
        @@include("partials/components/metric-row.html", {"label":"CPU узла","value":"23%","trend":"stable"})
        @@include("partials/components/metric-row.html", {"label":"Память","value":"61%","trend":"up"})
        @@include("partials/components/metric-row.html", {"label":"Сеть I/O","value":"412 Mb/s","trend":"stable"})
      </ul>
      <div class="hg-status-module hg-status-module--a4" data-indicator-type="A4">
        <span class="hg-status-module__label">A4</span>
        <div class="hg-status-module__chart" aria-hidden="true">
          <span class="hg-bar" style="--h:72%"></span>
          <span class="hg-bar" style="--h:48%"></span>
          <span class="hg-bar" style="--h:86%"></span>
          <span class="hg-bar" style="--h:35%"></span>
        </div>
        <p class="hg-status-module__caption">Агрегированный health-index</p>
        <span class="hg-status-module__value">0.94</span>
      </div>
    </div>
  </section>
</aside>
`);

w('src/partials/components/signal-card.html', `
<article class="hg-signal hg-signal--@@type" data-component="signal-card" data-signal-type="@@type">
  <div class="hg-signal__body">
    <h3 class="hg-signal__title">@@title</h3>
    <p class="hg-signal__desc">@@desc</p>
    <div class="hg-signal__actions">
      <a href="#" class="hg-link" data-hook="signal-detail">Подробнее</a>
      <span class="hg-signal__sep">/</span>
      <button type="button" class="hg-link hg-link--btn" data-hook="signal-dismiss">Удалить</button>
    </div>
  </div>
  <div class="hg-signal__indicator hg-indicator hg-indicator--@@status" data-indicator-type="@@type">
    <span class="hg-indicator__type">@@type</span>
    <span class="hg-indicator__label">@@statusLabel</span>
  </div>
</article>
`);

w('src/partials/components/metric-row.html', `
<li class="hg-metrics__item">
  <span class="hg-metrics__icon" aria-hidden="true"></span>
  <span class="hg-metrics__label">@@label</span>
  <span class="hg-metrics__value">@@value</span>
</li>
`);

w('README.md', `# HomeGateway v4.ai - MVP v1

Operational frontend skeleton (HTML / SCSS / JS / Gulp).

## Commands

\`\`\`bash
cd v1
npm install
npm run build
npm run watch
\`\`\`

Output: \`dist/index.html\`, \`dist/assets/css/main.css\`, \`dist/assets/js/\`.

## Layout source

\`projects/homegateway-v4-ai/design/v1/hg_shem-v1.png\` — layout map only (only schema file present in repo).

## Rules

- \`#main_area\` — empty operational workspace.
- Palette: \`#02091b\`, \`#d1e5ff\`, \`#ff0000\`, \`#00bf02\`, \`#00bdf0\`.
- v0 archive: \`../archive/v0/\`
`);

console.log('repair-mvp-v1-encoding: HTML partials written (UTF-8)');
