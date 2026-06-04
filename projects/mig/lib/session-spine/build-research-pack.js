"use strict";

const {
  discoverFromSerp,
  formatCompetitorObservationsMarkdown,
} = require("../competitor-discovery/discover-from-serp");
const { formatLandingObservationBlocksV2 } = require("./format-landing-intelligence-v2");

function bulletList(items) {
  if (!Array.isArray(items) || items.length === 0) {
    return "- SAFE UNKNOWN";
  }
  return items.map((item) => `- ${item}`).join("\n");
}

function formatAdsSummary(adsBlocks) {
  if (!adsBlocks || typeof adsBlocks !== "object") {
    return "SAFE UNKNOWN";
  }
  const top = adsBlocks.top_count ?? "SAFE UNKNOWN";
  const bottom = adsBlocks.bottom_count ?? "SAFE UNKNOWN";
  const patterns =
    Array.isArray(adsBlocks.visible_patterns) && adsBlocks.visible_patterns.length > 0
      ? adsBlocks.visible_patterns.join(", ")
      : "none observed";
  return `Top ads: ${top}; Bottom ads: ${bottom}; Patterns: ${patterns}`;
}

function formatDiscoveryCoverageBlock(competitorSection) {
  const coverage = competitorSection.discovery_coverage;
  if (!coverage) {
    return [
      "### Discovery coverage",
      "",
      "- SAFE UNKNOWN — multi-query coverage not computed (single-query session or legacy path)",
      "",
    ].join("\n");
  }

  const lines = [
    "### Discovery coverage",
    "",
    "| Field | Value |",
    "|-------|-------|",
    `| Query coverage | ${coverage.query_coverage} |`,
    `| Queries declared | ${coverage.queries_declared.join(", ") || "—"} |`,
    `| Queries executed | ${coverage.queries_executed.join(", ") || "—"} |`,
    `| Queries missing | ${coverage.queries_missing.length ? coverage.queries_missing.join(", ") : "none"} |`,
    "",
  ];

  if (coverage.query_coverage === "partial" && coverage.queries_missing.length) {
    lines.push(
      `Query coverage note: entities from missing queries (${coverage.queries_missing.join(", ")}) are not represented.`,
      ""
    );
  }

  return lines.join("\n");
}

function formatRecurrenceSummary(competitorSection) {
  const withRecurrence = (competitorSection.competitors || []).filter(
    (c) => c.recurrence || c.discovery_rules_fired?.includes("rule_repeated_domain")
  );

  if (!competitorSection.discovery_coverage) {
    return [
      "### Cross-query recurrence",
      "",
      "- SAFE UNKNOWN — cross-query recurrence not evaluated",
      "",
    ].join("\n");
  }

  if (competitorSection.discovery_coverage.queries_executed.length < 2) {
    return [
      "### Cross-query recurrence",
      "",
      "- SAFE UNKNOWN — only one SERP captured; cross-query recurrence not evaluated",
      "",
    ].join("\n");
  }

  if (!withRecurrence.length) {
    return [
      "### Cross-query recurrence",
      "",
      "- No domains matched organic top-N on two or more distinct queries",
      "",
    ].join("\n");
  }

  const lines = [
    "### Cross-query recurrence",
    "",
    "| Domain | Distinct queries | Query IDs | Strength |",
    "|--------|------------------|-----------|----------|",
  ];

  for (const c of withRecurrence) {
    const recurrence = c.recurrence || {
      distinct_query_count: c.query_ids_seen?.length || c.queries_seen.length,
      query_ids: c.query_ids_seen || [],
    };
    lines.push(
      `| ${c.primary_domain || "—"} | ${recurrence.distinct_query_count} | ${recurrence.query_ids.join(", ")} | ${c.discovery_strength} |`
    );
  }
  lines.push("");
  return lines.join("\n");
}

function formatQueryCoverageNotes(manifest, competitorSection) {
  const executed =
    manifest.queries?.queries_executed ||
    competitorSection.discovery_coverage?.queries_executed ||
    [];
  const seed = manifest.queries?.seed_queries || [];

  const lines = ["### Query coverage notes", ""];
  if (executed.length) {
    lines.push(`- Executed query ids: ${executed.join(", ")}`);
  } else if (manifest.queries?.query_used) {
    lines.push(`- Single-query pass: ${manifest.queries.query_used}`);
  }
  if (seed.length) {
    lines.push(`- Seed queries (${seed.length}): ${seed.join("; ")}`);
  }
  lines.push("");
  return lines.join("\n");
}

function capList(items, cap) {
  if (!Array.isArray(items)) {
    return [];
  }
  return items.slice(0, cap);
}

function formatWebsiteCaptureSummary(websiteIndex) {
  if (!websiteIndex || !Array.isArray(websiteIndex.snapshots)) {
    return [
      "## Website capture summary",
      "",
      "- SAFE UNKNOWN — website acquisition not executed",
      "",
    ].join("\n");
  }

  const lines = [
    "## Website capture summary",
    "",
    "| Snapshot | Competitor | URL | Status | Grade | Render |",
    "|----------|------------|-----|--------|-------|--------|",
  ];

  for (const snap of websiteIndex.snapshots) {
    lines.push(
      `| ${snap.snapshot_id} | ${snap.competitor_id || "—"} | ${snap.final_url || snap.requested_url} | ${snap.status} | ${snap.evidence_grade} | ${snap.render_status} |`
    );
  }

  lines.push(
    "",
    `Session coverage: **${websiteIndex.session_coverage}** · Section grade: **${websiteIndex.section_evidence_grade}**`,
    ""
  );
  return lines.join("\n");
}

function formatWebsiteObservationsSection(title, snapshots, projector, emptyLabel) {
  const lines = [`## ${title}`, ""];
  let hasContent = false;

  for (const snap of snapshots) {
    const items = projector(snap);
    if (!items.length) {
      continue;
    }
    hasContent = true;
    lines.push(`### ${snap.snapshot_id} (${snap.domain})`, "");
    for (const item of items) {
      lines.push(`- ${item}`);
    }
    lines.push("");
  }

  if (!hasContent) {
    lines.push(`- ${emptyLabel}`, "");
  }
  return lines.join("\n");
}

function formatLandingObservationBlocks(landingIndex, rules = {}) {
  const caps = rules.pack_projection_caps || {
    offers: 5,
    cta_elements: 5,
    pricing_signals: 5,
    trust_signals: 5,
    blocks: 10,
  };

  const landingLines = [
    "## Landing observations (structured)",
    "",
    "Visible structure only — from Landing Analysis artifacts.",
    "",
  ];

  if (!landingIndex?.landings?.length) {
    landingLines.push("- SAFE UNKNOWN — no landing observations in session index", "");
  } else {
    for (const row of landingIndex.landings) {
      landingLines.push(
        `### ${row.landing_id} · ${row.domain}`,
        "",
        `| Field | Value |`,
        `|-------|-------|`,
        `| Snapshot | ${row.snapshot_id} |`,
        `| Page type | ${row.page_type} |`,
        `| Grade | ${row.evidence_grade} |`,
        `| Ref | \`${row.artifact_ref}\` |`,
        ""
      );
    }
  }

  const detailByLanding = landingIndex?._detail || [];

  const offerSection = formatLandingDetailSection(
    "Offer observations",
    detailByLanding,
    (obs) =>
      capList(obs.offers, caps.offers).map((o) =>
        o.offer_surface ? `${o.text} [${o.offer_surface}]` : o.text
      ),
    "SAFE UNKNOWN — no offer strings in landing observations"
  );

  const ctaSection = formatLandingDetailSection(
    "CTA observations",
    detailByLanding,
    (obs) =>
      capList(obs.cta_patterns, caps.cta_elements).map((c) =>
        c.target_href ? `${c.label_text} (${c.cta_type}) → ${c.target_href}` : `${c.label_text} (${c.cta_type})`
      ),
    "SAFE UNKNOWN — no CTA patterns in landing observations"
  );

  const trustSection = formatLandingDetailSection(
    "Trust observations",
    detailByLanding,
    (obs) =>
      capList(obs.trust_patterns, caps.trust_signals).map((t) => `${t.text} [${t.trust_type}]`),
    "SAFE UNKNOWN — no trust patterns in landing observations"
  );

  const pricingSection = formatLandingDetailSection(
    "Pricing signals (visible)",
    detailByLanding,
    (obs) =>
      capList(obs.pricing_patterns, caps.pricing_signals).map((p) =>
        p.currency_hint ? `${p.text} [${p.currency_hint}]` : p.text
      ),
    "No pricing patterns in landing observations"
  );

  const blockSection = formatLandingDetailSection(
    "Block observations",
    detailByLanding,
    (obs) =>
      capList(obs.visible_blocks, caps.blocks).map(
        (b) => `${b.block_type}${b.heading_text ? `: ${b.heading_text}` : ""}`
      ),
    "SAFE UNKNOWN — no visible blocks detected"
  );

  const captureSummary = landingIndex
    ? [
        "## Landing analysis summary",
        "",
        `Session coverage: **${landingIndex.session_coverage}** · Section grade: **${landingIndex.section_evidence_grade}**`,
        `Landings analyzed: **${landingIndex.landings?.length ?? 0}**`,
        "",
      ].join("\n")
    : "";

  return [
    captureSummary,
    landingLines.join("\n"),
    offerSection,
    pricingSection,
    ctaSection,
    trustSection,
    blockSection,
  ]
    .filter(Boolean)
    .join("\n");
}

function formatLandingDetailSection(title, observations, projector, emptyLabel) {
  const lines = [`## ${title}`, ""];
  let hasContent = false;

  for (const obs of observations) {
    const items = projector(obs);
    if (!items.length) {
      continue;
    }
    hasContent = true;
    lines.push(`### ${obs.landing_id} (${obs.domain})`, "");
    for (const item of items) {
      lines.push(`- ${item}`);
    }
    lines.push("");
  }

  if (!hasContent) {
    lines.push(`- ${emptyLabel}`, "");
  }
  return lines.join("\n");
}

function formatWebsiteObservationBlocks(websiteIndex, rules = {}) {
  const caps = rules.pack_projection_caps || {
    offers: 5,
    cta_elements: 5,
    pricing_signals: 5,
    headings: 10,
    trust_signals: 5,
  };
  const snapshots = websiteIndex?.snapshots || [];

  const landing = formatWebsiteObservationsSection(
    "Website observations",
    snapshots,
    (snap) => {
      const rows = [];
      if (snap.title) {
        rows.push(`Title: ${snap.title}`);
      }
      if (snap.meta_description) {
        rows.push(`Meta: ${snap.meta_description}`);
      }
      for (const h of capList(snap.headings, caps.headings)) {
        rows.push(`H${h.level}: ${h.text}`);
      }
      if (snap.artifact_refs?.website_snapshot) {
        rows.push(`Ref: \`${snap.artifact_refs.website_snapshot}\``);
      }
      return rows;
    },
    "SAFE UNKNOWN — no landing observations captured"
  );

  const offers = formatWebsiteObservationsSection(
    "Offer observations",
    snapshots,
    (snap) =>
      capList(snap.offers, caps.offers).map((o) =>
        o.context ? `${o.text} (${o.context})` : o.text
      ),
    "SAFE UNKNOWN — no offer strings visible on captured pages"
  );

  const ctas = formatWebsiteObservationsSection(
    "CTA observations",
    snapshots,
    (snap) =>
      capList(snap.cta_elements, caps.cta_elements).map((c) =>
        c.href ? `${c.text} → ${c.href}` : c.text
      ),
    "SAFE UNKNOWN — no CTA elements visible on captured pages"
  );

  const trust = formatWebsiteObservationsSection(
    "Trust observations",
    snapshots,
    (snap) => capList(snap.trust_signals_visible, caps.trust_signals).map((t) => t.text),
    "SAFE UNKNOWN — no trust phrases visible on captured pages"
  );

  const pricing = formatWebsiteObservationsSection(
    "Pricing signals (visible)",
    snapshots,
    (snap) =>
      capList(snap.pricing_signals, caps.pricing_signals).map((p) =>
        p.currency_hint ? `${p.text} [${p.currency_hint}]` : p.text
      ),
    "No pricing signals visible on captured pages"
  );

  const contacts = [];
  const phones = new Set();
  const emails = new Set();
  for (const snap of snapshots) {
    for (const phone of snap.contacts?.phones || []) {
      phones.add(phone);
    }
    for (const email of snap.contacts?.emails || []) {
      emails.add(email);
    }
  }
  if (phones.size || emails.size) {
    contacts.push("### Contacts (session dedupe)", "");
    for (const phone of phones) {
      contacts.push(`- Phone: ${phone}`);
    }
    for (const email of emails) {
      contacts.push(`- Email: ${email}`);
    }
    contacts.push("");
  }

  return [formatWebsiteCaptureSummary(websiteIndex), landing, offers, pricing, ctas, trust, contacts.join("\n")]
    .filter(Boolean)
    .join("\n");
}

function formatArtifactRegistryBlock(manifest, competitorSection, options = {}) {
  const artifactFile =
    options.competitors_artifact_file ||
    manifest.artifacts?.competitors ||
    "competitors.json";
  const websiteFile =
    options.website_snapshots_file || manifest.artifacts?.website_snapshots || "website_snapshots.json";
  const landingFile =
    options.landing_observations_file ||
    manifest.artifacts?.landing_observations ||
    "landing_observations.json";
  const discoveryPassAt = competitorSection.discovery_pass_at || "SAFE UNKNOWN";
  const count = competitorSection.competitors?.length ?? 0;
  const snapshotCount = options.website_snapshot_count ?? 0;
  const landingCount = options.landing_count ?? 0;

  return [
    "## Artifact Registry",
    "",
    "| Artifact | Path | Notes |",
    "|----------|------|-------|",
    `| serp_result | ${manifest.artifacts?.serp_result || "serp_result.json"} | SERP capture SoT |`,
    `| competitors | ${artifactFile} | Competitor discovery SoT (${count} entities) |`,
    `| website_snapshots | ${websiteFile} | Website acquisition index (${snapshotCount} snapshots) |`,
  ...(landingCount > 0
    ? [`| landing_observations | ${landingFile} | Landing Analysis index (${landingCount} landings) |`]
    : []),
    `| research_pack_draft | ${manifest.artifacts?.research_pack_draft || "research_pack.draft.md"} | Human-readable projection |`,
    "",
    "### Competitor artifact reference",
    "",
    `| Field | Value |`,
    `|-------|-------|`,
    `| Artifact file | ${artifactFile} |`,
    `| Discovery pass | ${discoveryPassAt} |`,
    `| Competitor count | ${count} |`,
    `| Section grade | ${competitorSection.section_evidence_grade || "SAFE UNKNOWN"} |`,
    `| Coverage | ${competitorSection.section_coverage || "SAFE UNKNOWN"} |`,
    `| Discovery mode | ${competitorSection.discovery_mode || options.discovery_mode || "SAFE UNKNOWN"} |`,
    "",
    "### Website snapshots reference",
    "",
    `| Field | Value |`,
    `|-------|-------|`,
    `| Artifact file | ${websiteFile} |`,
    `| Snapshot count | ${snapshotCount} |`,
    `| Website section grade | ${options.website_section_grade || "SAFE UNKNOWN"} |`,
    "",
    "Full competitor and snapshot objects remain in session artifacts — this pack is a projection only.",
    "",
  ].join("\n");
}

function buildResearchPackDraft(manifest, serpResult, options = {}) {
  const scope = manifest.scope;
  const competitorSection =
    options.competitor_observations ||
    discoverFromSerp(serpResult, {
      queries_executed: manifest.queries?.queries_executed,
      rules: options.discovery_rules,
      rulesPath: options.discovery_rules_path,
    });
  const websiteIndex = options.website_snapshots || null;
  const landingIndex = options.landing_observations || null;
  const hasWebsiteCapture =
    websiteIndex && Array.isArray(websiteIndex.snapshots) && websiteIndex.snapshots.length > 0;
  const hasLandingAnalysis =
    landingIndex && Array.isArray(landingIndex.landings) && landingIndex.landings.length > 0;
  const migPhase =
    options.mig_phase ||
    manifest.mig_phase ||
    (hasLandingAnalysis ? "3" : hasWebsiteCapture ? "3" : competitorSection.competitors.length > 0 ? "2" : "1");

  const lines = [
    "# MIG Research Pack — Draft",
    "",
    "## Session Header",
    "",
    `| Field | Value |`,
    `|-------|-------|`,
    `| Session ID | ${manifest.session_id} |`,
    `| Stage | draft |`,
    `| Created | ${manifest.created_at} |`,
    `| Operator | ${manifest.operator_id} |`,
    `| Niche | ${scope.niche} |`,
    `| Region | ${scope.region} |`,
    `| City | ${scope.city || "SAFE UNKNOWN"} |`,
    `| Business type | ${scope.business_type} |`,
    `| Search engine | ${scope.search_engine} |`,
    `| Device | ${scope.device} |`,
    `| SERP mode | ${serpResult.source_mode} |`,
    `| MIG phase | ${migPhase} |`,
    "",
    "## Queries",
    "",
    "### Seed queries",
    "",
    bulletList(manifest.queries.seed_queries),
    "",
    "### Query used (single SERP pass)",
    "",
    `- ${manifest.queries.query_used}`,
    "",
    formatQueryCoverageNotes(manifest, competitorSection),
    "## SERP Summary",
    "",
    `| Field | Value |`,
    `|-------|-------|`,
    `| Query | ${serpResult.query} |`,
    `| Captured at | ${serpResult.captured_at} |`,
    `| SERP type | ${serpResult.serp_type} |`,
    `| Maps / local pack | ${serpResult.maps_local_pack} |`,
    `| Ads | ${formatAdsSummary(serpResult.ads_blocks)} |`,
    "",
    "### Aggregators",
    "",
    bulletList(serpResult.aggregators),
    "",
    "### Marketplaces",
    "",
    bulletList(serpResult.marketplaces),
    "",
    "### Offer patterns",
    "",
    bulletList(serpResult.offer_patterns),
    "",
    "### CTA patterns",
    "",
    bulletList(serpResult.cta_patterns),
    "",
    "### Landing observations",
    "",
    bulletList(serpResult.landing_observations),
    "",
    "### Organic results (normalized)",
    "",
    serpResult.organic_results && serpResult.organic_results.length > 0
      ? serpResult.organic_results
          .slice(0, 10)
          .map((row, index) => {
            const title = row.title || row.name || "SAFE UNKNOWN";
            const url = row.url || row.link || "SAFE UNKNOWN";
            return `${index + 1}. ${title} — ${url}`;
          })
          .join("\n")
      : "SAFE UNKNOWN — no organic results in spine payload",
    "",
    formatCompetitorObservationsMarkdown(competitorSection),
    formatDiscoveryCoverageBlock(competitorSection),
    formatRecurrenceSummary(competitorSection),
    ...(hasLandingAnalysis
      ? [
          landingIndex.analysis_phase === "landing_analysis_v2"
            ? formatLandingObservationBlocksV2(landingIndex)
            : formatLandingObservationBlocks(landingIndex, options.website_acquisition_rules),
          "",
        ]
      : hasWebsiteCapture
        ? [
            formatWebsiteObservationBlocks(websiteIndex, options.website_acquisition_rules),
            "",
          ]
        : []),
    formatArtifactRegistryBlock(manifest, competitorSection, {
      competitors_artifact_file: options.competitors_artifact_file,
      website_snapshots_file: options.website_snapshots_file,
      landing_observations_file: options.landing_observations_file,
      website_snapshot_count: websiteIndex?.snapshots?.length ?? 0,
      landing_count: landingIndex?.landings?.length ?? 0,
      website_section_grade: websiteIndex?.section_evidence_grade,
    }),
    "## SAFE UNKNOWN",
    "",
    bulletList(serpResult.safe_unknown),
    "",
    ...(competitorSection.safe_unknown && competitorSection.safe_unknown.length
      ? ["### Competitor discovery gaps", "", bulletList(competitorSection.safe_unknown), ""]
      : []),
    ...(landingIndex?.safe_unknown?.length
      ? ["### Landing analysis gaps", "", bulletList(landingIndex.safe_unknown), ""]
      : []),
    ...(websiteIndex?.safe_unknown?.length
      ? ["### Website acquisition gaps", "", bulletList(websiteIndex.safe_unknown), ""]
      : !hasWebsiteCapture
        ? [
            "### Website acquisition gaps",
            "",
            "- Website acquisition not executed — Phase 3 capture pending",
            "",
          ]
        : []),
    ...(hasWebsiteCapture && !hasLandingAnalysis
      ? [
          "### Landing analysis gaps",
          "",
          "- Landing Analysis pass not executed — structured landing analysis pending (legacy snapshot projection used)",
          "",
        ]
      : []),
    "## Status",
    "",
    "Status: **draft**",
    "",
    hasLandingAnalysis
      ? "This pack includes SERP, competitor discovery, website capture, and Landing Analysis projections. Human review required before approval or ORCA handoff."
      : hasWebsiteCapture
        ? "This pack includes SERP, competitor discovery, and website capture projections (legacy snapshot path). Human review required before approval or ORCA handoff."
        : "This pack is a SERP-only spine draft. Human review required before approval or ORCA handoff.",
    "",
  ];

  return `${lines.join("\n")}\n`;
}

module.exports = {
  buildResearchPackDraft,
  discoverFromSerp,
  formatCompetitorObservationsMarkdown,
  formatWebsiteCaptureSummary,
  formatWebsiteObservationBlocks,
  formatLandingObservationBlocks,
};
