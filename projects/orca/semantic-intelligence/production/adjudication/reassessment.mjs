import { assessDeterministic } from '../assessors/deterministic-assessor.mjs';

const RISK_CANDIDATES = [
  'protected_strata_conflict',
  'PROBLEM_QUERY',
  'SHORT_HEAD',
  'PRODUCT_VS_SERVICE',
  'PROVIDER_VS_DIY',
  'CAREER_VS_PROVIDER',
  'REGULATORY',
  'TOPIC_ONLY',
];

export function needsReassessment(primary, hardRuleResult) {
  if (primary.decision === 'ABSTAIN') return true;
  if (primary.decision === 'ACCEPT' && primary.confidence < 0.7) return true;
  if (primary.decision === 'ACCEPT' && primary.protected_strata_conflict) return true;
  if (primary.decision === 'ACCEPT' && primary.risk?.overall_risk === 'HIGH') return true;
  if (hardRuleResult?.blocked) return true;
  const amb = primary.ambiguity?.types || [];
  if (primary.decision === 'ACCEPT' && amb.some((t) => RISK_CANDIDATES.includes(t))) return true;
  return false;
}

export function runReassessment(phrase, context, primaryAssessment) {
  const altInterpretations = buildAlternatives(primaryAssessment, phrase);
  const secondary = assessDeterministic({
    raw_query: phrase.raw_query,
    normalized_query: phrase.normalized_query,
    business_scope: context.businessScope,
    serviceRegistry: context.serviceRegistry,
  });

  const agreement = secondary.decision === primaryAssessment.decision;
  const testedAlternatives = altInterpretations.map((alt) => ({
    interpretation: alt,
    plausibility: scoreAlternative(alt, primaryAssessment, secondary),
    evidence_for: alt.evidence_for || [],
    evidence_against: alt.evidence_against || [],
  }));

  let suggestedDecision = primaryAssessment.decision;
  let confidenceDelta = 0;
  if (!agreement) {
    if (secondary.confidence > primaryAssessment.confidence + 0.1) {
      suggestedDecision = secondary.decision;
      confidenceDelta = -0.15;
    } else {
      suggestedDecision = 'ABSTAIN';
      confidenceDelta = -0.2;
    }
  } else if (primaryAssessment.decision === 'ACCEPT' && primaryAssessment.confidence < 0.65) {
    suggestedDecision = 'ABSTAIN';
    confidenceDelta = -0.1;
  }

  return {
    reassessed_at: new Date().toISOString(),
    primary_decision: primaryAssessment.decision,
    secondary_decision: secondary.decision,
    agreement,
    alternative_interpretations_tested: testedAlternatives,
    suggested_decision: suggestedDecision,
    confidence_adjustment: confidenceDelta,
    evidence: {
      primary_rationale: primaryAssessment.rationale,
      secondary_rationale: secondary.rationale,
      not_blind_copy: secondary.rationale !== primaryAssessment.rationale || !agreement,
    },
    assessor_independence: 'secondary_pass_same_engine_different_context',
  };
}

function buildAlternatives(primary, phrase) {
  const alts = [];
  if (primary.provider_hire_likelihood > 0.4) {
    alts.push({ label: 'DIY_SELF_HELP', evidence_for: ['problem wording'], evidence_against: primary.commercial_evidence });
  }
  if (primary.career_likelihood > 0.2) {
    alts.push({ label: 'CAREER_SEARCH', evidence_for: ['employment terms'], evidence_against: [] });
  }
  if (primary.product_only_likelihood > 0.4) {
    alts.push({ label: 'PRODUCT_PURCHASE', evidence_for: ['module/config terms'], evidence_against: primary.commercial_evidence });
  }
  if (!alts.length) {
    alts.push({ label: 'INFORMATIONAL_ONLY', evidence_for: ['topic match only'], evidence_against: primary.commercial_evidence });
  }
  return alts;
}

function scoreAlternative(alt, primary, secondary) {
  if (alt.label === 'INFORMATIONAL_ONLY' && primary.reason_code === 'TOPIC_ONLY_INSUFFICIENT_EVIDENCE') return 0.7;
  if (alt.label === 'CAREER_SEARCH' && secondary.protected_intent_class === 'PROTECTED_CAREER') return 0.85;
  return 0.45;
}
