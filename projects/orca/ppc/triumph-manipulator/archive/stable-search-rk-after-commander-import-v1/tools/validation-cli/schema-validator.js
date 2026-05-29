"use strict";

const fs = require("fs");
const path = require("path");
const Ajv2020 = require("ajv/dist/2020");
const addFormats = require("ajv-formats");

const PACK_ROOT = path.resolve(__dirname, "..", "..");

const SCHEMA_PATHS = {
  document: path.join(
    PACK_ROOT,
    "schema",
    "json",
    "orca-ppc-document-v1.schema.json"
  ),
  report: path.join(
    PACK_ROOT,
    "schema",
    "json",
    "validation-report-v1.schema.json"
  ),
};

const schemaCache = new Map();

function loadSchema(kind) {
  if (!schemaCache.has(kind)) {
    schemaCache.set(kind, JSON.parse(fs.readFileSync(SCHEMA_PATHS[kind], "utf8")));
  }
  return schemaCache.get(kind);
}

function formatAjvErrors(errors) {
  return (errors || []).map((e) => {
    const p = e.instancePath || "/";
    return `${p} ${e.message}`.trim();
  });
}

function validateAgainstSchema(kind, data) {
  const schema = loadSchema(kind);
  const ajv = new Ajv2020({ allErrors: true, strict: false });
  addFormats(ajv);
  const validate = ajv.compile(schema);
  const valid = validate(data);
  return {
    valid,
    errors: valid ? [] : formatAjvErrors(validate.errors),
  };
}

function validateDocument(doc) {
  return validateAgainstSchema("document", doc);
}

function validateReport(report) {
  return validateAgainstSchema("report", report);
}

module.exports = {
  validateDocument,
  validateReport,
  SCHEMA_PATHS,
};
