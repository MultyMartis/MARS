# HomeGateway v4.ai MVP v1 — file bootstrap (one-time generator)
# NOTE: On Windows PowerShell 5.1, Cyrillic in here-strings may corrupt on write.
# For UTF-8 HTML repair, use: node projects/homegateway-v4-ai/tools/repair-mvp-v1-encoding.mjs
$v1 = "C:\AI MARS\workspaces\homegateway-v4-ai\v1"

function W($path, $content) {
  $full = Join-Path $v1 $path
  $dir = Split-Path $full -Parent
  if ($dir -and !(Test-Path $dir)) { New-Item -ItemType Directory -Force -Path $dir | Out-Null }
  [System.IO.File]::WriteAllText($full, $content.TrimStart("`r", "`n"), [System.Text.UTF8Encoding]::new($false))
}

# --- HTML: shell ---
W "src/partials/shell/head.html" @'
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="HomeGateway v4.ai — operational cockpit MVP v1">
  <title>HomeGateway v4.ai — MVP v1</title>
  <link rel="stylesheet" href="assets/css/main.css">
</head>
'@

W "src/partials/shell/scripts.html" @'
  <script src="assets/js/hooks/theme.js" defer></script>
  <script src="assets/js/hooks/favorites.js" defer></script>
  <script src="assets/js/main.js" defer></script>
'@

W "src/pages/index.html" @'
@@include("partials/shell/head.html")
<body class="hg-app-body" data-hg-version="v1">
  <a class="hg-skip-link" href="#main_area">Перейти к рабочей области</a>
  @@include("partials/sections/app-shell.html")
  @@include("partials/shell/scripts.html")
</body>
</html>
'@

W "src/partials/sections/app-shell.html" @'
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
'@

# --- HTML: topbar ---
W "src/partials/sections/topbar.html" @'
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
'@

# --- HTML: left sidebar ---
W "src/partials/sections/left-sidebar.html" @'
<aside class="hg-sidebar hg-sidebar--left" data-component="sidebar-left">
  <div class="hg-sidebar__logo hg-logo">
    <a href="/" class="hg-logo__link">
      <img class="hg-logo__img" src="assets/img/logo/logo-dark.svg" width="200" height="38" alt="Hub Gateway">
      <span class="hg-logo__tag">project manager</span>
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
    <button type="button" class="hg-quick-link" data-hook="quick-access-open">открыть список</button>
  </section>
</aside>
'@

W "src/partials/components/counter-pill.html" @'
<span class="hg-counter" data-component="counter">@@value</span>
'@

W "src/partials/components/list-row.html" @'
<li class="hg-list__item">
  <button type="button" class="hg-list__row" data-hook="list-row" data-icon="@@icon">
    <span class="hg-list__icon" aria-hidden="true"></span>
    <span class="hg-list__title">@@title</span>
    @@include("partials/components/counter-pill.html", {"value":"@@count"})
    <span class="hg-list__affordances" aria-hidden="true">
      @@for (var i = 0; i < parseInt('@@stars', 10); i++) {<span class="hg-star"></span>}
    </span>
  </button>
</li>
'@

# gulp-file-include doesn't support @@for - fix list-row without loop
W "src/partials/components/list-row.html" @'
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
'@

# --- favorites ---
W "src/partials/sections/favorites-row.html" @'
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
'@

# --- main area ---
W "src/partials/sections/main-area.html" @'
<main id="main_area" class="hg-main-area" data-component="main-area" aria-label="Рабочая область">
  <div class="hg-main-area__canvas">
    <span class="hg-main-area__label">#main_area</span>
    <p class="hg-main-area__hint">Операционная зона — контент подключается динамически</p>
  </div>
</main>
'@

# --- right sidebar ---
W "src/partials/sections/right-sidebar.html" @'
<aside class="hg-sidebar hg-sidebar--right" data-component="sidebar-right">
  <section class="hg-panel hg-panel--monitor" data-component="monitor-block">
    <header class="hg-panel__head">
      <h2 class="hg-panel__title">Монитор</h2>
    </header>
    <div class="hg-signals">
      @@include("partials/components/signal-card.html", {"type":"A1","title":"Сигнал ядра","desc":"Контур primary-gateway отвечает в пределах SLA. Очередь синхронизации стабильна.","status":"OK","statusLabel":"В норме"})
      @@include("partials/components/signal-card.html", {"type":"A1","title":"Контур данных","desc":"Репликация каталога завершена. Дельта 0.02% — в допустимом коридоре.","status":"OK","statusLabel":"В норме"})
      @@include("partials/components/signal-card.html", {"type":"A2","title":"Планировщик задач","desc":"2 задания ожидают подтверждения оператора. Окно обслуживания T+14м.","status":"WARN","statusLabel":"Внимание"})
      @@include("partials/components/signal-card.html", {"type":"A3","title":"Внешний API-шлюз","desc":"Повышенная задержка upstream (p95 840ms). Рекомендуется проверка маршрута.","status":"ALERT","statusLabel":"Отклонение"})
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
'@

W "src/partials/components/signal-card.html" @'
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
'@

W "src/partials/components/metric-row.html" @'
<li class="hg-metrics__item">
  <span class="hg-metrics__icon" aria-hidden="true"></span>
  <span class="hg-metrics__label">@@label</span>
  <span class="hg-metrics__value">@@value</span>
</li>
'@

# --- SCSS ---
W "src/scss/main.scss" @'
@use 'base/reset';
@use 'base/typography';
@use 'utilities/helpers';
@use 'layout/app-grid';
@use 'layout/topbar';
@use 'layout/sidebars';
@use 'layout/main-area';
@use 'components/buttons';
@use 'components/counter';
@use 'components/panel';
@use 'components/list-row';
@use 'components/signal-card';
@use 'components/status-module';
@use 'sections/favorites';
'@

W "src/scss/base/_variables.scss" @'
// HomeGateway v4.ai MVP v1 — palette lock
$hg-color-bg: #02091b;
$hg-color-border: #d1e5ff;
$hg-color-brand: #ff0000;
$hg-color-positive: #00bf02;
$hg-color-info: #00bdf0;

$hg-color-bg-elevated: rgba(209, 229, 255, 0.04);
$hg-color-border-muted: rgba(209, 229, 255, 0.18);
$hg-color-text: #d1e5ff;
$hg-color-text-muted: rgba(209, 229, 255, 0.62);
$hg-color-text-dim: rgba(209, 229, 255, 0.38);

$hg-font-sans: 'Segoe UI', system-ui, -apple-system, sans-serif;
$hg-font-mono: 'Consolas', 'Cascadia Mono', monospace;

$hg-radius-sm: 2px;
$hg-radius-md: 4px;

$hg-space-1: 4px;
$hg-space-2: 8px;
$hg-space-3: 12px;
$hg-space-4: 16px;
$hg-space-5: 20px;
$hg-space-6: 24px;

$hg-topbar-h: 52px;
$hg-sidebar-left-w: 280px;
$hg-sidebar-right-w: 360px;
$hg-favorites-h: 44px;

$hg-bp-2560: 2560px;
$hg-bp-1920: 1920px;
$hg-bp-1440: 1440px;
$hg-bp-1280: 1280px;
$hg-bp-1024: 1024px;
'@

W "src/scss/base/_reset.scss" @'
@use 'variables' as *;

*, *::before, *::after { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}

body.hg-app-body {
  font-family: $hg-font-sans;
  font-size: 13px;
  line-height: 1.45;
  color: $hg-color-text;
  background: $hg-color-bg;
  -webkit-font-smoothing: antialiased;
}

button, a { font: inherit; }

ul, ol { margin: 0; padding: 0; list-style: none; }

img { max-width: 100%; display: block; }
'@

W "src/scss/base/_typography.scss" @'
@use 'variables' as *;

.hg-panel__title {
  margin: 0;
  font-size: 11px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: $hg-color-text-muted;
}

.hg-signal__title {
  margin: 0 0 $hg-space-1;
  font-size: 13px;
  font-weight: 600;
}

.hg-signal__desc {
  margin: 0;
  font-size: 12px;
  color: $hg-color-text-muted;
}

.hg-link {
  font-size: 11px;
  color: $hg-color-info;
  text-decoration: none;
}

.hg-link:hover { text-decoration: underline; }

.hg-link--btn {
  background: none;
  border: 0;
  padding: 0;
  cursor: pointer;
}
'@

W "src/scss/utilities/_helpers.scss" @'
@use '../base/variables' as *;

.hg-skip-link {
  position: absolute;
  left: -9999px;
  top: 0;
  z-index: 1000;
  padding: $hg-space-2 $hg-space-3;
  background: $hg-color-bg;
  color: $hg-color-text;
  border: 1px solid $hg-color-border;
}

.hg-skip-link:focus {
  left: $hg-space-3;
  top: $hg-space-3;
}
'@

W "src/scss/layout/_app-grid.scss" @'
@use '../base/variables' as *;

.hg-app {
  display: grid;
  grid-template-rows: $hg-topbar-h 1fr;
  min-height: 100vh;
  max-height: 100vh;
  overflow: hidden;
}

.hg-app__workspace {
  display: grid;
  grid-template-columns: $hg-sidebar-left-w 1fr $hg-sidebar-right-w;
  min-height: 0;
  overflow: hidden;
}

.hg-app__center {
  display: grid;
  grid-template-rows: $hg-favorites-h 1fr;
  min-width: 0;
  min-height: 0;
}

@media (max-width: $hg-bp-1440) {
  .hg-app__workspace {
    grid-template-columns: 248px 1fr 320px;
  }
}

@media (max-width: $hg-bp-1280) {
  .hg-app__workspace {
    grid-template-columns: 220px 1fr 280px;
  }
}

@media (max-width: $hg-bp-1024) {
  .hg-app__workspace {
    grid-template-columns: 200px 1fr 260px;
  }
}
'@

W "src/scss/layout/_topbar.scss" @'
@use '../base/variables' as *;

.hg-topbar {
  display: grid;
  grid-template-columns: 1fr auto auto;
  align-items: center;
  gap: $hg-space-5;
  padding: 0 $hg-space-5;
  border-bottom: 1px solid $hg-color-border-muted;
  background: rgba(2, 9, 27, 0.96);
}

.hg-topbar__tabs {
  display: flex;
  gap: $hg-space-1;
}

.hg-tab {
  padding: $hg-space-2 $hg-space-4;
  border: 1px solid transparent;
  border-radius: $hg-radius-sm;
  background: transparent;
  color: $hg-color-text-muted;
  cursor: pointer;
  transition: color 0.15s, border-color 0.15s, background 0.15s;
}

.hg-tab:hover {
  color: $hg-color-text;
  border-color: $hg-color-border-muted;
}

.hg-tab--active {
  color: $hg-color-text;
  border-color: $hg-color-border-muted;
  background: $hg-color-bg-elevated;
}

.hg-topbar__utilities {
  display: flex;
  align-items: center;
  gap: $hg-space-2;
}

.hg-utility-btn {
  min-width: 32px;
  height: 28px;
  padding: 0 $hg-space-2;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: transparent;
  color: $hg-color-text-muted;
  font-family: $hg-font-mono;
  font-size: 11px;
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s, background 0.15s;
}

.hg-utility-btn:hover {
  color: $hg-color-text;
  border-color: $hg-color-border;
  background: $hg-color-bg-elevated;
}

.hg-theme-switch {
  display: inline-flex;
  align-items: center;
  gap: $hg-space-2;
  padding: $hg-space-1 $hg-space-2;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: transparent;
  color: $hg-color-text-muted;
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s;
}

.hg-theme-switch:hover {
  color: $hg-color-text;
  border-color: $hg-color-border;
}

.hg-theme-switch__track {
  width: 28px;
  height: 14px;
  border: 1px solid $hg-color-border-muted;
  border-radius: 7px;
  position: relative;
}

.hg-theme-switch__thumb {
  position: absolute;
  top: 1px;
  left: 1px;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: $hg-color-info;
}

.hg-theme-switch__label {
  font-size: 11px;
}

.hg-topbar__profile {
  display: flex;
  align-items: center;
  gap: $hg-space-3;
}

.hg-profile__meta {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  text-align: right;
}

.hg-profile__status {
  font-size: 10px;
  color: $hg-color-positive;
  letter-spacing: 0.04em;
}

.hg-profile__name {
  font-size: 12px;
  font-weight: 600;
}

.hg-profile__avatar {
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  font-size: 10px;
  font-weight: 700;
  color: $hg-color-brand;
}
'@

W "src/scss/layout/_sidebars.scss" @'
@use '../base/variables' as *;

.hg-sidebar {
  display: flex;
  flex-direction: column;
  gap: $hg-space-3;
  padding: $hg-space-3;
  min-height: 0;
  overflow: auto;
}

.hg-sidebar--left {
  border-right: 1px solid $hg-color-border-muted;
}

.hg-sidebar--right {
  border-left: 1px solid $hg-color-border-muted;
}

.hg-logo__link {
  display: flex;
  flex-direction: column;
  gap: $hg-space-1;
  text-decoration: none;
  color: inherit;
  padding: $hg-space-2 0 $hg-space-3;
}

.hg-logo__tag {
  font-size: 10px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: $hg-color-text-dim;
}

.hg-quick-link {
  width: 100%;
  text-align: left;
  padding: $hg-space-2 $hg-space-3;
  border: 1px dashed $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: transparent;
  color: $hg-color-text-muted;
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s;
}

.hg-quick-link:hover {
  color: $hg-color-text;
  border-color: $hg-color-border;
}

.hg-status-grid {
  display: grid;
  grid-template-columns: 1fr 120px;
  gap: $hg-space-3;
  align-items: stretch;
}
'@

W "src/scss/layout/_main-area.scss" @'
@use '../base/variables' as *;

.hg-main-area {
  min-height: 0;
  padding: $hg-space-3;
  overflow: hidden;
}

.hg-main-area__canvas {
  position: relative;
  height: 100%;
  min-height: 200px;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-md;
  background:
    linear-gradient(180deg, rgba(209, 229, 255, 0.02) 0%, transparent 40%),
  $hg-color-bg;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: $hg-space-2;
}

.hg-main-area__canvas::before {
  content: '';
  position: absolute;
  inset: $hg-space-4;
  border: 1px dashed rgba(209, 229, 255, 0.08);
  border-radius: $hg-radius-sm;
  pointer-events: none;
}

.hg-main-area__label {
  font-family: $hg-font-mono;
  font-size: 11px;
  color: $hg-color-text-dim;
  letter-spacing: 0.06em;
}

.hg-main-area__hint {
  margin: 0;
  font-size: 12px;
  color: $hg-color-text-dim;
  max-width: 320px;
  text-align: center;
}
'@

W "src/scss/components/_buttons.scss" @'
@use '../base/variables' as *;

.hg-fav-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 96px;
  height: 32px;
  padding: 0 $hg-space-4;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: $hg-color-bg-elevated;
  color: $hg-color-text;
  text-decoration: none;
  font-size: 12px;
  transition: border-color 0.15s, background 0.15s, color 0.15s;
}

.hg-fav-btn:hover {
  border-color: $hg-color-border;
  background: rgba(209, 229, 255, 0.08);
  color: $hg-color-text;
}

.hg-favorites__slide {
  flex: 0 0 auto;
  width: 40px;
  height: 32px;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: transparent;
  color: $hg-color-text-muted;
  font-family: $hg-font-mono;
  font-size: 11px;
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s, background 0.15s;
}

.hg-favorites__slide:hover {
  border-color: $hg-color-brand;
  color: $hg-color-brand;
  background: rgba(255, 0, 0, 0.06);
}
'@

W "src/scss/components/_counter.scss" @'
@use '../base/variables' as *;

.hg-counter {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-width: 22px;
  height: 18px;
  padding: 0 5px;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: rgba(2, 9, 27, 0.8);
  font-family: $hg-font-mono;
  font-size: 10px;
  font-weight: 600;
  color: $hg-color-text;
  line-height: 1;
}
'@

W "src/scss/components/_panel.scss" @'
@use '../base/variables' as *;

.hg-panel {
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-md;
  background: $hg-color-bg-elevated;
  padding: $hg-space-3;
}

.hg-panel__head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: $hg-space-2;
  margin-bottom: $hg-space-3;
  padding-bottom: $hg-space-2;
  border-bottom: 1px solid $hg-color-border-muted;
}

.hg-panel__counters {
  display: flex;
  gap: $hg-space-1;
}

.hg-panel__foot {
  margin-top: $hg-space-3;
  padding-top: $hg-space-2;
  border-top: 1px solid $hg-color-border-muted;
}

.hg-panel--monitor {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  flex-direction: column;
}

.hg-signals {
  display: flex;
  flex-direction: column;
  gap: $hg-space-2;
  overflow: auto;
  min-height: 0;
}
'@

W "src/scss/components/_list-row.scss" @'
@use '../base/variables' as *;

.hg-list__row {
  display: grid;
  grid-template-columns: 20px 1fr auto auto;
  align-items: center;
  gap: $hg-space-2;
  width: 100%;
  padding: $hg-space-2;
  border: 1px solid transparent;
  border-radius: $hg-radius-sm;
  background: transparent;
  color: inherit;
  text-align: left;
  cursor: pointer;
  transition: border-color 0.15s, background 0.15s;
}

.hg-list__row:hover {
  border-color: $hg-color-border-muted;
  background: rgba(209, 229, 255, 0.04);
}

.hg-list__icon {
  width: 14px;
  height: 14px;
  border: 1px solid $hg-color-border-muted;
  clip-path: polygon(50% 0%, 100% 38%, 82% 100%, 18% 100%, 0% 38%);
  background: rgba(0, 189, 240, 0.15);
}

.hg-list__title {
  font-size: 12px;
  font-weight: 500;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.hg-list__affordances {
  display: flex;
  gap: 2px;
}

.hg-star {
  width: 6px;
  height: 6px;
  border: 1px solid $hg-color-text-dim;
  transform: rotate(45deg);
}
'@

W "src/scss/components/_signal-card.scss" @'
@use '../base/variables' as *;

.hg-signal {
  display: grid;
  grid-template-columns: 1fr 88px;
  gap: $hg-space-2;
  padding: $hg-space-2;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: rgba(2, 9, 27, 0.6);
}

.hg-signal__actions {
  margin-top: $hg-space-2;
  display: flex;
  align-items: center;
  gap: $hg-space-1;
}

.hg-signal__sep {
  color: $hg-color-text-dim;
  font-size: 10px;
}

.hg-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: $hg-space-1;
  padding: $hg-space-2;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  text-align: center;
  min-height: 64px;
}

.hg-indicator__type {
  font-family: $hg-font-mono;
  font-size: 10px;
  color: $hg-color-text-dim;
}

.hg-indicator__label {
  font-size: 10px;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}

.hg-indicator--OK {
  border-color: rgba(0, 191, 2, 0.35);
  background: rgba(0, 191, 2, 0.08);
}

.hg-indicator--OK .hg-indicator__label { color: $hg-color-positive; }

.hg-indicator--WARN {
  border-color: rgba(209, 229, 255, 0.35);
  background: rgba(209, 229, 255, 0.06);
}

.hg-indicator--WARN .hg-indicator__label { color: $hg-color-text; }

.hg-indicator--ALERT {
  border-color: rgba(255, 0, 0, 0.4);
  background: rgba(255, 0, 0, 0.08);
}

.hg-indicator--ALERT .hg-indicator__label { color: $hg-color-brand; }
'@

W "src/scss/components/_status-module.scss" @'
@use '../base/variables' as *;

.hg-metrics__item {
  display: grid;
  grid-template-columns: 12px 1fr auto;
  gap: $hg-space-2;
  align-items: center;
  padding: $hg-space-1 0;
  font-size: 11px;
}

.hg-metrics__icon {
  width: 8px;
  height: 8px;
  border: 1px solid $hg-color-info;
  transform: rotate(45deg);
  opacity: 0.7;
}

.hg-metrics__label {
  color: $hg-color-text-muted;
}

.hg-metrics__value {
  font-family: $hg-font-mono;
  font-size: 11px;
}

.hg-status-module {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: $hg-space-2;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: rgba(0, 189, 240, 0.04);
}

.hg-status-module__label {
  font-family: $hg-font-mono;
  font-size: 10px;
  color: $hg-color-text-dim;
}

.hg-status-module__chart {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 48px;
  margin: $hg-space-2 0;
}

.hg-bar {
  width: 8px;
  height: var(--h, 50%);
  background: linear-gradient(180deg, $hg-color-info 0%, rgba(0, 189, 240, 0.2) 100%);
  border-radius: 1px 1px 0 0;
  opacity: 0.85;
}

.hg-status-module__caption {
  margin: 0;
  font-size: 9px;
  color: $hg-color-text-dim;
  text-align: center;
}

.hg-status-module__value {
  font-family: $hg-font-mono;
  font-size: 14px;
  font-weight: 700;
  color: $hg-color-positive;
}
'@

W "src/scss/sections/_favorites.scss" @'
@use '../base/variables' as *;

.hg-favorites {
  display: flex;
  align-items: center;
  gap: $hg-space-3;
  padding: $hg-space-2 $hg-space-3;
  border-bottom: 1px solid $hg-color-border-muted;
  min-height: $hg-favorites-h;
}

.hg-favorites__track {
  display: flex;
  flex: 1;
  gap: $hg-space-2;
  min-width: 0;
  overflow-x: auto;
}
'@

# Fix main.scss @use paths - reset needs variables
W "src/scss/base/_reset.scss" @'
@use 'variables' as *;

*, *::before, *::after { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}

body.hg-app-body {
  font-family: $hg-font-sans;
  font-size: 13px;
  line-height: 1.45;
  color: $hg-color-text;
  background: $hg-color-bg;
  -webkit-font-smoothing: antialiased;
}

button, a { font: inherit; }

ul, ol { margin: 0; padding: 0; list-style: none; }

img { max-width: 100%; display: block; }
'@

W "src/scss/main.scss" @'
@use 'base/variables';
@use 'base/reset';
@use 'base/typography';
@use 'utilities/helpers';
@use 'layout/app-grid';
@use 'layout/topbar';
@use 'layout/sidebars';
@use 'layout/main-area';
@use 'components/buttons';
@use 'components/counter';
@use 'components/panel';
@use 'components/list-row';
@use 'components/signal-card';
@use 'components/status-module';
@use 'sections/favorites';
'@

# --- JS ---
W "src/js/hooks/theme.js" @'
(function () {
  'use strict';
  var toggle = document.querySelector('[data-hook="theme-toggle"]');
  if (!toggle) return;
  toggle.addEventListener('click', function () {
    document.body.classList.toggle('hg-theme-alt');
    toggle.setAttribute('aria-pressed', document.body.classList.contains('hg-theme-alt'));
  });
})();
'@

W "src/js/hooks/favorites.js" @'
(function () {
  'use strict';
  var slideBtn = document.querySelector('[data-hook="favorites-slide"]');
  var track = document.querySelector('[data-hook="favorites-track"]');
  if (!slideBtn || !track) return;
  slideBtn.addEventListener('click', function () {
    track.setAttribute('data-favorites-set', track.getAttribute('data-favorites-set') === '02' ? '01' : '02');
  });
})();
'@

W "src/js/main.js" @'
(function () {
  'use strict';

  document.querySelectorAll('[data-hook="nav-tab"]').forEach(function (tab) {
    tab.addEventListener('click', function () {
      document.querySelectorAll('[data-hook="nav-tab"]').forEach(function (t) {
        t.classList.remove('hg-tab--active');
        t.setAttribute('aria-selected', 'false');
      });
      tab.classList.add('hg-tab--active');
      tab.setAttribute('aria-selected', 'true');
    });
  });

  document.querySelectorAll('[data-hook="list-row"]').forEach(function (row) {
    row.addEventListener('click', function () {
      row.setAttribute('data-selected', row.getAttribute('data-selected') === 'true' ? 'false' : 'true');
    });
  });
})();
'@

# archive manifest
W "archive-manifest-v0.md" @'
# Archive v0 catalog

Moved from workspace root on MVP v1 initialization.

## Contents

- `src/` — Prototype v0.1 cockpit wireframe (cockpit views, overlays, signals rail)
- `dist/` — Last build output
- `gulpfile.js`, `package.json`, `package-lock.json`, `README.md`, `.gitignore`

## Note

`node_modules` remained at workspace root for reuse; run `npm install` inside `v1/` for v1 dependencies.
'@

Write-Host "Bootstrap complete"
