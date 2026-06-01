#!/usr/bin/env node
/**
 * Local verification for MIG Multi-Query Discovery v0.3.
 * Usage: node projects/mig/tools/verify-multi-query-discovery-v0.mjs [fixture-path]
 */

import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const migRoot = path.join(__dirname, "..");
const require = createRequire(import.meta.url);

const { discoverFromSerp } = require(
  path.join(migRoot, "lib", "competitor-discovery", "discover-from-serp.js")
);
const {
  discoverFromSerpBundle,
  synthesizeLegacyIndex,
} = require(path.join(migRoot, "lib", "competitor-discovery", "discover-from-serp-bundle.js"));
const {
  buildCompetitorsArtifact,
  writeCompetitorsArtifact,
  deriveDiscoveryManifestMeta,
} = require(path.join(migRoot, "lib", "competitor-discovery", "write-competitors-artifact.js"));
const { buildResearchPackDraft } = require(
  path.join(migRoot, "lib", "session-spine", "build-research-pack.js")
);
const { finalizeManifest } = require(
  path.join(migRoot, "lib", "session-spine", "create-manifest.js")
);

const fixturePath =
  process.argv[2] ||
  path.join(migRoot, "test", "test-payload-multi-query-discovery-v0.1.json");

const legacyFixturePath = path.join(migRoot, "test", "test-payload-competitor-discovery-v0.1.json");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function validateSection(section, { requireCoverage = false } = {}) {
  assert(section.section_id === "competitor_observations", "section_id mismatch");
  assert(section.discovery_phase === 2, "discovery_phase must be 2");
  assert(Array.isArray(section.competitors), "competitors must be array");

  if (requireCoverage) {
    assert(section.discovery_coverage, "discovery_coverage required for multi-query");
    assert(
      ["full", "partial", "none"].includes(section.discovery_coverage.query_coverage),
      "query_coverage enum"
    );
  }

  for (const c of section.competitors) {
    assert(c.competitor_id, "competitor_id required");
    assert(c.discovery_rules_fired?.length, `rules required for ${c.competitor_id}`);
    assert(c.evidence?.length, `evidence required for ${c.competitor_id}`);
  }
}

function collectRepeatedDomains(section) {
  return section.competitors
    .filter((c) => c.discovery_rules_fired?.includes("rule_repeated_domain"))
    .map((c) => c.primary_domain)
    .filter(Boolean);
}

function runMultiQueryFixture(raw) {
  const serpIndex = raw.serp_index;
  const serpResults = raw.serp_results;
  assert(serpIndex, "fixture must contain serp_index");
  assert(serpResults, "fixture must contain serp_results");

  const section = discoverFromSerpBundle(serpIndex, { serp_results: serpResults });
  validateSection(section, { requireCoverage: true });

  const expectations = raw.expectations || {};
  if (expectations.min_competitors != null) {
    assert(
      section.competitors.length >= expectations.min_competitors,
      `expected >= ${expectations.min_competitors} competitors, got ${section.competitors.length}`
    );
  }

  if (expectations.query_coverage) {
    assert(
      section.discovery_coverage.query_coverage === expectations.query_coverage,
      `expected query_coverage ${expectations.query_coverage}, got ${section.discovery_coverage.query_coverage}`
    );
  }

  if (Array.isArray(expectations.repeated_domains)) {
    const repeated = collectRepeatedDomains(section);
    for (const domain of expectations.repeated_domains) {
      assert(repeated.includes(domain), `expected repeated domain: ${domain}`);
      const entity = section.competitors.find((c) => c.primary_domain === domain);
      assert(entity.recurrence, `recurrence block required for ${domain}`);
      assert(
        entity.recurrence.distinct_query_count >= 2,
        `recurrence.distinct_query_count >= 2 for ${domain}`
      );
      assert(
        entity.discovery_strength === "repeated" || entity.discovery_strength === "multi_surface",
        `discovery_strength repeated/multi_surface for ${domain}`
      );
    }
  }

  if (Array.isArray(expectations.excluded_domains)) {
    for (const domain of expectations.excluded_domains) {
      const hit = section.competitors.find((c) => c.primary_domain === domain);
      assert(!hit, `domain ${domain} should be excluded`);
    }
  }

  const rulesFired = new Set();
  for (const c of section.competitors) {
    for (const rule of c.discovery_rules_fired) {
      rulesFired.add(rule);
    }
  }
  if (Array.isArray(expectations.rules_expected)) {
    for (const rule of expectations.rules_expected) {
      assert(rulesFired.has(rule), `expected rule not fired: ${rule}`);
    }
  }

  const artifact = buildCompetitorsArtifact(raw.session_id, section, {
    generated_at: section.discovery_pass_at,
  });
  assert(artifact.discovery_mode === "multi_query", "artifact discovery_mode multi_query");

  const tmpDir = fs.mkdtempSync(path.join(migRoot, "test", ".verify-mq-"));
  const written = writeCompetitorsArtifact(tmpDir, artifact);
  const onDisk = JSON.parse(fs.readFileSync(written.path, "utf8"));
  assert(onDisk.competitor_observations.discovery_coverage, "on-disk discovery_coverage");

  const primarySerp = serpResults.q01 || Object.values(serpResults)[0];
  const manifest = {
    schema_version: "0.1",
    session_id: raw.session_id,
    created_at: primarySerp.captured_at,
    updated_at: primarySerp.captured_at,
    stage: "intake_complete",
    operator_id: "verify-multi-query",
    scope: {
      niche: "manipulator rental",
      region: primarySerp.region,
      city: primarySerp.city,
      business_type: "local_service",
      search_engine: primarySerp.search_engine,
      device: primarySerp.device,
    },
    queries: {
      seed_queries: serpIndex.query_set?.map((q) => q.query_text) || [],
      query_used: primarySerp.query,
      queries_executed: serpIndex.queries_executed,
      query_set: serpIndex.query_set,
    },
    serp: { mode: primarySerp.source_mode, captured_at: primarySerp.captured_at },
    artifacts: {
      serp_index: "serp_index.json",
      serp_results_dir: "serp_results/",
      competitors: "competitors.json",
      research_pack_draft: "research_pack.draft.md",
    },
    safe_unknown: [],
  };

  const finalManifest = finalizeManifest(
    manifest,
    { mode: primarySerp.source_mode, captured_at: primarySerp.captured_at, safe_unknown: [] },
    deriveDiscoveryManifestMeta(artifact)
  );

  const packMd = buildResearchPackDraft(finalManifest, primarySerp, {
    competitor_observations: section,
    discovery_mode: section.discovery_mode,
  });

  assert(packMd.includes("### Discovery coverage"), "pack discovery coverage");
  assert(packMd.includes("### Cross-query recurrence"), "pack recurrence section");
  assert(packMd.includes("manipulator-krd.ru"), "pack mentions repeated domain");

  fs.rmSync(tmpDir, { recursive: true, force: true });

  return {
    section,
    artifact,
    packMd,
    input_queries: serpIndex.entries.map((e) => ({
      query_id: e.query_id,
      query_text: e.query_text,
    })),
    domains_discovered: section.competitors.map((c) => c.primary_domain),
    repeated_domains: collectRepeatedDomains(section),
    coverage: section.discovery_coverage,
  };
}

function runBackwardCompat() {
  const raw = JSON.parse(fs.readFileSync(legacyFixturePath, "utf8"));
  const serpResult = raw.serp_result;
  const legacySection = discoverFromSerp(serpResult);
  validateSection(legacySection, { requireCoverage: false });
  assert(!legacySection.discovery_coverage, "legacy single-query must not add discovery_coverage");

  const legacyIndex = synthesizeLegacyIndex(serpResult);
  const bundleSection = discoverFromSerpBundle(legacyIndex, {
    serp_results: { q01: serpResult },
  });
  validateSection(bundleSection);
  assert(
    bundleSection.competitors.length === legacySection.competitors.length,
    "legacy bundle competitor count must match discoverFromSerp"
  );

  const artifact = buildCompetitorsArtifact(serpResult.session_id, legacySection);
  const packMd = buildResearchPackDraft(
    {
      session_id: serpResult.session_id,
      created_at: serpResult.captured_at,
      operator_id: "compat",
      scope: {
        niche: "test",
        region: serpResult.region,
        city: serpResult.city,
        business_type: "local_service",
        search_engine: serpResult.search_engine,
        device: serpResult.device,
      },
      queries: { seed_queries: [serpResult.query], query_used: serpResult.query },
      artifacts: { competitors: "competitors.json" },
    },
    serpResult,
    { competitor_observations: legacySection }
  );
  assert(packMd.includes("## Competitor Observations"), "legacy pack section");
  assert(
    packMd.includes("cross-query recurrence not evaluated") ||
      packMd.includes("multi-query coverage not computed"),
    "legacy pack SAFE UNKNOWN for recurrence"
  );

  return {
    legacy_competitor_count: legacySection.competitors.length,
    bundle_legacy_count: bundleSection.competitors.length,
    pack_ok: true,
  };
}

function main() {
  const raw = JSON.parse(fs.readFileSync(fixturePath, "utf8"));
  const mq = runMultiQueryFixture(raw);
  const compat = runBackwardCompat();

  const output = {
    status: "ok",
    verification: "v0.3-multi-query-discovery",
    fixture: fixturePath,
    bundle_discovery_summary: {
      discovery_mode: mq.section.discovery_mode,
      competitor_count: mq.section.competitors.length,
      input_queries: mq.input_queries,
      domains_discovered: mq.domains_discovered,
      repeated_domains: mq.repeated_domains,
      coverage: mq.coverage,
      section_evidence_grade: mq.section.section_evidence_grade,
      section_coverage: mq.section.section_coverage,
    },
    rule_repeated_domain_results: mq.section.competitors
      .filter((c) => c.discovery_rules_fired?.includes("rule_repeated_domain"))
      .map((c) => ({
        competitor_id: c.competitor_id,
        primary_domain: c.primary_domain,
        discovery_strength: c.discovery_strength,
        recurrence: c.recurrence,
        queries_seen: c.queries_seen,
      })),
    artifact_summary: {
      schema_version: mq.artifact.schema_version,
      discovery_mode: mq.artifact.discovery_mode,
      competitor_count: mq.artifact.competitor_observations.competitors.length,
    },
    pack_summary: {
      has_discovery_coverage: mq.packMd.includes("### Discovery coverage"),
      has_recurrence: mq.packMd.includes("### Cross-query recurrence"),
      query_coverage_line: mq.packMd.match(/\| Query coverage \| [^|]+ \|/)?.[0] || null,
    },
    backward_compatibility: compat,
  };

  console.log(JSON.stringify(output, null, 2));
}

try {
  main();
} catch (err) {
  console.error(JSON.stringify({ status: "error", message: err.message }, null, 2));
  process.exit(1);
}
