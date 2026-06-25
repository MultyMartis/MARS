/**
 * Independent XLSX evidence inspector v2 — reads workbook as external artefact.
 */
import fs from 'fs';
import path from 'path';
import { createRequire } from 'module';
import { fileURLToPath } from 'url';
import { isPlaceholderValue } from '../lib/evidence-format-v5.mjs';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT = path.resolve(__dirname, '../..');

const STRICT_NARRATIVE_HEADERS = new Set([
  'replacement',
  'representative_phrases',
  'explanation',
  'error',
  'error_details',
  'commercial_hypothesis',
  'exact_action',
  'correction',
  'evidence',
  'bad_value',
]);

const METRIC_VALUE_SHEETS = new Set([
  'Audit summary',
  'Placeholder count reconciliatio',
  'Placeholder count reconciliation',
  'Semantic-risk reconciliation',
  'V6 input repair package',
  'Independent gate details',
  'QA gate decision',
]);

const FORBIDDEN_LITERALS = ['[object Object]'];

function isFourDigitNarrative(s) {
  return /^\d{4}$/.test(String(s ?? '').trim());
}

function isMetricValueSheet(sheetName, headers) {
  if (METRIC_VALUE_SHEETS.has(sheetName)) return true;
  return headers[1] === 'metric' && headers[2] === 'value';
}

/**
 * @param {string} xlsxPath
 */
export async function inspectQaRepairWorkbook(xlsxPath) {
  const require = createRequire(import.meta.url);
  const exceljsPath = path.resolve(
    ROOT,
    '../../ppc/triumph-manipulator/tools/exporter-cli/node_modules/exceljs'
  );
  if (!fs.existsSync(exceljsPath)) {
    throw new Error(`ExcelJS not found at ${exceljsPath}`);
  }
  const ExcelJS = require(exceljsPath);

  const wb = new ExcelJS.Workbook();
  await wb.xlsx.readFile(xlsxPath);

  const findings = [];
  const sheetNames = [];

  for (const ws of wb.worksheets) {
    sheetNames.push(ws.name);
    const headers = [];
    ws.eachRow((row, rowNumber) => {
      if (rowNumber === 1) {
        row.eachCell((cell, col) => {
          headers[col] = String(cell.value ?? '').toLowerCase().trim();
        });
        return;
      }

      const metricSheet = isMetricValueSheet(ws.name, headers);

      row.eachCell({ includeEmpty: true }, (cell, col) => {
        const header = headers[col] || `col${col}`;
        const raw = cell.value;
        let display;
        if (raw == null) display = '';
        else if (typeof raw === 'object' && raw.richText) display = raw.richText.map((t) => t.text).join('');
        else if (typeof raw === 'object' && raw.formula) display = String(raw.result ?? '');
        else display = String(raw);

        if (metricSheet && header === 'value') return;

        const isStrictNarrative = STRICT_NARRATIVE_HEADERS.has(header);

        if (FORBIDDEN_LITERALS.includes(display)) {
          findings.push({ sheet: ws.name, row: rowNumber, col: header, issue: 'forbidden_literal', value: display });
        }
        if (isStrictNarrative && isFourDigitNarrative(display)) {
          findings.push({ sheet: ws.name, row: rowNumber, col: header, issue: 'four_digit_narrative', value: display });
        }
        if (isStrictNarrative && display === '') {
          findings.push({ sheet: ws.name, row: rowNumber, col: header, issue: 'empty_required_evidence', value: '(empty)' });
        }
        if (isStrictNarrative && isPlaceholderValue(display)) {
          findings.push({ sheet: ws.name, row: rowNumber, col: header, issue: 'placeholder', value: display });
        }
        if ((header === 'error' || header === 'error_details') && isFourDigitNarrative(display)) {
          findings.push({ sheet: ws.name, row: rowNumber, col: header, issue: 'regression_error_leak', value: display });
        }
        if (header === 'detail' && isStrictNarrative && isPlaceholderValue(display)) {
          findings.push({ sheet: ws.name, row: rowNumber, col: header, issue: 'placeholder_detail', value: display });
        }
      });
    });
  }

  const reconciliation = {
    workbook_sheets: sheetNames.length,
    expected_sheets: 14,
    sheets_match: sheetNames.length >= 13,
    placeholder_findings: findings.filter((f) => f.issue === 'placeholder' || f.issue === 'forbidden_literal').length,
    object_coercion: findings.filter((f) => f.value === '[object Object]').length,
    numeric_narrative_970: findings.filter((f) => f.value === '970').length,
    four_digit_narrative: findings.filter((f) => f.issue === 'four_digit_narrative').length,
    empty_required: findings.filter((f) => f.issue === 'empty_required_evidence').length,
  };

  return {
    inspected_at: new Date().toISOString(),
    workbook_path: xlsxPath,
    sheets: sheetNames,
    findings,
    reconciliation,
    passed:
      findings.length === 0 &&
      reconciliation.object_coercion === 0 &&
      reconciliation.numeric_narrative_970 === 0 &&
      reconciliation.four_digit_narrative === 0,
  };
}
