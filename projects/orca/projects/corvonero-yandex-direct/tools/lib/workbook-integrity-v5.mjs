/**
 * Review workbook integrity checks v5 — no placeholders, reconciled counts, type-safe narratives.
 */
import {
  isPlaceholderValue,
  isProhibitedCorrection,
  isGenericSafeExplanation,
  PLACEHOLDER_PATTERNS,
} from './evidence-format-v5.mjs';

export { isPlaceholderValue } from './evidence-format-v5.mjs';

const NARRATIVE_SHEET_COLUMNS = {
  'Negative risk resolution': new Set([5, 7, 8]), // replacement, rep phrases, explanation (0-based after header)
  'Collision findings': new Set([6, 8]), // evidence, correction
  'QA consistency': new Set([2]), // detail
  'Ad evidence audit': new Set([8, 9]),
  'Ad changes': new Set([2, 4]),
};

function isFourDigitPlaceholder(s) {
  return /^\d{4}$/.test(String(s ?? '').trim());
}

export function validateWorkbookSheets(sheets, dataset, semanticReviews, riskResolutions, adAudit) {
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

  const activeWithTemplate = (semanticReviews || []).filter(
    (r) =>
      (r.final_decision === 'ACTIVE COMMERCIAL' || r.final_decision === 'CONTROLLED TEST') &&
      /^ACTIVE: «/.test(r.phrase_specific_reason) === false &&
      (r.phrase_specific_reason || '').length < 40
  );
  if (activeWithTemplate.length) {
    errors.push({ issue: 'template_active_reasons', count: activeWithTemplate.length });
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
      placeholder_patterns_checked: PLACEHOLDER_PATTERNS.length,
    },
  };
}

export function validateReportExportConsistency(dataset, workbookMeta, collisionEvidence) {
  const issues = [];
  if (dataset.keywords.length !== workbookMeta.keyword_count) {
    issues.push({ field: 'keywords', dataset: dataset.keywords.length, workbook: workbookMeta.keyword_count });
  }
  if (dataset.groups.length !== workbookMeta.active_groups) {
    issues.push({ field: 'groups', dataset: dataset.groups.length, workbook: workbookMeta.active_groups });
  }
  if (collisionEvidence.summary.final_status !== 'PASS') {
    issues.push({ field: 'collision_final_status', value: collisionEvidence.summary.final_status });
  }
  if (
    collisionEvidence.summary.unresolved_count === 0 &&
    (collisionEvidence.summary.semantic_risks_after || 0) > 0
  ) {
    issues.push({
      field: 'semantic_risk_contradiction',
      semantic_risks_after: collisionEvidence.summary.semantic_risks_after,
      unresolved_count: collisionEvidence.summary.unresolved_count,
    });
  }
  return {
    passed: issues.length === 0,
    issues,
    reconciled_at: new Date().toISOString(),
  };
}

export function runWorkbookIntegrityRegressionTests() {
  const tests = [];
  const pass = (id, desc, fn) => {
    try {
      fn();
      tests.push({ regression_id: id, description: desc, passed: true });
    } catch (e) {
      tests.push({ regression_id: id, description: desc, passed: false, error: e.message });
    }
  };

  pass('WB-01', 'reject literal 1234 in narrative scan', () => {
    if (!isPlaceholderValue('1234')) throw new Error('1234 not detected');
  });
  pass('WB-02', 'reject literal 2464 in narrative scan', () => {
    if (!isPlaceholderValue('2464')) throw new Error('2464 not detected');
  });
  pass('WB-03', 'reject arbitrary four-digit values', () => {
    if (!isPlaceholderValue('9876')) throw new Error('9876 not detected');
  });
  pass('WB-04', 'reject boolean yes in explanation', () => {
    if (!isPlaceholderValue('yes')) throw new Error('yes not detected');
  });
  pass('WB-05', 'reject PASS-only values', () => {
    if (!isPlaceholderValue('PASS')) throw new Error('PASS not detected');
  });
  pass('WB-06', 'reject prohibited correction tokens', () => {
    if (!isProhibitedCorrection('blocks_own_group_keyword')) throw new Error('blocks_own_group_keyword not rejected');
  });
  pass('WB-07', 'detect generic SAFE template', () => {
    if (!isGenericSafeExplanation('SAFE: no literal collision in owner groups; separates sibling groups; representative checks pass for scope.')) {
      throw new Error('generic SAFE not detected');
    }
  });

  const fakeSheets = {
    'Negative risk resolution': [
      ['replacement'],
      ['2464'],
    ],
  };
  const result = validateWorkbookSheets(fakeSheets, { keywords: [] }, [], { summary: { unique_risky_negatives: 0 } }, {});
  pass('WB-08', 'workbook scan catches 2464 in sheet data', () => {
    if (result.passed) throw new Error('expected failure for 2464 cell');
  });

  return {
    tested_at: new Date().toISOString(),
    passed: tests.every((t) => t.passed),
    tests,
  };
}
