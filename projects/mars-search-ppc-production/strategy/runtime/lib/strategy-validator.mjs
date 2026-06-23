/**
 * Strategy validator — Wave 4
 */

export function validateSearchPpcStrategy(strategy, pack, options = {}) {
  const violations = [];

  if (strategy.strategy_status === 'PRODUCTION READY' && pack.pack_readiness !== 'COMPLETE') {
    violations.push({ code: 'provisional_claims_production' });
  }

  for (const rec of strategy.blockers || []) {
    if (strategy.strategy_status?.includes('COMPLETE') && rec.code?.includes('PAID SERP')) {
      violations.push({ code: 'missing_paid_serp_hidden' });
    }
  }

  if (!strategy.supporting_evidence_ids?.length && !options.allowProvisional) {
    violations.push({ code: 'no_evidence_linkage' });
  }

  for (const campaign of strategy.campaign_segmentation?.campaigns || []) {
    if (!campaign.landing && campaign.blockers?.includes('LANDING GAP')) {
      violations.push({ code: 'campaign_without_landing', campaign_id: campaign.campaign_id });
    }
    if (campaign.service_direction === 'unassigned') {
      violations.push({ code: 'cluster_without_owner_activated', campaign_id: campaign.campaign_id });
    }
  }

  const activated = strategy.keyword_activation_policy?.activate || [];
  const rejected = strategy.keyword_activation_policy?.unsafe_negative_warnings || [];
  for (const a of activated) {
    if (rejected.some((r) => r.phrase === a.phrase)) {
      violations.push({ code: 'rejected_phrase_activated', phrase: a.phrase });
    }
  }

  if (strategy.budget_framework?.total_monthly_budget && options.budgetNotApproved) {
    violations.push({ code: 'budget_invented' });
  }

  if (strategy.tier_activation_policy?.policies?.T5?.must_not_merge_with_main_launch === false) {
    violations.push({ code: 't5_mixed_into_main' });
  }

  if (strategy.keyword_activation_policy?.conflict_status === 'CONFLICT' && !strategy.blockers?.some((b) => b.code === 'negative_conflict')) {
    violations.push({ code: 'negative_conflict_ignored' });
  }

  return {
    ok: violations.length === 0,
    violations,
    verdict: violations.length === 0 ? 'PASS' : 'FAIL',
  };
}
