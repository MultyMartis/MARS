/**
 * Provider-neutral semantic model adapter interface.
 */
import crypto from 'node:crypto';

export const BLOCKER_MODEL_UNAVAILABLE = 'BLOCKED — PRODUCTION SEMANTIC MODEL UNAVAILABLE';

export function validateStructuredOutput(output) {
  const errors = [];
  if (!output || typeof output !== 'object') return ['output missing or not object'];
  const required = [
    'primary_intent', 'decision', 'confidence', 'rationale', 'blind_assessment',
    'commercial_eligibility',
  ];
  for (const field of required) {
    if (output[field] === undefined || output[field] === null) errors.push(`${field} required`);
  }
  if (output.decision && !['ACCEPT', 'REJECT', 'ABSTAIN'].includes(output.decision)) {
    errors.push('invalid decision tri-state');
  }
  if (output.commercial_eligibility?.decision && !['ACCEPT', 'REJECT', 'ABSTAIN'].includes(output.commercial_eligibility.decision)) {
    errors.push('invalid commercial_eligibility.decision');
  }
  if (output.blind_assessment !== true) errors.push('blind_assessment must be true for primary assessment');
  if (output.confidence !== undefined && (output.confidence < 0 || output.confidence > 1)) {
    errors.push('confidence out of range');
  }
  return errors;
}

export function contextChecksum(context) {
  const safe = {
    business_scope_version: context.businessScope?.version,
    service_registry_version: context.serviceRegistry?.version,
    service_ids: (context.serviceRegistry?.services || []).map((s) => s.service_id).sort(),
    taxonomy_keys: Object.keys(context.taxonomy || {}).sort(),
    policy_version: context.commercialPolicy?.version,
  };
  return crypto.createHash('sha256').update(JSON.stringify(safe)).digest('hex').slice(0, 16);
}

export async function assessSemanticIntent(params) {
  const {
    phrase,
    businessScope,
    serviceRegistry,
    taxonomy = {},
    commercialPolicy = {},
    protectedIntentPolicy = {},
    sourceMetadata = {},
    assessmentMode = 'BLIND_PRIMARY',
    adapter = null,
  } = params;

  const context = {
    phrase: sanitizePhraseForModel(phrase),
    businessScope: sanitizeBusinessScope(businessScope),
    serviceRegistry: sanitizeServiceRegistry(serviceRegistry),
    taxonomy,
    commercialPolicy,
    protectedIntentPolicy,
    sourceMetadata: sanitizeSourceMetadata(sourceMetadata),
    assessmentMode,
  };

  if (!adapter) {
    return { ok: false, blocker: BLOCKER_MODEL_UNAVAILABLE, errors: ['no adapter configured'] };
  }

  const result = await adapter.assess(context);
  if (!result.ok) return result;

  const validationErrors = validateStructuredOutput(result.output);
  if (validationErrors.length) {
    return { ok: false, blocker: 'MALFORMED_MODEL_OUTPUT', errors: validationErrors, raw: result.raw };
  }

  return {
    ok: true,
    output: result.output,
    metadata: result.metadata,
    context_checksum: contextChecksum(context),
  };
}

export function sanitizePhraseForModel(phrase) {
  return {
    phrase_id: phrase.phrase_id,
    raw_query: redactPii(phrase.raw_query),
    normalized_query: redactPii(phrase.normalized_query || phrase.raw_query),
    region: phrase.region,
  };
}

export function sanitizeBusinessScope(scope) {
  if (!scope) return {};
  return {
    version: scope.version,
    scope: scope.scope,
    description: scope.description,
    geography: scope.geography,
    excluded_intents: scope.excluded_intents,
  };
}

export function sanitizeServiceRegistry(registry) {
  if (!registry) return { services: [] };
  return {
    version: registry.version,
    registry_id: registry.registry_id,
    services: (registry.services || []).map((s) => ({
      service_id: s.service_id,
      name: s.name,
      description: s.description,
      included_tasks: s.included_tasks,
      excluded_tasks: s.excluded_tasks,
      operator_status: s.operator_status,
    })),
  };
}

export function sanitizeSourceMetadata(meta) {
  if (!meta) return {};
  const forbidden = ['expected_label', 'deterministic_decision', 'p0i_decision', 'legacy_orca_decision', 'adjudicator_result'];
  const safe = { ...meta };
  for (const k of forbidden) delete safe[k];
  return safe;
}

const PII_PATTERNS = [
  /\b[\w.-]+@[\w.-]+\.\w+\b/g,
  /\b\+?\d{10,15}\b/g,
];

export function redactPii(text) {
  if (!text || typeof text !== 'string') return text;
  let out = text;
  for (const pat of PII_PATTERNS) out = out.replace(pat, '[REDACTED]');
  return out;
}

export function assertBlindInputSeparation(inputContext) {
  const forbidden = [
    'deterministic_decision', 'deterministic_outcome', 'expected_label',
    'p0i_decision', 'legacy_orca_decision', 'adjudicator_result',
    'reassessment_outcome', 'primary_rationale', 'primary_decision',
  ];
  const leaks = forbidden.filter((k) => inputContext[k] !== undefined);
  return { blind: leaks.length === 0, leaks };
}
