// Diagnostic-only legacy regex patterns — isolated from authoritative admission.
// Source reference: corvonero-direct-v2-clean-room/tools/run-clean-room-semantic-pipeline-v1.mjs

const CAREER = [/ваканс/, /резюме/, /стажиров/];
const DIY = [/своими\s+руками/, /самостоятельно\s+(настро|установ|внедр)/];
const COMMERCIAL_HIRE = [/заказать/, /услуг[аи]/, /под\s+ключ/, /программист/];
const PRODUCT_CFG = [/1с\s*:\s*/, /управлени[ея]\s+торговл/];
const SUPPORT_AMBIG = [/не\s+работ/, /ошибк/, /завис/];

function normalizePhrase(raw) {
  let t = String(raw ?? '').trim().toLowerCase().replace(/ё/g, 'е');
  t = t.replace(/["«»""'']/g, '');
  t = t.replace(/[.,;:!?…]+/g, ' ').replace(/\s+/g, ' ').trim();
  return t;
}

export function legacyClassifyIntent(rawQuery) {
  const norm = { normalized: normalizePhrase(rawQuery), malformed: false };
  const p = norm.normalized;
  if (!p || p.length < 2) {
    return { legacy_intent: 'MALFORMED', legacy_eligibility: 'INELIGIBLE', legacy_reason: 'malformed_or_empty', review: false };
  }
  if (CAREER.some((r) => r.test(p))) {
    return { legacy_intent: 'CAREER/EMPLOYMENT', legacy_eligibility: 'INELIGIBLE', legacy_reason: 'career_pattern', review: false };
  }
  if (DIY.some((r) => r.test(p))) {
    return { legacy_intent: 'DIY/HOW-TO', legacy_eligibility: 'ELIGIBLE COMMERCIAL', legacy_reason: 'diy_pattern', review: true };
  }
  if (PRODUCT_CFG.some((r) => r.test(p)) && !/(программист|услуг|настрой|внедр)/.test(p)) {
    return { legacy_intent: 'COMMERCIAL PRODUCT/MODULE', legacy_eligibility: 'ELIGIBLE COMMERCIAL', legacy_reason: 'product_module_pattern', review: true };
  }
  if (SUPPORT_AMBIG.some((r) => r.test(p))) {
    return { legacy_intent: 'SUPPORT SEEKING — AMBIGUOUS', legacy_eligibility: 'ELIGIBLE COMMERCIAL', legacy_reason: 'support_ambiguous_pattern', review: true };
  }
  if (/(1с|1c)/i.test(p)) {
    const hire = COMMERCIAL_HIRE.some((r) => r.test(p));
    return {
      legacy_intent: hire ? 'COMMERCIAL SERVICE' : 'COMMERCIAL SERVICE',
      legacy_eligibility: 'ELIGIBLE COMMERCIAL',
      legacy_reason: hire ? 'explicit_hire' : '1c_commercial_context',
      review: !hire,
    };
  }
  return { legacy_intent: 'UNKNOWN', legacy_eligibility: 'INELIGIBLE', legacy_reason: 'no_rule_match', review: true };
}

export function buildLegacyComparison(rawQuery, newDecision, invariantFindings = [], reviewRoute = null) {
  const legacy = legacyClassifyIntent(rawQuery);
  let disagreementType = 'NONE';
  if (legacy.legacy_eligibility === 'ELIGIBLE COMMERCIAL' && newDecision === 'REJECT') disagreementType = 'LEGACY_ACCEPT_NEW_REJECT';
  if (legacy.legacy_eligibility === 'INELIGIBLE' && newDecision === 'ACCEPT') disagreementType = 'LEGACY_REJECT_NEW_ACCEPT';
  if (legacy.review && newDecision === 'ABSTAIN') disagreementType = 'LEGACY_ELIGIBLE_NEW_ABSTAIN';

  return {
    diagnostic_comparison: {
      legacy_intent: legacy.legacy_intent,
      legacy_eligibility: legacy.legacy_eligibility,
      legacy_reason: legacy.legacy_reason,
      new_candidate_decision: newDecision,
      disagreement_type: disagreementType,
      violated_invariants: invariantFindings.map((f) => f.invariant_id),
      review_route: reviewRoute,
      authority: 'DIAGNOSTIC ONLY — NOT SEMANTIC AUTHORITY',
    },
  };
}
