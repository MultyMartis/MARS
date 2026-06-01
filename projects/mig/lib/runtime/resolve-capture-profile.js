"use strict";

const DEFAULT_PROFILE = {
  multi_query: false,
  website_pass: false,
  landing_pass: false,
  keyword_pass: false,
  deep_research_pass: false,
};

const TYPE_DEFAULTS = {
  serp_capture: { ...DEFAULT_PROFILE },
  groundtruth_run: {
    multi_query: false,
    website_pass: true,
    landing_pass: true,
    keyword_pass: false,
    deep_research_pass: false,
  },
  competitor_discovery: { ...DEFAULT_PROFILE },
  landing_analysis: {
    multi_query: false,
    website_pass: true,
    landing_pass: true,
    keyword_pass: false,
    deep_research_pass: false,
  },
  deep_research: {
    multi_query: false,
    website_pass: true,
    landing_pass: true,
    keyword_pass: false,
    deep_research_pass: true,
  },
  session_resume: { ...DEFAULT_PROFILE },
  pack_retrieval: { ...DEFAULT_PROFILE },
};

/**
 * Resolve capture_profile from Research Request type + explicit profile object.
 * Deep Research and Keyword passes are forced off for Runtime MVP.
 */
function resolveCaptureProfile(request = {}) {
  const requestType = request.request_type || "serp_capture";
  const base = TYPE_DEFAULTS[requestType] || TYPE_DEFAULTS.serp_capture;
  const cp =
    request.capture_profile && typeof request.capture_profile === "object"
      ? request.capture_profile
      : {};

  const resolved = {
    multi_query: cp.multi_query ?? base.multi_query ?? false,
    website_pass: cp.website_pass ?? base.website_pass ?? false,
    landing_pass: cp.landing_pass ?? base.landing_pass ?? false,
    keyword_pass: false,
    deep_research_pass: false,
  };

  if (resolved.landing_pass && !resolved.website_pass) {
    resolved.website_pass = true;
  }

  return resolved;
}

module.exports = {
  DEFAULT_PROFILE,
  TYPE_DEFAULTS,
  resolveCaptureProfile,
};
