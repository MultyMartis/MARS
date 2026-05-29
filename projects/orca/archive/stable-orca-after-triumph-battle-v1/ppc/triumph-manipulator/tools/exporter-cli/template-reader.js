#!/usr/bin/env node
"use strict";

/**
 * ORCA Commander Template Reader v0
 * Template introspection only — NOT import automation, NOT Direct API, NOT runtime.
 *
 * Reads triumph-manipulator-commander-template-v0.xlsx, enumerates sheets,
 * detects header rows, builds commander-header-map-v0.json and template-sheet-index-v0.json.
 */

const fs = require("fs");
const path = require("path");
const ExcelJS = require("exceljs");

const DEFAULT_TEMPLATE = path.resolve(
  __dirname,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx"
);

const OUT_DIR = __dirname;
const SHEET_INDEX_FILE = path.join(OUT_DIR, "template-sheet-index-v0.json");
const HEADER_MAP_FILE = path.join(OUT_DIR, "commander-header-map-v0.json");

/** Logical ORCA field → candidate template headers (Russian literals from contract docs). */
const LOGICAL_CANDIDATES = Object.freeze({
  "campaigns.campaign_type": {
    sheet: "Тексты",
    candidates: ["Тип кампании:"],
    region: "campaign_metadata_block",
    notes: "Key-value row above data table, not a column header",
  },
  "campaigns.campaign_negatives": {
    sheet: "Тексты",
    candidates: ["Минус-фразы на кампанию:"],
    region: "campaign_metadata_block",
    notes: "Campaign-level minus phrases in metadata block",
  },
  "campaigns.promotion_url": {
    sheet: "Тексты",
    candidates: ["Объект продвижения:"],
    region: "campaign_metadata_block",
    notes: "Campaign promotion URL — may differ from per-ad Ссылка",
  },
  "groups.group_name": {
    sheet: "Тексты",
    candidates: ["Название группы"],
    region: "data_table",
  },
  "groups.group_id": {
    sheet: "Тексты",
    candidates: ["ID группы"],
    region: "data_table",
  },
  "keywords.phrase": {
    sheet: "Тексты",
    candidates: ["Фраза (с минус-словами)"],
    region: "data_table",
  },
  "keywords.phrase_id": {
    sheet: "Тексты",
    candidates: ["ID фразы"],
    region: "data_table",
  },
  "keywords.status": {
    sheet: "Тексты",
    candidates: ["Статус фразы"],
    region: "data_table",
  },
  "keywords.match_type": {
    sheet: "Тексты",
    candidates: [],
    region: "unknown",
    notes:
      "No dedicated match-type column found — match may be encoded inside phrase text",
  },
  "ads.headline_1": {
    sheet: "Тексты",
    candidates: ["Заголовок 1"],
    region: "data_table",
  },
  "ads.headline_2": {
    sheet: "Тексты",
    candidates: ["Заголовок 2"],
    region: "data_table",
  },
  "ads.description": {
    sheet: "Тексты",
    candidates: ["Текст"],
    region: "data_table",
  },
  "ads.ad_id": {
    sheet: "Тексты",
    candidates: ["ID объявления"],
    region: "data_table",
  },
  "ads.landing_url": {
    sheet: "Тексты",
    candidates: ["Ссылка"],
    region: "data_table",
  },
  "ads.display_url": {
    sheet: "Тексты",
    candidates: ["Отображаемая ссылка"],
    region: "data_table",
  },
  "ads.ad_status": {
    sheet: "Тексты",
    candidates: ["Статус объявления"],
    region: "data_table",
  },
  "ads.ad_type": {
    sheet: "Тексты",
    candidates: ["Тип объявления"],
    region: "data_table",
  },
  "extensions.fastlink_titles": {
    sheet: "Тексты",
    candidates: ["Заголовки быстрых ссылок"],
    region: "data_table",
    notes: "Combined multi-value cell format — SAFE UNKNOWN for row expansion",
  },
  "extensions.fastlink_descriptions": {
    sheet: "Тексты",
    candidates: ["Описания быстрых ссылок"],
    region: "data_table",
    notes: "Combined multi-value cell format — SAFE UNKNOWN",
  },
  "extensions.fastlink_urls": {
    sheet: "Тексты",
    candidates: ["Адреса быстрых ссылок"],
    region: "data_table",
    notes: "Combined multi-value cell format — SAFE UNKNOWN",
  },
  "extensions.callouts": {
    sheet: "Тексты",
    candidates: ["Уточнения"],
    region: "data_table",
    notes: "Callouts as combined Уточнения column — not one-row-per-callout",
  },
  "groups.group_negatives": {
    sheet: "Тексты",
    candidates: ["Минус-фразы на группу"],
    region: "data_table",
  },
  "geo.region": {
    sheet: "Тексты",
    candidates: ["Регион"],
    region: "data_table",
  },
  "campaigns.campaign_name": {
    sheet: "Тексты",
    candidates: [],
    region: "unknown",
    notes: "No dedicated campaign name column in data table — SAFE UNKNOWN",
  },
  "campaigns.primary_region": {
    sheet: "Регионы",
    candidates: ["Регионы"],
    region: "reference_tree",
    notes: "Separate reference sheet — not a flat campaign column",
  },
});

function cellText(value) {
  if (value == null) return "";
  if (typeof value === "object") {
    if (value.text) return String(value.text).trim();
    if (value.richText) {
      return value.richText.map((r) => r.text || "").join("").trim();
    }
    if (value.result != null) return String(value.result).trim();
    if (value.hyperlink) return String(value.hyperlink).trim();
    return "";
  }
  return String(value).trim();
}

function rowHasContent(row, maxCol = 120) {
  for (let c = 1; c <= maxCol; c++) {
    const t = cellText(row.getCell(c).value);
    if (t) return true;
  }
  return false;
}

function extractRowValues(row, maxCol = 120) {
  const cells = [];
  for (let c = 1; c <= maxCol; c++) {
    const t = cellText(row.getCell(c).value);
    if (t) cells.push({ col: c, value: t });
  }
  return cells;
}

/**
 * Score a row as a probable header: many non-empty cells, mostly short labels.
 */
function scoreHeaderRow(cells) {
  if (cells.length < 3) return 0;
  const unique = new Set(cells.map((c) => c.value));
  const shortLabels = cells.filter((c) => c.value.length > 0 && c.value.length < 80).length;
  return cells.length * 2 + unique.size + shortLabels;
}

function findProbableHeaderRows(worksheet, scanRows = 30) {
  const candidates = [];
  const limit = Math.min(scanRows, worksheet.rowCount || scanRows);
  for (let r = 1; r <= limit; r++) {
    const row = worksheet.getRow(r);
    if (!rowHasContent(row)) continue;
    const cells = extractRowValues(row);
    const score = scoreHeaderRow(cells);
    if (score >= 12) {
      candidates.push({
        row: r,
        score,
        nonEmptyCount: cells.length,
        preview: cells.slice(0, 12).map((c) => c.value),
      });
    }
  }
  candidates.sort((a, b) => b.score - a.score || a.row - b.row);

  // Commander templates often use dual header rows (main + length/sub-labels).
  // Prefer the earlier row when two consecutive candidates have similar density.
  if (candidates.length >= 2) {
    const top = candidates[0];
    const next = candidates[1];
    if (
      next.row === top.row - 1 &&
      Math.abs(top.nonEmptyCount - next.nonEmptyCount) <= 3
    ) {
      return [next, top, ...candidates.slice(2)];
    }
  }

  return candidates;
}

function buildHeaderIndex(worksheet, headerRowNum) {
  const row = worksheet.getRow(headerRowNum);
  const headers = [];
  const byName = {};
  for (let c = 1; c <= (worksheet.columnCount || 120); c++) {
    const t = cellText(row.getCell(c).value);
    if (!t) continue;
    const entry = { col: c, header: t };
    headers.push(entry);
    if (!byName[t]) byName[t] = [];
    byName[t].push(c);
  }
  return { row: headerRowNum, headers, byName };
}

function detectCampaignMetadataBlock(worksheet, beforeRow) {
  const block = [];
  for (let r = 1; r < beforeRow; r++) {
    const row = worksheet.getRow(r);
    const cells = extractRowValues(row);
    for (const cell of cells) {
      if (cell.value.endsWith(":") || cell.value.includes(":")) {
        block.push({ row: r, col: cell.col, label: cell.value });
      }
    }
  }
  return block;
}

function resolveLogicalMappings(sheetAnalyses) {
  const textsSheet = sheetAnalyses.find((s) => s.name === "Тексты");
  const headerByName = textsSheet?.primaryHeader?.byName || {};
  const metadataLabels = new Set(
    (textsSheet?.campaignMetadataBlock || []).map((m) => m.label.replace(/:$/, ""))
  );

  const map = {};
  const generatedAt = new Date().toISOString();

  for (const [logicalKey, spec] of Object.entries(LOGICAL_CANDIDATES)) {
    const entry = {
      logical: logicalKey,
      sheet: spec.sheet,
      region: spec.region,
      status: "unknown",
      notes: spec.notes || null,
    };

    if (spec.region === "campaign_metadata_block") {
      const label = spec.candidates[0];
      const found = (textsSheet?.campaignMetadataBlock || []).some(
        (m) => m.label === label || m.label.startsWith(label.replace(":", ""))
      );
      if (found) {
        entry.header = label;
        entry.status = "verified";
      } else if (spec.candidates.length === 0) {
        entry.status = "unsupported";
      } else {
        entry.status = "unknown";
        entry.safe_unknown = "Metadata label not found in template scan";
      }
    } else if (spec.region === "reference_tree") {
      const sheet = sheetAnalyses.find((s) => s.name === spec.sheet);
      if (sheet) {
        entry.header = spec.candidates[0] || null;
        entry.status = "probable";
        entry.safe_unknown =
          "Region reference tree — not a direct export column for campaigns.primary_region";
      } else {
        entry.status = "unsupported";
      }
    } else if (spec.candidates.length === 0) {
      entry.status = "unsupported";
      entry.safe_unknown = spec.notes || "No candidate headers defined";
    } else {
      const headerName = spec.candidates[0];
      const cols = headerByName[headerName];
      if (cols && cols.length === 1) {
        entry.header = headerName;
        entry.column = cols[0];
        entry.status = "verified";
      } else if (cols && cols.length > 1) {
        entry.header = headerName;
        entry.column = Math.min(...cols);
        entry.columns = cols;
        entry.status = "probable";
        entry.safe_unknown =
          "Duplicate header label in row — using leftmost column; combinatorics columns may share label";
      } else {
        const partial = Object.keys(headerByName).find(
          (h) => h.includes(headerName) || headerName.includes(h)
        );
        if (partial) {
          entry.header = partial;
          entry.column = headerByName[partial][0];
          entry.status = "probable";
        } else {
          entry.status = "unknown";
          entry.safe_unknown = `Header "${headerName}" not found in primary header row`;
        }
      }
    }

    map[logicalKey] = entry;
  }

  return {
    version: "commander-header-map-v0",
    template_file: "triumph-manipulator-commander-template-v0.xlsx",
    generated_at: generatedAt,
    disclaimer:
      "Template introspection artifact only. NOT import automation. Human review mandatory.",
    fields: map,
  };
}

async function analyzeTemplate(templatePath) {
  if (!fs.existsSync(templatePath)) {
    throw new Error(`Template not found: ${templatePath}`);
  }

  const workbook = new ExcelJS.Workbook();
  await workbook.xlsx.readFile(templatePath);

  const sheetAnalyses = [];

  for (const ws of workbook.worksheets) {
    const firstNonEmpty = [];
    for (let r = 1; r <= Math.min(40, ws.rowCount || 40); r++) {
      if (rowHasContent(ws.getRow(r))) {
        firstNonEmpty.push(r);
        if (firstNonEmpty.length >= 3) break;
      }
    }

    const headerCandidates = findProbableHeaderRows(ws);
    const primaryHeaderRow = headerCandidates[0]?.row ?? null;
    let primaryHeader = null;
    if (primaryHeaderRow) {
      primaryHeader = buildHeaderIndex(ws, primaryHeaderRow);
    }

    let campaignMetadataBlock = [];
    let dataStartRow = null;
    if (ws.name === "Тексты" && primaryHeaderRow) {
      campaignMetadataBlock = detectCampaignMetadataBlock(ws, primaryHeaderRow);
      dataStartRow = primaryHeaderRow + 1;
    }

    let entityRegion = "reference_or_dictionary";
    if (ws.name === "Тексты") entityRegion = "combined_text_blocks";
    if (ws.name === "Регионы") entityRegion = "geo_reference_tree";

    sheetAnalyses.push({
      name: ws.name,
      rowCount: ws.rowCount,
      columnCount: ws.columnCount,
      firstNonEmptyRows: firstNonEmpty,
      probableHeaderRows: headerCandidates.slice(0, 5),
      primaryHeaderRow,
      primaryHeader: primaryHeader
        ? {
            row: primaryHeader.row,
            headerCount: primaryHeader.headers.length,
            headers: primaryHeader.headers,
            byName: primaryHeader.byName,
          }
        : null,
      campaignMetadataBlock,
      dataStartRow,
      entityRegion,
    });
  }

  const headerMap = resolveLogicalMappings(sheetAnalyses);

  const sheetIndex = {
    version: "template-sheet-index-v0",
    template_file: path.basename(templatePath),
    template_path_relative:
      "../../assets/direct-commander-template/triumph-manipulator-commander-template-v0.xlsx",
    analyzed_at: new Date().toISOString(),
    sheet_count: sheetAnalyses.length,
    disclaimer:
      "Structural index from local template read. NOT proof of Commander import compatibility.",
    sheets: sheetAnalyses.map((s) => ({
      name: s.name,
      rowCount: s.rowCount,
      columnCount: s.columnCount,
      entityRegion: s.entityRegion,
      firstNonEmptyRows: s.firstNonEmptyRows,
      primaryHeaderRow: s.primaryHeaderRow,
      primaryHeaderCount: s.primaryHeader?.headerCount ?? 0,
      dataStartRow: s.dataStartRow,
      campaignMetadataLabels: (s.campaignMetadataBlock || []).map((m) => m.label),
      probableHeaderRows: s.probableHeaderRows,
    })),
    fidelity_notes: {
      prototype_sheet_model: ["campaigns", "groups", "keywords", "ads", "extensions"],
      template_sheet_model: ["Тексты", "Регионы", "Словарь значений полей"],
      structural_mismatch:
        "Template uses single combined Тексты sheet; prototype uses five logical sheets",
      safe_unknown: [
        "Hidden workbook logic",
        "Formatting and merged cells",
        "Combined fastlink/callout cell encoding",
        "Match type column absence",
        "Campaign name column absence in data table",
      ],
    },
  };

  return { sheetIndex, headerMap, sheetAnalyses };
}

function printAnalysis(sheetAnalyses, headerMap) {
  console.log("\n--- ORCA Commander Template Reader v0 ---");
  console.log("Template introspection only · NOT import · NOT Direct API\n");

  for (const s of sheetAnalyses) {
    console.log(`Sheet: ${s.name} (${s.rowCount} rows × ${s.columnCount} cols)`);
    console.log(`  Region: ${s.entityRegion}`);
    if (s.primaryHeaderRow) {
      console.log(
        `  Primary header row: ${s.primaryHeaderRow} (${s.primaryHeader?.headerCount} headers)`
      );
    }
    if (s.dataStartRow) {
      console.log(`  Data starts: row ${s.dataStartRow}`);
    }
    if (s.campaignMetadataBlock?.length) {
      console.log(`  Campaign metadata labels: ${s.campaignMetadataBlock.length}`);
    }
  }

  const verified = Object.values(headerMap.fields).filter((f) => f.status === "verified");
  const probable = Object.values(headerMap.fields).filter((f) => f.status === "probable");
  const unknown = Object.values(headerMap.fields).filter((f) => f.status === "unknown");
  const unsupported = Object.values(headerMap.fields).filter(
    (f) => f.status === "unsupported"
  );

  console.log("\nHeader map summary:");
  console.log(`  verified:    ${verified.length}`);
  console.log(`  probable:    ${probable.length}`);
  console.log(`  unknown:     ${unknown.length}`);
  console.log(`  unsupported: ${unsupported.length}`);
  console.log("\nHuman review required before Commander import.");
}

async function main() {
  const templateArg = process.argv[2];
  const templatePath = path.resolve(templateArg || DEFAULT_TEMPLATE);
  const writeOutputs = !process.argv.includes("--stdout-only");

  const { sheetIndex, headerMap, sheetAnalyses } = await analyzeTemplate(templatePath);

  printAnalysis(sheetAnalyses, headerMap);

  if (writeOutputs) {
    fs.writeFileSync(SHEET_INDEX_FILE, JSON.stringify(sheetIndex, null, 2), "utf8");
    fs.writeFileSync(HEADER_MAP_FILE, JSON.stringify(headerMap, null, 2), "utf8");
    console.log(`\nWrote: ${SHEET_INDEX_FILE}`);
    console.log(`Wrote: ${HEADER_MAP_FILE}`);
  }
}

if (require.main === module) {
  main().catch((err) => {
    console.error(`[FAILED] ${err.message}`);
    process.exit(1);
  });
}

module.exports = {
  analyzeTemplate,
  resolveLogicalMappings,
  cellText,
  DEFAULT_TEMPLATE,
  HEADER_MAP_FILE,
  SHEET_INDEX_FILE,
};
