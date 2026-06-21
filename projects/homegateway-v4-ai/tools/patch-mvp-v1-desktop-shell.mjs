#!/usr/bin/env node
/**
 * HomeGateway v4.ai MVP v1 — desktop viewport shell + typography + logo tag removal
 */
import { writeFileSync, mkdirSync, readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const V1 = join(__dirname, '../../../workspaces/homegateway-v4-ai/v1');

function w(relPath, content) {
  const full = join(V1, relPath);
  mkdirSync(dirname(full), { recursive: true });
  writeFileSync(full, content.replace(/^\n/, ''), 'utf8');
}

w('src/scss/base/_variables.scss', `
// HomeGateway v4.ai MVP v1 — palette lock + typography tokens
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

$hg-font-sans: 'Exo 2', system-ui, -apple-system, sans-serif;
$hg-font-mono: 'Consolas', 'Cascadia Mono', monospace;

$hg-font-size-base: 18px;
$hg-font-weight-base: 400;
$hg-font-size-heading: 24px;
$hg-font-weight-heading: 500;
$hg-font-size-button: 20px;
$hg-font-weight-button: 500;
$hg-font-size-small: 14px;
$hg-font-weight-small: 400;

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

$hg-shell-max-w: 1920px;
$hg-shell-min-h: 900px;
$hg-shell-max-h: 1080px;

$hg-bp-2560: 2560px;
$hg-bp-1920: 1920px;
$hg-bp-1440: 1440px;
$hg-bp-1280: 1280px;
$hg-bp-1024: 1024px;
`);

w('src/scss/base/_reset.scss', `
@use 'variables' as *;

*, *::before, *::after { box-sizing: border-box; }

html, body {
  margin: 0;
  padding: 0;
  height: 100%;
}

html {
  overflow: hidden;
}

body.hg-app-body {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  min-height: 100dvh;
  overflow: hidden;
  font-family: $hg-font-sans;
  font-size: $hg-font-size-base;
  font-weight: $hg-font-weight-base;
  line-height: 1.45;
  color: $hg-color-text;
  background: $hg-color-bg;
  -webkit-font-smoothing: antialiased;
}

button, a { font: inherit; }

ul, ol { margin: 0; padding: 0; list-style: none; }

img { max-width: 100%; display: block; }
`);

w('src/scss/layout/_viewport-shell.scss', `
@use '../base/variables' as *;

.hg-viewport-stage {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  min-height: 0;
  padding: clamp($hg-space-2, 2vh, $hg-space-6) clamp($hg-space-2, 2vw, $hg-space-6);
  overflow: hidden;
}

.hg-device-shell {
  display: flex;
  flex-direction: column;
  width: min(100%, $hg-shell-max-w);
  max-width: $hg-shell-max-w;
  min-height: min($hg-shell-min-h, 100%);
  max-height: min($hg-shell-max-h, 100%);
  height: min($hg-shell-max-h, 100%);
  overflow: hidden;
}
`);

w('src/scss/layout/_app-grid.scss', `
@use '../base/variables' as *;

.hg-app {
  display: grid;
  grid-template-rows: $hg-topbar-h 1fr;
  flex: 1 1 auto;
  min-height: 0;
  height: 100%;
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
`);

w('src/scss/base/_typography.scss', `
@use 'variables' as *;

.hg-panel__title {
  margin: 0;
  font-size: $hg-font-size-heading;
  font-weight: $hg-font-weight-heading;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: $hg-color-text-muted;
}

.hg-signal__title {
  margin: 0 0 $hg-space-1;
  font-size: $hg-font-size-heading;
  font-weight: $hg-font-weight-heading;
}

.hg-signal__desc {
  margin: 0;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  color: $hg-color-text-muted;
}

.hg-link {
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
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
`);

// Patch main.scss import
const mainScssPath = join(V1, 'src/scss/main.scss');
let mainScss = readFileSync(mainScssPath, 'utf8');
if (!mainScss.includes('layout/viewport-shell')) {
  mainScss = mainScss.replace(
    "@use 'layout/app-grid';",
    "@use 'layout/viewport-shell';\n@use 'layout/app-grid';"
  );
  writeFileSync(mainScssPath, mainScss, 'utf8');
}

// Sidebars — remove logo tag styles
w('src/scss/layout/_sidebars.scss', `
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
  display: block;
  text-decoration: none;
  color: inherit;
  padding: $hg-space-2 0 $hg-space-3;
}

.hg-quick-link {
  width: 100%;
  text-align: left;
  padding: $hg-space-2 $hg-space-3;
  border: 1px dashed $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  background: transparent;
  color: $hg-color-text-muted;
  font-size: $hg-font-size-button;
  font-weight: $hg-font-weight-button;
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
`);

w('src/scss/layout/_topbar.scss', `
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
  font-size: $hg-font-size-button;
  font-weight: $hg-font-weight-button;
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
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
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
  font-size: $hg-font-size-button;
  font-weight: $hg-font-weight-button;
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
  font-size: $hg-font-size-button;
  font-weight: $hg-font-weight-button;
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
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  color: $hg-color-positive;
  letter-spacing: 0.04em;
}

.hg-profile__name {
  font-size: $hg-font-size-base;
  font-weight: $hg-font-weight-heading;
}

.hg-profile__avatar {
  width: 32px;
  height: 32px;
  display: grid;
  place-items: center;
  border: 1px solid $hg-color-border-muted;
  border-radius: $hg-radius-sm;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-heading;
  color: $hg-color-brand;
}
`);

w('src/scss/components/_buttons.scss', `
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
  font-size: $hg-font-size-button;
  font-weight: $hg-font-weight-button;
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
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  cursor: pointer;
  transition: border-color 0.15s, color 0.15s, background 0.15s;
}

.hg-favorites__slide:hover {
  border-color: $hg-color-brand;
  color: $hg-color-brand;
  background: rgba(255, 0, 0, 0.06);
}
`);

w('src/scss/layout/_main-area.scss', `
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
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  color: $hg-color-text-dim;
  letter-spacing: 0.06em;
}

.hg-main-area__hint {
  margin: 0;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  color: $hg-color-text-dim;
  max-width: 320px;
  text-align: center;
}
`);

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

console.log('patch-mvp-v1-desktop-shell: SCSS + shell HTML updated');

