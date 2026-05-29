"use strict";

/**
 * ORCA XLSX Integrity Check v0
 * Reopens generated workbook via ExcelJS — fail-closed transport validation.
 * NOT binary XML parsing · NOT import automation · NOT runtime.
 */

const fs = require("fs");
const ExcelJS = require("exceljs");

function cellText(value) {
  if (value == null) return "";
  if (typeof value === "object") {
    if (value.text) return String(value.text).trim();
    if (value.richText) {
      return value.richText.map((r) => r.text || "").join("").trim();
    }
    if (value.result != null) return String(value.result).trim();
    if (value.formula) return String(value.formula).trim();
  }
  if (typeof value === "number") {
    if (Number.isNaN(value)) return "";
    return String(value);
  }
  return String(value).trim();
}

/**
 * @param {string} filePath
 * @param {object} options
 * @param {string} options.sheetName - required sheet (e.g. Тексты)
 * @param {number} options.dataStartRow
 * @param {number} options.rowsWritten - expected data rows
 * @param {Set<number>|number[]} options.mappedColumns - verified column indexes
 * @param {string[]} [options.probeLogicalKeys] - keys to require non-empty values
 * @param {"first-row"|"any-row"} [options.probeLogicalKeysMode] - first row only vs any data row
 * @param {Record<string,number>} [options.columnsByKey] - logical key → column
 */
async function runIntegrityCheck(filePath, options = {}) {
  const {
    sheetName,
    dataStartRow = 16,
    rowsWritten = 0,
    mappedColumns = [],
    columnsByKey = {},
    probeLogicalKeys = ["groups.group_name", "keywords.phrase", "ads.headline_1"],
    probeLogicalKeysMode = "first-row",
  } = options;

  const details = [];
  const colSet =
    mappedColumns instanceof Set
      ? mappedColumns
      : new Set(mappedColumns);

  if (!filePath || !fs.existsSync(filePath)) {
    return fail("FILE_MISSING", `Output file not found: ${filePath}`, details);
  }

  const stat = fs.statSync(filePath);
  if (!stat.size) {
    return fail("EMPTY_FILE", "Output file is zero bytes", details);
  }

  const workbook = new ExcelJS.Workbook();
  try {
    await workbook.xlsx.readFile(filePath);
  } catch (err) {
    return fail(
      "WORKBOOK_LOAD_FAILED",
      `ExcelJS could not reopen workbook: ${err.message}`,
      details
    );
  }

  const sheetNames = workbook.worksheets.map((ws) => ws.name);
  if (!sheetNames.length) {
    return fail("NO_SHEETS", "Workbook has no readable worksheets", details);
  }

  details.push(`Sheets readable: ${sheetNames.length} (${sheetNames.join(", ")})`);

  const worksheet = workbook.getWorksheet(sheetName);
  if (!worksheet) {
    return fail(
      "SHEET_MISSING",
      `Required sheet "${sheetName}" not found after reopen`,
      details
    );
  }

  let cellsScanned = 0;
  let dataRowsWithCells = 0;
  const lastRow = dataStartRow + Math.max(rowsWritten, 0) - 1;

  for (let r = dataStartRow; r <= lastRow; r++) {
    let rowHasMappedValue = false;
    for (const col of colSet) {
      const cell = worksheet.getCell(r, col);
      cellsScanned++;
      const text = cellText(cell.value);
      if (text.length) rowHasMappedValue = true;
    }
    if (rowHasMappedValue) dataRowsWithCells++;
  }

  if (rowsWritten > 0 && dataRowsWithCells < rowsWritten) {
    return fail(
      "WRITTEN_ROWS_MISSING",
      `Expected ${rowsWritten} data rows with mapped values from row ${dataStartRow}; found ${dataRowsWithCells}`,
      details
    );
  }

  if (rowsWritten > 0 && probeLogicalKeys.length) {
    const firstRow = dataStartRow;
    const lastDataRow = dataStartRow + rowsWritten - 1;
    const missingProbes = [];

    for (const key of probeLogicalKeys) {
      const col = columnsByKey[key];
      if (!col) continue;

      if (probeLogicalKeysMode === "any-row") {
        let found = false;
        for (let r = dataStartRow; r <= lastDataRow; r++) {
          if (cellText(worksheet.getCell(r, col).value).length) {
            found = true;
            break;
          }
        }
        if (!found) missingProbes.push(`${key} (col ${col}, no row in block)`);
        continue;
      }

      const text = cellText(worksheet.getCell(firstRow, col).value);
      if (!text.length) missingProbes.push(`${key} (col ${col})`);
    }

    if (missingProbes.length) {
      const scope =
        probeLogicalKeysMode === "any-row"
          ? `rows ${firstRow}–${lastDataRow}`
          : `first data row ${firstRow}`;
      return fail(
        "MAPPED_COLUMNS_UNREADABLE",
        `${scope} missing expected values: ${missingProbes.join(", ")}`,
        details
      );
    }
  }

  for (const col of colSet) {
    try {
      worksheet.getCell(dataStartRow, col);
    } catch (err) {
      return fail(
        "COLUMN_ACCESS_FAILED",
        `Cannot read column ${col} on row ${dataStartRow}: ${err.message}`,
        details
      );
    }
  }

  return {
    ok: true,
    code: "INTEGRITY_OK",
    message: "Workbook reopened successfully; required sheet and mapped columns readable",
    details,
    stats: {
      fileBytes: stat.size,
      sheetCount: sheetNames.length,
      sheetName,
      dataStartRow,
      rowsWritten,
      dataRowsWithCells,
      mappedColumnsChecked: colSet.size,
      cellsScanned,
    },
  };
}

function fail(code, message, details) {
  return {
    ok: false,
    code,
    message,
    details: [...details, message],
    stats: null,
  };
}

module.exports = {
  runIntegrityCheck,
  cellText,
};

