"use strict";

/**
 * Evidence-backed site pattern extraction across captured pages.
 * No interpretation — only repeated observable facts.
 */

function normalizeText(text) {
  return (text || "").replace(/\s+/g, " ").trim().toLowerCase();
}

function countOccurrences(items, keyFn) {
  const counts = new Map();
  for (const item of items) {
    const key = keyFn(item);
    if (!key) {
      continue;
    }
    counts.set(key, (counts.get(key) || 0) + 1);
  }
  return counts;
}

function repeatedEntries(counts, minCount = 2) {
  return [...counts.entries()]
    .filter(([, count]) => count >= minCount)
    .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]))
    .map(([text, count]) => ({ text, count }));
}

function extractServicePattern(pages) {
  const servicePages = pages.filter(
    (p) =>
      p.page_role === "service" ||
      p.priority_group === "SERVICE" ||
      p.priority_group === "MOVING" ||
      p.priority_group === "LOADERS"
  );
  const headings = [];
  for (const page of servicePages) {
    for (const h of page.headings || []) {
      if (h.level <= 2 && h.text) {
        headings.push({ text: h.text, page_url: page.final_url || page.requested_url, snapshot_id: page.snapshot_id });
      }
    }
  }
  const counts = countOccurrences(headings, (h) => normalizeText(h.text));
  return {
    pattern_type: "SERVICE_PATTERN",
    service_pages_count: servicePages.length,
    headings_observed: headings.slice(0, 50),
    repeated_headings: repeatedEntries(counts, 2),
    evidence_refs: servicePages.map((p) => p.snapshot_id).filter(Boolean),
  };
}

function extractPricingPattern(pages) {
  const signals = [];
  for (const page of pages) {
    for (const ps of page.pricing_signals || []) {
      signals.push({
        text: ps.text,
        currency_hint: ps.currency_hint,
        page_url: page.final_url || page.requested_url,
        snapshot_id: page.snapshot_id,
      });
    }
  }
  const counts = countOccurrences(signals, (s) => normalizeText(s.text));
  const pricingPages = pages.filter(
    (p) => p.page_role === "pricing" || p.priority_group === "PRICING" || (p.pricing_signals || []).length > 0
  );
  return {
    pattern_type: "PRICING_PATTERN",
    pricing_pages_count: pricingPages.length,
    signals_observed: signals.slice(0, 40),
    repeated_signals: repeatedEntries(counts, 2),
    evidence_refs: pricingPages.map((p) => p.snapshot_id).filter(Boolean),
  };
}

function extractCtaPattern(pages) {
  const ctas = [];
  for (const page of pages) {
    for (const cta of page.cta_elements || []) {
      ctas.push({
        text: cta.text,
        element_type: cta.element_type,
        href: cta.href,
        page_url: page.final_url || page.requested_url,
        snapshot_id: page.snapshot_id,
      });
    }
  }
  const counts = countOccurrences(ctas, (c) => normalizeText(c.text));
  return {
    pattern_type: "CTA_PATTERN",
    cta_count_total: ctas.length,
    ctas_observed: ctas.slice(0, 40),
    repeated_cta_text: repeatedEntries(counts, 2),
    evidence_refs: pages.map((p) => p.snapshot_id).filter(Boolean),
  };
}

function extractTrustPattern(pages) {
  const trust = [];
  for (const page of pages) {
    for (const t of page.trust_signals_visible || []) {
      trust.push({
        text: t.text,
        page_url: page.final_url || page.requested_url,
        snapshot_id: page.snapshot_id,
      });
    }
  }
  const counts = countOccurrences(trust, (t) => normalizeText(t.text));
  return {
    pattern_type: "TRUST_PATTERN",
    trust_signals_total: trust.length,
    signals_observed: trust.slice(0, 30),
    repeated_signals: repeatedEntries(counts, 2),
    evidence_refs: pages.filter((p) => (p.trust_signals_visible || []).length > 0).map((p) => p.snapshot_id),
  };
}

function extractLeadCapturePattern(pages) {
  const forms = [];
  const phones = new Set();
  const messengers = [];
  for (const page of pages) {
    for (const form of page.forms || []) {
      forms.push({
        form_id: form.form_id,
        action: form.action,
        method: form.method,
        field_count: (form.fields || []).length,
        page_url: page.final_url || page.requested_url,
        snapshot_id: page.snapshot_id,
      });
    }
    for (const phone of page.contacts?.phones || []) {
      phones.add(phone);
    }
    for (const msg of page.contacts?.messengers || []) {
      messengers.push({
        type: msg.type,
        handle: msg.handle,
        page_url: page.final_url || page.requested_url,
        snapshot_id: page.snapshot_id,
      });
    }
  }
  const msgCounts = countOccurrences(messengers, (m) => `${m.type}:${m.handle}`);
  return {
    pattern_type: "LEAD_CAPTURE_PATTERN",
    forms_observed: forms,
    unique_phones: [...phones],
    messengers_observed: messengers.slice(0, 20),
    repeated_messengers: repeatedEntries(msgCounts, 2),
    evidence_refs: pages
      .filter((p) => (p.forms || []).length > 0 || (p.contacts?.phones || []).length > 0)
      .map((p) => p.snapshot_id),
  };
}

function extractNavigationPattern(pages, discovery) {
  const navLinks = [];
  const homepage = pages.find((p) => p.page_role === "homepage" || p.priority_group === "HOME");
  if (homepage?.links?.internal) {
    for (const link of homepage.links.internal.slice(0, 40)) {
      navLinks.push({
        href: link.href,
        text: link.text,
        source: "homepage_internal_links",
        snapshot_id: homepage.snapshot_id,
      });
    }
  }
  const classified = (discovery?.candidates || []).slice(0, 30).map((c) => ({
    href: c.href,
    text: c.anchor_text,
    priority_group: c.priority_group,
    page_role: c.page_role,
  }));
  return {
    pattern_type: "NAVIGATION_PATTERN",
    homepage_nav_links: navLinks,
    classified_candidates: classified,
    evidence_refs: homepage ? [homepage.snapshot_id] : [],
  };
}

function extractAllSitePatterns(domainPages, discovery) {
  const pages = domainPages.filter((p) => p.status === "success" || p.status === "render_required");
  return {
    domain: domainPages[0]?.domain || discovery?.domain,
    patterns: [
      extractServicePattern(pages),
      extractPricingPattern(pages),
      extractCtaPattern(pages),
      extractTrustPattern(pages),
      extractLeadCapturePattern(pages),
      extractNavigationPattern(pages, discovery),
    ],
    generated_at: new Date().toISOString(),
  };
}

function buildSiteIntelligence(domainPages, patterns, discovery, acquisitionPlan) {
  const pages = domainPages.filter((p) => p.status === "success" || p.status === "render_required");
  const servicePages = pages.filter(
    (p) => ["service", "homepage"].includes(p.page_role) || ["SERVICE", "MOVING", "LOADERS"].includes(p.priority_group)
  );
  const pricingPages = pages.filter(
    (p) => p.page_role === "pricing" || p.priority_group === "PRICING" || (p.pricing_signals || []).length >= 3
  );
  const leadPages = pages.filter((p) => (p.forms || []).length > 0 || (p.cta_elements || []).length >= 2);
  const landingLike = pages.filter(
    (p) =>
      p.page_role === "homepage" ||
      (p.headings || []).some((h) => h.level === 1 && /груз|такси|перевоз|переезд/i.test(h.text || ""))
  );

  const servicePattern = patterns.patterns.find((p) => p.pattern_type === "SERVICE_PATTERN");
  const pricingPattern = patterns.patterns.find((p) => p.pattern_type === "PRICING_PATTERN");
  const ctaPattern = patterns.patterns.find((p) => p.pattern_type === "CTA_PATTERN");
  const trustPattern = patterns.patterns.find((p) => p.pattern_type === "TRUST_PATTERN");
  const leadPattern = patterns.patterns.find((p) => p.pattern_type === "LEAD_CAPTURE_PATTERN");

  return {
    domain: pages[0]?.domain,
    purpose: "site_structure_observation",
    pages_captured: pages.map((p) => ({
      snapshot_id: p.snapshot_id,
      url: p.final_url || p.requested_url,
      page_role: p.page_role,
      priority_group: p.priority_group,
      status: p.status,
      title: p.title,
    })),
    business_structure_observations: {
      services_observed: (servicePattern?.headings_observed || []).map((h) => ({
        text: h.text,
        evidence: h.snapshot_id,
      })),
      offers_repeated: (servicePattern?.repeated_headings || []).map((r) => ({ text: r.text, count: r.count })),
      pricing_repeated: (pricingPattern?.repeated_signals || []).map((r) => ({ text: r.text, count: r.count })),
      cta_repeated: (ctaPattern?.repeated_cta_text || []).map((r) => ({ text: r.text, count: r.count })),
      trust_repeated: (trustPattern?.repeated_signals || []).map((r) => ({ text: r.text, count: r.count })),
      lead_capture: {
        forms_count: (leadPattern?.forms_observed || []).length,
        unique_phones: leadPattern?.unique_phones || [],
        messengers: leadPattern?.messengers_observed || [],
      },
      landing_like_pages: landingLike.map((p) => ({
        url: p.final_url || p.requested_url,
        title: p.title,
        snapshot_id: p.snapshot_id,
      })),
    },
    acquisition_plan_ref: acquisitionPlan,
    discovery_ref: {
      candidates_count: discovery?.candidates?.length ?? 0,
      ignored_count: discovery?.ignored?.length ?? 0,
    },
    safe_unknown: pages
      .filter((p) => p.status !== "success")
      .map((p) => `${p.final_url || p.requested_url}: ${p.status}`),
    generated_at: new Date().toISOString(),
  };
}

function buildDomainSummary(intelligence, patterns) {
  const pages = intelligence.pages_captured || [];
  const obs = intelligence.business_structure_observations || {};
  return {
    domain: intelligence.domain,
    pages_captured: pages.length,
    page_urls: pages.map((p) => p.url),
    service_pages: pages.filter((p) => p.page_role === "service" || ["SERVICE", "MOVING", "LOADERS"].includes(p.priority_group)).length,
    pricing_pages: pages.filter((p) => p.page_role === "pricing" || p.priority_group === "PRICING").length,
    lead_pages: pages.filter((p) => (obs.lead_capture?.forms_count || 0) > 0 || p.page_role === "contact").length,
    trust_elements: (patterns.patterns.find((p) => p.pattern_type === "TRUST_PATTERN")?.signals_observed || []).length,
    repeated_offers: obs.offers_repeated || [],
    repeated_cta: obs.cta_repeated || [],
    safe_unknown: intelligence.safe_unknown?.length ? intelligence.safe_unknown : ["none observed"],
  };
}

function buildCrossDomainComparison(summaries, allPatterns) {
  const domains = summaries.map((s) => s.domain);

  const allCta = summaries.flatMap((s) => s.repeated_cta.map((c) => ({ domain: s.domain, ...c })));
  const ctaTextCounts = countOccurrences(allCta, (c) => normalizeText(c.text));
  const commonCta = repeatedEntries(
    new Map([...ctaTextCounts.entries()].filter(([text]) => {
      const domainSet = new Set(allCta.filter((c) => normalizeText(c.text) === text).map((c) => c.domain));
      return domainSet.size >= 2;
    })),
    1
  );

  const pricingVisibility = summaries.map((s) => ({
    domain: s.domain,
    pricing_pages: s.pricing_pages,
    repeated_pricing_count: (allPatterns.find((p) => p.domain === s.domain)?.patterns
      ?.find((x) => x.pattern_type === "PRICING_PATTERN")?.repeated_signals || []).length,
  }));

  const serviceCoverage = summaries.map((s) => ({
    domain: s.domain,
    service_pages: s.service_pages,
    pages_captured: s.pages_captured,
  }));

  const leadCapture = summaries.map((s) => ({
    domain: s.domain,
    lead_pages: s.lead_pages,
    forms: allPatterns
      .find((p) => p.domain === s.domain)
      ?.patterns.find((x) => x.pattern_type === "LEAD_CAPTURE_PATTERN")?.forms_observed?.length ?? 0,
    unique_phones: allPatterns
      .find((p) => p.domain === s.domain)
      ?.patterns.find((x) => x.pattern_type === "LEAD_CAPTURE_PATTERN")?.unique_phones?.length ?? 0,
  }));

  const uniquePatterns = [];
  for (const sp of allPatterns) {
    const pricingPat = sp.patterns.find((p) => p.pattern_type === "PRICING_PATTERN");
    if (pricingPat?.pricing_pages_count === 0) {
      uniquePatterns.push({ domain: sp.domain, note: "no dedicated pricing page in acquisition set" });
    }
  }

  return {
    domains_compared: domains,
    common_patterns: {
      repeated_cta_across_domains: commonCta,
      all_domains_captured: summaries.every((s) => s.pages_captured >= 3),
    },
    unique_patterns: uniquePatterns,
    service_coverage_differences: serviceCoverage,
    lead_capture_differences: leadCapture,
    pricing_visibility_differences: pricingVisibility,
    generated_at: new Date().toISOString(),
  };
}

module.exports = {
  extractAllSitePatterns,
  buildSiteIntelligence,
  buildDomainSummary,
  buildCrossDomainComparison,
  extractServicePattern,
  extractPricingPattern,
  extractCtaPattern,
  extractTrustPattern,
  extractLeadCapturePattern,
  extractNavigationPattern,
};
