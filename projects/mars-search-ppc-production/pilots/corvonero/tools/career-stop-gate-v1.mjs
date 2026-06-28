/**
 * Corvonero Run 004 Phase 4 — evidence-based career ACCEPT stop gate.
 * Support-layer only; does not modify ORCA adjudication.
 */

export const CAREER_ACCEPT_CLASSIFICATION = {
  RAW_CLASSIFIER_FLAG: 'RAW_CLASSIFIER_FLAG',
  CONFIRMED_POLICY_ERROR: 'CONFIRMED_POLICY_ERROR',
  OPERATOR_REVIEW_REQUIRED: 'OPERATOR_REVIEW_REQUIRED',
  CLASSIFIER_FALSE_POSITIVE: 'CLASSIFIER_FALSE_POSITIVE',
  OPERATOR_OVERRIDE: 'OPERATOR_OVERRIDE',
};

const COMMERCIAL_PRICE_WORK =
  /(?:сколько\s+стоит\s+работа|стоимость\s+работ(?:ы|)|цена\s+работ(?:ы|)|стоимость\s+услуг|расценки\s+специалиста|стоимость\s+работ\s+по)/i;
const PAYROLL_MODULE_SERVICE =
  /(?:(?:сопровожден|настройк|внедрен|обслуживан|доработк|конфигурац|модул|подсистем|обновлен|установк|подключ).{0,40}(?:зарплат|кадр)|(?:зарплат|кадр)\s+и\s+кадр)/i;
const CAREER_SALARY_MARKER =
  /(?:зарплат(?:а|ы)\s+(?:программист(?:а|ом|у|ы|ов|ами|е)?|разработчик(?:а|ом|у|ы|ов|ами|е)?|специалист(?:а|ом|у|ы|ов|ами|е)?)|зарплат(?:а|ы).{0,20}(?:ваканс|работ(?:а|у)\s+программист))/i;

const EXPLICIT_CAREER_MARKERS =
  /(?:ваканс|стажер|стажировк|резюме|работа\s+программист(?:ом|ами|ов|ке)|работа\s+разработчик(?:ом|ами|ов|ке)|ищу\s+работ|собеседован|работодател|трудоустройств|устроиться|карьер)/i;

const MONITORED_CAREER_PATTERNS =
  /(?:стажер|стажировк|ваканс|работа\s+программист(?:ом|ами|ов|ке)|ищу\s+работ|резюме|зарплат|собеседован)/i;

export function isCommercialPriceWorkConstruction(text) {
  return COMMERCIAL_PRICE_WORK.test(text);
}

export function isPayrollModuleServiceContext(text) {
  return PAYROLL_MODULE_SERVICE.test(text);
}

export function hasExplicitCareerEvidence(text) {
  if (isCommercialPriceWorkConstruction(text) || isPayrollModuleServiceContext(text)) return false;
  if (CAREER_SALARY_MARKER.test(text)) return true;
  return EXPLICIT_CAREER_MARKERS.test(text);
}

export function isCareerRelatedAccept(record) {
  const text = (record.normalized_phrase || record.phrase || '').toLowerCase();
  const authoritativeVerdict = record.final_authoritative_verdict || record.final_verdict;
  if (authoritativeVerdict !== 'ACCEPT') return false;
  if (record.observed_tags?.includes('career')) return true;
  if (record.primary_family === 'careers_training_education') return true;
  if (hasExplicitCareerEvidence(text)) return true;
  return false;
}

export function classifyCareerAccept(record, classifierResult = null, operatorOverrides = new Map()) {
  const phraseId = record.phrase_id;
  const text = (record.normalized_phrase || record.phrase || '').toLowerCase();
  const modelVerdict = record.model_verdict || record.final_verdict;
  const authoritativeVerdict = record.final_authoritative_verdict || record.final_verdict;

  if (operatorOverrides.has(phraseId)) {
    const ov = operatorOverrides.get(phraseId);
    return {
      phrase_id: phraseId,
      classification: CAREER_ACCEPT_CLASSIFICATION.OPERATOR_OVERRIDE,
      contributes_to_stop: false,
      model_verdict: ov.model_verdict || modelVerdict,
      final_authoritative_verdict: ov.operator_final_verdict,
      rationale: ov.rationale,
    };
  }

  if (authoritativeVerdict !== 'ACCEPT') {
    return null;
  }

  if (
    record.primary_verdict === 'REJECT' &&
    record.reassessment_verdict === 'REJECT' &&
    modelVerdict === 'ACCEPT' &&
    !operatorOverrides.has(phraseId)
  ) {
    return {
      phrase_id: phraseId,
      phrase: record.phrase,
      classification: CAREER_ACCEPT_CLASSIFICATION.OPERATOR_REVIEW_REQUIRED,
      contributes_to_stop: false,
      model_verdict: modelVerdict,
      final_authoritative_verdict: authoritativeVerdict,
      rationale: 'Primary/reassessment consensus REJECT contradicts final ACCEPT — review item, not broad stop contributor',
    };
  }

  const cls = classifierResult || {};
  const tagSource = cls.observed_tags ?? record.observed_tags ?? [];
  const familySource = cls.primary_family ?? record.primary_family;
  const hasCareerTag = tagSource.includes('career');
  const careerFamily = familySource === 'careers_training_education';

  if (!hasCareerTag && !careerFamily && !hasExplicitCareerEvidence(text)) {
    return null;
  }

  if (isCommercialPriceWorkConstruction(text)) {
    return {
      phrase_id: phraseId,
      phrase: record.phrase,
      classification: CAREER_ACCEPT_CLASSIFICATION.CLASSIFIER_FALSE_POSITIVE,
      contributes_to_stop: false,
      model_verdict: modelVerdict,
      final_authoritative_verdict: authoritativeVerdict,
      rationale: 'Service-price construction overrides bare "работа" career heuristic',
    };
  }

  if (isPayrollModuleServiceContext(text)) {
    return {
      phrase_id: phraseId,
      phrase: record.phrase,
      classification: CAREER_ACCEPT_CLASSIFICATION.CLASSIFIER_FALSE_POSITIVE,
      contributes_to_stop: false,
      model_verdict: modelVerdict,
      final_authoritative_verdict: authoritativeVerdict,
      rationale: 'Payroll/HR module service context — not employment career intent',
    };
  }

  if (hasExplicitCareerEvidence(text) || (hasCareerTag && careerFamily)) {
    if (cls.expected_verdict === 'REJECT' || careerFamily) {
      return {
        phrase_id: phraseId,
        phrase: record.phrase,
        classification: CAREER_ACCEPT_CLASSIFICATION.CONFIRMED_POLICY_ERROR,
        contributes_to_stop: true,
        model_verdict: modelVerdict,
        final_authoritative_verdict: authoritativeVerdict,
        rationale: 'Explicit career evidence with policy-derived REJECT expectation but model ACCEPT',
      };
    }
  }

  if (hasCareerTag && !hasExplicitCareerEvidence(text)) {
    return {
      phrase_id: phraseId,
      phrase: record.phrase,
      classification: CAREER_ACCEPT_CLASSIFICATION.CLASSIFIER_FALSE_POSITIVE,
      contributes_to_stop: false,
      model_verdict: modelVerdict,
      final_authoritative_verdict: authoritativeVerdict,
      rationale: 'Career tag without explicit employment markers — classifier false positive',
    };
  }

  return {
    phrase_id: phraseId,
    phrase: record.phrase,
    classification: CAREER_ACCEPT_CLASSIFICATION.OPERATOR_REVIEW_REQUIRED,
    contributes_to_stop: false,
    model_verdict: modelVerdict,
    final_authoritative_verdict: authoritativeVerdict,
    rationale: 'Ambiguous career-related ACCEPT — operator review required',
  };
}

export function analyzeCareerAcceptGate(allResults, classifiedById = new Map(), operatorOverrides = new Map()) {
  const items = [];
  let rawCount = 0;

  for (const record of allResults) {
    const cls = classifiedById.get(record.phrase_id);
    if (!isCareerRelatedAccept(record)) continue;
    rawCount++;
    const item = classifyCareerAccept(record, cls, operatorOverrides);
    if (item) items.push(item);
  }

  const counts = {
    career_accept_raw_count: rawCount,
    career_accept_confirmed_error_count: 0,
    career_accept_classifier_false_positive_count: 0,
    career_accept_review_pending_count: 0,
    career_accept_override_count: 0,
  };

  for (const item of items) {
    switch (item.classification) {
      case CAREER_ACCEPT_CLASSIFICATION.CONFIRMED_POLICY_ERROR:
        counts.career_accept_confirmed_error_count++;
        break;
      case CAREER_ACCEPT_CLASSIFICATION.CLASSIFIER_FALSE_POSITIVE:
        counts.career_accept_classifier_false_positive_count++;
        break;
      case CAREER_ACCEPT_CLASSIFICATION.OPERATOR_REVIEW_REQUIRED:
        counts.career_accept_review_pending_count++;
        break;
      case CAREER_ACCEPT_CLASSIFICATION.OPERATOR_OVERRIDE:
        counts.career_accept_override_count++;
        break;
      default:
        break;
    }
  }

  counts.career_accept_rate = allResults.length
    ? Number((rawCount / allResults.length).toFixed(6))
    : 0;

  const confirmedErrors = items.filter(
    (i) => i.classification === CAREER_ACCEPT_CLASSIFICATION.CONFIRMED_POLICY_ERROR && i.contributes_to_stop,
  );
  const unresolvedConfirmed = confirmedErrors.filter(
    (i) => !operatorOverrides.has(i.phrase_id),
  );

  const stopIssues = [];
  if (unresolvedConfirmed.length >= 2) {
    stopIssues.push('career_education_acceptance_family');
  }
  if (unresolvedConfirmed.length >= 1 && rawCount >= 3) {
    const rate = unresolvedConfirmed.length / Math.max(rawCount, 1);
    if (rate >= 0.5 && unresolvedConfirmed.length >= 2) {
      stopIssues.push('career_education_systematic_pattern');
    }
  }

  return {
    ...counts,
    items,
    confirmed_error_ids: confirmedErrors.map((i) => i.phrase_id),
    unresolved_confirmed_error_ids: unresolvedConfirmed.map((i) => i.phrase_id),
    stop_issues: stopIssues,
    stop_required: stopIssues.length > 0,
    monitored_patterns: MONITORED_CAREER_PATTERNS.source,
  };
}

export function buildImmediateCareerReviewList(allResults, classifiedById = new Map()) {
  const review = [];
  for (const record of allResults) {
    const text = (record.normalized_phrase || record.phrase || '').toLowerCase();
    const verdict = record.final_authoritative_verdict || record.final_verdict;
    if (verdict !== 'ACCEPT') continue;
    if (isCommercialPriceWorkConstruction(text)) continue;
    if (
      MONITORED_CAREER_PATTERNS.test(text) ||
      record.observed_tags?.includes('career') ||
      classifiedById.get(record.phrase_id)?.observed_tags?.includes('career')
    ) {
      review.push({
        phrase_id: record.phrase_id,
        phrase: record.phrase,
        final_verdict: verdict,
        observed_tags: record.observed_tags,
        primary_family: record.primary_family,
        review_reason: 'career_related_accept_monitor',
        added_at: new Date().toISOString(),
      });
    }
  }
  return review;
}
