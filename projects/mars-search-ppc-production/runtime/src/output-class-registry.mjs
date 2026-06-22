/**
 * MARS Search PPC — Output Class Registry and Quarantine (Wave 1.1)
 */
export const OUTPUT_CLASSES = {
  production_authority: {
    id: 'production_authority',
    description: 'Approved production SoT artifact',
    may_authorize_downstream: true,
  },
  proposal: {
    id: 'proposal',
    description: 'Proposed change awaiting approval',
    may_authorize_downstream: false,
  },
  diagnostic: {
    id: 'diagnostic',
    description: 'Diagnostic or pilot evidence only',
    may_authorize_downstream: false,
  },
  benchmark: {
    id: 'benchmark',
    description: 'Benchmark comparison artifact',
    may_authorize_downstream: false,
  },
  technical_pilot: {
    id: 'technical_pilot',
    description: 'Technical pilot slice',
    may_authorize_downstream: false,
  },
  draft: {
    id: 'draft',
    description: 'Unapproved draft',
    may_authorize_downstream: false,
  },
  superseded: {
    id: 'superseded',
    description: 'Replaced artifact — must not be used as authority',
    may_authorize_downstream: false,
  },
  export: {
    id: 'export',
    description: 'Transport/export artifact — not launch approval',
    may_authorize_downstream: false,
  },
  launch_evidence: {
    id: 'launch_evidence',
    description: 'Post-launch evidence pack',
    may_authorize_downstream: false,
  },
};

const QUARANTINE_RULES = [
  { from: 'diagnostic', as: 'production_authority', reason: 'diagnostic cannot be production authority' },
  { from: 'proposal', as: 'production_authority', reason: 'proposal cannot be approved authority' },
  { from: 'export', as: 'launch_evidence', reason: 'export cannot be launch approval' },
  { from: 'technical_pilot', as: 'production_authority', reason: 'pilot cannot substitute full corpus' },
  { from: 'draft', as: 'production_authority', reason: 'draft cannot be approved input' },
  { from: 'superseded', as: 'production_authority', reason: 'superseded evidence cannot authorize downstream' },
  { from: 'benchmark', as: 'production_authority', reason: 'benchmark cannot be production authority' },
];

export function validateOutputClass(artifactType, declaredClass, context = {}) {
  const cls = String(declaredClass || '').toLowerCase().replace(/[\s-]+/g, '_');
  if (!OUTPUT_CLASSES[cls]) {
    return {
      allowed: false,
      artifact: artifactType,
      declared_class: declaredClass,
      reason: `unknown output class: ${declaredClass}`,
    };
  }

  for (const rule of QUARANTINE_RULES) {
    if (cls === rule.from && context.assertedAs === rule.as) {
      return { allowed: false, artifact: artifactType, declared_class: cls, reason: rule.reason };
    }
  }

  if (context.requestedAsAuthority && !OUTPUT_CLASSES[cls].may_authorize_downstream) {
    const match = QUARANTINE_RULES.find((r) => r.from === cls);
    return {
      allowed: false,
      artifact: artifactType,
      declared_class: cls,
      reason: match?.reason || `${cls} cannot authorize downstream work`,
    };
  }

  return { allowed: true, artifact: artifactType, declared_class: cls };
}

export function rejectArtifactEntry(entry) {
  const issues = [];
  if (!entry) return { rejected: true, issues: ['artifact not registered'] };

  const cls = entry.output_class || entry.class;
  if (entry.status === 'DIAGNOSTIC ONLY' || entry.diagnostic_only === true) {
    issues.push('diagnostic cannot be production authority');
  }
  if (entry.status === 'PROPOSAL' || cls === 'proposal') {
    issues.push('proposal cannot be approved authority');
  }
  if (entry.status === 'SUPERSEDED' || entry.superseded === true || cls === 'superseded') {
    issues.push('superseded evidence cannot be used');
  }
  if (cls === 'export' && entry.asserted_launch_approval === true) {
    issues.push('export cannot be launch approval');
  }
  if (cls === 'technical_pilot' && entry.corpus_mode === 'PRODUCTION FULL CORPUS') {
    issues.push('pilot cannot substitute full corpus');
  }
  if (cls === 'draft' && entry.approved === true) {
    issues.push('draft cannot be approved input');
  }

  return { rejected: issues.length > 0, issues };
}

export function getOutputClassRegistry() {
  return { version: '1.0.0', classes: OUTPUT_CLASSES, quarantine_rules: QUARANTINE_RULES };
}
