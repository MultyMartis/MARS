'use strict';

const fs = require('fs');
const path = require('path');

const REGISTRY_PATH = path.join(__dirname, '../../src/data/static-demo/demo-page-registry.json');

const TASK_001_PLACEHOLDER_IDS = [
  'FP0002-DEMO-PG-032',
  'FP0002-DEMO-PG-033',
  'FP0002-DEMO-PG-037',
  'FP0002-DEMO-PG-038',
  'FP0002-DEMO-PG-039',
  'FP0002-DEMO-PG-040',
  'FP0002-DEMO-PG-041',
  'FP0002-DEMO-PG-042',
  'FP0002-DEMO-PG-043',
];

const TASK_002_PLACEHOLDER_IDS = [
  'FP0002-DEMO-PG-044',
  'FP0002-DEMO-PG-045',
  'FP0002-DEMO-PG-046',
  'FP0002-DEMO-PG-048',
];

function toPlaceholder(page, normalizationStatus) {
  page.template = 'PLACEHOLDER_PAGE';
  page.placeholder_message = 'Раздел скоро будет опубликован';
  page.eyebrow = null;
  page.normalization_status = normalizationStatus;
}

function main() {
  const registry = JSON.parse(fs.readFileSync(REGISTRY_PATH, 'utf8'));

  TASK_001_PLACEHOLDER_IDS.forEach((id) => {
    const page = registry.pages.find((p) => p.id === id);
    if (!page) {
      throw new Error(`Missing Task 001 page ${id}`);
    }
    toPlaceholder(page, 'OPERATOR_URGENT_TASK_001');
  });

  const pg033 = registry.pages.find((p) => p.id === 'FP0002-DEMO-PG-033');
  pg033.name = 'Эмоциональное выгорание';
  pg033.client_demo_name = 'Эмоциональное выгорание';
  pg033.h1 = 'Эмоциональное выгорание';
  pg033.title = 'Эмоциональное выгорание — Шпиговский Дом';
  const crumb033 = pg033.breadcrumbs.find((b) => b.current);
  if (crumb033) {
    crumb033.name = 'Эмоциональное выгорание';
  }

  const pg043 = registry.pages.find((p) => p.id === 'FP0002-DEMO-PG-043');
  pg043.name = 'Компульсивное переедание';
  pg043.client_demo_name = 'Компульсивное переедание';
  pg043.h1 = 'Компульсивное переедание';
  pg043.title = 'Компульсивное переедание — Шпиговский Дом';
  const crumb043 = pg043.breadcrumbs.find((b) => b.current);
  if (crumb043) {
    crumb043.name = 'Компульсивное переедание';
  }

  TASK_002_PLACEHOLDER_IDS.forEach((id) => {
    const page = registry.pages.find((p) => p.id === id);
    if (!page) {
      throw new Error(`Missing Task 002 page ${id}`);
    }
    toPlaceholder(page, 'OPERATOR_URGENT_TASK_002_CONVERTED_TO_PLACEHOLDER');
  });

  const pg048 = registry.pages.find((p) => p.id === 'FP0002-DEMO-PG-048');
  pg048.h1 = 'Лекарственная зависимость';
  pg048.title = 'Лекарственная зависимость — Шпиговский Дом';
  pg048.client_demo_name = 'Лекарственная зависимость';
  pg048.name = 'Лекарственная зависимость';
  const crumb048 = pg048.breadcrumbs.find((b) => b.current);
  if (crumb048) {
    crumb048.name = 'Лекарственная зависимость';
  }

  const pg003 = registry.pages.find((p) => p.id === 'FP0002-DEMO-PG-003');
  pg003.name = 'Зависимости';
  pg003.client_demo_name = 'Зависимости';
  pg003.template = 'PLACEHOLDER_PAGE';
  pg003.parent_id = 'FP0002-DEMO-PG-001';
  pg003.level = 1;
  pg003.menu = true;
  pg003.footer = false;
  pg003.url = '/zavisimosti/';
  pg003.output = 'zavisimosti/index.html';
  pg003.title = 'Зависимости — Шпиговский Дом';
  pg003.h1 = 'Зависимости';
  pg003.eyebrow = null;
  pg003.placeholder_message = 'Раздел скоро будет опубликован';
  pg003.breadcrumbs = [
    { name: 'Главная', url: '/', current: false },
    { name: 'Зависимости', url: '/zavisimosti/', current: true },
  ];
  pg003.normalization_status = 'OPERATOR_URGENT_TASK_003_RENAMED_FROM_GENOTIPIROVANIE';
  pg003.source.source_url = '/zavisimosti/';
  pg003.source.raw_url = 'https://shpigovsky.ru/zavisimosti/';

  const newPages = [
    {
      id: 'FP0002-DEMO-PG-057',
      source: {
        sheet: 'operator-urgent-v2',
        row: 1,
        raw_name: 'Профилактический анализ',
        raw_url: 'https://shpigovsky.ru/zavisimosti/genotipirovanie/profilakticheskiy-analiz/',
        source_url: '/zavisimosti/genotipirovanie/profilakticheskiy-analiz/',
      },
      name: 'Профилактический анализ',
      client_demo_name: 'Профилактический анализ',
      template: 'PLACEHOLDER_PAGE',
      parent_id: 'FP0002-DEMO-PG-003',
      level: 2,
      menu: false,
      footer: false,
      url: '/zavisimosti/genotipirovanie/profilakticheskiy-analiz/',
      output: 'zavisimosti/genotipirovanie/profilakticheskiy-analiz/index.html',
      title: 'Профилактический анализ — Шпиговский Дом',
      h1: 'Профилактический анализ',
      eyebrow: null,
      breadcrumbs: [
        { name: 'Главная', url: '/', current: false },
        { name: 'Зависимости', url: '/zavisimosti/', current: false },
        { name: 'Генотипирование', url: null, current: false },
        { name: 'Профилактический анализ', url: '/zavisimosti/genotipirovanie/profilakticheskiy-analiz/', current: true },
      ],
      placeholder_message: 'Раздел скоро будет опубликован',
      visibility: 'VISIBLE',
      normalization_status: 'OPERATOR_URGENT_TASK_001',
    },
    {
      id: 'FP0002-DEMO-PG-058',
      source: {
        sheet: 'operator-urgent-v2',
        row: 2,
        raw_name: 'Специалистам',
        raw_url: 'https://shpigovsky.ru/zavisimosti/genotipirovanie/specialistam/',
        source_url: '/zavisimosti/genotipirovanie/specialistam/',
      },
      name: 'Специалистам',
      client_demo_name: 'Специалистам',
      template: 'PLACEHOLDER_PAGE',
      parent_id: 'FP0002-DEMO-PG-003',
      level: 2,
      menu: false,
      footer: false,
      url: '/zavisimosti/genotipirovanie/specialistam/',
      output: 'zavisimosti/genotipirovanie/specialistam/index.html',
      title: 'Специалистам — Шпиговский Дом',
      h1: 'Специалистам',
      eyebrow: null,
      breadcrumbs: [
        { name: 'Главная', url: '/', current: false },
        { name: 'Зависимости', url: '/zavisimosti/', current: false },
        { name: 'Генотипирование', url: null, current: false },
        { name: 'Специалистам', url: '/zavisimosti/genotipirovanie/specialistam/', current: true },
      ],
      placeholder_message: 'Раздел скоро будет опубликован',
      visibility: 'VISIBLE',
      normalization_status: 'OPERATOR_URGENT_TASK_001',
    },
  ];

  registry.pages.push(...newPages);
  registry.meta.page_count = registry.pages.length;
  registry.meta.version = 'urgent-v2';
  registry.meta.operator_urgent_v2 = true;

  fs.writeFileSync(REGISTRY_PATH, `${JSON.stringify(registry, null, 2)}\n`, 'utf8');
  console.log(`Updated registry: ${registry.pages.length} pages`);
}

if (require.main === module) {
  main();
}

module.exports = { main };
