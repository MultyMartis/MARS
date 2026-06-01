"use strict";

const fs = require("fs");
const path = require("path");

/**
 * Attach full landing_observation objects for pack projection (_detail).
 */
function enrichLandingIndexWithDetail(sessionDir, landingIndex) {
  if (!landingIndex) {
    return null;
  }
  const detail = [];
  for (const row of landingIndex.landings || []) {
    const ref = row.artifact_ref || `landings/${row.landing_id}/landing_observation.json`;
    const filePath = path.join(sessionDir, ref);
    if (fs.existsSync(filePath)) {
      detail.push(JSON.parse(fs.readFileSync(filePath, "utf8")));
    }
  }
  return { ...landingIndex, _detail: detail };
}

module.exports = {
  enrichLandingIndexWithDetail,
};
