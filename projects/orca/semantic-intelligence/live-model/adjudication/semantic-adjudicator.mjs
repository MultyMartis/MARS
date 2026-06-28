/**
 * Model-aware semantic adjudicator — receives assessments only after both complete.
 * Wave 3.1F v2: mandatory semantic invariants applied after all primary outcome branches.
 */
import {
  extractServiceIntentEvidence,
  resolveScopeFit,
} from '../evidence/service-intent-evidence.mjs';
import {
  evaluatePlatformCompatibility,
  PLATFORM_CLASSIFICATION,
} from '../evidence/platform-compatibility.mjs';

export const ADJUDICATOR_VERSION = 'v1.5';
export const ADJUDICATION_OUTCOMES = [
  'FINAL ACCEPT', 'FINAL REJECT', 'FINAL ABSTAIN',
  'POLICY CONFLICT', 'DOMAIN CONFLICT', 'INVALID EVIDENCE',
];

export function adjudicateSemanticIntent(params) {
  const {
    assessmentA,
    assessmentB,
    hardRuleEvidence,
    invariantResults = [],
    businessScope,
    serviceRegistry,
    protectedIntentPolicy = {},
    phrase,
    structuredEvidence: structuredEvidenceIn,
    platformCompatibility: platformCompatibilityIn,
  } = params;

  const structuredEvidence = structuredEvidenceIn
    || (phrase ? extractServiceIntentEvidence(phrase) : null);
  const platformCompatibility = platformCompatibilityIn
    || (phrase ? evaluatePlatformCompatibility(phrase, businessScope, serviceRegistry) : null);
  const scopeFitResult = phrase ? resolveScopeFit(phrase, serviceRegistry) : null;

  const findings = [];
  let outcome = 'FINAL ABSTAIN';
  let confidence = 0.5;
  let humanRequired = false;
  let decisiveEvidence = [];
  let conflictingEvidence = [];
  let agreementState = 'UNKNOWN';
  const invariantApplications = [];

  if (!assessmentA?.decision) {
    return invalidEvidenceResult('assessment A missing decision');
  }

  const decisionA = assessmentA.decision;
  const decisionB = assessmentB?.decision;

  if (decisionB) {
    agreementState = decisionA === decisionB ? 'AGREE' : 'DISAGREE';
  } else {
    agreementState = 'SINGLE_ASSESSOR';
  }

  // Phase 1: hard-rule override
  if (hardRuleEvidence?.blocked && hardRuleEvidence.override_decision) {
    outcome = `FINAL ${hardRuleEvidence.override_decision}`;
    decisiveEvidence = hardRuleEvidence.evidence || [];
    findings.push('hard_rule_override');
  }

  // Phase 2: product version update blocks premature ACCEPT
  if (structuredEvidence?.product_version_update && !structuredEvidence?.service_update_intent) {
    if (outcome === 'FINAL ACCEPT' || decisionA === 'ACCEPT') {
      outcome = 'FINAL REJECT';
      confidence = 0.8;
      decisiveEvidence.push('product_version_update_not_service');
      findings.push('product_version_update_reject');
    }
  }

  const blockingInvariants = invariantResults.filter((f) => f.blocking);
  if (blockingInvariants.length && outcome.includes('ACCEPT')) {
    outcome = 'FINAL ABSTAIN';
    findings.push('invariant_blocked_accept');
    decisiveEvidence = blockingInvariants.map((f) => f.invariant_id);
  }

  if (assessmentA.protected_intent_class && decisionA === 'ACCEPT') {
    outcome = 'POLICY CONFLICT';
    humanRequired = true;
    conflictingEvidence.push('protected_intent_accept_conflict');
    findings.push('protected_class_accept');
  }

  if (hardRuleEvidence?.blocked && decisionA === 'ACCEPT' && !hardRuleEvidence.override_decision) {
    outcome = 'FINAL REJECT';
    decisiveEvidence = hardRuleEvidence.evidence || [];
    findings.push('hard_rule_blocks_accept');
  }

  // Phase 3: primary outcome branches (agreement / disagreement / single assessor)
  if (agreementState === 'AGREE' && !findings.includes('hard_rule_override')) {
    outcome = `FINAL ${decisionA}`;
    confidence = Math.max(assessmentA.confidence || 0.5, assessmentB?.confidence || 0);
    decisiveEvidence.push('assessor_agreement');
    if (decisionA === 'REJECT' && structuredEvidence?.strong_commercial_geo) {
      outcome = 'FINAL ACCEPT';
      confidence = Math.max(0.75, confidence);
      decisiveEvidence.push('structured_strong_commercial_geo_override');
      findings.push('scope_fit_separated_from_commercial_reject');
    }
    if (decisionA === 'REJECT' && structuredEvidence?.strong_commercial && !structuredEvidence?.strong_commercial_geo
      && !structuredEvidence?.product_version_update && !structuredEvidence?.ambiguous_diy_problem) {
      outcome = 'FINAL ACCEPT';
      confidence = Math.max(0.75, confidence);
      decisiveEvidence.push('structured_strong_commercial_override');
      findings.push('paid_problem_or_service_accept');
    }
  } else if (agreementState === 'DISAGREE') {
    findings.push('assessor_disagreement');
    const productReject = resolveProductServiceDisagreement(assessmentA, assessmentB);
    if (productReject) {
      outcome = 'FINAL REJECT';
      confidence = 0.75;
      decisiveEvidence.push('product_acquisition_not_service');
      findings.push('product_service_disagreement_resolved');
    } else {
      const geoCommercialAccept = resolveGeoCommercialDisagreement(
        assessmentA, assessmentB, structuredEvidence,
      );
      if (geoCommercialAccept) {
        outcome = 'FINAL ACCEPT';
        confidence = Math.max(assessmentA.confidence || 0.5, assessmentB?.confidence || 0.5, 0.75);
        decisiveEvidence.push('geo_service_commercial_evidence');
        findings.push('geo_commercial_disagreement_resolved');
      } else if (structuredEvidence?.strong_commercial_geo) {
        outcome = 'FINAL ACCEPT';
        confidence = 0.78;
        decisiveEvidence.push('structured_strong_commercial_geo');
        findings.push('structured_geo_commercial_disagreement_resolved');
      } else if (decisionA === 'REJECT' || decisionB === 'REJECT') {
        outcome = 'FINAL REJECT';
        confidence = 0.65;
        decisiveEvidence.push('reject_wins_on_disagreement');
      } else if (decisionA === 'ABSTAIN' || decisionB === 'ABSTAIN') {
        outcome = 'FINAL ABSTAIN';
        confidence = 0.5;
      } else {
        outcome = 'POLICY CONFLICT';
        humanRequired = true;
        conflictingEvidence.push('accept_abstain_split');
      }
    }
  } else if (agreementState === 'SINGLE_ASSESSOR' && !findings.includes('hard_rule_override')) {
    outcome = `FINAL ${decisionA}`;
    confidence = assessmentA.confidence || 0.5;
    if (decisionA === 'ACCEPT' && confidence < 0.75) {
      outcome = 'FINAL ABSTAIN';
      findings.push('single_assessor_low_confidence');
    }
    if (decisionA === 'REJECT' && (structuredEvidence?.strong_commercial_geo || structuredEvidence?.strong_commercial)
      && !structuredEvidence?.product_version_update && !structuredEvidence?.ambiguous_diy_problem) {
      outcome = 'FINAL ACCEPT';
      confidence = 0.76;
      decisiveEvidence.push('structured_strong_commercial_geo_single');
      findings.push('scope_fit_separated_from_commercial_reject');
    }
    if (decisionA === 'ABSTAIN' && structuredEvidence?.strong_commercial_problem) {
      outcome = 'FINAL ACCEPT';
      confidence = 0.77;
      decisiveEvidence.push('structured_paid_problem_resolution');
      findings.push('explicit_paid_problem_accept');
    }
  }

  // Phase 4: accept safety gates (before mandatory invariants)
  if (outcome === 'FINAL ACCEPT') {
    const hasCommercialEvidence = (assessmentA.commercial_evidence || []).length > 0
      || (assessmentB?.commercial_evidence || []).length > 0
      || structuredEvidence?.strong_commercial_geo
      || structuredEvidence?.strong_commercial
      || structuredEvidence?.supporting_commercial_geo;
    if (!hasCommercialEvidence && !decisiveEvidence.some((d) => d.includes('structured'))) {
      outcome = 'FINAL ABSTAIN';
      findings.push('accept_without_evidence_blocked');
    }
    if (confidence < 0.7 && !structuredEvidence?.strong_commercial_geo) {
      outcome = 'FINAL ABSTAIN';
      findings.push('low_confidence_accept_downgraded');
    }
  }

  if (serviceScopeHallucination(assessmentA, serviceRegistry) || serviceScopeHallucination(assessmentB, serviceRegistry)) {
    findings.push('scope_fit_out_of_registry');
    humanRequired = true;
    conflictingEvidence.push('service_outside_scope');
    if (outcome === 'FINAL ACCEPT' || outcome !== 'FINAL REJECT') {
      outcome = 'DOMAIN CONFLICT';
    }
  }

  // Phase 5: mandatory semantic invariants (always after primary branches)
  const invariantResult = applyMandatorySemanticInvariants({
    outcome,
    confidence,
    structuredEvidence,
    platformCompatibility,
    hardRuleEvidence,
    findings,
    decisiveEvidence,
    invariantApplications,
  });
  outcome = invariantResult.outcome;
  confidence = invariantResult.confidence;

  confidence = Math.max(0, Math.min(1, confidence));
  if (['POLICY CONFLICT', 'DOMAIN CONFLICT', 'INVALID EVIDENCE'].includes(outcome)) humanRequired = true;
  if (outcome === 'FINAL ABSTAIN' && confidence < 0.4) humanRequired = true;

  const finalDecision = outcome.replace('FINAL ', '').replace('POLICY CONFLICT', 'ABSTAIN').replace('DOMAIN CONFLICT', 'ABSTAIN').replace('INVALID EVIDENCE', 'ABSTAIN');

  return {
    outcome,
    final_decision: finalDecision,
    commercial_eligibility: {
      decision: finalDecision,
      confidence,
    },
    scope_fit: scopeFitResult?.scope_fit || 'UNKNOWN',
    ownership: scopeFitResult?.ownership || null,
    service_gap: scopeFitResult?.service_gap || false,
    structured_evidence: structuredEvidence,
    platform_compatibility: platformCompatibility,
    agreement_state: agreementState,
    decisive_evidence: decisiveEvidence,
    conflicting_evidence: conflictingEvidence,
    confidence,
    human_review_required: humanRequired,
    findings,
    invariant_applications: invariantApplications,
    explanation: buildExplanation(outcome, agreementState, findings, decisiveEvidence, conflictingEvidence),
  };
}

function hasDirectCommercialErrorOverride(structuredEvidence) {
  return Boolean(
    structuredEvidence?.strong_commercial_problem
    || (structuredEvidence?.provider_noun_detected && structuredEvidence?.service_task_detected
      && !structuredEvidence?.ambiguous_diy_problem),
  );
}

export function applyMandatorySemanticInvariants({
  outcome,
  confidence,
  structuredEvidence,
  platformCompatibility,
  hardRuleEvidence,
  findings,
  decisiveEvidence,
  invariantApplications,
}) {
  let nextOutcome = outcome;
  let nextConfidence = confidence;

  if (structuredEvidence?.ambiguous_diy_problem
    && !hasDirectCommercialErrorOverride(structuredEvidence)) {
    if (nextOutcome === 'FINAL REJECT' || nextOutcome === 'FINAL ACCEPT') {
      nextOutcome = 'FINAL ABSTAIN';
      nextConfidence = Math.min(nextConfidence, 0.48);
      findings.push('invariant_ambiguous_diy_abstain');
      decisiveEvidence.push('ambiguous_diy_problem');
      invariantApplications.push({
        invariant_id: 'ambiguous_diy_problem_abstain',
        applied: true,
        prior_outcome: outcome,
        final_outcome: nextOutcome,
      });
    }
  }

  if (platformCompatibility?.classification === PLATFORM_CLASSIFICATION.GENERIC_PLATFORM_FAMILY
    && (structuredEvidence?.product_version_update || structuredEvidence?.product_only)
    && !structuredEvidence?.service_update_intent) {
    if (nextOutcome === 'FINAL REJECT' || nextOutcome === 'FINAL ACCEPT') {
      nextOutcome = 'FINAL ABSTAIN';
      nextConfidence = Math.min(nextConfidence, 0.46);
      findings.push('invariant_generic_platform_family_abstain');
      decisiveEvidence.push('generic_platform_family_ambiguity');
      invariantApplications.push({
        invariant_id: 'generic_platform_family_abstain',
        applied: true,
        prior_outcome: outcome,
        final_outcome: nextOutcome,
      });
    }
  }

  if (structuredEvidence?.bare_error_insufficient_context && nextOutcome === 'FINAL REJECT') {
    nextOutcome = 'FINAL ABSTAIN';
    nextConfidence = Math.min(nextConfidence, 0.45);
    findings.push('invariant_bare_error_abstain');
    decisiveEvidence.push('insufficient_context_error_code');
    invariantApplications.push({
      invariant_id: 'bare_error_insufficient_context_abstain',
      applied: true,
      prior_outcome: outcome,
      final_outcome: nextOutcome,
    });
  }

  if (hardRuleEvidence?.reinforce_abstain
    && (nextOutcome === 'FINAL REJECT' || nextOutcome === 'FINAL ACCEPT')
    && structuredEvidence?.ambiguous_diy_problem
    && !hasDirectCommercialErrorOverride(structuredEvidence)) {
    nextOutcome = 'FINAL ABSTAIN';
    findings.push('invariant_hard_rule_reinforce_abstain');
    invariantApplications.push({
      invariant_id: 'hard_rule_reinforce_abstain',
      applied: true,
      prior_outcome: outcome,
      final_outcome: nextOutcome,
    });
  }

  return { outcome: nextOutcome, confidence: nextConfidence };
}

const CAREER_MARKERS = /(ваканси|резюме|зарплат|устроиться|трудоустройств|ищу работу|работа программист)/i;
const SERVICE_SCOPE_MARKERS = /(внедрен|настрой|интеграц|под ключ|специалист|обслуживан|сопровожден|доработ|миграц|администрир|программист|разработчик|мастер|юрист|бухгалтер)/i;
const PRODUCT_ACQUISITION_MARKERS = /(купить|скачать|лицензи|коробочн|дистрибутив|стоимость программ|цена программ|официальн.*сайт|верси.*проф|обновлен.*верси)/i;
const SUPPLY_WITHOUT_SERVICE = /(?:заказать\s+)?поставк(?:а|у|и)\s+(?!.*(?:внедрен|настрой|интеграц|специалист|под ключ))/i;

function resolveProductServiceDisagreement(assessmentA, assessmentB) {
  const acceptSide = [assessmentA, assessmentB].find((a) => a?.decision === 'ACCEPT');
  if (!acceptSide) return false;
  const other = assessmentA === acceptSide ? assessmentB : assessmentA;
  const text = `${acceptSide.rationale || ''} ${other?.rationale || ''}`.toLowerCase();
  const productOnly = Math.max(
    acceptSide.product_only_likelihood ?? 0,
    other?.product_only_likelihood ?? 0,
  );
  const providerHire = acceptSide.provider_hire_likelihood ?? 0;
  const protectedProduct = /product_only|product-only|software purchase|license purchase/i.test(
    `${acceptSide.protected_intent_class || ''} ${other?.protected_intent_class || ''}`,
  );
  const hasServiceScope = SERVICE_SCOPE_MARKERS.test(text)
    || (acceptSide.commercial_evidence || []).some((e) => SERVICE_SCOPE_MARKERS.test(String(e)));
  const productAcquisitionSignal = PRODUCT_ACQUISITION_MARKERS.test(text)
    || SUPPLY_WITHOUT_SERVICE.test(text)
    || protectedProduct;
  if (productAcquisitionSignal && !hasServiceScope && (productOnly >= 0.55 || providerHire < 0.5)) {
    return true;
  }
  if (other?.decision === 'REJECT' && productOnly >= 0.65 && providerHire < 0.45 && !hasServiceScope) {
    return true;
  }
  return false;
}

function resolveGeoCommercialDisagreement(assessmentA, assessmentB, structuredEvidence) {
  const candidates = [assessmentA, assessmentB].filter((a) => a?.decision === 'ACCEPT');
  if (candidates.length !== 1) return false;
  const accept = candidates[0];
  const rejectSide = [assessmentA, assessmentB].find((a) => a?.decision === 'REJECT');
  if (!rejectSide) return false;
  const hire = Math.max(
    accept.provider_hire_likelihood ?? 0,
    structuredEvidence?.strong_commercial_geo ? 0.7 : 0,
  );
  const career = Math.max(accept.career_likelihood ?? 0, rejectSide.career_likelihood ?? 0);
  const hasCommercialEvidence = (accept.commercial_evidence || []).length > 0
    || structuredEvidence?.strong_commercial_geo
    || structuredEvidence?.supporting_commercial_geo;
  const careerRationale = CAREER_MARKERS.test(`${rejectSide.rationale || ''} ${accept.rationale || ''}`)
    || structuredEvidence?.career;
  if (structuredEvidence?.strong_commercial_geo && !careerRationale) return true;
  return hasCommercialEvidence && hire >= career && hire >= 0.5 && !careerRationale;
}

function invalidEvidenceResult(reason) {
  return {
    outcome: 'INVALID EVIDENCE',
    final_decision: 'ABSTAIN',
    commercial_eligibility: { decision: 'ABSTAIN', confidence: 0 },
    scope_fit: 'UNKNOWN',
    ownership: null,
    agreement_state: 'INVALID',
    decisive_evidence: [],
    conflicting_evidence: [reason],
    confidence: 0,
    human_review_required: true,
    findings: ['invalid_evidence'],
    invariant_applications: [],
    explanation: reason,
  };
}

function serviceScopeHallucination(assessment, registry) {
  if (!assessment?.rationale) return false;
  const mentionsUnknownService = /service_id:\s*(\w+)/i.test(assessment.rationale);
  if (mentionsUnknownService) {
    const match = assessment.rationale.match(/service_id:\s*(\w+)/i);
    const id = match?.[1];
    const known = (registry?.services || []).some((s) => s.service_id === id);
    if (!known) return true;
  }
  return false;
}

function buildExplanation(outcome, agreement, findings, decisive, conflicting) {
  return [
    `Outcome: ${outcome}`,
    `Agreement: ${agreement}`,
    findings.length ? `Findings: ${findings.join(', ')}` : null,
    decisive.length ? `Decisive: ${decisive.join(', ')}` : null,
    conflicting.length ? `Conflicting: ${conflicting.join(', ')}` : null,
  ].filter(Boolean).join('; ');
}
