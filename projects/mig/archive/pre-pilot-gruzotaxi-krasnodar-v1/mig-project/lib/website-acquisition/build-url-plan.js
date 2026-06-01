"use strict";

const fs = require("fs");
const path = require("path");

const DEFAULT_RULES_PATH = path.join(
  __dirname,
  "..",
  "..",
  "config",
  "website-acquisition-rules-v0.json"
);

function loadRules(rulesPath) {
  const resolved = rulesPath || DEFAULT_RULES_PATH;
  return JSON.parse(fs.readFileSync(resolved, "utf8"));
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

function normalizeHomepageUrl(domain) {
  if (!domain) {
    return null;
  }
  return `https://${domain}/`;
}

function pickSerpUrl(competitor) {
  for (const item of competitor.evidence || []) {
    const url = item.surface_detail?.url;
    if (url) {
      const evidenceDomain = extractDomain(url);
      if (
        !competitor.primary_domain ||
        !evidenceDomain ||
        evidenceDomain === competitor.primary_domain ||
        evidenceDomain.endsWith(`.${competitor.primary_domain}`)
      ) {
        return url;
      }
    }
  }
  return null;
}

function pickCaptureUrlSeed(signals, competitor) {
  const seeds = signals?.capture_urls;
  if (!Array.isArray(seeds)) {
    return null;
  }
  for (const entry of seeds) {
    if (typeof entry === "string" && entry) {
      return entry;
    }
    if (entry && typeof entry === "object") {
      if (entry.competitor_id && entry.competitor_id !== competitor.competitor_id) {
        continue;
      }
      if (entry.domain && competitor.primary_domain && entry.domain !== competitor.primary_domain) {
        continue;
      }
      if (entry.url) {
        return entry.url;
      }
    }
  }
  return null;
}

function shouldSkipCompetitor(competitor, rules) {
  const skipTypes = rules.skip_surface_types || [];
  const surfaces = competitor.surface_types || [];
  return surfaces.some((type) => skipTypes.includes(type));
}

function resolveRequestedUrl(competitor, signals) {
  const fromSeed = pickCaptureUrlSeed(signals, competitor);
  if (fromSeed) {
    return { url: fromSeed, page_role: "operator_seed", source: "capture_urls" };
  }

  const serpUrl = pickSerpUrl(competitor);
  if (serpUrl) {
    const sameDomain =
      !competitor.primary_domain ||
      extractDomain(serpUrl) === competitor.primary_domain;
    return {
      url: serpUrl,
      page_role: sameDomain ? "homepage" : "serp_landing",
      source: "serp_evidence",
    };
  }

  const homepage = normalizeHomepageUrl(competitor.primary_domain);
  if (homepage) {
    return { url: homepage, page_role: "homepage", source: "primary_domain" };
  }

  return null;
}

/**
 * Build deterministic URL capture plan from competitors artifact envelope.
 * @param {object} competitorsArtifact - competitors.json envelope
 * @param {{ signals?: object, url_cap?: number, rules?: object, rulesPath?: string }} [options]
 */
function buildUrlPlan(competitorsArtifact, options = {}) {
  const rules = options.rules || loadRules(options.rulesPath);
  const sessionId = competitorsArtifact.session_id || "unknown-session";
  const section = competitorsArtifact.competitor_observations || {};
  const competitors = Array.isArray(section.competitors) ? section.competitors : [];
  const signals = options.signals || {};
  const cap = Math.min(
    options.url_cap ?? rules.url_cap_default ?? 5,
    rules.url_cap_hard_max ?? 10
  );

  const plan = [];
  const skipped = [];
  let seq = 0;

  for (const competitor of competitors) {
    if (plan.length >= cap) {
      skipped.push({
        competitor_id: competitor.competitor_id,
        reason: "session_url_cap_reached",
      });
      continue;
    }

    if (shouldSkipCompetitor(competitor, rules)) {
      skipped.push({
        competitor_id: competitor.competitor_id,
        reason: "skip_surface_type",
        surface_types: competitor.surface_types,
      });
      continue;
    }

    const resolved = resolveRequestedUrl(competitor, signals);
    if (!resolved) {
      skipped.push({
        competitor_id: competitor.competitor_id,
        reason: "no_resolvable_url",
      });
      continue;
    }

    seq += 1;
    const snapshotId = `${sessionId}-ws${String(seq).padStart(3, "0")}`;
    plan.push({
      snapshot_id: snapshotId,
      competitor_id: competitor.competitor_id,
      domain: extractDomain(resolved.url) || competitor.primary_domain || "unknown",
      requested_url: resolved.url,
      page_role: resolved.page_role,
      url_source: resolved.source,
    });
  }

  return {
    session_id: sessionId,
    url_cap: cap,
    planned_count: plan.length,
    skipped,
    entries: plan,
  };
}

module.exports = {
  loadRules,
  extractDomain,
  buildUrlPlan,
  resolveRequestedUrl,
  shouldSkipCompetitor,
};
