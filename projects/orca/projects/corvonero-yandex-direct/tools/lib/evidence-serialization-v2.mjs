/**
 * ORCA evidence serialization v2 — typed formatters for workbook/MD/JSON output.
 * Prevents object coercion, shared-string index leaks, and numeric narrative values.
 */
import {
  formatNarrative,
  isPlaceholderValue,
  EMPTY_REPLACEMENT_SENTINEL,
  EMPTY_REP_PHRASES_SENTINEL,
  EMPTY_DETAIL_SENTINEL,
} from './evidence-format-v5.mjs';

export const PASS_ERROR_SENTINEL = 'Not applicable — test passed';
export const NOT_APPLICABLE_SENTINEL = 'Not applicable';

/** @param {unknown} value */
export function formatStatusValue(value) {
  if (value == null || value === '') return 'UNKNOWN';
  if (typeof value === 'boolean') return value ? 'YES' : 'NO';
  if (typeof value === 'number') return String(value);
  if (typeof value === 'object') {
    if (Array.isArray(value)) return formatListValue(value);
    return Object.entries(value)
      .map(([k, v]) => `${k}=${formatMetricScalar(v)}`)
      .join('; ');
  }
  return String(value).trim();
}

/** @param {unknown} value */
function formatMetricScalar(value) {
  if (value == null) return 'null';
  if (typeof value === 'object' && !Array.isArray(value)) {
    return `{${Object.entries(value).map(([k, v]) => `${k}:${v}`).join(',')}}`;
  }
  return String(value);
}

/** @param {unknown} value */
export function formatCount(value, { label = '' } = {}) {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    throw new Error(`formatCount requires finite number, got ${typeof value}`);
  }
  return label ? `${label}: ${value}` : String(value);
}

/** @param {unknown} value */
export function formatListValue(value, { separator = '; ', numbered = false } = {}) {
  if (value == null) return NOT_APPLICABLE_SENTINEL;
  if (!Array.isArray(value)) {
    if (typeof value === 'string') return value.trim() || NOT_APPLICABLE_SENTINEL;
    throw new Error('formatListValue requires array or string');
  }
  if (!value.length) return NOT_APPLICABLE_SENTINEL;
  if (numbered) return value.map((x, i) => `${i + 1}. ${String(x)}`).join('\n');
  return value.map(String).join(separator);
}

/** @param {unknown} value */
export function formatOptionalEvidence(value, { field = 'detail' } = {}) {
  if (value == null || value === '') return EMPTY_DETAIL_SENTINEL;
  return formatNarrative(value, { field });
}

/** @param {unknown} value */
export function formatNotApplicable(reason = '') {
  return reason ? `Not applicable — ${reason}` : NOT_APPLICABLE_SENTINEL;
}

/** @param {unknown} value */
export function formatExactAction(value) {
  return formatNarrative(value, { field: 'correction', fallback: 'Action required' });
}

/**
 * Regression / test error column — never empty string (avoids shared-string index leak e.g. 970).
 * @param {boolean} passed
 * @param {unknown} error
 */
export function formatErrorDetails(passed, error) {
  if (passed) return PASS_ERROR_SENTINEL;
  const msg = error == null ? '' : String(error).trim();
  if (!msg) return 'Test failed — no error message recorded';
  if (isPlaceholderValue(msg)) return `Test failed — invalid placeholder in error: ${msg}`;
  return formatNarrative(msg, { field: 'detail' });
}

/**
 * Workbook metric row — objects/arrays/booleans safe for metric columns.
 * @param {string} key
 * @param {unknown} value
 */
export function formatMetricValue(key, value) {
  if (value == null) return '';
  if (typeof value === 'boolean') return value ? 'true' : 'false';
  if (typeof value === 'number') return String(value);
  if (typeof value === 'string') return value;
  if (Array.isArray(value)) return formatListValue(value);
  if (typeof value === 'object') return formatStatusValue(value);
  return String(value);
}

/** Serialize reconciliation metrics for workbook rows */
export function reconciliationMetricsToRows(reconciliation) {
  return Object.entries(reconciliation).map(([k, v]) => [k, formatMetricValue(k, v)]);
}

export function buildSerializationRootCauseV2() {
  return {
    audit_id: 'evidence-serialization-root-cause-v2',
    generated_at: new Date().toISOString(),
    defects: [
      {
        id: 'SER-01',
        symptom: 'Object-to-string coercion in workbook metric row',
        root_cause:
          'Object values (e.g. pass_requires: { UNRESOLVED: 0 }) written to workbook via String(v) without typed formatter.',
        source_file: 'tools/run-v5-qa-repair-gate.mjs',
        function: 'writeQaRepairWorkbook → Semantic-risk reconciliation sheet',
        field: 'pass_requires',
        mechanism: 'object_to_string_coercion',
        fix: 'formatMetricValue() / formatStatusValue() — never String(object)',
      },
      {
        id: 'SER-02',
        symptom: 'Shared-string index leak in regression error column (empty cell)',
        root_cause:
          'Empty string "" in regression test error column. ExcelJS deduplicates empty strings; operator tools display sharedStrings index (970 in QA repair workbook).',
        source_file: 'tools/run-v5-qa-repair-gate.mjs',
        function: 'writeQaRepairWorkbook → Generator regression tests',
        field: 'error',
        mechanism: 'shared_string_index_leak',
        related_index: 970,
        fix: 'formatErrorDetails(passed, error) → PASS uses «Not applicable — test passed»',
      },
      {
        id: 'SER-03',
        symptom: 'Shared-string index leak in narrative column (empty cell)',
        root_cause:
          'Empty narrative fields (replacement, representative_phrases, detail) deduplicated to sharedStrings[2464].',
        source_file: 'tools/generate-review-workbook-v5.cjs',
        function: 'Negative risk resolution row mapping',
        field: 'replacement, representative_phrases, detail',
        mechanism: 'shared_string_index_leak',
        related_index: 2464,
        fix: 'formatNarrative() with explicit sentinels; forbid bare empty strings',
      },
      {
        id: 'SER-04',
        symptom: 'Legacy four-digit placeholder literal in narrative scan',
        root_cause: 'Legacy placeholder literal in narrative scan fixtures.',
        mechanism: 'literal_placeholder',
        fix: 'isPlaceholderValue() rejects /^\\d{4}$/',
      },
    ],
    formatters: [
      'formatNarrative',
      'formatListValue',
      'formatStatusValue',
      'formatCount',
      'formatOptionalEvidence',
      'formatNotApplicable',
      'formatExactAction',
      'formatErrorDetails',
      'formatMetricValue',
    ],
    narrative_forbidden_types: ['object', 'array_without_formatting', 'integer', 'boolean', 'empty_string'],
    implementation: 'tools/lib/evidence-serialization-v2.mjs',
  };
}

export {
  formatNarrative,
  EMPTY_REPLACEMENT_SENTINEL,
  EMPTY_REP_PHRASES_SENTINEL,
  EMPTY_DETAIL_SENTINEL,
};
