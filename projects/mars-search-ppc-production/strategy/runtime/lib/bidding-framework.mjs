/**
 * Bidding strategy framework — Wave 4
 */

export const BIDDING_APPROACHES = [
  'manual_bidding',
  'automated_conversion_strategy',
  'hybrid_staged_launch',
  'low_data_cold_start',
  'experiment_campaign',
  'protected_budget_campaign',
];

export function recommendBiddingFramework(pack, architecture, measurement, options = {}) {
  const hasConversions = (measurement?.conversion_history?.count || 0) > 0;
  const trackingReady = measurement?.metrica_counter?.status === 'active';
  const recommendations = [];

  for (const campaign of architecture.campaigns) {
    let approach = 'manual_bidding';
    const tier = campaign.demand_tiers?.[0];
    const blockers = [];

    if (tier === 'T5') {
      approach = 'experiment_campaign';
    } else if (!trackingReady) {
      approach = 'manual_bidding';
      blockers.push('TRACKING GAP — auto bidding blocked');
    } else if (!hasConversions) {
      approach = options.coldStart ? 'low_data_cold_start' : 'hybrid_staged_launch';
      blockers.push('conversion_history_insufficient_for_auto');
    } else if (campaign.budget_role === 'high') {
      approach = 'automated_conversion_strategy';
    }

    if (options.autoWithoutConversions && approach === 'automated_conversion_strategy' && !hasConversions) {
      blockers.push('BLOCKED — auto strategy without conversion evidence');
      approach = 'manual_bidding';
    }

    recommendations.push({
      campaign_id: campaign.campaign_id,
      bidding_approach: approach,
      rationale: blockers.length ? blockers : ['data_maturity_matched'],
      exact_bids_known: false,
      auction_evidence_required: true,
      blockers,
    });
  }

  return {
    framework_id: `bid-${pack.project_identity?.project_id || 'unknown'}-v1`,
    recommendations,
    no_exact_bids_without_auction: true,
  };
}
