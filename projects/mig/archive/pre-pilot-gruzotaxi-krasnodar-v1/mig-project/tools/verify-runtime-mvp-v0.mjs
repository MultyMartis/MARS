#!/usr/bin/env node
/**
 * End-to-end verification for MIG Runtime MVP v0.
 * Usage: node projects/mig/tools/verify-runtime-mvp-v0.mjs [fixture-path]
 */

import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const migRoot = path.join(__dirname, "..");
const require = createRequire(import.meta.url);

const { runMigSession } = require(path.join(migRoot, "lib", "runtime", "run-mig-session.js"));

const fixturePath =
  process.argv[2] ||
  path.join(migRoot, "test", "fixtures", "runtime-mvp", "research-request-runtime-mvp-v0.1.json");
const fixtureRoot = path.join(migRoot, "test", "fixtures", "website-html");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function fileExists(dir, name) {
  return fs.existsSync(path.join(dir, name));
}

function readJson(dir, name) {
  return JSON.parse(fs.readFileSync(path.join(dir, name), "utf8"));
}

async function main() {
  const raw = JSON.parse(fs.readFileSync(fixturePath, "utf8"));
  const expectations = raw.expectations || {};
  const fixtureMap = raw.fixture_map || {};
  const sessionId = raw.session_id;

  const tmpRoot = fs.mkdtempSync(path.join(migRoot, "test", ".verify-runtime-"));

  const request = { ...raw };
  delete request.description;
  delete request.expectations;
  delete request.fixture_map;

  const result = await runMigSession(request, {
    session_id: sessionId,
    session_root: tmpRoot,
    fixture_root: fixtureRoot,
    fixture_map: fixtureMap,
  });

  const sessionDir = result.folder_path;
  const manifest = readJson(sessionDir, "session_manifest.json");

  assert(result.status === "ok", `runtime status ${result.status}`);
  assert(manifest.schema_version === "0.2", "manifest schema_version 0.2");
  assert(manifest.session_id === sessionId, "session_id matches fixture");
  assert(manifest.request_id === raw.request_id, "request_id preserved");

  assert(fileExists(sessionDir, "serp_result.json"), "serp_result.json");
  assert(fileExists(sessionDir, "competitors.json"), "competitors.json");
  assert(fileExists(sessionDir, "research_pack.draft.md"), "research_pack.draft.md");

  if (expectations.min_competitors != null) {
    assert(
      (manifest.competitor_discovery?.competitor_count ?? 0) >= expectations.min_competitors,
      "competitor count"
    );
  }

  if (raw.capture_profile?.website_pass) {
    assert(fileExists(sessionDir, "website_snapshots.json"), "website_snapshots.json");
    if (expectations.min_snapshots_success != null) {
      assert(
        (manifest.website_acquisition?.snapshots_success ?? 0) >= expectations.min_snapshots_success,
        "snapshots_success"
      );
    }
  }

  if (raw.capture_profile?.landing_pass) {
    assert(fileExists(sessionDir, "landing_observations.json"), "landing_observations.json");
    if (expectations.min_landings != null) {
      assert(
        (manifest.landing_analysis?.landings_analyzed ?? 0) >= expectations.min_landings,
        "landings_analyzed"
      );
    }
  }

  if (expectations.terminal_stage) {
    assert(
      manifest.stage === expectations.terminal_stage ||
        manifest.stage === "partial_complete",
      `terminal stage expected ${expectations.terminal_stage}, got ${manifest.stage}`
    );
  }

  const packMd = fs.readFileSync(path.join(sessionDir, "research_pack.draft.md"), "utf8");
  assert(packMd.includes("## SERP Summary"), "pack SERP section");
  assert(packMd.includes("## Competitor Observations"), "pack competitors section");

  if (expectations.pack_includes_landing_sections) {
    assert(packMd.includes("## Landing observations"), "pack landing observations");
    assert(!packMd.includes("## Deep Research"), "no deep research section");
  }

  assert(!packMd.toLowerCase().includes("wordstat"), "no keyword/wordstat content");

  const lifecycleSummary = result.lifecycle.map((row) => ({
    phase: row.phase,
    stage: row.stage,
    ...(row.competitor_count != null ? { competitor_count: row.competitor_count } : {}),
    ...(row.snapshots_success != null ? { snapshots_success: row.snapshots_success } : {}),
    ...(row.landings_analyzed != null ? { landings_analyzed: row.landings_analyzed } : {}),
  }));

  const output = {
    status: "ok",
    verification: "runtime-mvp-v0",
    fixture: fixturePath,
    session_id: result.session_id,
    request_id: result.request_id,
    terminal: {
      stage: manifest.stage,
      phase: manifest.phase,
      status: manifest.status,
      pack_state: manifest.pack?.pack_state,
      mig_phase: manifest.pack?.mig_phase,
    },
    lifecycle_summary: lifecycleSummary,
    artifacts_generated: {
      session_manifest: true,
      serp_result: fileExists(sessionDir, "serp_result.json"),
      competitors: fileExists(sessionDir, "competitors.json"),
      website_snapshots: fileExists(sessionDir, "website_snapshots.json"),
      landing_observations: fileExists(sessionDir, "landing_observations.json"),
      research_pack_draft: fileExists(sessionDir, "research_pack.draft.md"),
      snapshot_dirs: fs.existsSync(path.join(sessionDir, "snapshots", "sites")),
      landing_dirs: fs.existsSync(path.join(sessionDir, "landings")),
    },
    counts: {
      competitor_count: manifest.competitor_discovery?.competitor_count,
      snapshots_success: manifest.website_acquisition?.snapshots_success,
      landings_analyzed: manifest.landing_analysis?.landings_analyzed,
    },
    manifest_summary: {
      schema_version: manifest.schema_version,
      coverage: manifest.coverage,
      pass_status: manifest.pass_status,
      capture_profile: manifest.capture_profile,
    },
    safe_unknown_summary: manifest.safe_unknown,
    pack_excerpt_lines: packMd.split("\n").slice(0, 12),
    session_dir: sessionDir,
    note: "Session folder retained under test/.verify-runtime-* for inspection",
  };

  console.log(JSON.stringify(output, null, 2));
}

try {
  await main();
} catch (err) {
  console.error(
    JSON.stringify(
      {
        status: "error",
        message: err.message,
        stack: err.stack,
      },
      null,
      2
    )
  );
  process.exit(1);
}
