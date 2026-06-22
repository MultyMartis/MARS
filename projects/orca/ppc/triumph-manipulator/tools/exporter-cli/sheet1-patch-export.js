#!/usr/bin/env node
"use strict";

/**
 * ORCA XLSX Sheet1 Patch Export Prototype v0
 * ZIP-level patch: modify ONLY xl/worksheets/sheet1.xml; preserve sheet2/sheet3/rels.
 * ExcelJS used for mapping/diagnostics/reopen only — NOT full workbook serialization.
 * NOT production exporter · NOT Direct API · NOT runtime.
 */

const fs = require("fs");
const path = require("path");

const { runPrecheck } = require("./precheck");
const { mapDocument } = require("./mapping");
const { loadHeaderMap } = require("./workbook-writer");
const { runIntegrityCheck } = require("./xlsx-integrity-check");
const {
  patchSheet1DataRows,
  resolveEntityIdColumns,
  resolveWritableCleanupColumns,
  Sheet1XmlError,
  DATA_START_ROW,
  REQUIRED_LOGICAL_KEYS,
  ENTITY_ID_LOGICAL_KEYS,
} = require("./sheet1-xml-builder");
const {
  readZipEntryUtf8,
  patchSheet1InWorkbook,
  verifyPreservedEntries,
  ZipPatchError,
} = require("./xlsx-zip-patch");
const {
  enforceLegacyBoundary,
  emitLegacyBlock,
  isDiagnosticContext,
} = require("../../../../../mars-search-ppc-production/runtime/src/legacy-entry-boundary.cjs");
const {
  buildStructureIndex,
  compareIndexes,
} = require("./ooxml-forensics");

const EXPORTER_LABEL = "ORCA Commander Transport Split v1.4";
const DEFAULT_IMPORT_REFINED_OUTPUT = path.join(
  __dirname,
  "output",
  "triumph-sheet1-patch-import-refined-v0.4.xlsx"
);
const DEFAULT_ROW_CLEAN_OUTPUT = path.join(
  __dirname,
  "output",
  "triumph-sheet1-patch-row-clean-v0.xlsx"
);
const DEFAULT_FEEDBACK_OUTPUT = path.join(
  __dirname,
  "output",
  "triumph-sheet1-patch-feedback-v0.1.xlsx"
);
const DEFAULT_TEMPLATE = path.resolve(
  __dirname,
  "../../assets/direct-commander-template/triumph-manipulator-commander-template-v1.xlsx"
);
const DEFAULT_OUTPUT = path.join(__dirname, "output", "triumph-sheet1-patch-draft.xlsx");
const DEFAULT_CLEANUP_OUTPUT = path.join(
  __dirname,
  "output",
  "triumph-sheet1-patch-cleanup-draft.xlsx"
);
const SHEET_NAME = "Тексты";
const HEADER_ROW = 14;

class Sheet1PatchError extends Error {
  constructor(code, message, details = []) {
    super(message);
    this.name = "Sheet1PatchError";
    this.code = code;
    this.details = details;
  }
}

function parseCliFlags(args) {
  const flags = {
    newCampaignMode: true,
    enableCleanup: true,
    rowRemovalMode: true,
    preserveCommanderIds: false,
  };
  const positional = [];

  for (const arg of args) {
    if (arg === "--preserve-commander-ids") {
      flags.newCampaignMode = false;
      flags.preserveCommanderIds = true;
      continue;
    }
    if (arg === "--no-cleanup") {
      flags.enableCleanup = false;
      continue;
    }
    if (arg === "--no-new-campaign-mode") {
      flags.newCampaignMode = false;
      continue;
    }
    if (arg === "--no-row-removal" || arg === "--keep-template-tail") {
      flags.rowRemovalMode = false;
      continue;
    }
    positional.push(arg);
  }

  return { flags, positional };
}

function usage() {
  console.error(
    `Usage: node sheet1-patch-export.js <orca-ppc-document.json> <validation-report.json> [output.xlsx] [flags]\n\n` +
      `Flags:\n` +
      `  --preserve-commander-ids   Keep template Commander IDs (disables new-campaign mode)\n` +
      `  --no-cleanup               Skip stale-row neutralization when row removal is off\n` +
      `  --no-new-campaign-mode     Do not clear entity ID columns on exported rows\n` +
      `  --no-row-removal           Keep template tail rows (neutralize only; legacy)\n` +
      `  --keep-template-tail       Alias for --no-row-removal\n\n` +
      `Default: new-campaign mode ON, row removal ON (removes stale data rows after export block).\n` +
      `ZIP-level patch — ONLY sheet1.xml modified.\n` +
      `NOT production-safe · NOT Commander import automation · Human review required.`
  );
  process.exit(1);
}

function loadJson(filePath, label) {
  if (!fs.existsSync(filePath)) {
    throw new Sheet1PatchError("INPUT_NOT_FOUND", `${label} not found: ${filePath}`);
  }
  try {
    return JSON.parse(fs.readFileSync(filePath, "utf8"));
  } catch (err) {
    throw new Sheet1PatchError("INPUT_PARSE_ERROR", `Failed to parse ${label}: ${err.message}`);
  }
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
    throw new Sheet1PatchError(
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

/**
 * @param {object} mapped
 * @param {string} outputPath
 * @param {object} options
 */
async function runSheet1PatchExport(mapped, outputPath, options = {}) {
  const templatePath = path.resolve(options.templatePath || DEFAULT_TEMPLATE);
  const headerMapPath = options.headerMapPath;
  const skipIntegrity = options.skipIntegrity === true;
  const skipForensics = options.skipForensics === true;
  const newCampaignMode = options.newCampaignMode !== false;
  const enableCleanup = options.enableCleanup !== false;
  const rowRemovalMode = options.rowRemovalMode !== false;

  if (!fs.existsSync(templatePath)) {
    throw new Sheet1PatchError("TEMPLATE_NOT_FOUND", `Commander template not found: ${templatePath}`);
  }

  const headerMapData = loadHeaderMap(headerMapPath);
  if (!headerMapData) {
    throw new Sheet1PatchError(
      "HEADER_MAP_NOT_FOUND",
      "commander-header-map-v0.json is required for sheet1 patch export"
    );
  }

  const columns = resolveVerifiedColumns(headerMapData);
  const entityIdColumns = resolveEntityIdColumns(headerMapData);
  const writableColumns = resolveWritableCleanupColumns(headerMapData);
  const allowedColumns = buildAllowedColumnSet(columns);
  const fillRows = mapped.templateFillRows || [];
  const metadataPatches = mapped.metadataPatches || {};

  if (!fillRows.length) {
    throw new Sheet1PatchError(
      "NO_TEMPLATE_FILL_ROWS",
      "No template-fill rows produced from document — nothing to export"
    );
  }

  const sheet1Original = readZipEntryUtf8(templatePath, "xl/worksheets/sheet1.xml");
  const {
    sheetXml: patchedSheet1,
    rowsPatched,
    cellStats,
    cleanupStats,
    metadataStats,
    rowRemovalStats,
    lastExportRow,
  } = patchSheet1DataRows(sheet1Original, fillRows, columns, {
    dataStartRow: DATA_START_ROW,
    headerMapFields: headerMapData,
    newCampaignMode,
    enableCleanup,
    rowRemovalMode,
    entityIdColumns,
    writableColumns,
    metadataPatches,
    enableMetadata: true,
  });

  const zipResult = patchSheet1InWorkbook(templatePath, outputPath, patchedSheet1);
  const preserve = verifyPreservedEntries(templatePath, outputPath);

  if (!preserve.sheet1Changed) {
    throw new Sheet1PatchError(
      "SHEET1_UNCHANGED",
      "Patched workbook sheet1.xml hash matches template — patch did not apply"
    );
  }

  if (preserve.sharedStringsIntroduced) {
    throw new Sheet1PatchError(
      "SHARED_STRINGS_INTRODUCED",
      "xl/sharedStrings.xml appeared in patched workbook — forbidden for Commander template model"
    );
  }

  const preserveFailures = preserve.preservedEntries.filter((e) => !e.match);
  if (preserveFailures.length) {
    throw new Sheet1PatchError(
      "PRESERVE_ENTRY_MISMATCH",
      "One or more non-sheet1 ZIP entries differ from template after patch",
      preserveFailures.map((e) => `${e.entry}: ${e.templateBytes} vs ${e.patchedBytes} bytes`)
    );
  }

  let integrity = { ok: true, code: "INTEGRITY_SKIPPED", message: "Integrity check skipped" };
  if (!skipIntegrity) {
    const hasSplitTransport = fillRows.some((r) => r.transport_row_type);
    integrity = await runIntegrityCheck(outputPath, {
      sheetName: SHEET_NAME,
      dataStartRow: DATA_START_ROW,
      rowsWritten: fillRows.length,
      mappedColumns: allowedColumns,
      columnsByKey: columns,
      probeLogicalKeys: ["groups.group_name", "keywords.phrase", "ads.headline_1"],
      probeLogicalKeysMode: hasSplitTransport ? "any-row" : "first-row",
    });

    if (!integrity.ok) {
      try {
        fs.unlinkSync(outputPath);
      } catch {
        /* best-effort */
      }
      throw new Sheet1PatchError(
        "INTEGRITY_CHECK_FAILED",
        integrity.message,
        integrity.details || []
      );
    }
  }

  let forensics = null;
  if (!skipForensics) {
    const os = require("os");
    const tmpBase = path.join(os.tmpdir(), `orca-sheet1-patch-forensics-${process.pid}`);
    const tplExtract = path.join(tmpBase, "template");
    const outExtract = path.join(tmpBase, "patched");

    const templateIndex = buildStructureIndex(templatePath, "commander-template-v0", tplExtract);
    const patchedIndex = buildStructureIndex(outputPath, "sheet1-patch-draft", outExtract);
    const comparison = compareIndexes(templateIndex, patchedIndex);

    forensics = {
      comparison,
      templateIndexSummary: {
        zipEntryCount: templateIndex.zipEntryCount,
        sharedStrings: templateIndex.criticalParts["xl/sharedStrings.xml"]?.present,
      },
      patchedIndexSummary: {
        zipEntryCount: patchedIndex.zipEntryCount,
        sharedStrings: patchedIndex.criticalParts["xl/sharedStrings.xml"]?.present,
      },
    };

    try {
      fs.rmSync(tmpBase, { recursive: true, force: true });
    } catch {
      /* ignore */
    }
  }

  return {
    outputPath: zipResult.outputPath,
    mode: "sheet1-zip-patch",
    sheet: SHEET_NAME,
    headerRow: HEADER_ROW,
    dataStartRow: DATA_START_ROW,
    rowsWritten: fillRows.length,
    rowsPatched,
    lastExportRow,
    cellStats,
    cleanupStats,
    metadataStats,
    rowRemovalStats,
    metadataPatches,
    newCampaignMode,
    enableCleanup,
    rowRemovalMode,
    entityIdColumns,
    templateSource: templatePath,
    templateUnmodified: true,
    zipPatch: {
      sheet1EntryOnly: true,
      preserveVerification: preserve,
    },
    integrity,
    forensics,
    transportDiscipline: {
      exceljsFullRewrite: false,
      sheet1SurgicalPatch: true,
      inlineStrModelPreserved: true,
    },
    counts: mapped.counts,
  };
}

async function main() {
  const boundary = enforceLegacyBoundary({
    entryPointId: "triumph-sheet1-patch-export",
    replacementKey: "triumph-export",
    tool: "sheet1-patch-export.js",
    requestedAction: "commander_export",
    requestedStage: "SPPC-20",
    searchPpcMode: true,
    isDiagnostic: isDiagnosticContext(),
    command: `node sheet1-patch-export.js ${process.argv.slice(2).join(" ")}`,
  });
  if (!boundary.allowed) {
    emitLegacyBlock(boundary);
    process.exit(boundary.exit_code || 2);
  }

  const { resolveGuardedOutputPath } = await import(
    "../../../../../mars-search-ppc-production/runtime/src/output-path-guard.mjs"
  );

  const rawArgs = process.argv.slice(2);
  if (rawArgs.includes("-h") || rawArgs.includes("--help")) usage();

  const { flags, positional } = parseCliFlags(rawArgs);
  const docArg = positional[0];
  const reportArg = positional[1];
  const outArg = positional[2];
  if (!docArg || !reportArg) usage();

  const docPath = path.resolve(docArg);
  const reportPath = path.resolve(reportArg);
  const requestedOutput = path.resolve(outArg || DEFAULT_IMPORT_REFINED_OUTPUT);
  const guarded = resolveGuardedOutputPath(requestedOutput, {
    diagnostic: boundary.mode === "diagnostic",
  });
  if (guarded.allowed === false) {
    console.error(`\n[BLOCKED] ${guarded.message}`);
    process.exit(2);
  }
  const outputPath = guarded.path;

  try {
    const document = loadJson(docPath, "PPC document");
    const report = loadJson(reportPath, "ValidationReport");

    const precheck = runPrecheck(document, report, { reportPathProvided: true });
    if (!precheck.allowed) {
      console.error(`\n--- ${EXPORTER_LABEL} — EXPORT BLOCKED ---`);
      console.error(`Block code:  ${precheck.code}`);
      console.error(`Reason:      ${precheck.message}`);
      process.exit(1);
    }

    const mapped = mapDocument(document);
    const result = await runSheet1PatchExport(mapped, outputPath, {
      newCampaignMode: flags.newCampaignMode,
      enableCleanup: flags.enableCleanup,
      rowRemovalMode: flags.rowRemovalMode,
    });

    console.log(`\n--- ${EXPORTER_LABEL} — SUCCESS ---`);
    console.log(`Document:  ${docPath}`);
    console.log(`Report:    ${reportPath}`);
    console.log(`Output:    ${result.outputPath}`);
    console.log(`Mode:      ${result.mode}`);
    console.log(`Rows patched (sheet1.xml): ${result.rowsPatched}`);
    console.log(`New campaign mode: ${result.newCampaignMode}`);
    console.log(`Row removal mode: ${result.rowRemovalMode}`);
    console.log(`Stale-row neutralization: ${result.enableCleanup && !result.rowRemovalMode}`);
    if (result.lastExportRow) {
      console.log(`Last export row: ${result.lastExportRow}`);
    }
    if (result.metadataStats?.patchedKeys?.length) {
      console.log(`Metadata patched: ${result.metadataStats.patchedKeys.join(", ")}`);
    }
    if (result.cleanupStats) {
      const cs = result.cleanupStats;
      console.log(`Entity ID columns cleared (exported rows): ${cs.idCellsCleared} cells / ${cs.rowsIdCleared} rows`);
      if (result.rowRemovalMode) {
        console.log(
          `Stale rows removed: ${cs.rowsRemoved} (rows ${cs.firstStaleRow || "?"}–${cs.removedRowNumbers?.length ? Math.max(...cs.removedRowNumbers) : "?"})`
        );
        if (cs.dimension?.updated) {
          console.log(`Dimension: ${cs.dimension.dimensionBefore} → ${cs.dimension.dimensionAfter}`);
        } else if (cs.dimension?.safeUnknown) {
          console.log(`Dimension: unchanged (${cs.dimension.reason || "SAFE UNKNOWN"})`);
        }
        console.log(`Sheet1 rows after removal: ${cs.maxRowAfter} (max)`);
      } else if (cs.rowsNeutralized) {
        console.log(
          `Stale rows neutralized: ${cs.rowsNeutralized} (from row ${cs.firstStaleRow}, masked cells: ${cs.cellsMaskedOnStaleRows || 0})`
        );
      }
      if (result.cellStats?.autotargetSuppressed) {
        console.log(`Autotarget phrases suppressed: ${result.cellStats.autotargetSuppressed}`);
      }
    }
    console.log(`Template source unmodified: ${result.templateUnmodified}`);

    const pv = result.zipPatch.preserveVerification;
    console.log(`ZIP preserve check: ${pv.ok ? "PASS" : "FAIL"}`);
    console.log(`  sheet1 changed: ${pv.sheet1Changed}`);
    console.log(`  sharedStrings introduced: ${pv.sharedStringsIntroduced}`);
    for (const e of pv.preservedEntries) {
      console.log(`  ${e.entry}: ${e.match ? "byte-identical" : "MISMATCH"}`);
    }

    if (result.integrity) {
      console.log(`Integrity: ${result.integrity.code} — ${result.integrity.message}`);
    }

    if (result.forensics?.comparison) {
      const c = result.forensics.comparison;
      console.log(`OOXML forensics: sharedStrings added = ${c.sharedStringsAdded}`);
      console.log(`  onlyInGenerated entries: ${(c.onlyInGenerated || []).join(", ") || "(none)"}`);
      for (const w of (c.worksheetComparison || []).slice(0, 3)) {
        if (w.path.includes("sheet2") || w.path.includes("sheet3")) {
          console.log(
            `  ${w.path}: cells ${w.cellCountTemplate} → ${w.cellCountGenerated} (Δ ${w.cellCountDelta})`
          );
        }
      }
    }

    console.log(
      "\nNOT production-safe · NOT guaranteed Commander import · Human review required."
    );
  } catch (err) {
    if (
      err instanceof Sheet1PatchError ||
      err instanceof Sheet1XmlError ||
      err instanceof ZipPatchError
    ) {
      console.error(`\n--- ${EXPORTER_LABEL} — BLOCKED ---`);
      console.error(`Block code:  ${err.code}`);
      console.error(`Reason:      ${err.message}`);
      if (err.details?.length) {
        for (const d of err.details) console.error(`  - ${d}`);
      }
      process.exit(1);
    }
    console.error(`\n[BLOCKED] Unexpected error: ${err.message}`);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  runSheet1PatchExport,
  Sheet1PatchError,
  DEFAULT_OUTPUT,
  DEFAULT_CLEANUP_OUTPUT,
  DEFAULT_FEEDBACK_OUTPUT,
  DEFAULT_ROW_CLEAN_OUTPUT,
  DEFAULT_IMPORT_REFINED_OUTPUT,
  DEFAULT_TEMPLATE,
  ENTITY_ID_LOGICAL_KEYS,
};
