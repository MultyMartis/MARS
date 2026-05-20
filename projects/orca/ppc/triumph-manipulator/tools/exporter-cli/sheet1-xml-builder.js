"use strict";

/**
 * ORCA Sheet1 XML Builder v0
 * Surgical row/cell patching for xl/worksheets/sheet1.xml only.
 * Preserves t="str" + <v> inline string model (no sharedStrings).
 * NOT a full OOXML engine.
 */

const DATA_START_ROW = 16;

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

/** Commander entity IDs — verified row-14 headers; cleared in new-campaign mode. */
const ENTITY_ID_LOGICAL_KEYS = [
  "groups.group_id",
  "keywords.phrase_id",
  "ads.ad_id",
];

/** Extra verified writable PPC columns cleared on stale template rows. */
const STALE_ROW_EXTRA_CLEANUP_KEYS = ["groups.group_negatives", "geo.region"];

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

function buildFieldPatches(fillRow, columns, options = {}) {
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

  const patches = [];
  for (const [key, val] of fieldMap) {
    const col = columns[key];
    if (!col) continue;
    patches.push({ key, col, value: val });
  }

  const preserveCommanderIds = options.newCampaignMode === false;
  if (preserveCommanderIds && fillRow.ad_id && columns["ads.ad_id"]) {
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

function listSheetDataRows(sheetXml, dataStartRow) {
  const rows = [];
  const re = /<row r="(\d+)"[^>]*>/g;
  let m;
  while ((m = re.exec(sheetXml)) !== null) {
    const n = parseInt(m[1], 10);
    if (n >= dataStartRow) rows.push(n);
  }
  return rows.sort((a, b) => a - b);
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
 * Neutralize stale template rows (clear writable values only; never delete <row> nodes).
 */
function neutralizeStaleDataRows(sheetXml, options = {}) {
  const dataStartRow = options.dataStartRow || DATA_START_ROW;
  const exportedRowCount = options.exportedRowCount || 0;
  const writableColumns = options.writableColumns || {};
  const entityIdColumns = options.entityIdColumns || {};
  const enableCleanup = options.enableCleanup !== false;

  if (!enableCleanup) {
    return {
      sheetXml,
      rowsNeutralized: 0,
      neutralizedRowNumbers: [],
      cellsCleared: 0,
    };
  }

  const allDataRows = listSheetDataRows(sheetXml, dataStartRow);
  const firstStaleRow = dataStartRow + exportedRowCount;
  const staleRows = allDataRows.filter((r) => r >= firstStaleRow);

  const clearKeys = [
    ...REQUIRED_LOGICAL_KEYS,
    ...STALE_ROW_EXTRA_CLEANUP_KEYS,
    ...ENTITY_ID_LOGICAL_KEYS,
  ];
  const clearPatches = buildClearPatches(
    { ...writableColumns, ...entityIdColumns },
    clearKeys,
    ""
  );

  let nextSheet = sheetXml;
  let rowsNeutralized = 0;
  let cellsCleared = 0;
  const neutralizedRowNumbers = [];
  const unpatchedCells = [];

  for (const rowNum of staleRows) {
    const rowXml = extractRowXml(nextSheet, rowNum);
    if (!rowXml) continue;

    const { rowXml: patchedRow, results } = patchRowXml(rowXml, rowNum, clearPatches);
    let clearedInRow = 0;
    for (const r of results) {
      if (r.patched) clearedInRow++;
      else unpatchedCells.push(`${r.ref} (${r.key})`);
    }

    if (clearedInRow > 0) {
      nextSheet = replaceRowInSheet(nextSheet, rowNum, patchedRow);
      rowsNeutralized++;
      cellsCleared += clearedInRow;
      neutralizedRowNumbers.push(rowNum);
    }
  }

  return {
    sheetXml: nextSheet,
    rowsNeutralized,
    neutralizedRowNumbers,
    cellsCleared,
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
 * Optional stale-row cleanup and new-campaign entity ID isolation.
 * @param {string} sheetXml - raw worksheet XML (UTF-8 string)
 * @param {object[]} fillRows
 * @param {Record<string,number>} columns - logical key → 1-based column
 * @param {object} [options]
 * @returns {{ sheetXml: string, rowsPatched: number, cellStats: object, cleanupStats: object }}
 */
function patchSheet1DataRows(sheetXml, fillRows, columns, options = {}) {
  const dataStartRow = options.dataStartRow || DATA_START_ROW;
  const newCampaignMode = options.newCampaignMode !== false;
  const enableCleanup = options.enableCleanup !== false;
  const headerMapFields = options.headerMapFields || {};
  const writableColumns =
    options.writableColumns || resolveWritableCleanupColumns(headerMapFields);
  const entityIdColumns =
    options.entityIdColumns || resolveEntityIdColumns(headerMapFields);

  const missingRows = [];
  const unpatchedCells = [];
  let nextSheet = sheetXml;
  let rowsPatched = 0;

  for (let i = 0; i < fillRows.length; i++) {
    const rowNum = dataStartRow + i;
    const rowXml = extractRowXml(nextSheet, rowNum);
    if (!rowXml) {
      missingRows.push(rowNum);
      continue;
    }

    const patches = buildFieldPatches(fillRows[i], columns, { newCampaignMode });
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

  const neutralizeResult = neutralizeStaleDataRows(nextSheet, {
    dataStartRow,
    exportedRowCount: fillRows.length,
    writableColumns,
    entityIdColumns,
    enableCleanup,
  });
  nextSheet = neutralizeResult.sheetXml;

  return {
    sheetXml: nextSheet,
    rowsPatched,
    cellStats: {
      rowsRequested: fillRows.length,
      rowsPatched,
      unpatchedCells,
    },
    cleanupStats: {
      enableCleanup,
      newCampaignMode,
      entityIdColumns,
      writableColumnCount: Object.keys(writableColumns).length,
      rowsIdCleared: idClearResult.rowsIdCleared,
      idCellsCleared: idClearResult.idCellsCleared,
      rowsNeutralized: neutralizeResult.rowsNeutralized,
      neutralizedRowNumbers: neutralizeResult.neutralizedRowNumbers,
      cellsClearedOnStaleRows: neutralizeResult.cellsCleared,
      totalDataRowsInTemplate: neutralizeResult.totalDataRowsInTemplate,
      firstStaleRow: neutralizeResult.firstStaleRow,
      staleRowUnpatchedCells: neutralizeResult.unpatchedCells || [],
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
  neutralizeStaleDataRows,
  clearEntityIdsOnExportedRows,
  resolveEntityIdColumns,
  resolveWritableCleanupColumns,
  listSheetDataRows,
  buildClearPatches,
  DATA_START_ROW,
  REQUIRED_LOGICAL_KEYS,
  ENTITY_ID_LOGICAL_KEYS,
  STALE_ROW_EXTRA_CLEANUP_KEYS,
  PROBABLE_TRANSPORT_KEYS,
};
