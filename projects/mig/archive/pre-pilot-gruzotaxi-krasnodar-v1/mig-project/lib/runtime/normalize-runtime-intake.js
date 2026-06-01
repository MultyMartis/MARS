"use strict";

const crypto = require("crypto");
const { validateIntake, generateSessionId } = require("../session-spine/validate-intake");
const {
  isCanonicalShape,
  isLegacyFlatShape,
  canonicalToSpineFlat,
} = require("../task-file-adapter/normalize-request");

const SESSION_ID_PATTERN = /^mig-[0-9]{8}-[a-f0-9]{6}$/;

function pickSessionId(body, options = {}) {
  const candidate = options.session_id || body.session_id;
  if (candidate && SESSION_ID_PATTERN.test(String(candidate))) {
    return String(candidate);
  }
  return generateSessionId();
}

function canonicalToRuntimeIntake(request, options = {}) {
  const sessionId = pickSessionId(request, options);
  const queryUsed = String(request.queries.seed_queries[0]).trim();
  const createdAt = request.created_at || new Date().toISOString();

  return {
    session_id: sessionId,
    request_id: request.request_id || `req-${sessionId.slice(4)}`,
    request_type: request.request_type || "serp_capture",
    created_at: createdAt,
    capture_profile: request.capture_profile || null,
    runtime_profile: request.request_type || "serp_capture",
    intake: {
      niche: request.scope.niche,
      region: request.scope.region,
      city: request.scope.city || null,
      business_type: request.scope.business_type,
      seed_queries: request.queries.seed_queries,
      search_engine: request.scope.search_engine,
      device: request.scope.device,
      operator_id: request.operator_id,
    },
    query_used: queryUsed,
    manual_serp: request.manual_serp || null,
    serp_provider_response: request.provider_response || request.serp_provider_response || null,
    signals: request.signals || null,
    strict: Boolean(request.strict),
    source: request.source || null,
  };
}

/**
 * Normalize Research Request (canonical or legacy flat) for runtime execution.
 */
function normalizeRuntimeIntake(body, options = {}) {
  if (!body || typeof body !== "object") {
    const err = new Error("Runtime intake must be a JSON object");
    err.code = "INTAKE_INVALID";
    throw err;
  }

  if (isCanonicalShape(body)) {
    if (!body.operator_id || !body.queries?.seed_queries?.length) {
      const err = new Error("Canonical Research Request missing operator_id or seed_queries");
      err.code = "INTAKE_INVALID";
      throw err;
    }
    return canonicalToRuntimeIntake(body, options);
  }

  if (isLegacyFlatShape(body)) {
    const validated = validateIntake(body);
    return {
      session_id: pickSessionId(body, options),
      request_id: body.request_id || `req-${pickSessionId(body, options).slice(4)}`,
      request_type: body.request_type || "serp_capture",
      created_at: validated.created_at,
      capture_profile: body.capture_profile || null,
      runtime_profile: body.request_type || "serp_capture",
      intake: validated.intake,
      query_used: validated.query_used,
      manual_serp: validated.manual_serp,
      serp_provider_response: validated.serp_provider_response,
      signals: body.signals || null,
      strict: Boolean(body.strict),
      source: body.source || { adapter: "cli", adapter_version: "0.1" },
    };
  }

  const err = new Error(
    "Unrecognized runtime intake — use canonical Research Request or legacy flat spine map"
  );
  err.code = "INTAKE_INVALID";
  throw err;
}

module.exports = {
  normalizeRuntimeIntake,
  canonicalToRuntimeIntake,
  pickSessionId,
};
