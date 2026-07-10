/**
 * i-SEO Report Hub — Static Demo v0.4
 * INTLSEO-inspired UI, specialist workspace, content architecture. No backend.
 */
(function () {
  'use strict';

  var DEMO_PROJECTS = {
    service: {
      id: 'service',
      name: 'Сервисный сайт: инженерные услуги',
      client: 'Демо-клиент «Инжиниринг Сервис»',
      site: 'engineering-demo.example',
      type: 'Service / Corporate Site SEO',
      typeBadge: 'service',
      typeLabel: 'Service / Corporate',
      period: 'Июль 2026',
      specialist: 'Денис Demo',
      reviewer: 'Руководитель SEO Demo',
      monthlyStatus: 'draft',
      monthlyStatusLabel: 'Черновик (shell)',
      stageLabel: 'Неделя 1 — в работе',
      lifecycle: { w1: 'active', w2: 'not_started', w3: 'not_started', final: 'shell' },
      clientReportAvailable: false,
      clientReportReason: 'Недостаточно данных за отчётный период: завершена только неделя 1, monthly — пустая оболочка.',
      completenessPct: 12,
      nextAction: 'Завершить неделю 1 → начать неделю 2 (мета услуг, коммерческие факторы)',
      weeks: [
        { status: 'active', statusLabel: 'В работе', notStarted: false, summary: 'Стартовый аудит: инвентаризация страниц услуг, проверка целей конверсии, выявление технических блокеров на приоритетных URL.', works: ['Инвентаризация 24 страниц услуг — приоритетные 8 URL отмечены', 'Проверка целей «Отправка формы» в Метрике — работает; «Звонок» не настроен', 'Аудит редиректов: 3 цепочки на услугах монтажа — в работе', 'Начата переработка title/description для 4 приоритетных услуг'], metrics: 'Органика: 1 180 визитов (база июля). 9 заявок/звонков — предварительно. 18 приоритетных услуг в TOP-10.', blockers: 'Клиент не прислал список сертификатов — блокирует коммерческий блок на 3 услугах.', evidence: ['https://example.com/evidence/service-w1-audit', 'https://example.com/evidence/service-w1-goals'], nextPlan: 'Завершить редиректы на 7 URL\nПолучить сертификаты от клиента\nНачать черновик коммерческих факторов', internalNotes: 'Monthly создан как shell — не заполнять executive summary до W3. Клиент обещал сертификаты до 12 июля.', readyForReview: false, feedsMonthly: 'Работы W1 пойдут в блок «Выполненные работы» и «Техническое SEO» после закрытия недели.' },
        { status: 'not_started', statusLabel: 'Не начата', notStarted: true, summary: '', works: [], metrics: '', blockers: '', evidence: [], nextPlan: '', internalNotes: '', readyForReview: false, feedsMonthly: '' },
        { status: 'not_started', statusLabel: 'Не начата', notStarted: true, summary: '', works: [], metrics: '', blockers: '', evidence: [], nextPlan: '', internalNotes: '', readyForReview: false, feedsMonthly: '' }
      ],
      kpi: [
        { label: 'Органические визиты', value: '1 180', delta: 'база июля' },
        { label: 'Заявки / звонки', value: '9', delta: 'предварительно' },
        { label: 'Приоритетные услуги в TOP-10', value: '18', delta: 'стартовая база' },
        { label: 'Проверено служебных страниц', value: '11', delta: 'из 24' },
        { label: 'Коммерческие факторы', value: 'черновик', delta: 'аудит в работе' }
      ],
      checklistComplete: 2,
      checklistTotal: 16,
      missingBlocks: ['Executive Summary — пусто', 'Service Pages — не начато', 'Leads / Calls / Forms — черновик', 'Commercial Factors — черновик аудита', 'Semantic / Content — не начато', 'Positions / Visibility — не начато', 'Work Completed — W1 не свёрнуто в monthly'],
      risks: ['Сертификаты от клиента не получены — блокирует 3 услуги', 'Цель «звонок» не настроена — искажает отчёт по конверсиям', 'Monthly shell — клиентский отчёт недоступен'],
      executiveSummary: '',
      planNextMonth: ['Завершить технический аудит приоритетных услуг', 'Получить сертификаты и кейсы от клиента', 'Переписать мета для 8 услуг', 'Настроить цель на клик по телефону', 'Начать коммерческий чек-лист на TOP-услугах']
    },
    ecommerce: {
      id: 'ecommerce',
      name: 'Интернет-магазин инструментов',
      client: 'Демо-клиент «Industrial Tools»',
      site: 'demo-tools.example',
      type: 'E-commerce SEO',
      typeBadge: 'ecommerce',
      typeLabel: 'E-commerce',
      period: 'Июль 2026',
      specialist: 'Илья Demo',
      reviewer: 'Руководитель SEO Demo',
      monthlyStatus: 'draft',
      monthlyStatusLabel: 'Черновик (не готов клиенту)',
      stageLabel: 'Неделя 3 — на проверке',
      lifecycle: { w1: 'completed', w2: 'completed', w3: 'active', final: 'draft' },
      clientReportAvailable: false,
      clientReportReason: 'Monthly в черновике: нет интерпретации трафика, данные по заказам не сверены, решения по canonical фильтров не зафиксированы.',
      completenessPct: 58,
      nextAction: 'Завершить W3 → заполнить блок «Трафик» → отправить monthly на проверку',
      weeks: [
        { status: 'completed', statusLabel: 'Готово', notStarted: false, summary: 'Аудит структуры категорий, покрытие индексации, мета для приоритетных категорий.', works: ['Ревизия структуры 18 категорий — приоритетные 6 отмечены', 'Проверка индексации: 91% приоритетных категорий в индексе', 'Мета title/description для 4 категорий (шуруповёрты, перфораторы)', 'Выявлено 140 out-of-stock SKU в индексе — задача dev'], metrics: 'Органика +2% к предыдущей неделе. Индексация категорий стабильна.', blockers: '140 SKU out of stock в индексе — ждём dev.', evidence: ['https://example.com/evidence/ecom-w1-categories', 'https://example.com/evidence/ecom-w1-index'], nextPlan: 'Noindex на 12 фильтров\nТексты для 5 категорий\nНачать описания TOP-SKU', internalNotes: 'Dev backlog: out-of-stock noindex — приоритет на август.', readyForReview: true, feedsMonthly: 'W1 → блоки Category Pages, Indexing Coverage.' },
        { status: 'completed', statusLabel: 'Готово', notStarted: false, summary: 'Семантическое расширение, внутренняя перелинковка, доработка товарных страниц.', works: ['Семантическое расширение: +180 запросов в 4 категориях', 'Внутренняя перелинковка: блок «С этим покупают» на 8 категориях', '30 уникальных описаний TOP-SKU', 'Тексты и FAQ для 5 категорий'], metrics: 'Topvisor: +6 запросов TOP-10. Органика +5% к W1. Проверено 340 товарных страниц.', blockers: 'CRM ↔ Метрика: не все заказы с source=organic.', evidence: ['https://example.com/evidence/ecom-w2-semantic', 'https://example.com/topvisor-demo-categories-july'], nextPlan: 'Анализ фильтров/faceted nav\nИнтерпретация Topvisor\nПодготовить monthly draft', internalNotes: 'FAQ на 3 категориях — проверить микроразметку.', readyForReview: true, feedsMonthly: 'W2 → Semantic Expansion, Internal Linking, Product Pages.' },
        { status: 'review', statusLabel: 'На проверке', notStarted: false, summary: 'Анализ фильтров и faceted navigation. Интерпретация Topvisor. Monthly draft накоплен, но не готов клиенту.', works: ['Анализ canonical на 5 категориях с сортировкой — в работе', '15 описаний TOP-SKU (45 из 60 плана)', 'Черновик executive summary monthly', 'Topvisor: интерпретация видимости по «Шуруповёрты»'], metrics: 'Органика 4 820 (+11% к июню накопительно). Заказы CRM: ожидают сверки.', blockers: 'Релиз каталога 8 августа — риск новых дублей фильтров. Данные заказов не сверены.', evidence: ['https://example.com/evidence/ecom-w3-filters', 'https://example.com/evidence/ecom-w3-topvisor'], nextPlan: 'Завершить интерпретацию трафика\nЗафиксировать canonical-решения по фильтрам\nОтправить monthly на проверку', internalNotes: 'Monthly НЕ клиент-ready: блок Traffic пустой, Orders/Leads — черновик с caveat CRM.', readyForReview: false, feedsMonthly: 'W3 → Filters/Faceted Nav, Positions, Traffic (pending), Orders/Leads (pending).' }
      ],
      kpi: [
        { label: 'Органические визиты', value: '4 820', delta: '+11% к июню' },
        { label: 'Запросы в TOP-10', value: '146', delta: '+11' },
        { label: 'Обновлено категорий', value: '12', delta: 'тексты + мета' },
        { label: 'Проверено товарных страниц', value: '340', delta: 'из плана 400' },
        { label: 'Индексация приоритетных категорий', value: '91%', delta: 'GSC + краул' }
      ],
      checklistComplete: 11,
      checklistTotal: 19,
      missingBlocks: ['Traffic / Behavior — интерпретация не заполнена', 'Orders / Leads — данные ожидают сверки CRM', 'Filters / Faceted Navigation — canonical-решения не зафиксированы', 'Executive Summary — черновик, не client-safe'],
      risks: ['Дубли фильтров — частично; новые комбинации при обновлении каталога', '140 SKU out of stock в индексе', 'CRM ↔ Метрика: неполная связка — заказы как ориентир'],
      executiveSummary: 'В июле фокус — категории «Шуруповёрты», «Перфораторы», «Измерительный инструмент». Обновлены тексты, мета и перелинковка; в TOP-10 +11 запросов. Органика +11% к июню.\n\nТехнически закрыта часть дублей фильтров; остаётся риск при обновлении фида. 140 out-of-stock SKU в индексе — план noindex с dev на август.\n\n⚠️ ЧЕРНОВИК: блок трафика и заказов не готов к публикации клиенту. Требуется сверка CRM и интерпретация динамики.',
      planNextMonth: ['Завершить noindex/redirect для out-of-stock SKU (с dev)', 'Дописать описания 15 TOP-SKU', 'Зафиксировать canonical-политику фильтров', 'Настроить e-commerce цели в Метрике', 'Аудит фида после релиза каталога 8 августа']
    },
    local: {
      id: 'local',
      name: 'Региональный сайт услуг',
      client: 'Демо-клиент «Регион Сервис»',
      site: 'region-service-demo.example',
      type: 'Local / Regional SEO',
      typeBadge: 'local',
      typeLabel: 'Local / Regional',
      period: 'Июль 2026',
      specialist: 'SEO-специалист Demo',
      reviewer: 'Руководитель SEO Demo',
      monthlyStatus: 'published',
      monthlyStatusLabel: 'Опубликован',
      stageLabel: 'Финальный отчёт опубликован',
      lifecycle: { w1: 'completed', w2: 'completed', w3: 'completed', final: 'published' },
      clientReportAvailable: true,
      clientReportReason: '',
      completenessPct: 100,
      nextAction: 'Архивировать период; начать цикл августа (вне scope демо)',
      weeks: [
        { status: 'completed', statusLabel: 'Готово', notStarted: false, summary: 'Технический аудит, приоритетные regional pages, проверка контактов и реквизитов.', works: ['Технический аудит regional URL: 7 страниц в приоритете', 'Черновики landing Тольятти и Жигулёвск', 'LocalBusiness schema на пилотной странице', 'Проверка контактов и реквизитов на 4 URL'], metrics: 'Базовая видимость по «услуга + город» без существенных изменений.', blockers: 'Клиент не прислал реквизиты для 2 regional URL.', evidence: ['https://example.com/evidence/local-w1-audit', 'https://example.com/evidence/local-w1-contacts'], nextPlan: 'Опубликовать Тольятти\nОбновить Самару\nСобрать гео-семантику', internalNotes: 'Реквизиты — блокер для коммерческих факторов на 2 landing.', readyForReview: true, feedsMonthly: 'W1 → Technical SEO, Contacts/Requisites, Regional Landing Pages (draft).' },
        { status: 'completed', statusLabel: 'Готово', notStarted: false, summary: 'Обновление regional pages, гео-запросы, улучшение коммерческого доверия.', works: ['Опубликована «Ремонт — Тольятти»', 'Обновлена Самара (центр): тексты, мета, H1', 'Гео-семантика: +32 запроса «услуга + город»', 'FAQ и карта зоны на 2 страницах', 'Блок «Как мы работаем» на 3 regional URL'], metrics: '+12 гео-запросов TOP-10. Органика +5% к W1.', blockers: 'Кейсы с адресами объектов — не предоставлены.', evidence: ['https://example.com/evidence/local-w2-tolyatti', 'https://example.com/topvisor-demo-region-samara'], nextPlan: 'Жигулёвск — обновление\nРеквизиты на оставшихся landing\nВнутренние ссылки с главной', internalNotes: 'Topvisor группа «Регион Самара» — ссылка в monthly appendix.', readyForReview: true, feedsMonthly: 'W2 → Geo Queries, Local Trust, Regional Landing Pages.' },
        { status: 'completed', statusLabel: 'Готово', notStarted: false, summary: 'Финальные проверки, интерпретация видимости, client-safe риски, план на август.', works: ['Жигулёвск обновлён (+1 regional page)', 'Реквизиты и лицензия на странице Самара', 'Внутренние ссылки с главной на все 7 regional URL', 'Исправлено 18 технических замечаний (schema, canonical, дубли)', 'Monthly отправлен, проверен и опубликован'], metrics: 'Органика 2 940 (+9% к июню). Звонки/формы: 38 (+6). 64 региональных запроса TOP-10.', blockers: 'NAP на картах не синхронизирован — задача клиента (не блокирует публикацию).', evidence: ['https://example.com/evidence/local-w3-zhigulevsk', 'https://example.com/evidence/local-w3-published'], nextPlan: 'Micro-geo landing Самара (2 района)\nКейсы с геопривязкой\nNAP sync с картами', internalNotes: 'Monthly published v1 — client report доступен.', readyForReview: true, feedsMonthly: 'W3 → Positions/Visibility, Issues (client-safe), Plan, Evidence.' }
      ],
      kpi: [
        { label: 'Органические визиты', value: '2 940', delta: '+9% к июню' },
        { label: 'Звонки / формы', value: '38', delta: '+6 к июню' },
        { label: 'Региональные запросы в TOP-10', value: '64', delta: '+18' },
        { label: 'Обновлено региональных страниц', value: '7', delta: '+2 новые' },
        { label: 'Исправлено технических замечаний', value: '18', delta: 'GSC + краул' }
      ],
      checklistComplete: 18,
      checklistTotal: 18,
      missingBlocks: [],
      risks: ['Кейсы с геопривязкой не предоставлены — используем обезличенные описания', 'NAP на картах не синхронизирован — задача клиента на август', 'Атрибуция по регионам в аналитике неполная'],
      executiveSummary: 'Июль прошёл под задачу усиления региональной видимости по запросам «услуга + город». Обновлены 7 региональных посадочных; в TOP-10 вошли 64 гео-запроса (+18 к июню). Органика выросла на 9%, звонки и заявки — на 16% (38 обращений).\n\nНа всех regional страницах добавлены блоки доверия: «Как мы работаем», актуальные телефоны, карта зоны выезда, реквизиты на ключевых URL. Исправлено 18 технических замечаний (schema, canonical, дубли URL).\n\nНа август — micro-geo landing по районам Самары и синхронизация NAP с картами (задача клиента). Рекомендуем подготовить 3 кейса с геопривязкой для усиления CTR в региональной выдаче.',
      planNextMonth: ['Опубликовать 2 micro-geo landing (Самара: Промышленный, Кировский)', 'Добавить реквизиты на оставшиеся regional URL', 'Получить 3 кейса с городом/районом от клиента', 'Расширить семантику «услуга + район» (+40 запросов)', 'Синхронизировать NAP с картами (задача клиента)', 'Настроить click-to-call цели по regional landing']
    }
  };

  var TYPE_BLOCKS = {
    service: [
      { id: 'meta', title: 'Обложка / мета', inclusion: 'required', status: 'draft', clientSummary: 'Июль 2026 — ранний этап цикла', internalNote: 'Shell only', dataSource: 'manual', evidence: '', interpretation: '', nextAction: 'Заполнить после W3', owner: 'Денис Demo', updated: '10.07.2026' },
      { id: 'executive', title: 'Краткое резюме', inclusion: 'required', status: 'empty', clientSummary: '', internalNote: 'Не заполнять до W3', dataSource: '—', evidence: '', interpretation: '', nextAction: 'Ждать накопления weekly', owner: 'Денис Demo', updated: '—' },
      { id: 'kpi', title: 'KPI Snapshot', inclusion: 'required', status: 'draft', clientSummary: 'Предварительные метрики июля', internalNote: 'База W1, не финальные', dataSource: 'Метрика, Topvisor', evidence: 'example.com/evidence/service-w1-goals', interpretation: 'Стартовая база; рост оценим в конце месяца', nextAction: 'Обновить после W2', owner: 'Денис Demo', updated: '10.07.2026' },
      { id: 'service_pages', title: 'Service Pages', inclusion: 'required', status: 'empty', clientSummary: '', internalNote: 'Инвентаризация W1 — не свёрнута', dataSource: 'краул', evidence: '', interpretation: '', nextAction: 'Завершить аудит 8 приоритетных URL', owner: 'Денис Demo', updated: '—' },
      { id: 'leads', title: 'Leads / Calls / Forms', inclusion: 'required', status: 'draft', clientSummary: '9 обращений — предварительно', internalNote: 'Цель «звонок» не настроена', dataSource: 'Метрика', evidence: 'example.com/evidence/service-w1-goals', interpretation: 'Форма работает; звонки не размечены', nextAction: 'Настроить click-to-call цель с клиентом', owner: 'Денис Demo', updated: '10.07.2026' },
      { id: 'commercial', title: 'Commercial Factors', inclusion: 'required', status: 'draft', clientSummary: 'Черновик аудита коммерческих факторов', internalNote: 'Сертификаты блокируют 3 услуги', dataSource: 'manual checklist', evidence: '', interpretation: 'Без сертификатов сложно усилить доверие', nextAction: 'Получить сертификаты от клиента', owner: 'Клиент / Денис Demo', updated: '10.07.2026' },
      { id: 'technical', title: 'Technical SEO', inclusion: 'required', status: 'draft', clientSummary: 'Стартовый технический аудит', internalNote: '3 цепочки редиректов в работе', dataSource: 'GSC, краул', evidence: 'example.com/evidence/service-w1-audit', interpretation: 'Базовые проблемы выявлены, исправления в процессе', nextAction: 'Закрыть редиректы на 7 URL', owner: 'Денис Demo', updated: '10.07.2026' },
      { id: 'semantic', title: 'Semantic / Content', inclusion: 'required', status: 'empty', clientSummary: '', internalNote: 'Мета 4 услуг — в работе W1', dataSource: '—', evidence: '', interpretation: '', nextAction: 'Начать в W2', owner: 'Денис Demo', updated: '—' },
      { id: 'positions', title: 'Positions / Visibility', inclusion: 'required', status: 'empty', clientSummary: '', internalNote: '18 услуг TOP-10 — база', dataSource: 'Topvisor', evidence: '', interpretation: '', nextAction: 'Мониторинг с W2', owner: 'Денис Demo', updated: '—' },
      { id: 'issues', title: 'Issues / Plan / Evidence', inclusion: 'required', status: 'empty', clientSummary: '', internalNote: 'Риски фиксируются в weekly', dataSource: '—', evidence: '', interpretation: '', nextAction: 'Свёртка в monthly на W3', owner: 'Денис Demo', updated: '—' }
    ],
    ecommerce: [
      { id: 'meta', title: 'Обложка / мета', inclusion: 'required', status: 'approved', clientSummary: 'Июль 2026 — Industrial Tools', internalNote: 'Draft OK', dataSource: 'manual', evidence: '', interpretation: '', nextAction: '—', owner: 'Илья Demo', updated: '08.07.2026' },
      { id: 'executive', title: 'Краткое резюме', inclusion: 'required', status: 'draft', clientSummary: 'Черновик — не client-safe', internalNote: 'Нужна правка тона рисков', dataSource: 'manual', evidence: '', interpretation: 'Накоплено из W1–W2', nextAction: 'Дописать после W3', owner: 'Илья Demo', updated: '10.07.2026' },
      { id: 'kpi', title: 'KPI Snapshot', inclusion: 'required', status: 'approved', clientSummary: '4 820 визитов, 146 TOP-10, 12 категорий', internalNote: 'Заказы — ориентир', dataSource: 'Метрика, Topvisor, CRM', evidence: 'example.com/topvisor-demo-categories-july', interpretation: 'Рост за счёт категорийных страниц', nextAction: 'Сверить заказы CRM', owner: 'Илья Demo', updated: '10.07.2026' },
      { id: 'category', title: 'Category Pages', inclusion: 'required', status: 'approved', clientSummary: '12 категорий обновлены', internalNote: 'FAQ на 3 — проверить schema', dataSource: 'краул', evidence: 'example.com/evidence/ecom-w2-semantic', interpretation: 'Тексты + мета улучшили релевантность', nextAction: '—', owner: 'Илья Demo', updated: '09.07.2026' },
      { id: 'product', title: 'Product Pages', inclusion: 'required', status: 'draft', clientSummary: '340 SKU проверено, 45 описаний', internalNote: '15 SKU в W3 — в работе', dataSource: 'краул', evidence: 'example.com/evidence/ecom-w3-sku', interpretation: 'Thin content сокращается', nextAction: 'Дописать 15 TOP-SKU', owner: 'Илья Demo', updated: '10.07.2026' },
      { id: 'indexing', title: 'Indexing Coverage', inclusion: 'required', status: 'approved', clientSummary: '91% приоритетных категорий в индексе', internalNote: '140 OOS SKU — backlog', dataSource: 'GSC', evidence: 'example.com/evidence/ecom-w1-index', interpretation: 'Индексация стабильна; OOS — риск thin content', nextAction: 'Noindex OOS с dev', owner: 'Илья Demo / dev', updated: '08.07.2026' },
      { id: 'filters', title: 'Filters / Faceted Navigation', inclusion: 'required', status: 'needs_review', clientSummary: 'Анализ canonical в процессе', internalNote: 'Решения не зафиксированы', dataSource: 'краул', evidence: 'example.com/evidence/ecom-w3-filters', interpretation: 'Риск дублей при релизе 8 августа', nextAction: 'Зафиксировать canonical-политику', owner: 'Илья Demo', updated: '10.07.2026' },
      { id: 'semantic', title: 'Semantic Expansion', inclusion: 'required', status: 'approved', clientSummary: '+180 запросов в 4 категориях', internalNote: '', dataSource: 'Topvisor', evidence: 'example.com/evidence/ecom-w2-semantic', interpretation: '+6 TOP-10 за W2', nextAction: '—', owner: 'Илья Demo', updated: '09.07.2026' },
      { id: 'linking', title: 'Internal Linking', inclusion: 'required', status: 'approved', clientSummary: 'Блок «С этим покупают» на 8 категориях', internalNote: '', dataSource: 'manual', evidence: 'example.com/evidence/ecom-w2-semantic', interpretation: 'Улучшена перелинковка внутри кластеров', nextAction: '—', owner: 'Илья Demo', updated: '09.07.2026' },
      { id: 'positions', title: 'Positions / Visibility', inclusion: 'required', status: 'draft', clientSummary: '146 TOP-10 — интерпретация W3', internalNote: 'Topvisor card — приложить', dataSource: 'Topvisor', evidence: 'example.com/evidence/ecom-w3-topvisor', interpretation: 'В работе', nextAction: 'Завершить интерпретацию', owner: 'Илья Demo', updated: '10.07.2026' },
      { id: 'orders', title: 'Orders / Leads', inclusion: 'required', status: 'draft', clientSummary: 'Данные ожидают сверки CRM', internalNote: 'Не публиковать без caveat', dataSource: 'CRM (ориентир)', evidence: '', interpretation: 'Связка CRM↔Метрика неполная', nextAction: 'Сверить с клиентом', owner: 'Илья Demo', updated: '10.07.2026' },
      { id: 'traffic', title: 'Traffic / Behavior', inclusion: 'required', status: 'empty', clientSummary: '', internalNote: 'КРИТИЧНО — блокер публикации', dataSource: 'Метрика', evidence: '', interpretation: '', nextAction: 'Написать интерпретацию динамики', owner: 'Илья Demo', updated: '—' },
      { id: 'issues', title: 'Issues / Plan / Evidence', inclusion: 'required', status: 'draft', clientSummary: 'Риски дублей фильтров, OOS SKU', internalNote: 'Client-safe формулировки — проверить', dataSource: 'manual', evidence: '', interpretation: 'Честно о ограничениях данных', nextAction: 'Review с руководителем', owner: 'Илья Demo', updated: '10.07.2026' }
    ],
    local: [
      { id: 'meta', title: 'Обложка / мета', inclusion: 'required', status: 'published', clientSummary: 'Июль 2026 — Регион Сервис', internalNote: '', dataSource: 'manual', evidence: '', interpretation: '', nextAction: '—', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'executive', title: 'Краткое резюме', inclusion: 'required', status: 'published', clientSummary: 'Региональная видимость усилена: 7 landing, 64 geo TOP-10', internalNote: '', dataSource: 'manual', evidence: '', interpretation: 'Месяц закрыт успешно с оговорками по кейсам', nextAction: '—', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'kpi', title: 'KPI Snapshot', inclusion: 'required', status: 'published', clientSummary: '2 940 визитов, 38 обращений, 64 geo TOP-10', internalNote: '', dataSource: 'Метрика, Topvisor', evidence: 'example.com/topvisor-demo-region-samara', interpretation: '+9% органика, +16% обращения', nextAction: '—', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'regional', title: 'Regional Landing Pages', inclusion: 'required', status: 'published', clientSummary: '7 regional pages обновлены/опубликованы', internalNote: '', dataSource: 'краул', evidence: 'example.com/evidence/local-w2-tolyatti', interpretation: 'Рост видимости по «услуга + город»', nextAction: '—', owner: 'SEO-специалист Demo', updated: '09.07.2026' },
      { id: 'geo', title: 'Geo Queries', inclusion: 'required', status: 'published', clientSummary: '64 региональных запроса в TOP-10 (+18)', internalNote: '', dataSource: 'Topvisor', evidence: 'example.com/topvisor-demo-region-samara', interpretation: 'Сильнее всего Самара и Тольятти', nextAction: '—', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'trust', title: 'Local Trust / Commercial Factors', inclusion: 'required', status: 'published', clientSummary: 'Блоки доверия, FAQ, карта зоны на regional URL', internalNote: 'Кейсы — обезличенные', dataSource: 'manual', evidence: 'example.com/evidence/local-w3-zhigulevsk', interpretation: 'CTR улучшается на страницах с реквизитами', nextAction: 'Кейсы с гео — август', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'contacts', title: 'Contacts / Requisites', inclusion: 'required', status: 'published', clientSummary: 'Реквизиты и лицензия на ключевых URL', internalNote: 'Не на всех landing', dataSource: 'manual', evidence: 'example.com/evidence/local-w1-contacts', interpretation: 'Единый формат телефонов внедрён', nextAction: 'Добавить на оставшиеся URL', owner: 'Клиент / SEO Demo', updated: '08.07.2026' },
      { id: 'leads', title: 'Leads / Calls / Forms', inclusion: 'required', status: 'published', clientSummary: '38 звонков/форм (+6 к июню)', internalNote: 'Click-to-call — в плане', dataSource: 'Метрика', evidence: 'example.com/evidence/local-w3-published', interpretation: 'Рост на regional landing', nextAction: 'Настроить click-to-call по URL', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'technical', title: 'Technical SEO', inclusion: 'required', status: 'published', clientSummary: '18 технических замечаний исправлено', internalNote: '', dataSource: 'GSC, краул', evidence: 'example.com/evidence/local-w1-audit', interpretation: 'Schema LocalBusiness на 3 URL', nextAction: '—', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'positions', title: 'Positions / Visibility', inclusion: 'required', status: 'published', clientSummary: 'Topvisor: группа «Регион Самара»', internalNote: '', dataSource: 'Topvisor', evidence: 'example.com/topvisor-demo-region-samara', interpretation: 'Стабильный рост geo-запросов', nextAction: '—', owner: 'SEO-специалист Demo', updated: '10.07.2026' },
      { id: 'issues', title: 'Issues / Plan / Evidence', inclusion: 'required', status: 'published', clientSummary: 'NAP sync и кейсы — задачи на август', internalNote: 'Client-safe тон', dataSource: 'manual', evidence: 'example.com/evidence/local-w3-published', interpretation: 'Не блокируют итоги июля', nextAction: 'План на август согласован', owner: 'SEO-специалист Demo', updated: '10.07.2026' }
    ]
  };

  var MONTHLY_BLOCKS = [
    { num: 1, title: 'Обложка / мета', visibility: ['client', 'internal'], fields: 'meta' },
    { num: 2, title: 'Краткое резюме', visibility: ['client'], fields: 'summary' },
    { num: 3, title: 'KPI / ключевые показатели', visibility: ['client', 'data-source'], fields: 'kpi' },
    { num: 4, title: 'Выполненные работы', visibility: ['client', 'evidence'], fields: 'works' },
    { num: 5, title: 'Техническое SEO', visibility: ['client', 'internal'], fields: 'technical' },
    { num: 6, title: 'Семантика и контент', visibility: ['client'], fields: 'semantic' },
    { num: 7, title: 'Позиции и видимость', visibility: ['client', 'data-source'], fields: 'positions' },
    { num: 8, title: 'Трафик и поведение', visibility: ['client'], fields: 'traffic' },
    { num: 9, title: 'Лиды / конверсии', visibility: ['client'], fields: 'conversions' },
    { num: 10, title: 'Ссылки / авторитетность', visibility: ['client'], fields: 'links', optional: true },
    { num: 11, title: 'Проблемы / блокеры / риски', visibility: ['client', 'internal'], fields: 'risks' },
    { num: 12, title: 'План на следующий месяц', visibility: ['client'], fields: 'plan' },
    { num: 13, title: 'Подтверждения / приложение', visibility: ['client', 'evidence'], fields: 'evidence' }
  ];

  var WORKS_CONTENT = {
    service: {
      technical: '• Инвентаризация 24 страниц услуг — 8 приоритетных URL\n• Аудит редиректов: 3 цепочки на услугах монтажа — в работе\n• Проверка целей конверсии в Метрике\n• Начата переработка title/description для 4 услуг',
      semantic: '• Мета 4 приоритетных услуг — в работе (W1)\n• Семантика и контент — запланировано на W2',
      positions: '18 приоритетных услуг в TOP-10 — стартовая база июля.',
      traffic: 'Органика: 1 180 визитов — база первой недели.',
      conversions: '9 заявок/звонков — предварительно. Цель «звонок» не настроена.',
      links: '',
      servicePages: 'Инвентаризация 24 URL; приоритет: монтаж, проектирование, сервис.',
      commercial: 'Черновик аудита коммерческих факторов. Сертификаты — ожидание клиента.',
      profileExtra: 'Приоритетные услуги: проектирование, монтаж, сервис. Monthly — shell, W1 active.'
    },
    ecommerce: {
      technical: '• Noindex на 24 параметрических комбинации фильтров\n• Canonical для сортировок — в работе (W3)\n• Исправлены 404 на 11 устаревших SKU-URL\n• 91% приоритетных категорий в индексе',
      semantic: '• Семантическое расширение: +180 запросов в 4 категориях\n• Тексты и FAQ для 12 категорий\n• 45 уникальных описаний TOP-SKU (340 проверено)',
      positions: 'TOP-10: 146 запросов (+11). Topvisor «Категории июль 2026». Рост: шуруповёрты, перфораторы.',
      traffic: '',
      trafficMissing: true,
      conversions: 'Заказы (органика, CRM): ожидают сверки. Связка CRM ↔ Метрика неполная.',
      links: '',
      categoryPages: '12 категорий обновлены: тексты, мета, FAQ на 3.',
      productPages: '340 товарных страниц проверено; 45 описаний TOP-SKU готово.',
      indexing: '91% приоритетных категорий в индексе. 140 OOS SKU — backlog dev.',
      filters: 'Анализ canonical на сортировках — решения не зафиксированы.',
      profileExtra: 'Monthly draft — НЕ готов клиенту. Блоки Traffic, Orders pending.'
    },
    local: {
      technical: '• LocalBusiness schema на 3 regional URL\n• Исправлено 18 технических замечаний (schema, canonical, дубли)\n• Robots: закрыты staging-поддомены\n• Единый формат телефонов на regional landing',
      semantic: '• 7 regional landing обновлены/опубликованы\n• Гео-modifiers в title для 5 услуг\n• FAQ по срокам выезда на 3 landing\n• Внутренние ссылки с главной на все regional URL',
      positions: '64 региональных запроса TOP-10 (+18). Topvisor: группа «Регион Самара». SERP-скриншоты в приложении.',
      traffic: 'Органика: 2 940 (+9%). Рост на regional landing. Сквозная аналитика не разделяет регионы.',
      conversions: 'Звонки / формы: 38 (+6). Click-to-call по regional — в плане на август.',
      links: '',
      regional: '7 regional pages: Самара, Тольятти, Жигулёвск и др. Micro-geo — план августа.',
      geo: '64 geo-запроса TOP-10. Сильнее: «ремонт + Самара», «услуга + Тольятти».',
      trust: 'Блоки доверия, FAQ, карта зоны. Реквизиты на ключевых URL.',
      contacts: 'Реквизиты и лицензия на Самаре; единый NAP-формат.',
      profileExtra: 'Финальный отчёт опубликован. Client report доступен.'
    }
  };

  var CHECKLIST_ITEMS = [
    'Обложка / мета', 'Краткое резюме', 'KPI', 'Выполненные работы', 'Техническое SEO',
    'Семантика и контент', 'Позиции и видимость', 'Трафик и поведение', 'Лиды / конверсии',
    'Ссылки (опц.)', 'Проблемы / риски', 'План на месяц', 'Приложение'
  ];

  var WORK_CHECKLIST = {
    local: {
      technical: [
        { label: 'Исправлены schema / canonical на regional URL', checked: true, visibility: 'client', purpose: 'Техническая чистота regional landing' },
        { label: 'Robots: staging-поддомены закрыты', checked: true, visibility: 'internal', purpose: 'Исключить индексацию тестовых сред' }
      ],
      semantic: [
        { label: 'Обновлены title с гео-модификаторами', checked: true, visibility: 'client', purpose: 'Релевантность «услуга + город»' },
        { label: 'FAQ по срокам выезда на 3 landing', checked: true, visibility: 'client', purpose: 'Коммерческое доверие в SERP' }
      ],
      commercial: [
        { label: 'Реквизиты и лицензия на ключевых URL', checked: true, visibility: 'client', purpose: 'Доверие и конверсия' }
      ],
      positions: [
        { label: 'Topvisor: группа «Регион Самара» — интерпретация', checked: true, visibility: 'client', purpose: 'Подтверждение роста geo-видимости' }
      ],
      analytics: [
        { label: 'Сверка звонков/форм с Метрикой', checked: true, visibility: 'client', purpose: 'KPI для executive summary' }
      ],
      evidence: [
        { label: 'SERP-скриншоты regional запросов', checked: true, visibility: 'evidence', purpose: 'Приложение к отчёту' }
      ]
    },
    ecommerce: {
      technical: [
        { label: 'Noindex на 24 параметрических комбинации', checked: true, visibility: 'client', purpose: 'Снижение дублей фильтров' },
        { label: 'Canonical для сортировок — в работе', checked: false, visibility: 'reviewer', purpose: 'Блокер monthly Traffic' }
      ],
      semantic: [
        { label: '45 описаний TOP-SKU', checked: true, visibility: 'client', purpose: 'Thin content на приоритетных SKU' },
        { label: 'FAQ на 3 категориях — проверить schema', checked: false, visibility: 'reviewer', purpose: 'Микроразметка перед публикацией' }
      ],
      commercial: [
        { label: 'Блок «С этим покупают» на 8 категориях', checked: true, visibility: 'client', purpose: 'Внутренняя перелинковка кластеров' }
      ],
      positions: [
        { label: 'Интерпретация Topvisor «Шуруповёрты»', checked: false, visibility: 'client', purpose: 'Блок Positions / Visibility' }
      ],
      analytics: [
        { label: 'Интерпретация динамики трафика', checked: false, visibility: 'client', purpose: 'КРИТИЧНО — блок Traffic пустой' },
        { label: 'Сверка заказов CRM ↔ Метрика', checked: false, visibility: 'internal', purpose: 'Orders / Leads — не публиковать без caveat' }
      ],
      evidence: [
        { label: 'Скриншот GSC: индексация категорий', checked: true, visibility: 'evidence', purpose: 'Подтверждение 91% coverage' },
        { label: 'Topvisor export июль 2026', checked: false, visibility: 'evidence', purpose: 'Приложение к monthly' }
      ]
    },
    service: {
      technical: [
        { label: 'Инвентаризация 24 страниц услуг', checked: true, visibility: 'client', purpose: 'База для service pages block' },
        { label: 'Аудит редиректов: 3 цепочки', checked: false, visibility: 'internal', purpose: 'W1 — в работе' }
      ],
      semantic: [
        { label: 'Title/description для 4 приоритетных услуг', checked: false, visibility: 'client', purpose: 'Старт semantic block' }
      ],
      commercial: [
        { label: 'Черновик коммерческих факторов', checked: false, visibility: 'reviewer', purpose: 'Ждём сертификаты от клиента' }
      ],
      positions: [
        { label: 'База 18 услуг в TOP-10', checked: true, visibility: 'data-source', purpose: 'Стартовый snapshot Topvisor' }
      ],
      analytics: [
        { label: 'Проверка целей «Отправка формы»', checked: true, visibility: 'client', purpose: 'Leads block' },
        { label: 'Настроить цель «звонок»', checked: false, visibility: 'internal', purpose: 'Искажает конверсии в отчёте' }
      ],
      evidence: [
        { label: 'Скриншот целей Метрики', checked: true, visibility: 'evidence', purpose: 'Подтверждение tracking' }
      ]
    }
  };

  var WORK_CATEGORY_LABELS = {
    technical: 'Technical SEO',
    semantic: 'Semantic / Content',
    commercial: 'Commercial factors',
    positions: 'Positions / Visibility',
    analytics: 'Analytics / Conversions',
    evidence: 'Evidence / Screenshots'
  };

  var SPECIALIST_TEXTS = {
    local: {
      clientSummary: 'Июль: усилена региональная видимость по «услуга + город». 7 landing обновлены, 64 geo TOP-10 (+18). Органика +9%, обращения +16%.',
      changes: 'Опубликованы/обновлены regional pages Тольятти, Жигулёвск, Самара. Добавлены блоки доверия, FAQ, карта зоны.',
      interpretation: 'Рост за счёт гео-релевантных landing и технической чистоты. Сильнее всего Самара и Тольятти.',
      blockers: 'NAP на картах не синхронизирован — задача клиента. Кейсы с геопривязкой не предоставлены.',
      nextPlan: 'Micro-geo landing (2 района Самары). Синхронизация NAP. 3 кейса с гео от клиента.',
      internalNote: 'Monthly published v1. Client report доступен. Архивировать период.'
    },
    ecommerce: {
      clientSummary: 'Черновик: фокус на категории «Шуруповёрты», «Перфораторы». TOP-10 +11 запросов. Органика +11% к июню.',
      changes: '12 категорий обновлены. 45 SKU описаний. Частично закрыты дубли фильтров.',
      interpretation: 'Рост за счёт категорийных страниц. Блок трафика и заказов — в подготовке.',
      blockers: 'CRM ↔ Метрика неполная связка. Релиз каталога 8 августа — риск новых дублей.',
      nextPlan: 'Завершить интерпретацию Traffic. Зафиксировать canonical фильтров. Сверить заказы CRM.',
      internalNote: 'Monthly НЕ client-ready. W3 на проверке. Не отправлять клиенту до Traffic + Orders.'
    },
    service: {
      clientSummary: '',
      changes: 'W1: стартовый аудит 24 страниц услуг. Проверка целей конверсии. Начата мета для 4 услуг.',
      interpretation: 'Базовая неделя — накопление данных. Executive summary заполнять после W3.',
      blockers: 'Клиент не прислал сертификаты — блокирует коммерческий блок на 3 услугах.',
      nextPlan: 'Завершить редиректы. Получить сертификаты. Начать коммерческий чек-лист.',
      internalNote: 'Monthly shell — не заполнять executive summary до W3. Client report недоступен.'
    }
  };

  var KPI_INPUTS = {
    local: [
      { metric: 'Органические визиты', value: '2 940', period: 'Июль 2026', source: 'Яндекс.Метрика', interpretation: '+9% к июню', clientVisible: true },
      { metric: 'Звонки / формы', value: '38', period: 'Июль 2026', source: 'Метрика', interpretation: '+6 к июню', clientVisible: true },
      { metric: 'Региональные TOP-10', value: '64', period: 'Июль 2026', source: 'Topvisor', interpretation: '+18 geo-запросов', clientVisible: true }
    ],
    ecommerce: [
      { metric: 'Органические визиты', value: '4 820', period: 'Июль 2026', source: 'Метрика', interpretation: '+11% к июню — черновик', clientVisible: true },
      { metric: 'Запросы TOP-10', value: '146', period: 'Июль 2026', source: 'Topvisor', interpretation: '+11 — интерпретация W3', clientVisible: true },
      { metric: 'Заказы (органика)', value: '—', period: 'Июль 2026', source: 'CRM (ориентир)', interpretation: 'Ожидает сверки', clientVisible: false }
    ],
    service: [
      { metric: 'Органические визиты', value: '1 180', period: 'W1 июля', source: 'Метрика', interpretation: 'База первой недели', clientVisible: false },
      { metric: 'Заявки / звонки', value: '9', period: 'W1 июля', source: 'Метрика', interpretation: 'Предварительно, звонки не размечены', clientVisible: false },
      { metric: 'Услуги в TOP-10', value: '18', period: 'Июль 2026', source: 'Topvisor', interpretation: 'Стартовая база', clientVisible: false }
    ]
  };

  var EVIDENCE_ITEMS = {
    local: [
      { title: 'Topvisor — Регион Самара', source: 'Topvisor', block: 'Positions / Visibility', link: 'https://example.com/topvisor-demo-region-samara', clientVisible: true },
      { title: 'SERP screenshot — «ремонт Самара»', source: 'Manual screenshot', block: 'Geo Queries', link: 'https://example.com/evidence/local-serp-samara', clientVisible: true }
    ],
    ecommerce: [
      { title: 'GSC — индексация категорий', source: 'Google Search Console', block: 'Indexing Coverage', link: 'https://example.com/evidence/ecom-w1-index', clientVisible: true },
      { title: 'Анализ canonical фильтров', source: 'Краул', block: 'Filters / Faceted Nav', link: 'https://example.com/evidence/ecom-w3-filters', clientVisible: false },
      { title: 'Topvisor — категории июль', source: 'Topvisor', block: 'Positions', link: 'https://example.com/topvisor-demo-categories-july', clientVisible: false }
    ],
    service: [
      { title: 'Аудит целей Метрики', source: 'Яндекс.Метрика', block: 'Leads / Calls', link: 'https://example.com/evidence/service-w1-goals', clientVisible: false },
      { title: 'Стартовый технический аудит', source: 'GSC + краул', block: 'Technical SEO', link: 'https://example.com/evidence/service-w1-audit', clientVisible: false }
    ]
  };

  function $(sel, ctx) { return (ctx || document).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(sel)); }

  function statusBadgeClass(status) {
    var map = { completed: 'badge--completed', review: 'badge--review', draft: 'badge--draft', approved: 'badge--completed', published: 'badge--approved', submitted: 'badge--submitted', active: 'badge--review', not_started: 'badge--draft', empty: 'badge--draft', needs_review: 'badge--review' };
    return map[status] || 'badge--draft';
  }

  function blockStatusLabel(status) {
    var map = { empty: 'Пусто', draft: 'Черновик', needs_review: 'На проверке', approved: 'Утверждён', published: 'Опубликован' };
    return map[status] || status;
  }

  function lifecycleStepClass(state) {
    if (state === 'completed' || state === 'published') return 'lifecycle-step--done';
    if (state === 'active' || state === 'draft') return 'lifecycle-step--active';
    if (state === 'not_started' || state === 'shell') return 'lifecycle-step--pending';
    return 'lifecycle-step--pending';
  }

  function lifecycleStepIcon(state) {
    if (state === 'completed' || state === 'published') return '✓';
    if (state === 'active' || state === 'draft') return '◐';
    return '○';
  }

  function renderLifecycleStrip(lc) {
    var steps = [
      { key: 'w1', label: 'Неделя 1' },
      { key: 'w2', label: 'Неделя 2' },
      { key: 'w3', label: 'Неделя 3' },
      { key: 'final', label: 'Final' }
    ];
    return '<div class="lifecycle-strip">' + steps.map(function (s) {
      var st = lc[s.key];
      return '<div class="lifecycle-step ' + lifecycleStepClass(st) + '"><span class="lifecycle-step__icon">' + lifecycleStepIcon(st) + '</span><span class="lifecycle-step__label">' + s.label + '</span></div>';
    }).join('') + '</div>';
  }

  function renderBlockAnatomy(b) {
    return '<div class="block-anatomy">' +
      '<div class="block-anatomy__row"><span class="block-anatomy__key">Статус:</span> <span class="badge ' + statusBadgeClass(b.status) + '">' + blockStatusLabel(b.status) + '</span> <span class="block-anatomy__key">Включение:</span> ' + b.inclusion + '</div>' +
      (b.clientSummary ? '<div class="block-anatomy__row"><span class="block-anatomy__key">Клиенту:</span> ' + b.clientSummary + '</div>' : '') +
      (b.internalNote ? '<div class="block-anatomy__row block-anatomy__row--internal"><span class="block-anatomy__key">Внутреннее:</span> ' + b.internalNote + '</div>' : '') +
      (b.dataSource ? '<div class="block-anatomy__row"><span class="block-anatomy__key">Источник:</span> ' + b.dataSource + '</div>' : '') +
      (b.interpretation ? '<div class="block-anatomy__row"><span class="block-anatomy__key">Интерпретация:</span> ' + b.interpretation + '</div>' : '') +
      (b.nextAction && b.nextAction !== '—' ? '<div class="block-anatomy__row"><span class="block-anatomy__key">След. действие:</span> ' + b.nextAction + '</div>' : '') +
      '<div class="block-anatomy__meta"><span>Владелец: ' + b.owner + '</span> · <span>Обновлено: ' + b.updated + '</span></div>' +
      '</div>';
  }

  function visibilityBadges(vis) {
    var labels = { client: 'клиенту', internal: 'внутреннее', reviewer: 'проверяющему', 'data-source': 'источник данных', evidence: 'источник данных' };
    return vis.map(function (v) {
      return '<span class="visibility-badge visibility-badge--' + v + '">' + (labels[v] || v) + '</span>';
    }).join(' ');
  }

  function renderKpiGrid(kpi) {
    return kpi.map(function (k) {
      return '<div class="kpi-card"><div class="kpi-card__label">' + k.label + '</div><div class="kpi-card__value">' + k.value + '</div><div class="kpi-card__delta">' + k.delta + '</div></div>';
    }).join('');
  }

  function getProject(id) { return DEMO_PROJECTS[id] || DEMO_PROJECTS.service; }

  function initNav() {
    var currentPage = window.location.pathname.split('/').pop() || 'index.html';
    $$('.sidebar__nav a[data-page]').forEach(function (link) {
      if (link.getAttribute('data-page') === currentPage) link.classList.add('is-active');
    });
  }

  function initProjectTabs() {
    var root = $('[data-project-tabs]');
    if (!root) return;
    var defaultId = root.getAttribute('data-default-project') || 'service';
    var urlParam = new URLSearchParams(window.location.search).get('project');
    if (urlParam && DEMO_PROJECTS[urlParam]) defaultId = urlParam;

    function switchProject(id) {
      $$('[data-project-tab]').forEach(function (tab) {
        tab.classList.toggle('is-active', tab.getAttribute('data-project-tab') === id);
      });
      $$('[data-project-panel]').forEach(function (panel) {
        panel.hidden = panel.getAttribute('data-project-panel') !== id;
      });
      var sel = $('[data-project-select]');
      if (sel) sel.value = id;
      document.dispatchEvent(new CustomEvent('demo:project-change', { detail: { projectId: id } }));
    }

    $$('[data-project-tab]').forEach(function (tab) {
      tab.addEventListener('click', function () { switchProject(tab.getAttribute('data-project-tab')); });
    });
    var sel = $('[data-project-select]');
    if (sel) {
      sel.addEventListener('change', function () { switchProject(sel.value); });
    }
    switchProject(defaultId);
  }

  function initWeeklyEditor() {
    var root = $('[data-weekly-editor]');
    if (!root) return;
    var urlParam = new URLSearchParams(window.location.search).get('project');
    var projectId = (urlParam && DEMO_PROJECTS[urlParam]) ? urlParam : 'ecommerce';
    var projectSel = $('[data-project-select]');
    if (projectSel && DEMO_PROJECTS[projectSel.value]) projectId = projectSel.value;
    var weekParam = new URLSearchParams(window.location.search).get('week');
    var weekNum = weekParam ? parseInt(weekParam, 10) : 3;

    function render() {
      var p = getProject(projectId);
      var w = p.weeks[weekNum - 1];
      if (!w) return;
      var indicator = $('[data-week-indicator]');
      if (indicator) indicator.textContent = 'Неделя ' + weekNum + ' · ' + p.client;
      var title = $('[data-weekly-title]');
      if (title) title.textContent = p.client + ' — ' + p.name;
      var statusEl = $('[data-weekly-status]');
      if (statusEl) statusEl.innerHTML = '<span class="badge ' + statusBadgeClass(w.status) + '">' + w.statusLabel + '</span>';
      var emptyEl = $('[data-weekly-empty]', root);
      var contentEl = $('[data-weekly-content]', root);
      if (w.notStarted) {
        if (emptyEl) { emptyEl.hidden = false; emptyEl.innerHTML = '<div class="empty-state"><h3>Неделя ' + weekNum + ' не начата</h3><p>Для проекта «' + p.client + '» эта неделя ещё не открыта. Завершите предыдущие чекпоинты.</p></div>'; }
        if (contentEl) contentEl.hidden = true;
        return;
      }
      if (emptyEl) emptyEl.hidden = true;
      if (contentEl) contentEl.hidden = false;
      root.classList.toggle('is-week-locked', w.status === 'completed');
      root.classList.toggle('is-week-active', w.status === 'active' || w.status === 'review');
      var fields = {
        '[data-field="summary"]': w.summary,
        '[data-field="metrics"]': w.metrics,
        '[data-field="blockers"]': w.blockers,
        '[data-field="next-plan"]': w.nextPlan,
        '[data-field="internal-notes"]': w.internalNotes
      };
      Object.keys(fields).forEach(function (sel) {
        var el = $(sel, root);
        if (el) { el.value = fields[sel]; el.readOnly = w.status === 'completed'; }
      });
      var worksList = $('[data-field="works-list"]', root);
      if (worksList) {
        worksList.innerHTML = w.works.length ? w.works.map(function (item) {
          return '<li><input type="checkbox" checked disabled> ' + item + '</li>';
        }).join('') : '<li class="text-muted">Работы не зафиксированы</li>';
      }
      var evidence = $('[data-field="evidence-list"]', root);
      if (evidence) {
        evidence.innerHTML = w.evidence.length ? w.evidence.map(function (url) {
          return '<div class="evidence-card"><div class="evidence-card__icon">🔗</div><input class="form-input" type="url" value="' + url + '" readonly></div>';
        }).join('') : '<p class="text-muted">Подтверждения не добавлены</p>';
      }
      var ready = $('[data-field="ready-review"]', root);
      if (ready) { ready.checked = w.readyForReview; ready.disabled = w.status === 'completed'; }
      var feeds = $('[data-field="feeds-monthly"]', root);
      if (feeds && w.feedsMonthly) feeds.textContent = w.feedsMonthly;
      var lcStrip = $('[data-weekly-lifecycle]', root);
      if (lcStrip) lcStrip.innerHTML = renderLifecycleStrip(p.lifecycle);
    }

    document.addEventListener('demo:project-change', function (e) {
      projectId = e.detail.projectId;
      render();
    });

    var weekSel = $('[data-week-select]');
    if (weekSel) {
      weekSel.value = String(weekNum);
      weekSel.addEventListener('change', function () {
        weekNum = parseInt(weekSel.value, 10);
        render();
      });
    }
    render();
  }

  function initMonthlyEditor() {
    var root = $('[data-monthly-editor]');
    if (!root) return;

    function renderMonthly(projectId) {
      var p = getProject(projectId);
      var wc = WORKS_CONTENT[projectId];
      var statusEl = $('[data-monthly-status]');
      if (statusEl) statusEl.innerHTML = '<span class="badge ' + statusBadgeClass(p.monthlyStatus) + '">' + p.monthlyStatusLabel + '</span>';
      var title = $('[data-monthly-title]');
      if (title) title.textContent = p.client + ' — Закрытие месяца';
      var subtitle = $('[data-monthly-subtitle]');
      if (subtitle) subtitle.textContent = p.name + ' · ' + p.type + ' · ' + p.site;

      var missingEl = $('[data-monthly-missing]');
      if (missingEl) {
        if (p.missingBlocks.length) {
          missingEl.innerHTML = '<strong>Замечания по блокам:</strong><ul class="alert__list">' +
            p.missingBlocks.map(function (m) { return '<li>' + m + '</li>'; }).join('') + '</ul>';
          missingEl.className = 'alert alert--warning';
        } else {
          missingEl.innerHTML = '<strong>Все обязательные блоки заполнены.</strong> Отчёт готов к публикации (демо).';
          missingEl.className = 'alert alert--info';
        }
      }

      var completeness = $('[data-completeness-list]');
      if (completeness) {
        var filled = p.checklistComplete;
        completeness.innerHTML = CHECKLIST_ITEMS.map(function (item, i) {
          var done = i < filled;
          return '<li><input type="checkbox" ' + (done ? 'checked' : '') + ' disabled> ' + item + '</li>';
        }).join('');
      }
      var compPct = $('[data-completeness-pct]');
      if (compPct) compPct.textContent = (p.completenessPct || Math.round((p.checklistComplete / p.checklistTotal) * 100)) + '%';

      var lcEl = $('[data-monthly-lifecycle]');
      if (lcEl) lcEl.innerHTML = renderLifecycleStrip(p.lifecycle);

      var gateEl = $('[data-publish-gates]');
      if (gateEl) {
        var gates = [
          { label: 'Все required-блоки approved', ok: p.missingBlocks.length === 0 && p.monthlyStatus !== 'draft' },
          { label: 'Reviewer approval', ok: p.monthlyStatus === 'published' || p.monthlyStatus === 'approved' },
          { label: 'Client-safe text ready', ok: p.clientReportAvailable },
          { label: 'Evidence checked', ok: p.monthlyStatus === 'published' }
        ];
        gateEl.innerHTML = '<ul class="publish-gates">' + gates.map(function (g) {
          return '<li class="publish-gate ' + (g.ok ? 'publish-gate--ok' : 'publish-gate--pending') + '">' + (g.ok ? '✓' : '○') + ' ' + g.label + '</li>';
        }).join('') + '</ul>';
      }

      var typeMatrixEl = $('[data-type-block-matrix]');
      if (typeMatrixEl) {
        var blocks = TYPE_BLOCKS[projectId] || [];
        typeMatrixEl.innerHTML = blocks.map(function (b, i) {
          var extra = b.status === 'empty' ? ' is-missing' : (b.status === 'draft' || b.status === 'needs_review' ? ' is-draft' : '');
          return '<div class="report-block report-block--profile' + extra + '">' +
            '<div class="report-block__header"><span>' + (i + 1) + '. ' + b.title + '</span>' +
            '<span class="report-block__badges"><span class="badge ' + statusBadgeClass(b.status) + '">' + blockStatusLabel(b.status) + '</span></span></div>' +
            '<div class="report-block__body">' + renderBlockAnatomy(b) + '</div></div>';
        }).join('');
      }

      var blocksRoot = $('[data-monthly-blocks]');
      if (blocksRoot) blocksRoot.innerHTML = '';
    }

    document.addEventListener('demo:project-change', function (e) {
      renderMonthly(e.detail.projectId);
    });

    var urlParam = new URLSearchParams(window.location.search).get('project');
    var tabsRoot = $('[data-project-tabs]');
    var defaultId = (urlParam && DEMO_PROJECTS[urlParam]) ? urlParam : ((tabsRoot && tabsRoot.getAttribute('data-default-project')) || 'ecommerce');
    renderMonthly(defaultId);
  }

  function initClientReport() {
    var root = $('[data-client-report]');
    if (!root) return;

    function renderClient(projectId) {
      var p = getProject(projectId);
      var wc = WORKS_CONTENT[projectId];
      var gateEl = $('[data-client-gate]');
      var contentEl = $('[data-client-content]');
      if (gateEl) {
        if (!p.clientReportAvailable) {
          gateEl.hidden = false;
          gateEl.innerHTML = '<div class="client-gate alert alert--warning"><strong>Отчёт ещё не готов для клиента</strong><p>' + p.clientReportReason + '</p><p class="form-hint">Статус: ' + p.stageLabel + ' · Полнота: ' + p.completenessPct + '%</p></div>';
          if (contentEl) contentEl.classList.add('is-gated');
        } else {
          gateEl.hidden = true;
          gateEl.innerHTML = '';
          if (contentEl) contentEl.classList.remove('is-gated');
        }
      }
      $$('[data-client-field]').forEach(function (el) {
        var field = el.getAttribute('data-client-field');
        if (field === 'client') el.textContent = p.client;
        if (field === 'site') el.textContent = p.site;
        if (field === 'period') el.textContent = p.period;
        if (field === 'project') el.textContent = p.name;
        if (field === 'type') el.innerHTML = '<span class="badge badge--type-' + p.typeBadge + '">' + p.typeLabel + '</span>';
        if (field === 'specialist') el.textContent = p.specialist;
        if (field === 'summary') el.innerHTML = p.executiveSummary ? p.executiveSummary.split('\n\n').map(function (para) { return '<p class="client-report__summary">' + para + '</p>'; }).join('') : '<p class="text-muted">—</p>';
        if (field === 'kpi') el.innerHTML = renderKpiGrid(p.kpi);
        if (field === 'traffic' && wc.traffic) el.innerHTML = '<div class="chart-placeholder mb-16">Динамика органического трафика — заглушка</div><p class="client-report__summary">' + wc.traffic + '</p>';
        if (field === 'traffic' && wc.trafficMissing) el.innerHTML = '<p class="text-muted">Блок в подготовке.</p>';
        if (field === 'positions') el.innerHTML = '<div class="chart-placeholder chart-placeholder--sm mb-16">Динамика видимости — заглушка</div><p class="client-report__summary">' + wc.positions + '</p><div class="topvisor-card mt-16"><p class="topvisor-card__title">Отчёт Topvisor</p><a class="btn btn--primary" href="https://example.com/topvisor-demo-report">Открыть Topvisor</a></div>';
        if (field === 'conversions') el.innerHTML = '<p class="client-report__summary">' + wc.conversions + '</p>';
        if (field === 'works-technical') el.innerHTML = formatWorksList(wc.technical);
        if (field === 'works-semantic') el.innerHTML = formatWorksList(wc.semantic);
        if (field === 'works-regional' && wc.regional) el.innerHTML = '<p class="client-report__summary">' + wc.regional + '</p>';
        if (field === 'works-geo' && wc.geo) el.innerHTML = '<p class="client-report__summary">' + wc.geo + '</p>';
        if (field === 'works-trust' && wc.trust) el.innerHTML = '<p class="client-report__summary">' + wc.trust + '</p>';
        if (field === 'risks') el.innerHTML = '<ul class="work-list">' + p.risks.map(function (r) { return '<li>' + r + '</li>'; }).join('') + '</ul>';
        if (field === 'plan') el.innerHTML = '<ul class="work-list">' + p.planNextMonth.map(function (item) { return '<li>' + item + '</li>'; }).join('') + '</ul>';
        if (field === 'weeks') {
          el.innerHTML = p.weeks.filter(function (w) { return !w.notStarted; }).map(function (w, i) {
            return '<div class="weekly-summary-item"><div class="weekly-summary-item__week">Неделя ' + (i + 1) + '</div><p>' + (w.summary ? w.summary.split('.')[0] + '.' : '—') + '</p></div>';
          }).join('');
        }
        if (field === 'version') el.textContent = p.monthlyStatus === 'published' ? 'v1.0-demo · Опубликован 10.07.2026' : 'v0.9-demo · Предпросмотр';
      });
      document.title = 'SEO-отчёт — ' + p.client + ' — ' + p.period;
    }

    function formatWorksList(text) {
      if (!text) return '';
      return '<ul class="work-list">' + text.split('\n').filter(Boolean).map(function (line) {
        return '<li>' + line.replace(/^•\s*/, '') + '</li>';
      }).join('') + '</ul>';
    }

    document.addEventListener('demo:project-change', function (e) {
      renderClient(e.detail.projectId);
    });

    var defaultId = ($('[data-project-tabs]') && $('[data-project-tabs]').getAttribute('data-default-project')) || 'local';
    renderClient(defaultId);
  }

  function initProjectPanels() {
    $$('[data-project-panel]').forEach(function (panel) {
      var id = panel.getAttribute('data-project-panel');
      var p = getProject(id);
      if (!p) return;
      var kpiRoot = $('[data-panel-kpi]', panel);
      if (kpiRoot) kpiRoot.innerHTML = renderKpiGrid(p.kpi);
      var lc = $('[data-panel-lifecycle]', panel);
      if (lc) lc.innerHTML = renderLifecycleStrip(p.lifecycle);
      var pct = $('[data-panel-completeness]', panel);
      if (pct) pct.textContent = p.completenessPct + '%';
      var gate = $('[data-panel-client-gate]', panel);
      if (gate) {
        gate.innerHTML = p.clientReportAvailable
          ? '<span class="badge badge--approved">Client report: доступен</span>'
          : '<span class="badge badge--draft">Client report: не готов</span> <span class="text-muted">' + p.clientReportReason + '</span>';
      }
      var typeBlocks = $('[data-panel-type-blocks]', panel);
      if (typeBlocks) {
        var blocks = TYPE_BLOCKS[id] || [];
        typeBlocks.innerHTML = '<ul class="type-block-list">' + blocks.map(function (b) {
          return '<li><span class="badge ' + statusBadgeClass(b.status) + '">' + blockStatusLabel(b.status) + '</span> ' + b.title + '</li>';
        }).join('') + '</ul>';
      }
      var missing = $('[data-panel-missing]', panel);
      if (missing) {
        missing.innerHTML = p.missingBlocks.length
          ? '<ul class="alert__list">' + p.missingBlocks.map(function (m) { return '<li>' + m + '</li>'; }).join('') + '</ul>'
          : '<p class="form-hint">Все required-блоки заполнены</p>';
      }
      var next = $('[data-panel-next-action]', panel);
      if (next) next.textContent = p.nextAction;
      var risks = $('[data-panel-risks]', panel);
      if (risks) risks.innerHTML = '<ul class="work-list">' + p.risks.map(function (r) { return '<li>' + r + '</li>'; }).join('') + '</ul>';
    });
  }

  function initDashboard() {
    var cardsRoot = $('[data-dashboard-cards]');
    if (!cardsRoot) return;
    var order = ['local', 'ecommerce', 'service'];
    cardsRoot.innerHTML = order.map(function (id) {
      var p = getProject(id);
      var clientBadge = p.clientReportAvailable
        ? '<span class="badge badge--approved">Client: доступен</span>'
        : '<span class="badge badge--revision">Client: не готов</span>';
      var kpiHtml = p.kpi.slice(0, 4).map(function (k) {
        return '<div class="project-card__kpi-item"><span class="text-muted">' + k.label + '</span><strong>' + k.value + '</strong></div>';
      }).join('');
      var missing = p.missingBlocks.slice(0, 2).map(function (m) { return '<li>' + m + '</li>'; }).join('');
      return '<article class="project-card project-card--' + id + '">' +
        '<div class="project-card__header"><div><h3 class="project-card__title">' + p.name + '</h3>' +
        '<p class="project-card__client">' + p.client + '</p></div>' +
        '<span class="badge badge--type-' + p.typeBadge + '">' + p.typeLabel + '</span></div>' +
        '<p><span class="badge ' + statusBadgeClass(p.lifecycle.final === 'published' ? 'published' : (p.lifecycle.w3 === 'active' ? 'active' : 'draft')) + '">' + p.stageLabel + '</span> · ' + p.specialist + '</p>' +
        renderLifecycleStrip(p.lifecycle) +
        '<p class="project-card__meta">' + clientBadge + ' · Полнота: <strong>' + p.completenessPct + '%</strong></p>' +
        (missing ? '<ul class="alert__list project-card__missing">' + missing + '</ul>' : '') +
        '<p class="form-hint"><strong>След. действие:</strong> ' + p.nextAction + '</p>' +
        '<div class="project-card__kpi">' + kpiHtml + '</div>' +
        '<div class="project-card__actions">' +
        '<a href="specialist-workspace.html?project=' + id + '">Заполнить</a>' +
        '<a href="project.html?project=' + id + '">Проект</a>' +
        '<a href="monthly.html?project=' + id + '">Monthly</a>' +
        '<a href="client-report.html?project=' + id + '">Client' + (p.clientReportAvailable ? ' ✓' : '') + '</a></div></article>';
    }).join('');

    var matrix = $('[data-lifecycle-matrix]');
    if (matrix) {
      var rows = order.map(function (id) {
        var p = getProject(id);
        function cell(st) {
          var cls = lifecycleStepClass(st);
          return '<td><span class="lifecycle-cell ' + cls + '">' + lifecycleStepIcon(st) + '</span></td>';
        }
        return '<tr><td>' + p.client + '</td><td><span class="badge badge--type-' + p.typeBadge + '">' + p.typeLabel + '</span></td>' +
          cell(p.lifecycle.w1) + cell(p.lifecycle.w2) + cell(p.lifecycle.w3) + cell(p.lifecycle.final) +
          '<td>' + (p.clientReportAvailable ? '✓' : '—') + '</td><td><a href="project.html?project=' + id + '">→</a></td></tr>';
      }).join('');
      matrix.innerHTML = '<table class="data-table"><thead><tr><th>Проект</th><th>Тип</th><th>W1</th><th>W2</th><th>W3</th><th>Final</th><th>Client</th><th></th></tr></thead><tbody>' + rows + '</tbody></table>';
    }
  }

  function initReviewPanel() {
    var sel = $('[data-review-project-select]');
    if (!sel) return;
    function update() {
      var p = getProject(sel.value);
      var panel = $('[data-review-detail]');
      if (!panel) return;
      $('[data-review-project-name]', panel).textContent = p.client + ' — ' + p.name;
      $('[data-review-specialist]', panel).textContent = p.specialist;
      $('[data-review-status]', panel).innerHTML = '<span class="badge ' + statusBadgeClass(p.monthlyStatus) + '">' + p.monthlyStatusLabel + '</span>';
      var missing = $('[data-review-missing]', panel);
      if (p.missingBlocks.length) {
        missing.innerHTML = '<ul class="alert__list">' + p.missingBlocks.map(function (m) { return '<li>' + m + '</li>'; }).join('') + '</ul>';
      } else {
        missing.innerHTML = '<li>Все обязательные блоки заполнены</li>';
      }
      var blocks = $('[data-review-blocks]', panel);
      if (blocks) {
        var tblocks = TYPE_BLOCKS[sel.value] || [];
        blocks.innerHTML = tblocks.map(function (b) {
          var ok = b.status === 'approved' || b.status === 'published';
          return '<span class="block-chip ' + (ok ? 'block-chip--ok' : 'block-chip--missing') + '">' + (ok ? '✓' : '!') + ' ' + b.title + '</span>';
        }).join('');
      }
      var action = $('[data-review-action]', panel);
      if (action) action.textContent = p.nextAction;
      var notReady = $('[data-review-not-ready]', panel);
      if (notReady) {
        notReady.textContent = p.clientReportAvailable ? 'Готов к публикации клиенту' : p.clientReportReason;
      }
    }
    sel.addEventListener('change', update);
    update();
  }

  function initSpecialistWorkspace() {
    var root = $('[data-specialist-workspace]');
    if (!root) return;

    var projectId = 'ecommerce';
    var stage = 'w3';
    var urlProject = new URLSearchParams(window.location.search).get('project');
    var urlStage = new URLSearchParams(window.location.search).get('stage');
    if (urlProject && DEMO_PROJECTS[urlProject]) projectId = urlProject;
    if (urlStage && ['w1', 'w2', 'w3', 'final'].indexOf(urlStage) !== -1) stage = urlStage;

    function visBadge(v) {
      var map = { client: 'клиенту', internal: 'внутреннее', reviewer: 'проверяющему', 'data-source': 'источник данных', evidence: 'источник данных' };
      return '<span class="visibility-badge visibility-badge--' + v + '">' + (map[v] || v) + '</span>';
    }

    function inclusionBadge(inc) {
      var cls = inc === 'required' ? 'required' : (inc === 'recommended' ? 'recommended' : 'optional');
      var label = inc === 'required' ? 'Required' : (inc === 'recommended' ? 'Recommended' : 'Optional');
      return '<span class="inclusion-badge inclusion-badge--' + cls + '">' + label + '</span>';
    }

    function blockChecksFilled(b) {
      if (b.status === 'published' || b.status === 'approved') return { filled: true, evidence: true, client: true, reviewer: false };
      if (b.status === 'empty') return { filled: false, evidence: false, client: false, reviewer: false };
      if (b.status === 'needs_review') return { filled: true, evidence: !!b.evidence, client: false, reviewer: true };
      return { filled: b.status !== 'empty', evidence: !!b.evidence, client: !!b.clientSummary, reviewer: b.status === 'draft' };
    }

    function render() {
      var p = getProject(projectId);
      var texts = SPECIALIST_TEXTS[projectId] || SPECIALIST_TEXTS.service;
      var workCats = WORK_CHECKLIST[projectId] || WORK_CHECKLIST.service;
      var blocks = TYPE_BLOCKS[projectId] || [];

      $$('[data-project-card]').forEach(function (card) {
        card.classList.toggle('is-selected', card.getAttribute('data-project-card') === projectId);
      });

      $$('[data-stage-btn]').forEach(function (btn) {
        btn.classList.toggle('is-active', btn.getAttribute('data-stage-btn') === stage);
      });

      var meta = $('[data-ws-meta]');
      if (meta) {
        meta.innerHTML = '<span class="badge badge--type-' + p.typeBadge + '">' + p.typeLabel + '</span> ' +
          '<span class="badge ' + statusBadgeClass(p.monthlyStatus) + '">' + p.stageLabel + '</span> ' +
          (p.clientReportAvailable
            ? '<span class="badge badge--approved">Клиентский отчёт: доступен</span>'
            : '<span class="badge badge--revision">Клиентский отчёт: не готов</span>');
      }

      var blocksRoot = $('[data-ws-blocks]');
      if (blocksRoot) {
        blocksRoot.innerHTML = '<div class="block-check-header"><span>Блок</span><span>Заполнен</span><span>Evidence</span><span>Клиент-текст</span><span>Reviewer</span></div>' +
          blocks.map(function (b) {
            var c = blockChecksFilled(b);
            return '<div class="block-check-row">' +
              '<div class="block-check-row__title">' + inclusionBadge(b.inclusion) + ' ' + b.title + '</div>' +
              '<div><input type="checkbox" ' + (c.filled ? 'checked' : '') + ' disabled></div>' +
              '<div><input type="checkbox" ' + (c.evidence ? 'checked' : '') + ' disabled></div>' +
              '<div><input type="checkbox" ' + (c.client ? 'checked' : '') + ' disabled></div>' +
              '<div><input type="checkbox" ' + (c.reviewer ? 'checked' : '') + ' disabled></div></div>';
          }).join('');
      }

      var workRoot = $('[data-ws-works]');
      if (workRoot) {
        workRoot.innerHTML = Object.keys(WORK_CATEGORY_LABELS).map(function (catKey) {
          var items = workCats[catKey] || [];
          if (!items.length) return '';
          return '<div class="form-card"><div class="form-card__header">' + WORK_CATEGORY_LABELS[catKey] + '</div><div class="form-card__body">' +
            items.map(function (item) {
              return '<div class="work-check-item">' +
                '<input type="checkbox" ' + (item.checked ? 'checked' : '') + ' data-ws-work-check>' +
                '<div><strong>' + item.label + '</strong><div class="work-check-item__purpose">' + item.purpose + '</div></div>' +
                '<div>' + visBadge(item.visibility) + ' <button type="button" class="btn btn--ghost" style="padding:2px 6px;font-size:11px;" data-demo-action="add-work">+ заметка</button></div></div>';
            }).join('') + '</div></div>';
        }).join('');
      }

      var textFields = {
        'client-summary': texts.clientSummary,
        'changes': texts.changes,
        'interpretation': texts.interpretation,
        'blockers': texts.blockers,
        'next-plan': texts.nextPlan,
        'internal-note': texts.internalNote
      };
      Object.keys(textFields).forEach(function (key) {
        var el = $('[data-ws-text="' + key + '"]');
        if (el) el.value = textFields[key] || '';
      });

      var kpiRoot = $('[data-ws-kpi]');
      if (kpiRoot) {
        var kpis = KPI_INPUTS[projectId] || [];
        kpiRoot.innerHTML = '<div class="kpi-input-grid">' + kpis.map(function (k, i) {
          return '<div class="kpi-input-card">' +
            '<div class="form-group"><label class="form-label">Метрика</label><input class="mock-input" value="' + k.metric + '"></div>' +
            '<div class="form-group"><label class="form-label">Значение</label><input class="mock-input" value="' + k.value + '"></div>' +
            '<div class="form-group"><label class="form-label">Период</label><input class="mock-input" value="' + k.period + '"></div>' +
            '<div class="form-group"><label class="form-label">Источник</label><input class="mock-input" value="' + k.source + '"></div>' +
            '<div class="form-group"><label class="form-label">Интерпретация</label><textarea class="mock-textarea" rows="2">' + k.interpretation + '</textarea></div>' +
            '<div class="toggle-row"><input type="checkbox" id="kpi-vis-' + i + '" ' + (k.clientVisible ? 'checked' : '') + '><label for="kpi-vis-' + i + '">Видно клиенту</label></div></div>';
        }).join('') + '</div>';
      }

      var evRoot = $('[data-ws-evidence]');
      if (evRoot) {
        var evItems = EVIDENCE_ITEMS[projectId] || [];
        evRoot.innerHTML = evItems.map(function (e, i) {
          return '<div class="report-source-card">' +
            '<div class="report-source-card__row">' +
            '<div class="form-group"><label class="form-label">Название</label><input class="mock-input" value="' + e.title + '"></div>' +
            '<div class="form-group"><label class="form-label">Источник</label><input class="mock-input" value="' + e.source + '"></div></div>' +
            '<div class="form-group"><label class="form-label">Связанный блок</label><input class="mock-input" value="' + e.block + '"></div>' +
            '<div class="form-group"><label class="form-label">Ссылка</label><input class="mock-input" type="url" value="' + e.link + '"></div>' +
            '<div class="toggle-row"><input type="checkbox" id="ev-vis-' + i + '" ' + (e.clientVisible ? 'checked' : '') + '><label for="ev-vis-' + i + '">Видно клиенту</label></div></div>';
        }).join('') +
        '<div class="form-group mt-16"><label class="form-label">Topvisor report link</label><input class="mock-input" type="url" value="https://example.com/topvisor-demo-report"></div>';
      }

      var readinessRoot = $('[data-ws-readiness]');
      if (readinessRoot) {
        var items = [];
        var canSend = false;
        if (projectId === 'local') {
          items = [
            { ok: true, text: 'Обязательные блоки заполнены' },
            { ok: true, text: 'Клиентский текст проверен' },
            { ok: true, text: 'Внутренние заметки не попадут в client report' },
            { ok: true, text: 'Подтверждения приложены' },
            { ok: true, text: 'Reviewer approval получен' }
          ];
          canSend = true;
        } else if (projectId === 'ecommerce') {
          items = [
            { ok: false, text: 'Обязательные блоки: Traffic, Orders не готовы' },
            { ok: false, text: 'Клиентский текст: executive summary — черновик' },
            { ok: true, text: 'Внутренние caveats отмечены' },
            { ok: false, text: 'Topvisor export не приложен' },
            { ok: false, text: 'W3 review pending' }
          ];
        } else {
          items = [
            { ok: false, text: 'Только Week 1 — monthly shell' },
            { ok: false, text: 'Executive summary пустой' },
            { ok: true, text: 'Внутренние заметки отделены' },
            { ok: false, text: 'Evidence частично' },
            { ok: false, text: 'Reviewer: не в очереди' }
          ];
        }
        var remain = $('[data-ws-remain]');
        if (remain) {
          remain.innerHTML = p.missingBlocks.length
            ? '<ul class="alert__list">' + p.missingBlocks.map(function (m) { return '<li>' + m + '</li>'; }).join('') + '</ul>'
            : '<p class="form-hint">Все обязательные блоки закрыты.</p>';
        }
        readinessRoot.innerHTML = items.map(function (item) {
          return '<div class="readiness-item readiness-item--' + (item.ok ? 'ok' : 'fail') + '">' +
            '<span class="readiness-item__icon">' + (item.ok ? '✓' : '✗') + '</span><span>' + item.text + '</span></div>';
        }).join('') +
        '<div class="readiness-panel__verdict ' + (canSend ? 'readiness-panel__verdict--ready' : 'readiness-panel__verdict--not-ready') + '">' +
        (canSend ? 'Отчёт можно отправить клиенту (демо: Local published)' : 'Отчёт нельзя отправить клиенту — ' + p.stageLabel) + '</div>';
      }
    }

    $$('[data-project-card]').forEach(function (card) {
      card.addEventListener('click', function () {
        projectId = card.getAttribute('data-project-card');
        render();
      });
    });

    $$('[data-stage-btn]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        stage = btn.getAttribute('data-stage-btn');
        render();
      });
    });

    var uploadZone = $('[data-upload-zone]');
    if (uploadZone) {
      uploadZone.addEventListener('click', function () {
        var msg = $('[data-demo-feedback]');
        if (msg) {
          msg.textContent = 'Демо: зона загрузки — файлы не принимаются. В production здесь будет upload скриншота.';
          msg.hidden = false;
        }
      });
    }

    var previewBtn = $('[data-ws-preview]');
    if (previewBtn) {
      previewBtn.addEventListener('click', function (e) {
        e.preventDefault();
        window.open('client-report.html?project=' + projectId, '_blank');
        var msg = $('[data-demo-feedback]');
        if (msg) { msg.textContent = 'Демо: предпросмотр клиентского отчёта открыт.'; msg.hidden = false; }
      });
    }

    render();
  }

  // Collapsible
  $$('[data-collapsible-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var target = document.getElementById(btn.getAttribute('data-collapsible-toggle'));
      if (!target) return;
      target.hidden = !target.hidden;
      btn.textContent = target.hidden ? 'Показать приложение' : 'Скрыть приложение';
    });
  });

  // Demo actions
  $$('[data-demo-action]').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (btn.tagName === 'A' && btn.getAttribute('href')) return;
      e.preventDefault();
      var action = btn.getAttribute('data-demo-action');
      var msg = document.querySelector('[data-demo-feedback]');
      if (msg) {
        var labels = {
          approve: 'Демо: отчёт отмечен как утверждённый (без сохранения).',
          revision: 'Демо: запрос на доработку отправлен (без сохранения).',
          save: 'Демо: черновик сохранён локально в сессии (без backend — данные не персистятся).',
          submit: 'Демо: отчёт отправлен на проверку руководителю SEO (без сохранения).',
          preview: 'Демо: открывается предпросмотр клиентского отчёта в новой вкладке.',
          'add-evidence': 'Демо: добавлено поле подтверждения (без загрузки файла).',
          'add-work': 'Демо: добавлена строка в чек-лист работ (без сохранения).',
          'add-screenshot': 'Демо: зона загрузки — файлы не принимаются в static demo.'
        };
        msg.textContent = labels[action] || 'Демо-действие выполнено (без сохранения).';
        msg.hidden = false;
      }
    });
  });

  // Report block toggle
  $$('[data-block-toggle]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var block = btn.closest('.report-block');
      if (block) block.classList.toggle('is-collapsed');
    });
  });

  initNav();
  initDashboard();
  initProjectTabs();
  initProjectPanels();
  initWeeklyEditor();
  initMonthlyEditor();
  initClientReport();
  initReviewPanel();
  initSpecialistWorkspace();
})();
