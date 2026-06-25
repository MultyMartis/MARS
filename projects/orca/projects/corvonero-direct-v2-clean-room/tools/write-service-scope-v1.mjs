#!/usr/bin/env node
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { SERVICE_SCOPE } from './service-scope-data.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const intakeDir = path.resolve(__dirname, '../intake');

const services = SERVICE_SCOPE.map((s) => ({
  service_id: s.id,
  canonical_name: s.name,
  family: s.family,
  operator_source: s.operator_source,
  business_description: 'Подтверждённая услуга оператора в scope первого запуска',
  likely_customer_problem: 'Зависит от конкретной поисковой фразы — см. phrase-to-service map',
  paid_deliverable: 'Почасовая работа специалиста 1С по договору (от 2 часов)',
  known_configurations: s.family === 'configurations' ? [s.name] : ['1С:УТ', '1С:УНФ', '1С:Розница', '1С:КА', '1С:БП'],
  geographic_limitations: 'Удалённо по НСО; выезд только Новосибирск',
  must_be_represented_in_semantic_research: s.must_represent,
  safe_unknown: ['точный SLA', 'гарантии результата', 'фиксированная стоимость проекта'],
}));

fs.writeFileSync(
  path.join(intakeDir, 'corvonero-direct-v2-service-scope-v1.json'),
  JSON.stringify({ schema_version: '1', registry_id: 'corvonero-direct-v2-service-scope-v1', service_count: services.length, services }, null, 2) + '\n'
);

const lines = [
  '# Corvonero Direct V2 — Service Scope v1',
  '',
  `**Services:** ${services.length}`,
  '',
  '| ID | Service | Family | Must represent |',
  '|----|---------|--------|----------------|',
  ...services.map((s) => `| ${s.service_id} | ${s.canonical_name} | ${s.family} | ${s.must_be_represented_in_semantic_research} |`),
  '',
  'Mapping to phrases is not a campaign group decision.',
];
fs.writeFileSync(path.join(intakeDir, 'CORVONERO-DIRECT-V2-SERVICE-SCOPE-v1.md'), lines.join('\n') + '\n');
console.log('Service scope written:', services.length);
