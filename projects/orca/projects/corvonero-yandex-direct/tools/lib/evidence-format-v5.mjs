/**
 * ORCA evidence field formatting — type-safe narrative strings for workbooks.
 * Prevents empty cells that ExcelJS deduplicates to shared-string indices (operator-visible as "2464").
 */

export const EMPTY_REPLACEMENT_SENTINEL = 'Not required — negative retained';
export const EMPTY_REP_PHRASES_SENTINEL = 'None — no stem-near phrases in owner scope';
export const EMPTY_DETAIL_SENTINEL = 'No additional detail required';

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
  /^\[object Object\]$/i,
];

const NARRATIVE_FIELD_NAMES = new Set([
  'replacement',
  'representative_phrases',
  'representative_affected_phrases',
  'explanation',
  'correction',
  'evidence',
  'detail',
  'phrase_specific_reason',
  'phrase_reason',
  'original_problem',
  'correction_applied',
  'semantic_reason',
  'note',
]);

export function isNumericOnly(s) {
  return /^\d+$/.test(String(s ?? '').trim());
}

export function isPlaceholderValue(v, { allowEmpty = false } = {}) {
  const s = String(v ?? '').trim();
  if (!s) return !allowEmpty;
  if (isNumericOnly(s) && s.length >= 3) return true;
  return PLACEHOLDER_PATTERNS.some((re) => re.test(s));
}

export function isGenericSafeExplanation(explanation) {
  return GENERIC_SAFE_RE.test(String(explanation ?? '').trim());
}

export function isProhibitedCorrection(correction) {
  const s = String(correction ?? '').trim();
  if (!s) return true;
  return PROHIBITED_CORRECTIONS.has(s);
}

export function formatNarrative(value, { field = '', fallback = '' } = {}) {
  if (value == null || value === '') {
    if (field === 'replacement') return EMPTY_REPLACEMENT_SENTINEL;
    if (field === 'representative_phrases' || field === 'representative_affected_phrases') {
      return EMPTY_REP_PHRASES_SENTINEL;
    }
    if (field === 'detail') return EMPTY_DETAIL_SENTINEL;
    return fallback || EMPTY_DETAIL_SENTINEL;
  }
  if (typeof value === 'number') {
    throw new Error(`Numeric value ${value} forbidden in narrative field «${field}»`);
  }
  if (Array.isArray(value)) {
    if (!value.length) {
      return formatNarrative('', { field });
    }
    return value.map((x, i) => `${i + 1}. ${String(x)}`).join('\n');
  }
  if (typeof value === 'object') {
    throw new Error(`Object value forbidden in narrative field «${field}»`);
  }
  const s = String(value).trim();
  if (isPlaceholderValue(s)) {
    throw new Error(`Placeholder «${s}» forbidden in narrative field «${field}»`);
  }
  return s;
}

export function formatRiskResolutionRow(r) {
  return {
    ...r,
    replacement: r.replacement ? formatNarrative(r.replacement, { field: 'replacement' }) : EMPTY_REPLACEMENT_SENTINEL,
    representative_affected_phrases: (r.representative_affected_phrases || []).length
      ? r.representative_affected_phrases
      : [],
    representative_phrases_display: (r.representative_affected_phrases || []).length
      ? formatNarrative(r.representative_affected_phrases, { field: 'representative_phrases' })
      : EMPTY_REP_PHRASES_SENTINEL,
    explanation: formatNarrative(r.explanation, { field: 'explanation', fallback: 'Evidence required' }),
  };
}

export function formatCollisionCorrection(removal, finding) {
  const neg = removal?.negative || finding?.negative;
  const gid = removal?.group_id || finding?.group_id;
  const kw = (removal?.colliding_keywords || [finding?.keyword]).filter(Boolean)[0];
  const level = removal?.level || finding?.level || 'group_cross';
  return `DELETE NEGATIVE: removed «${neg}» (${level}) from scope ${gid} — literal collision with active keyword «${kw}»`;
}

export { NARRATIVE_FIELD_NAMES, PROHIBITED_CORRECTIONS, PLACEHOLDER_PATTERNS, GENERIC_SAFE_RE };
