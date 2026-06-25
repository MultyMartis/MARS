'use strict';

/**
 * Review workbook integrity v7.1 — narrative field validation including Keywords.hypothesis.
 */
const { isPlaceholderValue, PLACEHOLDER_PATTERNS } = require('./evidence-format-v5.cjs');
const {
  NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU,
} = require('./hypothesis-serialization-bridge.cjs');

const NARRATIVE_SHEETS = new Set([
  'Negative resolution',
  'Collision findings',
  'QA consistency',
  'Ad changes',
  'Semantic decisions',
  'Controlled tests',
  'Exclusions',
  'Keywords',
  'Regression repairs',
  'XLSX integrity',
]);

const NARRATIVE_COLUMNS = {
  Keywords: new Set([7]),
  'Collision findings': new Set([6]),
  'QA consistency': new Set([2]),
  'Semantic decisions': new Set([4]),
  'Controlled tests': new Set([3, 4, 6, 7]),
  Exclusions: new Set([4]),
  'Ad changes': new Set([2, 4]),
  'Negative resolution': new Set([5]),
  'Regression repairs': new Set([3, 4]),
  'XLSX integrity': new Set([2, 3]),
};

function isNumericOnlyNarrative(s) {
  const t = String(s ?? '').trim();
  if (!t) return false;
  if (/^\d+$/.test(t) && t.length >= 3) return true;
  return false;
}

function scanNarrativeCell(sheet, row, col, value) {
  const cols = NARRATIVE_COLUMNS[sheet];
  if (!cols || !cols.has(col)) return null;
  const s = String(value ?? '');
  if (!s.trim()) return { issue: 'placeholder_or_empty_narrative', value: '(empty)' };
  if (s === 'PASS' || s === 'FAIL') return null;
  if (typeof value === 'boolean') return { issue: 'boolean_in_field', value: s };
  if (typeof value === 'number') return { issue: 'numeric_in_narrative', value: s };
  if (isPlaceholderValue(s) && s !== '0') return { issue: 'placeholder_or_empty_narrative', value: s };
  if (isNumericOnlyNarrative(s)) return { issue: 'numeric_only_narrative', value: s };
  if (s === '[object Object]') return { issue: 'object_coercion', value: s };
  if (sheet === 'Keywords' && col === 7) {
    if (s === NON_CONTROLLED_HYPOTHESIS_SENTINEL_RU) return null;
    if (s.length < 12) return { issue: 'hypothesis_too_short', value: s };
  }
  return null;
}

function validateWorkbookSheetsV71(sheets, dataset, negFinalRows) {
  const errors = [];
  const allCells = [];

  for (const [name, data] of Object.entries(sheets)) {
    for (let ri = 1; ri < data.length; ri++) {
      for (let ci = 0; ci < data[ri].length; ci++) {
        const cell = data[ri][ci];
        allCells.push(String(cell ?? ''));
        if (!NARRATIVE_SHEETS.has(name)) continue;
        const err = scanNarrativeCell(name, ri, ci, cell);
        if (err) errors.push({ sheet: name, row: ri, col: ci, ...err });
      }
    }
  }

  const keywordRows = (sheets.Keywords || []).length - 1;
  if (keywordRows !== dataset.keywords.length) {
    errors.push({ issue: 'keyword_row_mismatch', expected: dataset.keywords.length, actual: keywordRows });
  }

  const negRows = (sheets['Negative resolution'] || []).length - 1;
  const expectedNeg = (negFinalRows || []).length;
  if (negRows !== expectedNeg) {
    errors.push({ issue: 'negative_resolution_row_mismatch', expected: expectedNeg, actual: negRows });
  }

  const hypothesisEmpty = (sheets.Keywords || [])
    .slice(1)
    .filter((r) => !r[7] || String(r[7]).trim() === '').length;

  if (hypothesisEmpty > 0) {
    errors.push({ issue: 'keywords_missing_hypothesis_sentinel', count: hypothesisEmpty });
  }

  return {
    passed: errors.length === 0,
    errors,
    checks: {
      no_272: !allCells.includes('272'),
      no_1234: !allCells.includes('1234'),
      no_2464: !allCells.includes('2464'),
      no_970_narrative: !allCells.includes('970'),
      keyword_hypothesis_sentinel_required: hypothesisEmpty === 0,
      placeholder_patterns_checked: PLACEHOLDER_PATTERNS.length,
    },
  };
}

module.exports = { validateWorkbookSheetsV71 };
