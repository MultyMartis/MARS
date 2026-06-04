"use strict";

const path = require("path");
const { detectBlocks } = require("./detect-blocks");
const { extractOffers } = require("./extract-offers");
const { extractCtaPatterns } = require("./extract-cta-patterns");
const { extractTrustPatterns } = require("./extract-trust-patterns");
const {
  loadBlockRegistry,
  landingIdFor,
  pricingIdFor,
  contactIdFor,
  formIdFor,
  makeEvidence,
  readPageHtml,
  readWebsiteSnapshotsIndex,
} = require("./utils");
const {
  buildLandingObservationsIndex,
  writeLandingObservation,
  writeLandingObservationsIndex,
  landingArtifactRefs,
} = require("./write-landing-observations");
const { buildObservationsV2 } = require("./build-observations-v2");

function inferPageType(snapshot, blocks, formPatterns) {
  const role = snapshot.page_role || "unknown";
  if (role === "homepage" || role === "operator_seed") {
    return "homepage";
  }
  if (role === "serp_landing" || role === "landing") {
    return "serp_landing";
  }
  if (role === "contact") {
    return "contact_focus";
  }
  if (role === "pricing" || role === "service") {
    return "service_landing";
  }
  if (role === "category") {
    return "catalog_entry";
  }

  const hasForm = formPatterns.length > 0;
  const offerCount = (snapshot.offers || []).length;
  const contactHeavy =
    (snapshot.contacts?.phones?.length || 0) + (snapshot.contacts?.emails?.length || 0) >= 2;

  if (contactHeavy && hasForm && blocks.some((b) => b.block_type === "contacts")) {
    return "contact_focus";
  }
  if (offerCount <= 2 && hasForm && blocks.some((b) => b.block_type === "hero")) {
    return "campaign_landing";
  }
  if (offerCount > 0) {
    return "service_landing";
  }
  return "unknown";
}

function extractPricingPatterns(snapshot, landingId, blocks) {
  const pricingBlock = blocks.find((b) => b.block_type === "pricing_block");
  const patterns = [];
  let seq = 1;
  for (let i = 0; i < (snapshot.pricing_signals || []).length; i += 1) {
    const signal = snapshot.pricing_signals[i];
    patterns.push({
      pricing_id: pricingIdFor(landingId, seq),
      text: signal.text,
      currency_hint: signal.currency_hint || null,
      block_id: pricingBlock?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: `/pricing_signals/${i}`,
        verbatim_text: signal.text,
      }),
    });
    seq += 1;
  }
  return patterns;
}

function extractContactPatterns(snapshot, landingId, blocks) {
  const contactBlock = blocks.find((b) => b.block_type === "contacts");
  const patterns = [];
  let seq = 1;
  const contacts = snapshot.contacts || {};

  for (const phone of contacts.phones || []) {
    patterns.push({
      contact_id: contactIdFor(landingId, seq),
      contact_type: "phone",
      value: phone,
      block_id: contactBlock?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/contacts/phones",
        verbatim_text: phone,
      }),
    });
    seq += 1;
  }
  for (const email of contacts.emails || []) {
    patterns.push({
      contact_id: contactIdFor(landingId, seq),
      contact_type: "email",
      value: email,
      block_id: contactBlock?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/contacts/emails",
        verbatim_text: email,
      }),
    });
    seq += 1;
  }
  for (const addr of contacts.addresses || []) {
    patterns.push({
      contact_id: contactIdFor(landingId, seq),
      contact_type: "address",
      value: addr,
      block_id: contactBlock?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/contacts/addresses",
        verbatim_text: addr,
      }),
    });
    seq += 1;
  }
  for (const msg of contacts.messengers || []) {
    patterns.push({
      contact_id: contactIdFor(landingId, seq),
      contact_type: "messenger",
      value: `${msg.type}:${msg.handle}`,
      block_id: contactBlock?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/contacts/messengers",
        verbatim_text: msg.handle,
      }),
    });
    seq += 1;
  }
  return patterns;
}

function extractFormPatterns(snapshot, landingId, blocks) {
  const leadBlock = blocks.find((b) => b.block_type === "lead_form");
  const patterns = [];
  let seq = 1;
  for (let i = 0; i < (snapshot.forms || []).length; i += 1) {
    const form = snapshot.forms[i];
    if ((form.fields || []).length < 2) {
      continue;
    }
    patterns.push({
      form_id: formIdFor(landingId, seq),
      action: form.action || null,
      method: form.method || null,
      fields: form.fields,
      visible_purpose: form.visible_purpose || null,
      cta_type: "lead_form",
      block_id: leadBlock?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: `/forms/${i}`,
        verbatim_text: form.visible_purpose || null,
      }),
    });
    seq += 1;
  }
  return patterns;
}

function extractPagePatterns(snapshot, blocks, registry) {
  const patterns = [];
  const cfg = registry.page_pattern || {};
  const headings = snapshot.headings || [];

  function addPattern(patternId, verbatim) {
    patterns.push({
      pattern_id: patternId,
      evidence: makeEvidence(snapshot, { verbatim_text: verbatim || patternId }),
    });
  }

  if (headings.length >= (cfg.long_scroll_heading_threshold || 4)) {
    addPattern("long_scroll_sections", `${headings.length} heading bands`);
  }
  if (blocks.some((b) => b.block_type === "faq")) {
    addPattern("faq_section_visible", "faq block detected");
  }
  if (blocks.some((b) => b.block_type === "reviews")) {
    addPattern("review_widget_visible", "reviews block detected");
  }
  if (blocks.some((b) => b.block_type === "pricing_block")) {
    addPattern("pricing_table_visible", "pricing block detected");
  }
  if ((snapshot.contacts?.phones?.length || 0) > 0) {
    addPattern("phone_prominent", snapshot.contacts.phones[0]);
  }
  if (blocks.some((b) => b.block_type === "messenger_cta")) {
    addPattern("messenger_prominent", "messenger CTA visible");
  }
  const ctaCount = (snapshot.cta_elements || []).length;
  if (ctaCount === 1) {
    addPattern("single_primary_cta", snapshot.cta_elements[0].text);
  } else if (ctaCount > 1) {
    addPattern("multi_cta_same_intent", `${ctaCount} CTA elements visible`);
  }

  return patterns;
}

function analyzeSnapshot(snapshot, sessionDir, options = {}) {
  const registry = options.registry || loadBlockRegistry(options.registryPath);
  const landingId = options.landing_id;
  const html = readPageHtml(sessionDir, snapshot) || "";
  const analyzedAt = options.analyzed_at || new Date().toISOString();
  const safeUnknown = [...(snapshot.safe_unknown || [])];

  if (!html && snapshot.status === "success") {
    safeUnknown.push("Block boundaries not re-derived from HTML — page.html missing");
  }

  const { visible_blocks, safe_unknown: blockUnknown } = detectBlocks(snapshot, {
    registry,
    landing_id: landingId,
    html,
  });
  safeUnknown.push(...blockUnknown);

  const form_patterns = extractFormPatterns(snapshot, landingId, visible_blocks);
  const contact_patterns = extractContactPatterns(snapshot, landingId, visible_blocks);
  const pricing_patterns = extractPricingPatterns(snapshot, landingId, visible_blocks);
  const offers = extractOffers(snapshot, { landing_id: landingId, visible_blocks });
  const trust_patterns = extractTrustPatterns(snapshot, {
    landing_id: landingId,
    visible_blocks,
    registry,
    html,
  });
  const cta_patterns = extractCtaPatterns(snapshot, {
    landing_id: landingId,
    visible_blocks,
    form_patterns,
    registry,
  });
  const page_patterns = extractPagePatterns(snapshot, visible_blocks, registry);
  const page_type = inferPageType(snapshot, visible_blocks, form_patterns);

  if (!offers.length && snapshot.status === "success" && snapshot.render_status !== "js_shell") {
    safeUnknown.push("No offer strings classified from snapshot or headings");
  }

  const artifactRefs = {
    ...landingArtifactRefs(landingId),
    website_snapshot: snapshot.artifact_refs?.website_snapshot || null,
    page_html: snapshot.artifact_refs?.page_html || null,
  };

  const legacyDetail = {
    landing_id: landingId,
    visible_blocks,
    offers,
    cta_patterns,
    pricing_patterns,
    trust_patterns,
    contact_patterns,
    form_patterns,
    page_patterns,
  };

  const v2Built = buildObservationsV2(legacyDetail, snapshot, {
    registry,
    navNoiseConfigPath: options.navNoiseConfigPath,
  });

  return {
    schema_version: "0.2",
    analysis_phase: "landing_analysis_v2",
    landing_id: landingId,
    snapshot_id: snapshot.snapshot_id,
    session_id: snapshot.session_id,
    competitor_id: snapshot.competitor_id ?? null,
    domain: snapshot.domain,
    final_url: snapshot.final_url,
    page_role: snapshot.page_role,
    page_type,
    analyzed_at: analyzedAt,
    observations: v2Built.observations,
    observation_summary: v2Built.observation_summary,
    _processing: v2Built._processing,
    _legacy: {
      visible_blocks,
      offers,
      cta_patterns,
      pricing_patterns,
      trust_patterns,
      contact_patterns,
      form_patterns,
      page_patterns,
    },
    visible_blocks,
    offers,
    cta_patterns,
    pricing_patterns,
    trust_patterns,
    contact_patterns,
    form_patterns,
    page_patterns,
    evidence: {
      primary_snapshot_id: snapshot.snapshot_id,
      capture_time: snapshot.capture_time,
      analysis_mode: html ? "snapshot_and_html" : "snapshot_only",
    },
    artifact_refs: artifactRefs,
    evidence_grade: snapshot.evidence_grade,
    safe_unknown: safeUnknown.length ? [...new Set(safeUnknown)] : undefined,
  };
}

/**
 * Run landing analysis pass for a session with website_snapshots.json.
 */
function runLandingPass(sessionDir, options = {}) {
  const websiteIndex = options.websiteIndex || readWebsiteSnapshotsIndex(sessionDir);
  const sessionId = websiteIndex.session_id;
  const analyzedAt = options.analyzed_at || new Date().toISOString();
  const registry = options.registry || loadBlockRegistry(options.registryPath);

  const landings = [];
  let seq = 1;

  for (const snapshot of websiteIndex.snapshots || []) {
    if (snapshot.status === "skipped") {
      continue;
    }
    const landingId = landingIdFor(sessionId, seq);
    const observation = analyzeSnapshot(snapshot, sessionDir, {
      landing_id: landingId,
      analyzed_at: analyzedAt,
      registry,
      registryPath: options.registryPath,
    });
    writeLandingObservation(sessionDir, observation);
    landings.push(observation);
    seq += 1;
  }

  const sessionSafeUnknown = options.safe_unknown || [];
  if (!landings.length) {
    sessionSafeUnknown.push("Landing Analysis pass produced zero landings — no analyzable snapshots");
  }

  const index = buildLandingObservationsIndex(sessionId, landings, {
    generated_at: analyzedAt,
    safe_unknown: sessionSafeUnknown,
    website_snapshots_file: "website_snapshots.json",
    competitors_file: "competitors.json",
  });
  const written = writeLandingObservationsIndex(sessionDir, index);

  return {
    session_id: sessionId,
    session_dir: sessionDir,
    index,
    index_path: written.path,
    landings,
  };
}

module.exports = {
  runLandingPass,
  analyzeSnapshot,
  inferPageType,
  extractPricingPatterns,
  extractContactPatterns,
  extractFormPatterns,
  extractPagePatterns,
};
