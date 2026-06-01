"use strict";

const { validateIntake } = require("./validate-intake");
const { createInitialManifest, finalizeManifest } = require("./create-manifest");
const { pickSerpSource, normalizeSerp } = require("./normalize-serp");
const { buildResearchPackDraft, discoverFromSerp } = require("./build-research-pack");
const { writeArtifacts } = require("./write-artifacts");
const { getSessionRoot } = require("./paths");
const {
  buildCompetitorsArtifact,
  deriveDiscoveryManifestMeta,
} = require("../competitor-discovery/write-competitors-artifact");

function readStdin() {
  return new Promise((resolve, reject) => {
    const chunks = [];
    process.stdin.on("data", (chunk) => chunks.push(chunk));
    process.stdin.on("end", () => {
      const raw = Buffer.concat(chunks).toString("utf8").trim();
      if (!raw) {
        resolve({});
        return;
      }
      try {
        resolve(JSON.parse(raw));
      } catch (err) {
        reject(new Error(`Invalid JSON on stdin: ${err.message}`));
      }
    });
    process.stdin.on("error", reject);
  });
}

function runSessionSpine(body) {
  const validated = validateIntake(body);
  const manifest = createInitialManifest(validated);
  const serpSource = pickSerpSource(validated);
  const serpResult = normalizeSerp(validated, serpSource);
  const competitorSection = discoverFromSerp(serpResult, {
    queries_executed: manifest.queries?.queries_executed,
  });
  const competitorsArtifact = buildCompetitorsArtifact(
    validated.session_id,
    competitorSection,
    { generated_at: competitorSection.discovery_pass_at }
  );
  const competitorMeta = deriveDiscoveryManifestMeta(competitorsArtifact);
  const finalManifest = finalizeManifest(
    manifest,
    {
      mode: serpResult.source_mode,
      captured_at: serpResult.captured_at,
      safe_unknown: serpResult.safe_unknown,
    },
    competitorMeta
  );
  const researchPack = buildResearchPackDraft(finalManifest, serpResult, {
    competitor_observations: competitorSection,
    competitors_artifact: competitorsArtifact,
  });
  const written = writeArtifacts(
    validated.session_id,
    finalManifest,
    serpResult,
    researchPack,
    competitorsArtifact
  );

  return {
    status: "ok",
    session_id: validated.session_id,
    folder_path: written.session_dir,
    stage: finalManifest.stage,
    serp_mode: serpResult.source_mode,
    competitor_count: competitorMeta.competitor_count,
    mig_phase: finalManifest.mig_phase || "1",
    files: written.files,
    session_root: getSessionRoot(),
  };
}

async function main() {
  const argPath = process.argv[2];
  let body;

  if (argPath && argPath !== "--stdin") {
    const fs = require("fs");
    body = JSON.parse(fs.readFileSync(argPath, "utf8"));
  } else {
    body = await readStdin();
  }

  try {
    const result = runSessionSpine(body);
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
  } catch (err) {
    const payload = {
      status: "error",
      code: err.code || "SESSION_SPINE_ERROR",
      message: err.message,
      details: err.details || null,
    };
    process.stderr.write(`${JSON.stringify(payload, null, 2)}\n`);
    process.exit(1);
  }
}

if (require.main === module) {
  main();
}

module.exports = {
  runSessionSpine,
};
