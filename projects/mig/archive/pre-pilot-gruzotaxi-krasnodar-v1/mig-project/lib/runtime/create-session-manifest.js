"use strict";

const { resolveCaptureProfile } = require("./resolve-capture-profile");

const SCHEMA_VERSION = "0.2";

function skippedPassBlock(artifactFile) {
  return {
    status: "skipped",
    artifact_file: artifactFile,
  };
}

/**
 * Create session_manifest.json v0.2 after P0 intake.
 * @param {object} runtimeIntake - output of normalizeRuntimeIntake
 */
function createSessionManifest(runtimeIntake) {
  const captureProfile = resolveCaptureProfile({
    request_type: runtimeIntake.request_type,
    capture_profile: runtimeIntake.capture_profile,
  });
  const now = runtimeIntake.created_at || new Date().toISOString();

  return {
    schema_version: SCHEMA_VERSION,
    session_id: runtimeIntake.session_id,
    request_id: runtimeIntake.request_id,
    created_at: now,
    updated_at: now,

    status: "running",
    stage: "intake_complete",
    phase: "intake",
    runtime_profile: runtimeIntake.runtime_profile || runtimeIntake.request_type,

    operator_id: runtimeIntake.intake.operator_id,
    request_type: runtimeIntake.request_type,
    capture_profile: captureProfile,

    scope: {
      niche: runtimeIntake.intake.niche,
      region: runtimeIntake.intake.region,
      city: runtimeIntake.intake.city,
      business_type: runtimeIntake.intake.business_type,
      search_engine: runtimeIntake.intake.search_engine,
      device: runtimeIntake.intake.device,
    },

    queries: {
      seed_queries: runtimeIntake.intake.seed_queries,
      query_used: runtimeIntake.query_used,
      query_set: [],
      queries_executed: [],
    },

    serp: {
      mode: null,
      captured_at: null,
      result_file: "serp_result.json",
      discovery_mode: "single",
    },

    competitor_discovery: {
      status: "pending",
      competitor_count: 0,
      discovery_mode: "single",
      query_coverage: "pending",
      generated_at: null,
      artifact_file: "competitors.json",
    },

    website_acquisition: {
      status: "pending",
      snapshots_planned: 0,
      snapshots_success: 0,
      artifact_file: "website_snapshots.json",
    },

    landing_analysis: {
      status: "pending",
      landings_analyzed: 0,
      artifact_file: "landing_observations.json",
    },

    keyword_intelligence: {
      status: "skipped",
      artifact_file: "keyword_registry.json",
    },

    deep_research: {
      status: "skipped",
      artifact_file: "research_findings.json",
    },

    pack: {
      pack_state: "pending",
      mig_phase: "1",
      draft_file: "research_pack.draft.md",
      approved_file: null,
      approved_by: null,
      approved_at: null,
      published_at: null,
      consumed_at: null,
    },

    artifacts: {
      session_manifest: "session_manifest.json",
      serp_result: "serp_result.json",
      serp_index: null,
      competitors: "competitors.json",
      website_snapshots: null,
      landing_observations: null,
      keyword_registry: null,
      research_findings: null,
      research_pack_draft: null,
    },

    coverage: {
      session_grade: "X",
      phases_completed: ["intake"],
      phases_skipped: [],
      phases_failed: [],
      partial: false,
    },

    errors: [],
    safe_unknown: [],

    runtime_metadata: {
      spine_version: "0.2",
      orchestrator: "mig_runtime_mvp",
      last_pass: "intake",
      n8n_execution_id: null,
    },

    pass_status: {
      intake: "complete",
      search: "pending",
      competitors: "pending",
      websites: captureProfile.website_pass ? "pending" : "skipped",
      landings: captureProfile.landing_pass ? "pending" : "skipped",
      keywords: "skipped",
      deep_research: "skipped",
      pack: "pending",
    },

    approval: {
      pack_state: "pending",
      approved_by: null,
      approved_at: null,
    },
  };
}

module.exports = {
  SCHEMA_VERSION,
  createSessionManifest,
  skippedPassBlock,
};
