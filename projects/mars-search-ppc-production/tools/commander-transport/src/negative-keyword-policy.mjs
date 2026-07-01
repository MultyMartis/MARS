/**
 * Negative-keyword policy — embedded XLSX vs separate TXT import.
 */

export const NEGATIVE_MODES = Object.freeze({
  EMBEDDED_BLANK: 'blank',
  EMBEDDED_SET: 'set',
  TXT_SEPARATE: 'txt_separate',
});

export const METADATA_OPS = Object.freeze({
  MISSING: 'MISSING',
  PRESERVE: 'PRESERVE',
  EXPLICIT_CLEAR: 'EXPLICIT_CLEAR',
  SET_VALUE: 'SET_VALUE',
});

/**
 * Resolve E9 campaign negatives operation.
 * @param {object} input — { operation, value, policy }
 */
export function resolveCampaignNegativeOperation(input) {
  const op = String(input.operation ?? '').toLowerCase();
  const policy = input.policy ?? NEGATIVE_MODES.EMBEDDED_BLANK;

  if (policy === NEGATIVE_MODES.EMBEDDED_BLANK || op === 'clear' || input.value === '') {
    return { op: METADATA_OPS.EXPLICIT_CLEAR, xlsx_value: null };
  }
  if (op === 'preserve') {
    return { op: METADATA_OPS.PRESERVE, xlsx_value: input.template_value ?? null };
  }
  if (op === 'set' && input.value) {
    return { op: METADATA_OPS.SET_VALUE, xlsx_value: input.value };
  }
  return { op: METADATA_OPS.MISSING, xlsx_value: undefined };
}

/**
 * Reject quoted values that simulate phrase-match in negatives.
 * @param {string} negative
 */
export function validateNegativeSyntax(negative) {
  const violations = [];
  const n = String(negative ?? '').trim();
  if (/^".*"$/.test(n)) {
    violations.push({
      code: 'QUOTED_PSEUDO_PHRASE_MATCH',
      severity: 'HARD_FAIL',
      message: `Quoted negative rejected: ${n}`,
    });
  }
  return violations;
}

/**
 * @param {string[]} negatives
 * @param {string[]} includedKeywords
 */
export function detectIncludedKeywordConflict(negatives, includedKeywords) {
  const violations = [];
  const inc = new Set(includedKeywords.map((k) => k.toLowerCase().trim()));
  for (const neg of negatives) {
    const core = neg.replace(/^[-+!]/, '').toLowerCase().trim();
    if (inc.has(core)) {
      violations.push({
        code: 'NEGATIVE_INCLUDED_KEYWORD_CONFLICT',
        severity: 'HARD_FAIL',
        message: `Negative "${neg}" conflicts with included keyword "${core}"`,
      });
    }
  }
  return violations;
}
