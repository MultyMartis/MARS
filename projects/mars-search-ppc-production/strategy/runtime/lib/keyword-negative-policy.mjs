/**
 * Keyword and negative distribution policy — Wave 4
 */

export function recommendKeywordNegativeDistribution(pack, architecture) {
  const admission = pack.demand_admission || {};
  const negatives = pack.negative_intelligence?.negatives || [];
  const clusters = pack.semantic_clusters?.clusters || [];
  const recommendations = {
    activate: [],
    watchlist: [],
    experimental: [],
    global_negatives: negatives.filter((n) => n.scope === 'global').map((n) => n.phrase),
    cross_negatives: [],
    unsafe_negative_warnings: [],
    conflict_status: 'CLEAR',
    overrides: [],
  };

  for (const cluster of clusters) {
    const tier = cluster.tier || cluster.demand_tier;
    const phrases = cluster.phrases || cluster.accepted_phrases || [];
    const owner = cluster.service_id || cluster.owner_service_id;
    const campaign = architecture.campaigns.find((c) => c.service_direction === owner);

    for (const phrase of phrases) {
      const entry = {
        phrase_id: phrase.phrase_id || phrase.id,
        phrase: phrase.text || phrase.normalized_query,
        cluster_id: cluster.cluster_id,
        campaign_id: campaign?.campaign_id,
        tier,
        ownership: owner,
      };
      if (phrase.decision === 'REJECT') {
        recommendations.unsafe_negative_warnings.push({ ...entry, warning: 'rejected_phrase_must_not_activate' });
        continue;
      }
      if (tier === 'T5') recommendations.experimental.push(entry);
      else if (tier === 'T4') recommendations.watchlist.push(entry);
      else recommendations.activate.push(entry);
    }
  }

  const conflicts = detectNegativeConflicts(negatives, recommendations.activate);
  if (conflicts.length) {
    recommendations.conflict_status = 'CONFLICT';
    recommendations.unsafe_negative_warnings.push(...conflicts);
  }

  return recommendations;
}

function detectNegativeConflicts(negatives, activate) {
  const conflicts = [];
  const negSet = new Set(negatives.map((n) => (n.phrase || n.text || '').toLowerCase()));
  for (const a of activate) {
    if (negSet.has((a.phrase || '').toLowerCase())) {
      conflicts.push({ phrase: a.phrase, warning: 'negative_conflict' });
    }
  }
  return conflicts;
}
