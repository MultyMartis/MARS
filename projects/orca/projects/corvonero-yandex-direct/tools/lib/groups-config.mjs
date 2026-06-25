/** @typedef {{ id: string, campaign: string, direction: string, name: string, intent: string, landing: string, url: string, bid: string, priority: number, filter: (k: any) => boolean }} GroupDef */

/** @type {GroupDef[]} — most specific groups first (priority desc) */
export const GROUPS = [
  // CORV-C08 — most specific regulatory
  { id: 'CORV-G08-01', campaign: 'CORV-C08', direction: 'specialist', name: 'ТС ПИОТ настройка', intent: 'ts_piot_setup', landing: 'LP-31', url: '/ts-piot-1c/', bid: 'T3', priority: 95, filter: (k) => (/тс пиот|ts piot/.test(k.normalized_phrase || '') && /настрой|внедр|подключ/.test(k.normalized_phrase || '')) || (k.cluster === 'D_ts_piot' && /настрой|внедр|подключ/.test(k.normalized_phrase || '')) || k.keyword_id === 'kw-corv01-019' },
  { id: 'CORV-G08-02', campaign: 'CORV-C08', direction: 'specialist', name: 'ТС ПИОТ интеграция с 1С', intent: 'ts_piot_integration', landing: 'LP-31', url: '/ts-piot-1c/', bid: 'T3', priority: 94, filter: (k) => (/тс пиот|ts piot/.test(k.normalized_phrase || '') && !/настрой|внедр|подключ/.test(k.normalized_phrase || '')) || (k.cluster === 'D_ts_piot' && /интеграц|1с/.test(k.normalized_phrase || '') && !/настрой|внедр|подключ/.test(k.normalized_phrase || '')) },

  // CORV-C06 — product marking (specific before generic)
  { id: 'CORV-G06-05', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка напитков и алкоголя', intent: 'marking_beverages', landing: 'LP-20', url: '/markirovka-napitkov-1c/', bid: 'T3', priority: 90, filter: (k) => (k.cluster === 'E_product_labeling' && /пив|алкогол|напит/.test(k.normalized_phrase || '')) || k.keyword_id === 'kw-corv01-016' },
  { id: 'CORV-G06-06', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка воды', intent: 'marking_water', landing: 'LP-21', url: '/markirovka-vody-1c/', bid: 'T3', priority: 89, filter: (k) => /маркиров.*вод|вода.*маркиров/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-017' },
  { id: 'CORV-G06-07', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка косметики', intent: 'marking_cosmetics', landing: 'LP-22', url: '/markirovka-kosmetiki-1c/', bid: 'T3', priority: 88, filter: (k) => /косметик.*маркиров|маркиров.*косметик/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-08', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка лекарств', intent: 'marking_medicines', landing: 'LP-23', url: '/markirovka-lekarstv-1c/', bid: 'T3', priority: 87, filter: (k) => (k.cluster === 'E_product_labeling' && /лекарств/.test(k.normalized_phrase || '')) || k.keyword_id === 'kw-corv01-018' },
  { id: 'CORV-G06-09', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка бытовой химии', intent: 'marking_household_chem', landing: 'LP-24', url: '/markirovka-byt-himii-1c/', bid: 'T4', priority: 86, filter: (k) => /бытов.*хим.*маркиров|маркиров.*бытов.*хим/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-10', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка автозапчастей', intent: 'marking_auto_parts', landing: 'LP-25', url: '/markirovka-avtozapchastej-1c/', bid: 'T3', priority: 85, filter: (k) => /автозапчаст|авто запчаст/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-020' },
  { id: 'CORV-G06-11', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка масел', intent: 'marking_oils', landing: 'LP-26', url: '/markirovka-masel-1c/', bid: 'T4', priority: 84, filter: (k) => /масл.*маркиров|маркиров.*масл/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-12', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка техники', intent: 'marking_equipment', landing: 'LP-27', url: '/markirovka-tehniki-1c/', bid: 'T4', priority: 83, filter: (k) => /техник.*маркиров|маркиров.*техник/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-13', campaign: 'CORV-C06', direction: 'marking', name: 'Маркировка строительных материалов', intent: 'marking_building_materials', landing: 'LP-28', url: '/markirovka-stroymaterialov-1c/', bid: 'T4', priority: 82, filter: (k) => /строительн.*материал.*маркиров|маркиров.*строительн/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-03', campaign: 'CORV-C06', direction: 'marking', name: 'Честный знак и 1С', intent: 'honest_sign', landing: 'LP-19', url: '/chestnyj-znak-1c/', bid: 'T1', priority: 81, filter: (k) => k.cluster === 'D_labeling' && /честн.*знак|честный знак/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-008' },
  { id: 'CORV-G06-04', campaign: 'CORV-C06', direction: 'marking', name: 'Устранение ошибок маркировки', intent: 'marking_troubleshooting', landing: 'LP-18', url: '/markirovka-1c/', bid: 'T2', priority: 80, filter: (k) => k.cluster === 'D_labeling' && /ошибк.*маркиров|маркиров.*ошибк|не работ.*маркиров/.test(k.normalized_phrase || '') },
  { id: 'CORV-G06-01', campaign: 'CORV-C06', direction: 'marking', name: 'Подключение маркировки в 1С', intent: 'marking_setup', landing: 'LP-18', url: '/markirovka-1c/', bid: 'T2', priority: 79, filter: (k) => k.cluster === 'D_labeling' && /подключ|внедр|настро.*маркиров/.test(k.normalized_phrase || '') && !/честн/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-007' },
  { id: 'CORV-G06-02', campaign: 'CORV-C06', direction: 'marking', name: 'Настройка маркировки 1С', intent: 'marking_configuration', landing: 'LP-18', url: '/markirovka-1c/', bid: 'T2', priority: 78, filter: (k) => k.cluster === 'D_labeling' && /настрой.*маркиров|маркиров.*настрой/.test(k.normalized_phrase || '') && !/подключ|внедр/.test(k.normalized_phrase || '') },

  // CORV-C07
  { id: 'CORV-G07-03', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Не работает обмен / синхронизация', intent: 'sync_failure', landing: 'LP-30', url: '/obmen-1c-ne-rabotaet/', bid: 'T2', priority: 77, filter: (k) => /не работ.*обмен|сломал.*синхрон|не работ.*синхрон|обмен.*не работ/.test(k.normalized_phrase || '') },
  { id: 'CORV-G07-02', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Ошибка 1С / после обновления', intent: 'error_after_update', landing: 'LP-29', url: '/1c-ne-rabotaet/', bid: 'T2', priority: 76, filter: (k) => /ошибк.*1с|1с.*ошибк|после обновлен/.test(k.normalized_phrase || '') && k.intent_class !== 'regulatory' && !/обмен|синхрон/.test(k.normalized_phrase || '') },
  { id: 'CORV-G07-04', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Восстановление работы 1С', intent: 'recovery', landing: 'LP-29', url: '/1c-ne-rabotaet/', bid: 'T2', priority: 75, filter: (k) => /восстановлен.*работ|восстановить.*1с/.test(k.normalized_phrase || '') },
  { id: 'CORV-G07-01', campaign: 'CORV-C07', direction: 'troubleshooting', name: 'Программа 1С не работает', intent: 'urgent_not_working', landing: 'LP-29', url: '/1c-ne-rabotaet/', bid: 'T1', priority: 74, filter: (k) => (k.cluster === 'A_urgent' || /не работает|не запуска/.test(k.normalized_phrase || '')) && !/обмен|синхрон|ошибк.*маркиров/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-015' },

  // CORV-C05
  { id: 'CORV-G05-02', campaign: 'CORV-C05', direction: 'integrations', name: 'Интеграция 1С Битрикс', intent: 'bitrix_integration', landing: 'LP-14', url: '/integraciya-1c-bitrix/', bid: 'T2', priority: 73, filter: (k) => k.cluster === 'C_integrations' && /битрикс/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-006' },
  { id: 'CORV-G05-01', campaign: 'CORV-C05', direction: 'integrations', name: 'Интеграция 1С с сайтом', intent: 'website_integration', landing: 'LP-13', url: '/integraciya-1c-s-sajtom/', bid: 'T1', priority: 72, filter: (k) => k.cluster === 'C_integrations' && /сайт/.test(k.normalized_phrase || '') && !/битрикс/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-005' },
  { id: 'CORV-G05-03', campaign: 'CORV-C05', direction: 'integrations', name: 'Интеграция 1С с кассой', intent: 'cash_register_integration', landing: 'LP-15', url: '/integraciya-1c-kassa/', bid: 'T2', priority: 71, filter: (k) => !/тс пиот|ts piot/.test(k.normalized_phrase || '') && /касс|ккт|фискальн|эквайр/.test(k.normalized_phrase || '') && /интеграц|1с/.test(k.normalized_phrase || '') },
  { id: 'CORV-G05-06', campaign: 'CORV-C05', direction: 'integrations', name: 'Перенос данных в 1С', intent: 'data_migration', landing: 'LP-17', url: '/perenos-dannyh-1c/', bid: 'T3', priority: 70, filter: (k) => /перенос.*данн|миграц.*данн|загрузк.*данн/.test(k.normalized_phrase || '') && !/доработ/.test(k.normalized_phrase || '') },
  { id: 'CORV-G05-04', campaign: 'CORV-C05', direction: 'integrations', name: 'Синхронизация и обмен 1С', intent: 'sync_exchange', landing: 'LP-16', url: '/sinhronizaciya-1c/', bid: 'T2', priority: 69, filter: (k) => (k.cluster === 'C_integrations' && (/синхрон|обмен/.test(k.normalized_phrase || '')) && !/сайт|битрикс|не работ/.test(k.normalized_phrase || '')) || k.keyword_id === 'kw-corv01-012' },
  { id: 'CORV-G05-05', campaign: 'CORV-C05', direction: 'integrations', name: 'Настройка обмена 1С', intent: 'exchange_setup', landing: 'LP-16', url: '/sinhronizaciya-1c/', bid: 'T2', priority: 68, filter: (k) => /настройк.*обмен|обмен.*настройк/.test(k.normalized_phrase || '') && !/не работ/.test(k.normalized_phrase || '') },

  // CORV-C04
  { id: 'CORV-G04-01', campaign: 'CORV-C04', direction: 'management', name: 'Расчёт себестоимости в 1С', intent: 'cost_calculation', landing: 'LP-10', url: '/sebestoimost-1c/', bid: 'T2', priority: 67, filter: (k) => /себестоим/.test(k.normalized_phrase || '') },
  { id: 'CORV-G04-02', campaign: 'CORV-C04', direction: 'management', name: 'Планирование закупок 1С', intent: 'procurement_planning', landing: 'LP-11', url: '/plan-zakupok-1c/', bid: 'T3', priority: 66, filter: (k) => /планирован.*закуп|закуп.*план/.test(k.normalized_phrase || '') },
  { id: 'CORV-G04-03', campaign: 'CORV-C04', direction: 'management', name: 'Платёжный календарь 1С', intent: 'payment_calendar', landing: 'LP-12', url: '/platezhnyj-kalendar-1c/', bid: 'T3', priority: 65, filter: (k) => /платежн.*календар|календар.*платеж/.test(k.normalized_phrase || '') },

  // CORV-C03
  { id: 'CORV-G03-04', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Доработка печатной формы', intent: 'print_form_modification', landing: 'LP-08', url: '/pechatnye-formy-1c/', bid: 'T1', priority: 64, filter: (k) => k.keyword_id === 'kw-corv01-010' || (k.cluster === 'B_forms' && /доработк.*печатн|изменить печатн/.test(k.normalized_phrase || '')) },
  { id: 'CORV-G03-06', campaign: 'CORV-C03', direction: 'reports_forms', name: 'РМК и рабочее место кассира', intent: 'rmk_cashier', landing: 'LP-09', url: '/rmk-1c/', bid: 'T3', priority: 63, filter: (k) => !/тс пиот|ts piot/.test(k.normalized_phrase || '') && (k.cluster === 'B_rmk' || /рмк|рабоч.*мест.*кассир/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-011') },
  { id: 'CORV-G03-05', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Внешние отчёты и обработки', intent: 'external_reports', landing: 'LP-07', url: '/otchety-1c/', bid: 'T2', priority: 62, filter: (k) => /внешн.*отчет|внешн.*обработк|внешн.*печатн/.test(k.normalized_phrase || '') },
  { id: 'CORV-G03-02', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Создание отчёта 1С', intent: 'report_creation', landing: 'LP-07', url: '/otchety-1c/', bid: 'T2', priority: 61, filter: (k) => /создан.*отчет|новый отчет/.test(k.normalized_phrase || '') },
  { id: 'CORV-G03-01', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Доработка и настройка отчёта 1С', intent: 'report_customization', landing: 'LP-07', url: '/otchety-1c/', bid: 'T1', priority: 60, filter: (k) => ((k.cluster === 'B_reports' || (k.cluster === 'A_modification' && /отчет/.test(k.normalized_phrase || ''))) && /отчет/.test(k.normalized_phrase || '')) || k.keyword_id === 'kw-corv01-009' },
  { id: 'CORV-G03-03', campaign: 'CORV-C03', direction: 'reports_forms', name: 'Печатные формы 1С', intent: 'print_forms_general', landing: 'LP-08', url: '/pechatnye-formy-1c/', bid: 'T1', priority: 59, filter: (k) => k.cluster === 'B_forms' && /печатн.*форм/.test(k.normalized_phrase || '') && !/упд|счет|зуп|доработк/.test(k.normalized_phrase || '') },

  // CORV-C02
  { id: 'CORV-G02-04', campaign: 'CORV-C02', direction: 'modifications', name: 'Обновление доработанной 1С', intent: 'update_custom_base', landing: 'LP-06', url: '/obnovlenie-dorabotok-1c/', bid: 'T2', priority: 58, filter: (k) => (k.cluster === 'A_support' && /обновлен.*доработ|доработ.*обновлен/.test(k.normalized_phrase || '')) || k.keyword_id === 'kw-corv01-013' },
  { id: 'CORV-G02-05', campaign: 'CORV-C02', direction: 'modifications', name: 'Перенос и сохранение доработок', intent: 'migration_customizations', landing: 'LP-06', url: '/obnovlenie-dorabotok-1c/', bid: 'T3', priority: 57, filter: (k) => /перенос.*доработ|сохранен.*доработ/.test(k.normalized_phrase || '') },
  { id: 'CORV-G02-06', campaign: 'CORV-C02', direction: 'modifications', name: 'Исправление доработок после обновления', intent: 'fix_after_update', landing: 'LP-06', url: '/obnovlenie-dorabotok-1c/', bid: 'T2', priority: 56, filter: (k) => /исправлен.*доработ|доработ.*после обнов/.test(k.normalized_phrase || '') },
  { id: 'CORV-G02-02', campaign: 'CORV-C02', direction: 'modifications', name: 'Доработка конфигурации 1С', intent: 'modification_config', landing: 'LP-05', url: '/dorabotka-1c/', bid: 'T2', priority: 55, filter: (k) => k.cluster === 'A_modification' && /конфигурац|расширен|модул/.test(k.normalized_phrase || '') },
  { id: 'CORV-G02-03', campaign: 'CORV-C02', direction: 'modifications', name: 'Доработка базы 1С', intent: 'modification_database', landing: 'LP-05', url: '/dorabotka-1c/', bid: 'T2', priority: 54, filter: (k) => k.cluster === 'A_modification' && /баз/.test(k.normalized_phrase || '') && /доработ/.test(k.normalized_phrase || '') },
  { id: 'CORV-G02-01', campaign: 'CORV-C02', direction: 'modifications', name: 'Доработка 1С', intent: 'modification_general', landing: 'LP-05', url: '/dorabotka-1c/', bid: 'T1', priority: 53, filter: (k) => k.cluster === 'A_modification' && /доработ/.test(k.normalized_phrase || '') && !/отчет|печатн|конфигурац|баз|обновлен|перенос|исправлен/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-004' },

  // CORV-C01 — broad last
  { id: 'CORV-G01-02', campaign: 'CORV-C01', direction: 'general_1c', name: 'Программист 1С Новосибирск', intent: 'local_1c_dev', landing: 'LP-01', url: '/uslugi-1c/', bid: 'T1', priority: 52, filter: (k) => /новосибирск/.test(k.normalized_phrase || '') && /программист/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-002' },
  { id: 'CORV-G01-07', campaign: 'CORV-C01', direction: 'general_1c', name: 'Абонентское сопровождение', intent: 'subscription_support', landing: 'LP-04', url: '/soprovozhdenie-1c/', bid: 'T2', priority: 51, filter: (k) => /абонент/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-06', campaign: 'CORV-C01', direction: 'general_1c', name: 'Обслуживание 1С', intent: 'maintenance_1c', landing: 'LP-04', url: '/soprovozhdenie-1c/', bid: 'T2', priority: 50, filter: (k) => /обслуживан/.test(k.normalized_phrase || '') && !/абонент/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-05', campaign: 'CORV-C01', direction: 'general_1c', name: 'Сопровождение 1С', intent: 'support_retainer', landing: 'LP-04', url: '/soprovozhdenie-1c/', bid: 'T1', priority: 49, filter: (k) => k.cluster === 'A_support' && /сопровожден/.test(k.normalized_phrase || '') && !/абонент|обслужив/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-003' },
  { id: 'CORV-G01-04', campaign: 'CORV-C01', direction: 'general_1c', name: 'Внедрение 1С', intent: 'implementation_1c', landing: 'LP-03', url: '/vnedrenie-1c/', bid: 'T2', priority: 48, filter: (k) => /внедрен/.test(k.normalized_phrase || '') && !/маркиров/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-03', campaign: 'CORV-C01', direction: 'general_1c', name: 'Настройка 1С', intent: 'setup_1c', landing: 'LP-02', url: '/nastroyka-1c/', bid: 'T2', priority: 47, filter: (k) => k.cluster === 'A_broad_commercial' && /настройк/.test(k.normalized_phrase || '') && !/маркиров|интеграц|синхрон|обмен|отчет|печатн|обмен/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-08', campaign: 'CORV-C01', direction: 'general_1c', name: 'Разовые работы 1С', intent: 'one_off_1c', landing: 'LP-01', url: '/uslugi-1c/', bid: 'T2', priority: 46, filter: (k) => /разов/.test(k.normalized_phrase || '') },
  { id: 'CORV-G01-01', campaign: 'CORV-C01', direction: 'general_1c', name: 'Услуги программиста 1С', intent: 'hire_outsource_1c_dev', landing: 'LP-01', url: '/uslugi-1c/', bid: 'T1', priority: 45, filter: (k) => k.cluster === 'A_broad_commercial' && /программист|услуги программиста|аутсорс.*1с|1с.*аутсорс/.test(k.normalized_phrase || '') && !/новосибирск|обучен|курс|зарплат|стажер|ваканс|резюме|с нуля|москва|санкт|екатеринбург/.test(k.normalized_phrase || '') || k.keyword_id === 'kw-corv01-001' },
];

export const CAMPAIGNS = [
  { id: 'CORV-C01', name: 'Корво Неро — Общие услуги 1С', utm_campaign: 'corv_general_1c' },
  { id: 'CORV-C02', name: 'Корво Неро — Доработки 1С', utm_campaign: 'corv_modifications' },
  { id: 'CORV-C03', name: 'Корво Неро — Отчёты и формы', utm_campaign: 'corv_reports_forms' },
  { id: 'CORV-C04', name: 'Корво Неро — Управленческие задачи', utm_campaign: 'corv_management' },
  { id: 'CORV-C05', name: 'Корво Неро — Интеграции', utm_campaign: 'corv_integrations' },
  { id: 'CORV-C06', name: 'Корво Неро — Маркировка', utm_campaign: 'corv_marking' },
  { id: 'CORV-C07', name: 'Корво Неро — Неисправности', utm_campaign: 'corv_troubleshooting' },
  { id: 'CORV-C08', name: 'Корво Неро — Специализированные', utm_campaign: 'corv_specialist' },
];

export const SEED_FALLBACK = {
  'CORV-G01-01': ['программист 1С', 'услуги программиста 1С', 'программист 1с на аутсорсе'],
  'CORV-G01-02': ['программист 1С Новосибирск', 'программист 1с новосибирск'],
  'CORV-G01-03': ['настройка 1С', 'настройка 1с под ключ'],
  'CORV-G01-04': ['внедрение 1С', 'внедрение 1с под ключ'],
  'CORV-G01-05': ['сопровождение 1С', 'сопровождение 1с для бизнеса'],
  'CORV-G01-06': ['обслуживание 1С', 'обслуживание 1с для организации'],
  'CORV-G01-07': ['абонентское сопровождение 1С', 'абонентское обслуживание 1с'],
  'CORV-G01-08': ['разовые работы 1С', 'разовая доработка 1с'],
  'CORV-G02-01': ['доработка 1С', 'доработка 1с под задачу'],
  'CORV-G02-02': ['доработка конфигурации 1С', 'доработка конфигурации 1с'],
  'CORV-G02-03': ['доработка базы 1С', 'доработка базы 1с'],
  'CORV-G02-04': ['обновление доработанной 1С', 'обновление доработанной 1с'],
  'CORV-G02-05': ['перенос доработок 1С', 'сохранение доработок при обновлении 1с'],
  'CORV-G02-06': ['исправление доработок после обновления 1С'],
  'CORV-G03-01': ['доработка отчёта 1С', 'настройка отчета 1с'],
  'CORV-G03-02': ['создание отчёта 1С', 'новый отчет 1с'],
  'CORV-G03-03': ['печатные формы 1С', 'печатная форма 1с'],
  'CORV-G03-04': ['доработка печатной формы 1С'],
  'CORV-G03-05': ['внешний отчет 1С', 'внешняя обработка 1с'],
  'CORV-G03-06': ['доработка РМК 1С', 'настройка рмк 1с'],
  'CORV-G04-01': ['расчет себестоимости 1С', 'себестоимость в 1с'],
  'CORV-G04-02': ['планирование закупок 1С'],
  'CORV-G04-03': ['платежный календарь 1С'],
  'CORV-G05-01': ['интеграция 1С с сайтом'],
  'CORV-G05-02': ['интеграция 1С Битрикс', 'интеграция 1с и битрикс'],
  'CORV-G05-03': ['интеграция 1С с кассой'],
  'CORV-G05-04': ['настройка синхронизации 1С', 'синхронизация 1с'],
  'CORV-G05-05': ['настройка обмена 1С'],
  'CORV-G05-06': ['перенос данных в 1С', 'миграция данных 1с'],
  'CORV-G06-01': ['маркировка в 1С', 'подключение маркировки 1с'],
  'CORV-G06-02': ['настройка маркировки 1С'],
  'CORV-G06-03': ['Честный знак 1С', 'честный знак 1с'],
  'CORV-G06-04': ['ошибка маркировки 1С'],
  'CORV-G06-05': ['маркировка пива 1С'],
  'CORV-G06-06': ['маркировка воды 1С'],
  'CORV-G06-07': ['маркировка косметики 1С'],
  'CORV-G06-08': ['маркировка лекарств 1С'],
  'CORV-G06-09': ['маркировка бытовой химии 1С'],
  'CORV-G06-10': ['маркировка автозапчастей 1С'],
  'CORV-G06-11': ['маркировка масел 1С'],
  'CORV-G06-12': ['маркировка техники 1С'],
  'CORV-G06-13': ['маркировка строительных материалов 1С'],
  'CORV-G07-01': ['1С не работает', 'программа 1с не работает'],
  'CORV-G07-02': ['ошибка 1С', 'ошибка 1с после обновления'],
  'CORV-G07-03': ['не работает обмен 1С', 'не работает синхронизация 1с'],
  'CORV-G07-04': ['восстановление работы 1С'],
  'CORV-G08-01': ['ТС ПИОТ 1С', 'настройка тс пиот 1с'],
  'CORV-G08-02': ['интеграция тс пиот 1с'],
};

export const TIER_LIMITS = { T1: 25, T2: 20, T3: 15, T4: 10 };
export const DOMAIN = 'https://lk.corvonero.ru';
