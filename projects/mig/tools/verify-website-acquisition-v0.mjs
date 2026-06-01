#!/usr/bin/env node
/**
 * Local verification for MIG Website Acquisition MVP v0.
 * Usage: node projects/mig/tools/verify-website-acquisition-v0.mjs [fixture-path]
 */

import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { fileURLToPath } from "url";
import { spawnSync } from "child_process";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const migRoot = path.join(__dirname, "..");
const require = createRequire(import.meta.url);

const { buildUrlPlan } = require(path.join(migRoot, "lib", "website-acquisition", "build-url-plan.js"));
const { extractPageFacts } = require(path.join(migRoot, "lib", "website-acquisition", "extract-page-facts.js"));
const { runWebsitePass } = require(path.join(migRoot, "lib", "website-acquisition", "run-website-pass.js"));
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

const fixturePath =
  process.argv[2] ||
  path.join(migRoot, "test", "test-payload-website-acquisition-v0.1.json");
const fixtureRoot = path.join(migRoot, "test", "fixtures", "website-html");

function assert(condition, message) {
  if (!condition) {
    throw new Error(message);
  }
}

function validateSnapshot(snapshot) {
  assert(snapshot.snapshot_id, "snapshot_id required");
  assert(snapshot.session_id, "session_id required");
  assert(snapshot.domain, "domain required");
  assert(snapshot.requested_url, "requested_url required");
  assert(snapshot.final_url, "final_url required");
  assert(snapshot.status, "status required");
  assert(snapshot.render_status, "render_status required");
  assert(Array.isArray(snapshot.headings), "headings array required");
  assert(snapshot.contacts, "contacts required");
  assert(snapshot.artifact_refs?.page_html, "artifact_refs.page_html required");
}

function validateIndex(index) {
  assert(index.schema_version === "0.1", "index schema_version");
  assert(index.acquisition_phase === 3, "acquisition_phase must be 3");
  assert(Array.isArray(index.url_plan), "url_plan required");
  assert(Array.isArray(index.snapshots), "snapshots required");
  assert(index.section_evidence_grade, "section_evidence_grade required");
}

function runExtractionFixtureChecks() {
  const expectedPath = path.join(fixtureRoot, "expected-extraction.json");
  const expected = JSON.parse(fs.readFileSync(expectedPath, "utf8"));

  for (const [file, rules] of Object.entries(expected)) {
    const html = fs.readFileSync(path.join(fixtureRoot, file), "utf8");
    const facts = extractPageFacts(html, `https://fixture.local/${file}`);
    if (rules.title) {
      assert(facts.title === rules.title, `${file}: title mismatch`);
    }
    if (rules.phones_min != null) {
      assert(
        facts.contacts.phones.length >= rules.phones_min,
        `${file}: expected >= ${rules.phones_min} phones`
      );
    }
    if (rules.emails_min != null) {
      assert(
        facts.contacts.emails.length >= rules.emails_min,
        `${file}: expected >= ${rules.emails_min} emails`
      );
    }
    if (rules.forms_min != null) {
      assert(facts.forms.length >= rules.forms_min, `${file}: forms`);
    }
    if (rules.pricing_signals_min != null) {
      assert(
        facts.pricing_signals.length >= rules.pricing_signals_min,
        `${file}: pricing_signals`
      );
    }
    if (rules.cta_elements_min != null) {
      assert(facts.cta_elements.length >= rules.cta_elements_min, `${file}: cta_elements`);
    }
    if (rules.render_status) {
      assert(facts.render_status === rules.render_status, `${file}: render_status`);
    }
    if (rules.acquisition_status) {
      assert(facts.acquisition_status === rules.acquisition_status, `${file}: acquisition_status`);
    }
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
  assert(packWithoutWebsite.includes("## Competitor Observations"), "pack without website: competitors");
  assert(
    packWithoutWebsite.includes("Website acquisition not executed"),
    "pack without website: SAFE UNKNOWN"
  );

  return {
    competitor_discovery: "ok",
    multi_query_discovery: "ok",
    research_pack_without_website: "ok",
  };
}

async function main() {
  runExtractionFixtureChecks();

  const raw = JSON.parse(fs.readFileSync(fixturePath, "utf8"));
  const competitorsArtifact = raw.competitors_artifact;
  assert(competitorsArtifact, "fixture must contain competitors_artifact");

  const urlPlan = buildUrlPlan(competitorsArtifact, { url_cap: 5 });
  const expectations = raw.expectations || {};

  if (expectations.planned_urls != null) {
    assert(urlPlan.planned_count === expectations.planned_urls, "url plan count");
  }
  if (expectations.skipped_aggregators != null) {
    const skippedAgg = urlPlan.skipped.filter((s) => s.reason === "skip_surface_type");
    assert(skippedAgg.length >= expectations.skipped_aggregators, "aggregator skip");
  }

  const tmpDir = fs.mkdtempSync(path.join(migRoot, "test", ".verify-website-"));
  fs.writeFileSync(
    path.join(tmpDir, "competitors.json"),
    `${JSON.stringify(competitorsArtifact, null, 2)}\n`,
    "utf8"
  );

  const fixtureMap = {};
  for (const [url, file] of Object.entries(raw.fixture_map || {})) {
    fixtureMap[url] = path.join(fixtureRoot, file);
  }

  const passResult = await runWebsitePass(tmpDir, {
    competitorsArtifact,
    fixtureRoot,
    fixtureMap,
  });

  validateIndex(passResult.index);
  assert(
    passResult.snapshots.length >= (expectations.min_snapshots ?? 1),
    "snapshot count"
  );

  for (const snapshot of passResult.snapshots) {
    validateSnapshot(snapshot);
    const snapPath = path.join(
      tmpDir,
      "snapshots",
      "sites",
      snapshot.snapshot_id,
      "website_snapshot.json"
    );
    assert(fs.existsSync(snapPath), `missing ${snapPath}`);
    assert(fs.existsSync(path.join(path.dirname(snapPath), "page.html")), "page.html missing");
    assert(fs.existsSync(path.join(path.dirname(snapPath), "headers.json")), "headers.json missing");
  }

  const phones = passResult.snapshots.flatMap((s) => s.contacts?.phones || []);
  const forms = passResult.snapshots.flatMap((s) => s.forms || []);
  const pricing = passResult.snapshots.flatMap((s) => s.pricing_signals || []);
  const ctas = passResult.snapshots.flatMap((s) => s.cta_elements || []);

  if (expectations.min_phones != null) {
    assert(phones.length >= expectations.min_phones, "phones found");
  }
  if (expectations.min_forms != null) {
    assert(forms.length >= expectations.min_forms, "forms found");
  }
  if (expectations.min_pricing_signals != null) {
    assert(pricing.length >= expectations.min_pricing_signals, "pricing signals");
  }
  if (expectations.min_cta_elements != null) {
    assert(ctas.length >= expectations.min_cta_elements, "cta elements");
  }

  const manifest = finalizeManifest(
    {
      schema_version: "0.1",
      session_id: raw.session_id,
      created_at: competitorsArtifact.generated_at,
      operator_id: "verify-website-acquisition",
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
  manifest.artifacts.website_snapshots = "website_snapshots.json";

  const packMd = buildResearchPackDraft(manifest, raw.serp_result, {
    competitor_observations: competitorsArtifact.competitor_observations,
    website_snapshots: passResult.index,
    mig_phase: "3",
  });

  assert(packMd.includes("## Website capture summary"), "pack website summary");
  assert(packMd.includes("## Website observations"), "pack website observations");
  assert(packMd.includes("## Offer observations"), "pack offer observations");
  assert(packMd.includes("## CTA observations"), "pack CTA observations");
  assert(packMd.includes("## Trust observations"), "pack trust observations");
  assert(packMd.includes("website_snapshots.json"), "pack registry website_snapshots");

  const backward = runBackwardCompatibility();

  const compVerify = spawnSync(
    process.execPath,
    [path.join(migRoot, "tools", "verify-competitor-discovery-v0.mjs")],
    { encoding: "utf8" }
  );
  const mqVerify = spawnSync(
    process.execPath,
    [path.join(migRoot, "tools", "verify-multi-query-discovery-v0.mjs")],
    { encoding: "utf8" }
  );

  backward.verify_competitor_discovery_script =
    compVerify.status === 0 ? "ok" : `exit ${compVerify.status}`;
  backward.verify_multi_query_script = mqVerify.status === 0 ? "ok" : `exit ${mqVerify.status}`;

  try {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  } catch {
    /* ignore */
  }

  const exampleSnapshot = passResult.snapshots[0];
  const websiteObsStart = packMd.indexOf("## Website observations");
  const websiteObsEnd = packMd.indexOf("## Offer observations", websiteObsStart);
  const websiteObsPreview = packMd.slice(
    websiteObsStart,
    websiteObsEnd > 0 ? websiteObsEnd : websiteObsStart + 800
  );

  const output = {
    status: "ok",
    verification: "website-acquisition-mvp-v0",
    fixture: fixturePath,
    url_plan_summary: {
      planned_count: urlPlan.planned_count,
      url_cap: urlPlan.url_cap,
      skipped: urlPlan.skipped,
      urls: urlPlan.entries.map((e) => e.requested_url),
    },
    acquisition_summary: {
      snapshots_generated: passResult.snapshots.length,
      urls_processed: passResult.snapshots.map((s) => ({
        snapshot_id: s.snapshot_id,
        requested_url: s.requested_url,
        final_url: s.final_url,
        status: s.status,
        http_status: s.http_status,
      })),
      contacts_found: { phones: phones.length, emails: passResult.snapshots.flatMap((s) => s.contacts?.emails || []).length },
      pricing_signals_found: pricing.length,
      forms_found: forms.length,
      cta_elements_found: ctas.length,
      session_coverage: passResult.index.session_coverage,
      section_evidence_grade: passResult.index.section_evidence_grade,
    },
    pack_output_summary: {
      mig_phase: "3",
      sections_present: [
        "Website capture summary",
        "Website observations",
        "Offer observations",
        "CTA observations",
        "Trust observations",
      ],
      website_observations_preview: websiteObsPreview.trim(),
    },
    example_snapshot: {
      snapshot_id: exampleSnapshot.snapshot_id,
      title: exampleSnapshot.title,
      status: exampleSnapshot.status,
      contacts: exampleSnapshot.contacts,
      pricing_signals: exampleSnapshot.pricing_signals.slice(0, 3),
      forms_count: exampleSnapshot.forms.length,
      cta_elements: exampleSnapshot.cta_elements.slice(0, 3),
    },
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
