#!/usr/bin/env node
/**
 * Market leader intelligence pass — website acquisition + landing analysis v2.
 * Source groundtruth: mig-20260604-mqgt01 (read-only). New session output only.
 */
import {
  readFileSync,
  writeFileSync,
  mkdirSync,
  copyFileSync,
  existsSync,
  cpSync,
} from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = join(__dirname, "..");
const MIG_ROOT = join(PILOT_ROOT, "..", "..", "..", "..", "projects", "mig");
const require = createRequire(import.meta.url);

const SOURCE_SESSION_ID = "mig-20260604-mqgt01";
const SESSION_ID = "mig-20260605-mlint01";
const SOURCE_DIR = join(PILOT_ROOT, `session-${SOURCE_SESSION_ID}`);
const SESSION_DIR = join(PILOT_ROOT, `session-${SESSION_ID}`);

const MARKET_LEADER_DOMAINS = [
  "gruzotaxi-triumph.ru",
  "gruzovichec.ru",
  "krasnodar.gruzovichkof.ru",
  "krasnodar.taximaxim.ru",
  "city-mobil.ru",
];

const EXCLUDED_SURFACE_TYPES = ["aggregator", "marketplace_listing", "informational_surface"];

const { runWebsitePass } = require(join(MIG_ROOT, "lib", "website-acquisition", "run-website-pass.js"));
const { runLandingPass } = require(join(MIG_ROOT, "lib", "landing-analysis", "run-landing-pass.js"));
const { enrichLandingIndexWithDetail } = require(join(MIG_ROOT, "lib", "runtime", "load-landing-detail.js"));
const { buildResearchPackDraft } = require(join(MIG_ROOT, "lib", "session-spine", "build-research-pack.js"));
const { loadRules } = require(join(MIG_ROOT, "lib", "website-acquisition", "build-url-plan.js"));

function loadJson(p) {
  return JSON.parse(readFileSync(p, "utf8"));
}

function classifyEntity(c) {
  const domain = c.primary_domain || "";
  const surfaces = c.surface_types || [];
  const rules = loadJson(join(MIG_ROOT, "config", "competitor-discovery-rules-v0.json"));

  const isAgg = rules.aggregator_domains?.some((d) => domain === d || domain.endsWith(`.${d}`));
  const isMkt = rules.marketplace_domains?.some((d) => domain === d || domain.endsWith(`.${d}`));

  if (domain === "2gis.ru") return "DIRECTORY";
  if (domain === "city-mobil.ru" || domain === "krasnodar.taximaxim.ru") return "SERVICE_BRAND";
  if (domain === "dostavista.ru" || domain === "taxi.yandex.ru" || domain === "dostavka.yandex.ru")
    return "PLATFORM";
  if (domain === "auto.ru" || domain === "auto.drom.ru" || domain === "gazkrasnodar.ru" || domain.includes("autoretail"))
    return "MARKETPLACE";
  if (isMkt || surfaces.includes("marketplace_listing")) return "MARKETPLACE";
  if (isAgg || surfaces.includes("aggregator")) return "AGGREGATOR";
  if (MARKET_LEADER_DOMAINS.includes(domain)) return "SERVICE_BRAND";
  if (surfaces.includes("serp_organic") && (c.recurrence?.distinct_query_count ?? 0) >= 1)
    return "SERVICE_BRAND";
  return "CLIENT";
}

function buildClassificationProposal(section) {
  const rows = (section.competitors || []).map((c) => ({
    domain: c.primary_domain,
    display_name: (c.display_name || "").slice(0, 80),
    classification: classifyEntity(c),
    distinct_queries: c.recurrence?.distinct_query_count ?? c.queries_seen?.length ?? 0,
    appearances: c.evidence?.length ?? 0,
    surface_types: (c.surface_types || []).join(", "),
    evidence_ref: `competitors.json → ${c.competitor_id}`,
  }));
  rows.sort((a, b) => b.distinct_queries - a.distinct_queries || b.appearances - a.appearances);

  const lines = [
    "# Entity classification proposal",
    "",
    "Rules-only, evidence from multi-query SERP (`mig-20260604-mqgt01`). No ATLAS dependency.",
    "",
    "| Domain | Classification | Distinct Queries | Appearances | Surface Types | Evidence |",
    "| --- | --- | --- | --- | --- | --- |",
    ...rows.map(
      (r) =>
        `| ${r.domain} | ${r.classification} | ${r.distinct_queries} | ${r.appearances} | ${r.surface_types} | ${r.evidence_ref} |`
    ),
    "",
    "## Classification rules applied",
    "",
    "- **SERVICE_BRAND** — registrable domain of a cargo-taxi / freight operator; organic SERP titles describe direct hire or regional service (not listing aggregation).",
    "- **AGGREGATOR** — multi-provider directory (Yandex Uslugi, Profi, Yandex Delivery landing, taxi.yandex tariff pages).",
    "- **MARKETPLACE** — classifieds / listings (Avito, Youla, auto sales).",
    "- **DIRECTORY** — business map / org index (2GIS).",
    "- **PLATFORM** — app-first dispatch platform (CityMobil/TaxiMaxim-style national apps; Dostavista).",
    "- **CLIENT** — single-query or ambiguous local operator not in repeated market-leader set.",
    "",
  ];
  return { rows, markdown: lines.join("\n") };
}

function buildShortlist(section) {
  const leaders = (section.competitors || []).filter((c) =>
    MARKET_LEADER_DOMAINS.includes(c.primary_domain)
  );
  return {
    session_id: SESSION_ID,
    source_session: SOURCE_SESSION_ID,
    generated_at: new Date().toISOString(),
    criteria: {
      include: "SERVICE_BRAND with rule_repeated_domain",
      exclude: "AGGREGATOR, MARKETPLACE, DIRECTORY domains per task brief",
    },
    domains: MARKET_LEADER_DOMAINS,
    competitors: leaders.map((c) => ({
      competitor_id: c.competitor_id,
      domain: c.primary_domain,
      display_name: c.display_name,
      distinct_queries: c.recurrence?.distinct_query_count,
      query_ids: c.recurrence?.query_ids || c.query_ids_seen,
      evidence_count: c.evidence?.length,
    })),
  };
}

function filterCompetitorsArtifact(sourceArtifact, shortlist) {
  const ids = new Set(shortlist.competitors.map((c) => c.competitor_id));
  const filtered = (sourceArtifact.competitor_observations?.competitors || []).filter((c) =>
    ids.has(c.competitor_id)
  );
  return {
    ...sourceArtifact,
    session_id: SESSION_ID,
    generated_at: new Date().toISOString(),
    competitor_observations: {
      ...sourceArtifact.competitor_observations,
      competitors: filtered.map((c, i) => ({
        ...c,
        competitor_id: `${SESSION_ID}-c${String(i + 1).padStart(3, "0")}`,
      })),
    },
  };
}

function remapCompetitorIds(competitorsArtifact, shortlist) {
  const idMap = {};
  const oldIds = shortlist.competitors.map((c) => c.competitor_id);
  const newCompetitors = competitorsArtifact.competitor_observations.competitors;
  oldIds.forEach((oldId, i) => {
    idMap[oldId] = newCompetitors[i].competitor_id;
  });
  return idMap;
}

function buildComparisonMatrix(landingIndex, websiteIndex, competitorsArtifact) {
  const rows = [];
  for (const landing of landingIndex.landings || []) {
    const snap = (websiteIndex.snapshots || []).find((s) => s.snapshot_id === landing.snapshot_id);
    const obs = landing.observation_summary || {};
    const families = obs.families_present || [];
    const topOffers = (obs.top_signals || [])
      .filter((s) => s.family === "OFFERS")
      .map((s) => s.text)
      .slice(0, 3);
    const pricing = (obs.top_signals || [])
      .filter((s) => s.family === "PRICING")
      .map((s) => s.text)
      .slice(0, 3);
    const delivery = (obs.top_signals || [])
      .filter((s) => s.family === "DELIVERY_PROMISE")
      .map((s) => s.text)
      .slice(0, 2);
    const trust = (obs.top_signals || [])
      .filter((s) => ["TRUST", "SOCIAL_PROOF"].includes(s.family))
      .map((s) => s.text)
      .slice(0, 3);
    const leadCapture = (obs.top_signals || [])
      .filter((s) => ["CTA", "LEAD_CAPTURE"].includes(s.family))
      .map((s) => s.text)
      .slice(0, 3);
    const contacts = snap?.contacts || {};
    const messengerLabels = (contacts.messengers || [])
      .map((m) => (typeof m === "object" ? `${m.type || "msg"}:${m.handle || ""}` : String(m)))
      .slice(0, 2);
    const contactModel = [
      contacts.phones?.length ? `phones: ${contacts.phones.slice(0, 2).join(", ")}` : null,
      contacts.emails?.length ? `emails: ${contacts.emails.slice(0, 1).join(", ")}` : null,
      contacts.messengers?.length ? `messengers: ${messengerLabels.join(", ")}` : null,
    ]
      .filter(Boolean)
      .join("; ") || "SAFE UNKNOWN";
    const pageStructure = (snap?.headings || [])
      .slice(0, 6)
      .map((h) => h.text || h)
      .join(" → ");

    rows.push({
      domain: landing.domain,
      primary_offer: topOffers.join("; ") || "SAFE UNKNOWN",
      pricing_signals: pricing.join("; ") || "SAFE UNKNOWN",
      delivery_promise: delivery.join("; ") || "SAFE UNKNOWN",
      trust_signals: trust.join("; ") || "SAFE UNKNOWN",
      lead_capture_model: leadCapture.join("; ") || (snap?.forms?.length ? "form present" : "SAFE UNKNOWN"),
      contact_model: contactModel,
      page_structure: pageStructure || "SAFE UNKNOWN",
      evidence_refs: [
        landing.artifact_ref,
        snap?.artifact_refs?.website_snapshot,
        snap?.artifact_refs?.page_html,
      ]
        .filter(Boolean)
        .join(", "),
      families_present: families.join(", "),
      acquisition_status: snap?.status || "SAFE UNKNOWN",
    });
  }
  return rows;
}

function comparisonMarkdown(rows) {
  const headers = [
    "Domain",
    "Primary Offer",
    "Pricing Signals",
    "Delivery Promise",
    "Trust Signals",
    "Lead Capture Model",
    "Contact Model",
    "Page Structure",
    "Evidence References",
  ];
  const lines = [
    "# Market leader comparison matrix",
    "",
    "Facts only — no strategic conclusions.",
    "",
    "| " + headers.join(" | ") + " |",
    "| " + headers.map(() => "---").join(" | ") + " |",
    ...rows.map((r) =>
      "| " +
        [
          r.domain,
          r.primary_offer.replace(/\|/g, "\\|").slice(0, 120),
          r.pricing_signals.replace(/\|/g, "\\|").slice(0, 100),
          r.delivery_promise.replace(/\|/g, "\\|").slice(0, 80),
          r.trust_signals.replace(/\|/g, "\\|").slice(0, 80),
          r.lead_capture_model.replace(/\|/g, "\\|").slice(0, 80),
          r.contact_model.replace(/\|/g, "\\|").slice(0, 80),
          r.page_structure.replace(/\|/g, "\\|").slice(0, 100),
          r.evidence_refs,
        ].join(" | ") +
        " |"
    ),
    "",
  ];
  return lines.join("\n");
}

async function main() {
  if (!existsSync(SOURCE_DIR)) {
    throw new Error(`Source session not found: ${SOURCE_DIR}`);
  }

  mkdirSync(SESSION_DIR, { recursive: true });
  mkdirSync(join(SESSION_DIR, "serp_results"), { recursive: true });

  const sourceManifest = loadJson(join(SOURCE_DIR, "session_manifest.json"));
  const sourceCompetitors = loadJson(join(SOURCE_DIR, "competitors.json"));
  const section = sourceCompetitors.competitor_observations;

  const { markdown: classificationMd, rows: classificationRows } = buildClassificationProposal(section);
  writeFileSync(join(SESSION_DIR, "entity-classification-proposal.md"), classificationMd, "utf8");

  const shortlist = buildShortlist(section);
  writeFileSync(join(SESSION_DIR, "market-leader-shortlist.json"), `${JSON.stringify(shortlist, null, 2)}\n`, "utf8");

  const filteredCompetitors = filterCompetitorsArtifact(sourceCompetitors, shortlist);
  writeFileSync(join(SESSION_DIR, "competitors.json"), `${JSON.stringify(filteredCompetitors, null, 2)}\n`, "utf8");

  copyFileSync(join(SOURCE_DIR, "serp_index.json"), join(SESSION_DIR, "serp_index.json"));
  if (existsSync(join(SOURCE_DIR, "serp_results", "q01.json"))) {
    copyFileSync(join(SOURCE_DIR, "serp_results", "q01.json"), join(SESSION_DIR, "serp_result.json"));
    copyFileSync(join(SOURCE_DIR, "serp_results", "q01.json"), join(SESSION_DIR, "serp_results", "q01.json"));
  }

  const manifest = {
    ...sourceManifest,
    session_id: SESSION_ID,
    created_at: new Date().toISOString(),
    operator_id: "market-leader-intelligence-pass",
    mig_phase: "3",
    parent_session: SOURCE_SESSION_ID,
    capture_profile: {
      ...sourceManifest.capture_profile,
      serp_pass: true,
      competitor_discovery: true,
      website_pass: true,
      landing_pass: true,
    },
    artifacts: {
      ...sourceManifest.artifacts,
      market_leader_shortlist: "market-leader-shortlist.json",
      entity_classification: "entity-classification-proposal.md",
      comparison_matrix: "market-leader-comparison-matrix.md",
    },
    status: "draft",
  };
  writeFileSync(join(SESSION_DIR, "session_manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`, "utf8");

  writeFileSync(
    join(SESSION_DIR, "groundtruth-ref.json"),
    `${JSON.stringify({ source_session: SOURCE_SESSION_ID, source_dir: SOURCE_DIR, read_only: true }, null, 2)}\n`,
    "utf8"
  );

  const rules = {
    ...loadRules(),
    url_cap_default: 6,
    url_cap_hard_max: 10,
    fetch_timeout_ms: 20000,
    skip_surface_types: EXCLUDED_SURFACE_TYPES,
    inter_request_delay_ms: 1000,
  };

  console.log("Running website acquisition for", shortlist.competitors.length, "market leaders...");
  const websiteResult = await runWebsitePass(SESSION_DIR, {
    competitorsArtifact: filteredCompetitors,
    url_cap: 6,
    rules,
  });

  console.log("Running landing analysis v2...");
  const landingResult = runLandingPass(SESSION_DIR);
  const landingIndex = enrichLandingIndexWithDetail(SESSION_DIR, landingResult.index);

  const serp = loadJson(join(SESSION_DIR, "serp_result.json"));
  const pack = buildResearchPackDraft(manifest, serp, {
    competitor_observations: filteredCompetitors.competitor_observations,
    website_snapshots: websiteResult.index,
    landing_observations: landingIndex,
    mig_phase: "3",
  });
  writeFileSync(join(SESSION_DIR, "research_pack.draft.md"), pack, "utf8");

  const comparisonRows = buildComparisonMatrix(landingIndex, websiteResult.index, filteredCompetitors);
  writeFileSync(
    join(SESSION_DIR, "market-leader-comparison-matrix.md"),
    comparisonMarkdown(comparisonRows),
    "utf8"
  );
  writeFileSync(
    join(SESSION_DIR, "market-leader-comparison-matrix.json"),
    `${JSON.stringify({ session_id: SESSION_ID, rows: comparisonRows }, null, 2)}\n`,
    "utf8"
  );

  const acquisitionSummary = {
    session_id: SESSION_ID,
    snapshots_planned: websiteResult.url_plan.planned_count,
    snapshots_captured: websiteResult.snapshots.length,
    skipped: websiteResult.url_plan.skipped,
    by_status: websiteResult.snapshots.reduce((acc, s) => {
      acc[s.status] = (acc[s.status] || 0) + 1;
      return acc;
    }, {}),
  };
  writeFileSync(
    join(SESSION_DIR, "website-acquisition-summary.json"),
    `${JSON.stringify(acquisitionSummary, null, 2)}\n`,
    "utf8"
  );

  const reportPath = join(PILOT_ROOT, "REPORT-top-repeated-domains-intelligence-pass.md");
  const report = buildReport({
    classificationRows,
    shortlist,
    acquisitionSummary,
    comparisonRows,
    landingIndex,
    websiteResult,
    sourceSession: SOURCE_SESSION_ID,
  });
  writeFileSync(reportPath, report, "utf8");
  copyFileSync(reportPath, join(SESSION_DIR, "REPORT-top-repeated-domains-intelligence-pass.md"));

  console.log(
    JSON.stringify(
      {
        session_dir: SESSION_DIR,
        report: reportPath,
        snapshots: websiteResult.snapshots.length,
        landing_phase: landingIndex.analysis_phase,
      },
      null,
      2
    )
  );
}

function buildReport(ctx) {
  const {
    classificationRows,
    shortlist,
    acquisitionSummary,
    comparisonRows,
    landingIndex,
    websiteResult,
    sourceSession,
  } = ctx;

  const leaderRows = classificationRows.filter((r) => r.classification === "SERVICE_BRAND" && r.distinct_queries >= 2);
  const excluded = classificationRows.filter((r) =>
    ["AGGREGATOR", "MARKETPLACE", "DIRECTORY"].includes(r.classification)
  );

  const serpOnly = leaderRows.map(
    (r) => `- **${r.domain}** — SERP titles/snippets only; recurrence ${r.distinct_queries} queries`
  );
  const websiteVisible = comparisonRows.map((r) => {
    const fam = r.families_present || "—";
    return `- **${r.domain}** — acquisition \`${r.acquisition_status}\`; families: ${fam}`;
  });

  return `# REPORT — Top Repeated Domains Intelligence Pass

## Classification Review

Entity classification from \`${sourceSession}\` competitor-frequency-table and competitors.json.

| Type | Count | Examples |
| --- | --- | --- |
| SERVICE_BRAND | ${classificationRows.filter((r) => r.classification === "SERVICE_BRAND").length} | gruzovichec.ru, krasnodar.gruzovichkof.ru, gruzotaxi-triumph.ru |
| AGGREGATOR | ${classificationRows.filter((r) => r.classification === "AGGREGATOR").length} | uslugi.yandex.ru, dostavka.yandex.ru, profi.ru |
| MARKETPLACE | ${classificationRows.filter((r) => r.classification === "MARKETPLACE").length} | m.avito.ru, youla.ru, auto.ru |
| DIRECTORY | ${classificationRows.filter((r) => r.classification === "DIRECTORY").length} | 2gis.ru |
| PLATFORM | ${classificationRows.filter((r) => r.classification === "PLATFORM").length} | dostavista.ru, taxi.yandex.ru, dostavka.yandex.ru |
| CLIENT | ${classificationRows.filter((r) => r.classification === "CLIENT").length} | perivoz.ru, krasnodar.bystraya-logistika.ru |

Full table: \`session-${SESSION_ID}/entity-classification-proposal.md\`

**Excluded from website pass (per task):** ${excluded.map((r) => r.domain).join(", ")}

## Market Leader Shortlist

Approved **${shortlist.competitors.length}** SERVICE_BRAND domains with \`rule_repeated_domain\`:

${shortlist.competitors.map((c) => `- **${c.domain}** — ${c.distinct_queries} distinct queries; evidence rows: ${c.evidence_count}; id ref ${c.competitor_id}`).join("\n")}

Artifact: \`session-${SESSION_ID}/market-leader-shortlist.json\`

## Website Acquisition Results

| Metric | Value |
| --- | --- |
| Session | \`${SESSION_ID}\` |
| Planned snapshots | ${acquisitionSummary.snapshots_planned} |
| Captured | ${acquisitionSummary.snapshots_captured} |
| Status breakdown | ${JSON.stringify(acquisitionSummary.by_status)} |

Per-domain:

${websiteResult.snapshots
  .map(
    (s) =>
      `- **${s.domain}** — HTTP ${s.http_status ?? "—"}; status \`${s.status}\`; URL \`${s.final_url || s.requested_url}\`; headings ${s.headings?.length ?? 0}; offers ${s.offers?.length ?? 0}; forms ${s.forms?.length ?? 0}`
  )
  .join("\n")}

## Landing Analysis Results

Analysis phase: \`${landingIndex.analysis_phase}\` (schema ${landingIndex.schema_version})

${(landingIndex.landings || [])
  .map((l) => {
    const sum = l.observation_summary || {};
    return `### ${l.domain}

- Families: ${(sum.families_present || []).join(", ") || "SAFE UNKNOWN"}
- Top signals: ${(sum.top_signals || [])
      .slice(0, 5)
      .map((s) => `${s.family}: ${(s.text || "").slice(0, 60)}`)
      .join("; ") || "SAFE UNKNOWN"}
- Artifact: \`${l.artifact_ref}\``;
  })
  .join("\n\n")}

## Comparison Matrix

See \`session-${SESSION_ID}/market-leader-comparison-matrix.md\`

## New Groundtruth

Session \`${SESSION_ID}\` — separate from \`mig-20260604-61b585\` and \`mig-20260604-mqgt01\`.

| Artifact | Path |
| --- | --- |
| Shortlist | session-${SESSION_ID}/market-leader-shortlist.json |
| Website snapshots | session-${SESSION_ID}/website_snapshots.json |
| Landing observations | session-${SESSION_ID}/landing_observations.json |
| Research pack | session-${SESSION_ID}/research_pack.draft.md |
| Comparison matrix | session-${SESSION_ID}/market-leader-comparison-matrix.md |

## SERP vs Website Findings

**Visible from SERP alone:**

${serpOnly.join("\n")}

**Visible only after website acquisition:**

${websiteVisible.join("\n")}

**What changed:** Page-level headings, offer text, pricing strings, form/CTA elements, phone/email contacts, and trust phrases are now captured with HTML evidence refs. SERP provided title/snippet/position only.

## SAFE UNKNOWN

- Queries q05, q06, q07 not captured in source session — entities from those intents absent
- Actual dispatch pricing at order time (dynamic quotes) — only visible page text captured
- Human personalization / logged-in SERP variants
- Conversion performance, ad spend, fleet size — not observable from acquisition pass
- Whether SERP snippet prices match live page prices at capture time

## Readiness Assessment

MIG **now produces structured market intelligence beyond observation counts** for the approved shortlist: landing analysis v2 emits \`observations[]\` with families (offer, pricing, delivery_promise, trust, lead_capture), per-domain comparison matrix, and research pack intelligence cards.

**Limitation:** Intelligence remains **page-visible facts** at one URL per domain (homepage or SERP landing URL). No multi-page crawl, no ORCA interpretation, partial query coverage from source groundtruth.

**Verdict:** Useful **comparative landing intelligence** for market leaders — not yet full market intelligence (no keyword pass, no ads surface, no multi-page depth).

## Recommended Next Step

Human review of captured HTML under \`session-${SESSION_ID}/snapshots/sites/\` and comparison matrix; no automated strategy synthesis.

---

*Generated ${new Date().toISOString()} · Lane A · session ${SESSION_ID}*
`;
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
