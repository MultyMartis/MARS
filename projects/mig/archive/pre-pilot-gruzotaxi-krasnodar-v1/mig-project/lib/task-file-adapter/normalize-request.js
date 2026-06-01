"use strict";

const crypto = require("crypto");

const ADAPTER_VERSION = "0.1";
const SUPPORTED_V0_TYPES = new Set(["serp_capture"]);

function generateRequestId(now = new Date()) {
  const date = now.toISOString().slice(0, 10).replace(/-/g, "");
  const suffix = crypto.randomBytes(3).toString("hex");
  return `req-${date}-${suffix}`;
}

function isCanonicalShape(raw) {
  return (
    raw &&
    typeof raw === "object" &&
    raw.schema_version === "0" &&
    raw.scope &&
    typeof raw.scope === "object" &&
    raw.queries &&
    Array.isArray(raw.queries.seed_queries)
  );
}

function isLegacyFlatShape(raw) {
  return raw && typeof raw === "object" && Array.isArray(raw.seed_queries) && raw.niche;
}

function legacyToCanonical(raw, transportRef) {
  const now = new Date();
  return {
    schema_version: "0",
    request_id: raw.request_id || generateRequestId(now),
    request_type: raw.request_type || "serp_capture",
    scope: {
      niche: String(raw.niche).trim(),
      region: String(raw.region).trim(),
      city: raw.city ? String(raw.city).trim() : null,
      business_type: String(raw.business_type || "local_service").trim(),
      search_engine: String(raw.search_engine).trim().toLowerCase(),
      device: String(raw.device).trim().toLowerCase(),
    },
    queries: {
      seed_queries: raw.seed_queries.map((q) => String(q).trim()).filter(Boolean),
    },
    operator_id: String(raw.operator_id).trim(),
    created_at: raw.created_at || now.toISOString(),
    source: {
      adapter: "task_file",
      adapter_version: ADAPTER_VERSION,
      transport_ref: transportRef,
    },
    manual_serp: raw.manual_serp || null,
    provider_response: raw.provider_response || raw.serp_provider_response || null,
    priority: raw.priority || "normal",
    strict: Boolean(raw.strict),
    downstream_context: raw.downstream_context || null,
    status: "submitted",
  };
}

function enrichCanonical(raw, transportRef) {
  const now = new Date();
  const request = { ...raw };
  request.schema_version = "0";
  request.request_id = request.request_id || generateRequestId(now);
  request.request_type = request.request_type || "serp_capture";
  request.created_at = request.created_at || now.toISOString();
  request.operator_id = String(request.operator_id).trim();
  request.scope = {
    ...request.scope,
    business_type: String(request.scope.business_type || "local_service").trim(),
    search_engine: String(request.scope.search_engine).trim().toLowerCase(),
    device: String(request.scope.device).trim().toLowerCase(),
    niche: String(request.scope.niche).trim(),
    region: String(request.scope.region).trim(),
    city: request.scope.city ? String(request.scope.city).trim() : null,
  };
  request.queries = {
    seed_queries: request.queries.seed_queries.map((q) => String(q).trim()).filter(Boolean),
  };
  request.source = {
    adapter: "task_file",
    adapter_version: ADAPTER_VERSION,
    transport_ref: transportRef,
    ...(raw.source && typeof raw.source === "object" ? raw.source : {}),
  };
  request.source.adapter = "task_file";
  request.source.adapter_version = ADAPTER_VERSION;
  if (!request.source.transport_ref) {
    request.source.transport_ref = transportRef;
  }
  request.status = "submitted";
  if (request.provider_response === undefined && request.serp_provider_response) {
    request.provider_response = request.serp_provider_response;
  }
  return request;
}

function normalizeFromFile(raw, transportRef) {
  if (!raw || typeof raw !== "object") {
    const err = new Error("Request file must contain a JSON object");
    err.code = "INVALID_JSON_SHAPE";
    throw err;
  }

  if (isCanonicalShape(raw)) {
    return enrichCanonical(raw, transportRef);
  }
  if (isLegacyFlatShape(raw)) {
    return legacyToCanonical(raw, transportRef);
  }

  const err = new Error(
    "Unrecognized request shape — use canonical Research Request (schema_version 0) or legacy flat intake"
  );
  err.code = "UNRECOGNIZED_SHAPE";
  throw err;
}

function canonicalToSpineFlat(request) {
  return {
    niche: request.scope.niche,
    region: request.scope.region,
    city: request.scope.city,
    business_type: request.scope.business_type,
    seed_queries: request.queries.seed_queries,
    search_engine: request.scope.search_engine,
    device: request.scope.device,
    operator_id: request.operator_id,
    manual_serp: request.manual_serp || null,
    serp_provider_response: request.provider_response || null,
  };
}

module.exports = {
  ADAPTER_VERSION,
  SUPPORTED_V0_TYPES,
  generateRequestId,
  normalizeFromFile,
  canonicalToSpineFlat,
  isCanonicalShape,
  isLegacyFlatShape,
};
