/**
 * Build operator semantic exclusion registry v1 from authoritative sources.
 */
import fs from 'node:fs';
import path from 'node:path';

export function normPhrase(p) {
  return String(p || '')
    .toLowerCase()
    .replace(/ё/g, 'е')
    .replace(/\s+/g, ' ')
    .trim();
}

const V71_CONFIRMED = [
  {
    exclusion_id: 'EXC-V71-001',
    normalized_phrase: '1с программист без образования',
    variants: ['1с программист без образования'],
    category: 'EDUCATIONAL_CAREER',
    authority_source: 'v5-collision-actions-final.json CF-0016; v5-career-education-query-audit; v7.1 regression repair',
    first_decision_version: 'v5',
    last_confirmed_version: 'v7.1',
    reason: 'Educational qualification intent — not provider hire.',
    override_policy: 'operator_approved_override_only',
  },
  {
    exclusion_id: 'EXC-V71-002',
    normalized_phrase: 'программист 1с без высшего образования',
    variants: ['программист 1с без высшего образования'],
    category: 'EDUCATIONAL_CAREER',
    authority_source: 'v5-collision-actions-final.json; v5-career-education-query-audit; v7.1 regression repair',
    first_decision_version: 'v5',
    last_confirmed_version: 'v7.1',
    reason: 'Educational qualification intent — not provider hire.',
    override_policy: 'operator_approved_override_only',
  },
  {
    exclusion_id: 'EXC-V71-003',
    normalized_phrase: 'задание программисту 1с',
    variants: ['задание программисту 1с'],
    category: 'AMBIGUOUS_INLINE_MINUS_RESCUE',
    authority_source: 'v7.1 phrase review; destructive inline-minus tail in v7 export',
    first_decision_version: 'v5',
    last_confirmed_version: 'v7.1',
    reason: 'Ambiguous base phrase; v7 used long inline-negative rescue tail.',
    override_policy: 'operator_approved_override_only',
  },
  {
    exclusion_id: 'EXC-V71-004',
    normalized_phrase: 'часа программиста 1с',
    variants: ['часа программиста 1с'],
    category: 'UNNATURAL_MALFORMED',
    authority_source: 'v7.1 phrase review; unnatural generator artefact',
    first_decision_version: 'v5',
    last_confirmed_version: 'v7.1',
    reason: 'Grammatically broken / unnatural phrase without stable commercial formulation.',
    override_policy: 'operator_approved_override_only',
  },
  {
    exclusion_id: 'EXC-V71-005',
    normalized_phrase: 'образование программист 1с',
    variants: ['образование программист 1с'],
    category: 'EDUCATIONAL_CAREER',
    authority_source: 'v5-career-education-query-audit; v5-collision-actions-final.json',
    first_decision_version: 'v5',
    last_confirmed_version: 'v7.1',
    reason: 'Education intent — wrongly restored by v7 scope recovery.',
    override_policy: 'operator_approved_override_only',
  },
  {
    exclusion_id: 'EXC-V71-006',
    normalized_phrase: 'программист 1с высшее образование',
    variants: ['программист 1с высшее образование'],
    category: 'EDUCATIONAL_CAREER',
    authority_source: 'v5-career-education-query-audit; v5-collision-actions-final.json',
    first_decision_version: 'v5',
    last_confirmed_version: 'v7.1',
    reason: 'Education intent — wrongly restored by v7 scope recovery.',
    override_policy: 'operator_approved_override_only',
  },
];

const V5_HARD_INFORMATIONAL = [
  'маркировка лекарств проверить',
  'маркировка автозапчастей 2026',
  'маркировка автозапчастей честный знак 2026',
  '1с программист 2026',
];

export function buildExclusionRegistry(root) {
  const exclusions = [...V71_CONFIRMED];
  let seq = 100;

  for (const phrase of V5_HARD_INFORMATIONAL) {
    exclusions.push({
      exclusion_id: `EXC-V5-INFO-${seq++}`,
      normalized_phrase: normPhrase(phrase),
      variants: [phrase],
      category: 'INFORMATIONAL_REGULATORY',
      authority_source: 'v7-scope-recovery-apply HARD_EXCLUDES',
      first_decision_version: 'v7',
      last_confirmed_version: 'v7.1',
      reason: 'Informational/regulatory phrase — hard exclude in production.',
      override_policy: 'operator_approved_override_only',
    });
  }

  const v5AuditPath = path.join(root, 'production/audit/v5-career-education-query-audit.json');
  if (fs.existsSync(v5AuditPath)) {
    const audit = JSON.parse(fs.readFileSync(v5AuditPath, 'utf8'));
    for (const row of audit.rows || []) {
      const np = normPhrase(row.phrase);
      if (exclusions.some((e) => e.normalized_phrase === np)) continue;
      exclusions.push({
        exclusion_id: `EXC-V5-AUDIT-${row.keyword_id}`,
        normalized_phrase: np,
        variants: [row.phrase],
        category: 'EDUCATIONAL_CAREER',
        authority_source: 'v5-career-education-query-audit.json',
        first_decision_version: 'v5',
        last_confirmed_version: 'v7.1',
        reason: row.reason,
        override_policy: 'operator_approved_override_only',
      });
    }
  }

  const byPhrase = new Map();
  for (const e of exclusions) {
    byPhrase.set(e.normalized_phrase, e);
  }

  return {
    registry_id: 'operator-semantic-exclusion-registry-v1',
    version: 'v1',
    project_id: 'corvonero-yandex-direct',
    generated_at: new Date().toISOString(),
    policy: {
      automatic_pipeline_restore: 'FORBIDDEN',
      inline_minus_bypass: 'FORBIDDEN',
      normalization_bypass: 'FORBIDDEN',
      restoration_requires: 'explicit_operator_approved_override',
    },
    exclusions: [...byPhrase.values()],
    exclusion_count: byPhrase.size,
  };
}

export function isExcludedPositivePhrase(phrase, registry) {
  const { positive } = splitPositive(phrase);
  const np = normPhrase(positive);
  return (registry.exclusions || []).some((e) => e.normalized_phrase === np);
}

function splitPositive(phrase) {
  const raw = String(phrase || '');
  const positive = raw.replace(/\s+-[\wа-яё]+/gi, '').replace(/\s+/g, ' ').trim();
  return { positive };
}
