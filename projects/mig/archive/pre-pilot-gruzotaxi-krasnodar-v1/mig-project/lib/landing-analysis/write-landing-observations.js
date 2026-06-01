"use strict";

const fs = require("fs");
const path = require("path");

const INDEX_FILENAME = "landing_observations.json";

function landingArtifactRefs(landingId) {
  return {
    landing_observation: `landings/${landingId}/landing_observation.json`,
  };
}

function buildLandingObservationsIndex(sessionId, landings, options = {}) {
  const generatedAt = options.generated_at || new Date().toISOString();
  const grades = landings.map((l) => l.evidence_grade);
  const { worstGrade } = require("./utils");

  const successLike = landings.filter((l) => l.evidence_grade !== "X");
  let sessionCoverage = "unknown";
  if (!landings.length) {
    sessionCoverage = "minimal";
  } else if (successLike.length === landings.length) {
    sessionCoverage = "complete";
  } else if (successLike.length > 0) {
    sessionCoverage = "partial";
  } else {
    sessionCoverage = "minimal";
  }

  const sessionSafeUnknown = options.safe_unknown || [];
  if (landings.some((l) => l.page_type === "unknown")) {
    sessionSafeUnknown.push("One or more landings have structural page_type unknown");
  }

  return {
    schema_version: "0.1",
    session_id: sessionId,
    generated_at: generatedAt,
    analysis_phase: "landing_analysis_v1",
    upstream_artifacts: {
      website_snapshots: options.website_snapshots_file || "website_snapshots.json",
      competitors: options.competitors_file || "competitors.json",
    },
    landings: landings.map((l) => ({
      landing_id: l.landing_id,
      snapshot_id: l.snapshot_id,
      competitor_id: l.competitor_id,
      domain: l.domain,
      final_url: l.final_url,
      page_type: l.page_type,
      evidence_grade: l.evidence_grade,
      artifact_ref: `landings/${l.landing_id}/landing_observation.json`,
      block_count: l.visible_blocks?.length ?? 0,
      offer_count: l.offers?.length ?? 0,
      cta_count: l.cta_patterns?.length ?? 0,
      trust_count: l.trust_patterns?.length ?? 0,
    })),
    session_coverage: sessionCoverage,
    section_evidence_grade: worstGrade(grades),
    safe_unknown: sessionSafeUnknown,
  };
}

function writeLandingObservation(sessionDir, observation) {
  const landingDir = path.join(sessionDir, "landings", observation.landing_id);
  fs.mkdirSync(landingDir, { recursive: true });
  const filePath = path.join(landingDir, "landing_observation.json");
  fs.writeFileSync(filePath, `${JSON.stringify(observation, null, 2)}\n`, "utf8");
  return filePath;
}

function writeLandingObservationsIndex(sessionDir, index) {
  const indexPath = path.join(sessionDir, INDEX_FILENAME);
  fs.writeFileSync(indexPath, `${JSON.stringify(index, null, 2)}\n`, "utf8");
  return { path: indexPath, filename: INDEX_FILENAME };
}

function deriveLandingManifestMeta(index) {
  return {
    status: index.landings.length > 0 ? "complete" : "empty",
    landing_count: index.landings.length,
    generated_at: index.generated_at,
    artifact_file: INDEX_FILENAME,
    section_evidence_grade: index.section_evidence_grade,
    session_coverage: index.session_coverage,
  };
}

module.exports = {
  INDEX_FILENAME,
  landingArtifactRefs,
  buildLandingObservationsIndex,
  writeLandingObservation,
  writeLandingObservationsIndex,
  deriveLandingManifestMeta,
};
