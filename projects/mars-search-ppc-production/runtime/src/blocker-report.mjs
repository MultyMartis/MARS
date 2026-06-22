export function buildBlockerReport(result, manifest, options = {}) {
  const requested = options.requested_stage || options.requested_action || manifest.current_lifecycle_stage;

  return {
    status: result.status,
    project_id: manifest.project_id,
    project_name: manifest.project_name,
    current_lifecycle_stage: manifest.current_lifecycle_stage,
    requested_stage_or_action: requested,
    missing_required_inputs: result.missing_required_inputs || [],
    invalid_or_insufficient_evidence: result.invalid_evidence || [],
    required_system_or_role: result.required_owners || [],
    allowed_next_action: result.allowed_next_action || [],
    forbidden_until_resolved: result.forbidden_until_resolved || [],
    degraded_mode_available: result.degraded_mode_available === 'YES' || result.degraded_mode_available === true ? 'YES' : 'NO',
    operator_approval_required: result.operator_approval_required ? 'YES' : 'NO',
    blockers: result.blockers || [],
    blocker_codes: (result.blockers || []).map((b) => b.code),
  };
}

export function formatBlockerReportMd(report) {
  const lines = [
    'STATUS: BLOCKED',
    '',
    `Project: ${report.project_id}`,
    `Current lifecycle stage: ${report.current_lifecycle_stage}`,
    `Requested stage/action: ${report.requested_stage_or_action}`,
    '',
    'Missing required inputs:',
    ...(report.missing_required_inputs.length
      ? report.missing_required_inputs.map((x) => `- ${x}`)
      : ['- (none)']),
    '',
    'Invalid or insufficient evidence:',
    ...(report.invalid_or_insufficient_evidence.length
      ? report.invalid_or_insufficient_evidence.map((x) => `- ${typeof x === 'string' ? x : `${x.id}: ${(x.issues || []).join(', ')}`}`)
      : ['- (none)']),
    '',
    'Required system/role:',
    ...(report.required_system_or_role.length
      ? report.required_system_or_role.map((x) => `- ${x}`)
      : ['- (none)']),
    '',
    'Allowed next action:',
    ...(report.allowed_next_action.length
      ? report.allowed_next_action.map((x) => `- ${x}`)
      : ['- (none)']),
    '',
    'Forbidden until resolved:',
    ...(report.forbidden_until_resolved.length
      ? report.forbidden_until_resolved.map((x) => `- ${x}`)
      : ['- (none)']),
    '',
    `Degraded mode available: ${report.degraded_mode_available}`,
    `Operator approval required: ${report.operator_approval_required}`,
  ];

  if (report.status === 'BLOCKED') {
    lines.unshift('BLOCKED — LIFECYCLE REQUIREMENT NOT MET', '');
  }

  return lines.join('\n');
}
