const TASK_PATTERNS = [
  { re: /внедр|миграц/i, task: 'implementation', serviceHint: 'svc-implementation' },
  { re: /настройк|установк/i, task: 'configuration', serviceHint: 'svc-configuration' },
  { re: /доработ|интеграц|обмен/i, task: 'modification', serviceHint: 'svc-modification' },
  { re: /сопровожд|обслужив|аудит|консультац/i, task: 'support', serviceHint: 'svc-support' },
  { re: /программист|разработчик|специалист/i, task: 'hire_specialist', serviceHint: 'svc-hire' },
  { re: /не\s+работ|ошибк|восстанов|починить/i, task: 'problem_resolution', serviceHint: 'svc-support' },
  { re: /маркиров|честн/i, task: 'marking_compliance', serviceHint: 'svc-marking' },
];

export function assignOwnership(record, serviceRegistry) {
  if (record.adjudication_result?.outcome !== 'FINAL ACCEPT') {
    return { outcome: 'SKIPPED', reason: 'not_final_accept' };
  }

  const approved = (serviceRegistry?.services || []).filter((s) => s.operator_status === 'APPROVED');
  if (!approved.length) {
    return { outcome: 'SERVICE GAP', reason: 'no_approved_services' };
  }

  const text = record.normalized_query || record.raw_query || '';
  const matches = TASK_PATTERNS.filter((p) => p.re.test(text));
  const candidates = [];

  for (const m of matches) {
    const svc = approved.find((s) => s.service_id === m.serviceHint)
      || approved.find((s) => (s.included_tasks || []).includes(m.task));
    if (svc) candidates.push({ service: svc, task: m.task, confidence: 0.75 });
  }

  if (!candidates.length) {
    const fallback = approved.sort((a, b) => (b.commercial_priority || 0) - (a.commercial_priority || 0))[0];
    if (fallback) {
      candidates.push({ service: fallback, task: 'general_commercial', confidence: 0.45 });
    }
  }

  if (!candidates.length) {
    return { outcome: 'SERVICE GAP', reason: 'no_matching_service' };
  }

  const primary = candidates[0];
  const secondary = candidates[1] || null;
  const conflict = candidates.length > 1
    && candidates[0].service.service_id !== candidates[1].service.service_id
    && candidates[0].confidence < 0.7;

  const landing = (primary.service.landing_candidates || [])[0] || null;
  if (!landing) {
    return {
      outcome: 'LANDING GAP',
      primary_service_id: primary.service.service_id,
      user_task: primary.task,
      ownership_confidence: primary.confidence,
    };
  }

  return {
    outcome: conflict ? 'OWNERSHIP CONFLICT' : 'OWNED',
    primary_service_id: primary.service.service_id,
    primary_service_name: primary.service.name,
    secondary_candidate: secondary?.service.service_id || null,
    user_task: primary.task,
    commercial_scenario: inferScenario(record),
    ownership_confidence: primary.confidence,
    rationale: `Matched task ${primary.task} to ${primary.service.service_id}`,
    landing_candidate: landing,
    conflict_state: conflict ? 'UNRESOLVED_MULTI_SERVICE' : 'NONE',
  };
}

function inferScenario(record) {
  const tier = record.demand_tier;
  if (tier === 'T1') return 'explicit_hire_or_quote';
  if (tier === 'T2') return 'problem_requires_specialist';
  return 'extended_service_demand';
}

export function validateSingleOwner(ownershipByPhrase) {
  const owners = new Map();
  const duplicates = [];
  for (const [phraseId, own] of ownershipByPhrase) {
    if (own.outcome !== 'OWNED' && own.outcome !== 'OWNERSHIP CONFLICT') continue;
    const key = own.primary_service_id;
    if (!owners.has(phraseId)) owners.set(phraseId, key);
    else if (owners.get(phraseId) !== key) duplicates.push(phraseId);
  }
  return { valid: duplicates.length === 0, duplicates };
}
