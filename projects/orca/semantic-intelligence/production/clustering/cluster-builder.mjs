export function buildClusters(acceptedRecords, ownershipMap) {
  const groups = new Map();

  for (const rec of acceptedRecords) {
    const own = ownershipMap.get(rec.phrase_id);
    if (!own || (own.outcome !== 'OWNED' && own.outcome !== 'OWNERSHIP CONFLICT')) continue;

    const key = [
      own.primary_service_id,
      own.user_task,
      own.commercial_scenario,
      rec.demand_tier,
      own.landing_candidate,
    ].join('::');

    if (!groups.has(key)) {
      groups.set(key, {
        cluster_key: key,
        service_owner: own.primary_service_id,
        user_task: own.user_task,
        commercial_scenario: own.commercial_scenario,
        demand_tiers: new Set(),
        landing_candidate: own.landing_candidate,
        phrase_ids: [],
        representative_phrases: [],
        offer_direction: inferOfferDirection(own, rec),
        exclusion_boundaries: [],
        confidence: 0,
      });
    }
    const g = groups.get(key);
    g.phrase_ids.push(rec.phrase_id);
    g.demand_tiers.add(rec.demand_tier);
    if (g.representative_phrases.length < 5) g.representative_phrases.push(rec.raw_query);
    g.confidence = Math.max(g.confidence, own.ownership_confidence || 0);
  }

  const clusters = [];
  let idx = 0;
  for (const g of groups.values()) {
    idx += 1;
    clusters.push({
      cluster_id: `CLU-${String(idx).padStart(4, '0')}`,
      name: `${g.service_owner} — ${g.user_task}`,
      service_owner: g.service_owner,
      phrase_ids: g.phrase_ids,
      representative_phrases: g.representative_phrases,
      user_task: g.user_task,
      demand_tiers: [...g.demand_tiers],
      offer_direction: g.offer_direction,
      landing_candidate: g.landing_candidate,
      exclusion_boundaries: g.exclusion_boundaries,
      neighboring_clusters: [],
      confidence: g.confidence,
      unresolved_conflicts: [],
    });
  }

  for (let i = 0; i < clusters.length; i++) {
    for (let j = i + 1; j < clusters.length; j++) {
      if (clusters[i].service_owner === clusters[j].service_owner && clusters[i].user_task !== clusters[j].user_task) {
        clusters[i].neighboring_clusters.push(clusters[j].cluster_id);
        clusters[j].neighboring_clusters.push(clusters[i].cluster_id);
      }
    }
  }

  return clusters;
}

function inferOfferDirection(own, rec) {
  if (rec.demand_tier === 'T1') return 'explicit_cta_quote_or_contact';
  if (rec.demand_tier === 'T2') return 'problem_resolution_cta';
  return 'service_exploration_cta';
}
