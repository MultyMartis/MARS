import { BLOCKER_CODES } from './constants.mjs';

export function validateHumanReviewBoundary(manifest) {
  const blockers = [];
  const hr = manifest.human_review_policy || manifest.human_review || {};

  if (hr.primary_classification_engine === true) {
    blockers.push({
      code: 'HUMAN_REVIEW_PRIMARY',
      message: BLOCKER_CODES.HUMAN_REVIEW_PRIMARY,
      required_remediation: ['automated reassessment', 'evidence enrichment', 'adjudication', 'domain-specific automation', 'approved exceptional manual mode'],
    });
  }

  if (hr.wholesale_abstain_to_operator === true) {
    blockers.push({
      code: 'HUMAN_REVIEW_PRIMARY',
      message: `${BLOCKER_CODES.HUMAN_REVIEW_PRIMARY} — unresolved ABSTAIN sent wholesale to operator`,
      required_remediation: ['automated reassessment', 'adjudication'],
    });
  }

  if (hr.classify_whole_corpus_requested === true) {
    blockers.push({
      code: 'HUMAN_REVIEW_PRIMARY',
      message: `${BLOCKER_CODES.HUMAN_REVIEW_PRIMARY} — operator asked to classify whole corpus`,
      required_remediation: ['automated reassessment', 'evidence enrichment', 'adjudication'],
    });
  }

  if (hr.no_automated_reassessment === true && hr.pending_review_count > 0) {
    blockers.push({
      code: 'HUMAN_REVIEW_PRIMARY',
      message: `${BLOCKER_CODES.HUMAN_REVIEW_PRIMARY} — no automated reassessment/adjudication attempt`,
      required_remediation: ['automated reassessment', 'adjudication'],
    });
  }

  if (hr.claims_automation === true && hr.manual_review_ratio === 1) {
    blockers.push({
      code: 'HUMAN_REVIEW_PRIMARY',
      message: `${BLOCKER_CODES.HUMAN_REVIEW_PRIMARY} — project claims automation while relying on full manual review`,
      required_remediation: ['domain-specific automation', 'approved exceptional manual mode'],
    });
  }

  const queueExceedsPolicy = hr.queue_exceeds_bounded_policy === true;
  if (queueExceedsPolicy && !hr.escalation_recorded) {
    blockers.push({
      code: 'HUMAN_REVIEW_PRIMARY',
      message: `${BLOCKER_CODES.HUMAN_REVIEW_PRIMARY} — mandatory human review queue exceeds bounded policy without escalation`,
      required_remediation: ['automated reassessment', 'adjudication', 'approved exceptional manual mode'],
      quantitative_limit: 'SAFE UNKNOWN — pending operator approval',
    });
  }

  return { valid: blockers.length === 0, blockers };
}
