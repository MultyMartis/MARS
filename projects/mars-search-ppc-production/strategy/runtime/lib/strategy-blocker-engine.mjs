/**
 * Strategy blocker engine — Wave 4
 */

export function collectStrategyBlockers(context) {
  const blockers = [];
  const {
    pack,
    readiness,
    architecture,
    alignment,
    measurement,
    budget,
    keywordPolicy,
    provisionalMode,
  } = context;

  for (const b of readiness?.blockers || pack?.blockers || []) {
    blockers.push(makeBlocker(b, 'SPPC-12', pack?.missing_evidence));
  }

  for (const b of architecture?.blockers || []) {
    blockers.push(makeBlocker(b.blocker || b, 'SPPC-14', b.service_id));
  }

  for (const r of alignment?.results || []) {
    if (r.blocks_activation) {
      blockers.push(makeBlocker(r.outcome, 'SPPC-17', r.campaign_id));
    }
  }

  for (const b of measurement?.blockers || []) {
    blockers.push(makeBlocker(b, 'SPPC-13', 'measurement'));
  }

  for (const b of budget?.blockers || []) {
    blockers.push(makeBlocker(b, 'SPPC-18', 'budget'));
  }

  if (keywordPolicy?.conflict_status === 'CONFLICT') {
    blockers.push(makeBlocker('negative_conflict', 'SPPC-15', 'negatives'));
  }

  if (provisionalMode && context.claimsProduction) {
    blockers.push(makeBlocker('provisional_strategy_marked_production', 'SPPC-13', null, false));
  }

  return {
    blocker_count: blockers.length,
    blockers,
    production_blocked: blockers.some((b) => !b.provisional_allowed),
  };
}

function makeBlocker(code, stage, artifact, provisionalAllowed = true) {
  const remediation = REMEDIATION[code] || `Resolve: ${code}`;
  return {
    code,
    blocking_stage: stage,
    missing_artifact_or_decision: artifact,
    remediation,
    provisional_strategy_allowed: provisionalAllowed && !code.includes('INVENTED'),
  };
}

const REMEDIATION = {
  'BLOCKED — PAID SERP LIVE EVIDENCE MISSING': 'Collect genuine Paid SERP evidence via MIG SPPC-10',
  'BLOCKED — SERVICE REGISTRY NOT APPROVED': 'Complete ORCA service ownership registry SPPC-07',
  'BLOCKED — EVIDENCE STALE': 'Refresh stale artifacts and re-register in manifest',
  'LANDING GAP': 'Provide landing inventory with aligned pages per service',
  'TRACKING GAP': 'Activate Metrica counter and conversion goals',
  'BUDGET DECISION REQUIRED': 'Operator must declare monthly budget',
  negative_conflict: 'Resolve negative phrase conflicts before activation',
  'provisional_strategy_marked_production': 'Remove production authority claim from provisional draft',
};
