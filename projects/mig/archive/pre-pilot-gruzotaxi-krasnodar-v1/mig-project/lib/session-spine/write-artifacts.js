"use strict";

const fs = require("fs");
const path = require("path");

const { getSessionDir } = require("./paths");

function writeArtifacts(sessionId, manifest, serpResult, researchPackMarkdown, competitorsArtifact) {
  const sessionDir = getSessionDir(sessionId);
  fs.mkdirSync(sessionDir, { recursive: true });

  const manifestPath = path.join(sessionDir, "session_manifest.json");
  const serpPath = path.join(sessionDir, "serp_result.json");
  const packPath = path.join(sessionDir, "research_pack.draft.md");

  const files = {
    session_manifest: manifestPath,
    serp_result: serpPath,
    research_pack_draft: packPath,
  };

  fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
  fs.writeFileSync(serpPath, `${JSON.stringify(serpResult, null, 2)}\n`, "utf8");
  fs.writeFileSync(packPath, researchPackMarkdown, "utf8");

  if (competitorsArtifact) {
    const { writeCompetitorsArtifact } = require("../competitor-discovery/write-competitors-artifact");
    const written = writeCompetitorsArtifact(sessionDir, competitorsArtifact);
    files.competitors = written.path;
  }

  return {
    session_dir: sessionDir,
    files,
  };
}

module.exports = {
  writeArtifacts,
};
