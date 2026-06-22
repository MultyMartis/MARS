export const QUERY_SELECTION_MODES = {
  production_governed: {
    description: 'Consumes approved T1/T2 and cluster artifacts',
    requires: ['t1_direct_commercial', 't2_problem_demand', 'cluster_artifacts'],
    contaminates_semantic_authority: false,
  },
  pre_semantic_research: {
    description: 'Operator-approved commercial seed queries for market observation only',
    requires: ['operator_approved_seeds'],
    contaminates_semantic_authority: false,
    labels: ['research_seed', 'not_semantic_core', 'not_commercial_admission'],
  },
};

export function selectQueries({ mode, seeds, approvedArtifacts }) {
  if (mode === 'pre_semantic_research') {
    return (seeds || []).map((q, i) => ({
      query_id: `seed-${i + 1}`,
      query: typeof q === 'string' ? q : q.query,
      selection_rationale: 'operator-approved research seed',
      authority: 'research_seed',
      commercial_admission: false,
      semantic_core: false,
    }));
  }

  const candidates = [];
  for (const src of ['t1_direct_commercial', 'strategic_high_value', 'core_service_clusters', 't2_problem_demand']) {
    const items = approvedArtifacts?.[src] || [];
    for (const item of items) {
      candidates.push({
        query_id: item.id || item.query,
        query: item.query || item.phrase,
        selection_rationale: src,
        authority: 'production_governed',
      });
    }
  }
  return candidates;
}
