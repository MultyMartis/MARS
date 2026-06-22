/**
 * Deterministic/local diagnostic assessor for fixtures and production default.
 * NOT live semantic model authority — see MODEL-RUNTIME-BOUNDARY-v1.md
 */
import { assessPhrase, normalizePhrase } from '../../integration/pilot-runs/p0-i-real-slice-v1/runs/pilot-assessor-v1.mjs';
import { ASSESSOR_MODES } from './assessor-contract.mjs';

const LIKELIHOOD_MAP = {
  HIRE_PROVIDER: { provider_hire: 0.85, diy: 0.1, career: 0.05, education: 0.05, navigation: 0.05, product_only: 0.1 },
  FIND_EMPLOYMENT: { provider_hire: 0.1, diy: 0.05, career: 0.9, education: 0.1, navigation: 0.05, product_only: 0.05 },
  LEARN_SKILL: { provider_hire: 0.15, diy: 0.2, career: 0.1, education: 0.85, navigation: 0.05, product_only: 0.1 },
  SELF_SERVICE: { provider_hire: 0.2, diy: 0.85, career: 0.05, education: 0.15, navigation: 0.05, product_only: 0.2 },
  NAVIGATE: { provider_hire: 0.05, diy: 0.05, career: 0.05, education: 0.05, navigation: 0.9, product_only: 0.1 },
  ACQUIRE_PRODUCT: { provider_hire: 0.25, diy: 0.15, career: 0.05, education: 0.05, navigation: 0.1, product_only: 0.8 },
  RESOLVE_PROBLEM: { provider_hire: 0.55, diy: 0.45, career: 0.05, education: 0.05, navigation: 0.05, product_only: 0.15 },
  UNKNOWN: { provider_hire: 0.3, diy: 0.3, career: 0.15, education: 0.15, navigation: 0.1, product_only: 0.25 },
};

export const DETERMINISTIC_ASSESSOR_VERSION = ASSESSOR_MODES.DETERMINISTIC;

export function assessDeterministic(assessorContext) {
  const raw = assessorContext.raw_query;
  const norm = assessorContext.normalized_query;
  const result = assessPhrase(raw, norm);
  const a = result.assessor;
  const goal = a.likely_user_goal || 'UNKNOWN';
  const likelihoods = LIKELIHOOD_MAP[goal] || LIKELIHOOD_MAP.UNKNOWN;

  const protectedClass = detectProtectedClass(a.primary_intent, a.commercial_eligibility.reason_code);

  return {
    assessor_version: DETERMINISTIC_ASSESSOR_VERSION,
    model_execution: 'NOT_VALIDATED',
    primary_intent: a.primary_intent,
    secondary_intent: null,
    likely_next_user_action: goal,
    commercial_eligibility: a.commercial_eligibility.decision === 'ACCEPT',
    decision: a.commercial_eligibility.decision,
    commercial_evidence: a.commercial_eligibility.supporting_evidence || [],
    non_commercial_evidence: a.commercial_eligibility.opposing_evidence || [],
    protected_intent_class: protectedClass,
    provider_hire_likelihood: likelihoods.provider_hire,
    diy_likelihood: likelihoods.diy,
    career_likelihood: likelihoods.career,
    education_likelihood: likelihoods.education,
    navigation_likelihood: likelihoods.navigation,
    product_only_likelihood: likelihoods.product_only,
    ambiguity_class: (a.ambiguity?.types || ['NONE']).join('|'),
    confidence: a.commercial_eligibility.confidence ?? 0.5,
    rationale: a.literal_interpretation || a.commercial_eligibility.reason_code,
    alternative_interpretation: a.ambiguity?.competing_interpretations?.[0] || null,
    signals: a.signals || [],
    ambiguity: a.ambiguity,
    risk: a.risk,
    reason_code: a.commercial_eligibility.reason_code,
    protected_strata_conflict: result.protected_strata_conflict || false,
    normalization: normalizePhrase(norm),
  };
}

function detectProtectedClass(intent, reasonCode) {
  if (/CAREER/i.test(intent || '') || /CAREER/i.test(reasonCode || '')) return 'PROTECTED_CAREER';
  if (/EDUCATION/i.test(intent || '') || /EDUCATION/i.test(reasonCode || '')) return 'PROTECTED_EDUCATION';
  if (/DIY/i.test(intent || '') || /DIY/i.test(reasonCode || '')) return 'PROTECTED_DIY';
  if (/DOWNLOAD|FREE/i.test(reasonCode || '')) return 'PROTECTED_DOWNLOAD';
  if (/NAV|LOGIN/i.test(intent || '') || /NAV/i.test(reasonCode || '')) return 'PROTECTED_NAVIGATION';
  if (/INFORMATIONAL/i.test(intent || '')) return 'PROTECTED_INFORMATIONAL';
  return null;
}
