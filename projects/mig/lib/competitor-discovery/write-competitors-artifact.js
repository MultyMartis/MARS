"use strict";

const fs = require("fs");
const path = require("path");

const COMPETITORS_FILENAME = "competitors.json";
const ARTIFACT_SCHEMA_VERSION = "0.1";

/**
 * Build canonical competitors.json envelope (machine-readable SoT).
 * @param {string} sessionId
 * @param {object} competitorSection - output of discoverFromSerp (section wrapper)
 * @param {{ generated_at?: string }} [options]
 */
function buildCompetitorsArtifact(sessionId, competitorSection, options = {}) {
  const generatedAt = options.generated_at || new Date().toISOString();
  const discoveryPhase =
    competitorSection.discovery_phase != null ? competitorSection.discovery_phase : 2;

  const envelope = {
    schema_version: ARTIFACT_SCHEMA_VERSION,
    session_id: sessionId,
    generated_at: generatedAt,
    discovery_phase: discoveryPhase,
    competitor_observations: competitorSection,
  };
  if (competitorSection.discovery_mode) {
    envelope.discovery_mode = competitorSection.discovery_mode;
  }
  return envelope;
}

function writeCompetitorsArtifact(sessionDir, artifact) {
  const filePath = path.join(sessionDir, COMPETITORS_FILENAME);
  fs.writeFileSync(filePath, `${JSON.stringify(artifact, null, 2)}\n`, "utf8");
  return {
    path: filePath,
    filename: COMPETITORS_FILENAME,
    competitor_count: artifact.competitor_observations?.competitors?.length ?? 0,
  };
}

function deriveDiscoveryManifestMeta(artifact) {
  const section = artifact.competitor_observations || {};
  const count = Array.isArray(section.competitors) ? section.competitors.length : 0;
  const status = count > 0 ? "complete" : "empty";

  return {
    status,
    competitor_count: count,
    generated_at: artifact.generated_at,
    discovery_pass_at: section.discovery_pass_at || artifact.generated_at,
    artifact_file: COMPETITORS_FILENAME,
  };
}

module.exports = {
  COMPETITORS_FILENAME,
  ARTIFACT_SCHEMA_VERSION,
  buildCompetitorsArtifact,
  writeCompetitorsArtifact,
  deriveDiscoveryManifestMeta,
};
