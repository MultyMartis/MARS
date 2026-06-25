/**
 * Forensic keyword classification v2 — one status per phrase.
 */

export const CLASSIFICATION_STATUSES = [
  'KEEP',
  'KEEP_TEST',
  'EXCLUDE_INFORMATIONAL',
  'EXCLUDE_DIY',
  'EXCLUDE_EMPLOYMENT',
  'EXCLUDE_TRAINING',
  'EXCLUDE_DOWNLOAD',
  'EXCLUDE_REGULATORY',
  'EXCLUDE_GEO_IRRELEVANT',
  'EXCLUDE_IRRELEVANT',
  'EXCLUDE_TYPO_UNKNOWN',
  'EXCLUDE_DUPLICATE',
  'DEFER_AMBIGUOUS',
];

/** Explicit operator-flagged phrases — always exclude unless commercial override documented */
const EXPLICIT_EXCLUDE = new Set(
  [
    'как стать программистом 1с',
    'какие автозапчасти подлежат маркировке',
    'какие автозапчасти подлежат маркировке честный знак',
    'маркировка автозапчастей сроки',
    'как в 1с настроить маркировку товара',
    'как настроить маркировку в 1с бухгалтерия',
    'как настроить маркировку в 1с розница',
    'как настроить маркировку в 1с ут',
    'как изменить печатную форму в 1с',
    'как сделать печатную форму в 1с',
    'как настроить печатную форму в 1с',
    'знак маркировки на лекарствах',
    'лекарства подлежащие маркировке',
    'исмет маркировка лекарств',
  ].map(normPhrase)
);

/** Commercial hire signals — allow despite DIY-ish tokens */
const COMMERCIAL_HIRE_SIGNALS =
  /услуг|заказ|специалист|аутсорс|для организац|для бизнес|для юрлиц|под ключ$|на аутсорсе|вызов|вызвать|найм|нанять|заказать/;

export function normPhrase(s) {
  return String(s || '')
    .toLowerCase()
    .replace(/ё/g, 'е')
    .replace(/\s+/g, ' ')
    .trim();
}

/** Strip inline minus words for classification */
export function stripInlineNegatives(phrase) {
  return normPhrase(phrase.replace(/\s+-[\wа-яё]+/gi, ''));
}

function testAny(patterns, p) {
  return patterns.some((re) => re.test(p));
}

const EMPLOYMENT_PATTERNS = [
  /ваканс/i,
  /резюме/,
  /зарплат/,
  /собеседован/,
  /стажер/,
  /стажировк/,
  /без опыта/,
  /^работа программист/,
  /^работа 1с/,
  /^работа на 1с/,
  /^работа сопровождение/,
  /удаленная работа программист/,
  /удалённая работа программист/,
  /\bhh\.ru\b/,
  /\bhh\b/,
  /superjob/,
  /работодател/,
  /трудоустройств/,
  /как стать программист/,
  /программист.*бесплатно/,
  /бесплатно.*программист/,
];

const TRAINING_PATTERNS = [
  /обучен/i,
  /\bкурс\b/,
  /\bкурсы\b/,
  /урок/i,
  /экзамен/,
  /сертифик/i,
  /с нуля/,
  /школ/i,
  /учебник/,
  /учиться/,
  /профессия/,
  /диплом/,
  /курсовая/,
  /реферат/,
  /студент/,
  /видеоурок/,
];

const DOWNLOAD_PATTERNS = [/скачать/, /торрент/, /кряк/, /\bcrack\b/, /torrent/, /демо верс/, /ключ активации/, /бесплатно скачать/];

const DIY_PATTERNS = [/своими руками/, /самостоятельно/];

const INFORMATIONAL_PATTERNS = [
  /^что такое/,
  /как работает/,
  /\bинструкция\b/,
  /\bдокументация\b/,
  /\bфорум\b/,
  /\bpdf\b/,
  /\bкнига\b/,
  /\bруководство\b/,
  /^как (сделать|изменить)/,
  /^как настроить/,
  /^как в 1с настроить/,
  /^как подключить маркировку/,
  /какие (товары|автозапчасти|лекарства)/,
  /подлеж.*маркиров/,
  /маркиров.*подлеж/,
  /сроки.*маркиров/,
  /маркиров.*сроки/,
  /список маркируем/,
  /знак маркировки на лекарствах/,
  /лекарства подлежащие/,
  /исмет маркировка/,
  /код маркировки лекарства/,
  /автозапчасти и комплектующие транспортных/,
  /комплектующие транспортных средств маркировка/,
];

const REGULATORY_PATTERNS = [/обязательн.*маркиров.*срок/, /перечень маркируем/, /норматив.*маркиров/];

const GEO_PATTERNS = [/москва/, /санкт-петербург/, /екатеринбург/, /краснодар/, /\bспб\b/];

/** Seeds and head terms that are valid commercial even if short */
const COMMERCIAL_HEAD_TERMS = new Set(
  [
    'программист 1с',
    'услуги программиста 1с',
    'настройка 1с',
    'внедрение 1с',
    'сопровождение 1с',
    'доработка 1с',
    '1с не работает',
    'честный знак 1с',
    'тс пиот 1с',
  ].map(normPhrase)
);

/**
 * @param {object} k keyword record from MIG registry
 * @returns {{ status: string, reason: string, keep_test?: boolean }}
 */
export function classifyKeywordV2(k) {
  const raw = k.source_phrase || k.normalized_phrase || '';
  const p = stripInlineNegatives(raw);

  if (!p || p.length < 3) {
    return { status: 'EXCLUDE_TYPO_UNKNOWN', reason: 'empty_or_too_short' };
  }

  if (EXPLICIT_EXCLUDE.has(p)) {
    return { status: 'EXCLUDE_INFORMATIONAL', reason: 'operator_explicit_list' };
  }

  const commercialOverride =
    COMMERCIAL_HEAD_TERMS.has(p) ||
    (COMMERCIAL_HIRE_SIGNALS.test(p) && !testAny(EMPLOYMENT_PATTERNS, p));

  if (!commercialOverride) {
    if (testAny(EMPLOYMENT_PATTERNS, p) && !/не работает/.test(p)) {
      return { status: 'EXCLUDE_EMPLOYMENT', reason: 'employment_signal' };
    }
    if (testAny(TRAINING_PATTERNS, p) && !/настройк|доработ/.test(p)) {
      return { status: 'EXCLUDE_TRAINING', reason: 'training_signal' };
    }
    if (testAny(DOWNLOAD_PATTERNS, p)) {
      return { status: 'EXCLUDE_DOWNLOAD', reason: 'download_signal' };
    }
    if (testAny(DIY_PATTERNS, p)) {
      return { status: 'EXCLUDE_DIY', reason: 'diy_signal' };
    }
    if (testAny(INFORMATIONAL_PATTERNS, p)) {
      return { status: 'EXCLUDE_INFORMATIONAL', reason: 'informational_diy_pattern' };
    }
    if (testAny(REGULATORY_PATTERNS, p)) {
      return { status: 'EXCLUDE_REGULATORY', reason: 'regulatory_informational' };
    }
  }

  if (testAny(GEO_PATTERNS, p) && !/новосибирск/.test(p)) {
    return { status: 'EXCLUDE_GEO_IRRELEVANT', reason: 'foreign_geo' };
  }

  if (k.intent_class === 'regulatory' && k.commercial_relevance !== 'high') {
    return { status: 'EXCLUDE_REGULATORY', reason: 'regulatory_non_service' };
  }

  const nc = k.noise_classes || [];
  const onlyNoise =
    nc.length > 0 &&
    nc.every((n) => ['job-seeking', 'training', 'salary', 'remote-work', 'informational'].includes(n));
  if (onlyNoise && k.intent_class !== 'direct-commercial' && k.intent_class !== 'troubleshooting') {
    return { status: 'EXCLUDE_EMPLOYMENT', reason: 'noise_classes_only' };
  }

  if (
    k.intent_class === 'direct-commercial' ||
    k.intent_class === 'troubleshooting' ||
    (k.intent_class === 'commercial-mixed' && k.commercial_relevance !== 'low')
  ) {
    if (k.commercial_relevance === 'medium' && k.intent_class === 'commercial-mixed' && /как /.test(p)) {
      return { status: 'KEEP_TEST', reason: 'commercial_mixed_test', keep_test: true };
    }
    return { status: 'KEEP', reason: 'commercial_intent' };
  }

  if (k.intent_class === 'commercial-mixed') {
    return { status: 'DEFER_AMBIGUOUS', reason: 'mixed_low_commercial' };
  }

  if (k.intent_class === 'informational') {
    return { status: 'EXCLUDE_INFORMATIONAL', reason: 'intent_informational' };
  }

  return { status: 'EXCLUDE_IRRELEVANT', reason: 'non_commercial' };
}

export function isActiveClassification(cls) {
  return cls.status === 'KEEP' || cls.status === 'KEEP_TEST';
}
