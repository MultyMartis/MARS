#!/usr/bin/env node
/**
 * Rebuild comparison matrix from existing session artifacts (no acquisition).
 * Usage: node rebuild-comparison-matrix.mjs <session_dir>
 */
import { readFileSync, writeFileSync, existsSync } from "fs";
import { join } from "path";
import { createRequire } from "module";

const require = createRequire(import.meta.url);
const MIG_ROOT = join(import.meta.dirname, "..");
const { enrichLandingIndexWithDetail } = require(join(MIG_ROOT, "lib", "runtime", "load-landing-detail.js"));
const {
  buildComparisonMatrix,
  comparisonMatrixMarkdown,
} = require(join(MIG_ROOT, "lib", "session-spine", "build-comparison-matrix.js"));

function loadJson(p) {
  return JSON.parse(readFileSync(p, "utf8"));
}

function main() {
  const sessionDir = process.argv[2];
  if (!sessionDir) {
    console.error("Usage: node rebuild-comparison-matrix.mjs <session_dir>");
    process.exit(1);
  }

  const landingPath = join(sessionDir, "landing_observations.json");
  const websitePath = join(sessionDir, "website_snapshots.json");
  if (!existsSync(landingPath) || !existsSync(websitePath)) {
    throw new Error(`Missing landing_observations.json or website_snapshots.json in ${sessionDir}`);
  }

  const landingIndex = loadJson(landingPath);
  const websiteIndex = loadJson(websitePath);
  const enriched = enrichLandingIndexWithDetail(sessionDir, landingIndex);
  const rows = buildComparisonMatrix(enriched, websiteIndex);
  const sessionId = landingIndex.session_id || "unknown";

  writeFileSync(join(sessionDir, "market-leader-comparison-matrix.md"), comparisonMatrixMarkdown(rows), "utf8");
  writeFileSync(
    join(sessionDir, "market-leader-comparison-matrix.json"),
    `${JSON.stringify({ session_id: sessionId, rows, rebuilt_at: new Date().toISOString() }, null, 2)}\n`,
    "utf8"
  );

  console.log(
    JSON.stringify(
      {
        session_dir: sessionDir,
        rows: rows.length,
        matrix_md: "market-leader-comparison-matrix.md",
        matrix_json: "market-leader-comparison-matrix.json",
      },
      null,
      2
    )
  );
}

main();
