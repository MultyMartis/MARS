/**
 * Campaign architecture recommendation — strategy level (not Commander rows)
 */

export function recommendCampaignArchitecture(pack, activationPolicy, options = {}) {
  const clusters = pack.semantic_clusters?.clusters || [];
  const ownership = pack.service_ownership?.services || [];
  const campaigns = [];
  const blockers = [];

  const byService = groupClustersByService(clusters, ownership);

  for (const [serviceId, serviceClusters] of Object.entries(byService)) {
    const tiers = [...new Set(serviceClusters.map((c) => c.tier || c.demand_tier))];
    const primaryTier = tiers.includes('T1') ? 'T1' : tiers[0];
    const policy = activationPolicy.policies[primaryTier];
    if (!policy || policy.launch_status?.startsWith('BLOCKED')) {
      blockers.push({ service_id: serviceId, blocker: 'tier_activation_blocked' });
      continue;
    }
    if (policy.launch_status === 'DEFERRED' && options.launchMode === 't1_only') {
      continue;
    }

    const landing = resolveLanding(serviceId, pack.landing_inventory);
    if (!landing && policy.landing_requirement === 'mandatory_aligned') {
      blockers.push({ service_id: serviceId, blocker: 'LANDING GAP — campaign cannot authorize without landing path' });
    }

    campaigns.push({
      campaign_id: `camp-${serviceId}-${primaryTier}`,
      purpose: `Activate ${primaryTier} demand for service ${serviceId}`,
      service_direction: serviceId,
      included_clusters: serviceClusters.map((c) => c.cluster_id),
      excluded_clusters: [],
      demand_tiers: tiers,
      geography: pack.geography,
      schedule: options.schedule || 'business_hours_default',
      landing: landing?.url || null,
      conversion: pack.business_authority?.primary_conversion || 'lead',
      budget_role: policy.budget_priority,
      experiment_status: primaryTier === 'T5' ? 'isolated_experiment' : 'production',
      dependencies: [`service_ownership:${serviceId}`],
      blockers: landing ? [] : ['LANDING GAP'],
    });
  }

  return {
    architecture_id: `arch-${pack.project_identity?.project_id || 'unknown'}-v1`,
    hierarchy: ['portfolio', 'campaign', 'service_direction', 'cluster_group', 'demand_tier', 'geography', 'landing', 'offer', 'measurement'],
    campaigns,
    blockers,
    portfolio: {
      project_id: pack.project_identity?.project_id,
      campaign_count: campaigns.length,
    },
  };
}

function groupClustersByService(clusters, services) {
  const map = {};
  for (const c of clusters) {
    const sid = c.service_id || c.owner_service_id || 'unassigned';
    if (!map[sid]) map[sid] = [];
    map[sid].push(c);
  }
  if (map.unassigned?.length) {
    return { unassigned: map.unassigned };
  }
  return map;
}

function resolveLanding(serviceId, inventory) {
  const pages = inventory?.pages || inventory?.landings || [];
  return pages.find((p) => p.service_id === serviceId && p.status !== 'unavailable');
}
