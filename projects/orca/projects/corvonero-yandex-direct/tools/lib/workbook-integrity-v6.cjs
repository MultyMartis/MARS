/**
 * Review workbook integrity v6 — narrative-only placeholder scan.
 */
const {
  isPlaceholderValue,
  isProhibitedCorrection,
  PLACEHOLDER_PATTERNS,
} = require('./evidence-format-v5.cjs');

const NARRATIVE_ONLY_SHEETS = new Set([
  'Negative resolution',
  'Collision findings',
  'QA consistency',
  'Ad changes',
  'Semantic decisions',
  'Controlled tests',
  'Exclusions',
]);

const METRIC_VALUE_SHEETS = new Set([
  'Campaign',
  'Directions',
  'Groups',
  'Group viability',
  'Keywords',
  'Bids',
  'URLs',
  'Held groups',
  'Collision summary',
  'Commander row reconciliation',
  'Exact collision actions',
]);

function isFourDigitPlaceholder(s) {
  return /^\d{4}$/.test(String(s ?? '').trim());
}

const NARRATIVE_COLUMNS = {
  'Collision findings': new Set([6]), // correction only; col 7 result_after may be PASS
  'QA consistency': new Set([2]), // detail only; col 1 result may be PASS/FAIL
  'Semantic decisions': new Set([4]),
  'Controlled tests': new Set([3, 4, 6, 7]),
  'Exclusions': new Set([4]),
  'Ad changes': new Set([2, 4]),
  'Negative resolution': new Set([5]),
};

function scanNarrativeCell(sheet, row, col, value) {
  const cols = NARRATIVE_COLUMNS[sheet];
  if (!cols || !cols.has(col)) return null;
  const s = String(value ?? '');
  if (!s) return { issue: 'placeholder_or_empty_narrative', value: '(empty)' };
  if (s === 'PASS' || s === 'FAIL') return null;
  if (isPlaceholderValue(s) && s !== '0') {
    return { issue: 'placeholder_or_empty_narrative', value: s };
  }
  if (isFourDigitPlaceholder(s)) {
    return { issue: 'four_digit_placeholder', value: s };
  }
  if (typeof value === 'boolean') {
    return { issue: 'boolean_in_field', value: s };
  }
  return null;
}

function validateWorkbookSheetsV6(sheets, dataset, negFinalRows) {
  const errors = [];
  const allCells = [];

  for (const [name, data] of Object.entries(sheets)) {
    for (let ri = 1; ri < data.length; ri++) {
      for (let ci = 0; ci < data[ri].length; ci++) {
        const cell = data[ri][ci];
        const s = String(cell ?? '');
        allCells.push(s);
        if (!NARRATIVE_ONLY_SHEETS.has(name)) continue;
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

  const controlledRows = (sheets['Controlled tests'] || []).length - 1;
  const withHypothesis = (sheets['Controlled tests'] || []).slice(1).filter((r) => r[3] && String(r[3]).length > 10);
  if (controlledRows > 0 && withHypothesis.length < controlledRows) {
    errors.push({ issue: 'controlled_test_missing_hypothesis', missing: controlledRows - withHypothesis.length });
  }

  return {
    passed: errors.length === 0,
    errors,
    checks: {
      no_1234: !allCells.includes('1234'),
      no_2464: !allCells.includes('2464'),
      no_970_narrative: !allCells.includes('970'),
      keyword_coverage: keywordRows === dataset.keywords.length,
      negative_resolution_rows: negRows === expectedNeg,
      placeholder_patterns_checked: PLACEHOLDER_PATTERNS.length,
    },
  };
}

module.exports = { validateWorkbookSheetsV6 };
