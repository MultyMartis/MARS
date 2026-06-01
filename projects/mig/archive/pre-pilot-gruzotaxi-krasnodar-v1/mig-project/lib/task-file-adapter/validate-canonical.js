"use strict";

const { SUPPORTED_V0_TYPES } = require("./normalize-request");

const REQUEST_ID_RE = /^[a-zA-Z0-9][a-zA-Z0-9_-]{0,127}$/;

function validateCanonicalRequest(request) {
  const errors = [];

  if (request.schema_version !== "0") {
    errors.push('schema_version must be "0"');
  }

  if (!request.request_id || !REQUEST_ID_RE.test(request.request_id)) {
    errors.push("request_id is required (max 128 chars, alphanumeric start)");
  }

  if (!request.request_type || !SUPPORTED_V0_TYPES.has(request.request_type)) {
    errors.push(
      `request_type must be one of v0.1 supported types: ${[...SUPPORTED_V0_TYPES].join(", ")}`
    );
  }

  const scope = request.scope || {};
  for (const field of ["niche", "region", "business_type", "search_engine", "device"]) {
    const value = scope[field];
    if (value === undefined || value === null || String(value).trim() === "") {
      errors.push(`scope.${field} is required`);
    }
  }

  const seeds = request.queries && request.queries.seed_queries;
  if (!Array.isArray(seeds) || seeds.length === 0) {
    errors.push("queries.seed_queries must be a non-empty array");
  }

  if (!request.operator_id || String(request.operator_id).trim() === "") {
    errors.push("operator_id is required");
  }

  if (!request.created_at) {
    errors.push("created_at is required");
  }

  const source = request.source || {};
  if (source.adapter !== "task_file") {
    errors.push('source.adapter must be "task_file" after normalization');
  }
  if (!source.adapter_version) {
    errors.push("source.adapter_version is required");
  }

  if (request.session_id) {
    errors.push("session_id must not be set before adapter processing (v0.1)");
  }

  if (errors.length > 0) {
    const err = new Error(errors.join("; "));
    err.code = "VALIDATION_ERROR";
    err.details = errors;
    throw err;
  }

  return { status: "validated", request };
}

module.exports = {
  REQUEST_ID_RE,
  validateCanonicalRequest,
};
