import fs from 'fs';
import path from 'path';

const root = process.argv[2] || path.resolve('workspaces/homegateway-v4-ai/v1');

function w(rel, content) {
  const p = path.join(root, rel);
  fs.mkdirSync(path.dirname(p), { recursive: true });
  fs.writeFileSync(p, content, 'utf8');
  console.log('wrote', rel);
}

w(
  'src/scss/components/_icons.scss',
  `@use '../base/variables' as *;

.hg-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  font-style: normal;
}

.hg-icon--nav {
  font-size: 14px;
  color: rgba(0, 189, 240, 0.85);
}

.hg-icon--telemetry {
  font-size: 11px;
  color: $hg-color-text-dim;
  width: 12px;
}

.hg-icon--signal {
  font-size: 18px;
  margin-bottom: $hg-gap-micro;
}

.hg-signal--A1 .hg-icon--signal { color: $hg-color-brand; }
.hg-signal--A2 .hg-icon--signal { color: $hg-color-text-muted; }
.hg-signal--A3 .hg-icon--signal { color: $hg-color-info; }

.hg-icon--metric {
  font-size: 10px;
  color: rgba(0, 189, 240, 0.65);
}

.hg-icon--status-a4 {
  font-size: 16px;
  color: $hg-color-positive;
}
`
);

w(
  'src/scss/components/_telemetry.scss',
  `@use '../base/variables' as *;

.hg-telemetry {
  display: flex;
  align-items: center;
  gap: $hg-gap-micro;
  flex: 0 0 auto;
}

.hg-telemetry__item {
  display: inline-flex;
  align-items: center;
  gap: 3px;
  min-width: 0;
  padding: 0 2px;
  border: 1px solid transparent;
  border-radius: $hg-radius;
  line-height: 1;
}

.hg-telemetry__value {
  font-family: $hg-font-sans;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  font-variant-numeric: tabular-nums;
  color: $hg-color-text-muted;
  min-width: 1ch;
  max-width: 3ch;
  overflow: hidden;
  text-overflow: ellipsis;
  text-align: right;
}

.hg-telemetry__item--problems .hg-telemetry__value:not(:empty) {
  color: $hg-color-brand;
}

.hg-telemetry__item--problems[data-telemetry-value='0'] .hg-telemetry__value,
.hg-telemetry__item--problems .hg-telemetry__value:empty {
  color: $hg-color-text-dim;
}

.hg-telemetry__item--completed-tasks .hg-icon--telemetry {
  color: rgba(0, 191, 2, 0.55);
}

.hg-telemetry__item--completed-tasks .hg-telemetry__value {
  color: rgba(0, 191, 2, 0.75);
}
`
);

// Patch main.scss
const mainScssPath = path.join(root, 'src/scss/main.scss');
let mainScss = fs.readFileSync(mainScssPath, 'utf8');
if (!mainScss.includes('_icons.scss')) {
  mainScss = mainScss.replace(
    "@use 'components/buttons';",
    "@use 'components/icons';\n@use 'components/telemetry';\n@use 'components/buttons';"
  );
  fs.writeFileSync(mainScssPath, mainScss, 'utf8');
  console.log('patched main.scss');
}

// Read and patch existing scss files via full writes for list-row, topbar, buttons, signal, status, favorites
const listRowScss = `@use '../base/variables' as *;
@use '../utilities/interaction-states' as state;

.hg-list {
  display: flex;
  flex-direction: column;
  gap: $hg-gap-micro;
}

.hg-list__row {
  display: grid;
  grid-template-columns: 20px 1fr auto;
  align-items: center;
  gap: $hg-gap-compact;
  width: 100%;
  min-height: $hg-height-list-row;
  padding: 0 $hg-gap-compact;
  border-radius: $hg-radius;
  color: inherit;
  font-family: $hg-font-sans;
  text-align: left;
  cursor: pointer;
  @include state.hg-state-row;
}

.hg-list__icon {
  width: 20px;
  height: 20px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  background: transparent;
}

.hg-list__title {
  font-family: $hg-font-sans;
  font-size: $hg-font-size-list-title;
  font-weight: $hg-font-weight-list-title;
  line-height: 1.2;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
`;
w('src/scss/components/_list-row.scss', listRowScss);

const topbarPatch = fs.readFileSync(path.join(root, 'src/scss/layout/_topbar.scss'), 'utf8');
const newTopbar = topbarPatch
  .replace(/\.hg-theme-switch[\s\S]*?\.hg-theme-switch__label[\s\S]*?\}\n\n/, '')
  .replace(
    /\.hg-utility-btn \{[\s\S]*?\}\n\n/,
    `.hg-utility-btn {
  height: $hg-height-control;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 0 $hg-gap-medium;
  border-radius: $hg-radius;
  color: $hg-utility-text;
  font-family: $hg-font-sans;
  font-size: $hg-font-size-base;
  font-weight: $hg-font-weight-base;
  cursor: pointer;
  @include state.hg-state-surface($hg-utility-border);

  &:hover:not(:disabled) {
    color: $hg-color-text-muted;
    border-color: $hg-border-subtle;
    background: $hg-surface-hover;
  }
}

.hg-utility-btn--icon {
  width: $hg-height-control;
  min-width: $hg-height-control;
  padding: 0;
}

.hg-utility-btn--icon .hg-icon {
  font-size: 18px;
}

`
  );
fs.writeFileSync(path.join(root, 'src/scss/layout/_topbar.scss'), newTopbar, 'utf8');
console.log('patched _topbar.scss');

const signalScss = `@use '../base/variables' as *;

.hg-signal {
  display: grid;
  grid-template-columns: 1fr 88px;
  gap: $hg-gap-compact;
  align-items: stretch;
  padding: $hg-gap-compact;
  border: 1px solid $hg-operational-border;
  border-radius: $hg-radius;
  background: $hg-operational-surface;
}

.hg-signal__body {
  display: flex;
  flex-direction: column;
  gap: $hg-gap-micro;
  min-width: 0;
}

.hg-signal__actions {
  margin-top: $hg-gap-micro;
  display: flex;
  align-items: center;
  gap: $hg-gap-compact;
}

.hg-signal__sep {
  color: $hg-color-text-dim;
  font-size: $hg-font-size-small;
}

.hg-indicator {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: $hg-gap-micro;
  padding: $hg-gap-compact;
  border: 1px solid $hg-border-default;
  border-radius: $hg-radius;
  text-align: center;
  min-height: 64px;
}

.hg-indicator__label {
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  line-height: 1.2;
}

.hg-indicator--OK {
  border-color: rgba(0, 191, 2, 0.35);
  background: rgba(0, 191, 2, 0.08);
}

.hg-indicator--OK .hg-indicator__label { color: $hg-color-positive; }

.hg-indicator--WARN {
  border-color: rgba(209, 229, 255, 0.28);
  background: rgba(209, 229, 255, 0.05);
}

.hg-indicator--WARN .hg-indicator__label { color: $hg-color-text-muted; }

.hg-indicator--ALERT {
  border-color: rgba(255, 0, 0, 0.35);
  background: rgba(255, 0, 0, 0.08);
}

.hg-indicator--ALERT .hg-indicator__label { color: $hg-color-brand; }
`;
w('src/scss/components/_signal-card.scss', signalScss);

const statusScss = `@use '../base/variables' as *;

.hg-metrics__item {
  display: grid;
  grid-template-columns: 14px 1fr auto;
  gap: $hg-gap-compact;
  align-items: center;
  padding: $hg-gap-micro 0;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
}

.hg-metrics__icon {
  width: 14px;
  height: 14px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border: none;
  background: transparent;
}

.hg-metrics__label {
  color: $hg-color-text-muted;
}

.hg-metrics__value {
  font-family: $hg-font-sans;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  font-variant-numeric: tabular-nums;
  color: $hg-color-text;
}

.hg-status-module {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: $hg-gap-compact;
  border: 1px solid $hg-border-default;
  border-radius: $hg-radius;
  background: rgba(0, 189, 240, 0.03);
}

.hg-status-module__head {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: $hg-gap-micro;
}

.hg-status-module__label {
  font-family: $hg-font-sans;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  color: $hg-color-text-dim;
  text-align: center;
}

.hg-status-module__chart {
  display: flex;
  align-items: flex-end;
  gap: $hg-gap-micro;
  height: 48px;
  margin: $hg-gap-compact 0;
}

.hg-bar {
  width: 8px;
  height: var(--h, 50%);
  background: linear-gradient(180deg, $hg-color-info 0%, rgba(0, 189, 240, 0.2) 100%);
  border-radius: $hg-radius;
  opacity: 0.75;
}

.hg-status-module__caption {
  margin: 0;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-small;
  color: $hg-color-text-dim;
  text-align: center;
  line-height: 1.35;
}

.hg-status-module__value {
  font-family: $hg-font-sans;
  font-size: $hg-font-size-small;
  font-weight: $hg-font-weight-list-title;
  font-variant-numeric: tabular-nums;
  color: $hg-color-positive;
}
`;
w('src/scss/components/_status-module.scss', statusScss);

const favoritesScss = `@use '../base/variables' as *;
@use '../utilities/interaction-states' as state;

.hg-favorites {
  display: flex;
  align-items: center;
  gap: $hg-gap-compact;
  min-height: $hg-height-favorites;
  padding: $hg-gap-compact 0;
}

.hg-favorites__track {
  display: flex;
  flex: 1;
  gap: $hg-gap-compact;
  min-width: 0;
  overflow-x: auto;
}

.hg-fav-btn {
  display: inline-grid;
  grid-template-columns: auto 1fr auto;
  align-items: center;
  gap: $hg-gap-compact;
  min-width: 96px;
  height: $hg-height-control;
  padding: 0 $hg-gap-medium;
  border-radius: $hg-radius;
  color: $hg-utility-text;
  text-decoration: none;
  font-size: $hg-font-size-base;
  font-weight: $hg-font-weight-base;
  @include state.hg-state-surface($hg-utility-border);

  &:hover:not(:disabled) {
    color: $hg-color-text-muted;
    border-color: $hg-border-subtle;
    background: $hg-surface-hover;
  }

  &:hover .hg-fav-btn__action-zone {
    opacity: 1;
    visibility: visible;
  }
}

.hg-fav-btn__icon-zone {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 18px;
  flex: 0 0 auto;
}

.hg-fav-btn__icon-placeholder {
  font-size: 12px;
  opacity: 0.55;
}

.hg-fav-btn__text-zone {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.hg-fav-btn__action-zone {
  display: inline-flex;
  align-items: center;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.12s ease;
}

.hg-fav-btn__external {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  color: $hg-color-text-dim;
  font-size: 11px;
}

.hg-favorites__slide {
  flex: 0 0 auto;
  width: 40px;
  height: $hg-height-control;
  border-radius: $hg-radius;
  color: $hg-utility-text;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  @include state.hg-state-surface($hg-utility-border);

  &:hover:not(:disabled) {
    color: $hg-color-text-muted;
    border-color: $hg-border-subtle;
    background: $hg-surface-hover;
  }
}

.hg-favorites__slide--icon .hg-icon {
  font-size: 14px;
  opacity: 0.65;
}
`;
w('src/scss/sections/_favorites.scss', favoritesScss);

console.log('SCSS applied to', root);
