import crypto from 'node:crypto';

export function routeHumanReview(record, config = {}, context = {}) {
  const decision = record.commercial_eligibility?.decision;
  const risk = record.risk?.overall_risk;
  const ambiguity = record.ambiguity || {};
  const types = new Set(ambiguity.types || []);
  const routes = [];
  const reasons = [];

  const push = (code, reason) => {
    routes.push(code);
    reasons.push(reason);
  };

  if (decision === 'ABSTAIN') push('ABSTAIN_MANDATORY', 'Every ABSTAIN requires human review');
  if (['HIGH', 'CRITICAL'].includes(risk)) push('HIGH_RISK', `Risk level ${risk}`);
  if (context.protected_strata_conflict) push('PROTECTED_STRATA', 'Protected strata conflict');
  if (types.has('SHORT_HEAD_TERM')) push('SHORT_HEAD', 'Short-head ambiguity');
  if (types.has('INTENT') && ambiguity.severity !== 'LOW') push('PROBLEM_QUERY', 'Problem-query ambiguity');
  if (types.has('PRODUCT_VS_SERVICE')) push('PRODUCT_SERVICE', 'Product/service conflict');
  if (types.has('CAREER_VS_PROVIDER')) push('CAREER_PROVIDER', 'Career/provider conflict');
  if (types.has('PROVIDER_VS_DIY')) push('PROVIDER_DIY', 'Provider/DIY conflict');
  if (context.assessor_disagreement) push('ASSESSOR_DISAGREEMENT', 'Assessor disagreement');
  if ((context.invariant_warnings || []).length) push('INVARIANT_WARNING', 'Invariant warning requires review');

  const acceptAuditRate = config.random_accept_audit_rate ?? 0;
  const rejectAuditRate = config.random_reject_audit_rate ?? 0;
  const seed = `${record.query_id}:${config.audit_seed || 'fixture'}`;
  const bucket = deterministicBucket(seed);

  if (decision === 'ACCEPT' && acceptAuditRate > 0 && bucket < acceptAuditRate) {
    push('RANDOM_ACCEPT_AUDIT', 'Configured random ACCEPT audit');
  }
  if (decision === 'REJECT' && rejectAuditRate > 0 && bucket < rejectAuditRate) {
    push('RANDOM_REJECT_AUDIT', 'Configured random REJECT audit');
  }

  const routed = routes.length > 0 || record.commercial_eligibility?.reviewer_required;
  const reviewTask = routed
    ? {
        task_id: `review-${record.query_id}`,
        query_id: record.query_id,
        routes,
        reasons,
        automated_decision_preserved: decision,
        automated_output_snapshot: {
          commercial_eligibility: { ...record.commercial_eligibility },
          primary_intent: record.primary_intent,
          risk: record.risk,
        },
        status: 'QUEUED',
        created_at: new Date().toISOString(),
      }
    : null;

  return {
    routed,
    routes,
    reasons,
    review_task: reviewTask,
    workflow_status: routed ? 'PENDING_HUMAN_REVIEW' : record.review?.workflow_status || 'AUTO_SCREENED',
  };
}

function deterministicBucket(seed) {
  const h = crypto.createHash('sha256').update(seed).digest();
  return h[0] / 255;
}
