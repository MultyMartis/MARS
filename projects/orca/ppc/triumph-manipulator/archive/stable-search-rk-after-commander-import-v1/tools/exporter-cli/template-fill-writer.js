"use strict";

/**
 * ORCA Commander Template-Fill Writer v0
 * Clones triumph-manipulator-commander-template-v0.xlsx and writes rows into sheet "Тексты".
 * XLSX integrity hardening: exact-cell writes only, no range clears, fail-closed reopen check.
 * NOT import automation · NOT Direct API · NOT runtime.
 */

const fs = require("fs");
const path = require("path");
const ExcelJS = require("exceljs");
const {
  loadHeaderMap,
  safeSetCell,
  TEMPLATE_METADATA_ROW_LIMIT,
} = require("./workbook-writer");
const { runIntegrityCheck } = require("./xlsx-integrity-check");

const DEFAULT_TEMPLATE = path.resolve(
  __dirname,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx"
);

const SHEET_NAME = "Тексты";
const HEADER_ROW = 14;
const DATA_START_ROW = 16;

/** Verified-only columns required for template-fill export. */
const REQUIRED_LOGICAL_KEYS = [
  "groups.group_name",
  "keywords.phrase",
  "ads.headline_1",
  "ads.headline_2",
  "ads.description",
  "ads.landing_url",
  "ads.display_url",
  "ads.ad_status",
  "keywords.status",
  "extensions.fastlink_titles",
  "extensions.fastlink_descriptions",
  "extensions.fastlink_urls",
  "extensions.callouts",
];

const EXTENSION_JOIN_DELIMITER = "||";

class TemplateFillError extends Error {
  constructor(code, message, details = []) {
    super(message);
    this.name = "TemplateFillError";
    this.code = code;
    this.details = details;
  }
}

function wrapWriteError(err, context) {
  if (err instanceof TemplateFillError) return err;
  const code = err.code || "SAFE_WRITE_VIOLATION";
  return new TemplateFillError(
    code,
    `${context}: ${err.message}`,
    err.details || []
  );
}

function cellText(value) {
  if (value == null) return "";
  if (typeof value === "object") {
    if (value.text) return String(value.text).trim();
    if (value.richText) {
      return value.richText.map((r) => r.text || "").join("").trim();
    }
    if (value.result != null) return String(value.result).trim();
  }
  return String(value).trim();
}

function resolveVerifiedColumns(headerMapFields) {
  const columns = {};
  const missing = [];

  for (const key of REQUIRED_LOGICAL_KEYS) {
    const spec = headerMapFields[key];
    if (!spec || spec.status !== "verified" || !spec.column) {
      missing.push(key);
      continue;
    }
    columns[key] = spec.column;
  }

  if (missing.length) {
    throw new TemplateFillError(
      "UNRESOLVED_VERIFIED_MAPPING",
      `Required verified column mapping missing: ${missing.join(", ")}`,
      missing
    );
  }

  return columns;
}

function buildAllowedColumnSet(columns) {
  return new Set(Object.values(columns).filter((c) => Number.isInteger(c) && c >= 1));
}

function verifySheetHeaders(worksheet, headerMapFields, columns) {
  const headerRow = worksheet.getRow(HEADER_ROW);
  const mismatches = [];

  for (const key of REQUIRED_LOGICAL_KEYS) {
    const spec = headerMapFields[key];
    const col = columns[key];
    const actual = cellText(headerRow.getCell(col).value);
    const expected = spec.header;
    if (expected && actual && actual !== expected) {
      mismatches.push(
        `${key}: row ${HEADER_ROW} col ${col} expected "${expected}", found "${actual}"`
      );
    }
  }

  if (mismatches.length) {
    throw new TemplateFillError(
      "HEADER_ROW_MISMATCH",
      `Template header row ${HEADER_ROW} does not match commander-header-map-v0.json`,
      mismatches
    );
  }
}

function writeTemplateFillRow(worksheet, rowNum, fillRow, columns, writeOptions) {
  const fieldMap = [
    ["groups.group_name", fillRow.group_name],
    ["keywords.phrase", fillRow.phrase],
    ["ads.headline_1", fillRow.headline_1],
    ["ads.headline_2", fillRow.headline_2],
    ["ads.description", fillRow.description],
    ["ads.landing_url", fillRow.landing_url],
    ["ads.display_url", fillRow.display_url],
    ["ads.ad_status", fillRow.ad_status],
    ["keywords.status", fillRow.keyword_status],
    ["extensions.fastlink_titles", fillRow.fastlink_titles],
    ["extensions.fastlink_descriptions", fillRow.fastlink_descriptions],
    ["extensions.fastlink_urls", fillRow.fastlink_urls],
    ["extensions.callouts", fillRow.callouts],
  ];

  for (const [key, value] of fieldMap) {
    const col = columns[key];
    if (!col) continue;
    try {
      safeSetCell(worksheet, rowNum, col, value, writeOptions);
    } catch (err) {
      throw wrapWriteError(err, `row ${rowNum} ${key}`);
    }
  }

  if (fillRow.ad_id && columns["ads.ad_id"]) {
    try {
      safeSetCell(worksheet, rowNum, columns["ads.ad_id"], fillRow.ad_id, writeOptions);
    } catch (err) {
      throw wrapWriteError(err, `row ${rowNum} ads.ad_id`);
    }
  }
}

/**
 * Clone template to outputPath (never modifies source), write fill rows into Тексты.
 * Only exact mapped cells from row 16+ are touched — no broad range clears.
 */
async function writeTemplateFill(mapped, outputPath, options = {}) {
  const templatePath = path.resolve(options.templatePath || DEFAULT_TEMPLATE);
  const headerMapPath = options.headerMapPath;
  const skipIntegrity = options.skipIntegrity === true;

  if (!fs.existsSync(templatePath)) {
    throw new TemplateFillError(
      "TEMPLATE_NOT_FOUND",
      `Commander template not found: ${templatePath}`
    );
  }

  const headerMapData = loadHeaderMap(headerMapPath);
  if (!headerMapData) {
    throw new TemplateFillError(
      "HEADER_MAP_NOT_FOUND",
      "commander-header-map-v0.json is required for template-fill export"
    );
  }

  const columns = resolveVerifiedColumns(headerMapData);
  if (headerMapData["ads.ad_id"]?.status === "verified") {
    columns["ads.ad_id"] = headerMapData["ads.ad_id"].column;
  }

  const allowedColumns = buildAllowedColumnSet(columns);
  const writeOptions = {
    dataStartRow: DATA_START_ROW,
    allowedColumns,
  };

  const fillRows = mapped.templateFillRows || [];
  if (!fillRows.length) {
    throw new TemplateFillError(
      "NO_TEMPLATE_FILL_ROWS",
      "No template-fill rows produced from document — nothing to export"
    );
  }

  const outDir = path.dirname(outputPath);
  fs.mkdirSync(outDir, { recursive: true });

  const templateStatBefore = fs.statSync(templatePath);
  fs.copyFileSync(templatePath, outputPath);
  const templateStatAfter = fs.statSync(templatePath);

  if (
    templateStatBefore.mtimeMs !== templateStatAfter.mtimeMs ||
    templateStatBefore.size !== templateStatAfter.size
  ) {
    throw new TemplateFillError(
      "TEMPLATE_SOURCE_MUTATED",
      "Original template file changed during export — aborting"
    );
  }

  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(outputPath);

  const worksheet = workbook.getWorksheet(SHEET_NAME);
  if (!worksheet) {
    throw new TemplateFillError(
      "SHEET_MISSING",
      `Worksheet "${SHEET_NAME}" not found in template`
    );
  }

  verifySheetHeaders(worksheet, headerMapData, columns);

  let rowNum = DATA_START_ROW;
  for (const fillRow of fillRows) {
    writeTemplateFillRow(worksheet, rowNum, fillRow, columns, writeOptions);
    rowNum++;
  }

  workbook.creator = "ORCA Template-Fill Export Prototype v0 (integrity-hardened)";
  workbook.lastModifiedBy = "ORCA Template-Fill Export Prototype v0 (integrity-hardened)";
  workbook.modified = new Date();

  await workbook.xlsx.writeFile(outputPath);

  let integrity = { ok: true, code: "INTEGRITY_SKIPPED", message: "Integrity check skipped" };
  if (!skipIntegrity) {
    integrity = await runIntegrityCheck(outputPath, {
      sheetName: SHEET_NAME,
      dataStartRow: DATA_START_ROW,
      rowsWritten: fillRows.length,
      mappedColumns: allowedColumns,
      columnsByKey: columns,
      probeLogicalKeys: [
        "groups.group_name",
        "keywords.phrase",
        "ads.headline_1",
      ],
    });

    if (!integrity.ok) {
      try {
        fs.unlinkSync(outputPath);
      } catch {
        /* best-effort remove corrupt output */
      }
      throw new TemplateFillError(
        "INTEGRITY_CHECK_FAILED",
        integrity.message,
        integrity.details || []
      );
    }
  }

  return {
    outputPath,
    mode: "template-fill",
    sheet: SHEET_NAME,
    headerRow: HEADER_ROW,
    dataStartRow: DATA_START_ROW,
    metadataRowLimit: TEMPLATE_METADATA_ROW_LIMIT,
    rowsWritten: fillRows.length,
    templateSource: templatePath,
    templateUnmodified: true,
    extensionJoinDelimiter: EXTENSION_JOIN_DELIMITER,
    integrity,
    writeDiscipline: {
      rangeClearRemoved: true,
      exactCellWritesOnly: true,
      mergedCellFailClosed: true,
    },
    counts: mapped.counts,
  };
}

module.exports = {
  writeTemplateFill,
  TemplateFillError,
  SHEET_NAME,
  HEADER_ROW,
  DATA_START_ROW,
  REQUIRED_LOGICAL_KEYS,
  EXTENSION_JOIN_DELIMITER,
};
