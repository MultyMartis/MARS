"use strict";

const fs = require("fs");
const path = require("path");
const { extractDomain } = require("./build-url-plan");
const { extractLinks, stripTags } = require("./extract-page-facts");

const DEFAULT_RULES_PATH = path.join(
  __dirname,
  "..",
  "..",
  "config",
  "site-surface-discovery-rules-v0.json"
);

function loadSurfaceRules(rulesPath) {
  const resolved = rulesPath || DEFAULT_RULES_PATH;
  return JSON.parse(fs.readFileSync(resolved, "utf8"));
}

function normalizePathname(url) {
  try {
    const parsed = new URL(url);
    let p = parsed.pathname || "/";
    if (p.length > 1 && p.endsWith("/")) {
      p = p.slice(0, -1);
    }
    return p.toLowerCase();
  } catch {
    return "/";
  }
}

function normalizeUrlForDedup(url) {
  try {
    const parsed = new URL(url);
    parsed.hash = "";
    let pathname = parsed.pathname || "/";
    if (pathname.length > 1 && pathname.endsWith("/")) {
      pathname = pathname.slice(0, -1);
    }
    parsed.pathname = pathname;
    return parsed.href;
  } catch {
    return url;
  }
}

function matchesAny(text, patterns, asRegex = false) {
  if (!text) {
    return false;
  }
  const lower = text.toLowerCase();
  for (const pattern of patterns || []) {
    if (asRegex) {
      if (new RegExp(pattern, "i").test(text)) {
        return true;
      }
    } else if (lower.includes(String(pattern).toLowerCase())) {
      return true;
    }
  }
  return false;
}

function shouldIgnoreLink(href, anchorText, rules) {
  const pathname = normalizePathname(href);
  const full = `${pathname} ${anchorText || ""}`.toLowerCase();

  for (const fragment of rules.ignore_path_patterns || []) {
    if (full.includes(fragment.toLowerCase())) {
      return { ignored: true, reason: `ignore_path:${fragment}` };
    }
  }
  for (const regex of rules.ignore_path_regex || []) {
    if (new RegExp(regex, "i").test(pathname) || new RegExp(regex, "i").test(href)) {
      return { ignored: true, reason: `ignore_regex:${regex}` };
    }
  }
  if (matchesAny(anchorText, rules.ignore_anchor_patterns)) {
    return { ignored: true, reason: "ignore_anchor" };
  }
  if (href.startsWith("#") || href.startsWith("javascript:") || href.startsWith("mailto:") || href.startsWith("tel:")) {
    return { ignored: true, reason: "non_navigational_scheme" };
  }
  return { ignored: false, reason: null };
}

function classifyLink(href, anchorText, rules) {
  const pathname = normalizePathname(href);
  const combined = `${pathname} ${anchorText || ""}`;

  for (const group of rules.priority_groups || []) {
    if (group === "HOME") {
      continue;
    }
    const pathPatterns = rules.group_path_patterns?.[group] || [];
    const anchorPatterns = rules.group_anchor_patterns?.[group] || [];
    const pathHit = matchesAny(pathname, pathPatterns.filter((p) => !p.startsWith("^")), false);
    const pathRegexHit = (pathPatterns || []).some((p) => p.startsWith("^") && new RegExp(p, "i").test(pathname));
    const anchorHit = matchesAny(anchorText, anchorPatterns);
    if (pathHit || pathRegexHit || anchorHit) {
      return {
        priority_group: group,
        page_role: rules.page_role_map?.[group] || "unknown",
        classification_basis: [
          pathHit || pathRegexHit ? "path" : null,
          anchorHit ? "anchor" : null,
        ].filter(Boolean),
      };
    }
  }
  return { priority_group: "UNCLASSIFIED", page_role: "unknown", classification_basis: [] };
}

/**
 * Discover internal links from homepage HTML and classify them.
 */
function discoverSiteSurface(html, homepageUrl, domain, rules) {
  const resolvedRules = rules || loadSurfaceRules();
  const links = extractLinks(html, homepageUrl, resolvedRules.links_cap_per_homepage || 200);
  const candidates = [];
  const ignored = [];
  const seen = new Set();

  for (const link of links.internal || []) {
    const hrefNorm = normalizeUrlForDedup(link.href);
    const linkDomain = extractDomain(link.href);
    if (linkDomain && domain && linkDomain !== domain && !linkDomain.endsWith(`.${domain}`)) {
      ignored.push({ href: link.href, text: link.text, reason: "external_domain" });
      continue;
    }
    if (seen.has(hrefNorm)) {
      continue;
    }
    seen.add(hrefNorm);

    const ignore = shouldIgnoreLink(link.href, link.text, resolvedRules);
    if (ignore.ignored) {
      ignored.push({ href: link.href, text: link.text, reason: ignore.reason });
      continue;
    }

    const classification = classifyLink(link.href, link.text, resolvedRules);
    candidates.push({
      href: link.href,
      href_normalized: hrefNorm,
      anchor_text: link.text,
      pathname: normalizePathname(link.href),
      priority_group: classification.priority_group,
      page_role: classification.page_role,
      classification_basis: classification.classification_basis,
    });
  }

  return {
    domain,
    homepage_url: homepageUrl,
    discovered_at: new Date().toISOString(),
    internal_links_total: (links.internal || []).length,
    candidates,
    ignored,
    rules_ref: "site-surface-discovery-rules-v0.json",
  };
}

/**
 * Select high-value pages per domain (deterministic).
 */
function selectAcquisitionPlan(discovery, homepageUrl, options = {}) {
  const rules = options.rules || loadSurfaceRules();
  const maxPages = Math.min(
    options.max_pages ?? rules.pages_per_domain_default ?? 8,
    rules.pages_per_domain_max ?? 10
  );
  const minPages = rules.pages_per_domain_min ?? 3;
  const selected = [];
  const skipped = [];

  const homeNorm = normalizeUrlForDedup(homepageUrl);
  selected.push({
    url: homepageUrl,
    href_normalized: homeNorm,
    priority_group: "HOME",
    page_role: "homepage",
    selection_reason: "homepage_seed",
    anchor_text: null,
  });

  const usedGroups = new Set(["HOME"]);
  const usedUrls = new Set([homeNorm]);

  const priorityOrder = (rules.priority_groups || []).filter((g) => g !== "HOME");
  const byGroup = {};
  for (const c of discovery.candidates || []) {
    if (!byGroup[c.priority_group]) {
      byGroup[c.priority_group] = [];
    }
    byGroup[c.priority_group].push(c);
  }

  for (const group of priorityOrder) {
    if (selected.length >= maxPages) {
      break;
    }
    if (usedGroups.has(group)) {
      continue;
    }
    const pool = (byGroup[group] || []).filter((c) => !usedUrls.has(c.href_normalized));
    if (!pool.length) {
      continue;
    }
    pool.sort((a, b) => a.pathname.localeCompare(b.pathname));
    const pick = pool[0];
    selected.push({
      url: pick.href,
      href_normalized: pick.href_normalized,
      priority_group: group,
      page_role: pick.page_role,
      selection_reason: `priority_group:${group}`,
      anchor_text: pick.anchor_text,
      classification_basis: pick.classification_basis,
    });
    usedGroups.add(group);
    usedUrls.add(pick.href_normalized);
  }

  const unclassified = (discovery.candidates || [])
    .filter((c) => c.priority_group === "UNCLASSIFIED" && !usedUrls.has(c.href_normalized))
    .sort((a, b) => a.pathname.localeCompare(b.pathname));

  for (const c of unclassified) {
    if (selected.length >= maxPages) {
      skipped.push({ ...c, reason: "cap_reached" });
      continue;
    }
    selected.push({
      url: c.href,
      href_normalized: c.href_normalized,
      priority_group: "UNCLASSIFIED",
      page_role: "unknown",
      selection_reason: "fill_to_cap_unclassified",
      anchor_text: c.anchor_text,
    });
    usedUrls.add(c.href_normalized);
  }

  for (const c of discovery.candidates || []) {
    if (!usedUrls.has(c.href_normalized) && !skipped.find((s) => s.href_normalized === c.href_normalized)) {
      skipped.push({ ...c, reason: selected.length >= maxPages ? "cap_reached" : "lower_priority" });
    }
  }

  while (selected.length < minPages && unclassified.length > selected.length - 1) {
    const remaining = unclassified.filter((c) => !usedUrls.has(c.href_normalized));
    if (!remaining.length) {
      break;
    }
    const pick = remaining[0];
    selected.push({
      url: pick.href,
      href_normalized: pick.href_normalized,
      priority_group: pick.priority_group,
      page_role: pick.page_role,
      selection_reason: "fill_to_min",
      anchor_text: pick.anchor_text,
    });
    usedUrls.add(pick.href_normalized);
  }

  return {
    domain: discovery.domain,
    homepage_url: homepageUrl,
    pages_min: minPages,
    pages_max: maxPages,
    selected_count: selected.length,
    selected,
    skipped,
  };
}

module.exports = {
  loadSurfaceRules,
  discoverSiteSurface,
  selectAcquisitionPlan,
  normalizeUrlForDedup,
  classifyLink,
  shouldIgnoreLink,
};
