"use strict";

/**
 * ORCA Sheet1 XML Builder v0.6
 * Surgical row/cell patching for xl/worksheets/sheet1.xml only.
 * Import-feedback + image/geo hygiene + safe stale data row removal (sheet1 only).
 * NOT a full OOXML engine.
 */

const { isAutotargetPhrase, TRANSPORT_ROW_AD, TRANSPORT_ROW_KEYWORD } = require("./mapping");

const DATA_START_ROW = 16;

/** Visible transport mask for stale rows (template uses «-» in structural cols). */
const TRANSPORT_MASK_VALUE = "-";

const REQUIRED_LOGICAL_KEYS = [
  "groups.group_name",
  "groups.group_number",
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

/** Commander entity IDs — verified row-14 headers; cleared in new-campaign mode. */
const ENTITY_ID_LOGICAL_KEYS = [
  "groups.group_id",
  "keywords.phrase_id",
  "ads.ad_id",
];

/** Image/creative columns — cleared on export + stale rows (search-only transport). */
const IMAGE_CREATIVE_CLEANUP_KEYS = [
  "ads.image",
  "ads.creative",
  "ads.creative_moderation_status",
];

/** Extra verified writable PPC columns cleared on stale template rows. */
const STALE_ROW_EXTRA_CLEANUP_KEYS = [
  "groups.group_negatives",
  "geo.region",
  "groups.group_number",
  ...IMAGE_CREATIVE_CLEANUP_KEYS,
];

/** Columns masked (not blanked) on stale rows to reduce Commander UI garbage. */
const STALE_ROW_MASK_KEYS = [
  "groups.group_name",
  "keywords.phrase",
  "ads.headline_1",
  "ads.headline_2",
  "ads.description",
];

/**
 * Verified metadata block cell positions (sheet Тексты, value column = 5).
 * From template introspection 2026-05-21 — NOT auto-discovered at runtime.
 */
const { TEMPLATE_METADATA_CELL_MAP } = require("./template-campaign-metadata-v1.4");

const METADATA_CELL_MAP = TEMPLATE_METADATA_CELL_MAP;

/** Probable transport columns — documented only; not cleared without verified map entry. */
const PROBABLE_TRANSPORT_KEYS = ["groups.group_number"];

class Sheet1XmlError extends Error {
  constructor(code, message, details = []) {
    super(message);
    this.name = "Sheet1XmlError";
    this.code = code;
    this.details = details;
  }
}

function escapeXml(text) {
  return String(text ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&apos;");
}

/** 1-based column index → Excel column letters (1=A, 27=AA). */
function colToLetter(col) {
  if (!Number.isInteger(col) || col < 1) {
    throw new Sheet1XmlError("INVALID_COLUMN", `Invalid column index: ${col}`);
  }
  let n = col;
  let s = "";
  while (n > 0) {
    const rem = (n - 1) % 26;
    s = String.fromCharCode(65 + rem) + s;
    n = Math.floor((n - 1) / 26);
  }
  return s;
}

function cellRef(row, col) {
  return `${colToLetter(col)}${row}`;
}

function extractRowXml(sheetXml, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  const m = sheetXml.match(re);
  return m ? m[0] : null;
}

/**
 * Patch <v> inside an existing <c r="Xnn" ...> block. Preserves attributes and <f> siblings.
 */
function patchCellInRow(rowXml, ref, value) {
  const escaped = escapeXml(value);
  const cellRe = new RegExp(
    `(<c\\s+r="${ref}"(?:\\s[^>]*)?>)([\\s\\S]*?)(</c>)`,
    "i"
  );
  const m = rowXml.match(cellRe);
  if (!m) {
    return { rowXml, patched: false, ref };
  }

  let inner = m[2];
  if (/<v>/.test(inner)) {
    inner = inner.replace(/<v>[\s\S]*?<\/v>/, `<v>${escaped}</v>`);
  } else {
    inner = `${inner}<v>${escaped}</v>`;
  }

  const patchedRow = rowXml.replace(cellRe, `${m[1]}${inner}${m[3]}`);
  return { rowXml: patchedRow, patched: true, ref };
}

function resolveColumnsFromHeaderMap(headerMapFields, logicalKeys) {
  const columns = {};
  for (const key of logicalKeys) {
    const spec = headerMapFields[key];
    if (spec?.status === "verified" && Number.isInteger(spec.column) && spec.column >= 1) {
      columns[key] = spec.column;
    }
  }
  return columns;
}

function resolveEntityIdColumns(headerMapFields) {
  return resolveColumnsFromHeaderMap(headerMapFields, ENTITY_ID_LOGICAL_KEYS);
}

function resolveWritableCleanupColumns(headerMapFields) {
  const keys = [...REQUIRED_LOGICAL_KEYS, ...STALE_ROW_EXTRA_CLEANUP_KEYS];
  return resolveColumnsFromHeaderMap(headerMapFields, keys);
}

function resolveImageCreativeColumns(headerMapFields) {
  return resolveColumnsFromHeaderMap(headerMapFields, IMAGE_CREATIVE_CLEANUP_KEYS);
}

function resolveGeoRegionColumn(headerMapFields) {
  return resolveColumnsFromHeaderMap(headerMapFields, ["geo.region"]);
}

function resolveGroupNumberColumn(headerMapFields) {
  const cols = resolveColumnsFromHeaderMap(headerMapFields, ["groups.group_number"]);
  return cols["groups.group_number"] || 6;
}

function buildFieldPatches(fillRow, columns, options = {}) {
  const rowType = fillRow.transport_row_type || TRANSPORT_ROW_AD;
  const isAdRow = rowType === TRANSPORT_ROW_AD;
  const isKeywordRow = rowType === TRANSPORT_ROW_KEYWORD;

  const fieldMap = [
    ["ads.group_additional_ad", fillRow.group_additional_ad ?? ""],
    ["groups.group_name", fillRow.group_name],
    ["groups.group_number", fillRow.group_number],
    ["keywords.phrase", isAdRow ? "" : fillRow.phrase],
    ["ads.headline_1", isKeywordRow ? "" : fillRow.headline_1],
    ["ads.headline_2", isKeywordRow ? "" : fillRow.headline_2],
    ["ads.description", isKeywordRow ? "" : fillRow.description],
    ["ads.landing_url", isKeywordRow ? "" : fillRow.landing_url],
    ["ads.display_url", isKeywordRow ? "" : fillRow.display_url],
    ["ads.ad_status", isKeywordRow ? "" : fillRow.ad_status],
    ["keywords.status", isAdRow ? "" : fillRow.keyword_status],
    ["extensions.fastlink_titles", isKeywordRow ? "" : fillRow.fastlink_titles],
    ["extensions.fastlink_descriptions", isKeywordRow ? "" : fillRow.fastlink_descriptions],
    ["extensions.fastlink_urls", isKeywordRow ? "" : fillRow.fastlink_urls],
    ["extensions.callouts", isKeywordRow ? "" : fillRow.callouts],
    ["geo.region", fillRow.geo_region],
    ["keywords.bid", isKeywordRow ? fillRow.phrase_bid ?? "" : ""],
    ["groups.group_negatives", isAdRow && fillRow.group_negatives ? fillRow.group_negatives : ""],
    ["ads.ad_type", isKeywordRow ? "" : fillRow.ad_type_transport],
    ["ads.image", ""],
    ["ads.creative", ""],
    ["ads.creative_moderation_status", ""],
  ];

  const patches = [];
  for (const [key, val] of fieldMap) {
    const col = columns[key];
    if (!col) continue;
    let value = val;
    if (key === "keywords.phrase" && isAutotargetPhrase(value)) {
      value = "";
    }
    patches.push({ key, col, value });
  }

  const preserveCommanderIds = options.newCampaignMode === false;
  if (preserveCommanderIds && isAdRow && fillRow.ad_id && columns["ads.ad_id"]) {
    patches.push({ key: "ads.ad_id", col: columns["ads.ad_id"], value: fillRow.ad_id });
  }

  return patches;
}

function buildClearPatches(columnMap, logicalKeys, value = "") {
  const patches = [];
  for (const key of logicalKeys) {
    const col = columnMap[key];
    if (!col) continue;
    patches.push({ key, col, value });
  }
  return patches;
}

function buildMaskPatches(columnMap, logicalKeys, maskValue = TRANSPORT_MASK_VALUE) {
  const patches = [];
  for (const key of logicalKeys) {
    const col = columnMap[key];
    if (!col) continue;
    patches.push({ key, col, value: maskValue });
  }
  return patches;
}

function listAllSheetRows(sheetXml) {
  const rows = [];
  const re = /<row r="(\d+)"[^>]*>/g;
  let m;
  while ((m = re.exec(sheetXml)) !== null) {
    rows.push(parseInt(m[1], 10));
  }
  return rows.sort((a, b) => a - b);
}

function listSheetDataRows(sheetXml, dataStartRow) {
  return listAllSheetRows(sheetXml).filter((n) => n >= dataStartRow);
}

function findDuplicateRowRefs(rowNumbers) {
  const seen = new Set();
  const duplicates = [];
  for (const n of rowNumbers) {
    if (seen.has(n)) duplicates.push(n);
    seen.add(n);
  }
  return duplicates;
}

function parseMergeRefMaxRow(ref) {
  let max = 0;
  for (const part of String(ref).split(":")) {
    const m = part.match(/(\d+)$/);
    if (m) max = Math.max(max, parseInt(m[1], 10));
  }
  return max;
}

function findMergeRefsBeyondRow(sheetXml, lastRow) {
  const block = sheetXml.match(/<mergeCells[\s\S]*?<\/mergeCells>/);
  if (!block) return [];
  const conflicts = [];
  const re = /ref="([^"]+)"/g;
  let m;
  while ((m = re.exec(block[0])) !== null) {
    const max = parseMergeRefMaxRow(m[1]);
    if (max > lastRow) conflicts.push(m[1]);
  }
  return conflicts;
}

function extractDimensionRef(sheetXml) {
  const m = sheetXml.match(/<dimension\s+ref="([^"]+)"/);
  return m ? m[1] : null;
}

/**
 * Update sheet dimension ref end row when format is START:COLROW (e.g. A6:BZ133).
 */
function updateSheetDimensionRef(sheetXml, lastRow) {
  const before = extractDimensionRef(sheetXml);
  if (!before) {
    return {
      sheetXml,
      updated: false,
      dimensionBefore: null,
      dimensionAfter: null,
      safeUnknown: true,
      reason: "NO_DIMENSION_ELEMENT",
    };
  }

  const parsed = before.match(/^([A-Z]+\d+):([A-Z]+)(\d+)$/);
  if (!parsed) {
    return {
      sheetXml,
      updated: false,
      dimensionBefore: before,
      dimensionAfter: before,
      safeUnknown: true,
      reason: "DIMENSION_REF_UNPARSED",
    };
  }

  const after = `${parsed[1]}:${parsed[2]}${lastRow}`;
  if (after === before) {
    return {
      sheetXml,
      updated: false,
      dimensionBefore: before,
      dimensionAfter: before,
    };
  }

  const nextSheet = sheetXml.replace(
    /<dimension\s+ref="[^"]+"/,
    `<dimension ref="${after}"`
  );

  return {
    sheetXml: nextSheet,
    updated: true,
    dimensionBefore: before,
    dimensionAfter: after,
  };
}

function removeRowXmlFromSheet(sheetXml, rowNum) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>\\s*`);
  return sheetXml.replace(re, "");
}

/**
 * Build safe removal plan for stale template data rows (rows > lastExportRow).
 */
function buildRowRemovalPlan(sheetXml, options = {}) {
  const dataStartRow = options.dataStartRow || DATA_START_ROW;
  const exportedRowCount = options.exportedRowCount || 0;
  const rowRemovalMode = options.rowRemovalMode === true;

  if (!rowRemovalMode) {
    return { enabled: false, rowRemovalMode: false };
  }

  if (!Number.isInteger(exportedRowCount) || exportedRowCount < 1) {
    throw new Sheet1XmlError(
      "INVALID_EXPORT_ROW_COUNT",
      `exportedRowCount must be >= 1 for row removal, got ${exportedRowCount}`
    );
  }

  const lastExportRow = dataStartRow + exportedRowCount - 1;
  if (lastExportRow < dataStartRow) {
    throw new Sheet1XmlError(
      "INVALID_LAST_EXPORT_ROW",
      `lastExportRow ${lastExportRow} is before dataStartRow ${dataStartRow}`
    );
  }

  const allRows = listAllSheetRows(sheetXml);
  if (!allRows.length) {
    throw new Sheet1XmlError("NO_SHEET_ROWS", "sheet1.xml contains no <row> elements");
  }

  const duplicates = findDuplicateRowRefs(allRows);
  if (duplicates.length) {
    throw new Sheet1XmlError(
      "DUPLICATE_ROW_REFS",
      "Duplicate <row r=\"…\"> references detected in sheet1.xml",
      duplicates.map(String)
    );
  }

  const maxRowBefore = Math.max(...allRows);
  const dataRows = listSheetDataRows(sheetXml, dataStartRow);
  const rowsToRemove = dataRows.filter((r) => r > lastExportRow);

  const missingExportRows = [];
  for (let i = 0; i < exportedRowCount; i++) {
    const rowNum = dataStartRow + i;
    if (!allRows.includes(rowNum)) missingExportRows.push(rowNum);
  }
  if (missingExportRows.length) {
    throw new Sheet1XmlError(
      "EXPORT_ROWS_MISSING_BEFORE_REMOVAL",
      "Cannot remove stale rows — exported ORCA rows missing from template",
      missingExportRows.map(String)
    );
  }

  const protectedViolations = rowsToRemove.filter((r) => r < dataStartRow);
  if (protectedViolations.length) {
    throw new Sheet1XmlError(
      "PROTECTED_ROWS_IN_REMOVAL_PLAN",
      "Row removal plan would touch metadata/header rows",
      protectedViolations.map(String)
    );
  }

  const mergeConflicts = findMergeRefsBeyondRow(sheetXml, lastExportRow);

  return {
    enabled: true,
    rowRemovalMode: true,
    dataStartRow,
    exportedRowCount,
    lastExportRow,
    rowsToRemove,
    rowCountBefore: allRows.length,
    maxRowBefore,
    firstRemovedRow: rowsToRemove.length ? Math.min(...rowsToRemove) : null,
    lastRemovedRow: rowsToRemove.length ? Math.max(...rowsToRemove) : null,
    mergeConflicts,
  };
}

/**
 * Remove stale template <row> nodes after lastExportRow; update dimension when deterministic.
 */
function removeStaleSheetDataRows(sheetXml, options = {}) {
  const plan = buildRowRemovalPlan(sheetXml, options);
  if (!plan.enabled) {
    return {
      sheetXml,
      rowRemovalMode: false,
      rowsRemoved: 0,
      plan,
    };
  }

  if (plan.mergeConflicts.length) {
    throw new Sheet1XmlError(
      "MERGE_REF_BEYOND_LAST_EXPORT_ROW",
      "mergeCells reference rows beyond lastExportRow — row removal unsafe",
      plan.mergeConflicts
    );
  }

  if (!plan.rowsToRemove.length) {
    if (plan.maxRowBefore > plan.lastExportRow) {
      throw new Sheet1XmlError(
        "ROW_REMOVAL_EXPECTED",
        `Template max row ${plan.maxRowBefore} > lastExportRow ${plan.lastExportRow} but no removable data rows detected`,
        [`lastExportRow=${plan.lastExportRow}`]
      );
    }
    const dimensionResult = updateSheetDimensionRef(sheetXml, plan.lastExportRow);
    return {
      sheetXml: dimensionResult.sheetXml,
      rowRemovalMode: true,
      rowsRemoved: 0,
      plan,
      dimension: dimensionResult,
      rowCountAfter: plan.rowCountBefore,
      maxRowAfter: plan.maxRowBefore,
    };
  }

  let nextSheet = sheetXml;
  let rowsRemoved = 0;
  const removedRowNumbers = [];

  for (const rowNum of [...plan.rowsToRemove].sort((a, b) => b - a)) {
    const before = nextSheet;
    nextSheet = removeRowXmlFromSheet(nextSheet, rowNum);
    if (nextSheet !== before) {
      rowsRemoved++;
      removedRowNumbers.push(rowNum);
    }
  }

  if (rowsRemoved === 0) {
    throw new Sheet1XmlError(
      "ROW_REMOVAL_FAILED",
      `Expected to remove ${plan.rowsToRemove.length} stale rows — XML pattern match removed 0`,
      plan.rowsToRemove.slice(0, 10).map(String)
    );
  }

  if (rowsRemoved !== plan.rowsToRemove.length) {
    throw new Sheet1XmlError(
      "PARTIAL_ROW_REMOVAL",
      `Removed ${rowsRemoved} of ${plan.rowsToRemove.length} planned stale rows`,
      plan.rowsToRemove.map(String)
    );
  }

  const afterRows = listAllSheetRows(nextSheet);
  const maxRowAfter = Math.max(...afterRows);

  for (let i = 0; i < plan.exportedRowCount; i++) {
    const rowNum = plan.dataStartRow + i;
    if (!afterRows.includes(rowNum)) {
      throw new Sheet1XmlError(
        "EXPORT_ROW_REMOVED",
        `Row removal accidentally removed exported row ${rowNum}`,
        [String(rowNum)]
      );
    }
  }

  if (maxRowAfter > plan.lastExportRow) {
    throw new Sheet1XmlError(
      "STALE_ROWS_REMAIN",
      `After removal, max row ${maxRowAfter} still exceeds lastExportRow ${plan.lastExportRow}`,
      afterRows.filter((r) => r > plan.lastExportRow).map(String)
    );
  }

  for (let r = 1; r < plan.dataStartRow; r++) {
    if (!afterRows.includes(r) && listAllSheetRows(sheetXml).includes(r)) {
      throw new Sheet1XmlError(
        "METADATA_ROW_REMOVED",
        `Protected row ${r} was removed — metadata/header rows must remain`,
        [String(r)]
      );
    }
  }

  const dimensionResult = updateSheetDimensionRef(nextSheet, plan.lastExportRow);
  nextSheet = dimensionResult.sheetXml;

  return {
    sheetXml: nextSheet,
    rowRemovalMode: true,
    rowsRemoved,
    removedRowNumbers,
    plan,
    dimension: dimensionResult,
    rowCountAfter: afterRows.length,
    maxRowAfter,
  };
}

function patchRowXml(rowXml, rowNum, patches) {
  let next = rowXml;
  const results = [];

  for (const p of patches) {
    const ref = cellRef(rowNum, p.col);
    const out = patchCellInRow(next, ref, p.value);
    next = out.rowXml;
    results.push({ ...p, ref, patched: out.patched });
  }

  return { rowXml: next, results };
}

function replaceRowInSheet(sheetXml, rowNum, newRowXml) {
  const re = new RegExp(`<row r="${rowNum}"[^>]*>[\\s\\S]*?</row>`);
  if (!re.test(sheetXml)) {
    throw new Sheet1XmlError(
      "ROW_NOT_FOUND",
      `Row ${rowNum} not found in sheet1.xml — cannot patch`,
      [String(rowNum)]
    );
  }
  return sheetXml.replace(re, newRowXml);
}

/**
 * Patch campaign metadata block (rows 7–12 value cells) when patches provided.
 */
function patchCampaignMetadataBlock(sheetXml, metadataPatches = {}, options = {}) {
  const enableMetadata = options.enableMetadata !== false;
  if (!enableMetadata || !metadataPatches || !Object.keys(metadataPatches).length) {
    return { sheetXml, cellsPatched: 0, patchedKeys: [] };
  }

  let nextSheet = sheetXml;
  let cellsPatched = 0;
  const patchedKeys = [];

  for (const [key, value] of Object.entries(metadataPatches)) {
    const pos = METADATA_CELL_MAP[key];
    if (!pos || value == null || value === "") continue;

    const rowXml = extractRowXml(nextSheet, pos.row);
    if (!rowXml) continue;

    const ref = cellRef(pos.row, pos.col);
    const { rowXml: patchedRow, patched } = patchCellInRow(rowXml, ref, value);
    if (patched) {
      nextSheet = replaceRowInSheet(nextSheet, pos.row, patchedRow);
      cellsPatched++;
      patchedKeys.push(key);
    }
  }

  return { sheetXml: nextSheet, cellsPatched, patchedKeys };
}

/**
 * Neutralize stale template rows (clear writable values; mask visible cols; never delete <row> nodes).
 */
function neutralizeStaleDataRows(sheetXml, options = {}) {
  const dataStartRow = options.dataStartRow || DATA_START_ROW;
  const exportedRowCount = options.exportedRowCount || 0;
  const writableColumns = options.writableColumns || {};
  const entityIdColumns = options.entityIdColumns || {};
  const enableCleanup = options.enableCleanup !== false;
  const transportMask = options.transportMaskValue ?? TRANSPORT_MASK_VALUE;

  if (!enableCleanup) {
    return {
      sheetXml,
      rowsNeutralized: 0,
      neutralizedRowNumbers: [],
      cellsCleared: 0,
      cellsMasked: 0,
    };
  }

  const allDataRows = listSheetDataRows(sheetXml, dataStartRow);
  const firstStaleRow = dataStartRow + exportedRowCount;
  const staleRows = allDataRows.filter((r) => r >= firstStaleRow);

  const columnMap = { ...writableColumns, ...entityIdColumns };
  const clearKeys = [
    ...REQUIRED_LOGICAL_KEYS,
    ...STALE_ROW_EXTRA_CLEANUP_KEYS,
    ...ENTITY_ID_LOGICAL_KEYS,
  ].filter((k) => !STALE_ROW_MASK_KEYS.includes(k));

  const clearPatches = buildClearPatches(columnMap, clearKeys, "");
  const maskPatches = buildMaskPatches(columnMap, STALE_ROW_MASK_KEYS, transportMask);

  let nextSheet = sheetXml;
  let rowsNeutralized = 0;
  let cellsCleared = 0;
  let cellsMasked = 0;
  const neutralizedRowNumbers = [];
  const unpatchedCells = [];

  for (const rowNum of staleRows) {
    const rowXml = extractRowXml(nextSheet, rowNum);
    if (!rowXml) continue;

    const clearResult = patchRowXml(rowXml, rowNum, clearPatches);
    const maskResult = patchRowXml(clearResult.rowXml, rowNum, maskPatches);

    let clearedInRow = 0;
    let maskedInRow = 0;
    for (const r of [...clearResult.results, ...maskResult.results]) {
      if (r.patched) {
        if (STALE_ROW_MASK_KEYS.includes(r.key)) maskedInRow++;
        else clearedInRow++;
      } else {
        unpatchedCells.push(`${r.ref} (${r.key})`);
      }
    }

    if (clearedInRow > 0 || maskedInRow > 0) {
      nextSheet = replaceRowInSheet(nextSheet, rowNum, maskResult.rowXml);
      rowsNeutralized++;
      cellsCleared += clearedInRow;
      cellsMasked += maskedInRow;
      neutralizedRowNumbers.push(rowNum);
    }
  }

  return {
    sheetXml: nextSheet,
    rowsNeutralized,
    neutralizedRowNumbers,
    cellsCleared,
    cellsMasked,
    unpatchedCells,
    totalDataRowsInTemplate: allDataRows.length,
    firstStaleRow,
  };
}

/**
 * Clear Commander entity ID cells on exported rows (new-campaign import intent).
 */
function clearEntityIdsOnExportedRows(sheetXml, options = {}) {
  const dataStartRow = options.dataStartRow || DATA_START_ROW;
  const exportedRowCount = options.exportedRowCount || 0;
  const entityIdColumns = options.entityIdColumns || {};
  const newCampaignMode = options.newCampaignMode === true;

  if (!newCampaignMode || !exportedRowCount) {
    return { sheetXml, rowsIdCleared: 0, idCellsCleared: 0 };
  }

  const idPatches = buildClearPatches(entityIdColumns, ENTITY_ID_LOGICAL_KEYS, "");
  let nextSheet = sheetXml;
  let rowsIdCleared = 0;
  let idCellsCleared = 0;

  for (let i = 0; i < exportedRowCount; i++) {
    const rowNum = dataStartRow + i;
    const rowXml = extractRowXml(nextSheet, rowNum);
    if (!rowXml) continue;

    const { rowXml: patchedRow, results } = patchRowXml(rowXml, rowNum, idPatches);
    const cleared = results.filter((r) => r.patched).length;
    if (cleared > 0) {
      nextSheet = replaceRowInSheet(nextSheet, rowNum, patchedRow);
      rowsIdCleared++;
      idCellsCleared += cleared;
    }
  }

  return { sheetXml: nextSheet, rowsIdCleared, idCellsCleared };
}

/**
 * Apply template-fill rows to sheet1 XML via surgical row patching (rows 16+).
 */
function patchSheet1DataRows(sheetXml, fillRows, columns, options = {}) {
  const dataStartRow = options.dataStartRow || DATA_START_ROW;
  const newCampaignMode = options.newCampaignMode !== false;
  const enableCleanup = options.enableCleanup !== false;
  const rowRemovalMode = options.rowRemovalMode !== false;
  const enableMetadata = options.enableMetadata !== false;
  const metadataPatches = options.metadataPatches || {};
  const headerMapFields = options.headerMapFields || {};
  const writableColumns =
    options.writableColumns || resolveWritableCleanupColumns(headerMapFields);
  const entityIdColumns =
    options.entityIdColumns || resolveEntityIdColumns(headerMapFields);

  const groupNumberCol =
    columns["groups.group_number"] ||
    resolveGroupNumberColumn(headerMapFields);
  const effectiveColumns = {
    ...columns,
    ...resolveGeoRegionColumn(headerMapFields),
    ...resolveImageCreativeColumns(headerMapFields),
    ...resolveColumnsFromHeaderMap(headerMapFields, [
      "ads.ad_type",
      "ads.group_additional_ad",
      "keywords.bid",
      "groups.group_negatives",
    ]),
    "groups.group_number": groupNumberCol,
  };

  let nextSheet = sheetXml;

  const metadataResult = patchCampaignMetadataBlock(nextSheet, metadataPatches, {
    enableMetadata,
  });
  nextSheet = metadataResult.sheetXml;

  const missingRows = [];
  const unpatchedCells = [];
  let rowsPatched = 0;
  let autotargetSuppressed = 0;

  for (let i = 0; i < fillRows.length; i++) {
    const rowNum = dataStartRow + i;
    const rowXml = extractRowXml(nextSheet, rowNum);
    if (!rowXml) {
      missingRows.push(rowNum);
      continue;
    }

    if (isAutotargetPhrase(fillRows[i].phrase)) {
      autotargetSuppressed++;
      fillRows[i] = { ...fillRows[i], phrase: "" };
    }

    const patches = buildFieldPatches(fillRows[i], effectiveColumns, { newCampaignMode });
    const { rowXml: patchedRow, results } = patchRowXml(rowXml, rowNum, patches);

    for (const r of results) {
      if (!r.patched) unpatchedCells.push(`${r.ref} (${r.key})`);
    }

    nextSheet = replaceRowInSheet(nextSheet, rowNum, patchedRow);
    rowsPatched++;
  }

  if (missingRows.length) {
    throw new Sheet1XmlError(
      "DATA_ROWS_MISSING",
      `Template sheet1 missing data rows starting at ${dataStartRow}`,
      missingRows.map(String)
    );
  }

  const idClearResult = clearEntityIdsOnExportedRows(nextSheet, {
    dataStartRow,
    exportedRowCount: fillRows.length,
    entityIdColumns,
    newCampaignMode,
  });
  nextSheet = idClearResult.sheetXml;

  let neutralizeResult = null;
  let rowRemovalResult = null;

  if (rowRemovalMode) {
    rowRemovalResult = removeStaleSheetDataRows(nextSheet, {
      dataStartRow,
      exportedRowCount: fillRows.length,
      rowRemovalMode: true,
    });
    nextSheet = rowRemovalResult.sheetXml;
  } else if (enableCleanup) {
    neutralizeResult = neutralizeStaleDataRows(nextSheet, {
      dataStartRow,
      exportedRowCount: fillRows.length,
      writableColumns,
      entityIdColumns,
      enableCleanup: true,
    });
    nextSheet = neutralizeResult.sheetXml;
  }

  const lastExportRow = dataStartRow + fillRows.length - 1;

  return {
    sheetXml: nextSheet,
    rowsPatched,
    lastExportRow,
    rowRemovalMode,
    cellStats: {
      rowsRequested: fillRows.length,
      rowsPatched,
      autotargetSuppressed,
      unpatchedCells,
    },
    metadataStats: metadataResult,
    rowRemovalStats: rowRemovalResult,
    cleanupStats: {
      enableCleanup,
      rowRemovalMode,
      newCampaignMode,
      entityIdColumns,
      writableColumnCount: Object.keys(writableColumns).length,
      rowsIdCleared: idClearResult.rowsIdCleared,
      idCellsCleared: idClearResult.idCellsCleared,
      rowsNeutralized: neutralizeResult?.rowsNeutralized ?? 0,
      neutralizedRowNumbers: neutralizeResult?.neutralizedRowNumbers ?? [],
      cellsClearedOnStaleRows: neutralizeResult?.cellsCleared ?? 0,
      cellsMaskedOnStaleRows: neutralizeResult?.cellsMasked ?? 0,
      totalDataRowsInTemplate:
        rowRemovalResult?.plan?.rowCountBefore ??
        neutralizeResult?.totalDataRowsInTemplate ??
        0,
      firstStaleRow:
        rowRemovalResult?.plan?.firstRemovedRow ?? neutralizeResult?.firstStaleRow ?? null,
      lastExportRow,
      staleRowUnpatchedCells: neutralizeResult?.unpatchedCells || [],
      rowsRemoved: rowRemovalResult?.rowsRemoved ?? 0,
      removedRowNumbers: rowRemovalResult?.removedRowNumbers ?? [],
      maxRowAfter: rowRemovalResult?.maxRowAfter ?? null,
      dimension: rowRemovalResult?.dimension ?? null,
    },
  };
}

module.exports = {
  Sheet1XmlError,
  escapeXml,
  colToLetter,
  cellRef,
  extractRowXml,
  patchCellInRow,
  patchRowXml,
  patchSheet1DataRows,
  patchCampaignMetadataBlock,
  neutralizeStaleDataRows,
  clearEntityIdsOnExportedRows,
  resolveEntityIdColumns,
  resolveWritableCleanupColumns,
  resolveGroupNumberColumn,
  listAllSheetRows,
  listSheetDataRows,
  buildRowRemovalPlan,
  removeStaleSheetDataRows,
  updateSheetDimensionRef,
  extractDimensionRef,
  findDuplicateRowRefs,
  removeRowXmlFromSheet,
  buildClearPatches,
  buildMaskPatches,
  DATA_START_ROW,
  REQUIRED_LOGICAL_KEYS,
  ENTITY_ID_LOGICAL_KEYS,
  STALE_ROW_EXTRA_CLEANUP_KEYS,
  STALE_ROW_MASK_KEYS,
  IMAGE_CREATIVE_CLEANUP_KEYS,
  resolveImageCreativeColumns,
  resolveGeoRegionColumn,
  METADATA_CELL_MAP,
  TRANSPORT_MASK_VALUE,
  PROBABLE_TRANSPORT_KEYS,
};
