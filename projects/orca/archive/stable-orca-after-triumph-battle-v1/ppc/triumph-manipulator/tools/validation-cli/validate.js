#!/usr/bin/env node
"use strict";

/**
 * ORCA Validation CLI Hardening v0.1
 * Human-triggered, single-run, local-only. NOT a service or daemon.
 */

const fs = require("fs");
const path = require("path");

const { validateDocument, validateReport } = require("./schema-validator");
const {
  executeRules,
  buildReport,
  applyReportSchemaFailure,
  markReportSchemaValid,
} = require("./rules");
const { writeReport, finalizeReport } = require("./report-writer");

const VALIDATOR_LABEL = "ORCA Validation CLI Hardening v0.1";

function usage() {
  console.error(
    "Usage: node validate.js <path-to-orca-ppc-document.json>\n" +
      "Example: node validate.js ../../schema/instances/triumph-s-tier-draft-v1.json\n\n" +
      "Exit 0: export_allowed true (no blocking errors, valid input + output schema)\n" +
      "Exit 1: blocking errors, input schema failure, or invalid ValidationReport\n\n" +
      "Optional: ORCA_VALIDATOR_FIXED_TIMESTAMP=ISO-8601 for deterministic golden fixtures"
  );
  process.exit(1);
}

function loadJson(filePath) {
  const raw = fs.readFileSync(filePath, "utf8");
  return JSON.parse(raw);
}

function printSummary(report, reportSchemaValid) {
  console.log(`\n--- ${VALIDATOR_LABEL} ---`);
  console.log(`Project:      ${report.project_id}`);
  console.log(`Status:       ${report.validation_status}`);
  console.log(`Export OK:    ${report.export_allowed}`);
  console.log(`Report schema: ${reportSchemaValid ? "valid" : "INVALID"}`);
  console.log(`Human review: ${report.human_review_required}`);
  console.log(
    `Launch:       NOT SET (human-only; export_allowed ≠ launch approval)`
  );
  console.log(
    `Summary:      ${report.summary.passed} pass, ${report.summary.warned} warn, ${report.summary.failed} fail`
  );

  if (report.blocking_errors.length) {
    console.log("\nBlocking errors:");
    for (const e of report.blocking_errors.slice(0, 15)) {
      console.log(`  [${e.rule_id}] ${e.message}`);
    }
    if (report.blocking_errors.length > 15) {
      console.log(`  ... and ${report.blocking_errors.length - 15} more`);
    }
  }

  if (report.warnings.length) {
    console.log("\nWarnings:");
    for (const w of report.warnings.slice(0, 15)) {
      console.log(`  [${w.rule_id}] ${w.message}`);
    }
    if (report.warnings.length > 15) {
      console.log(`  ... and ${report.warnings.length - 15} more`);
    }
  }
}

function computeExitCode(report) {
  return report.export_allowed === true ? 0 : 1;
}

function main() {
  const inputArg = process.argv[2];
  if (!inputArg) usage();

  const inputPath = path.resolve(process.cwd(), inputArg);
  if (!fs.existsSync(inputPath)) {
    console.error(`File not found: ${inputPath}`);
    process.exit(1);
  }

  let doc;
  try {
    doc = loadJson(inputPath);
  } catch (err) {
    console.error(`Invalid JSON: ${err.message}`);
    process.exit(1);
  }

  const { valid: inputSchemaValid, errors: inputSchemaErrors } =
    validateDocument(doc);
  const ruleResults = executeRules(doc);
  let report = finalizeReport(
    buildReport(doc, ruleResults, inputSchemaValid, inputSchemaErrors)
  );

  let reportSchemaCheck = validateReport(report);
  if (reportSchemaCheck.valid) {
    report = finalizeReport(markReportSchemaValid(report));
  } else {
    console.error("\nValidationReport schema INVALID (fail-closed):");
    for (const err of reportSchemaCheck.errors.slice(0, 10)) {
      console.error(`  ${err}`);
    }
    if (reportSchemaCheck.errors.length > 10) {
      console.error(
        `  ... and ${reportSchemaCheck.errors.length - 10} more`
      );
    }
    report = finalizeReport(
      applyReportSchemaFailure(report, reportSchemaCheck.errors)
    );
    reportSchemaCheck = validateReport(report);
  }

  const outputPath = writeReport(report, { finalize: false });
  printSummary(report, reportSchemaCheck.valid);
  console.log(`\nReport written: ${outputPath}`);

  process.exit(computeExitCode(report));
}

main();
