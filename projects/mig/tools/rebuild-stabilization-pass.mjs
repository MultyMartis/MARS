#!/usr/bin/env node
/**
 * Rebuild session intelligence outputs (landing pass + comparison matrix + research pack).
 * No acquisition — uses existing website_snapshots.json only.
 * Usage: node rebuild-stabilization-pass.mjs <session_dir>
 */
import { readFileSync, writeFileSync, existsSync } from "fs";
import { join } from "path";
import { createRequire } from "module";

const require = createRequire(import.meta.url);
const MIG_ROOT = join(import.meta.dirname, "..");

const { runLandingPass } = require(join(MIG_ROOT, "lib", "landing-analysis", "run-landing-pass.js"));
const { enrichLandingIndexWithDetail } = require(join(MIG_ROOT, "lib", "runtime", "load-landing-detail.js"));
const { buildResearchPackDraft } = require(join(MIG_ROOT, "lib", "session-spine", "build-research-pack.js"));
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
    console.error("Usage: node rebuild-stabilization-pass.mjs <session_dir>");
    process.exit(1);
  }

  const manifestPath = join(sessionDir, "session_manifest.json");
  const websitePath = join(sessionDir, "website_snapshots.json");
  if (!existsSync(manifestPath) || !existsSync(websitePath)) {
    throw new Error(`Missing session_manifest.json or website_snapshots.json in ${sessionDir}`);
  }

  const manifest = loadJson(manifestPath);
  const researchScope = manifest.scope || {};

  console.log("Rebuilding landing analysis v2 (no acquisition)...");
  const landingResult = runLandingPass(sessionDir, { researchScope });
  const landingIndex = enrichLandingIndexWithDetail(sessionDir, landingResult.index);

  const websiteIndex = loadJson(websitePath);
  const serpPath = join(sessionDir, "serp_result.json");
  const competitorsPath = join(sessionDir, "competitors.json");
  const serp = existsSync(serpPath) ? loadJson(serpPath) : null;
  const competitors = existsSync(competitorsPath) ? loadJson(competitorsPath) : null;

  if (serp && competitors) {
    const pack = buildResearchPackDraft(manifest, serp, {
      competitor_observations: competitors.competitor_observations || competitors,
      website_snapshots: websiteIndex,
      landing_observations: landingIndex,
      mig_phase: manifest.mig_phase || "3",
    });
    writeFileSync(join(sessionDir, "research_pack.draft.md"), pack, "utf8");
  }

  const comparisonRows = buildComparisonMatrix(landingIndex, websiteIndex);
  const sessionId = landingIndex.session_id || manifest.session_id || "unknown";
  writeFileSync(join(sessionDir, "market-leader-comparison-matrix.md"), comparisonMatrixMarkdown(comparisonRows), "utf8");
  writeFileSync(
    join(sessionDir, "market-leader-comparison-matrix.json"),
    `${JSON.stringify({ session_id: sessionId, rows: comparisonRows, rebuilt_at: new Date().toISOString() }, null, 2)}\n`,
    "utf8"
  );

  console.log(
    JSON.stringify(
      {
        session_dir: sessionDir,
        landings: landingResult.landings.length,
        comparison_rows: comparisonRows.length,
        research_scope: researchScope,
      },
      null,
      2
    )
  );
}

main();
