#!/usr/bin/env node
/**
 * Pilot #1 backtest: re-run Landing Analysis v2 on existing session artifacts (no new acquisition).
 * Usage: node projects/mig/tools/backtest-landing-analysis-v2-pilot.mjs [sessionDir]
 */

import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const migRoot = path.join(__dirname, "..");
const require = createRequire(import.meta.url);

const { runLandingPass } = require(path.join(migRoot, "lib", "landing-analysis", "run-landing-pass.js"));
const { enrichLandingIndexWithDetail } = require(path.join(migRoot, "lib", "runtime", "load-landing-detail.js"));
const { buildResearchPackDraft } = require(path.join(migRoot, "lib", "session-spine", "build-research-pack.js"));

const SESSION_ID = "mig-20260604-61b585";
const sessionDir =
  process.argv[2] || path.join(migRoot, "sessions", SESSION_ID);
const reportDir = path.join(migRoot, "reports", "backtest-landing-v2-pilot");

function readJson(p) {
  return JSON.parse(fs.readFileSync(p, "utf8"));
}

function countNavOffersInDetail(detail) {
  let nav = 0;
  for (const o of detail.offers || []) {
    const t = (o.text || "").toLowerCase();
    if (
      /отзывы|вопросы и ответы|о компании|контакты|социальных сетях/.test(t) &&
      t.length < 60
    ) {
      nav += 1;
    }
  }
  return nav;
}

function main() {
  if (!fs.existsSync(path.join(sessionDir, "website_snapshots.json"))) {
    throw new Error(`Missing website_snapshots.json in ${sessionDir}`);
  }

  fs.mkdirSync(reportDir, { recursive: true });

  const packV1Path = path.join(sessionDir, "research_pack.draft.md");
  const indexV1Path = path.join(sessionDir, "landing_observations.json");
  const packV1 = fs.existsSync(packV1Path) ? fs.readFileSync(packV1Path, "utf8") : "";
  const indexV1 = fs.existsSync(indexV1Path) ? readJson(indexV1Path) : null;

  const detailV1 = [];
  for (const row of indexV1?.landings || []) {
    const p = path.join(sessionDir, row.artifact_ref);
    if (fs.existsSync(p)) {
      detailV1.push(readJson(p));
    }
  }

  fs.writeFileSync(path.join(reportDir, "pack-v1.snapshot.md"), packV1, "utf8");
  fs.writeFileSync(
    path.join(reportDir, "index-v1.snapshot.json"),
    `${JSON.stringify(indexV1, null, 2)}\n`,
    "utf8"
  );

  const landingResult = runLandingPass(sessionDir);
  const landingIndexV2 = enrichLandingIndexWithDetail(sessionDir, landingResult.index);

  const manifest = readJson(path.join(sessionDir, "session_manifest.json"));
  const serp = readJson(path.join(sessionDir, "serp_result.json"));
  const competitors = readJson(path.join(sessionDir, "competitors.json"));
  const websiteIndex = readJson(path.join(sessionDir, "website_snapshots.json"));

  const packV2 = buildResearchPackDraft(manifest, serp, {
    competitor_observations: competitors.competitor_observations || competitors,
    website_snapshots: websiteIndex,
    landing_observations: landingIndexV2,
    mig_phase: "3",
  });

  fs.writeFileSync(path.join(sessionDir, "research_pack.draft.md"), packV2, "utf8");
  fs.writeFileSync(path.join(reportDir, "pack-v2.generated.md"), packV2, "utf8");
  fs.writeFileSync(
    path.join(reportDir, "index-v2.generated.json"),
    `${JSON.stringify(landingIndexV2, null, 2)}\n`,
    "utf8"
  );

  const comparison = [];
  comparison.push("# Pilot backtest — Landing Analysis v2");
  comparison.push("");
  comparison.push(`Session: \`${SESSION_ID}\``);
  comparison.push(`Generated: ${new Date().toISOString()}`);
  comparison.push("");

  comparison.push("## Index (v1 → v2)");
  comparison.push("");
  comparison.push("| Landing | v1 offer_count | v2 families_present | v2 top signal |");
  comparison.push("|---------|----------------|---------------------|---------------|");
  for (const row of landingIndexV2.landings || []) {
    const v1row = indexV1?.landings?.find((r) => r.landing_id === row.landing_id);
    const top = row.observation_summary?.top_signals?.[0]?.text?.slice(0, 50) || "—";
    comparison.push(
      `| ${row.domain} | ${v1row?.offer_count ?? "—"} | ${(row.observation_summary?.families_present || []).join(", ")} | ${top} |`
    );
  }

  comparison.push("");
  comparison.push("## Nav-noise (v1 offers mis-tagged)");
  for (const obs of landingResult.landings) {
    const ex = obs._processing?.excluded_offers?.length ?? 0;
    const v1nav = countNavOffersInDetail(detailV1.find((d) => d.landing_id === obs.landing_id) || {});
    comparison.push(`- ${obs.domain}: v1 nav-like offer rows ≈ ${v1nav}; v2 excluded ${ex}`);
  }

  comparison.push("");
  comparison.push("## Pack structure");
  comparison.push(`- v1 has flat «Offer observations»: ${packV1.includes("## Offer observations")}`);
  comparison.push(`- v2 has intelligence cards: ${packV2.includes("## Landing intelligence —")}`);
  comparison.push(`- v1 count table in index: ${JSON.stringify(indexV1?.landings?.[0] || {}).includes("offer_count")}`);

  const reportPath = path.join(reportDir, "comparison.md");
  fs.writeFileSync(reportPath, `${comparison.join("\n")}\n`, "utf8");

  console.log(
    JSON.stringify(
      {
        session_id: SESSION_ID,
        report_dir: reportDir,
        comparison: reportPath,
        schema_version: landingIndexV2.schema_version,
        analysis_phase: landingIndexV2.analysis_phase,
      },
      null,
      2
    )
  );
}

main();
