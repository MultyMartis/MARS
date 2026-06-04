#!/usr/bin/env node
/**
 * Multi-page market leader pass — controlled site surface discovery + acquisition.
 * Source session: mig-20260605-mlint01 (validated market leaders only).
 */
import { readFileSync, writeFileSync, mkdirSync, existsSync, copyFileSync } from "fs";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { createRequire } from "module";

const __dirname = dirname(fileURLToPath(import.meta.url));
const PILOT_ROOT = join(__dirname, "..");
const MIG_ROOT = join(PILOT_ROOT, "..", "..", "..", "..", "projects", "mig");
const require = createRequire(import.meta.url);

const SESSION_ID = "mig-20260605-mlint01";
const SESSION_DIR = join(PILOT_ROOT, `session-${SESSION_ID}`);

const {
  loadSurfaceRules,
  discoverSiteSurface,
  selectAcquisitionPlan,
  normalizeUrlForDedup,
} = require(join(MIG_ROOT, "lib", "website-acquisition", "discover-site-surface.js"));
const { fetchPage } = require(join(MIG_ROOT, "lib", "website-acquisition", "fetch-page.js"));
const { extractPageFacts } = require(join(MIG_ROOT, "lib", "website-acquisition", "extract-page-facts.js"));
const { loadRules } = require(join(MIG_ROOT, "lib", "website-acquisition", "build-url-plan.js"));
const { buildSnapshotRecord } = require(join(MIG_ROOT, "lib", "website-acquisition", "write-website-snapshot.js"));
const {
  extractAllSitePatterns,
  buildSiteIntelligence,
  buildDomainSummary,
  buildCrossDomainComparison,
} = require(join(MIG_ROOT, "lib", "website-acquisition", "extract-site-patterns.js"));

function loadJson(p) {
  return JSON.parse(readFileSync(p, "utf8"));
}

function delay(ms) {
  return new Promise((r) => setTimeout(r, ms));
}

function writeSitePageArtifacts(sessionDir, snapshot, fetchResult) {
  const snapshotDir = join(sessionDir, "site-pages", snapshot.snapshot_id);
  mkdirSync(snapshotDir, { recursive: true });
  writeFileSync(join(snapshotDir, "page.html"), fetchResult.body || "", "utf8");
  writeFileSync(
    join(snapshotDir, "headers.json"),
    `${JSON.stringify(
      {
        http_status: fetchResult.http_status,
        final_url: fetchResult.final_url,
        redirect_chain: fetchResult.redirect_chain || [],
        headers: fetchResult.headers || {},
        fetch_duration_ms: fetchResult.duration_ms ?? null,
        captured_at: snapshot.capture_time,
      },
      null,
      2
    )}\n`,
    "utf8"
  );
  snapshot.artifact_refs = {
    website_snapshot: `site-pages/${snapshot.snapshot_id}/website_snapshot.json`,
    page_html: `site-pages/${snapshot.snapshot_id}/page.html`,
    headers: `site-pages/${snapshot.snapshot_id}/headers.json`,
  };
  writeFileSync(join(snapshotDir, "website_snapshot.json"), `${JSON.stringify(snapshot, null, 2)}\n`, "utf8");
  return snapshotDir;
}

function buildAcquisitionScopeDoc(rules) {
  return {
    schema_version: "0",
    session_id: SESSION_ID,
    generated_at: new Date().toISOString(),
    purpose: "controlled_multi_page_acquisition",
    rules_ref: "projects/mig/config/site-surface-discovery-rules-v0.json",
    constraints: {
      no_full_site_crawl: true,
      pages_per_domain_min: rules.pages_per_domain_min,
      pages_per_domain_max: rules.pages_per_domain_max,
      discovery_source: "homepage_internal_links_only",
    },
    priority_groups: rules.priority_groups,
    ignore_categories: [
      "blog",
      "news",
      "privacy",
      "legal",
      "vacancies",
      "technical (wp-content, feeds, assets)",
    ],
    selection_algorithm: [
      "1. Always include homepage seed from prior single-page pass",
      "2. For each priority group (SERVICE, PRICING, MOVING, LOADERS, CONTACTS, FAQ), pick first matching link by pathname sort",
      "3. Fill remaining cap with unclassified internal links",
      "4. Stop at pages_per_domain_max (10); ensure at least pages_per_domain_min (3) when candidates exist",
    ],
  };
}

async function main() {
  if (!existsSync(SESSION_DIR)) {
    throw new Error(`Session not found: ${SESSION_DIR}`);
  }

  const surfaceRules = loadSurfaceRules();
  const fetchRules = loadRules();
  const websiteIndex = loadJson(join(SESSION_DIR, "website_snapshots.json"));
  const shortlist = loadJson(join(SESSION_DIR, "market-leader-shortlist.json"));

  mkdirSync(join(SESSION_DIR, "site-pages"), { recursive: true });
  mkdirSync(join(SESSION_DIR, "site-intelligence"), { recursive: true });

  const acquisitionScope = buildAcquisitionScopeDoc(surfaceRules);
  writeFileSync(
    join(SESSION_DIR, "site-acquisition-scope.json"),
    `${JSON.stringify(acquisitionScope, null, 2)}\n`,
    "utf8"
  );

  const discoveries = [];
  const plans = [];
  const allDomainPages = [];
  let pageSeq = 0;

  for (const competitor of shortlist.competitors) {
    const domain = competitor.domain;
    const homepageSnap = websiteIndex.snapshots.find((s) => s.domain === domain);
    if (!homepageSnap) {
      console.warn(`No homepage snapshot for ${domain}, skipping`);
      continue;
    }

    const htmlPath = join(SESSION_DIR, homepageSnap.artifact_refs.page_html);
    const html = readFileSync(htmlPath, "utf8");
    const homepageUrl = homepageSnap.final_url || homepageSnap.requested_url;

    const discovery = discoverSiteSurface(html, homepageUrl, domain, surfaceRules);
    discoveries.push(discovery);

    const plan = selectAcquisitionPlan(discovery, homepageUrl, { rules: surfaceRules });
    plans.push(plan);

    const domainPages = [];

    for (const entry of plan.selected) {
      pageSeq += 1;
      const snapshotId = `${SESSION_ID}-sp${String(pageSeq).padStart(3, "0")}`;
      const homeNorm = normalizeUrlForDedup(homepageUrl);
      const entryNorm = normalizeUrlForDedup(entry.url);
      const isHomepageReuse =
        entry.priority_group === "HOME" && entryNorm === homeNorm && homepageSnap.status === "success";

      let fetchResult;
      let facts;
      const captureTime = new Date().toISOString();

      if (isHomepageReuse) {
        fetchResult = {
          ok: true,
          status: "success",
          http_status: homepageSnap.http_status,
          final_url: homepageSnap.final_url,
          redirect_chain: homepageSnap.redirect_chain || [],
          headers: {},
          content_type: homepageSnap.content_type,
          body: html,
          duration_ms: homepageSnap.fetch_duration_ms,
          acquisition_method: "reuse_homepage_snapshot",
        };
        facts = {
          title: homepageSnap.title,
          meta_description: homepageSnap.meta_description,
          canonical_url: homepageSnap.canonical_url,
          lang: homepageSnap.lang,
          headings: homepageSnap.headings,
          contacts: homepageSnap.contacts,
          offers: homepageSnap.offers,
          pricing_signals: homepageSnap.pricing_signals,
          cta_elements: homepageSnap.cta_elements,
          forms: homepageSnap.forms,
          links: homepageSnap.links,
          trust_signals_visible: homepageSnap.trust_signals_visible,
          visible_text_excerpt: homepageSnap.visible_text_excerpt,
          render_status: homepageSnap.render_status,
          acquisition_status: "success",
        };
      } else {
        if (domainPages.length > 0 && surfaceRules.inter_request_delay_ms > 0) {
          await delay(surfaceRules.inter_request_delay_ms);
        }
        fetchResult = await fetchPage(entry.url, {
          timeoutMs: surfaceRules.fetch_timeout_ms || fetchRules.fetch_timeout_ms,
          maxRedirects: surfaceRules.max_redirects || fetchRules.max_redirects,
        });
        facts =
          fetchResult.body && fetchResult.ok
            ? extractPageFacts(fetchResult.body, fetchResult.final_url || entry.url, { rules: fetchRules })
            : {
                headings: [],
                contacts: { phones: [], emails: [], addresses: [], messengers: [] },
                offers: [],
                pricing_signals: [],
                cta_elements: [],
                forms: [],
                links: { internal: [], external: [] },
                trust_signals_visible: [],
                render_status: "unknown",
                acquisition_status: fetchResult.status === "timeout" ? "timeout" : "failed",
              };
      }

      const planEntry = {
        snapshot_id: snapshotId,
        competitor_id: competitor.competitor_id,
        domain,
        requested_url: entry.url,
        page_role: entry.page_role,
        priority_group: entry.priority_group,
        selection_reason: entry.selection_reason,
      };

      const snapshot = buildSnapshotRecord(planEntry, fetchResult, facts, SESSION_ID, captureTime);
      snapshot.priority_group = entry.priority_group;
      snapshot.selection_reason = entry.selection_reason;
      snapshot.homepage_snapshot_ref = isHomepageReuse ? homepageSnap.snapshot_id : null;

      writeSitePageArtifacts(SESSION_DIR, snapshot, fetchResult);

      domainPages.push(snapshot);
      allDomainPages.push(snapshot);
    }

    const patterns = extractAllSitePatterns(domainPages, discovery);
    const intelligence = buildSiteIntelligence(domainPages, patterns, discovery, plan);
    const summary = buildDomainSummary(intelligence, patterns);

    writeFileSync(
      join(SESSION_DIR, "site-intelligence", `${domain.replace(/\./g, "_")}-patterns.json`),
      `${JSON.stringify(patterns, null, 2)}\n`,
      "utf8"
    );
    writeFileSync(
      join(SESSION_DIR, "site-intelligence", `${domain.replace(/\./g, "_")}-intelligence.json`),
      `${JSON.stringify(intelligence, null, 2)}\n`,
      "utf8"
    );

    discovery._summary = summary;
    discovery._patterns = patterns;
    discovery._intelligence = intelligence;
  }

  writeFileSync(
    join(SESSION_DIR, "site-surface-discovery.json"),
    `${JSON.stringify({ session_id: SESSION_ID, discoveries, generated_at: new Date().toISOString() }, null, 2)}\n`,
    "utf8"
  );
  writeFileSync(
    join(SESSION_DIR, "site-acquisition-plans.json"),
    `${JSON.stringify({ session_id: SESSION_ID, plans, generated_at: new Date().toISOString() }, null, 2)}\n`,
    "utf8"
  );

  const allPatterns = discoveries.map((d) => d._patterns).filter(Boolean);
  const summaries = discoveries.map((d) => d._summary).filter(Boolean);
  const crossDomain = buildCrossDomainComparison(summaries, allPatterns);

  writeFileSync(
    join(SESSION_DIR, "site-patterns.json"),
    `${JSON.stringify({ session_id: SESSION_ID, domains: allPatterns, generated_at: new Date().toISOString() }, null, 2)}\n`,
    "utf8"
  );
  writeFileSync(
    join(SESSION_DIR, "site-structure-summaries.json"),
    `${JSON.stringify({ session_id: SESSION_ID, summaries, generated_at: new Date().toISOString() }, null, 2)}\n`,
    "utf8"
  );
  writeFileSync(
    join(SESSION_DIR, "site-cross-domain-comparison.json"),
    `${JSON.stringify(crossDomain, null, 2)}\n`,
    "utf8"
  );

  const pagesIndex = {
    schema_version: "0.1",
    session_id: SESSION_ID,
    acquisition_mode: "multi_page_controlled",
    generated_at: new Date().toISOString(),
    pages_per_domain_max: surfaceRules.pages_per_domain_max,
    total_pages: allDomainPages.length,
    by_domain: summaries.map((s) => ({
      domain: s.domain,
      pages_captured: s.pages_captured,
      snapshot_ids: allDomainPages.filter((p) => p.domain === s.domain).map((p) => p.snapshot_id),
    })),
    snapshots: allDomainPages,
  };
  writeFileSync(join(SESSION_DIR, "site-pages-index.json"), `${JSON.stringify(pagesIndex, null, 2)}\n`, "utf8");

  const landingIndex = loadJson(join(SESSION_DIR, "landing_observations.json"));
  const report = buildReport({
    acquisitionScope,
    discoveries,
    plans,
    summaries,
    allPatterns,
    crossDomain,
    allDomainPages,
    landingIndex,
    websiteIndex,
  });

  const reportPath = join(SESSION_DIR, "REPORT-multi-page-market-leader-pass.md");
  writeFileSync(reportPath, report, "utf8");
  copyFileSync(reportPath, join(PILOT_ROOT, "REPORT-multi-page-market-leader-pass.md"));

  const manifest = loadJson(join(SESSION_DIR, "session_manifest.json"));
  manifest.capture_profile = {
    ...manifest.capture_profile,
    site_surface_discovery: true,
    multi_page_acquisition: true,
  };
  manifest.artifacts = {
    ...manifest.artifacts,
    site_acquisition_scope: "site-acquisition-scope.json",
    site_surface_discovery: "site-surface-discovery.json",
    site_acquisition_plans: "site-acquisition-plans.json",
    site_pages_index: "site-pages-index.json",
    site_patterns: "site-patterns.json",
    site_structure_summaries: "site-structure-summaries.json",
    site_cross_domain_comparison: "site-cross-domain-comparison.json",
    multi_page_report: "REPORT-multi-page-market-leader-pass.md",
  };
  writeFileSync(join(SESSION_DIR, "session_manifest.json"), `${JSON.stringify(manifest, null, 2)}\n`, "utf8");

  console.log(
    JSON.stringify(
      {
        session_dir: SESSION_DIR,
        report: reportPath,
        total_pages: allDomainPages.length,
        domains: summaries.length,
      },
      null,
      2
    )
  );
}

function buildReport(ctx) {
  const {
    acquisitionScope,
    discoveries,
    plans,
    summaries,
    allPatterns,
    crossDomain,
    allDomainPages,
    landingIndex,
    websiteIndex,
  } = ctx;

  const pagesCapturedSection = summaries
    .map((s) => {
      const domainPages = allDomainPages.filter((p) => p.domain === s.domain);
      return `### ${s.domain}

| Metric | Value |
| --- | --- |
| Pages captured | ${s.pages_captured} |
| Service pages | ${s.service_pages} |
| Pricing pages | ${s.pricing_pages} |
| Lead pages | ${s.lead_pages} |
| Trust elements | ${s.trust_elements} |

URLs:
${domainPages.map((p) => `- \`${p.final_url || p.requested_url}\` — role \`${p.page_role}\` / group \`${p.priority_group}\` — \`${p.status}\``).join("\n")}`;
    })
    .join("\n\n");

  const siteIntelligenceSection = discoveries
    .map((d) => {
      const intel = d._intelligence;
      if (!intel) return "";
      const obs = intel.business_structure_observations;
      return `### ${d.domain}

- **Services observed:** ${obs.services_observed.slice(0, 8).map((s) => s.text).join("; ") || "SAFE UNKNOWN"}
- **Repeated offers:** ${obs.offers_repeated.map((o) => `"${o.text}" (×${o.count})`).join(", ") || "none"}
- **Repeated pricing:** ${obs.pricing_repeated.map((p) => `"${p.text.slice(0, 60)}" (×${p.count})`).join(", ") || "none"}
- **Repeated CTA:** ${obs.cta_repeated.map((c) => `"${c.text}" (×${c.count})`).join(", ") || "none"}
- **Trust repeated:** ${obs.trust_repeated.map((t) => `"${t.text.slice(0, 50)}" (×${t.count})`).join(", ") || "none"}
- **Landing-like pages:** ${obs.landing_like_pages.map((p) => p.url).join(", ") || "SAFE UNKNOWN"}
- **Lead capture:** forms ${obs.lead_capture.forms_count}; phones ${obs.lead_capture.unique_phones.slice(0, 3).join(", ") || "—"}`;
    })
    .filter(Boolean)
    .join("\n\n");

  const patternsSection = allPatterns
    .map((dp) => {
      const lines = dp.patterns.map((p) => {
        if (p.pattern_type === "SERVICE_PATTERN") {
          return `- **SERVICE_PATTERN:** ${p.service_pages_count} service pages; repeated headings: ${p.repeated_headings.map((h) => h.text).slice(0, 3).join(", ") || "none"}`;
        }
        if (p.pattern_type === "PRICING_PATTERN") {
          return `- **PRICING_PATTERN:** ${p.pricing_pages_count} pricing pages; repeated: ${p.repeated_signals.map((s) => s.text.slice(0, 40)).slice(0, 2).join("; ") || "none"}`;
        }
        if (p.pattern_type === "CTA_PATTERN") {
          return `- **CTA_PATTERN:** ${p.cta_count_total} CTAs; repeated: ${p.repeated_cta_text.map((c) => c.text).slice(0, 3).join(", ") || "none"}`;
        }
        if (p.pattern_type === "TRUST_PATTERN") {
          return `- **TRUST_PATTERN:** ${p.trust_signals_total} signals; repeated: ${p.repeated_signals.map((s) => s.text.slice(0, 40)).slice(0, 2).join("; ") || "none"}`;
        }
        if (p.pattern_type === "LEAD_CAPTURE_PATTERN") {
          return `- **LEAD_CAPTURE_PATTERN:** ${p.forms_observed.length} forms; ${p.unique_phones.length} unique phones`;
        }
        if (p.pattern_type === "NAVIGATION_PATTERN") {
          return `- **NAVIGATION_PATTERN:** ${p.homepage_nav_links.length} homepage nav links; ${p.classified_candidates.length} classified candidates`;
        }
        return "";
      });
      return `### ${dp.domain}\n\n${lines.join("\n")}`;
    })
    .join("\n\n");

  const domainSummariesSection = summaries
    .map(
      (s) =>
        `| ${s.domain} | ${s.pages_captured} | ${s.service_pages} | ${s.pricing_pages} | ${s.lead_pages} | ${s.trust_elements} | ${s.repeated_offers.length ? s.repeated_offers.map((o) => o.text).slice(0, 2).join("; ") : "—"} | ${s.repeated_cta.length ? s.repeated_cta.map((c) => c.text).slice(0, 2).join("; ") : "—"} | ${Array.isArray(s.safe_unknown) ? s.safe_unknown.join("; ") : s.safe_unknown} |`
    )
    .join("\n");

  const crossSection = `
**Common patterns:**
- Repeated CTA across domains: ${crossDomain.common_patterns.repeated_cta_across_domains.map((c) => `"${c.text}"`).join(", ") || "none with count ≥2 domains"}
- All domains ≥3 pages: ${crossDomain.common_patterns.all_domains_captured}

**Service coverage:**
${crossDomain.service_coverage_differences.map((s) => `- ${s.domain}: ${s.service_pages} service pages / ${s.pages_captured} total`).join("\n")}

**Lead capture:**
${crossDomain.lead_capture_differences.map((l) => `- ${l.domain}: ${l.lead_pages} lead pages, ${l.forms} forms, ${l.unique_phones} phones`).join("\n")}

**Pricing visibility:**
${crossDomain.pricing_visibility_differences.map((p) => `- ${p.domain}: ${p.pricing_pages} pricing pages, ${p.repeated_pricing_count} repeated pricing signals`).join("\n")}

**Unique patterns:**
${crossDomain.unique_patterns.map((u) => `- ${u.domain}: ${u.note}`).join("\n") || "—"}
`;

  const singlePageLandings = (landingIndex.landings || []).map((l) => {
    const sum = l.observation_summary || {};
    return `- **${l.domain}** — families: ${(sum.families_present || []).join(", ")}; one URL only`;
  });

  const multiPageVisible = summaries.map((s) => {
    const plan = plans.find((p) => p.domain === s.domain);
    const groups = (plan?.selected || []).map((e) => e.priority_group).filter((g) => g !== "HOME");
    return `- **${s.domain}** — ${s.pages_captured} pages; priority groups beyond HOME: ${groups.join(", ") || "HOME only"}`;
  });

  return `# REPORT — Multi-Page Market Leader Pass

Session \`${SESSION_ID}\` · validated market leaders only · no new discovery · no ORCA · no Deep Research

## Acquisition Scope

Controlled multi-page acquisition from homepage internal links.

| Rule | Value |
| --- | --- |
| Min pages / domain | ${acquisitionScope.constraints.pages_per_domain_min} |
| Max pages / domain | ${acquisitionScope.constraints.pages_per_domain_max} |
| Discovery source | Homepage internal links only |
| Full-site crawl | **No** |

**Priority groups:** ${acquisitionScope.priority_groups.join(" → ")}

**Ignored:** ${acquisitionScope.ignore_categories.join(", ")}

Artifact: \`site-acquisition-scope.json\`

## Pages Captured

Total pages: **${allDomainPages.length}** across **${summaries.length}** domains.

${pagesCapturedSection}

Index: \`site-pages-index.json\`

## Site Intelligence

${siteIntelligenceSection}

Per-domain artifacts: \`site-intelligence/<domain>-intelligence.json\`

## Site Patterns

${patternsSection}

Artifact: \`site-patterns.json\`

## Domain Summaries

| Domain | Pages | Service | Pricing | Lead | Trust | Repeated Offers | Repeated CTA | SAFE UNKNOWN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
${domainSummariesSection}

Artifact: \`site-structure-summaries.json\`

## Cross-Domain Comparison

${crossSection}

Artifact: \`site-cross-domain-comparison.json\`

## New Groundtruth

| Artifact | Path |
| --- | --- |
| Acquisition scope | session-${SESSION_ID}/site-acquisition-scope.json |
| Surface discovery | session-${SESSION_ID}/site-surface-discovery.json |
| Acquisition plans | session-${SESSION_ID}/site-acquisition-plans.json |
| Site pages index | session-${SESSION_ID}/site-pages-index.json |
| Site patterns | session-${SESSION_ID}/site-patterns.json |
| Structure summaries | session-${SESSION_ID}/site-structure-summaries.json |
| Cross-domain comparison | session-${SESSION_ID}/site-cross-domain-comparison.json |

## SAFE UNKNOWN

- Dynamic quote pricing at order time — only visible page text captured
- JavaScript-rendered pages may be incomplete (\`render_required\` status)
- Pages not linked from homepage navigation are invisible to this pass
- Conversion rates, fleet size, ad spend — not observable
- q05, q06, q07 queries not in source session — move-intent pages may be underrepresented

## Readiness Assessment

MIG **now captures multi-page site structure** for validated market leaders: controlled link discovery, 3–10 pages per domain, evidence-backed pattern extraction (SERVICE, PRICING, CTA, TRUST, LEAD_CAPTURE, NAVIGATION), and cross-domain factual comparison.

**Limitation:** Discovery is **homepage-nav bounded** — no sitemap, no crawl beyond selected links. Patterns are **observable repetition only**, no strategic interpretation.

**Verdict:** **Site Intelligence layer operational** for human-supervised market leader review. Suitable input for business-structure understanding; not full competitive intelligence.

## Recommended Next Step

Human review of \`site-pages/\` HTML captures and \`site-cross-domain-comparison.json\`; confirm priority-group classification rules before expanding to additional sessions.

---

### Reality Review — Single Page vs Multi-Page

**Visible from single landing pass only:**

${singlePageLandings.join("\n")}

**Visible only after multi-page acquisition:**

${multiPageVisible.join("\n")}

**What changed:** Service sub-pages, dedicated pricing/contact routes, repeated CTA/trust across pages, navigation structure, and per-domain business surface beyond one SERP landing URL.

*Generated ${new Date().toISOString()} · Lane A · session ${SESSION_ID}*
`;
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
