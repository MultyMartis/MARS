"use strict";

const fs = require("fs");
const path = require("path");

const { normalizeRuntimeIntake } = require("./normalize-runtime-intake");
const { resolveCaptureProfile } = require("./resolve-capture-profile");
const { createSessionManifest } = require("./create-session-manifest");
const { updateSessionManifest, setStagePhase } = require("./update-session-manifest");
const { finalizeSession, mergeSerpSafeUnknown } = require("./finalize-session");
const { persistManifest } = require("./persist-manifest");
const { enrichLandingIndexWithDetail } = require("./load-landing-detail");

const { pickSerpSource, normalizeSerp } = require("../session-spine/normalize-serp");
const { buildResearchPackDraft } = require("../session-spine/build-research-pack");
const { getSessionDir } = require("../session-spine/paths");
const {
  buildCompetitorsArtifact,
  deriveDiscoveryManifestMeta,
} = require("../competitor-discovery/write-competitors-artifact");
const { discoverFromSerp } = require("../competitor-discovery/discover-from-serp");
const { runWebsitePass } = require("../website-acquisition/run-website-pass");
const { runLandingPass } = require("../landing-analysis/run-landing-pass");

function spineValidatedFromRuntime(runtimeIntake) {
  return {
    session_id: runtimeIntake.session_id,
    created_at: runtimeIntake.created_at,
    intake: runtimeIntake.intake,
    query_used: runtimeIntake.query_used,
    manual_serp: runtimeIntake.manual_serp,
    serp_provider_response: runtimeIntake.serp_provider_response,
  };
}

function writeJson(sessionDir, filename, data) {
  const filePath = path.join(sessionDir, filename);
  fs.writeFileSync(filePath, `${JSON.stringify(data, null, 2)}\n`, "utf8");
  return filePath;
}

function countSuccessfulSnapshots(websiteIndex) {
  return (websiteIndex?.snapshots || []).filter((s) => s.status === "success").length;
}

/**
 * Execute full MIG Runtime MVP sequence (P0 → P1 → P2 → optional P3/P4 → P6).
 * @param {object} body - Research Request or legacy flat intake
 * @param {object} [options]
 * @param {string} [options.session_id] - deterministic session id for fixtures
 * @param {string} [options.session_root] - override MIG_SESSION_ROOT
 * @param {Record<string,string>} [options.fixture_map] - URL → html fixture file
 * @param {string} [options.fixture_root] - directory for fixture_map values
 */
async function runMigSession(body, options = {}) {
  if (options.session_root) {
    process.env.MIG_SESSION_ROOT = options.session_root;
  }

  const lifecycle = [];
  const runtimeIntake = normalizeRuntimeIntake(body, options);
  const captureProfile = resolveCaptureProfile({
    request_type: runtimeIntake.request_type,
    capture_profile: runtimeIntake.capture_profile,
  });
  const spineValidated = spineValidatedFromRuntime(runtimeIntake);
  const sessionId = runtimeIntake.session_id;
  const sessionDir = getSessionDir(sessionId);

  let manifest = createSessionManifest(runtimeIntake);
  persistManifest(sessionId, manifest);
  lifecycle.push({ phase: "P0", stage: manifest.stage, status: manifest.status });

  let serpResult = null;
  let competitorsArtifact = null;
  let websiteIndex = null;
  let landingIndex = null;
  let competitorSection = null;

  // —— P1 Search Acquisition ——
  manifest = setStagePhase(manifest, {
    stage: "acquiring_serp",
    phase: "search",
    status: "running",
    last_pass: "search",
  });
  manifest.pass_status = { ...manifest.pass_status, search: "running" };
  persistManifest(sessionId, manifest);

  try {
    const serpSource = pickSerpSource(spineValidated);
    serpResult = normalizeSerp(spineValidated, serpSource);

    if (
      serpResult.source_mode === "fallback" &&
      (!serpResult.organic_results || serpResult.organic_results.length === 0) &&
      runtimeIntake.strict
    ) {
      const err = new Error("SERP unavailable and strict intake forbids fallback-only session");
      err.code = "SERP_UNAVAILABLE";
      throw err;
    }

    manifest = mergeSerpSafeUnknown(manifest, serpResult);
    manifest = updateSessionManifest(manifest, {
      stage: "serp_complete",
      phase: "search",
      serp: {
        mode: serpResult.source_mode,
        captured_at: serpResult.captured_at,
        result_file: "serp_result.json",
        discovery_mode: "single",
      },
      pass_status: { search: "complete" },
      runtime_metadata: { last_pass: "search" },
    });
    writeJson(sessionDir, "serp_result.json", serpResult);
    lifecycle.push({ phase: "P1", stage: manifest.stage, serp_mode: serpResult.source_mode });
  } catch (err) {
    manifest = updateSessionManifest(manifest, {
      stage: "failed",
      phase: "search",
      status: "failed",
      pass_status: { search: "failed" },
      errors: [
        {
          code: err.code || "SERP_UNAVAILABLE",
          pass: "search",
          message: err.message,
          recoverable: false,
        },
      ],
      safe_unknown: ["SERP acquisition failed — session terminated"],
    });
    manifest = finalizeSession(manifest, { packWritten: false, fatal: true });
    persistManifest(sessionId, manifest);
    return buildRunResult(manifest, lifecycle, sessionDir, {
      serpResult,
      competitorsArtifact,
      websiteIndex,
      landingIndex,
    });
  }

  persistManifest(sessionId, manifest);

  // —— P2 Competitor Discovery ——
  manifest = setStagePhase(manifest, {
    stage: "discovering_competitors",
    phase: "competitors",
    last_pass: "competitor_discovery",
  });
  manifest.pass_status = { ...manifest.pass_status, competitors: "running" };
  persistManifest(sessionId, manifest);

  try {
    competitorSection = discoverFromSerp(serpResult, {
      queries_executed: manifest.queries?.queries_executed,
    });
    competitorsArtifact = buildCompetitorsArtifact(sessionId, competitorSection, {
      generated_at: competitorSection.discovery_pass_at,
    });
    const competitorMeta = deriveDiscoveryManifestMeta(competitorsArtifact);
    writeJson(sessionDir, "competitors.json", competitorsArtifact);

    manifest = updateSessionManifest(manifest, {
      stage: "competitors_complete",
      phase: "competitors",
      competitor_discovery: {
        ...competitorMeta,
        discovery_mode: competitorSection.discovery_mode || "single",
        query_coverage: competitorSection.discovery_coverage?.query_coverage || "complete",
      },
      pass_status: {
        competitors: competitorMeta.status === "empty" ? "empty" : "complete",
      },
      mig_phase: competitorMeta.competitor_count > 0 ? "2" : "1",
      pack: { mig_phase: competitorMeta.competitor_count > 0 ? "2" : "1" },
      safe_unknown: competitorSection.safe_unknown || [],
      runtime_metadata: { last_pass: "competitor_discovery" },
    });
    lifecycle.push({
      phase: "P2",
      stage: manifest.stage,
      competitor_count: competitorMeta.competitor_count,
    });
  } catch (err) {
    const emptySection = {
      section_id: "competitor_observations",
      schema_version: "0",
      discovery_pass_at: new Date().toISOString(),
      competitors: [],
      section_evidence_grade: "X",
      section_coverage: "failed",
      safe_unknown: ["Competitor discovery pass failed"],
    };
    competitorsArtifact = buildCompetitorsArtifact(sessionId, emptySection);
    writeJson(sessionDir, "competitors.json", competitorsArtifact);
    competitorSection = emptySection;

    manifest = updateSessionManifest(manifest, {
      stage: "competitors_complete",
      phase: "competitors",
      competitor_discovery: {
        status: "empty",
        competitor_count: 0,
        discovery_mode: "single",
        query_coverage: "failed",
        generated_at: new Date().toISOString(),
        artifact_file: "competitors.json",
      },
      pass_status: { competitors: "failed" },
      errors: [
        {
          code: "COMPETITOR_DISCOVERY_FAILED",
          pass: "competitors",
          message: err.message,
          recoverable: true,
        },
      ],
      safe_unknown: ["Competitor discovery pass failed — empty competitors.json written"],
    });
    lifecycle.push({ phase: "P2", stage: manifest.stage, error: err.message });
  }

  persistManifest(sessionId, manifest);

  // —— P3 Website Acquisition ——
  if (captureProfile.website_pass) {
    manifest = setStagePhase(manifest, {
      stage: "acquiring_sites",
      phase: "websites",
      last_pass: "website_acquisition",
    });
    manifest.pass_status = { ...manifest.pass_status, websites: "running" };
    persistManifest(sessionId, manifest);

    try {
      const websiteResult = await runWebsitePass(sessionDir, {
        fixtureRoot: options.fixture_root,
        fixtureMap: options.fixture_map,
        signals: runtimeIntake.signals,
      });
      websiteIndex = websiteResult.index;
      const successCount = countSuccessfulSnapshots(websiteIndex);
      const planned =
        websiteIndex.url_plan?.length ?? websiteResult.url_plan?.planned_count ?? 0;
      const waStatus =
        successCount === 0
          ? "failed"
          : successCount < planned
            ? "partial"
            : "complete";

      manifest = updateSessionManifest(manifest, {
        stage: "sites_complete",
        phase: "websites",
        website_acquisition: {
          status: waStatus,
          snapshots_planned: planned,
          snapshots_success: successCount,
          artifact_file: "website_snapshots.json",
        },
        artifacts: { website_snapshots: "website_snapshots.json" },
        pass_status: { websites: waStatus === "failed" ? "failed" : "complete" },
        pack: { mig_phase: successCount > 0 ? "3" : manifest.pack.mig_phase },
        safe_unknown: websiteIndex.safe_unknown || [],
        runtime_metadata: { last_pass: "website_acquisition" },
      });

      if (waStatus === "partial") {
        manifest.safe_unknown = [
          ...(manifest.safe_unknown || []),
          "Website acquisition partial — some URLs failed or were skipped",
        ];
      }
      if (waStatus === "failed") {
        manifest.safe_unknown = [
          ...(manifest.safe_unknown || []),
          "Website acquisition produced no successful snapshots",
        ];
      }

      lifecycle.push({
        phase: "P3",
        stage: manifest.stage,
        snapshots_success: successCount,
        website_status: waStatus,
      });
    } catch (err) {
      manifest = updateSessionManifest(manifest, {
        stage: "sites_complete",
        phase: "websites",
        website_acquisition: {
          status: "failed",
          snapshots_planned: 0,
          snapshots_success: 0,
          artifact_file: "website_snapshots.json",
        },
        pass_status: { websites: "failed" },
        errors: [
          {
            code: "WEBSITE_PARTIAL",
            pass: "websites",
            message: err.message,
            recoverable: true,
          },
        ],
        safe_unknown: ["Website acquisition pass error — see session errors"],
        runtime_metadata: { last_pass: "website_acquisition" },
      });
      lifecycle.push({ phase: "P3", stage: manifest.stage, error: err.message });
    }
  } else {
    manifest = updateSessionManifest(manifest, {
      website_acquisition: {
        status: "skipped",
        snapshots_planned: 0,
        snapshots_success: 0,
        artifact_file: "website_snapshots.json",
      },
      pass_status: { websites: "skipped" },
      safe_unknown: "Website acquisition skipped by capture_profile",
    });
    lifecycle.push({ phase: "P3", stage: "skipped" });
  }

  persistManifest(sessionId, manifest);

  // —— P4 Landing Analysis ——
  const websiteSuccess = countSuccessfulSnapshots(websiteIndex);
  if (captureProfile.landing_pass && websiteSuccess > 0) {
    manifest = setStagePhase(manifest, {
      stage: "analyzing_landings",
      phase: "landings",
      last_pass: "landing_analysis",
    });
    manifest.pass_status = { ...manifest.pass_status, landings: "running" };
    persistManifest(sessionId, manifest);

    try {
      const landingResult = runLandingPass(sessionDir, { websiteIndex });
      landingIndex = enrichLandingIndexWithDetail(sessionDir, landingResult.index);
      const landingCount = landingIndex.landings?.length ?? 0;

      manifest = updateSessionManifest(manifest, {
        stage: "landings_complete",
        phase: "landings",
        landing_analysis: {
          status: landingCount > 0 ? "complete" : "skipped",
          landings_analyzed: landingCount,
          artifact_file: "landing_observations.json",
        },
        artifacts: { landing_observations: "landing_observations.json" },
        pass_status: { landings: landingCount > 0 ? "complete" : "skipped" },
        pack: { mig_phase: landingCount > 0 ? "3" : manifest.pack.mig_phase },
        safe_unknown: landingIndex.safe_unknown || [],
        runtime_metadata: { last_pass: "landing_analysis" },
      });
      lifecycle.push({ phase: "P4", stage: manifest.stage, landings_analyzed: landingCount });
    } catch (err) {
      manifest = updateSessionManifest(manifest, {
        stage: "landings_complete",
        phase: "landings",
        landing_analysis: {
          status: "skipped",
          landings_analyzed: 0,
          artifact_file: "landing_observations.json",
        },
        pass_status: { landings: "skipped" },
        errors: [
          {
            code: "LANDING_SKIPPED",
            pass: "landings",
            message: err.message,
            recoverable: true,
          },
        ],
        safe_unknown: ["Landing Analysis pass not executed — error during pass"],
        runtime_metadata: { last_pass: "landing_analysis" },
      });
      lifecycle.push({ phase: "P4", stage: manifest.stage, error: err.message });
    }
  } else {
    const skipReason =
      !captureProfile.landing_pass
        ? "Landing Analysis skipped by capture_profile"
        : "Landing Analysis skipped — no successful website snapshots";
    manifest = updateSessionManifest(manifest, {
      landing_analysis: {
        status: "skipped",
        landings_analyzed: 0,
        artifact_file: "landing_observations.json",
      },
      pass_status: { landings: "skipped" },
      safe_unknown: skipReason,
    });
    lifecycle.push({ phase: "P4", stage: "skipped", reason: skipReason });
  }

  persistManifest(sessionId, manifest);

  // —— P6 Research Pack Assembly ——
  if (!serpResult) {
    manifest = finalizeSession(
      updateSessionManifest(manifest, {
        status: "failed",
        stage: "failed",
        pass_status: { pack: "failed" },
      }),
      { packWritten: false, fatal: true }
    );
    persistManifest(sessionId, manifest);
    return buildRunResult(manifest, lifecycle, sessionDir, {
      serpResult,
      competitorsArtifact,
      websiteIndex,
      landingIndex,
    });
  }

  manifest = setStagePhase(manifest, {
    stage: "assembling_pack",
    phase: "pack",
    last_pass: "pack",
  });
  manifest.pass_status = { ...manifest.pass_status, pack: "running" };
  persistManifest(sessionId, manifest);

  try {
    if (!competitorsArtifact && competitorSection) {
      competitorsArtifact = buildCompetitorsArtifact(sessionId, competitorSection);
    }
    if (!competitorsArtifact) {
      competitorSection =
        competitorSection ||
        discoverFromSerp(serpResult, { queries_executed: manifest.queries?.queries_executed });
      competitorsArtifact = buildCompetitorsArtifact(sessionId, competitorSection);
      writeJson(sessionDir, "competitors.json", competitorsArtifact);
    }

    const packOptions = {
      competitor_observations: competitorsArtifact.competitor_observations,
      competitors_artifact: competitorsArtifact,
      website_snapshots: websiteIndex,
      landing_observations: landingIndex,
      mig_phase: manifest.pack?.mig_phase || "2",
    };

    const researchPack = buildResearchPackDraft(manifest, serpResult, packOptions);
    fs.writeFileSync(path.join(sessionDir, "research_pack.draft.md"), researchPack, "utf8");

    manifest = updateSessionManifest(manifest, {
      artifacts: { research_pack_draft: "research_pack.draft.md" },
      pack: {
        pack_state: "draft",
        mig_phase:
          landingIndex?.landings?.length > 0
            ? "3"
            : websiteIndex?.snapshots?.length > 0
              ? "3"
              : manifest.pack.mig_phase,
      },
    });

    manifest = finalizeSession(manifest, { packWritten: true, fatal: false });
    lifecycle.push({
      phase: "P6",
      stage: manifest.stage,
      pack_state: manifest.pack.pack_state,
    });
  } catch (err) {
    manifest = updateSessionManifest(manifest, {
      status: "failed",
      stage: "failed",
      pass_status: { pack: "failed" },
      errors: [
        {
          code: "PACK_ASSEMBLY_FAILED",
          pass: "pack",
          message: err.message,
          recoverable: false,
        },
      ],
    });
    manifest = finalizeSession(manifest, { packWritten: false, fatal: true });
    lifecycle.push({ phase: "P6", stage: "failed", error: err.message });
  }

  persistManifest(sessionId, manifest);

  return buildRunResult(manifest, lifecycle, sessionDir, {
    serpResult,
    competitorsArtifact,
    websiteIndex,
    landingIndex,
  });
}

function buildRunResult(manifest, lifecycle, sessionDir, artifacts) {
  return {
    status: manifest.status === "failed" ? "error" : "ok",
    session_id: manifest.session_id,
    request_id: manifest.request_id,
    folder_path: sessionDir,
    stage: manifest.stage,
    phase: manifest.phase,
    pack_state: manifest.pack?.pack_state,
    mig_phase: manifest.pack?.mig_phase,
    serp_mode: manifest.serp?.mode,
    competitor_count: manifest.competitor_discovery?.competitor_count ?? 0,
    snapshots_success: manifest.website_acquisition?.snapshots_success ?? 0,
    landings_analyzed: manifest.landing_analysis?.landings_analyzed ?? 0,
    lifecycle,
    coverage: manifest.coverage,
    safe_unknown: manifest.safe_unknown,
    errors: manifest.errors,
    artifacts: {
      serp: Boolean(artifacts.serpResult),
      competitors: Boolean(artifacts.competitorsArtifact),
      website_snapshots: Boolean(artifacts.websiteIndex),
      landing_observations: Boolean(artifacts.landingIndex),
      research_pack_draft: manifest.artifacts?.research_pack_draft != null,
    },
  };
}

async function main() {
  const argPath = process.argv[2];
  let body = {};

  if (argPath && argPath !== "--stdin") {
    body = JSON.parse(fs.readFileSync(argPath, "utf8"));
  } else {
    const chunks = [];
    for await (const chunk of process.stdin) {
      chunks.push(chunk);
    }
    const raw = Buffer.concat(chunks).toString("utf8").trim();
    if (raw) {
      body = JSON.parse(raw);
    }
  }

  const fixtureMap = body._runtime_fixture_map || body.fixture_map;
  const fixtureRoot = body._runtime_fixture_root || body.fixture_root;
  const sessionRoot = body._runtime_session_root;
  delete body._runtime_fixture_map;
  delete body._runtime_fixture_root;
  delete body._runtime_session_root;

  try {
    const result = await runMigSession(body, {
      fixture_map: fixtureMap,
      fixture_root: fixtureRoot,
      session_root: sessionRoot,
      session_id: body.session_id,
    });
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
    if (result.status === "error") {
      process.exit(1);
    }
  } catch (err) {
    process.stderr.write(
      `${JSON.stringify(
        {
          status: "error",
          code: err.code || "RUNTIME_ERROR",
          message: err.message,
        },
        null,
        2
      )}\n`
    );
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  runMigSession,
};
