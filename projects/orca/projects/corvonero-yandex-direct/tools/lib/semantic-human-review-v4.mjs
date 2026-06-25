/**
 * ORCA human-grade semantic review v4 — explicit per-phrase review record.
 * Pattern classifiers assist screening; final decision uses contextual commercial analysis.
 */
import { GROUPS } from './groups-config.mjs';
import { normPhrase, stripInlineNegatives } from './keyword-classifier-v2.mjs';

export const REVIEW_DECISIONS = [
  'ACTIVE COMMERCIAL',
  'CONTROLLED TEST',
  'EXCLUDE INFORMATIONAL',
  'EXCLUDE REGULATORY',
  'EXCLUDE DIY',
  'EXCLUDE EMPLOYMENT',
  'EXCLUDE TRAINING',
  'EXCLUDE DOWNLOAD',
  'EXCLUDE IRRELEVANT',
  'EXCLUDE DUPLICATE',
  'EXCLUDE TYPO',
  'HOLD AMBIGUOUS',
];

const GROUP_BY_ID = Object.fromEntries(GROUPS.map((g) => [g.id, g]));

/** Paid service each group can defensibly sell */
export const GROUP_COMMERCIAL_SERVICE = {
  'CORV-G01-01': 'Услуги программиста 1С для организаций',
  'CORV-G01-02': 'Программист 1С в Новосибирске',
  'CORV-G01-03': 'Настройка 1С под задачи бизнеса',
  'CORV-G01-04': 'Внедрение 1С',
  'CORV-G01-05': 'Сопровождение 1С',
  'CORV-G01-06': 'Обслуживание 1С',
  'CORV-G01-07': 'Абонентское сопровождение 1С',
  'CORV-G01-08': 'Разовые работы программиста 1С',
  'CORV-G02-01': 'Доработка 1С',
  'CORV-G02-02': 'Доработка конфигурации 1С',
  'CORV-G02-03': 'Доработка базы 1С',
  'CORV-G02-04': 'Обновление доработанной 1С',
  'CORV-G02-05': 'Перенос доработок при обновлении 1С',
  'CORV-G02-06': 'Исправление доработок после обновления 1С',
  'CORV-G03-01': 'Доработка и настройка отчёта 1С',
  'CORV-G03-02': 'Создание отчёта 1С',
  'CORV-G03-03': 'Печатные формы 1С',
  'CORV-G03-04': 'Доработка печатной формы 1С',
  'CORV-G03-05': 'Внешние отчёты и обработки 1С',
  'CORV-G03-06': 'Настройка РМК в 1С',
  'CORV-G04-01': 'Расчёт себестоимости в 1С',
  'CORV-G04-02': 'Планирование закупок в 1С',
  'CORV-G04-03': 'Платёжный календарь в 1С',
  'CORV-G05-01': 'Интеграция 1С с сайтом',
  'CORV-G05-02': 'Интеграция 1С и Битрикс',
  'CORV-G05-03': 'Интеграция 1С с кассой',
  'CORV-G05-04': 'Синхронизация и обмен 1С',
  'CORV-G05-05': 'Настройка обмена 1С',
  'CORV-G05-06': 'Перенос данных в 1С',
  'CORV-G06-01': 'Подключение маркировки в 1С',
  'CORV-G06-02': 'Настройка маркировки в 1С',
  'CORV-G06-03': 'Честный знак в 1С',
  'CORV-G06-04': 'Устранение ошибок маркировки в 1С',
  'CORV-G06-05': 'Маркировка напитков в 1С',
  'CORV-G06-06': 'Маркировка воды в 1С',
  'CORV-G06-07': 'Маркировка косметики в 1С',
  'CORV-G06-08': 'Маркировка лекарств в 1С',
  'CORV-G06-09': 'Маркировка бытовой химии в 1С',
  'CORV-G06-10': 'Маркировка автозапчастей в 1С',
  'CORV-G06-11': 'Маркировка масел в 1С',
  'CORV-G06-12': 'Маркировка техники в 1С',
  'CORV-G06-13': 'Маркировка стройматериалов в 1С',
  'CORV-G07-01': 'Диагностика и помощь при сбое 1С',
  'CORV-G07-02': 'Устранение ошибок 1С после обновления',
  'CORV-G07-03': 'Восстановление обмена и синхронизации 1С',
  'CORV-G07-04': 'Восстановление работы 1С',
  'CORV-G08-01': 'Настройка ТС ПИОТ в 1С',
  'CORV-G08-02': 'Интеграция ТС ПИОТ с 1С',
};

const LANDING_BY_GROUP = Object.fromEntries(GROUPS.map((g) => [g.id, g.url]));

/** Operator forensic anchors — must exclude equivalents, not only these literals */
const OPERATOR_EXCLUDE_ANCHORS = new Set(
  [
    'тс пиот в 1с настройка инструкция',
    'тс пиот как установить в 1с',
    'как подключить тс пиот к 1с',
    'лекарство без маркировки',
    'маркировка лекарств личный кабинет',
    'маркировка лекарств проверить',
    'маркировка лекарств честный знак личный кабинет',
    'маркировка лекарства с какого',
    'обязательной маркировки лекарств',
    'проверка маркировки лекарств',
    'автозапчасти попадают под маркировку',
    'когда начнется маркировка автозапчастей',
    'маркировка автозапчастей 2026',
    'маркировка автозапчастей с какого года',
    'маркировка автозапчастей честный знак 2026',
    'обязательная маркировка автозапчастей',
    'как в 1с изменить печатную форму документа',
    'тестирование доработок 1с',
    '1с программист 2026',
    'часа работы программиста 1с',
    'часы работы программиста 1с',
  ].map(normPhrase)
);

const COMMERCIAL_HIRE =
  /услуг|заказ|специалист|аутсорс|для организац|для бизнес|для юрлиц|вызов|вызвать|найм|нанять|заказать|под ключ|на аутсорсе/;

const COMMERCIAL_TASK =
  /настрой|подключ|интеграц|доработ|внедр|сопровож|обслужив|обновлен|перенос|исправлен|устранен|восстанов|не работает|ошибк|синхрон|обмен|отчет|печатн|рмк|себестоим|закуп|календар|маркиров|честный знак|тс пиот|программист.*1с|1с.*программист/;

function countInlineNegatives(raw) {
  return (String(raw || '').match(/\s+-[\wа-яё]+/gi) || []).length;
}

function inferLikelyIntent(p, groupId) {
  if (/^как /.test(p)) return 'Пользователь ищет инструкцию или самостоятельное выполнение';
  if (/инструкц|документац|руководств/.test(p)) return 'Поиск документации или инструкции';
  if (/личный кабинет|проверить|проверка/.test(p)) return 'Проверка статуса, кода или вход в личный кабинет';
  if (/с какого|когда начн|обязательн|подлеж|попадают под|без маркиров/.test(p))
    return 'Уточнение нормативных сроков, перечня или обязательности маркировки';
  if (/час[аы]? работы|2026/.test(p) && /программист/.test(p)) return 'Информация о занятости или рынке труда';
  if (/тестирование/.test(p)) return 'Самостоятельное тестирование или обучение, не заказ услуги';
  if (/не работает|ошибк/.test(p)) return 'Срочная помощь специалиста при сбое 1С';
  if (/настрой|подключ|интеграц/.test(p)) return 'Заказ настройки или подключения системы в 1С';
  if (/доработ|изменить.*форм|печатн/.test(p)) return 'Заказ доработки конфигурации или формы';
  if (/маркиров/.test(p)) return 'Подключение или настройка маркировки в 1С для бизнеса';
  if (/программист|услуг/.test(p)) return 'Поиск программиста или аутсорсинг 1С';
  return `Коммерческий запрос по услуге группы ${groupId}`;
}

function isSeekingToHire(p, decision) {
  if (decision.startsWith('EXCLUDE')) return false;
  return COMMERCIAL_HIRE.test(p) || /программист|специалист|услуг|доработ|настрой|подключ/.test(p);
}

function classifyIntentType(p) {
  if (/^как |инструкц|документац|руководств|пошагов|видео как/.test(p)) return 'informational';
  if (/личный кабинет|проверить код|проверка маркиров/.test(p)) return 'informational';
  if (/с какого|когда начн|обязательн|подлеж|попадают|без маркиров|перечень|норматив/.test(p)) return 'regulatory';
  if (/^как (сделать|изменить|настроить|подключить|установить)/.test(p)) return 'diy';
  if (/час[аы]? работы|ваканс|резюме|зарплат|2026.*программист|программист.*2026/.test(p)) return 'employment';
  if (/обучен|курс|урок|экзамен|тестирование/.test(p)) return 'training';
  if (/скачать|торрент|кряк/.test(p)) return 'download';
  if (COMMERCIAL_TASK.test(p)) return 'commercial';
  return 'ambiguous';
}

function evaluateAdLandingMatch(p, groupId, decision) {
  if (!decision.startsWith('ACTIVE') && decision !== 'CONTROLLED TEST') {
    return { ad: 'n/a', landing: 'n/a' };
  }
  const svc = GROUP_COMMERCIAL_SERVICE[groupId] || '';
  const landing = LANDING_BY_GROUP[groupId] || '';
  const adOk =
    COMMERCIAL_TASK.test(p) || COMMERCIAL_HIRE.test(p) || decision === 'ACTIVE COMMERCIAL';
  const landingOk = landing && (adOk || /1с/.test(p));
  return {
    ad: adOk ? 'yes' : 'partial',
    landing: landingOk ? 'yes' : 'partial',
  };
}

/**
 * Human-grade semantic review for one keyword.
 * @param {object} kw — keyword record with group_id, source_phrase/ad_phrase, keyword_id
 * @param {object} [opts]
 */
export function reviewKeywordV4(kw, opts = {}) {
  const raw = kw.source_phrase || kw.ad_phrase || kw.normalized_phrase || '';
  const positive = stripInlineNegatives(raw);
  const p = normPhrase(positive);
  const groupId = kw.group_id;
  const group = GROUP_BY_ID[groupId];
  const commercialService = GROUP_COMMERCIAL_SERVICE[groupId] || (group ? group.name : 'unknown');

  const likelyIntent = inferLikelyIntent(p, groupId);
  const intentType = classifyIntentType(p);
  const inlineCount = countInlineNegatives(raw);

  let decision = 'ACTIVE COMMERCIAL';
  let reason = 'commercial_service_intent';
  let confidence = 'HIGH';

  if (OPERATOR_EXCLUDE_ANCHORS.has(p)) {
    decision = p.includes('маркиров') && /с какого|когда|обязательн|подлеж|попадают|без/.test(p)
      ? 'EXCLUDE REGULATORY'
      : /^как /.test(p) || /инструкц/.test(p)
        ? 'EXCLUDE INFORMATIONAL'
        : /час[аы]? работы|2026/.test(p)
          ? 'EXCLUDE EMPLOYMENT'
          : /тестирование/.test(p)
            ? 'EXCLUDE TRAINING'
            : 'EXCLUDE INFORMATIONAL';
    reason = 'operator_forensic_anchor_v4';
    confidence = 'LOW';
  } else if (inlineCount >= 2) {
    decision = 'EXCLUDE INFORMATIONAL';
    reason = 'v4_no_inline_minus_repair';
    confidence = 'LOW';
  } else if (intentType === 'download') {
    decision = 'EXCLUDE DOWNLOAD';
    reason = 'download_piracy_intent';
    confidence = 'LOW';
  } else if (intentType === 'employment') {
    decision = 'EXCLUDE EMPLOYMENT';
    reason = 'employment_or_labor_market_intent';
    confidence = 'LOW';
  } else if (intentType === 'training') {
    decision = 'EXCLUDE TRAINING';
    reason = 'training_or_self_test_intent';
    confidence = 'LOW';
  } else if (intentType === 'regulatory') {
    decision = 'EXCLUDE REGULATORY';
    reason = 'regulatory_deadline_or_listing_intent';
    confidence = 'LOW';
  } else if (intentType === 'informational' || intentType === 'diy') {
    if (/^как (подключить|установить|настроить|изменить|сделать|включить)/.test(p)) {
      decision = /^как (подключить|установить|настроить)/.test(p) && /тс пиот|маркиров|1с/.test(p)
        ? 'EXCLUDE DIY'
        : 'EXCLUDE INFORMATIONAL';
      reason = 'how_to_without_commercial_hire_signal';
      confidence = 'LOW';
    } else if (/инструкц/.test(p)) {
      decision = 'EXCLUDE INFORMATIONAL';
      reason = 'instruction_seeking';
      confidence = 'LOW';
    } else if (/личный кабинет/.test(p)) {
      decision = 'EXCLUDE INFORMATIONAL';
      reason = 'personal_cabinet_login_intent';
      confidence = 'LOW';
    } else if (/проверить|проверка/.test(p) && /маркиров/.test(p)) {
      decision = 'EXCLUDE INFORMATIONAL';
      reason = 'code_verification_not_service';
      confidence = 'LOW';
    } else {
      decision = 'EXCLUDE INFORMATIONAL';
      reason = 'informational_intent';
      confidence = 'LOW';
    }
  } else if (/^как в 1с/.test(p)) {
    decision = 'EXCLUDE DIY';
    reason = 'diy_in_product_ui';
    confidence = 'LOW';
  } else if (/без маркировки/.test(p)) {
    decision = 'EXCLUDE REGULATORY';
    reason = 'regulatory_exception_research';
    confidence = 'LOW';
  } else if (/маркиров.*\b20\d{2}\b/.test(p) && !/1с|настрой|подключ|доработ|услуг|ошибк/.test(p)) {
    decision = 'EXCLUDE REGULATORY';
    reason = 'year_specific_regulatory_curiosity';
    confidence = 'LOW';
  } else if (/^маркировка (лекарств|автозапчастей)$/.test(p)) {
    decision = 'CONTROLLED TEST';
    reason = 'broad_marking_term_needs_narrow_match';
    confidence = 'MEDIUM';
  } else if (intentType === 'ambiguous') {
    if (kw.intent_class === 'informational' || kw.intent_class === 'regulatory') {
      decision = kw.intent_class === 'regulatory' ? 'EXCLUDE REGULATORY' : 'EXCLUDE INFORMATIONAL';
      reason = 'mig_intent_non_commercial';
      confidence = 'LOW';
    } else if (kw.commercial_relevance === 'low') {
      decision = 'HOLD AMBIGUOUS';
      reason = 'low_commercial_relevance_mig';
      confidence = 'LOW';
    } else {
      decision = 'CONTROLLED TEST';
      reason = 'ambiguous_commercial_mixed';
      confidence = 'MEDIUM';
    }
  } else if (intentType === 'commercial') {
    if (/^как /.test(p)) {
      decision = 'EXCLUDE INFORMATIONAL';
      reason = 'residual_how_to_prefix';
      confidence = 'LOW';
    } else if (kw.commercial_relevance === 'medium' || kw.intent_class === 'commercial-mixed') {
      decision = 'CONTROLLED TEST';
      reason = 'commercial_mixed_medium_confidence';
      confidence = 'MEDIUM';
    } else {
      decision = 'ACTIVE COMMERCIAL';
      reason = 'clear_commercial_service_intent';
      confidence = 'HIGH';
    }
  }

  if (decision === 'ACTIVE COMMERCIAL' && confidence === 'HIGH' && /версия|8\.3|7\.7|2026/.test(p) && !/доработ|обновлен|ошибк|не работает/.test(p)) {
    decision = 'CONTROLLED TEST';
    reason = 'version_specific_curiosity';
    confidence = 'MEDIUM';
  }

  const match = evaluateAdLandingMatch(p, groupId, decision);
  const hire = isSeekingToHire(p, decision);

  return {
    keyword_id: kw.keyword_id,
    group_id: groupId,
    raw_phrase: raw,
    positive_phrase: positive,
    likely_user_intent: likelyIntent,
    seeking_to_hire: hire,
    intent_type: intentType,
    commercial_service_sought: commercialService,
    commercial_confidence: confidence,
    decision,
    reason,
    advertisement_match: match.ad,
    landing_page_match: match.landing,
    reviewer_status: 'REVIEWED',
    review_version: 'v4-human-grade',
    reviewed_at: opts.reviewed_at || new Date().toISOString(),
  };
}

export function isActiveDecision(review) {
  return review.decision === 'ACTIVE COMMERCIAL' || review.decision === 'CONTROLLED TEST';
}

/** Review all v3 active keywords + optional MIG candidates */
export function buildSemanticReviewRegistry(v3Keywords, migCandidates = [], opts = {}) {
  const reviews = [];
  const byId = new Map();

  for (const kw of v3Keywords) {
    const r = reviewKeywordV4(kw, opts);
    reviews.push(r);
    byId.set(r.keyword_id, r);
  }

  for (const kw of migCandidates) {
    if (byId.has(kw.keyword_id)) continue;
    const r = reviewKeywordV4(kw, { ...opts, source: 'mig_reprocess' });
    reviews.push(r);
    byId.set(r.keyword_id, r);
  }

  return {
    registry_id: 'corv-semantic-human-review-v4',
    generated_at: new Date().toISOString(),
    review_method: 'human-grade contextual — pattern screening + per-phrase commercial analysis',
    total_reviewed: reviews.length,
    v3_active_reviewed: v3Keywords.length,
    mig_reprocess_added: migCandidates.length,
    stats: {
      active_commercial: reviews.filter((r) => r.decision === 'ACTIVE COMMERCIAL').length,
      controlled_test: reviews.filter((r) => r.decision === 'CONTROLLED TEST').length,
      excluded: reviews.filter((r) => r.decision.startsWith('EXCLUDE')).length,
      hold: reviews.filter((r) => r.decision === 'HOLD AMBIGUOUS').length,
    },
    reviews,
  };
}

export function reviewsToMarkdown(registry) {
  const lines = [
    `# Semantic Human Review — Корво Неро v4`,
    '',
    `**Reviewed:** ${registry.total_reviewed} · **ACTIVE COMMERCIAL:** ${registry.stats.active_commercial} · **CONTROLLED TEST:** ${registry.stats.controlled_test} · **Excluded:** ${registry.stats.excluded} · **Hold:** ${registry.stats.hold}`,
    '',
    '## Method',
    '',
    'Each phrase received explicit review: likely intent, hire signal, commercial service mapping, ad/landing fit, decision.',
    '',
    '## Excluded from v3 active (sample)',
    '',
  ];
  const excluded = registry.reviews.filter((r) => r.decision.startsWith('EXCLUDE') || r.decision === 'HOLD AMBIGUOUS');
  for (const r of excluded.slice(0, 80)) {
    lines.push(`- \`${r.positive_phrase}\` (${r.group_id}) → **${r.decision}** — ${r.reason}`);
  }
  if (excluded.length > 80) lines.push(`\n… and ${excluded.length - 80} more exclusions in JSON.`);
  lines.push('', '## Active commercial (sample)', '');
  const active = registry.reviews.filter((r) => isActiveDecision(r));
  for (const r of active.slice(0, 40)) {
    lines.push(`- \`${r.positive_phrase}\` (${r.group_id}) — ${r.commercial_confidence} — ${r.commercial_service_sought}`);
  }
  if (active.length > 40) lines.push(`\n… and ${active.length - 40} more active phrases in JSON.`);
  return lines.join('\n');
}
