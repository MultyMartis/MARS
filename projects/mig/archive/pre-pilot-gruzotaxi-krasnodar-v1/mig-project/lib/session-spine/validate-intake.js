"use strict";

const crypto = require("crypto");

const REQUIRED_FIELDS = [
  "niche",
  "region",
  "business_type",
  "seed_queries",
  "search_engine",
  "device",
  "operator_id",
];

function generateSessionId(now = new Date()) {
  const date = now.toISOString().slice(0, 10).replace(/-/g, "");
  const suffix = crypto.randomBytes(3).toString("hex");
  return `mig-${date}-${suffix}`;
}

function validateIntake(body) {
  const intake = body && typeof body === "object" ? body : {};
  const errors = [];

  for (const field of REQUIRED_FIELDS) {
    if (field === "seed_queries") {
      if (!Array.isArray(intake.seed_queries) || intake.seed_queries.length === 0) {
        errors.push("seed_queries must be a non-empty array");
      }
      continue;
    }
    const value = intake[field];
    if (value === undefined || value === null || String(value).trim() === "") {
      errors.push(`${field} is required`);
    }
  }

  if (errors.length > 0) {
    const err = new Error(errors.join("; "));
    err.code = "VALIDATION_ERROR";
    err.details = errors;
    throw err;
  }

  const sessionId = generateSessionId();
  const queryUsed = String(intake.seed_queries[0]).trim();

  return {
    session_id: sessionId,
    created_at: new Date().toISOString(),
    intake: {
      niche: String(intake.niche).trim(),
      region: String(intake.region).trim(),
      city: intake.city ? String(intake.city).trim() : null,
      business_type: String(intake.business_type).trim(),
      seed_queries: intake.seed_queries.map((q) => String(q).trim()),
      search_engine: String(intake.search_engine).trim().toLowerCase(),
      device: String(intake.device).trim().toLowerCase(),
      operator_id: String(intake.operator_id).trim(),
    },
    query_used: queryUsed,
    manual_serp: intake.manual_serp || null,
    serp_provider_response: intake.serp_provider_response || null,
  };
}

module.exports = {
  REQUIRED_FIELDS,
  generateSessionId,
  validateIntake,
};
