import { nowIso, EVIDENCE_READINESS } from './utils.mjs';
import { assessFreshness } from './freshness.mjs';

export function buildEvidenceManifest({
  projectId,
  manifestPath,
  sourceRegistry,
  rawCorpus,
  canonicalRegistry,
  paidSerpSessions,
  competitorPack,
  orcaSemanticArtifacts,
  freshnessPolicy,
  degradedRecords,
}) {
  const missingOrca = [
    'commercial_admission_registry',
    'demand_tier_registry',
    'service_ownership_registry',
    'semantic_cluster_registry',
    'negative_intelligence_pack',
  ].filter((a) => !orcaSemanticArtifacts?.[a]);

  const freshness = assessFreshness({ paidSerpSessions, sourceRegistry, competitorPack, policy: freshnessPolicy });

  let readiness = 'MIG EVIDENCE PARTIAL';
  if (missingOrca.length) readiness = 'MIG EVIDENCE PARTIAL';
  if (!sourceRegistry?.sources?.length) readiness = 'MIG EVIDENCE BLOCKED';
  if (freshness.any_stale) readiness = 'STALE — RECOLLECTION REQUIRED';
  if (
    sourceRegistry?.sources?.length &&
    rawCorpus?.final_raw_corpus_count > 0 &&
    canonicalRegistry?.entry_count > 0 &&
    paidSerpSessions?.length &&
    competitorPack &&
    !freshness.any_stale &&
    !degradedRecords?.unapproved?.length
  ) {
    readiness = 'MIG EVIDENCE READY';
  }

  const manifest = {
    schema_version: '1.0.0',
    lifecycle_stage_contribution: 'SPPC-12',
    sppc_12_complete: false,
    sppc_12_complete_blocked_reason: 'BLOCKED — ORCA SEMANTIC EVIDENCE MISSING',
    project_id: projectId,
    manifest_path: manifestPath,
    generated_at: nowIso(),
    readiness,
    valid_readiness_values: EVIDENCE_READINESS,
    references: {
      business_scope_authority: manifestPath,
      source_registry: sourceRegistry,
      raw_corpus: rawCorpus,
      canonical_registry: canonicalRegistry,
      paid_serp_sessions: paidSerpSessions,
      competitor_evidence: competitorPack,
    },
    missing_orca_semantic_artifacts: missingOrca,
    evidence_freshness: freshness,
    degraded_evidence: degradedRecords || [],
    lifecycle_readiness_note:
      'MIG evidence contribution for SPPC-12 — does not mark full analytical pack complete without ORCA outputs',
  };

  if (manifest.sppc_12_complete && missingOrca.length) {
    return {
      ok: false,
      blockers: ['BLOCKED — EVIDENCE PACK CLAIMS SPPC-12 COMPLETE WITHOUT ORCA OUTPUTS'],
      manifest,
    };
  }

  return { ok: true, manifest, readiness };
}
