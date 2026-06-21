#!/usr/bin/env node
import { readFileSync, existsSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const V1 = join(dirname(fileURLToPath(import.meta.url)), '../../../workspaces/homegateway-v4-ai/v1');
const html = readFileSync(join(V1, 'dist/index.html'), 'utf8');
const css = readFileSync(join(V1, 'dist/assets/css/main.css'), 'utf8');

const checks = {
  distExists: existsSync(join(V1, 'dist/index.html')),
  viewportStage: html.includes('hg-viewport-stage'),
  deviceShell: html.includes('hg-device-shell'),
  noLogoTag: !html.includes('hg-logo__tag'),
  exo2Head: html.includes('Exo+2'),
  mainAreaPresent: html.includes('id="main_area"'),
  mainAreaPlaceholder: html.includes('#main_area'),
  russianOk: html.includes('Проекты') && html.includes('Перейти к рабочей области'),
  mojibake: /Р[Ѐ-Я]/.test(html),
  cssViewport: css.includes('.hg-viewport-stage') && css.includes('.hg-device-shell'),
  cssMaxWidth: css.includes('1920px'),
  cssMinHeight: css.includes('900px'),
  cssMaxHeight: css.includes('1080px'),
  cssExo2: css.includes("'Exo 2'"),
  cssFont18: css.includes('18px'),
  cssFont24: css.includes('24px'),
  cssFont20: css.includes('20px'),
  cssFont14: css.includes('14px'),
};

console.log(JSON.stringify(checks, null, 2));
const failed = Object.entries(checks).filter(([, v]) => !v);
if (failed.length) {
  console.error('FAILED:', failed.map(([k]) => k).join(', '));
  process.exit(1);
}
