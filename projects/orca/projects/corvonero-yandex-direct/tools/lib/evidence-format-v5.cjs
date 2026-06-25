'use strict';
/** CommonJS evidence formatting — mirror of evidence-format-v5.mjs for generate-review-workbook-v5.cjs */

const EMPTY_REPLACEMENT_SENTINEL = 'Not required — negative retained';
const EMPTY_REP_PHRASES_SENTINEL = 'None — no stem-near phrases in owner scope';
const EMPTY_DETAIL_SENTINEL = 'No additional detail required';

const GENERIC_SAFE_RE =
  /^SAFE: no literal collision in owner groups; separates (sibling groups|.*); representative checks pass/i;

const PROHIBITED_CORRECTIONS = new Set([
  'blocks_own_group_keyword',
  'collision',
  'fixed',
  'PASS',
  'unresolved',
  'filtered_from_export',
]);

const PLACEHOLDER_PATTERNS = [
  /^1234$/,
  /^2464$/,
  /^\d{4}$/,
  /^yes$/i,
  /^true$/i,
  /^PASS$/i,
  /^REVIEWED$/i,
  /^n\/a$/i,
  /^TBD$/i,
  /^TODO$/i,
];

function isNumericOnly(s) {
  return /^\d+$/.test(String(s ?? '').trim());
}

function isPlaceholderValue(v, opts = {}) {
  const s = String(v ?? '').trim();
  if (!s) return !opts.allowEmpty;
  if (isNumericOnly(s) && s.length >= 3) return true;
  return PLACEHOLDER_PATTERNS.some((re) => re.test(s));
}

function isGenericSafeExplanation(explanation) {
  return GENERIC_SAFE_RE.test(String(explanation ?? '').trim());
}

function isProhibitedCorrection(correction) {
  const s = String(correction ?? '').trim();
  if (!s) return true;
  return PROHIBITED_CORRECTIONS.has(s);
}

function formatNarrative(value, opts = {}) {
  const field = opts.field || '';
  if (value == null || value === '') {
    if (field === 'replacement') return EMPTY_REPLACEMENT_SENTINEL;
    if (field === 'representative_phrases' || field === 'representative_affected_phrases') {
      return EMPTY_REP_PHRASES_SENTINEL;
    }
    if (field === 'detail') return EMPTY_DETAIL_SENTINEL;
    return opts.fallback || EMPTY_DETAIL_SENTINEL;
  }
  if (typeof value === 'number') {
    throw new Error(`Numeric value ${value} forbidden in narrative field «${field}»`);
  }
  if (typeof value === 'object') {
    throw new Error(`Object value forbidden in narrative field «${field}»`);
  }
  if (Array.isArray(value)) {
    if (!value.length) return formatNarrative('', { field });
    return value.map((x, i) => `${i + 1}. ${String(x)}`).join('\n');
  }
  const s = String(value).trim();
  if (isPlaceholderValue(s)) {    throw new Error(`Placeholder «${s}» forbidden in narrative field «${field}»`);
  }
  return s;
}

function formatRiskResolutionRow(r) {
  const reps = r.representative_affected_phrases || [];
  return {
    replacement: r.replacement
      ? formatNarrative(r.replacement, { field: 'replacement' })
      : EMPTY_REPLACEMENT_SENTINEL,
    representative_phrases: reps.length
      ? formatNarrative(reps, { field: 'representative_phrases' })
      : EMPTY_REP_PHRASES_SENTINEL,
    explanation: formatNarrative(r.explanation, { field: 'explanation', fallback: 'Evidence required' }),
  };
}

function formatCollisionCorrection(removal, finding) {
  const neg = removal?.negative || finding?.negative;
  const gid = removal?.group_id || finding?.group_id;
  const kw = (removal?.colliding_keywords || [finding?.keyword]).filter(Boolean)[0];
  const level = removal?.level || finding?.level || 'group_cross';
  return `DELETE NEGATIVE: removed «${neg}» (${level}) from scope ${gid} — literal collision with active keyword «${kw}»`;
}

module.exports = {
  isPlaceholderValue,
  isProhibitedCorrection,
  isGenericSafeExplanation,
  formatNarrative,
  formatRiskResolutionRow,
  formatCollisionCorrection,
  EMPTY_REPLACEMENT_SENTINEL,
  EMPTY_REP_PHRASES_SENTINEL,
  EMPTY_DETAIL_SENTINEL,
  PLACEHOLDER_PATTERNS,
};
