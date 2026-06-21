#!/usr/bin/env node
/**
 * One-off: V6 commercial copy correction pass (routes/partials only).
 */
import { readFileSync, writeFileSync, readdirSync, statSync } from 'node:fs';
import { join, relative } from 'node:path';

const ROOT = join(import.meta.dirname, '..', 'src');
const changed = [];

function walk(dir, acc = []) {
  for (const name of readdirSync(dir)) {
    const p = join(dir, name);
    if (statSync(p).isDirectory()) walk(p, acc);
    else if (p.endsWith('.html')) acc.push(p);
  }
  return acc;
}

const SITE_FORM_LEAD =
  'Оставьте заявку. Перезвоним и&nbsp;уточним: тип груза &middot; адрес подачи &middot; соориентируем по&nbsp;стоимости';

const HERO_FORM_NOTE =
  'Перезвоним и&nbsp;уточним: тип груза &middot; адрес подачи &middot; соориентируем по&nbsp;стоимости';

const EYEBROW_LINE = /\s*<p class="machine-transport__eyebrow">Диспетчерская подача<\/p>\n/g;

function applyCopy(text) {
  let out = text;

  // Task 2 — eyebrow
  out = out.replace(EYEBROW_LINE, '\n');

  // Task 3 — body size (multiple formats)
  out = out.replace(/6\.2\s*[×x]\s*2\.2&nbsp;м/g, '6.0 × 2.45&nbsp;м');
  out = out.replace(/6\.2&nbsp;×&nbsp;2\.2&nbsp;м/g, '6.0&nbsp;×&nbsp;2.45&nbsp;м');
  out = out.replace(/Кузов\s*-\s*6\.0 × 2\.45&nbsp;м/g, 'Кузов — 6.0 × 2.45&nbsp;м');

  // Task 4 & 5 — dedicated form texts
  out = out.replace(
    /<p class="site-form__lead">[\s\S]*?<\/p>/g,
    `<p class="site-form__lead">${SITE_FORM_LEAD}</p>`
  );
  out = out.replace(
    /<p class="hero-form__note">[\s\S]*?<\/p>/g,
    `<p class="hero-form__note">${HERO_FORM_NOTE}</p>`
  );

  // Task 1 — orientational pricing wording (not form lead/note — already replaced)
  const pricingReplacements = [
    [/ориентировочную&nbsp;стоимость&nbsp;доставки/g, 'точный&nbsp;расчёт&nbsp;стоимости&nbsp;доставки'],
    [/ориентировочную&nbsp;стоимость&nbsp;перевозки/g, 'точный&nbsp;расчёт&nbsp;стоимости&nbsp;перевозки'],
    [/ориентировочную&nbsp;стоимость&nbsp;работы/g, 'точный&nbsp;расчёт&nbsp;стоимости&nbsp;работы'],
    [/ориентировочная&nbsp;стоимость&nbsp;работы/g, 'точный&nbsp;расчёт&nbsp;стоимости&nbsp;работы'],
    [/ориентировочную&nbsp;стоимость/g, 'точный&nbsp;расчёт&nbsp;стоимости'],
    [/ориентировочная&nbsp;стоимость/g, 'точный&nbsp;расчёт&nbsp;стоимости'],
    [/ориентировочную стоимость/g, 'точный расчёт стоимости'],
    [/ориентировочная стоимость/g, 'точный расчёт стоимости'],
    [/ориентировочный&nbsp;расчёт/g, 'точный&nbsp;расчёт&nbsp;стоимости'],
    [/ориентировочный расчёт/g, 'точный расчёт стоимости'],
    [/сколько примерно будет стоить/g, 'назовём точную цену'],
    [
      /Подходит ли машина, ориентировочная стоимость и/g,
      'Подходит ли машина, назовём точную цену и'
    ],
    [
      /Подтверждаем маршрут, схему работ, ориентировочную стоимость и/g,
      'Подтверждаем маршрут, схему работ, назовём точную цену и'
    ],
  ];

  for (const [re, rep] of pricingReplacements) {
    out = out.replace(re, rep);
  }

  return out;
}

for (const file of walk(ROOT)) {
  const before = readFileSync(file, 'utf8');
  const after = applyCopy(before);
  if (after !== before) {
    writeFileSync(file, after, 'utf8');
    changed.push(relative(join(import.meta.dirname, '..'), file));
  }
}

console.log(`Updated ${changed.length} file(s):`);
for (const f of changed.sort()) console.log(`  ${f}`);
