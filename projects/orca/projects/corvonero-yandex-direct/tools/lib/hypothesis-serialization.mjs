/**
 * Narrative hypothesis serialization for Review workbook Keywords sheet.
 * Replaces blank/null coercion that can surface as numeric placeholders in XLSX consumers.
 */
export const NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU =
  'Не применимо — ключевое слово не является контролируемым тестом';

export const NON_CONTROLLED_HYPOTHESIS_SENTINEL_EN =
  'Not applicable — keyword is not a controlled test';

export function resolveKeywordHypothesis(keyword, controlledById = new Map()) {
  const fromKw = keyword.controlled_test_hypothesis;
  if (fromKw && String(fromKw).trim().length > 10) {
    return String(fromKw).trim();
  }
  const ct = controlledById.get(keyword.keyword_id);
  if (ct?.commercial_hypothesis && String(ct.commercial_hypothesis).trim().length > 10) {
    return String(ct.commercial_hypothesis).trim();
  }
  const decision = String(keyword.semantic_decision || keyword.final_status || '').toUpperCase();
  if (decision.includes('CONTROLLED TEST')) {
    throw new Error(
      `Controlled test keyword ${keyword.keyword_id} missing phrase-specific hypothesis`
    );
  }
  return NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU;
}

export function isValidNarrativeField(value, { field = '', allowPassFail = false } = {}) {
  if (value == null) return { ok: false, reason: 'null_or_undefined' };
  if (typeof value === 'boolean') return { ok: false, reason: 'boolean' };
  if (typeof value === 'number') return { ok: false, reason: 'raw_number' };
  if (typeof value === 'object') return { ok: false, reason: 'raw_object' };
  const s = String(value).trim();
  if (!s) return { ok: false, reason: 'empty_string' };
  if (s === '[object Object]') return { ok: false, reason: 'object_coercion' };
  if (/^\[\s*.+\s*\]$/.test(s) && s.includes(',')) return { ok: false, reason: 'raw_array' };
  if (allowPassFail && (s === 'PASS' || s === 'FAIL')) return { ok: true };
  if (/^\d+$/.test(s) && s.length >= 3) return { ok: false, reason: 'numeric_only_string' };
  if (/^(true|false)$/i.test(s)) return { ok: false, reason: 'boolean_string' };
  if (/^n\/a$/i.test(s)) return { ok: false, reason: 'unexplained_na' };
  return { ok: true };
}

export function stripInlineNegatives(phrase) {
  return String(phrase || '')
    .replace(/\s+-[\wа-яё]+/gi, '')
    .replace(/\s+/g, ' ')
    .trim();
}

export function splitInlineNegatives(phrase) {
  const raw = String(phrase || '');
  const negatives = [];
  const positive = raw
    .replace(/\s+(-[\wа-яё]+)/gi, (_, neg) => {
      negatives.push(neg.replace(/^-/, ''));
      return '';
    })
    .replace(/\s+/g, ' ')
    .trim();
  return { positive, negatives };
}
