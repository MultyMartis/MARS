"use strict";

const fs = require("fs");
const path = require("path");
const Ajv2020 = require("ajv/dist/2020");
const addFormats = require("ajv-formats");

const PACK_ROOT = path.resolve(__dirname, "..", "..");

const REPORT_SCHEMA_PATH = path.join(
  PACK_ROOT,
  "schema",
  "json",
  "validation-report-v1.schema.json"
);

let compiledValidate = null;

function getValidator() {
  if (!compiledValidate) {
    const schema = JSON.parse(fs.readFileSync(REPORT_SCHEMA_PATH, "utf8"));
    const ajv = new Ajv2020({ allErrors: true, strict: false });
    addFormats(ajv);
    compiledValidate = ajv.compile(schema);
  }
  return compiledValidate;
}

function formatAjvErrors(errors) {
  return (errors || []).map((e) => {
    const p = e.instancePath || "/";
    return `${p} ${e.message}`.trim();
  });
}

function validateReportSchema(report) {
  const validate = getValidator();
  const valid = validate(report);
  return {
    valid,
    errors: valid ? [] : formatAjvErrors(validate.errors),
  };
}

module.exports = {
  validateReportSchema,
  REPORT_SCHEMA_PATH,
};
