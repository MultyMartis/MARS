"use strict";

const { validateReportSchema } = require("./report-validator");

const SUPPORTED_REPORT_SCHEMA = "v1";
const SUPPORTED_DOCUMENT_SCHEMA = "v1";

const BLOCK = {
  MISSING_VALIDATION_REPORT: "MISSING_VALIDATION_REPORT",
  EXPORT_NOT_ALLOWED: "EXPORT_NOT_ALLOWED",
  BLOCKING_ERRORS_PRESENT: "BLOCKING_ERRORS_PRESENT",
  VALIDATION_FAILED: "VALIDATION_FAILED",
  UNSUPPORTED_SCHEMA_VERSION: "UNSUPPORTED_SCHEMA_VERSION",
  NON_SEARCH_SCOPE: "NON_SEARCH_SCOPE",
  INVALID_REPORT_SCHEMA: "INVALID_REPORT_SCHEMA",
  DOCUMENT_ID_MISMATCH: "DOCUMENT_ID_MISMATCH",
  INVALID_DOCUMENT: "INVALID_DOCUMENT",
  UNSUPPORTED_CAMPAIGN_TYPE: "UNSUPPORTED_CAMPAIGN_TYPE",
};

function fail(code, message, details = []) {
  return { allowed: false, code, message, details, blockCodes: [code] };
}

function compareId(report, document) {
  const docId = document.project_id;
  const validatedId = report.validated_document_id;
  if (docId && validatedId && docId !== validatedId) {
    return fail(
      BLOCK.DOCUMENT_ID_MISMATCH,
      `ValidationReport validated_document_id "${validatedId}" does not match document project_id "${docId}".`,
      [`expected: ${docId}`, `report: ${validatedId}`]
    );
  }
  return null;
}

function checkDocumentStructure(document) {
  if (!document || typeof document !== "object") {
    return fail(BLOCK.INVALID_DOCUMENT, "PPC document is missing or not a JSON object.");
  }
  if (document.schema_version !== SUPPORTED_DOCUMENT_SCHEMA) {
    return fail(
      BLOCK.UNSUPPORTED_SCHEMA_VERSION,
      `Unsupported document schema_version "${document.schema_version}". Supported: ${SUPPORTED_DOCUMENT_SCHEMA}.`
    );
  }
  if (document.search_only_scope !== true) {
    return fail(
      BLOCK.NON_SEARCH_SCOPE,
      "Document search_only_scope must be true (search-only pack)."
    );
  }
  const campaigns = document.campaigns || [];
  for (const camp of campaigns) {
    if (camp.search_only_scope !== true) {
      return fail(
        BLOCK.NON_SEARCH_SCOPE,
        `Campaign "${camp.campaign_id || camp.campaign_name}" has search_only_scope !== true.`
      );
    }
    if (camp.campaign_type && camp.campaign_type !== "search") {
      return fail(
        BLOCK.UNSUPPORTED_CAMPAIGN_TYPE,
        `Campaign "${camp.campaign_id}" campaign_type "${camp.campaign_type}" is not supported (search only).`
      );
    }
  }
  if (!campaigns.length) {
    return fail(BLOCK.INVALID_DOCUMENT, "Document has no campaigns to export.");
  }
  return null;
}

/**
 * Fail-closed export gate. report may be null when file missing (handled by caller).
 */
function runPrecheck(document, report, options = {}) {
  const { reportPathProvided = true } = options;

  if (!reportPathProvided || report == null) {
    return fail(
      BLOCK.MISSING_VALIDATION_REPORT,
      "ValidationReport is required. Run validation-cli first and pass the report JSON path."
    );
  }

  const schemaResult = validateReportSchema(report);
  if (!schemaResult.valid) {
    return {
      allowed: false,
      code: BLOCK.INVALID_REPORT_SCHEMA,
      message:
        "ValidationReport failed schema validation (validation-report-v1.schema.json). Export blocked.",
      details: schemaResult.errors.slice(0, 10),
      blockCodes: [BLOCK.INVALID_REPORT_SCHEMA],
    };
  }

  if (report.schema_version !== SUPPORTED_REPORT_SCHEMA) {
    return fail(
      BLOCK.UNSUPPORTED_SCHEMA_VERSION,
      `Unsupported ValidationReport schema_version "${report.schema_version}". Supported: ${SUPPORTED_REPORT_SCHEMA}.`
    );
  }

  const docStruct = checkDocumentStructure(document);
  if (docStruct) return docStruct;

  const idMismatch = compareId(report, document);
  if (idMismatch) return idMismatch;

  if (Array.isArray(report.blocking_errors) && report.blocking_errors.length > 0) {
    const preview = report.blocking_errors
      .slice(0, 5)
      .map((e) => `[${e.rule_id}] ${e.message}`);
    return {
      allowed: false,
      code: BLOCK.BLOCKING_ERRORS_PRESENT,
      message: `ValidationReport has ${report.blocking_errors.length} blocking error(s). Export blocked.`,
      details: preview,
      blockCodes: [BLOCK.BLOCKING_ERRORS_PRESENT],
    };
  }

  if (report.export_allowed !== true) {
    return fail(
      BLOCK.EXPORT_NOT_ALLOWED,
      "export_allowed is not true. Fix validation findings and re-run validator."
    );
  }

  if (
    report.validation_status === "failed" ||
    report.validation_status === "incomplete"
  ) {
    return fail(
      BLOCK.VALIDATION_FAILED,
      `validation_status is "${report.validation_status}". Re-validate after fixes.`
    );
  }

  return {
    allowed: true,
    code: null,
    message: "Precheck passed — export may proceed (transport draft only).",
    details: [],
    blockCodes: [],
  };
}

module.exports = {
  runPrecheck,
  BLOCK,
  SUPPORTED_REPORT_SCHEMA,
  SUPPORTED_DOCUMENT_SCHEMA,
};
