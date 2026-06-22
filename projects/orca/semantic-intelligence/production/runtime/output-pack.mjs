import { sha256Json } from './lib.mjs';

export function buildOutputPack({
  runId, manifest, inputs, records, clusters, clusterQA, negatives, negConflicts, review, metrics, contractLoad, versions,
}) {
  const accept = records.filter((r) => r.adjudication_result?.outcome === 'FINAL ACCEPT');
  const reject = records.filter((r) => r.adjudication_result?.outcome === 'FINAL REJECT');
  const abstain = records.filter((r) => r.adjudication_result?.outcome === 'FINAL ABSTAIN');

  const runManifest = {
    run_id: runId,
    pack_version: 'semantic-output-pack-v1',
    generated_at: new Date().toISOString(),
    project_id: manifest?.project_id || inputs.corpus?.project_id || 'fixture',
    input_reconciliation: {
      expected_count: inputs.expectedCount,
      processed_count: records.length,
      reconciled: records.length === inputs.expectedCount,
    },
    runtime_versions: versions,
    contract_bundle: contractLoad?.bundleVersion,
    checksums: {},
  };

  const packBody = {
    run_manifest: runManifest,
    final_accept: accept.map(summarize),
    final_reject: reject.map(summarize),
    final_abstain: abstain.map(summarize),
    demand_tiers: groupByTier(accept),
    service_ownership: records.filter((r) => r.ownership).map((r) => ({ phrase_id: r.phrase_id, ...r.ownership })),
    ownership_conflicts: records.filter((r) => r.ownership?.outcome === 'OWNERSHIP CONFLICT'),
    clusters,
    cluster_qa: clusterQA,
    negative_library: negatives,
    negative_conflicts: negConflicts,
    bounded_review_queue: review.queue,
    metrics,
    output_class: 'PRODUCTION_SEMANTIC_PACK',
    complete: false,
  };

  runManifest.checksums.pack_body = sha256Json(packBody);

  const executionReceipt = {
    run_id: runId,
    ok: true,
    input_count: inputs.expectedCount,
    output_count: records.length,
    reconciled: records.length === inputs.expectedCount,
    review_queue_size: review.queue.length,
    cluster_count: clusters.length,
    negative_conflict_blocked: negConflicts.blocked,
    completed_at: new Date().toISOString(),
  };

  return {
    ...packBody,
    execution_receipt: executionReceipt,
    human_readable_summary: buildHumanSummary(metrics, clusters, review),
  };
}

function summarize(r) {
  return {
    phrase_id: r.phrase_id,
    raw_query: r.raw_query,
    decision: r.decision,
    demand_tier: r.demand_tier,
    service: r.ownership?.primary_service_id,
    cluster_id: r.cluster_id,
  };
}

function groupByTier(accepted) {
  const tiers = { T1: [], T2: [], T3: [], T4: [], T5: [] };
  for (const r of accepted) {
    if (r.demand_tier && tiers[r.demand_tier]) tiers[r.demand_tier].push(r.phrase_id);
  }
  return tiers;
}

function buildHumanSummary(metrics, clusters, review) {
  return {
    demand_by_tier: metrics.tier_counts,
    cluster_count: clusters.length,
    review_burden: { human: metrics.human_review_required, ratio: metrics.review_ratio },
    automation_primary: metrics.automation_primary,
    excluded_intent_families: Object.keys(metrics.protected_intent_counts || {}),
    unresolved_conflicts: metrics.unresolved_records,
  };
}
