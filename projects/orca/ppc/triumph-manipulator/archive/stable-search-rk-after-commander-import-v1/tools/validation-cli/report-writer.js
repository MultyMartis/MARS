"use strict";

const fs = require("fs");
const path = require("path");

function compareStrings(a, b) {
  const sa = a == null ? "" : String(a);
  const sb = b == null ? "" : String(b);
  return sa.localeCompare(sb, "en");
}

function compareEntityRef(a, b) {
  const ak = a?.entity_kind ?? "";
  const bk = b?.entity_kind ?? "";
  const ck = compareStrings(ak, bk);
  if (ck !== 0) return ck;
  return compareStrings(a?.entity_id, b?.entity_id);
}

function sortRuleResults(results) {
  return [...results].sort((a, b) => {
    const r = compareStrings(a.rule_id, b.rule_id);
    if (r !== 0) return r;
    const e = compareEntityRef(a.entity_ref, b.entity_ref);
    if (e !== 0) return e;
    const fp = compareStrings(a.entity_ref?.field_path, b.entity_ref?.field_path);
    if (fp !== 0) return fp;
    return compareStrings(a.message, b.message);
  });
}

function sortFindings(findings) {
  return [...findings].sort((a, b) => {
    const r = compareStrings(a.rule_id, b.rule_id);
    if (r !== 0) return r;
    const e = compareEntityRef(a.entity_ref, b.entity_ref);
    if (e !== 0) return e;
    return compareStrings(a.message, b.message);
  });
}

function sortEntityResults(entities) {
  return [...entities]
    .map((e) => ({
      ...e,
      rule_ids: [...new Set(e.rule_ids || [])].sort(compareStrings),
    }))
    .sort((a, b) => {
      const k = compareStrings(a.entity_kind, b.entity_kind);
      if (k !== 0) return k;
      return compareStrings(a.entity_id, b.entity_id);
    });
}

/**
 * Stable ordering for regression diffs and golden fixture comparison.
 */
function finalizeReport(report) {
  const next = { ...report };
  next.rule_results = sortRuleResults(next.rule_results || []);
  next.blocking_errors = sortFindings(next.blocking_errors || []);
  next.warnings = sortFindings(next.warnings || []);
  next.entity_results = sortEntityResults(next.entity_results || []);
  next.safe_unknown = sortFindings(next.safe_unknown || []);
  return next;
}

/**
 * Fields that change every run — exclude when diffing against golden fixture.
 */
function stripVolatileReportFields(report) {
  const copy = JSON.parse(JSON.stringify(report));
  delete copy.validation_timestamp;
  if (copy.meta) {
    delete copy.meta.validation_run_id;
  }
  return copy;
}

/**
 * Writes validation-report.output.json to tools/validation-cli/output/
 */
function writeReport(report, options = {}) {
  const outputDir = options.outputDir || path.join(__dirname, "output");
  if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
  }

  const toWrite = options.finalize !== false ? finalizeReport(report) : report;
  const outputPath = path.join(outputDir, "validation-report.output.json");
  fs.writeFileSync(outputPath, JSON.stringify(toWrite, null, 2), "utf8");

  return outputPath;
}

module.exports = {
  writeReport,
  finalizeReport,
  stripVolatileReportFields,
  sortRuleResults,
  sortFindings,
};
