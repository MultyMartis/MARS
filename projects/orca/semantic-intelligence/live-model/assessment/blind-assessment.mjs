/**
 * Blind primary assessment — no leakage of deterministic/legacy/expected labels.
 */
import { assessSemanticIntent, assertBlindInputSeparation, sanitizeSourceMetadata } from '../adapters/model-adapter-interface.mjs';

export async function runBlindPrimaryAssessment(params) {
  const {
    phrase,
    businessScope,
    serviceRegistry,
    taxonomy,
    commercialPolicy,
    protectedIntentPolicy,
    adapter,
    forbiddenContext = {},
  } = params;

  const separation = assertBlindInputSeparation(forbiddenContext);
  if (!separation.blind) {
    return {
      ok: false,
      blocker: 'BLIND_ASSESSMENT_LEAKAGE',
      leaks: separation.leaks,
    };
  }

  const result = await assessSemanticIntent({
    phrase,
    businessScope,
    serviceRegistry,
    taxonomy,
    commercialPolicy,
    protectedIntentPolicy,
    sourceMetadata: sanitizeSourceMetadata(phrase.source_metadata || {}),
    assessmentMode: 'BLIND_PRIMARY',
    adapter,
  });

  if (!result.ok) return result;

  result.output.blind_assessment = true;
  result.independence_level = null;
  result.assessment_role = 'PRIMARY_A';

  return result;
}

export function buildBlindInputEvidence(params) {
  const separation = assertBlindInputSeparation(params.forbiddenContext || {});
  return {
    blind_assessment: true,
    input_separation_proven: separation.blind,
    excluded_fields: [
      'deterministic_decision', 'expected_label', 'p0i_decision',
      'legacy_orca_decision', 'adjudicator_result',
    ],
    leaks_detected: separation.leaks,
    timestamp: new Date().toISOString(),
  };
}
