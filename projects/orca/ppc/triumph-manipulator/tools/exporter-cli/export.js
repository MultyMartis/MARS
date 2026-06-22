#!/usr/bin/env node
"use strict";

/**
 * ORCA Exporter Prototype v0
 * Human-triggered, single-run, local-only. NOT a service, daemon, or Direct API.
 *
 * Modes:
 *   default         — logical multi-sheet transport draft (workbook-writer.js)
 *   --template-fill — clone Commander template, write into sheet "Тексты"
 */

const fs = require("fs");
const path = require("path");

const { runPrecheck } = require("./precheck");
const { mapDocument } = require("./mapping");
const { writeWorkbook } = require("./workbook-writer");
const { writeTemplateFill, TemplateFillError } = require("./template-fill-writer");
const {
  enforceLegacyBoundary,
  emitLegacyBlock,
  isDiagnosticContext,
} = require("../../../../../mars-search-ppc-production/runtime/src/legacy-entry-boundary.cjs");

const EXPORTER_LABEL = "ORCA Exporter Prototype v0";
const DEFAULT_OUTPUT = path.join(__dirname, "output", "triumph-export-draft.xlsx");
const DEFAULT_TEMPLATE_FILL_OUTPUT = path.join(
  __dirname,
  "output",
  "triumph-commander-template-fill-draft.xlsx"
);

function usage() {
  console.error(
    `Usage: node export.js <orca-ppc-document.json> <validation-report.json> [options] [output.xlsx]\n\n` +
      `Options:\n` +
      `  --template-fill    Clone Commander template and write into sheet "Тексты"\n` +
      `  --logical          Logical multi-sheet draft (default)\n\n` +
      `Examples:\n` +
      `  node export.js ../../schema/instances/triumph-s-tier-draft-v1.json \\\n` +
      `    fixtures/validation-report.export-allowed.fixture.json\n\n` +
      `  node export.js ../../schema/instances/triumph-s-tier-draft-v1.json \\\n` +
      `    fixtures/validation-report.export-allowed.fixture.json --template-fill\n\n` +
      `Exit 0: precheck passed, XLSX written\n` +
      `Exit 1: export blocked (fail-closed)\n\n` +
      `NOT production exporter · NOT Direct API · NOT autonomous export`
  );
  process.exit(1);
}

function loadJson(filePath, label) {
  if (!fs.existsSync(filePath)) {
    console.error(`\n[BLOCKED] ${label} not found: ${filePath}`);
    process.exit(1);
  }
  try {
    const raw = fs.readFileSync(filePath, "utf8");
    return JSON.parse(raw);
  } catch (err) {
    console.error(`\n[BLOCKED] Failed to parse ${label}: ${err.message}`);
    process.exit(1);
  }
}

function printBlocked(result) {
  console.error(`\n--- ${EXPORTER_LABEL} — EXPORT BLOCKED ---`);
  console.error(`Block code:  ${result.code}`);
  console.error(`Reason:      ${result.message}`);
  if (result.details && result.details.length) {
    console.error("Details:");
    for (const d of result.details) {
      console.error(`  - ${d}`);
    }
  }
  console.error(
    "\nOperator: fix validation findings → re-run validation-cli → retry export."
  );
}

function printTemplateFillBlocked(err) {
  console.error(`\n--- ${EXPORTER_LABEL} — TEMPLATE-FILL BLOCKED ---`);
  console.error(`Block code:  ${err.code}`);
  console.error(`Reason:      ${err.message}`);
  if (err.details && err.details.length) {
    console.error("Details:");
    for (const d of err.details) {
      console.error(`  - ${d}`);
    }
  }
}

function parseArgs(argv) {
  const positional = [];
  let templateFill = false;
  let logical = false;

  for (const arg of argv) {
    if (arg === "--template-fill") {
      templateFill = true;
    } else if (arg === "--logical") {
      logical = true;
    } else if (arg.startsWith("-")) {
      console.error(`Unknown option: ${arg}`);
      usage();
    } else {
      positional.push(arg);
    }
  }

  if (templateFill && logical) {
    console.error("Use only one of --template-fill or --logical.");
    usage();
  }

  return {
    docArg: positional[0],
    reportArg: positional[1],
    outArg: positional[2],
    templateFill,
  };
}

async function main() {
  const boundary = enforceLegacyBoundary({
    entryPointId: "triumph-export",
    replacementKey: "triumph-export",
    tool: "export.js",
    requestedAction: "commander_export",
    requestedStage: "SPPC-20",
    searchPpcMode: true,
    isDiagnostic: isDiagnosticContext(),
    command: `node export.js ${process.argv.slice(2).join(" ")}`,
  });
  if (!boundary.allowed) {
    emitLegacyBlock(boundary);
    process.exit(boundary.exit_code || 2);
  }

  const { resolveGuardedOutputPath } = await import(
    "../../../../../mars-search-ppc-production/runtime/src/output-path-guard.mjs"
  );

  const { docArg, reportArg, outArg, templateFill } = parseArgs(
    process.argv.slice(2)
  );

  if (!docArg || !reportArg) usage();

  const docPath = path.resolve(docArg);
  const reportPath = path.resolve(reportArg);
  const defaultOut = templateFill ? DEFAULT_TEMPLATE_FILL_OUTPUT : DEFAULT_OUTPUT;
  const requestedOutput = path.resolve(outArg || defaultOut);
  const guarded = resolveGuardedOutputPath(requestedOutput, {
    diagnostic: boundary.mode === "diagnostic",
  });
  if (guarded.allowed === false) {
    console.error(`\n[BLOCKED] ${guarded.message}`);
    process.exit(2);
  }
  const outputPath = guarded.path;

  const document = loadJson(docPath, "PPC document");
  const report = loadJson(reportPath, "ValidationReport");

  const precheck = runPrecheck(document, report, { reportPathProvided: true });
  if (!precheck.allowed) {
    printBlocked(precheck);
    process.exit(1);
  }

  const mapped = mapDocument(document);

  let result;
  try {
    if (templateFill) {
      result = await writeTemplateFill(mapped, outputPath);
    } else {
      result = await writeWorkbook(mapped, outputPath);
    }
  } catch (err) {
    if (err instanceof TemplateFillError) {
      printTemplateFillBlocked(err);
      process.exit(1);
    }
    throw err;
  }

  const modeLabel = templateFill
    ? "SUCCESS (template-fill draft)"
    : "SUCCESS (logical transport draft)";

  console.log(`\n--- ${EXPORTER_LABEL} — ${modeLabel} ---`);
  console.log(`Document:  ${docPath}`);
  console.log(`Report:    ${reportPath}`);
  console.log(`Output:    ${result.outputPath}`);
  console.log(`Mode:      ${result.mode || "logical"}`);

  if (templateFill) {
    console.log(`Sheet:     ${result.sheet} (header row ${result.headerRow})`);
    console.log(`Rows written: ${result.rowsWritten}`);
    console.log(`Template source unmodified: ${result.templateUnmodified}`);
    console.log(
      `Extension join delimiter: "${result.extensionJoinDelimiter}" (fastlinks/callouts)`
    );
    if (result.integrity) {
      console.log(`Integrity:   ${result.integrity.code} — ${result.integrity.message}`);
      if (result.integrity.stats) {
        console.log(
          `  Reopen: ${result.integrity.stats.sheetCount} sheets, ${result.integrity.stats.dataRowsWithCells} data rows verified`
        );
      }
    }
    if (result.writeDiscipline) {
      console.log(
        `Write discipline: exact cells only (row ${result.dataStartRow}+), no range clear`
      );
    }
  } else {
    console.log("Row counts:");
    console.log(`  campaigns:  ${result.counts.campaigns}`);
    console.log(`  groups:     ${result.counts.groups}`);
    console.log(`  keywords:   ${result.counts.keywords}`);
    console.log(`  ads:        ${result.counts.ads}`);
    console.log(`  extensions: ${result.counts.extensions}`);
  }

  console.log(
    "\nNOT production-safe · NOT guaranteed Commander import · Human review required."
  );
}

main().catch((err) => {
  console.error(`\n[BLOCKED] Unexpected error: ${err.message}`);
  process.exit(1);
});
