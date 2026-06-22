import { nowIso } from './utils.mjs';

export function assessFreshness({ paidSerpSessions, sourceRegistry, competitorPack, policy = {} }) {
  const classes = {
    source_corpus: assessClass(sourceRegistry?.updated_at, policy.source_corpus),
    paid_serp: assessClass(paidSerpSessions?.[0]?.generated_at, policy.paid_serp),
    competitor_ads: assessClass(competitorPack?.generated_at, policy.competitor_ads),
    landing_evidence: assessClass(competitorPack?.landing_evidence?.[0]?.capture_timestamp, policy.landing_evidence),
  };

  const anyStale = Object.values(classes).some((c) => c.stale);
  return { classes, any_stale: anyStale, policy_source: 'project_or_lifecycle' };
}

function assessClass(collectedAt, policyClass) {
  if (!collectedAt) return { collected_at: null, stale: false, required_recollection: false, note: 'not yet collected' };
  if (!policyClass?.valid_through_days) {
    return { collected_at: collectedAt, stale: false, valid_through: null, note: 'no expiry configured' };
  }
  const collected = new Date(collectedAt);
  const validThrough = new Date(collected);
  validThrough.setDate(validThrough.getDate() + policyClass.valid_through_days);
  const stale = new Date() > validThrough;
  return {
    collected_at: collectedAt,
    valid_through: validThrough.toISOString(),
    stale,
    required_recollection: stale,
  };
}

export function buildDegradedRecord({
  completedQueries,
  incompleteQueries,
  reason,
  evidence,
  impact,
  retryRecommendation,
  lifecycleContinuationPermitted,
  operatorApprovalRequired,
}) {
  return {
    schema_version: '1.0.0',
    recorded_at: nowIso(),
    completed_queries: completedQueries,
    incomplete_queries: incompleteQueries,
    reason,
    evidence,
    impact,
    retry_recommendation: retryRecommendation,
    lifecycle_continuation_permitted: lifecycleContinuationPermitted ?? false,
    operator_approval_required: operatorApprovalRequired ?? true,
    collection_status: 'COLLECTION DEGRADED',
  };
}
