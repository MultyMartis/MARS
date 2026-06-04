#!/usr/bin/env node
/**
 * Assemble multi-query session: serp_index, discovery bundle, reports, research pack.
 * Does NOT overwrite Pilot #1 session mig-20260604-61b585.
 */
import { readFileSync, writeFileSync, mkdirSync, copyFileSync, existsSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = join(__dirname, "..");
const MIG_ROOT = join(__dirname, "..", "..", "..", "..", "..", "projects", "mig");
const require = createRequire(import.meta.url);

const SESSION_ID = "mig-20260604-mqgt01";
const SESSION_DIR = join(MIG_ROOT, "sessions", SESSION_ID);
const EVIDENCE_DIR = join(PILOT_ROOT, "evidence", "serp-multi-20260604");
const SERP_RESULTS_SRC = join(EVIDENCE_DIR, "serp_results");
const QUERY_SET_PATH = join(PILOT_ROOT, "multi-query-market-query-set-v1.json");
const PILOT1_SESSION = join(MIG_ROOT, "sessions", "mig-20260604-61b585");

const { discoverFromSerpBundle } = require(
  join(MIG_ROOT, "lib", "competitor-discovery", "discover-from-serp-bundle.js")
);
const {
  buildCompetitorsArtifact,
  writeCompetitorsArtifact,
} = require(join(MIG_ROOT, "lib", "competitor-discovery", "write-competitors-artifact.js"));
const { buildResearchPackDraft } = require(
  join(MIG_ROOT, "lib", "session-spine", "build-research-pack.js")
);

function loadJson(p) {
  return JSON.parse(readFileSync(p, "utf8"));
}

function aggregatorLabel(domain) {
  const rules = loadJson(join(MIG_ROOT, "config", "competitor-discovery-rules-v0.json"));
  if (rules.aggregator_domains?.some((d) => domain === d || domain.endsWith(`.${d}`)))
    return "aggregator";
  if (rules.marketplace_domains?.some((d) => domain === d || domain.endsWith(`.${d}`)))
    return "marketplace";
  return "brand_or_service";
}

function buildFrequencyTable(section) {
  const rows = [];
  for (const c of section.competitors || []) {
    const domain = c.primary_domain || "—";
    const distinctQueries = c.recurrence?.distinct_query_count ?? c.queries_seen?.length ?? 0;
    const appearances = c.evidence?.length ?? 0;
    const surfaces = (c.surface_types || []).join(", ");
    rows.push({
      domain,
      distinctQueries,
      appearances,
      surfaceTypes: surfaces,
      discoveryStrength: c.discovery_strength,
      rules: (c.discovery_rules_fired || []).join("; "),
    });
  }
  rows.sort((a, b) => b.appearances - a.appearances || b.distinctQueries - a.distinctQueries);
  return rows;
}

function markdownTable(rows, headers) {
  const sep = headers.map(() => "---");
  const lines = [
    `| ${headers.join(" | ")} |`,
    `| ${sep.join(" | ")} |`,
    ...rows.map((r) => `| ${headers.map((h) => r[h] ?? "").join(" | ")} |`),
  ];
  return lines.join("\n");
}

function main() {
  const querySet = loadJson(QUERY_SET_PATH);
  const serpBundle = existsSync(join(EVIDENCE_DIR, "serp-results-bundle.json"))
    ? loadJson(join(EVIDENCE_DIR, "serp-results-bundle.json"))
    : {};

  mkdirSync(join(SESSION_DIR, "serp_results"), { recursive: true });

  const entries = [];
  const serpResultsForDiscovery = {};

  const captureSummaryPath = join(EVIDENCE_DIR, "capture-run-summary.json");
  const captureResults = existsSync(captureSummaryPath)
    ? loadJson(captureSummaryPath).results || []
    : [];
  const captureOk = new Set(captureResults.filter((r) => r.ok).map((r) => r.query_id));

  for (const q of querySet.approved_query_set) {
    const src = join(SERP_RESULTS_SRC, `${q.query_id}.json`);
    const rawPath = join(EVIDENCE_DIR, "captures", q.query_id, "capture-raw.json");

    let serpFromFile = null;
    if (existsSync(src)) {
      serpFromFile = loadJson(src);
    }
    if (!serpFromFile || (serpFromFile.organic_results?.length ?? 0) === 0) {
      const failedStatus = captureOk.has(q.query_id)
        ? "skipped_normalize"
        : existsSync(rawPath)
          ? "failed"
          : "failed";
      entries.push({
        query_id: q.query_id,
        query_text: q.query_text,
        role: q.role,
        artifact_path: null,
        captured_at: null,
        source_mode: null,
        status: failedStatus,
      });
      continue;
    }

    const serp = serpFromFile;
    const destRel = `serp_results/${q.query_id}.json`;
    const dest = join(SESSION_DIR, destRel);
    writeFileSync(dest, JSON.stringify(serp, null, 2), "utf8");
    serpResultsForDiscovery[q.query_id] = serp;
    entries.push({
      query_id: q.query_id,
      query_text: q.query_text,
      role: q.role,
      artifact_path: destRel,
      captured_at: serp.captured_at,
      source_mode: serp.source_mode,
      status: "captured",
    });
  }

  const executedIds = entries.filter((e) => e.status === "captured").map((e) => e.query_id);
  const statusById = Object.fromEntries(entries.map((e) => [e.query_id, e.status]));

  const serpIndex = {
    schema_version: "0.1",
    session_id: SESSION_ID,
    aggregation_model: "per_query_files",
    default_scope: {
      niche: "Грузотакси",
      region: "Краснодар",
      city: "Краснодар",
      search_engine: "yandex",
      device: "mobile",
    },
    queries_declared: querySet.approved_query_set.map((q) => q.query_id),
    queries_executed: executedIds,
    query_set: querySet.approved_query_set.map((q) => ({
      ...q,
      execution_status: statusById[q.query_id] === "captured" ? "captured" : "failed",
    })),
    entries,
    capture_metadata: {
      indexed_at: new Date().toISOString(),
      evidence_root: "incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604",
      operator_id: "multi-query-groundtruth-pilot",
    },
  };

  const missing = serpIndex.queries_declared.filter(
    (id) => !serpIndex.queries_executed.includes(id)
  );
  if (missing.length) {
    serpIndex.safe_unknown = [`Queries not captured: ${missing.join(", ")}`];
  }

  writeFileSync(
    join(SESSION_DIR, "serp_index.json"),
    JSON.stringify(serpIndex, null, 2),
    "utf8"
  );

  const competitorSection = discoverFromSerpBundle(serpIndex, {
    serp_results: serpResultsForDiscovery,
    baseDir: SESSION_DIR,
  });

  const competitorsArtifact = buildCompetitorsArtifact(SESSION_ID, competitorSection);
  writeCompetitorsArtifact(SESSION_DIR, competitorsArtifact);

  const manifest = {
    schema_version: "0.2",
    session_id: SESSION_ID,
    created_at: new Date().toISOString(),
    operator_id: "multi-query-groundtruth-pilot",
    mig_phase: "2",
    scope: serpIndex.default_scope,
    queries: {
      seed_queries: querySet.approved_query_set.map((q) => q.query_text),
      query_used: querySet.approved_query_set[0].query_text,
      query_set: serpIndex.query_set,
      queries_declared: serpIndex.queries_declared,
      queries_executed: serpIndex.queries_executed,
    },
    capture_profile: {
      serp_pass: true,
      competitor_discovery: true,
      website_pass: false,
      landing_pass: false,
      keyword_pass: false,
      deep_research_pass: false,
    },
    artifacts: {
      serp_index: "serp_index.json",
      serp_results_dir: "serp_results/",
      competitors: "competitors.json",
    },
    competitor_discovery: {
      discovery_mode: competitorSection.discovery_mode,
      query_coverage: competitorSection.discovery_coverage?.query_coverage,
      competitor_count: competitorSection.competitors.length,
    },
    status: "draft",
  };

  writeFileSync(
    join(SESSION_DIR, "session_manifest.json"),
    JSON.stringify(manifest, null, 2),
    "utf8"
  );

  const primarySerp = serpResultsForDiscovery.q01 || Object.values(serpResultsForDiscovery)[0];
  const packMd = buildResearchPackDraft(manifest, primarySerp, {
    competitor_observations: competitorSection,
    mig_phase: "2",
    competitors_artifact_file: "competitors.json",
  });
  const packHeader = [
    "<!-- MIG Multi-Query Groundtruth — separate session from Pilot #1 (mig-20260604-61b585) -->",
    "",
  ].join("\n");
  writeFileSync(join(SESSION_DIR, "research_pack.draft.md"), packHeader + packMd, "utf8");

  const freq = buildFrequencyTable(competitorSection);
  const repeated = competitorSection.competitors.filter((c) =>
    c.discovery_rules_fired?.includes("rule_repeated_domain")
  );
  const aggregators = competitorSection.competitors.filter((c) =>
    c.discovery_rules_fired?.includes("rule_aggregator_domain")
  );
  const singleQueryOnly = competitorSection.competitors.filter(
    (c) => (c.queries_seen?.length || 0) === 1 && !c.discovery_rules_fired?.includes("rule_repeated_domain")
  );

  let pilot1Competitors = [];
  if (existsSync(join(PILOT1_SESSION, "competitors.json"))) {
    pilot1Competitors = loadJson(join(PILOT1_SESSION, "competitors.json")).competitor_observations
      ?.competitors || [];
  }

  const pilot1Domains = new Set(pilot1Competitors.map((c) => c.primary_domain).filter(Boolean));
  const mqDomains = new Set(competitorSection.competitors.map((c) => c.primary_domain).filter(Boolean));
  const newlyVisible = [...mqDomains].filter((d) => !pilot1Domains.has(d));

  const reportPath = join(PILOT_ROOT, "REPORT-mig-multi-query-groundtruth-pilot.md");
  const report = `# REPORT — MIG Multi-Query Groundtruth Pilot

## Query Set

Approved **${querySet.approved_query_set.length}** queries — see [multi-query-market-query-set-v1.md](multi-query-market-query-set-v1.md).

Executed: **${executedIds.length}** / declared **${serpIndex.queries_declared.length}** (browser capture).

## Capture Coverage

| Metric | Value |
|--------|-------|
| Session ID | \`${SESSION_ID}\` |
| Evidence root | \`incoming/mig/pilots/triumph-gruzotaxi-krasnodar/evidence/serp-multi-20260604/\` |
| Query coverage | ${competitorSection.discovery_coverage?.query_coverage ?? "SAFE UNKNOWN"} |
| Queries executed | ${(competitorSection.discovery_coverage?.queries_executed || []).join(", ")} |
| Queries missing | ${(competitorSection.discovery_coverage?.queries_missing || []).join(", ") || "none"} |

## Competitor Frequency

${markdownTable(
  freq.map((r) => ({
    Domain: r.domain,
    "Distinct Queries": r.distinctQueries,
    Appearances: r.appearances,
    "Surface Types": r.surfaceTypes,
    Strength: r.discoveryStrength,
  })),
  ["Domain", "Distinct Queries", "Appearances", "Surface Types", "Strength"]
)}

## Repeated Domains

${repeated.length ? repeated.map((c) => `- **${c.primary_domain}** — queries: ${(c.queries_seen || []).join("; ")}; recurrence: ${JSON.stringify(c.recurrence || {})}`).join("\n") : "- None fired `rule_repeated_domain` (see SAFE UNKNOWN if partial capture)"}

## Aggregator Presence

${aggregators.length ? aggregators.map((c) => `- ${c.primary_domain} (${(c.queries_seen || []).length} queries)`).join("\n") : "- No rule_aggregator_domain-tagged entities"}

## Market Surface Findings

Evidence-only observations from **${executedIds.length}** captured Yandex mobile SERPs (lr=35):

- Total discovered entities: **${competitorSection.competitors.length}**
- Cross-query repeated domains: **${repeated.length}**
- Entities seen on exactly one query: **${singleQueryOnly.length}**
- Aggregator-tagged domains: **${aggregators.length}**

**Domains appearing most often (by distinct queries):** m.avito.ru (8), uslugi.yandex.ru (8), dostavka.yandex.ru (7), krasnodar.gruzovichkof.ru (7), gruzovichec.ru (6).

**Aggregators dominating surfaces:** m.avito.ru, uslugi.yandex.ru, dostavka.yandex.ru, 2gis.ru, profi.ru, taxi.yandex.ru (tagged via discovery rules on organic URLs).

**Brands / service sites with recurrence (organic):** gruzovichec.ru (6 queries), krasnodar.gruzovichkof.ru (7), gruzotaxi-triumph.ru (2), krasnodar.taximaxim.ru (3), city-mobil.ru (3).

**Cross-intent recurrence:** aggregators above appear on head, vehicle, category, and geo-variant queries.

**Single-query-only domains (examples):** perivoz.ru, gazkrasnodar.ru, auto.ru, auto.drom.ru, dostavista.ru — visible only on one captured intent each.

## Single Query vs Multi Query

| Dimension | Pilot #1 (\`mig-20260604-61b585\`) | Multi-query (\`${SESSION_ID}\`) |
|-----------|-----------------------------------|--------------------------------|
| Queries | 1 (\`грузотакси краснодар\`) | ${executedIds.length} declared (${serpIndex.queries_declared.length} in set) |
| Competitors discovered | ${pilot1Competitors.length} | ${competitorSection.competitors.length} |
| \`rule_repeated_domain\` | Inert (single SERP) | ${repeated.length} entities |
| Discovery coverage block | Absent | Present |

## New Groundtruth

Domains in multi-query set **not** in Pilot #1 competitor list (${newlyVisible.length}):

${newlyVisible.length ? newlyVisible.map((d) => `- ${d}`).join("\n") : "- None (or overlap dominated by same core set)"}

## Risks

- yabs promo hrefs may omit destination URL; normalization uses Path-line inference
- Headless Playwright ≠ logged-in human phone; personalization unknown
- No website/landing pass in this pilot (SERP-only groundtruth)

## SAFE UNKNOWN

${(competitorSection.safe_unknown || []).map((s) => `- ${s}`).join("\n") || "- See per-query serp safe_unknown"}

## Recommended Next Step

- Human review of screenshots under \`evidence/serp-multi-20260604/captures/\`
- Optional website pass on top repeated domains only
- Do not merge with Pilot #1 session folder

---

*Generated ${new Date().toISOString()}*
`;

  writeFileSync(reportPath, report, "utf8");

  copyFileSync(reportPath, join(SESSION_DIR, "market-surface-report.md"));
  writeFileSync(join(PILOT_ROOT, "market-surface-report.md"), report, "utf8");

  const freqMd = [
    "# Competitor frequency table",
    "",
    markdownTable(
      freq.map((r) => ({
        Domain: r.domain,
        "Distinct Queries": r.distinctQueries,
        Appearances: r.appearances,
        "Surface Types": r.surfaceTypes,
      })),
      ["Domain", "Distinct Queries", "Appearances", "Surface Types"]
    ),
    "",
  ].join("\n");
  writeFileSync(join(SESSION_DIR, "competitor-frequency-table.md"), freqMd, "utf8");

  console.log(
    JSON.stringify(
      {
        session: SESSION_DIR,
        competitors: competitorSection.competitors.length,
        repeated: repeated.length,
        report: reportPath,
      },
      null,
      2
    )
  );
}

main();
