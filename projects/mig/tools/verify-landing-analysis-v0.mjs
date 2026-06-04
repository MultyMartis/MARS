#!/usr/bin/env node
/**
 * Local verification for MIG Landing Analysis MVP v0.
 * Usage: node projects/mig/tools/verify-landing-analysis-v0.mjs [website-acquisition-fixture-path]
 */

import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { fileURLToPath } from "url";
import { spawnSync } from "child_process";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const migRoot = path.join(__dirname, "..");
const require = createRequire(import.meta.url);

const { extractPageFacts } = require(path.join(migRoot, "lib", "website-acquisition", "extract-page-facts.js"));
const { runWebsitePass } = require(path.join(migRoot, "lib", "website-acquisition", "run-website-pass.js"));
const { runLandingPass, analyzeSnapshot } = require(
  path.join(migRoot, "lib", "landing-analysis", "run-landing-pass.js")
);
const { buildResearchPackDraft } = require(
  path.join(migRoot, "lib", "session-spine", "build-research-pack.js")
);
const { discoverFromSerp } = require(
  path.join(migRoot, "lib", "competitor-discovery", "discover-from-serp.js")
);
const { discoverFromSerpBundle } = require(
  path.join(migRoot, "lib", "competitor-discovery", "discover-from-serp-bundle.js")
);
const { finalizeManifest } = require(path.join(migRoot, "lib", "session-spine", "create-manifest.js"));
const { landingIdFor, loadBlockRegistry } = require(path.join(migRoot, "lib", "landing-analysis", "utils.js"));

const websiteFixturePath =
  process.argv[2] ||
  path.join(migRoot, "test", "test-payload-website-acquisition-v0.1.json");
const fixtureRoot = path.join(migRoot, "test", "fixtures", "website-html");
const landingExpectedPath = path.join(
  migRoot,
  "test",
  "fixtures",
  "landing-analysis",
  "expected-landing-analysis.json"
);

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function validateLandingObservation(obs) {
  assert(obs.landing_id, "landing_id required");
  assert(obs.snapshot_id, "snapshot_id required");
  assert(obs.page_type, "page_type required");
  if (obs.analysis_phase === "landing_analysis_v2") {
    assert(obs.schema_version === "0.2", "detail schema_version 0.2");
    assert(Array.isArray(obs.observations), "observations[] required for v2");
    assert(obs.observation_summary, "observation_summary required for v2");
    for (const o of obs.observations) {
      assert(o.observation_id && o.family && o.text !== undefined, "observation shape");
      assert(/^(A|B|C|X)$/.test(o.confidence), "observation confidence A|B|C|X");
      assert(o.evidence, "observation evidence required");
    }
  }
  assert(Array.isArray(obs.visible_blocks), "visible_blocks required");
  assert(Array.isArray(obs.offers), "offers required");
  assert(Array.isArray(obs.cta_patterns), "cta_patterns required");
  assert(Array.isArray(obs.trust_patterns), "trust_patterns required");
  assert(Array.isArray(obs.pricing_patterns), "pricing_patterns required");
  assert(Array.isArray(obs.contact_patterns), "contact_patterns required");
  assert(Array.isArray(obs.form_patterns), "form_patterns required");
  assert(obs.artifact_refs?.landing_observation, "artifact_refs.landing_observation required");
  for (const block of obs.visible_blocks) {
    assert(block.block_id && block.block_type, "block_id and block_type required");
    assert(block.detection_method, "detection_method required");
    assert(!("confidence" in block), "confidence must not be used on blocks");
  }
}

function validateLandingIndex(index) {
  assert(index.schema_version === "0.1" || index.schema_version === "0.2", "index schema_version");
  assert(
    index.analysis_phase === "landing_analysis_v1" || index.analysis_phase === "landing_analysis_v2",
    "analysis_phase"
  );
  assert(Array.isArray(index.landings), "landings array required");
  assert(index.section_evidence_grade, "section_evidence_grade required");
  if (index.analysis_phase === "landing_analysis_v2") {
    for (const row of index.landings) {
      assert(row.observation_summary, "observation_summary per landing");
      assert(row._derived, "_derived debug counts");
    }
  }
}

function runUnitFixtureChecks() {
  const expected = JSON.parse(fs.readFileSync(landingExpectedPath, "utf8"));
  const registry = loadBlockRegistry();
  const sessionId = "mig-fixture-la";

  for (const [file, rules] of Object.entries(expected)) {
    const html = fs.readFileSync(path.join(fixtureRoot, file), "utf8");
    const facts = extractPageFacts(html, `https://fixture.local/${file}`);
    const snapshot = {
      snapshot_id: `${sessionId}-snap-${file}`,
      session_id: sessionId,
      competitor_id: null,
      domain: "fixture.local",
      final_url: `https://fixture.local/${file}`,
      page_role: file === "contact-only.html" ? "contact" : "homepage",
      capture_time: "2026-06-01T12:00:00.000Z",
      status: facts.acquisition_status === "render_required" ? "render_required" : "success",
      render_status: facts.render_status,
      headings: facts.headings,
      contacts: facts.contacts,
      offers: facts.offers,
      pricing_signals: facts.pricing_signals,
      cta_elements: facts.cta_elements,
      forms: facts.forms,
      trust_signals_visible: facts.trust_signals_visible,
      artifact_refs: {
        page_html: `snapshots/sites/${sessionId}-snap-${file}/page.html`,
      },
      evidence_grade: "B",
    };

    const tmpDir = fs.mkdtempSync(path.join(migRoot, "test", ".verify-la-unit-"));
    const snapDir = path.join(tmpDir, "snapshots", "sites", snapshot.snapshot_id);
    fs.mkdirSync(snapDir, { recursive: true });
    fs.writeFileSync(path.join(snapDir, "page.html"), html, "utf8");

    const obs = analyzeSnapshot(snapshot, tmpDir, {
      landing_id: landingIdFor(sessionId, 1),
      registry,
    });

    if (rules.render_status) {
      assert(snapshot.render_status === rules.render_status, `${file}: render_status`);
    }
    if (rules.min_blocks != null) {
      assert(obs.visible_blocks.length >= rules.min_blocks, `${file}: min_blocks`);
    }
    if (rules.required_block_types) {
      const types = new Set(obs.visible_blocks.map((b) => b.block_type));
      for (const t of rules.required_block_types) {
        assert(types.has(t), `${file}: missing block ${t}`);
      }
    }
    if (rules.min_offers != null) {
      assert(obs.offers.length >= rules.min_offers, `${file}: min_offers`);
    }
    if (rules.min_cta_patterns != null) {
      assert(obs.cta_patterns.length >= rules.min_cta_patterns, `${file}: min_cta_patterns`);
    }
    if (rules.min_trust_patterns != null) {
      assert(obs.trust_patterns.length >= rules.min_trust_patterns, `${file}: min_trust_patterns`);
    }
    if (rules.min_pricing_patterns != null) {
      assert(obs.pricing_patterns.length >= rules.min_pricing_patterns, `${file}: min_pricing_patterns`);
    }
    if (rules.min_form_patterns != null) {
      assert(obs.form_patterns.length >= rules.min_form_patterns, `${file}: min_form_patterns`);
    }
    if (rules.page_type) {
      assert(obs.page_type === rules.page_type, `${file}: page_type expected ${rules.page_type} got ${obs.page_type}`);
    }

    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
}

function runBackwardCompatibility() {
  const competitorFixture = path.join(migRoot, "test", "test-payload-competitor-discovery-v0.1.json");
  const multiFixture = path.join(migRoot, "test", "test-payload-multi-query-discovery-v0.1.json");

  const compRaw = JSON.parse(fs.readFileSync(competitorFixture, "utf8"));
  const compSection = discoverFromSerp(compRaw.serp_result);
  assert(compSection.section_id === "competitor_observations", "competitor discovery regression");

  const mqRaw = JSON.parse(fs.readFileSync(multiFixture, "utf8"));
  const mqSection = discoverFromSerpBundle(mqRaw.serp_index, { serp_results: mqRaw.serp_results });
  assert(mqSection.discovery_coverage, "multi-query discovery_coverage regression");

  const manifest = {
    schema_version: "0.1",
    session_id: compRaw.serp_result.session_id,
    created_at: compRaw.serp_result.captured_at,
    operator_id: "verify",
    scope: {
      niche: "test",
      region: compRaw.serp_result.region,
      business_type: "local_service",
      search_engine: compRaw.serp_result.search_engine,
      device: compRaw.serp_result.device,
    },
    queries: { seed_queries: [compRaw.serp_result.query], query_used: compRaw.serp_result.query },
    artifacts: {
      serp_result: "serp_result.json",
      competitors: "competitors.json",
      research_pack_draft: "research_pack.draft.md",
    },
  };
  const packWithoutWebsite = buildResearchPackDraft(manifest, compRaw.serp_result, {
    competitor_observations: compSection,
  });
  assert(packWithoutWebsite.includes("Website acquisition not executed"), "pack without website");

  const compVerify = spawnSync(process.execPath, [path.join(migRoot, "tools", "verify-competitor-discovery-v0.mjs")], {
    encoding: "utf8",
  });
  const mqVerify = spawnSync(process.execPath, [path.join(migRoot, "tools", "verify-multi-query-discovery-v0.mjs")], {
    encoding: "utf8",
  });
  const waVerify = spawnSync(process.execPath, [path.join(migRoot, "tools", "verify-website-acquisition-v0.mjs")], {
    encoding: "utf8",
  });

  return {
    competitor_discovery: "ok",
    multi_query_discovery: "ok",
    research_pack_without_website: "ok",
    verify_competitor_discovery_script: compVerify.status === 0 ? "ok" : `exit ${compVerify.status}`,
    verify_multi_query_script: mqVerify.status === 0 ? "ok" : `exit ${mqVerify.status}`,
    verify_website_acquisition_script: waVerify.status === 0 ? "ok" : `exit ${waVerify.status}`,
  };
}

function attachLandingDetails(sessionDir, index) {
  const detail = [];
  for (const row of index.landings) {
    const p = path.join(sessionDir, row.artifact_ref);
    detail.push(JSON.parse(fs.readFileSync(p, "utf8")));
  }
  return { ...index, _detail: detail };
}

async function main() {
  runUnitFixtureChecks();

  const raw = JSON.parse(fs.readFileSync(websiteFixturePath, "utf8"));
  const competitorsArtifact = raw.competitors_artifact;
  assert(competitorsArtifact, "fixture must contain competitors_artifact");

  const tmpDir = fs.mkdtempSync(path.join(migRoot, "test", ".verify-landing-"));
  fs.writeFileSync(
    path.join(tmpDir, "competitors.json"),
    `${JSON.stringify(competitorsArtifact, null, 2)}\n`,
    "utf8"
  );

  const fixtureMap = {};
  for (const [url, file] of Object.entries(raw.fixture_map || {})) {
    fixtureMap[url] = path.join(fixtureRoot, file);
  }

  const websitePass = await runWebsitePass(tmpDir, {
    competitorsArtifact,
    fixtureRoot,
    fixtureMap,
  });

  const landingPass = runLandingPass(tmpDir);
  validateLandingIndex(landingPass.index);

  for (const obs of landingPass.landings) {
    validateLandingObservation(obs);
    const artifactPath = path.join(tmpDir, "landings", obs.landing_id, "landing_observation.json");
    assert(fs.existsSync(artifactPath), `missing ${artifactPath}`);
  }

  assert(fs.existsSync(path.join(tmpDir, "landing_observations.json")), "landing_observations.json missing");

  const landingIndexWithDetail = attachLandingDetails(tmpDir, landingPass.index);

  const manifest = finalizeManifest(
    {
      schema_version: "0.1",
      session_id: raw.session_id,
      created_at: competitorsArtifact.generated_at,
      operator_id: "verify-landing-analysis",
      scope: {
        niche: "manipulator rental",
        region: "Krasnodar Krai",
        business_type: "local_service",
        search_engine: "yandex",
        device: "mobile",
      },
      queries: { seed_queries: ["аренда манипулятора Краснодар"], query_used: "аренда манипулятора Краснодар" },
      artifacts: {
        serp_result: "serp_result.json",
        competitors: "competitors.json",
        website_snapshots: "website_snapshots.json",
        landing_observations: "landing_observations.json",
        research_pack_draft: "research_pack.draft.md",
      },
    },
    { mode: raw.serp_result.source_mode, captured_at: raw.serp_result.captured_at, safe_unknown: [] },
    {
      status: "complete",
      competitor_count: competitorsArtifact.competitor_observations.competitors.length,
      generated_at: competitorsArtifact.generated_at,
      discovery_pass_at: competitorsArtifact.competitor_observations.discovery_pass_at,
      artifact_file: "competitors.json",
    }
  );
  manifest.mig_phase = "3";

  const packWithLanding = buildResearchPackDraft(manifest, raw.serp_result, {
    competitor_observations: competitorsArtifact.competitor_observations,
    website_snapshots: websitePass.index,
    landing_observations: landingIndexWithDetail,
    mig_phase: "3",
  });

  const packIsV2 = landingPass.index.analysis_phase === "landing_analysis_v2";
  if (packIsV2) {
    assert(packWithLanding.includes("## Landing intelligence —"), "pack v2 intelligence card");
    assert(packWithLanding.includes("### Value & offers"), "pack v2 offers section");
  } else {
    assert(packWithLanding.includes("## Landing observations (structured)"), "pack landing section");
    assert(packWithLanding.includes("## Offer observations"), "pack offers from landing");
  }
  assert(packWithLanding.includes("landing_observations.json"), "pack registry landing_observations");
  assert(!packWithLanding.includes("legacy snapshot projection used"), "should not use legacy when landing exists");

  const packLegacy = buildResearchPackDraft(manifest, raw.serp_result, {
    competitor_observations: competitorsArtifact.competitor_observations,
    website_snapshots: websitePass.index,
    mig_phase: "3",
  });
  assert(
    packLegacy.includes("structured landing analysis pending"),
    "legacy fallback SAFE UNKNOWN when no landing index"
  );

  const backward = runBackwardCompatibility();

  const blockTypes = landingPass.landings.flatMap((l) => l.visible_blocks.map((b) => b.block_type));
  const exampleObs = landingPass.landings.find((l) => l.offers.length > 0) || landingPass.landings[0];

  try {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  } catch {
    /* ignore */
  }

  const output = {
    status: "ok",
    verification: "landing-analysis-mvp-v0",
    landing_count: landingPass.landings.length,
    blocks_detected: blockTypes.length,
    block_types: [...new Set(blockTypes)],
    offers_detected: landingPass.landings.reduce((n, l) => n + l.offers.length, 0),
    cta_patterns_detected: landingPass.landings.reduce((n, l) => n + l.cta_patterns.length, 0),
    trust_patterns_detected: landingPass.landings.reduce((n, l) => n + l.trust_patterns.length, 0),
    pricing_patterns_detected: landingPass.landings.reduce((n, l) => n + l.pricing_patterns.length, 0),
    form_patterns_detected: landingPass.landings.reduce((n, l) => n + l.form_patterns.length, 0),
    session_coverage: landingPass.index.session_coverage,
    section_evidence_grade: landingPass.index.section_evidence_grade,
    pack_summary: {
      sections: [
        "Landing observations (structured)",
        "Offer observations",
        "CTA observations",
        "Trust observations",
        "Block observations",
      ],
      uses_landing_artifacts: true,
    },
    example_landing_observation: exampleObs,
    backward_compatibility: backward,
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
