/**
 * Provider-neutral semantic assessor contract.
 * Implementations: deterministic-assessor (fixtures), future model provider.
 */
export const ASSESSOR_MODES = {
  DETERMINISTIC: 'deterministic-v1',
  MODEL: 'model-provider-v1',
};

export function validateAssessorOutput(output) {
  const errors = [];
  if (!output || typeof output !== 'object') errors.push('assessor output missing');
  if (!output.primary_intent) errors.push('primary_intent required');
  if (!output.commercial_eligibility?.decision) errors.push('commercial_eligibility.decision required');
  if (!['ACCEPT', 'REJECT', 'ABSTAIN'].includes(output.commercial_eligibility.decision)) {
    errors.push('invalid tri-state decision');
  }
  return errors;
}

export function createAssessorContext(phrase, context) {
  return {
    phrase,
    raw_query: phrase.raw_query,
    normalized_query: phrase.normalized_query || phrase.raw_query,
    business_scope: context.businessScope,
    services: context.serviceRegistry?.services || [],
    geography: context.geography || phrase.region,
    taxonomy: context.taxonomy || {},
    commercial_policy: context.commercialPolicy || {},
    protected_intent_rules: context.protectedIntentRules || {},
    source_metadata: phrase.source_metadata || {},
  };
}
