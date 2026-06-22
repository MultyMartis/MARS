/**
 * Hard rules — block protected intents; must not be sole positive classifier.
 */
const HARD_REJECT_PATTERNS = [
  { pattern: /ваканс|резюме|headhunter|hh\.ru/i, class: 'PROTECTED_CAREER', reason: 'career_hard_rule' },
  { pattern: /скачать|торрент|кряк/i, class: 'PROTECTED_DOWNLOAD', reason: 'download_hard_rule' },
  { pattern: /личн.*кабинет|\bвход\b/i, class: 'PROTECTED_NAVIGATION', reason: 'login_hard_rule' },
];

export function applyHardRules(phrase, primaryAssessment) {
  const text = phrase.normalized_query || phrase.raw_query || '';
  const evidence = [];
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
  return { blocked: false, evidence: [], rationale: null };
}

export function topicalMatchOnlyBlocked(assessment) {
  return assessment.reason_code === 'TOPIC_ONLY_INSUFFICIENT_EVIDENCE' && assessment.decision === 'ACCEPT';
}
