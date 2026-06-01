"use strict";

const fs = require("fs");
const path = require("path");
const { getSessionDir } = require("../session-spine/paths");

function persistManifest(sessionId, manifest) {
  const sessionDir = getSessionDir(sessionId);
  fs.mkdirSync(sessionDir, { recursive: true });
  const manifestPath = path.join(sessionDir, "session_manifest.json");
  fs.writeFileSync(manifestPath, `${JSON.stringify(manifest, null, 2)}\n`, "utf8");
  return manifestPath;
}

module.exports = {
  persistManifest,
};
