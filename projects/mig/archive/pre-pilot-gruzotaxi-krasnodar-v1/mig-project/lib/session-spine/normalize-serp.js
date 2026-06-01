"use strict";

function pickSerpSource(validated) {
  if (validated.manual_serp && typeof validated.manual_serp === "object") {
    return { mode: "manual", raw: validated.manual_serp };
  }
  if (
    validated.serp_provider_response &&
    typeof validated.serp_provider_response === "object"
  ) {
    return { mode: "provider", raw: validated.serp_provider_response };
  }
  return { mode: "fallback", raw: null };
}

function normalizeSerp(validated, source) {
  const capturedAt = new Date().toISOString();
  const intake = validated.intake;
  const query = validated.query_used;

  if (source.mode === "manual") {
    const raw = source.raw;
    return {
      schema_version: "0.1",
      session_id: validated.session_id,
      captured_at: raw.timestamp || capturedAt,
      source_mode: "manual",
      search_engine: raw.search_engine || intake.search_engine,
      region: raw.region || intake.region,
      city: raw.city || intake.city,
      device: raw.device || intake.device,
      localization: raw.localization || null,
      query: raw.query || query,
      serp_type: raw.serp_type || "SAFE UNKNOWN",
      ads_blocks: raw.ads_blocks || { top_count: null, bottom_count: null, visible_patterns: [] },
      maps_local_pack: raw.maps_local_pack || "SAFE UNKNOWN",
      aggregators: Array.isArray(raw.aggregators) ? raw.aggregators : [],
      marketplaces: Array.isArray(raw.marketplaces) ? raw.marketplaces : [],
      review_signals: Array.isArray(raw.review_signals) ? raw.review_signals : [],
      offer_patterns: Array.isArray(raw.offer_patterns) ? raw.offer_patterns : [],
      cta_patterns: Array.isArray(raw.cta_patterns) ? raw.cta_patterns : [],
      landing_observations: Array.isArray(raw.landing_observations)
        ? raw.landing_observations
        : [],
      organic_results: Array.isArray(raw.organic_results) ? raw.organic_results : [],
      safe_unknown: Array.isArray(raw.safe_unknown)
        ? raw.safe_unknown
        : ["manual payload may omit fields not supplied by operator"],
    };
  }

  if (source.mode === "provider") {
    const raw = source.raw;
    const results = Array.isArray(raw.results) ? raw.results : raw.organic_results || [];
    return {
      schema_version: "0.1",
      session_id: validated.session_id,
      captured_at: raw.captured_at || capturedAt,
      source_mode: "provider",
      search_engine: raw.search_engine || intake.search_engine,
      region: raw.region || intake.region,
      city: raw.city || intake.city,
      device: raw.device || intake.device,
      localization: raw.localization || null,
      query: raw.query || query,
      serp_type: raw.serp_type || "mixed",
      ads_blocks: raw.ads_blocks || { top_count: null, bottom_count: null, visible_patterns: [] },
      maps_local_pack: raw.maps_local_pack || "SAFE UNKNOWN",
      aggregators: Array.isArray(raw.aggregators) ? raw.aggregators : [],
      marketplaces: Array.isArray(raw.marketplaces) ? raw.marketplaces : [],
      review_signals: Array.isArray(raw.review_signals) ? raw.review_signals : [],
      offer_patterns: Array.isArray(raw.offer_patterns) ? raw.offer_patterns : [],
      cta_patterns: Array.isArray(raw.cta_patterns) ? raw.cta_patterns : [],
      landing_observations: Array.isArray(raw.landing_observations)
        ? raw.landing_observations
        : [],
      organic_results: results,
      provider_meta: raw.provider_meta || null,
      safe_unknown: Array.isArray(raw.safe_unknown)
        ? raw.safe_unknown
        : ["provider-normalized fields may be incomplete without human review"],
    };
  }

  return {
    schema_version: "0.1",
    session_id: validated.session_id,
    captured_at: capturedAt,
    source_mode: "fallback",
    search_engine: intake.search_engine,
    region: intake.region,
    city: intake.city,
    device: intake.device,
    localization: null,
    query,
    serp_type: "SAFE UNKNOWN",
    ads_blocks: { top_count: null, bottom_count: null, visible_patterns: [] },
    maps_local_pack: "SAFE UNKNOWN",
    aggregators: [],
    marketplaces: [],
    review_signals: [],
    offer_patterns: [],
    cta_patterns: [],
    landing_observations: [],
    organic_results: [],
    safe_unknown: [
      "SERP provider unavailable — no manual_serp or serp_provider_response supplied",
      "SERP observation not captured; spine completed in SERP-only fallback mode",
      "All SERP detail fields require human capture before downstream use",
    ],
  };
}

module.exports = {
  pickSerpSource,
  normalizeSerp,
};
