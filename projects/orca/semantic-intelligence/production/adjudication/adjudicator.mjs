import { FINAL_DECISIONS, ADJUDICATION_ESCALATIONS } from '../runtime/lib.mjs';

export function adjudicate({ primary, reassessment, hardRules, invariantResults, businessScope }) {
  const findings = [];
  let outcome = `FINAL ${primary.decision}`;
  let confidence = primary.confidence;
  let humanRequired = false;
  let decisiveEvidence = [];
  let unresolvedAmbiguity = null;

  if (hardRules?.blocked && hardRules.override_decision) {
    outcome = `FINAL ${hardRules.override_decision}`;
    decisiveEvidence = hardRules.evidence;
    findings.push('hard_rule_override');
  }

  const blockingInvariants = (invariantResults || []).filter((f) => f.blocking);
  if (blockingInvariants.length) {
    if (primary.decision === 'ACCEPT') {
      outcome = 'FINAL ABSTAIN';
      findings.push('invariant_blocked_accept');
      decisiveEvidence = blockingInvariants.map((f) => f.invariant_id);
    }
  }

  if (reassessment && !reassessment.agreement) {
    findings.push('assessor_disagreement');
    if (reassessment.suggested_decision !== primary.decision) {
      outcome = `FINAL ${reassessment.suggested_decision}`;
      confidence += reassessment.confidence_adjustment || 0;
      decisiveEvidence.push('reassessment_disagreement');
    }
  }

  if (reassessment?.suggested_decision === 'ABSTAIN' && outcome === 'FINAL ACCEPT' && primary.confidence < 0.75) {
    outcome = 'FINAL ABSTAIN';
    findings.push('low_confidence_accept_downgraded');
  }

  if (outcome === 'FINAL ACCEPT' && primary.reason_code === 'TOPIC_ONLY_INSUFFICIENT_EVIDENCE') {
    outcome = 'ESCALATE POLICY CONFLICT';
    humanRequired = true;
    unresolvedAmbiguity = 'topical_match_used_as_positive';
  }

  if (primary.protected_strata_conflict && outcome === 'FINAL ACCEPT') {
    outcome = 'ESCALATE DOMAIN CONFLICT';
    humanRequired = true;
    unresolvedAmbiguity = 'protected_strata_overlap';
  }

  if (!primary.decision || !['ACCEPT', 'REJECT', 'ABSTAIN'].includes(primary.decision)) {
    outcome = 'INVALID RECORD';
    humanRequired = true;
  }

  if (ADJUDICATION_ESCALATIONS.has(outcome)) humanRequired = true;
  if (outcome === 'FINAL ABSTAIN' && primary.confidence < 0.5) humanRequired = true;

  confidence = Math.max(0, Math.min(1, confidence));

  return {
    outcome,
    agreement: reassessment?.agreement ?? true,
    decisive_evidence: decisiveEvidence,
    unresolved_ambiguity: unresolvedAmbiguity,
    final_confidence: confidence,
    human_review_required: humanRequired,
    findings,
    explanation: buildExplanation(outcome, findings, decisiveEvidence, humanRequired),
    final_decision: outcome.replace('FINAL ', ''),
  };
}

function buildExplanation(outcome, findings, evidence, humanRequired) {
  const parts = [`Outcome: ${outcome}`];
  if (findings.length) parts.push(`Findings: ${findings.join(', ')}`);
  if (evidence.length) parts.push(`Decisive: ${JSON.stringify(evidence)}`);
  parts.push(humanRequired ? 'Human review required' : 'Automated final — no human review');
  return parts.join('; ');
}
