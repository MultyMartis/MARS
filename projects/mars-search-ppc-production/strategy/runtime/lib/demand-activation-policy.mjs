/**
 * Demand activation policy T1–T5 — Wave 4
 */

export function buildDemandActivationPolicy(tierDistribution, options = {}) {
  const policies = {};
  const launchMode = options.launchMode || 'staged';

  policies.T1 = {
    tier: 'T1',
    launch_status: 'PRIMARY_LAUNCH',
    campaign_class: 'core_conversion',
    budget_priority: 'high',
    bid_priority: 'high',
    landing_requirement: 'mandatory_aligned',
    measurement_requirement: 'conversion_goals_required',
    exclusion_risk: 'low',
  };

  policies.T2 = {
    tier: 'T2',
    launch_status: launchMode === 't1_only' ? 'DEFERRED' : 'CONTROLLED_LAUNCH',
    campaign_class: 'problem_commercial',
    budget_priority: launchMode === 't1_only' ? 'none' : 'medium',
    bid_priority: 'medium',
    landing_requirement: 'mandatory_aligned',
    measurement_requirement: 'conversion_goals_required',
    exclusion_risk: 'medium',
  };

  policies.T3 = {
    tier: 'T3',
    launch_status: 'SECONDARY',
    campaign_class: 'extended_service',
    budget_priority: 'low',
    bid_priority: 'low',
    landing_requirement: 'service_specific',
    measurement_requirement: 'lead_or_consult',
    exclusion_risk: 'medium',
  };

  policies.T4 = {
    tier: 'T4',
    launch_status: 'WATCHLIST',
    campaign_class: 'supplementary',
    budget_priority: 'minimal',
    bid_priority: 'minimal',
    landing_requirement: 'optional',
    measurement_requirement: 'awareness_or_lead',
    exclusion_risk: 'high',
  };

  policies.T5 = {
    tier: 'T5',
    launch_status: 'ISOLATED_EXPERIMENT',
    campaign_class: 'experiment',
    budget_priority: 'capped_experiment',
    bid_priority: 'conservative',
    landing_requirement: 'experiment_landing',
    measurement_requirement: 'isolated_measurement',
    exclusion_risk: 'high',
    isolation_required: true,
    must_not_merge_with_main_launch: true,
  };

  if (options.t5MixedIntoMain) {
    policies.T5.launch_status = 'BLOCKED — T5 MUST NOT MERGE WITH MAIN LAUNCH';
  }

  return {
    activation_policy_id: `dap-${options.projectId || 'unknown'}-tiers-v1`,
    tier_distribution: tierDistribution,
    policies,
    merge_all_tiers_forbidden: true,
  };
}
