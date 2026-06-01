"use strict";

const fs = require("fs");
const path = require("path");

const { loadRules, extractDomain } = require("./discover-from-serp");

const GRADE_ORDER = { A: 0, B: 1, C: 2, D: 3, X: 4 };
const DEFAULT_MIN_DISTINCT_QUERIES = 2;

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

function uniqueStrings(values) {
  return [...new Set(values.filter(Boolean))];
}

function evidenceGradeForSerpMode(sourceMode) {
  if (sourceMode === "manual" || sourceMode === "provider") {
    return "B";
  }
  if (sourceMode === "fallback") {
    return "D";
  }
  return "C";
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

function buildEvidenceItem(competitorId, seq, context, row, grade) {
  return {
    evidence_id: `${competitorId}-e${String(seq).padStart(2, "0")}`,
    source_type: sourceTypeForSerpMode(context.source_mode),
    artifact_ref: context.artifact_ref,
    observed_at: context.captured_at,
    grade,
    surface_detail: {
      query_id: context.query_id,
      query_text: context.query_text,
      position: row.position,
      url: row.url || row.link || null,
      title: row.title || row.name || null,
      snippet: row.snippet || null,
    },
  };
}

function synthesizeLegacyIndex(serpResult) {
  const sessionId = serpResult.session_id || "unknown-session";
  const queryId = serpResult.query_id || "q01";
  return {
    schema_version: "0.1",
    session_id: sessionId,
    aggregation_model: "legacy_single",
    entries: [
      {
        query_id: queryId,
        query_text: serpResult.query || "SAFE UNKNOWN",
        role: "primary",
        artifact_path: "serp_result.json",
        captured_at: serpResult.captured_at,
        source_mode: serpResult.source_mode,
        status: "captured",
      },
    ],
    queries_declared: [queryId],
    queries_executed: [queryId],
  };
}

function loadSerpIndex(indexPathOrObject, baseDir) {
  const index =
    typeof indexPathOrObject === "string"
      ? JSON.parse(fs.readFileSync(indexPathOrObject, "utf8"))
      : indexPathOrObject;
  const resolvedBase = baseDir || (typeof indexPathOrObject === "string" ? path.dirname(indexPathOrObject) : null);
  return { index, baseDir: resolvedBase };
}

function loadSerpForEntry(entry, baseDir, serpByQueryId) {
  const queryId = entry.query_id;
  if (serpByQueryId && serpByQueryId[queryId]) {
    return serpByQueryId[queryId];
  }
  if (!baseDir || !entry.artifact_path) {
    return null;
  }
  const filePath = path.join(baseDir, entry.artifact_path);
  if (!fs.existsSync(filePath)) {
    return null;
  }
  return JSON.parse(fs.readFileSync(filePath, "utf8"));
}

function computeDiscoveryCoverage(serpIndex) {
  const declared =
    serpIndex.queries_declared ||
    serpIndex.entries.map((e) => e.query_id);
  const executed = serpIndex.entries
    .filter((e) => e.status === "captured")
    .map((e) => e.query_id);
  const executedSet = new Set(executed);
  const missing = declared.filter((id) => !executedSet.has(id));

  let queryCoverage = "none";
  if (executed.length > 0 && missing.length === 0) {
    queryCoverage = "full";
  } else if (executed.length > 0) {
    queryCoverage = "partial";
  }

  return {
    queries_declared: declared,
    queries_executed: executed,
    queries_missing: missing,
    query_coverage: queryCoverage,
  };
}

function collectOrganicHits(serpResult, entry, rules, topN) {
  const organic = Array.isArray(serpResult.organic_results) ? serpResult.organic_results : [];
  const queryId = entry.query_id;
  const queryText = entry.query_text || serpResult.query || "SAFE UNKNOWN";
  const artifactRef =
    entry.artifact_path && entry.artifact_path !== "serp_result.json"
      ? entry.artifact_path.replace(/\\/g, "/")
      : entry.artifact_path === "serp_result.json"
        ? "serp_result"
        : `serp_results/${queryId}.json`;

  const hits = [];
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
    hits.push({
      query_id: queryId,
      query_text: queryText,
      domain,
      displayName,
      domainKey: domain || `name:${String(displayName).toLowerCase()}`,
      position,
      row,
      artifactRef,
      captured_at: serpResult.captured_at,
      source_mode: serpResult.source_mode,
      region: serpResult.region || "SAFE UNKNOWN",
      city: serpResult.city ?? null,
      grade: evidenceGradeForSerpMode(serpResult.source_mode),
    });
  });
  return hits;
}

function discoverFromSerpBundle(serpIndex, options = {}) {
  const rules = options.rules || loadRules(options.rulesPath);
  const topN = rules.top_n ?? 10;
  const minDistinctQueries =
    rules.min_distinct_queries_for_repeated_domain ?? DEFAULT_MIN_DISTINCT_QUERIES;
  const baseDir = options.baseDir || null;
  const serpByQueryId = options.serp_results || options.serpByQueryId || null;
  const discoveryPassAt = new Date().toISOString();
  const sessionId = serpIndex.session_id || "unknown-session";
  const sectionSafeUnknown = [...(serpIndex.safe_unknown || [])];

  const coverage = computeDiscoveryCoverage(serpIndex);
  const capturedEntries = serpIndex.entries.filter((e) => e.status === "captured");
  const discoveryMode =
    serpIndex.aggregation_model === "legacy_single" || capturedEntries.length <= 1
      ? "single"
      : "multi_query";

  if (capturedEntries.length === 0) {
    sectionSafeUnknown.push(
      "No captured SERP queries — competitor discovery produced empty set"
    );
    return wrapBundleSection({
      sessionId,
      serpIndex,
      discoveryPassAt,
      competitors: [],
      sectionSafeUnknown,
      coverage,
      discoveryMode,
      serpCap: "X",
    });
  }

  if (capturedEntries.length < minDistinctQueries) {
    sectionSafeUnknown.push(
      "Only one SERP captured — cross-query recurrence not evaluated"
    );
  }

  const entityByKey = new Map();
  const domainOrganicQueryIds = new Map();
  let seq = 0;
  let serpCap = "A";

  for (const entry of capturedEntries) {
    const serpResult = loadSerpForEntry(entry, baseDir, serpByQueryId);
    if (!serpResult) {
      sectionSafeUnknown.push(
        `serp_index lists ${entry.query_id} but SERP file missing (${entry.artifact_path || "unknown"})`
      );
      continue;
    }

    const baseGrade = evidenceGradeForSerpMode(serpResult.source_mode);
    if (GRADE_ORDER[baseGrade] > GRADE_ORDER[serpCap]) {
      serpCap = baseGrade;
    }

    const hits = collectOrganicHits(serpResult, entry, rules, topN);
    if (hits.length === 0) {
      continue;
    }

    for (const hit of hits) {
      let entity = entityByKey.get(hit.domainKey);
      if (!entity) {
        seq += 1;
        const competitorId = `${sessionId}-c${String(seq).padStart(3, "0")}`;
        entity = {
          competitor_id: competitorId,
          display_name: hit.displayName,
          primary_domain: hit.domain,
          domains_observed: hit.domain ? [hit.domain] : [],
          surface_types: [],
          discovery_sources: [],
          first_seen_query: hit.query_text,
          queries_seen: [],
          query_ids_seen: [],
          discovery_rules_fired: [],
          discovery_strength: "single",
          region: hit.region,
          city: hit.city,
          evidence: [],
          evidence_grade: hit.grade,
          capture_time: hit.captured_at,
          updated_at: hit.captured_at,
          _surfaceKinds: new Set(),
          _organicQueryIds: new Set(),
        };
        entityByKey.set(hit.domainKey, entity);
      }

      if (!entity.queries_seen.includes(hit.query_text)) {
        entity.queries_seen.push(hit.query_text);
      }
      if (!entity.query_ids_seen.includes(hit.query_id)) {
        entity.query_ids_seen.push(hit.query_id);
      }

      if (!entity.discovery_rules_fired.includes("rule_serp_organic_top_n")) {
        entity.discovery_rules_fired.push("rule_serp_organic_top_n");
      }

      if (!entity.surface_types.includes("serp_organic")) {
        entity.surface_types.push("serp_organic");
      }
      entity._surfaceKinds.add("serp_organic");

      if (hit.domain) {
        const domainQueries = domainOrganicQueryIds.get(hit.domain) || new Set();
        domainQueries.add(hit.query_id);
        domainOrganicQueryIds.set(hit.domain, domainQueries);
        entity._organicQueryIds.add(hit.query_id);

        if (domainInList(hit.domain, rules.aggregator_domains)) {
          if (!entity.surface_types.includes("aggregator")) {
            entity.surface_types.push("aggregator");
          }
          entity._surfaceKinds.add("aggregator");
          if (!entity.discovery_rules_fired.includes("rule_aggregator_domain")) {
            entity.discovery_rules_fired.push("rule_aggregator_domain");
          }
        }
        if (domainInList(hit.domain, rules.marketplace_domains)) {
          if (!entity.surface_types.includes("marketplace_listing")) {
            entity.surface_types.push("marketplace_listing");
          }
          entity._surfaceKinds.add("marketplace_listing");
          if (!entity.discovery_rules_fired.includes("rule_marketplace_domain")) {
            entity.discovery_rules_fired.push("rule_marketplace_domain");
          }
        }
        if (domainInList(hit.domain, rules.informational_domains)) {
          if (!entity.surface_types.includes("informational_surface")) {
            entity.surface_types.push("informational_surface");
          }
          entity._surfaceKinds.add("informational_surface");
        }
        if (!entity.domains_observed.includes(hit.domain)) {
          entity.domains_observed.push(hit.domain);
        }
        if (!entity.primary_domain) {
          entity.primary_domain = hit.domain;
        }
      }

      const sourceEntry = {
        source_kind: "serp_organic",
        artifact_ref: hit.artifactRef,
        observed_at: hit.captured_at,
        query_id: hit.query_id,
      };
      const hasSource = entity.discovery_sources.some(
        (s) =>
          s.source_kind === sourceEntry.source_kind &&
          s.artifact_ref === sourceEntry.artifact_ref &&
          s.query_id === sourceEntry.query_id
      );
      if (!hasSource) {
        entity.discovery_sources.push(sourceEntry);
      }

      const evidenceSeq = entity.evidence.length + 1;
      entity.evidence.push(
        buildEvidenceItem(
          entity.competitor_id,
          evidenceSeq,
          {
            query_id: hit.query_id,
            query_text: hit.query_text,
            artifact_ref: hit.artifactRef,
            captured_at: hit.captured_at,
            source_mode: hit.source_mode,
          },
          { ...hit.row, position: hit.position },
          hit.grade
        )
      );
      entity.evidence_grade = worstGrade(entity.evidence.map((e) => e.grade));
      if (hit.captured_at > entity.updated_at) {
        entity.updated_at = hit.captured_at;
      }
      if (hit.captured_at < entity.capture_time) {
        entity.capture_time = hit.captured_at;
      }
    }
  }

  const competitors = [];
  for (const entity of entityByKey.values()) {
    if (entity._surfaceKinds.size >= 2) {
      if (!entity.discovery_rules_fired.includes("rule_multi_surface")) {
        entity.discovery_rules_fired.push("rule_multi_surface");
      }
      entity.discovery_strength = "multi_surface";
    }

    const organicQueryCount = entity._organicQueryIds.size;
    if (
      entity.primary_domain &&
      organicQueryCount >= minDistinctQueries &&
      capturedEntries.length >= minDistinctQueries
    ) {
      const queryIds = [...entity._organicQueryIds].sort();
      if (!entity.discovery_rules_fired.includes("rule_repeated_domain")) {
        entity.discovery_rules_fired.push("rule_repeated_domain");
      }
      if (entity.discovery_strength === "single") {
        entity.discovery_strength = "repeated";
      }
      entity.recurrence = {
        distinct_query_count: queryIds.length,
        query_ids: queryIds,
      };
    }

    delete entity._surfaceKinds;
    delete entity._organicQueryIds;
    if (entity.query_ids_seen.length === 0) {
      delete entity.query_ids_seen;
    }
    competitors.push(entity);
  }

  if (competitors.length === 0 && capturedEntries.length > 0) {
    sectionSafeUnknown.push(
      "SERP organic rows present but no entities passed exclusion rules (search engines / empty rows)"
    );
  }

  const querySetRef =
    serpIndex.query_set?.map((q) => q.query_text).join(" | ") ||
    uniqueStrings(capturedEntries.map((e) => e.query_text)).join(" | ") ||
    "SAFE UNKNOWN";

  return wrapBundleSection({
    sessionId,
    serpIndex,
    discoveryPassAt,
    competitors,
    sectionSafeUnknown,
    coverage,
    discoveryMode,
    serpCap,
    querySetRef,
  });
}

function wrapBundleSection({
  discoveryPassAt,
  competitors,
  sectionSafeUnknown,
  coverage,
  discoveryMode,
  serpCap,
  querySetRef,
}) {
  const competitorGrades = competitors.map((c) => c.evidence_grade);
  let sectionGrade = competitors.length ? worstGrade(competitorGrades) : "X";
  if (GRADE_ORDER[sectionGrade] < GRADE_ORDER[serpCap]) {
    sectionGrade = serpCap;
  }

  let sectionCoverage = "unknown";
  if (competitors.length === 0) {
    sectionCoverage = coverage.query_coverage === "none" ? "minimal" : "partial";
  } else if (competitors.every((c) => GRADE_ORDER[c.evidence_grade] <= GRADE_ORDER.C)) {
    sectionCoverage = coverage.query_coverage === "full" ? "complete" : "partial";
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
    discovery_mode: discoveryMode,
    query_set_ref: querySetRef || "SAFE UNKNOWN",
    discovery_coverage: coverage,
    competitors,
    section_evidence_grade: sectionGrade,
    section_coverage: sectionCoverage,
    safe_unknown: safeUnknown.length ? safeUnknown : undefined,
  };
}

function discoverFromSerpBundlePaths(sessionDir, options = {}) {
  const indexPath = path.join(sessionDir, "serp_index.json");
  let serpIndex;
  let baseDir = sessionDir;

  if (fs.existsSync(indexPath)) {
    serpIndex = JSON.parse(fs.readFileSync(indexPath, "utf8"));
  } else {
    const legacyPath = path.join(sessionDir, "serp_result.json");
    if (!fs.existsSync(legacyPath)) {
      throw new Error("No serp_index.json or serp_result.json in session directory");
    }
    const serpResult = JSON.parse(fs.readFileSync(legacyPath, "utf8"));
    serpIndex = synthesizeLegacyIndex(serpResult);
    if (options.serp_results) {
      return discoverFromSerpBundle(serpIndex, { ...options, baseDir });
    }
    return discoverFromSerpBundle(serpIndex, { ...options, baseDir });
  }

  return discoverFromSerpBundle(serpIndex, { ...options, baseDir });
}

module.exports = {
  discoverFromSerpBundle,
  discoverFromSerpBundlePaths,
  loadSerpIndex,
  synthesizeLegacyIndex,
  computeDiscoveryCoverage,
};
