/**
 * Hard rules — block protected intents; must not be sole positive classifier.
 * Wave 3.1F: bare error abstain; price+service not product acquisition.
 */
import { extractServiceIntentEvidence } from '../../live-model/evidence/service-intent-evidence.mjs';

const HARD_REJECT_PATTERNS = [
  { pattern: /ваканс|резюме|headhunter|hh\.ru/i, class: 'PROTECTED_CAREER', reason: 'career_hard_rule' },
  { pattern: /скачать|торрент|кряк/i, class: 'PROTECTED_DOWNLOAD', reason: 'download_hard_rule' },
  { pattern: /личн.*кабинет|\bвход\b/i, class: 'PROTECTED_NAVIGATION', reason: 'login_hard_rule' },
];

const SERVICE_SCOPE_MARKERS = /(?:внедрен|настрой|интеграц|под ключ|специалист|обслуживан|сопровожден|доработ|миграц|администрир|программист|разработчик)/i;
const PRODUCT_ACQUISITION_MARKERS = /(?:купить|заказать\s+поставку|коробочн(?:ая|ой|ую)?\s+поставк|лицензи(?:я|и|ю).*(?:цена|стоимость|купить)|скачать\s+(?:дистрибутив|программ)|стоимость\s+программ|цена\s+(?:программ|лицензи)(?!\s+(?:настройк|внедрен|интеграц))|официальн(?:ый|ого)\s+(?:сайт|дистрибутив)|установ(?:ить|ка)\s+самостоятельно)/i;
const PRICE_SERVICE_PATTERN = /(?:цена|стоимость|сколько стоит)\s+(?:настройк|внедрен|интеграц|обслуживан|сопровожден|ремонт|установк)/i;

export function applyHardRules(phrase, primaryAssessment) {
  const text = phrase.normalized_query || phrase.raw_query || '';
  const evidence = [];
  const structured = extractServiceIntentEvidence(phrase);

  if (structured.bare_error_insufficient_context) {
    evidence.push({ rule: 'bare_error_abstain_rule', class: 'INSUFFICIENT_CONTEXT', span: 'error_code' });
    if (primaryAssessment.decision === 'REJECT') {
      return {
        blocked: true,
        override_decision: 'ABSTAIN',
        evidence,
        rationale: 'Bare error code without commercial signals → ABSTAIN not REJECT',
      };
    }
    return { blocked: false, reinforce_abstain: true, evidence, rationale: 'bare_error_abstain_rule' };
  }

  for (const rule of HARD_REJECT_PATTERNS) {
    if (rule.pattern.test(text)) {
      evidence.push({ rule: rule.reason, class: rule.class, span: text.match(rule.pattern)?.[0] });
      if (primaryAssessment.decision === 'ACCEPT') {
        return {
          blocked: true,
          override_decision: 'REJECT',
          evidence,
          rationale: `Hard rule ${rule.reason} blocks ACCEPT`,
        };
      }
      return { blocked: false, reinforce_reject: true, evidence, rationale: rule.reason };
    }
  }

  if (PRICE_SERVICE_PATTERN.test(text) && structured.strong_commercial_geo) {
    return { blocked: false, evidence: [{ rule: 'price_service_geo_pass', class: 'COMMERCIAL_GEO' }], rationale: null };
  }

  if (PRODUCT_ACQUISITION_MARKERS.test(text) && !SERVICE_SCOPE_MARKERS.test(text) && !structured.product_plus_service) {
    evidence.push({ rule: 'product_acquisition_hard_rule', class: 'PROTECTED_PRODUCT', span: 'product_supply' });
    if (primaryAssessment.decision === 'ACCEPT') {
      return {
        blocked: true,
        override_decision: 'REJECT',
        evidence,
        rationale: 'Product acquisition without service scope blocks ACCEPT',
      };
    }
    return { blocked: false, reinforce_reject: true, evidence, rationale: 'product_acquisition_hard_rule' };
  }
  return { blocked: false, evidence: [], rationale: null };
}

export function topicalMatchOnlyBlocked(assessment) {
  return assessment.reason_code === 'TOPIC_ONLY_INSUFFICIENT_EVIDENCE' && assessment.decision === 'ACCEPT';
}
