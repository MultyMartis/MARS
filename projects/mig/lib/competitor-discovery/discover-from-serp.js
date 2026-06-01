"use strict";

const fs = require("fs");
const path = require("path");

const DEFAULT_RULES_PATH = path.join(
  __dirname,
  "..",
  "..",
  "config",
  "competitor-discovery-rules-v0.json"
);

const GRADE_ORDER = { A: 0, B: 1, C: 2, D: 3, X: 4 };

function loadRules(rulesPath) {
  const resolved = rulesPath || DEFAULT_RULES_PATH;
  const raw = fs.readFileSync(resolved, "utf8");
  return JSON.parse(raw);
}

function extractDomain(url) {
  if (!url || typeof url !== "string") {
    return null;
  }
  try {
    const normalized = url.startsWith("http") ? url : `https://${url}`;
    const parsed = new URL(normalized);
    let host = parsed.hostname.toLowerCase();
    if (host.startsWith("www.")) {
      host = host.slice(4);
    }
    return host || null;
  } catch {
    return null;
  }
}

function isSearchEngineDomain(domain, rules) {
  if (!domain) {
    return false;
  }
  const blocked = rules.exclude_search_engine_domains || [];
  return blocked.some((entry) => {
    const needle = entry.replace(/^www\./, "").toLowerCase();
    return domain === needle;
  });
}

function domainInList(domain, list) {
  if (!domain || !Array.isArray(list)) {
    return false;
  }
  return list.some((entry) => {
    const needle = String(entry).replace(/^www\./, "").toLowerCase();
    return domain === needle || domain.endsWith(`.${needle}`);
  });
}

function worstGrade(grades) {
  if (!grades.length) {
    return "X";
  }
  return grades.reduce((worst, grade) =>
    GRADE_ORDER[grade] > GRADE_ORDER[worst] ? grade : worst
  );
}

function sourceTypeForSerpMode(sourceMode) {
  if (sourceMode === "manual") {
    return "human";
  }
  if (sourceMode === "provider") {
    return "serp_provider";
  }
  return "filesystem_artifact";
}

function evidenceGradeForSerpMode(sourceMode) {
  if (sourceMode === "manual") {
    return "B";
  }
  if (sourceMode === "provider") {
    return "B";
  }
  if (sourceMode === "fallback") {
    return "D";
  }
  return "C";
}

function uniqueStrings(values) {
  return [...new Set(values.filter(Boolean))];
}

function buildEvidenceItem(competitorId, seq, serpResult, row, grade) {
  const observedAt = serpResult.captured_at;
  return {
    evidence_id: `${competitorId}-e${String(seq).padStart(2, "0")}`,
    source_type: sourceTypeForSerpMode(serpResult.source_mode),
    artifact_ref: "serp_result",
    observed_at: observedAt,
    grade,
    surface_detail: {
      position: row.position,
      url: row.url || row.link || null,
      title: row.title || row.name || null,
      snippet: row.snippet || null,
    },
  };
}

function discoverFromSerp(serpResult, options = {}) {
  const rules = options.rules || loadRules(options.rulesPath);
  const topN = rules.top_n ?? 10;
  const sessionId = serpResult.session_id || "unknown-session";
  const query = serpResult.query || "SAFE UNKNOWN";
  const region = serpResult.region || "SAFE UNKNOWN";
  const city = serpResult.city ?? null;
  const discoveryPassAt = new Date().toISOString();
  const baseGrade = evidenceGradeForSerpMode(serpResult.source_mode);
  const sectionSafeUnknown = [];

  const organic = Array.isArray(serpResult.organic_results) ? serpResult.organic_results : [];

  if (organic.length === 0) {
    sectionSafeUnknown.push(
      "No organic SERP rows — competitor discovery produced empty set (rule_serp_organic_top_n had no matches)"
    );
    if (serpResult.source_mode === "fallback") {
      sectionSafeUnknown.push(
        "SERP fallback mode — competitor section empty pending human SERP capture"
      );
    }
    return wrapSection({
      sessionId,
      query,
      discoveryPassAt,
      competitors: [],
      sectionSafeUnknown,
      serpResult,
      baseGrade,
    });
  }

  const entityByDomain = new Map();
  let seq = 0;

  organic.forEach((row, index) => {
    const position = row.position ?? index + 1;
    if (position > topN) {
      return;
    }

    const url = row.url || row.link || null;
    const domain = extractDomain(url);
    const displayName = row.title || row.name || domain || null;

    if (!displayName && !domain) {
      return;
    }
    if (domain && isSearchEngineDomain(domain, rules)) {
      return;
    }

    const domainKey = domain || `name:${String(displayName).toLowerCase()}`;
    let entity = entityByDomain.get(domainKey);

    if (!entity) {
      seq += 1;
      const competitorId = `${sessionId}-c${String(seq).padStart(3, "0")}`;
      entity = {
        competitor_id: competitorId,
        display_name: displayName,
        primary_domain: domain,
        domains_observed: domain ? [domain] : [],
        surface_types: [],
        discovery_sources: [],
        first_seen_query: query,
        queries_seen: [query],
        discovery_rules_fired: [],
        discovery_strength: "single",
        region,
        city,
        evidence: [],
        evidence_grade: baseGrade,
        capture_time: serpResult.captured_at,
        _domainKey: domainKey,
        _surfaceKinds: new Set(),
      };
      entityByDomain.set(domainKey, entity);
    }

    const rulesFired = entity.discovery_rules_fired;
    if (!rulesFired.includes("rule_serp_organic_top_n")) {
      rulesFired.push("rule_serp_organic_top_n");
    }

    if (!entity.surface_types.includes("serp_organic")) {
      entity.surface_types.push("serp_organic");
    }
    entity._surfaceKinds.add("serp_organic");

    if (domain && domainInList(domain, rules.aggregator_domains)) {
      if (!entity.surface_types.includes("aggregator")) {
        entity.surface_types.push("aggregator");
      }
      entity._surfaceKinds.add("aggregator");
      if (!rulesFired.includes("rule_aggregator_domain")) {
        rulesFired.push("rule_aggregator_domain");
      }
    }

    if (domain && domainInList(domain, rules.marketplace_domains)) {
      if (!entity.surface_types.includes("marketplace_listing")) {
        entity.surface_types.push("marketplace_listing");
      }
      entity._surfaceKinds.add("marketplace_listing");
      if (!rulesFired.includes("rule_marketplace_domain")) {
        rulesFired.push("rule_marketplace_domain");
      }
    }

    if (domain && domainInList(domain, rules.informational_domains)) {
      if (!entity.surface_types.includes("informational_surface")) {
        entity.surface_types.push("informational_surface");
      }
      entity._surfaceKinds.add("informational_surface");
    }

    const sourceEntry = {
      source_kind: "serp_organic",
      artifact_ref: "serp_result",
      observed_at: serpResult.captured_at,
    };
    const hasSource = entity.discovery_sources.some(
      (s) => s.source_kind === sourceEntry.source_kind && s.artifact_ref === sourceEntry.artifact_ref
    );
    if (!hasSource) {
      entity.discovery_sources.push(sourceEntry);
    }

    const evidenceSeq = entity.evidence.length + 1;
    entity.evidence.push(
      buildEvidenceItem(entity.competitor_id, evidenceSeq, serpResult, { ...row, position }, baseGrade)
    );
    entity.evidence_grade = worstGrade(entity.evidence.map((e) => e.grade));
    if (domain && !entity.domains_observed.includes(domain)) {
      entity.domains_observed.push(domain);
    }
    if (!entity.primary_domain && domain) {
      entity.primary_domain = domain;
    }
  });

  const domainQueryHits = new Map();
  for (const entity of entityByDomain.values()) {
    if (entity.primary_domain) {
      const hits = domainQueryHits.get(entity.primary_domain) || new Set();
      hits.add(query);
      domainQueryHits.set(entity.primary_domain, hits);
    }
  }

  const competitors = [];
  for (const entity of entityByDomain.values()) {
    if (entity._surfaceKinds.size >= 2) {
      if (!entity.discovery_rules_fired.includes("rule_multi_surface")) {
        entity.discovery_rules_fired.push("rule_multi_surface");
      }
      entity.discovery_strength = "multi_surface";
    }

    const queryHits = entity.primary_domain
      ? domainQueryHits.get(entity.primary_domain)
      : null;
    if (queryHits && queryHits.size >= 2) {
      if (!entity.discovery_rules_fired.includes("rule_repeated_domain")) {
        entity.discovery_rules_fired.push("rule_repeated_domain");
      }
      if (entity.discovery_strength === "single") {
        entity.discovery_strength = "repeated";
      }
    }

    const extraQueries = options.queries_executed;
    if (Array.isArray(extraQueries) && extraQueries.length >= 2 && entity.primary_domain) {
      const appearances = extraQueries.filter((q) =>
        organic.some((row) => {
          const rowQuery = row.query || query;
          const rowDomain = extractDomain(row.url || row.link);
          return rowQuery === q && rowDomain === entity.primary_domain;
        })
      );
      if (appearances.length >= 2) {
        entity.queries_seen = uniqueStrings([...entity.queries_seen, ...appearances]);
        if (!entity.discovery_rules_fired.includes("rule_repeated_domain")) {
          entity.discovery_rules_fired.push("rule_repeated_domain");
        }
        if (entity.discovery_strength === "single") {
          entity.discovery_strength = "repeated";
        }
      }
    }

    delete entity._domainKey;
    delete entity._surfaceKinds;
    competitors.push(entity);
  }

  if (competitors.length === 0) {
    sectionSafeUnknown.push(
      "SERP organic rows present but no entities passed exclusion rules (search engines / empty rows)"
    );
  }

  return wrapSection({
    sessionId,
    query,
    discoveryPassAt,
    competitors,
    sectionSafeUnknown,
    serpResult,
    baseGrade,
  });
}

function wrapSection({
  query,
  discoveryPassAt,
  competitors,
  sectionSafeUnknown,
  serpResult,
  baseGrade,
}) {
  const serpCap = evidenceGradeForSerpMode(serpResult.source_mode);
  const competitorGrades = competitors.map((c) => c.evidence_grade);
  let sectionGrade = competitors.length
    ? worstGrade(competitorGrades)
    : "X";
  if (GRADE_ORDER[sectionGrade] < GRADE_ORDER[serpCap]) {
    sectionGrade = serpCap;
  }

  let sectionCoverage = "unknown";
  if (competitors.length === 0) {
    sectionCoverage = serpResult.source_mode === "fallback" ? "minimal" : "partial";
  } else if (competitors.every((c) => GRADE_ORDER[c.evidence_grade] <= GRADE_ORDER.C)) {
    sectionCoverage = "complete";
  } else {
    sectionCoverage = "partial";
  }

  const safeUnknown = [...sectionSafeUnknown];
  if (competitors.length === 0 && safeUnknown.length === 0) {
    safeUnknown.push("No competitor entities discovered from SERP organic results");
  }

  return {
    section_id: "competitor_observations",
    schema_version: "0",
    discovery_pass_at: discoveryPassAt,
    discovery_phase: 2,
    query_set_ref: query,
    competitors,
    section_evidence_grade: sectionGrade,
    section_coverage: sectionCoverage,
    safe_unknown: safeUnknown.length ? safeUnknown : undefined,
  };
}

function formatCompetitorObservationsMarkdown(section) {
  const lines = [
    "## Competitor Observations",
    "",
    `| Field | Value |`,
    `|-------|-------|`,
    `| Discovery pass | ${section.discovery_pass_at} |`,
    `| Phase | ${section.discovery_phase} |`,
    `| Query ref | ${section.query_set_ref} |`,
    `| Section grade | ${section.section_evidence_grade} |`,
    `| Coverage | ${section.section_coverage} |`,
    `| Competitor count | ${section.competitors.length} |`,
    "",
  ];

  if (!section.competitors.length) {
    lines.push("### Competitors", "", "- SAFE UNKNOWN — no entities discovered", "");
    if (section.safe_unknown && section.safe_unknown.length) {
      lines.push("### Discovery gaps", "");
      section.safe_unknown.forEach((entry) => lines.push(`- ${entry}`));
      lines.push("");
    }
    return lines.join("\n");
  }

  lines.push(
    "| ID | Name | Domain | Types | Strength | Grade | First query |",
    "|----|------|--------|-------|----------|-------|-------------|"
  );

  for (const c of section.competitors) {
    const types = c.surface_types.join(", ");
    const rules = c.discovery_rules_fired.join(", ");
    lines.push(
      `| ${c.competitor_id} | ${c.display_name} | ${c.primary_domain || "—"} | ${types} | ${c.discovery_strength} | ${c.evidence_grade} | ${c.first_seen_query} |`
    );
    lines.push("", `**Rules:** ${rules}`, "");
  }

  if (section.safe_unknown && section.safe_unknown.length) {
    lines.push("### Discovery gaps", "");
    section.safe_unknown.forEach((entry) => lines.push(`- ${entry}`));
    lines.push("");
  }

  return lines.join("\n");
}

module.exports = {
  loadRules,
  extractDomain,
  discoverFromSerp,
  formatCompetitorObservationsMarkdown,
};
