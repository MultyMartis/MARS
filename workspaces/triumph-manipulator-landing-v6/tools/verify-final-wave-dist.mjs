import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const routes = [
  'index',
  '5-tonn',
  'bytovki',
  'konteynery',
  'oborudovanie',
  'fbs-zhbi',
  'armatura',
  'kirpich-bloki',
  'stroymaterialy',
  'vezdehod',
  'yurlic',
  'kray',
];

const ppcChecks = [
  ['contacts x1', (c) => (c.match(/id="contacts"/g) || []).length === 1],
  ['faq--split-cta', (c) => c.includes('faq--split-cta')],
  ['contact-cta--embedded', (c) => c.includes('contact-cta--embedded')],
  ['no hero__notice', (c) => !c.includes('hero__notice')],
  ['no mock', (c) => !c.includes('data-form-handler="mock"')],
  ['no api endpoint', (c) => !c.includes('backend/api/forms/send.php')],
  ['Что не перевозим', (c) => c.includes('Что не перевозим')],
  ['Частые вопросы', (c) => c.includes('Частые вопросы')],
  ['hero__cargo-action', (c) => c.includes('hero__cargo-action')],
  ['machine-showcase__spec-panel', (c) => c.includes('machine-showcase__spec-panel')],
  ['machine-transport--ops-grid', (c) => c.includes('machine-transport--ops-grid')],
  ['pricing-factors--system', (c) => c.includes('pricing-factors--system')],
  ['order-steps--process', (c) => c.includes('order-steps--process')],
  ['hero__shell', (c) => c.includes('hero__shell')],
  ['hero__lower', (c) => c.includes('hero__lower')],
];

let exit = 0;
for (const r of routes) {
  const file = path.join(root, 'dist', r === 'index' ? 'index.html' : `${r}.html`);
  if (!fs.existsSync(file)) {
    console.log(`MISSING ${r}`);
    exit = 1;
    continue;
  }
  const c = fs.readFileSync(file, 'utf8');
  if (r === 'index') {
    console.log(`PASS ${r} (dist exists)`);
    continue;
  }
  const fail = ppcChecks.filter(([, fn]) => !fn(c)).map(([n]) => n);
  console.log(`${fail.length ? 'FAIL' : 'PASS'} ${r}${fail.length ? ` [${fail.join(', ')}]` : ''}`);
  if (fail.length) exit = 1;
}
process.exit(exit);
