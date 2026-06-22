import fs from 'node:fs';
import path from 'node:path';
import { loadContracts } from '../../integration/runtime/src/contract-loader.mjs';
import { validateInvariants } from '../../integration/runtime/src/invariant-validator.mjs';
import { authorizeProductionRun, validateCorpusMode } from './production-gate.mjs';
import { loadProductionInputs, loadCorpusFromFixture } from './corpus-loader.mjs';
import { buildProductionRecord, PRODUCTION_VERSION } from './record-builder.mjs';
import { assignOwnership } from '../ownership/ownership-engine.mjs';
import { buildClusters } from '../clustering/cluster-builder.mjs';
import { runClusterQA } from '../clustering/cluster-qa.mjs';
import { buildNegativeIntelligence } from '../negatives/negative-intelligence.mjs';
import { validateNegativeConflicts } from '../negatives/negative-conflict-validator.mjs';
import { routeBoundedReview } from '../conflict-queue/review-router.mjs';
import { writeJson, sha256Json, BLOCKERS, PRODUCTION_VERSION as VER, readJson } from './lib.mjs';
import { buildOutputPack } from './output-pack.mjs';

const DEFAULT_BATCH_SIZE = 100;

export async function runFullCorpusProduction(options) {
  const started = Date.now();
  const runId = options.runId || `orca-sem-${new Date().toISOString().replace(/[:.]/g, '-')}`;
  const outDir = options.outDir;
  fs.mkdirSync(outDir, { recursive: true });

  let manifest = null;
  let inputs;

  if (options.fixtureCorpus) {
    inputs = loadCorpusFromFixture(options.fixtureCorpus);
    if (options.requireManifest !== false && !options.manifestPath) {
      throw new Error('fixture runs in production mode require manifest unless requireManifest=false (diagnostic only)');
    }
  } else {
    const auth = authorizeProductionRun({ manifestPath: options.manifestPath });
    if (!auth.ok) return failRun(runId, auth.message, outDir);
    manifest = auth.manifest;
    inputs = loadProductionInputs(manifest);
    const corpusCheck = validateCorpusMode(
      { phrase_count: inputs.phrases.length, corpus_mode: manifest.artifact_registry?.canonical_phrase_registry?.corpus_mode },
      inputs.expectedCount,
    );
    if (!corpusCheck.ok) return failRun(runId, corpusCheck.message, outDir);
  }

  if (!inputs.serviceRegistry && !options.allowMissingServiceRegistry) {
    return failRun(runId, BLOCKERS.MISSING_REGISTRY, outDir);
  }

  let contractLoad = { ok: true, bundleVersion: 'p0-i-bundle-v1' };
  if (!options.skipContractLoad) {
    contractLoad = loadContracts({ lockPath: options.lockPath });
    if (!contractLoad.ok) return failRun(runId, BLOCKERS.CONTRACT_CHECKSUM, outDir);
  }

  const checkpointPath = path.join(outDir, 'checkpoint-v1.json');
  let checkpoint = fs.existsSync(checkpointPath) ? readJson(checkpointPath) : { processed_ids: [], batch_index: 0 };
  const processedSet = new Set(checkpoint.processed_ids || []);

  const batchSize = options.batchSize || DEFAULT_BATCH_SIZE;
  const records = [];
  const versions = {
    business_scope_version: inputs.businessScope?.version || 'v1',
    service_registry_version: inputs.serviceRegistry?.version || 'v1',
    policy_version: 'orca-semantic-admission-policy-v1',
  };

  const context = {
    businessScope: inputs.businessScope,
    serviceRegistry: inputs.serviceRegistry,
    commercialPolicy: options.commercialPolicy || {},
  };

  for (const phrase of inputs.phrases) {
    if (processedSet.has(phrase.phrase_id)) continue;

    let record = buildProductionRecord(phrase, context, versions);

    const invRecord = toInvariantRecord(record, phrase);
    const inv = validateInvariants(invRecord, {
      abstain_supported: true,
      provenance_status: 'COMPLETE',
      protected_strata_conflict: record.primary_assessment?.protected_strata_conflict,
    });
    record.invariant_results = inv.findings;

    if (inv.blocked && record.adjudication_result.outcome === 'FINAL ACCEPT') {
      record.adjudication_result = {
        ...record.adjudication_result,
        outcome: 'FINAL ABSTAIN',
        final_decision: 'ABSTAIN',
        human_review_required: true,
        findings: [...(record.adjudication_result.findings || []), 'invariant_blocked'],
      };
      record.final_authority = 'FINAL ABSTAIN';
      record.decision = 'ABSTAIN';
      record.commercial_eligibility = false;
      record.demand_tier = null;
    }

    records.push(record);
    processedSet.add(phrase.phrase_id);

    if (records.length % batchSize === 0) {
      writeJson(checkpointPath, {
        run_id: runId,
        processed_ids: [...processedSet],
        batch_index: checkpoint.batch_index + 1,
        last_phrase_id: phrase.phrase_id,
        provenance: { resumed: checkpoint.processed_ids?.length > 0 },
      });
      checkpoint.batch_index += 1;
    }
  }

  if (processedSet.size !== inputs.phrases.length) {
    return failRun(runId, BLOCKERS.COUNT_MISMATCH, outDir, { expected: inputs.phrases.length, got: processedSet.size });
  }

  const ownershipMap = new Map();
  for (const rec of records) {
    const own = assignOwnership(rec, inputs.serviceRegistry);
    rec.ownership = own;
    ownershipMap.set(rec.phrase_id, own);
  }

  const accepted = records.filter((r) => r.adjudication_result?.outcome === 'FINAL ACCEPT');
  const clusters = buildClusters(accepted, ownershipMap);
  const clusterQA = runClusterQA(clusters, ownershipMap, records);

  for (const rec of accepted) {
    const cluster = clusters.find((c) => c.phrase_ids.includes(rec.phrase_id));
    if (cluster) rec.cluster_id = cluster.cluster_id;
  }

  const negatives = buildNegativeIntelligence(records, clusters, ownershipMap);
  const negConflicts = validateNegativeConflicts(negatives, records, clusters);
  const review = routeBoundedReview(records, options.reviewConfig || {});

  const metrics = buildMetrics(records, review, clusterQA, negConflicts, started);

  const pack = buildOutputPack({
    runId,
    manifest,
    inputs,
    records,
    clusters,
    clusterQA,
    negatives,
    negConflicts,
    review,
    metrics,
    contractLoad,
    versions: { runtime: VER, assessor: records[0]?.assessor_version },
  });

  if (records.length !== inputs.phrases.length) {
    pack.complete = false;
    pack.blocker = BLOCKERS.COUNT_MISMATCH;
    writeJson(path.join(outDir, 'semantic-output-pack-v1.json'), pack);
    return failRun(runId, BLOCKERS.COUNT_MISMATCH, outDir, pack);
  }

  if (options.markComplete === false) {
    pack.complete = false;
    pack.blocker = BLOCKERS.PARTIAL_COMPLETE;
  } else {
    pack.complete = true;
  }

  writeJson(path.join(outDir, 'semantic-output-pack-v1.json'), pack);
  writeJson(path.join(outDir, 'run-manifest-v1.json'), pack.run_manifest);
  writeJson(path.join(outDir, 'execution-receipt-v1.json'), pack.execution_receipt);
  writeJson(path.join(outDir, 'automation-metrics-v1.json'), metrics);
  writeJson(path.join(outDir, 'review-queue-v1.json'), review);
  fs.unlinkSync(checkpointPath);

  return { ok: true, runId, outDir, pack, metrics };
}

function toInvariantRecord(record, phrase) {
  return {
    query_id: record.phrase_id,
    provenance_status: 'COMPLETE',
    primary_intent: record.primary_intent,
    signals: record.primary_assessment?.signals || [],
    ambiguity: record.primary_assessment?.ambiguity || { severity: 'LOW', types: [] },
    commercial_eligibility: {
      decision: record.primary_assessment?.decision || record.decision,
      supporting_evidence: record.commercial_evidence,
      opposing_evidence: record.non_commercial_evidence,
      confidence: record.confidence,
    },
    service_candidate: { mapping_status: 'NOT_STARTED', candidate_service_ids: [] },
    versioning: { taxonomy_version: 'v1', schema_version: 'v1', guideline_version: 'v1' },
    raw_query: phrase.raw_query,
    normalized_query: phrase.normalized_query,
  };
}

function buildMetrics(records, review, clusterQA, negConflicts, started) {
  const accept = records.filter((r) => r.adjudication_result?.outcome === 'FINAL ACCEPT').length;
  const reject = records.filter((r) => r.adjudication_result?.outcome === 'FINAL REJECT').length;
  const abstain = records.filter((r) => r.adjudication_result?.outcome === 'FINAL ABSTAIN').length;
  const tiers = {};
  for (const r of records) {
    if (r.demand_tier) tiers[r.demand_tier] = (tiers[r.demand_tier] || 0) + 1;
  }
  return {
    corpus_size: records.length,
    automatically_finalized: review.metrics.automated_final,
    human_review_required: review.metrics.human_review,
    review_ratio: review.metrics.review_ratio,
    accept, reject, abstain,
    protected_intent_counts: review.metrics.protected_classes,
    reassessment_count: records.filter((r) => r.reassessment_result).length,
    adjudication_count: records.length,
    tier_counts: tiers,
    ownership_conflicts: records.filter((r) => r.ownership?.outcome === 'OWNERSHIP CONFLICT').length,
    service_gaps: records.filter((r) => r.ownership?.outcome === 'SERVICE GAP').length,
    cluster_defects: clusterQA.summary.major,
    negative_conflicts: negConflicts.conflicts.length,
    runtime_failures: 0,
    unresolved_records: records.filter((r) => r.adjudication_result?.outcome?.startsWith('ESCALATE')).length,
    elapsed_ms: Date.now() - started,
    automation_primary: review.metrics.automation_primary,
  };
}

function failRun(runId, message, outDir, detail = {}) {
  writeJson(path.join(outDir, 'execution-receipt-v1.json'), {
    run_id: runId,
    ok: false,
    blocker: message,
    detail,
    completed_at: new Date().toISOString(),
  });
  return { ok: false, blocker: message, detail };
}
