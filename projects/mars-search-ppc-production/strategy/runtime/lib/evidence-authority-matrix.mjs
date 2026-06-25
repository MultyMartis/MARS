/**
 * Evidence authority matrix — Wave 4
 */
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';

export const AUTHORITY_CLASSES = [
  'PRODUCTION AUTHORITY',
  'APPROVED EVIDENCE',
  'APPROVED WITH DEGRADATION',
  'PROVISIONAL',
  'PROPOSAL',
  'DIAGNOSTIC',
  'TECHNICAL TEST',
  'STALE',
  'BLOCKED',
  'SUPERSEDED',
];

const DIAGNOSTIC_MARKERS = /diagnostic|synthetic|pilot|mock|fixture-only|do not promote/i;
const STALE_DAYS_DEFAULT = 90;

export function checksumFile(filePath) {
  if (!filePath || !fs.existsSync(filePath)) return null;
  const data = fs.readFileSync(filePath);
  return crypto.createHash('sha256').update(data).digest('hex');
}

export function classifyArtifactAuthority(entry, content = null) {
  if (!entry?.path) {
    return { authority_level: 'BLOCKED', limitations: ['missing_path'] };
  }
  if (entry.status === 'BLOCKED' || entry.authority === 'BLOCKED') {
    return { authority_level: 'BLOCKED', limitations: ['manifest_blocked'] };
  }
  if (entry.synthetic === true || content?.synthetic === true) {
    return { authority_level: 'TECHNICAL TEST', limitations: ['synthetic_fixture'] };
  }
  if (isDiagnosticContent(content, entry)) {
    return { authority_level: 'DIAGNOSTIC', limitations: ['diagnostic_only'] };
  }
  if (entry.degraded_mode === true || content?.degraded_mode === true) {
    return { authority_level: 'APPROVED WITH DEGRADATION', limitations: ['degraded_evidence'] };
  }
  if (entry.status === 'REGISTERED' && entry.approved !== false) {
    return { authority_level: 'APPROVED EVIDENCE', limitations: [] };
  }
  if (entry.status === 'PROVISIONAL') {
    return { authority_level: 'PROVISIONAL', limitations: ['provisional_not_production'] };
  }
  return { authority_level: 'PROPOSAL', limitations: ['unapproved'] };
}

export function isProductionEligible(authorityLevel) {
  return ['PRODUCTION AUTHORITY', 'APPROVED EVIDENCE', 'APPROVED WITH DEGRADATION'].includes(authorityLevel);
}

export function buildEvidenceAuthorityMatrix(manifest, repoRoot, options = {}) {
  const staleDays = options.staleDays ?? STALE_DAYS_DEFAULT;
  const now = options.now ? new Date(options.now) : new Date();
  const registry = manifest.artifact_registry || {};
  const entries = [];

  for (const [artifactType, entry] of Object.entries(registry)) {
    const absPath = entry.path ? path.resolve(repoRoot, entry.path) : null;
    let content = null;
    let checksum = null;
    let exists = false;
    if (absPath && fs.existsSync(absPath)) {
      exists = true;
      try {
        content = JSON.parse(fs.readFileSync(absPath, 'utf8'));
      } catch {
        content = fs.readFileSync(absPath, 'utf8');
      }
      checksum = checksumFile(absPath);
    }
    const { authority_level, limitations } = classifyArtifactAuthority(entry, content);
    let freshness = 'UNKNOWN';
    const collected = content?.collected_at || content?.as_of || entry.collected_at;
    if (collected) {
      const ageMs = now - new Date(collected);
      const ageDays = ageMs / (86400 * 1000);
      freshness = ageDays > staleDays ? 'STALE' : 'CURRENT';
      if (freshness === 'STALE' && authority_level === 'APPROVED EVIDENCE') {
        limitations.push('stale_evidence');
      }
    } else if (exists) {
      freshness = 'CURRENT';
    }

    const effectiveAuthority = freshness === 'STALE' && !limitations.includes('degraded_evidence')
      ? 'STALE'
      : authority_level;

    entries.push({
      artifact_id: `${manifest.project_id || 'unknown'}:${artifactType}`,
      project_id: manifest.project_id,
      artifact_type: artifactType,
      producer: entry.producer || inferProducer(artifactType),
      lifecycle_stage: inferStage(artifactType),
      output_class: artifactType,
      status: entry.status || 'UNKNOWN',
      authority_level: effectiveAuthority,
      freshness,
      checksum,
      path: entry.path,
      exists,
      limitations: [...limitations],
      permitted_consumers: permittedConsumers(effectiveAuthority),
      production_eligible: isProductionEligible(effectiveAuthority) && freshness !== 'STALE',
    });
  }

  return {
    matrix_id: `eam-${manifest.project_id || 'unknown'}-v1`,
    project_id: manifest.project_id,
    generated_at: now.toISOString(),
    entries,
  };
}

function inferProducer(artifactType) {
  if (artifactType.includes('serp') || artifactType.includes('competitor') || artifactType.includes('source')) return 'MIG';
  if (artifactType.includes('semantic') || artifactType.includes('admission') || artifactType.includes('tier') || artifactType.includes('cluster') || artifactType.includes('negative')) return 'ORCA';
  if (artifactType.includes('analytical') || artifactType.includes('strategy')) return 'STRATEGY';
  if (artifactType.includes('business')) return 'ATLAS';
  return 'UNKNOWN';
}

function inferStage(artifactType) {
  const map = {
    business_scope_operator_authority: 'SPPC-01',
    source_registry: 'SPPC-02',
    full_semantic_corpus_intake: 'SPPC-03',
    canonical_phrase_registry: 'SPPC-04',
    commercial_admission_registry: 'SPPC-05',
    demand_tier_registry: 'SPPC-06',
    service_ownership_registry: 'SPPC-07',
    semantic_cluster_registry: 'SPPC-08',
    negative_intelligence_pack: 'SPPC-09',
    paid_serp_business_hours_evidence: 'SPPC-10',
    competitor_advertising_audit: 'SPPC-11',
    dated_analytical_pack: 'SPPC-12',
    ppc_strategy_decision_record: 'SPPC-13',
  };
  return map[artifactType] || 'UNKNOWN';
}

function permittedConsumers(authorityLevel) {
  if (isProductionEligible(authorityLevel)) return ['SPPC-12', 'SPPC-13', 'SPPC-14'];
  if (authorityLevel === 'PROVISIONAL') return ['SPPC-12-draft', 'SPPC-13-provisional'];
  if (authorityLevel === 'DIAGNOSTIC' || authorityLevel === 'TECHNICAL TEST') return ['regression_only'];
  return [];
}

export function validateAuthorityForConsumer(matrix, artifactType, consumerStage) {
  const entry = matrix.entries.find((e) => e.artifact_type === artifactType);
  if (!entry) return { ok: false, blocker: 'BLOCKED — ARTIFACT NOT IN MATRIX' };
  if (!entry.production_eligible && consumerStage === 'SPPC-13-production') {
    return { ok: false, blocker: `BLOCKED — ${entry.authority_level} cannot authorize production strategy` };
  }
  if (!entry.permitted_consumers.includes(consumerStage) && !entry.permitted_consumers.some((c) => consumerStage.startsWith(c))) {
    return { ok: false, blocker: `BLOCKED — ${artifactType} not permitted for ${consumerStage}` };
  }
  return { ok: true, entry };
}

function isDiagnosticContent(content, entry) {
  if (entry?.diagnostic === true || content?.diagnostic === true) return true;
  if (content?.authority_classification === 'DIAGNOSTIC') return true;
  const scopedText = `${content?.note || ''} ${content?.authority_classification || ''} ${typeof content === 'string' ? content : ''}`;
  return DIAGNOSTIC_MARKERS.test(scopedText);
}
