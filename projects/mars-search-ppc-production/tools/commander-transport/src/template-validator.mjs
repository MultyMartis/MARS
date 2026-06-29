import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import path from 'node:path';
import ExcelJS from 'exceljs';
import {
  COMMANDER_COLUMN_COUNT,
  COMMANDER_HEADER_ROW,
  COMMANDER_SHEET_REGIONS,
  COMMANDER_SHEET_TEXTS,
  EXPECTED_TEMPLATE_SHA256,
  REQUIRED_REGION_VALUE,
  TEMPLATE_MISMATCH_STOP,
} from './constants.mjs';
import { assertReadablePath } from './filesystem-guard.mjs';

/**
 * @param {string} filePath
 */
export async function computeSha256(filePath) {
  const buf = await readFile(filePath);
  return createHash('sha256').update(buf).digest('hex');
}

/**
 * @param {import('exceljs').Worksheet} sheet
 * @param {number} rowNum
 */
function countPopulatedColumns(sheet, rowNum) {
  const row = sheet.getRow(rowNum);
  let maxCol = 0;
  row.eachCell({ includeEmpty: false }, (cell, colNumber) => {
    if (cell.value !== null && cell.value !== undefined && String(cell.value).trim() !== '') {
      maxCol = Math.max(maxCol, colNumber);
    }
  });
  return maxCol;
}

/**
 * @param {import('exceljs').Worksheet} sheet
 */
function sheetHasRegionValue(sheet, regionName) {
  let found = false;
  sheet.eachRow({ includeEmpty: true }, (row) => {
    row.eachCell({ includeEmpty: true }, (cell) => {
      const text = cell.value == null ? '' : String(cell.value).trim();
      if (text === regionName) found = true;
    });
  });
  return found;
}

/**
 * @param {string} templatePath
 * @param {object} [options]
 */
export async function validateTemplate(templatePath, options = {}) {
  const failures = [];
  const resolved = options.skipPathGuard
    ? path.resolve(templatePath)
    : assertReadablePath(templatePath, options);


  let sha256;
  try {
    sha256 = await computeSha256(resolved);
  } catch (err) {
    failures.push({ check: 'exists', message: String(err.message) });
    return failResult(failures, null);
  }

  if (sha256 !== EXPECTED_TEMPLATE_SHA256) {
    failures.push({
      check: 'sha256',
      message: `SHA-256 mismatch: expected ${EXPECTED_TEMPLATE_SHA256}, got ${sha256}`,
    });
  }

  const workbook = new ExcelJS.Workbook();
  try {
    await workbook.xlsx.readFile(resolved);
  } catch (err) {
    failures.push({ check: 'workbook', message: `Cannot read workbook: ${err.message}` });
    return failResult(failures, sha256);
  }

  const textsSheet = workbook.getWorksheet(COMMANDER_SHEET_TEXTS);
  if (!textsSheet) {
    failures.push({ check: 'sheet_texts', message: `Sheet "${COMMANDER_SHEET_TEXTS}" missing` });
  } else {
    const actualCols = textsSheet.actualColumnCount || textsSheet.columnCount || 0;
    if (actualCols < COMMANDER_COLUMN_COUNT) {
      failures.push({
        check: 'column_count',
        message: `Sheet column count ${actualCols} < ${COMMANDER_COLUMN_COUNT}`,
      });
    }
    const headerCell = textsSheet.getRow(COMMANDER_HEADER_ROW).getCell(5);
    if (!headerCell?.value) {
      failures.push({
        check: 'header_row',
        message: `Header row ${COMMANDER_HEADER_ROW} appears empty at column 5`,
      });
    }
  }

  const regionsSheet = workbook.getWorksheet(COMMANDER_SHEET_REGIONS);
  if (!regionsSheet) {
    failures.push({ check: 'sheet_regions', message: `Sheet "${COMMANDER_SHEET_REGIONS}" missing` });
  } else if (!sheetHasRegionValue(regionsSheet, REQUIRED_REGION_VALUE)) {
    failures.push({
      check: 'region_dictionary',
      message: `Required region "${REQUIRED_REGION_VALUE}" not found in "${COMMANDER_SHEET_REGIONS}"`,
    });
  }

  if (failures.length > 0) {
    return failResult(failures, sha256);
  }

  return {
    ok: true,
    stop_code: null,
    template_path: resolved,
    sha256,
    sheet_texts: COMMANDER_SHEET_TEXTS,
    header_row: COMMANDER_HEADER_ROW,
    column_count: COMMANDER_COLUMN_COUNT,
    required_region: REQUIRED_REGION_VALUE,
  };
}

function failResult(failures, sha256) {
  return {
    ok: false,
    stop_code: TEMPLATE_MISMATCH_STOP,
    failures,
    sha256,
  };
}

export async function assertTemplateValid(templatePath, options = {}) {
  const result = await validateTemplate(templatePath, options);
  if (!result.ok) {
    const err = new Error(TEMPLATE_MISMATCH_STOP);
    err.result = result;
    throw err;
  }
  return result;
}
