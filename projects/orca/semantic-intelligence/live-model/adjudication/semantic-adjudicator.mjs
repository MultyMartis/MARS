/**
 * Model-aware semantic adjudicator — receives assessments only after both complete.
 */
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
  } = params;

  const findings = [];
  let outcome = 'FINAL ABSTAIN';
  let confidence = 0.5;
  let humanRequired = false;
  let decisiveEvidence = [];
  let conflictingEvidence = [];
  let agreementState = 'UNKNOWN';

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

  if (hardRuleEvidence?.blocked && hardRuleEvidence.override_decision) {
    outcome = `FINAL ${hardRuleEvidence.override_decision}`;
    decisiveEvidence = hardRuleEvidence.evidence || [];
    findings.push('hard_rule_override');
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

  if (hardRuleEvidence?.blocked && decisionA === 'ACCEPT') {
    outcome = 'FINAL REJECT';
    decisiveEvidence = hardRuleEvidence.evidence || [];
    findings.push('hard_rule_blocks_accept');
  }

  if (agreementState === 'AGREE' && !findings.includes('hard_rule_override')) {
    outcome = `FINAL ${decisionA}`;
    confidence = Math.max(assessmentA.confidence || 0.5, assessmentB?.confidence || 0);
    decisiveEvidence.push('assessor_agreement');
  } else if (agreementState === 'DISAGREE') {
    findings.push('assessor_disagreement');
    if (decisionA === 'REJECT' || decisionB === 'REJECT') {
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
  } else if (agreementState === 'SINGLE_ASSESSOR') {
    outcome = `FINAL ${decisionA}`;
    confidence = assessmentA.confidence || 0.5;
    if (decisionA === 'ACCEPT' && confidence < 0.75) {
      outcome = 'FINAL ABSTAIN';
      findings.push('single_assessor_low_confidence');
    }
  }

  if (outcome === 'FINAL ACCEPT') {
    const hasCommercialEvidence = (assessmentA.commercial_evidence || []).length > 0
      || (assessmentB?.commercial_evidence || []).length > 0;
    if (!hasCommercialEvidence && !decisiveEvidence.includes('assessor_agreement')) {
      outcome = 'FINAL ABSTAIN';
      findings.push('accept_without_evidence_blocked');
    }
    if (confidence < 0.7) {
      outcome = 'FINAL ABSTAIN';
      findings.push('low_confidence_accept_downgraded');
    }
  }

  if (serviceScopeHallucination(assessmentA, serviceRegistry) || serviceScopeHallucination(assessmentB, serviceRegistry)) {
    outcome = 'DOMAIN CONFLICT';
    humanRequired = true;
    conflictingEvidence.push('service_outside_scope');
  }

  confidence = Math.max(0, Math.min(1, confidence));
  if (['POLICY CONFLICT', 'DOMAIN CONFLICT', 'INVALID EVIDENCE'].includes(outcome)) humanRequired = true;
  if (outcome === 'FINAL ABSTAIN' && confidence < 0.4) humanRequired = true;

  return {
    outcome,
    final_decision: outcome.replace('FINAL ', '').replace('POLICY CONFLICT', 'ABSTAIN').replace('DOMAIN CONFLICT', 'ABSTAIN').replace('INVALID EVIDENCE', 'ABSTAIN'),
    agreement_state: agreementState,
    decisive_evidence: decisiveEvidence,
    conflicting_evidence: conflictingEvidence,
    confidence,
    human_review_required: humanRequired,
    findings,
    explanation: buildExplanation(outcome, agreementState, findings, decisiveEvidence, conflictingEvidence),
  };
}

function invalidEvidenceResult(reason) {
  return {
    outcome: 'INVALID EVIDENCE',
    final_decision: 'ABSTAIN',
    agreement_state: 'INVALID',
    decisive_evidence: [],
    conflicting_evidence: [reason],
    confidence: 0,
    human_review_required: true,
    findings: ['invalid_evidence'],
    explanation: reason,
  };
}

function serviceScopeHallucination(assessment, registry) {
  if (!assessment?.rationale) return false;
  const services = (registry?.services || []).map((s) => s.name.toLowerCase());
  const hireSignals = ['hire', 'найм', 'специалист'];
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
