'use strict';
/**
 * Review workbook integrity checks v5 — CommonJS for generate-review-workbook-v5.cjs
 */
const {
  isPlaceholderValue,
  isProhibitedCorrection,
  isGenericSafeExplanation,
  PLACEHOLDER_PATTERNS,
} = require('./evidence-format-v5.cjs');

const NARRATIVE_SHEET_COLUMNS = {
  'Negative risk resolution': new Set([5, 7, 8]),
  'Collision findings': new Set([6, 8]),
  'QA consistency': new Set([2]),
  'Ad evidence audit': new Set([8, 9]),
  'Ad changes': new Set([2, 4]),
};

function isFourDigitPlaceholder(s) {
  return /^\d{4}$/.test(String(s ?? '').trim());
}

function validateWorkbookSheets(sheets, dataset, semanticReviews, riskResolutions, adAudit) {
  const errors = [];
  const allCells = [];

  for (const [name, data] of Object.entries(sheets)) {
    const narrativeCols = NARRATIVE_SHEET_COLUMNS[name];
    for (let ri = 1; ri < data.length; ri++) {
      data[ri].forEach((cell, ci) => {
        const s = String(cell ?? '');
        allCells.push(s);
        if (isPlaceholderValue(s)) {
          errors.push({ sheet: name, row: ri, col: ci, issue: 'placeholder_or_empty_narrative', value: s || '(empty)' });
        }
        if (isFourDigitPlaceholder(s)) {
          errors.push({ sheet: name, row: ri, col: ci, issue: 'four_digit_placeholder', value: s });
        }
        if (narrativeCols?.has(ci) && typeof cell === 'number') {
          errors.push({ sheet: name, row: ri, col: ci, issue: 'numeric_in_narrative_field', value: cell });
        }
        if (narrativeCols?.has(ci) && isGenericSafeExplanation(s)) {
          errors.push({ sheet: name, row: ri, col: ci, issue: 'generic_safe_explanation', value: s.slice(0, 60) });
        }
      });
    }
  }

  const semanticRows = (sheets['Semantic evidence review'] || []).length - 1;
  if (semanticRows !== dataset.keywords.length) {
    errors.push({ issue: 'semantic_row_mismatch', expected: dataset.keywords.length, actual: semanticRows });
  }

  const riskRows = (sheets['Negative risk resolution'] || []).length - 1;
  const uniqueRisks = riskResolutions?.summary?.unique_risky_negatives ?? 0;
  if (riskRows !== uniqueRisks) {
    errors.push({ issue: 'risk_row_mismatch', expected: uniqueRisks, actual: riskRows });
  }

  for (const row of (sheets['Collision findings'] || []).slice(1)) {
    const correction = row[8];
    const resultBefore = row[7];
    if (resultBefore === 'BLOCKING' && (isPlaceholderValue(correction) || isProhibitedCorrection(correction))) {
      errors.push({ issue: 'invalid_correction_for_blocking', keyword: row[2], correction });
    }
  }

  for (const ch of adAudit?.changes || []) {
    if (isPlaceholderValue(ch.original_problem) || isPlaceholderValue(ch.correction_applied)) {
      errors.push({ issue: 'ad_change_missing_evidence', ad_id: ch.ad_id });
    }
  }

  const collisionSummary = Object.fromEntries((sheets['Collision summary'] || []).slice(1).map((r) => [r[0], r[1]]));
  if (collisionSummary.unresolved_count === 0 && Number(collisionSummary.semantic_risks_after) > 0) {
    errors.push({
      issue: 'collision_summary_contradiction',
      semantic_risks_after: collisionSummary.semantic_risks_after,
      unresolved_count: collisionSummary.unresolved_count,
    });
  }

  return {
    passed: errors.length === 0,
    errors,
    checks: {
      no_1234: !allCells.includes('1234'),
      no_2464: !allCells.includes('2464'),
      no_four_digit_narrative: !allCells.some(isFourDigitPlaceholder),
      semantic_coverage: semanticRows === dataset.keywords.length,
      risk_resolution_rows: riskRows === uniqueRisks,
    },
  };
}

module.exports = { validateWorkbookSheets, isPlaceholderValue };
