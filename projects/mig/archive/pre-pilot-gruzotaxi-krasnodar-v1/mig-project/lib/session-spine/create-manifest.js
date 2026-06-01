"use strict";

function createInitialManifest(validated) {
  return {
    schema_version: "0.1",
    session_id: validated.session_id,
    created_at: validated.created_at,
    updated_at: validated.created_at,
    stage: "intake_complete",
    operator_id: validated.intake.operator_id,
    scope: {
      niche: validated.intake.niche,
      region: validated.intake.region,
      city: validated.intake.city,
      business_type: validated.intake.business_type,
      search_engine: validated.intake.search_engine,
      device: validated.intake.device,
    },
    queries: {
      seed_queries: validated.intake.seed_queries,
      query_used: validated.query_used,
    },
    serp: {
      mode: null,
      captured_at: null,
      result_file: "serp_result.json",
    },
    artifacts: {
      session_manifest: "session_manifest.json",
      serp_result: "serp_result.json",
      competitors: "competitors.json",
      research_pack_draft: "research_pack.draft.md",
    },
    safe_unknown: [],
  };
}

function finalizeManifest(manifest, serpMeta, competitorMeta) {
  const next = {
    ...manifest,
    updated_at: new Date().toISOString(),
    stage: "draft_complete",
    serp: {
      ...manifest.serp,
      mode: serpMeta.mode,
      captured_at: serpMeta.captured_at,
    },
    safe_unknown: serpMeta.safe_unknown || manifest.safe_unknown || [],
  };

  if (competitorMeta) {
    next.competitor_discovery = competitorMeta;
    if (competitorMeta.competitor_count > 0) {
      next.mig_phase = "2";
    } else {
      next.mig_phase = "1";
    }
  }

  return next;
}

module.exports = {
  createInitialManifest,
  finalizeManifest,
};
