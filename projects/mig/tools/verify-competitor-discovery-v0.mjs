#!/usr/bin/env node
/**
 * Local verification for MIG Competitor Discovery v0.2b (artifact integration).
 * Usage: node projects/mig/tools/verify-competitor-discovery-v0.mjs [fixture-path]
 */

import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const migRoot = path.join(__dirname, "..");
const require = createRequire(import.meta.url);

const { discoverFromSerp, formatCompetitorObservationsMarkdown } = require(
  path.join(migRoot, "lib", "competitor-discovery", "discover-from-serp.js")
);
const {
  buildCompetitorsArtifact,
  writeCompetitorsArtifact,
  deriveDiscoveryManifestMeta,
  ARTIFACT_SCHEMA_VERSION,
} = require(path.join(migRoot, "lib", "competitor-discovery", "write-competitors-artifact.js"));
const { buildResearchPackDraft } = require(
  path.join(migRoot, "lib", "session-spine", "build-research-pack.js")
);
const { finalizeManifest } = require(
  path.join(migRoot, "lib", "session-spine", "create-manifest.js")
);

const fixturePath =
  process.argv[2] ||
  path.join(migRoot, "test", "test-payload-competitor-discovery-v0.1.json");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function validateSection(section) {
  assert(section.section_id === "competitor_observations", "section_id mismatch");
  assert(section.schema_version === "0", "schema_version mismatch");
  assert(section.discovery_phase === 2, "discovery_phase must be 2");
  assert(Array.isArray(section.competitors), "competitors must be array");
  assert(section.section_evidence_grade, "section_evidence_grade required");
  assert(section.section_coverage, "section_coverage required");

  for (const c of section.competitors) {
    assert(c.competitor_id, "competitor_id required");
    assert(c.display_name, "display_name required");
    assert(c.discovery_rules_fired?.length, `rules required for ${c.competitor_id}`);
    assert(c.evidence?.length, `evidence required for ${c.competitor_id}`);
    assert(["single", "repeated", "multi_surface"].includes(c.discovery_strength), "discovery_strength enum");
  }
}

function validateArtifact(artifact) {
  assert(artifact.schema_version === ARTIFACT_SCHEMA_VERSION, "artifact schema_version");
  assert(artifact.session_id, "artifact session_id required");
  assert(artifact.generated_at, "artifact generated_at required");
  assert(artifact.discovery_phase === 2, "artifact discovery_phase");
  assert(artifact.competitor_observations, "competitor_observations wrapper required");
  validateSection(artifact.competitor_observations);
}

function collectRulesFired(section) {
  const set = new Set();
  for (const c of section.competitors) {
    for (const rule of c.discovery_rules_fired) {
      set.add(rule);
    }
  }
  return [...set].sort();
}

function main() {
  const raw = JSON.parse(fs.readFileSync(fixturePath, "utf8"));
  const serpResult = raw.serp_result;
  assert(serpResult, "fixture must contain serp_result");

  const section = discoverFromSerp(serpResult);
  validateSection(section);

  const expectations = raw.expectations || {};
  if (expectations.min_competitors != null) {
    assert(
      section.competitors.length >= expectations.min_competitors,
      `expected >= ${expectations.min_competitors} competitors, got ${section.competitors.length}`
    );
  }

  if (Array.isArray(expectations.excluded_domains)) {
    for (const domain of expectations.excluded_domains) {
      const hit = section.competitors.find((c) => c.primary_domain === domain);
      assert(!hit, `domain ${domain} should be excluded but was discovered`);
    }
  }

  const rulesFired = collectRulesFired(section);
  if (Array.isArray(expectations.rules_expected)) {
    for (const rule of expectations.rules_expected) {
      assert(rulesFired.includes(rule), `expected rule not fired: ${rule}`);
    }
  }

  const artifact = buildCompetitorsArtifact(serpResult.session_id, section, {
    generated_at: section.discovery_pass_at,
  });
  validateArtifact(artifact);

  const tmpDir = fs.mkdtempSync(path.join(migRoot, "test", ".verify-competitors-"));
  const written = writeCompetitorsArtifact(tmpDir, artifact);
  assert(fs.existsSync(written.path), "competitors.json must be written");
  const onDisk = JSON.parse(fs.readFileSync(written.path, "utf8"));
  validateArtifact(onDisk);
  assert(
    onDisk.competitor_observations.competitors.length === section.competitors.length,
    "on-disk competitor count must match discovery"
  );

  const manifest = {
    schema_version: "0.1",
    session_id: serpResult.session_id,
    created_at: serpResult.captured_at,
    updated_at: serpResult.captured_at,
    stage: "intake_complete",
    operator_id: "verify-competitor-discovery",
    scope: {
      niche: "manipulator rental",
      region: serpResult.region,
      city: serpResult.city,
      business_type: "local_service",
      search_engine: serpResult.search_engine,
      device: serpResult.device,
    },
    queries: {
      seed_queries: [serpResult.query],
      query_used: serpResult.query,
    },
    serp: { mode: serpResult.source_mode, captured_at: serpResult.captured_at, result_file: "serp_result.json" },
    artifacts: {
      session_manifest: "session_manifest.json",
      serp_result: "serp_result.json",
      competitors: "competitors.json",
      research_pack_draft: "research_pack.draft.md",
    },
    safe_unknown: [],
  };

  const competitorMeta = deriveDiscoveryManifestMeta(artifact);
  const finalManifest = finalizeManifest(
    manifest,
    {
      mode: serpResult.source_mode,
      captured_at: serpResult.captured_at,
      safe_unknown: serpResult.safe_unknown || [],
    },
    competitorMeta
  );

  assert(finalManifest.competitor_discovery, "manifest must include competitor_discovery");
  assert(
    finalManifest.competitor_discovery.competitor_count === section.competitors.length,
    "manifest competitor_count must match artifact"
  );
  assert(
    finalManifest.artifacts.competitors === "competitors.json",
    "manifest artifacts.competitors path"
  );
  assert(finalManifest.mig_phase === (section.competitors.length > 0 ? "2" : "1"), "manifest mig_phase");

  const packMd = buildResearchPackDraft(finalManifest, serpResult, {
    competitor_observations: section,
    competitors_artifact_file: "competitors.json",
  });
  assert(packMd.includes("## Competitor Observations"), "pack must include Competitor Observations");
  assert(packMd.includes("## Artifact Registry"), "pack must include Artifact Registry");
  assert(packMd.includes("competitors.json"), "pack must reference competitors.json");
  assert(
    packMd.includes(`| Competitor count | ${section.competitors.length} |`),
    "pack competitor count must match artifact"
  );

  const previewStart = packMd.indexOf("## Competitor Observations");
  const previewEnd = packMd.indexOf("## Artifact Registry", previewStart);
  const packSectionPreview = packMd.slice(previewStart, previewEnd > 0 ? previewEnd : previewStart + 1200);

  const registryStart = packMd.indexOf("## Artifact Registry");
  const registryEnd = packMd.indexOf("## SAFE UNKNOWN", registryStart);
  const registryPreview = packMd.slice(
    registryStart,
    registryEnd > 0 ? registryEnd : registryStart + 800
  );

  const safeUnknownLines = [
    ...(section.safe_unknown || []),
    ...(section.competitors.length === 0 ? ["(empty competitors — section SAFE UNKNOWN)"] : []),
  ];

  try {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  } catch {
    /* ignore cleanup errors */
  }

  const output = {
    status: "ok",
    verification: "v0.2b-artifact-integration",
    fixture: fixturePath,
    input_summary: {
      session_id: serpResult.session_id,
      query: serpResult.query,
      source_mode: serpResult.source_mode,
      organic_count: serpResult.organic_results?.length ?? 0,
      region: serpResult.region,
    },
    artifact_summary: {
      schema_version: artifact.schema_version,
      generated_at: artifact.generated_at,
      discovery_phase: artifact.discovery_phase,
      competitor_count: section.competitors.length,
    },
    manifest_summary: {
      mig_phase: finalManifest.mig_phase,
      competitor_discovery: finalManifest.competitor_discovery,
    },
    output_summary: {
      competitor_count: section.competitors.length,
      section_evidence_grade: section.section_evidence_grade,
      section_coverage: section.section_coverage,
      rules_fired: rulesFired,
    },
    safe_unknown: safeUnknownLines.length ? safeUnknownLines : ["none at section level"],
    competitors: section.competitors.map((c) => ({
      competitor_id: c.competitor_id,
      display_name: c.display_name,
      primary_domain: c.primary_domain,
      surface_types: c.surface_types,
      discovery_strength: c.discovery_strength,
      discovery_rules_fired: c.discovery_rules_fired,
      evidence_grade: c.evidence_grade,
    })),
    research_pack_section_preview: packSectionPreview.trim(),
    artifact_registry_preview: registryPreview.trim(),
  };

  console.log(JSON.stringify(output, null, 2));
}

try {
  main();
} catch (err) {
  console.error(
    JSON.stringify(
      {
        status: "error",
        message: err.message,
      },
      null,
      2
    )
  );
  process.exit(1);
}
