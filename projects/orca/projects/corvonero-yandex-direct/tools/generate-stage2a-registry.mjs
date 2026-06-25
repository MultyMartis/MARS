/**
 * Stage 2A ad-group registry generator — Corvonero full-service architecture.
 * Reads MIG keyword_registry.json; outputs ad-group-registry-v1.json.
 * Run: node tools/generate-stage2a-registry.mjs
 */
import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '..');
const MIG = path.resolve(
  ROOT,
  '../../../../incoming/mig/pilots/corvonero/session-mig-20260622-corv01/keyword_registry.json'
);

const kr = JSON.parse(fs.readFileSync(MIG, 'utf8'));

const NOISE_REJECT = [
  'job-seeking', 'training', 'salary', 'education', 'download', 'torrent',
  'crack', 'vacancy', 'resume', 'course', 'certification', 'student',
  'self-service', 'forum', 'documentation-only', 'regulatory-research',
];

function isCommercial(k) {
  if (k.intent_class === 'regulatory' && k.commercial_relevance !== 'high') return false;
  if (k.intent_class === 'informational') return false;
  const nc = k.noise_classes || [];
  const onlyNoise = nc.length > 0 && nc.every((n) =>
    ['job-seeking', 'training', 'salary', 'remote-work', 'informational'].includes(n)
  );
  if (onlyNoise && k.intent_class !== 'direct-commercial') return false;
  return (
    k.intent_class === 'direct-commercial' ||
    k.intent_class === 'troubleshooting' ||
    (k.intent_class === 'commercial-mixed' && k.commercial_relevance !== 'low')
  );
}

function pickKeywords(filterFn, limit = 12) {
  return kr.keywords
    .filter((k) => isCommercial(k) && filterFn(k))
    .slice(0, limit)
    .map((k) => ({
      keyword_id: k.keyword_id,
      phrase: k.source_phrase || k.normalized_phrase,
      evidence_ref: k.query_id || k.keyword_id,
    }));
}

const GROUPS = [
  // CORV-C01 — Общие услуги 1С
  { id: 'CORV-G01-01', campaign: 'CORV-C01', direction: 'general_1c', name: 'Услуги программиста 1С', intent: 'hire_outsource_1c_dev', landing: 'LP-01', url: '/uslugi-1c/', bid: 'T1', filter: (k) => k.cluster === 'A_broad_commercial' && /программист|услуги программиста/.test(k.normalized_phrase || '') && !/новосибирск|обучен|курс|зарплат|стажер|ваканс|резюме|с нуля/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-02', campaign: 'CORV-C01', direction: 'general_1c', name: 'Программист 1С Новосибирск', intent: 'local_1c_dev', landing: 'LP-01', url: '/uslugi-1c/', bid: 'T1', filter: (k) => /новосибирск/.test(k.normalized_phrase || '') && /программист/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-03', campaign: 'CORV-C01', direction: 'general_1c', name: 'Настройка 1С', intent: 'setup_1c', landing: 'LP-02', url: '/nastroyka-1c/', bid: 'T2', filter: (k) => k.cluster === 'A_broad_commercial' && /настройк/.test(k.normalized_phrase || '') && !/маркиров|интеграц|синхрон|обмен|отчет|печатн/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-04', campaign: 'CORV-C01', direction: 'general_1c', name: 'Внедрение 1С', intent: 'implementation_1c', landing: 'LP-03', url: '/vnedrenie-1c/', bid: 'T2', filter: (k) => /внедрен/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-05', campaign: 'CORV-C01', direction: 'general_1c', name: 'Сопровождение 1С', intent: 'support_retainer', landing: 'LP-04', url: '/soprovozhdenie-1c/', bid: 'T1', filter: (k) => k.cluster === 'A_support' && /сопровожден/.test(k.normalized_phrase || '') && !/абонент|обслужив/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-06', campaign: 'CORV-C01', direction: 'general_1c', name: 'Обслуживание 1С', intent: 'maintenance_1c', landing: 'LP-04', url: '/soprovozhdenie-1c/', bid: 'T2', filter: (k) => /обслуживан/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-07', campaign: 'CORV-C01', direction: 'general_1c', name: 'Абонентское сопровождение', intent: 'subscription_support', landing: 'LP-04', url: '/soprovozhdenie-1c/', bid: 'T2', filter: (k) => /абонент/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-08', campaign: 'CORV-C01', direction: 'general_1c', name: 'Разовые работы 1С', intent: 'one_off_1c', landing: 'LP-01', url: '/uslugi-1c/', bid: 'T2', filter: (k) => /разов/.test(k.normalized_phrase || '') },

  // CORV-C02 — Доработки
  { id: 'CORV-G02-01', campaign: 'CORV-C02', direction: 'modifications', name: 'Доработка 1С', intent: 'modification_general', landing: 'LP-05', url: '/dorabotka-1c/', bid: 'T1', filter: (k) => k.cluster === 'A_modification' && /^доработка 1с$|доработка 1с$|доработка 1с /.test(k.normalized_phrase || '') || (k.keyword_id === 'kw-corv01-004') },
  { id: 'CORV-G02-02', campaign: 'CORV-C02', direction: 'modifications', name: 'Доработка конфигурации 1С', intent: 'modification_config', landing: 'LP-05', url: '/dorabotka-1c/', bid: 'T2', filter: (k) => k.cluster === 'A_modification' && /конфигурац|расширен|модул/.test(k.normalized_phrase || '') },
  { id: 'CORV-G02-03', campaign: 'CORV-C02', direction: 'modifications', name: 'Доработка базы 1С', intent: 'modification_database', landing: 'LP-05', url: '/dorabotka-1c/', bid: 'T2', filter: (k) => k.cluster === 'A_modification' && /баз/.test(k.normalized_phrase || '') },
  { id: 'CORV-G02-04', campaign: 'CORV-C02', direction: 'modifications', name: 'Обновление доработанной 1С', intent: 'update_custom_base', landing: 'LP-06', url: '/obnovlenie-dorabotok-1c/', bid: 'T2', filter: (k) => k.cluster === 'A_support' && /обновлен.*доработ|доработ.*обновлен/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-013' },
  { id: 'CORV-G02-05', campaign: 'CORV-C02', direction: 'modifications', name: 'Перенос и сохранение доработок', intent: 'migration_customizations', landing: 'LP-06', url: '/obnovlenie-dorabotok-1c/', bid: 'T3', filter: (k) => /перенос.*доработ|сохранен.*доработ/.test(k.normalized_phrase || '') },
  { id: 'CORV-G02-06', campaign: 'CORV-C02', direction: 'modifications', name: 'Исправление доработок после обновления', intent: 'fix_after_update', landing: 'LP-06', url: '/obnovlenie-dorabotok-1c/', bid: 'T2', filter: (k) => /исправлен.*доработ|доработ.*после обнов/.test(k.normalized_phrase || '') },

  // CORV-C03 — Отчёты и формы
  { id: 'CORV-G03-01', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Доработка и настройка отчёта 1С', intent: 'report_customization', landing: 'LP-07', url: '/otchety-1c/', bid: 'T1', filter: (k) => (k.cluster === 'B_reports' || (k.cluster === 'A_modification' && /отчет/.test(k.normalized_phrase || ''))) && /отчет/.test(k.normalized_phrase || '') },
  { id: 'CORV-G03-02', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Создание отчёта 1С', intent: 'report_creation', landing: 'LP-07', url: '/otchety-1c/', bid: 'T2', filter: (k) => /создан.*отчет|новый отчет/.test(k.normalized_phrase || '') },
  { id: 'CORV-G03-03', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Печатные формы 1С', intent: 'print_forms_general', landing: 'LP-08', url: '/pechatnye-formy-1c/', bid: 'T1', filter: (k) => k.cluster === 'B_forms' && /печатн.*форм/.test(k.normalized_phrase || '') && !/упд|счет|зуп/.test(k.normalized_phrase || '') },
  { id: 'CORV-G03-04', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Доработка печатной формы', intent: 'print_form_modification', landing: 'LP-08', url: '/pechatnye-formy-1c/', bid: 'T1', filter: (k) => k.keyword_id === 'kw-corv01-010' || (k.cluster === 'B_forms' && /доработк.*печатн|изменить печатн|как сделать печатн/.test(k.normalized_phrase || '')) },
  { id: 'CORV-G03-05', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Внешние отчёты и обработки', intent: 'external_reports', landing: 'LP-07', url: '/otchety-1c/', bid: 'T2', filter: (k) => /внешн.*отчет|внешн.*обработк|внешн.*печатн/.test(k.normalized_phrase || '') },
  { id: 'CORV-G03-06', campaign: 'CORV-C03', direction: 'reports_forms', name: 'РМК и рабочее место кассира', intent: 'rmk_cashier', landing: 'LP-09', url: '/rmk-1c/', bid: 'T3', filter: (k) => k.cluster === 'B_rmk' || /рмк|рабоч.*мест.*кассир/.test(k.normalized_phrase || '') },

  // CORV-C04 — Управленческие задачи
  { id: 'CORV-G04-01', campaign: 'CORV-C04', direction: 'management', name: 'Расчёт себестоимости в 1С', intent: 'cost_calculation', landing: 'LP-10', url: '/sebestoimost-1c/', bid: 'T2', filter: (k) => /себестоим/.test(k.normalized_phrase || '') },
  { id: 'CORV-G04-02', campaign: 'CORV-C04', direction: 'management', name: 'Планирование закупок 1С', intent: 'procurement_planning', landing: 'LP-11', url: '/plan-zakupok-1c/', bid: 'T3', filter: (k) => /планирован.*закуп|закуп.*план/.test(k.normalized_phrase || '') },
  { id: 'CORV-G04-03', campaign: 'CORV-C04', direction: 'management', name: 'Платёжный календарь 1С', intent: 'payment_calendar', landing: 'LP-12', url: '/platezhnyj-kalendar-1c/', bid: 'T3', filter: (k) => /платежн.*календар|календар.*платеж/.test(k.normalized_phrase || '') },

  // CORV-C05 — Интеграции
  { id: 'CORV-G05-01', campaign: 'CORV-C05', direction: 'integrations', name: 'Интеграция 1С с сайтом', intent: 'website_integration', landing: 'LP-13', url: '/integraciya-1c-s-sajtom/', bid: 'T1', filter: (k) => k.cluster === 'C_integrations' && /сайт/.test(k.normalized_phrase || '') && !/битрикс/.test(k.normalized_phrase || '') },
  { id: 'CORV-G05-02', campaign: 'CORV-C05', direction: 'integrations', name: 'Интеграция 1С Битрикс', intent: 'bitrix_integration', landing: 'LP-14', url: '/integraciya-1c-bitrix/', bid: 'T2', filter: (k) => k.cluster === 'C_integrations' && /битрикс/.test(k.normalized_phrase || '') },
  { id: 'CORV-G05-03', campaign: 'CORV-C05', direction: 'integrations', name: 'Интеграция 1С с кассой', intent: 'cash_register_integration', landing: 'LP-15', url: '/integraciya-1c-kassa/', bid: 'T2', filter: (k) => /касс|ккт|фискальн|эквайр/.test(k.normalized_phrase || '') },
  { id: 'CORV-G05-04', campaign: 'CORV-C05', direction: 'integrations', name: 'Синхронизация и обмен 1С', intent: 'sync_exchange', landing: 'LP-16', url: '/sinhronizaciya-1c/', bid: 'T2', filter: (k) => k.cluster === 'C_integrations' && (/синхрон|обмен/.test(k.normalized_phrase || '')) && !/сайт|битрикс/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-012' },
  { id: 'CORV-G05-05', campaign: 'CORV-C05', direction: 'integrations', name: 'Настройка обмена 1С', intent: 'exchange_setup', landing: 'LP-16', url: '/sinhronizaciya-1c/', bid: 'T2', filter: (k) => /настройк.*обмен|обмен.*настройк/.test(k.normalized_phrase || '') },
  { id: 'CORV-G05-06', campaign: 'CORV-C05', direction: 'integrations', name: 'Перенос данных в 1С', intent: 'data_migration', landing: 'LP-17', url: '/perenos-dannyh-1c/', bid: 'T3', filter: (k) => /перенос.*данн|миграц.*данн|загрузк.*данн/.test(k.normalized_phrase || '') && !/доработ/.test(k.normalized_phrase || '') },

  // CORV-C06 — Маркировка
  { id: 'CORV-G06-01', campaign: 'CORV-C06', direction: 'marking', name: 'Подключение маркировки в 1С', intent: 'marking_setup', landing: 'LP-18', url: '/markirovka-1c/', bid: 'T2', filter: (k) => k.cluster === 'D_labeling' && /подключ|внедр|настро.*маркиров/.test(k.normalized_phrase || '') && !/честн/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-02', campaign: 'CORV-C06', direction: 'marking', name: 'Настройка маркировки 1С', intent: 'marking_configuration', landing: 'LP-18', url: '/markirovka-1c/', bid: 'T2', filter: (k) => k.cluster === 'D_labeling' && /настрой.*маркиров|маркиров.*настрой/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-03', campaign: 'CORV-C06', direction: 'marking', name: 'Честный знак и 1С', intent: 'honest_sign', landing: 'LP-19', url: '/chestnyj-znak-1c/', bid: 'T1', filter: (k) => k.cluster === 'D_labeling' && /честн.*знак|честный знак/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-008' },
  { id: 'CORV-G06-04', campaign: 'CORV-C06', direction: 'marking', name: 'Устранение ошибок маркировки', intent: 'marking_troubleshooting', landing: 'LP-18', url: '/markirovka-1c/', bid: 'T2', filter: (k) => k.cluster === 'D_labeling' && /ошибк.*маркиров|маркиров.*ошибк|не работ.*маркиров/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-05', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка напитков и алкоголя', intent: 'marking_beverages', landing: 'LP-20', url: '/markirovka-napitkov-1c/', bid: 'T3', filter: (k) => k.cluster === 'E_product_labeling' && /пив|алкогол|напит/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-016' },
  { id: 'CORV-G06-06', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка воды', intent: 'marking_water', landing: 'LP-21', url: '/markirovka-vody-1c/', bid: 'T3', filter: (k) => /маркиров.*вод|вода.*маркиров/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-017' },
  { id: 'CORV-G06-07', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка косметики', intent: 'marking_cosmetics', landing: 'LP-22', url: '/markirovka-kosmetiki-1c/', bid: 'T3', filter: (k) => /косметик.*маркиров|маркиров.*косметик/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-08', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка лекарств', intent: 'marking_medicines', landing: 'LP-23', url: '/markirovka-lekarstv-1c/', bid: 'T3', filter: (k) => k.cluster === 'E_product_labeling' && /лекарств/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-018' },
  { id: 'CORV-G06-09', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка бытовой химии', intent: 'marking_household_chem', landing: 'LP-24', url: '/markirovka-byt-himii-1c/', bid: 'T4', filter: (k) => /бытов.*хим.*маркиров|маркиров.*бытов.*хим/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-10', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка автозапчастей', intent: 'marking_auto_parts', landing: 'LP-25', url: '/markirovka-avtozapchastej-1c/', bid: 'T3', filter: (k) => /автозапчаст|авто запчаст/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-020' },
  { id: 'CORV-G06-11', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка масел', intent: 'marking_oils', landing: 'LP-26', url: '/markirovka-masel-1c/', bid: 'T4', filter: (k) => /масл.*маркиров|маркиров.*масл/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-12', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка техники', intent: 'marking_equipment', landing: 'LP-27', url: '/markirovka-tehniki-1c/', bid: 'T4', filter: (k) => /техник.*маркиров|маркиров.*техник/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-13', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка строительных материалов', intent: 'marking_building_materials', landing: 'LP-28', url: '/markirovka-stroymaterialov-1c/', bid: 'T4', filter: (k) => /строительн.*материал.*маркиров|маркиров.*строительн/.test(k.normalized_phrase || '') },

  // CORV-C07 — Неисправности
  { id: 'CORV-G07-01', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Программа 1С не работает', intent: 'urgent_not_working', landing: 'LP-29', url: '/1c-ne-rabotaet/', bid: 'T1', filter: (k) => k.cluster === 'A_urgent' || /не работает|не запуска/.test(k.normalized_phrase || '') },
  { id: 'CORV-G07-02', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Ошибка 1С / после обновления', intent: 'error_after_update', landing: 'LP-29', url: '/1c-ne-rabotaet/', bid: 'T2', filter: (k) => /ошибк.*1с|1с.*ошибк|после обновлен/.test(k.normalized_phrase || '') && k.intent_class !== 'regulatory' },
  { id: 'CORV-G07-03', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Не работает обмен / синхронизация', intent: 'sync_failure', landing: 'LP-30', url: '/obmen-1c-ne-rabotaet/', bid: 'T2', filter: (k) => /не работ.*обмен|сломал.*синхрон|не работ.*синхрон|обмен.*не работ/.test(k.normalized_phrase || '') },
  { id: 'CORV-G07-04', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Восстановление работы 1С', intent: 'recovery', landing: 'LP-29', url: '/1c-ne-rabotaet/', bid: 'T2', filter: (k) => /восстановлен.*работ|восстановить.*1с/.test(k.normalized_phrase || '') },

  // CORV-C08 — Специализированные
  { id: 'CORV-G08-01', campaign: 'CORV-C08', direction: 'specialist', name: 'ТС ПИОТ настройка', intent: 'ts_piot_setup', landing: 'LP-31', url: '/ts-piot-1c/', bid: 'T3', filter: (k) => k.cluster === 'D_ts_piot' && /настрой|внедр|подключ/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-019' },
  { id: 'CORV-G08-02', campaign: 'CORV-C08', direction: 'specialist', name: 'ТС ПИОТ интеграция с 1С', intent: 'ts_piot_integration', landing: 'LP-31', url: '/ts-piot-1c/', bid: 'T3', filter: (k) => k.cluster === 'D_ts_piot' && /интеграц|1с/.test(k.normalized_phrase || '') },
];

const SEED_FALLBACK = {
  'CORV-G01-01': ['программист 1С', 'услуги программиста 1С'],
  'CORV-G01-02': ['программист 1С Новосибирск'],
  'CORV-G01-05': ['сопровождение 1С'],
  'CORV-G02-01': ['доработка 1С'],
  'CORV-G03-01': ['доработка отчёта 1С'],
  'CORV-G03-04': ['доработка печатной формы 1С'],
  'CORV-G03-06': ['доработка РМК 1С'],
  'CORV-G05-01': ['интеграция 1С с сайтом'],
  'CORV-G05-02': ['интеграция 1С Битрикс'],
  'CORV-G05-04': ['настройка синхронизации 1С'],
  'CORV-G06-01': ['маркировка в 1С'],
  'CORV-G06-03': ['Честный знак 1С'],
  'CORV-G07-01': ['1С не работает', 'программа 1С не работает'],
  'CORV-G08-01': ['ТС ПИОТ 1С'],
};

const registry = {
  registry_id: 'corv-ad-group-registry-v1',
  project_id: 'corvonero-yandex-direct',
  generated_at: new Date().toISOString(),
  operating_model: 'FULL-SERVICE CLUSTERED SEARCH CAMPAIGN',
  geo: 'Новосибирск + Новосибирская область',
  domain: 'https://lk.corvonero.ru',
  campaigns: [
    { id: 'CORV-C01', name: 'Корво Неро — Общие услуги 1С', utm_campaign: 'corv_general_1c', purpose: 'Broad and retainer 1C services for B2B' },
    { id: 'CORV-C02', name: 'Корво Неро — Доработки 1С', utm_campaign: 'corv_modifications', purpose: 'Customization and update preservation' },
    { id: 'CORV-C03', name: 'Корво Неро — Отчёты и формы', utm_campaign: 'corv_reports_forms', purpose: 'Reports, print forms, RMK' },
    { id: 'CORV-C04', name: 'Корво Неро — Управленческие задачи', utm_campaign: 'corv_management', purpose: 'Cost, procurement, payment calendar' },
    { id: 'CORV-C05', name: 'Корво Неро — Интеграции', utm_campaign: 'corv_integrations', purpose: 'Website, Bitrix, cash, sync, data transfer' },
    { id: 'CORV-C06', name: 'Корво Неро — Маркировка', utm_campaign: 'corv_marking', purpose: 'Marking, Honest Sign, product categories' },
    { id: 'CORV-C07', name: 'Корво Неро — Неисправности', utm_campaign: 'corv_troubleshooting', purpose: 'Urgent fix and recovery' },
    { id: 'CORV-C08', name: 'Корво Неро — Специализированные', utm_campaign: 'corv_specialist', purpose: 'TS PIOT and narrow regulatory setup' },
  ],
  groups: GROUPS.map((g) => {
    let keywords = pickKeywords(g.filter, 15);
    if (keywords.length === 0 && SEED_FALLBACK[g.id]) {
      keywords = SEED_FALLBACK[g.id].map((phrase, i) => ({
        keyword_id: `seed-${g.id}-${i + 1}`,
        phrase,
        evidence_ref: 'operator_seed',
      }));
    }
    return {
      group_id: g.id,
      campaign_id: g.campaign,
      service_direction: g.direction,
      group_name: g.name,
      user_intent: g.intent,
      landing_page_id: g.landing,
      planned_url: `https://lk.corvonero.ru${g.url}`,
      url_status: 'PLANNED — PAGE NOT YET PUBLISHED',
      bid_tier: g.bid,
      match_strategy: 'phrase_with_group_negatives',
      ad_requirement: { min_ads: 1, max_ads: 2, ad_type: 'text-and-image-search' },
      keywords,
      keyword_count_planned: '15-25 at production',
      group_negatives: [],
      phrase_negatives: [],
      evidence_notes: keywords.length ? 'MIG keyword_registry filtered' : 'Seed fallback — expand in Stage 2B',
    };
  }),
  stats: {
    total_groups: GROUPS.length,
    total_campaigns: 8,
    mig_keywords_total: kr.keywords.length,
    noise_reject_classes: NOISE_REJECT,
  },
};

const outPath = path.join(ROOT, 'production/ad-group-registry-v1.json');
fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, JSON.stringify(registry, null, 2), 'utf8');
console.log('Written', outPath, 'groups:', registry.groups.length);
