/**
 * Pack readiness levels — Wave 4 SPPC-12
 */

export const READINESS_LEVELS = [
  'COMPLETE',
  'COMPLETE WITH APPROVED DEGRADATION',
  'PARTIAL — PROVISIONAL ONLY',
  'BLOCKED',
];

export const MANDATORY_ARTIFACTS = [
  'business_scope_operator_authority',
  'source_registry',
  'full_semantic_corpus_intake',
  'commercial_admission_registry',
  'demand_tier_registry',
  'service_ownership_registry',
  'semantic_cluster_registry',
  'negative_intelligence_pack',
  'paid_serp_business_hours_evidence',
];

export function assessPackReadiness(matrix, options = {}) {
  const blockers = [];
  const missing = [];
  const stale = [];
  let hasDegradation = false;

  for (const artifactType of MANDATORY_ARTIFACTS) {
    const entry = matrix.entries.find((e) => e.artifact_type === artifactType);
    if (!entry || !entry.exists) {
      missing.push(artifactType);
      blockers.push(blockerForMissing(artifactType));
      continue;
    }
    if (entry.freshness === 'STALE') stale.push(artifactType);
    if (entry.authority_level === 'DIAGNOSTIC' || entry.authority_level === 'TECHNICAL TEST') {
      blockers.push(`BLOCKED — ${artifactType.toUpperCase().replace(/_/g, ' ')} IS DIAGNOSTIC ONLY`);
    }
    if (entry.authority_level === 'APPROVED WITH DEGRADATION') hasDegradation = true;
    if (!entry.production_eligible && artifactType === 'paid_serp_business_hours_evidence') {
      blockers.push('BLOCKED — PAID SERP LIVE EVIDENCE MISSING');
    }
  }

  if (missing.includes('paid_serp_business_hours_evidence')) {
    return {
      readiness: 'BLOCKED',
      blockers: ['BLOCKED — PAID SERP LIVE EVIDENCE MISSING'],
      missing_evidence: missing,
      stale_evidence: stale,
      provisional_allowed: true,
    };
  }
  if (missing.includes('service_ownership_registry')) {
    blockers.push('BLOCKED — SERVICE REGISTRY NOT APPROVED');
  }
  if (stale.length) {
    blockers.push('BLOCKED — EVIDENCE STALE');
  }
  if (blockers.length) {
    const provisionalOnly = missing.length > 0 || stale.length > 0
      || matrix.entries.some((e) => MANDATORY_ARTIFACTS.includes(e.artifact_type) && !e.production_eligible);
    return {
      readiness: provisionalOnly && !missing.includes('business_scope_operator_authority')
        ? 'PARTIAL — PROVISIONAL ONLY'
        : 'BLOCKED',
      blockers: [...new Set(blockers)],
      missing_evidence: missing,
      stale_evidence: stale,
      provisional_allowed: provisionalOnly,
    };
  }
  if (hasDegradation) {
    return {
      readiness: 'COMPLETE WITH APPROVED DEGRADATION',
      blockers: [],
      missing_evidence: [],
      stale_evidence: [],
      provisional_allowed: false,
    };
  }
  return {
    readiness: 'COMPLETE',
    blockers: [],
    missing_evidence: [],
    stale_evidence: [],
    provisional_allowed: false,
  };
}

function blockerForMissing(artifactType) {
  const map = {
    business_scope_operator_authority: 'BLOCKED — BUSINESS AUTHORITY MISSING',
    source_registry: 'BLOCKED — SOURCE REGISTRY MISSING',
    full_semantic_corpus_intake: 'BLOCKED — CORPUS INTAKE MISSING',
    commercial_admission_registry: 'BLOCKED — ORCA SEMANTIC PACK MISSING',
    demand_tier_registry: 'BLOCKED — DEMAND TIER REGISTRY MISSING',
    service_ownership_registry: 'BLOCKED — SERVICE REGISTRY NOT APPROVED',
    semantic_cluster_registry: 'BLOCKED — CLUSTER REGISTRY MISSING',
    negative_intelligence_pack: 'BLOCKED — NEGATIVE INTELLIGENCE MISSING',
    paid_serp_business_hours_evidence: 'BLOCKED — PAID SERP LIVE EVIDENCE MISSING',
  };
  return map[artifactType] || `BLOCKED — ${artifactType.toUpperCase()} MISSING`;
}
