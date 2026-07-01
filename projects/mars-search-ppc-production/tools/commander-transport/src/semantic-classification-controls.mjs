/**
 * Reusable semantic classification controls — operator judgement preserved via HOLD / OPERATOR_REVIEW.
 */

import corpus from '../contracts/search-ppc-regression-corpus-v1.json' with { type: 'json' };

export const INTENT_CLASSES = Object.freeze({
  BUYER_SERVICE: 'BUYER_SERVICE',
  EMPLOYMENT: 'EMPLOYMENT',
  COMMERCIAL_PRICE: 'COMMERCIAL_PRICE',
  CAREER: 'CAREER',
  EDUCATION: 'EDUCATION',
  TUTORIAL_ONLY: 'TUTORIAL_ONLY',
  DOWNLOAD_PIRACY: 'DOWNLOAD_PIRACY',
  FOREIGN_MARKET: 'FOREIGN_MARKET',
  OPERATOR_REVIEW: 'OPERATOR_REVIEW',
});

export const ROUTING_MODES = Object.freeze({
  LOCAL_ONLY: 'LOCAL_ONLY',
  REMOTE_ONLY: 'REMOTE_ONLY',
  REJECT_RUSSIA_ONLY_SCOPE: 'REJECT_RUSSIA_ONLY_SCOPE',
});

const EMPLOYMENT_MARKERS = [
  'ваканс', 'резюме', 'работа программист', 'зарплат', 'заработн', 'карьер', 'трудоустрой',
];
const EDUCATION_MARKERS = ['курс', 'обучен', 'колледж', 'университет', 'школ', 'с нуля'];
const TUTORIAL_MARKERS = ['как сделать', 'как настроить', 'инструкция', 'пример тз', 'ошибки программиста'];
const BUYER_MARKERS = ['нужен', 'найти', 'ищу', 'где найти', 'стоимость', 'цена', 'услуг', 'аутсорс'];

/**
 * Lightweight classifier for regression fixtures — not automatic authority for new clients.
 * @param {string} phrase
 */
export function classifyPhraseIntent(phrase) {
  const p = phrase.toLowerCase().trim();
  if (EMPLOYMENT_MARKERS.some((m) => p.includes(m))) {
    return { decision: 'REJECT', intent: INTENT_CLASSES.EMPLOYMENT, severity: 'HARD_FAIL' };
  }
  if (EDUCATION_MARKERS.some((m) => p.includes(m))) {
    return { decision: 'REJECT', intent: INTENT_CLASSES.EDUCATION, severity: 'HARD_FAIL' };
  }
  if (TUTORIAL_MARKERS.some((m) => p.includes(m))) {
    return { decision: 'REJECT', intent: INTENT_CLASSES.TUTORIAL_ONLY, severity: 'HARD_FAIL' };
  }
  if (p.includes('скачать') || p.includes('торрент') || p.includes('кряк')) {
    return { decision: 'REJECT', intent: INTENT_CLASSES.DOWNLOAD_PIRACY, severity: 'HARD_FAIL' };
  }
  if (p.includes('стоимость') || p.includes('цена') || p.includes('сколько стоит')) {
    return { decision: 'KEEP_CANDIDATE', intent: INTENT_CLASSES.COMMERCIAL_PRICE, severity: 'OPERATOR_REVIEW' };
  }
  if (BUYER_MARKERS.some((m) => p.includes(m))) {
    return { decision: 'KEEP_CANDIDATE', intent: INTENT_CLASSES.BUYER_SERVICE, severity: 'OPERATOR_REVIEW' };
  }
  return { decision: 'HOLD', intent: INTENT_CLASSES.OPERATOR_REVIEW, severity: 'OPERATOR_REVIEW' };
}

/**
 * @param {string} city
 */
export function classifyGeoRouting(city) {
  const examples = corpus.geo_examples ?? {};
  if (examples[city]) return { city, routing: examples[city] };
  if (/минск|алматы|казахстан|беларус/i.test(city)) {
    return { city, routing: ROUTING_MODES.REJECT_RUSSIA_ONLY_SCOPE };
  }
  if (/новосибирск/i.test(city)) {
    return { city, routing: ROUTING_MODES.LOCAL_ONLY };
  }
  return { city, routing: ROUTING_MODES.REMOTE_ONLY };
}

/**
 * @param {string} phrase
 */
export function classifyServiceFamily(phrase) {
  const p = phrase.toLowerCase();
  const examples = corpus.service_routing_examples ?? {};
  for (const [key, family] of Object.entries(examples)) {
    if (p.includes(key.toLowerCase())) return { family, matched: key };
  }
  if (/честн|маркировк|знак/.test(p)) return { family: 'CA-05', matched: 'honest_sign' };
  if (/интеграц|api|сайт|bitrix/.test(p)) return { family: 'CA-04', matched: 'integration' };
  if (/сопровожден|абонент|поддержк/.test(p)) return { family: 'CA-02', matched: 'support' };
  if (/доработк|внедрен|настройк/.test(p)) return { family: 'CA-03', matched: 'modification' };
  return { family: 'CA-01', matched: null, severity: 'OPERATOR_REVIEW' };
}
