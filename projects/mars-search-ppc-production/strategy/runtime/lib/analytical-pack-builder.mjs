/**
 * Analytical pack builder — SPPC-12 Wave 4
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { buildEvidenceAuthorityMatrix } from './evidence-authority-matrix.mjs';
import { assessPackReadiness } from './pack-readiness.mjs';
import { createStatement } from './statement-model.mjs';

function loadJson(filePath) {
  return JSON.parse(fs.readFileSync(filePath, 'utf8'));
}

function loadEvidenceArtifact(repoRoot, entry) {
  if (!entry?.path) return null;
  const abs = path.resolve(repoRoot, entry.path);
  if (!fs.existsSync(abs)) return null;
  try {
    return loadJson(abs);
  } catch {
    return { raw_path: entry.path };
  }
}

export function buildDatedAnalyticalPack(params) {
  const {
    manifest,
    repoRoot,
    analysisPeriod,
    options = {},
  } = params;

  if (!manifest?.project_id) {
    return { ok: false, blocker: 'BLOCKED — MANIFEST INVALID', exit_code: 2 };
  }

  const matrix = buildEvidenceAuthorityMatrix(manifest, repoRoot, options);
  const readiness = assessPackReadiness(matrix, options);
  const registry = manifest.artifact_registry || {};
  const evidence = {};

  for (const [key, entry] of Object.entries(registry)) {
    evidence[key] = loadEvidenceArtifact(repoRoot, entry);
  }

  const statements = [];
  const tierDist = summarizeTiers(evidence.demand_tier_registry);
  if (tierDist) {
    statements.push(createStatement({
      statementId: 'STMT-TIER-DIST',
      statementType: 'OBSERVED FACT',
      text: `T1–T5 distribution recorded in demand tier registry`,
      supportingEvidenceIds: [matrix.entries.find((e) => e.artifact_type === 'demand_tier_registry')?.artifact_id].filter(Boolean),
      confidence: 0.95,
      affectedStrategySections: ['demand_priorities', 'tier_activation'],
    }));
  }

  const packId = `dap-${manifest.project_id}-${analysisPeriod?.end || new Date().toISOString().slice(0, 10)}-v1`;
  const pack = {
    schema_version: '1.0.0',
    pack_id: packId,
    project_identity: {
      project_id: manifest.project_id,
      project_name: manifest.project_name,
      platform: manifest.platform || 'Yandex Direct',
      campaign_type: manifest.campaign_type || 'search',
    },
    business_authority: evidence.business_scope_operator_authority,
    analysis_period: analysisPeriod || { start: null, end: new Date().toISOString().slice(0, 10), timezone: manifest.timezone || 'UTC' },
    evidence_inventory: matrix.entries.map((e) => ({
      artifact_id: e.artifact_id,
      artifact_type: e.artifact_type,
      authority_level: e.authority_level,
      checksum: e.checksum,
      freshness: e.freshness,
    })),
    source_coverage: evidence.source_registry,
    corpus_summary: evidence.full_semantic_corpus_intake,
    demand_admission: {
      accepted: evidence.commercial_admission_registry?.accepted_count ?? null,
      rejected: evidence.commercial_admission_registry?.rejected_count ?? null,
      abstain: evidence.commercial_admission_registry?.abstain_count ?? null,
    },
    tier_distribution: tierDist,
    service_ownership: evidence.service_ownership_registry,
    semantic_clusters: evidence.semantic_cluster_registry,
    negative_intelligence: evidence.negative_intelligence_pack,
    paid_serp_evidence: evidence.paid_serp_business_hours_evidence,
    competitor_advertising: evidence.competitor_advertising_audit,
    competitor_landing: evidence.competitor_advertising_audit?.landing_evidence || null,
    landing_inventory: evidence.landing_inventory || options.landingInventory || null,
    offer_inventory: evidence.offer_inventory || options.offerInventory || null,
    geography: manifest.region || evidence.business_scope_operator_authority?.geography,
    historical_campaigns: options.historicalCampaigns || null,
    data_limitations: collectLimitations(matrix),
    stale_evidence: readiness.stale_evidence,
    missing_evidence: readiness.missing_evidence,
    statements,
    readiness_assessment: readiness,
    pack_readiness: readiness.readiness,
    blockers: readiness.blockers,
  };

  const receipt = {
    receipt_id: `sppc-receipt-${Date.now()}-${crypto.randomBytes(4).toString('hex')}`,
    stage: 'SPPC-12',
    pack_id: packId,
    readiness: readiness.readiness,
    generated_at: new Date().toISOString(),
    checksum: crypto.createHash('sha256').update(JSON.stringify(pack)).digest('hex'),
  };

  return {
    ok: readiness.readiness !== 'BLOCKED' || readiness.provisional_allowed,
    pack,
    matrix,
    readiness,
    receipt,
    exit_code: readiness.readiness === 'COMPLETE' || readiness.readiness === 'COMPLETE WITH APPROVED DEGRADATION' ? 0 : 2,
  };
}

function summarizeTiers(tierRegistry) {
  if (!tierRegistry?.tiers) return null;
  const dist = { T1: 0, T2: 0, T3: 0, T4: 0, T5: 0 };
  for (const row of tierRegistry.tiers) {
    const t = row.tier || row.demand_tier;
    if (dist[t] !== undefined) dist[t]++;
  }
  return dist;
}

function collectLimitations(matrix) {
  const limits = [];
  for (const e of matrix.entries) {
    if (e.limitations?.length) limits.push({ artifact_type: e.artifact_type, limitations: e.limitations });
  }
  return limits;
}
