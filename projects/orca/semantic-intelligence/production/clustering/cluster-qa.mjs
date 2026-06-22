export function runClusterQA(clusters, ownershipMap, records) {
  const defects = [];
  const phraseToCluster = new Map();
  const acceptedIds = new Set(records.filter((r) => r.adjudication_result?.outcome === 'FINAL ACCEPT').map((r) => r.phrase_id));

  for (const c of clusters) {
    const services = new Set();
    const tasks = new Set();
    const scenarios = new Set();
    const landings = new Set();
    const tiers = new Set(c.demand_tiers || []);

    for (const pid of c.phrase_ids) {
      if (phraseToCluster.has(pid)) {
        defects.push({ type: 'duplicate_phrase_ownership', phrase_id: pid, clusters: [phraseToCluster.get(pid), c.cluster_id] });
      }
      phraseToCluster.set(pid, c.cluster_id);
      const own = ownershipMap.get(pid);
      if (own) {
        services.add(own.primary_service_id);
        tasks.add(own.user_task);
        scenarios.add(own.commercial_scenario);
        landings.add(own.landing_candidate);
      }
    }

    if (services.size > 1) defects.push({ type: 'mixed_services', cluster_id: c.cluster_id, services: [...services] });
    if (tasks.size > 1) defects.push({ type: 'mixed_user_tasks', cluster_id: c.cluster_id, tasks: [...tasks] });
    if (scenarios.size > 1) defects.push({ type: 'mixed_commercial_scenarios', cluster_id: c.cluster_id });
    if (landings.size > 1) defects.push({ type: 'incompatible_landing', cluster_id: c.cluster_id, landings: [...landings] });
    if (tiers.has('T1') && tiers.has('T5')) defects.push({ type: 'direct_and_experimental_mixed', cluster_id: c.cluster_id });
    if (c.phrase_ids.length > 200) defects.push({ type: 'overly_broad_cluster', cluster_id: c.cluster_id, count: c.phrase_ids.length });
  }

  for (const pid of acceptedIds) {
    if (!phraseToCluster.has(pid)) {
      defects.push({ type: 'orphan_phrase', phrase_id: pid });
    }
  }

  const major = defects.filter((d) =>
    ['mixed_services', 'mixed_user_tasks', 'duplicate_phrase_ownership', 'orphan_phrase', 'incompatible_landing'].includes(d.type));

  return {
    defects,
    major_defects: major,
    campaign_production_blocked: major.length > 0,
    summary: { total_defects: defects.length, major: major.length },
  };
}
