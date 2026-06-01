"use strict";

const { stripTags } = require("../website-acquisition/extract-page-facts");
const {
  blockIdFor,
  makeEvidence,
  headingMatchesPatterns,
} = require("./utils");

function firstH1(headings) {
  return headings.find((h) => h.level === 1) || null;
}

function findHeadingByPatterns(headings, patterns) {
  return headings.find((h) => headingMatchesPatterns(h.text, patterns)) || null;
}

function summarizeRegion(text, maxChars) {
  if (!text) {
    return null;
  }
  const normalized = text.replace(/\s+/g, " ").trim();
  if (normalized.length <= maxChars) {
    return normalized;
  }
  return `${normalized.slice(0, maxChars)}…`;
}

/**
 * Detect MVP visible blocks from snapshot (+ optional HTML).
 */
function detectBlocks(snapshot, options = {}) {
  const registry = options.registry || {};
  const landingId = options.landing_id;
  const html = options.html || "";
  const blocks = [];
  const safeUnknown = [];
  let order = 0;
  let seq = 1;

  const headings = snapshot.headings || [];
  const blockConfig = registry.blocks || {};
  const summaryMax = registry.content_summary_max_chars || 200;

  if (snapshot.render_status === "js_shell") {
    safeUnknown.push("Block boundaries not derived — JavaScript shell page");
    return { visible_blocks: blocks, safe_unknown: safeUnknown };
  }

  const h1 = firstH1(headings);
  if (h1 && blockConfig.hero) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "hero",
      order,
      heading_text: h1.text,
      content_summary: summarizeRegion(h1.text, summaryMax),
      detection_method: "heading_heuristic",
      evidence: makeEvidence(snapshot, {
        source: "website_snapshot",
        snapshot_field: `/headings/${h1.order}`,
        verbatim_text: h1.text,
      }),
    });
    order += 1;
    seq += 1;
  } else if (blockConfig.hero) {
    safeUnknown.push("Hero block omitted — no h1 in snapshot headings");
  }

  const offers = snapshot.offers || [];
  const offerHeading = findHeadingByPatterns(
    headings,
    blockConfig.offer_block?.rules?.heading_text_patterns || []
  );
  if (offers.length >= 1 || offerHeading) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "offer_block",
      order,
      heading_text: offerHeading?.text || offers[0]?.text || null,
      content_summary: summarizeRegion(
        offers.map((o) => o.text).join("; "),
        summaryMax
      ),
      detection_method: offers.length ? "snapshot_field_map" : "heading_heuristic",
      evidence: makeEvidence(snapshot, {
        snapshot_field: offers.length ? "/offers" : offerHeading ? `/headings/${offerHeading.order}` : null,
        verbatim_text: offerHeading?.text || offers[0]?.text || null,
      }),
    });
    order += 1;
    seq += 1;
  }

  const pricingSignals = snapshot.pricing_signals || [];
  const pricingHeading = findHeadingByPatterns(
    headings,
    blockConfig.pricing_block?.rules?.heading_text_patterns || []
  );
  if (pricingSignals.length >= 1 || pricingHeading) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "pricing_block",
      order,
      heading_text: pricingHeading?.text || null,
      content_summary: summarizeRegion(
        pricingSignals.map((p) => p.text).join("; "),
        summaryMax
      ),
      detection_method: pricingSignals.length ? "snapshot_field_map" : "heading_heuristic",
      evidence: makeEvidence(snapshot, {
        snapshot_field: pricingSignals.length ? "/pricing_signals" : null,
        verbatim_text: pricingSignals[0]?.text || pricingHeading?.text || null,
      }),
    });
    order += 1;
    seq += 1;
  }

  const faqHeading = findHeadingByPatterns(
    headings,
    blockConfig.faq?.rules?.heading_patterns || []
  );
  if (faqHeading || /faq|вопрос|ответ/i.test(html)) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "faq",
      order,
      heading_text: faqHeading?.text || "FAQ section (pattern)",
      content_summary: null,
      detection_method: faqHeading ? "heading_heuristic" : "dom_landmark",
      evidence: makeEvidence(snapshot, {
        source: faqHeading ? "website_snapshot" : "page_html",
        snapshot_field: faqHeading ? `/headings/${faqHeading.order}` : null,
        verbatim_text: faqHeading?.text || null,
      }),
    });
    order += 1;
    seq += 1;
  }

  const reviewHeading = findHeadingByPatterns(
    headings,
    blockConfig.reviews?.rules?.heading_patterns || []
  );
  const reviewBodyHit = (blockConfig.reviews?.rules?.body_patterns || []).some((p) =>
    stripTags(html).toLowerCase().includes(p.toLowerCase())
  );
  if (reviewHeading || reviewBodyHit) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "reviews",
      order,
      heading_text: reviewHeading?.text || null,
      content_summary: null,
      detection_method: reviewHeading ? "heading_heuristic" : "dom_landmark",
      evidence: makeEvidence(snapshot, {
        source: reviewHeading ? "website_snapshot" : "page_html",
        verbatim_text: reviewHeading?.text || "review markers in body",
      }),
    });
    order += 1;
    seq += 1;
  }

  const contacts = snapshot.contacts || {};
  const hasContactData =
    (contacts.phones?.length || 0) +
      (contacts.emails?.length || 0) +
      (contacts.addresses?.length || 0) >
    0;
  const contactHeading = findHeadingByPatterns(
    headings,
    blockConfig.contacts?.rules?.heading_patterns || []
  );
  if (hasContactData || contactHeading) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "contacts",
      order,
      heading_text: contactHeading?.text || null,
      content_summary: summarizeRegion(
        [
          ...(contacts.phones || []),
          ...(contacts.emails || []),
          ...(contacts.addresses || []),
        ].join("; "),
        summaryMax
      ),
      detection_method: "snapshot_field_map",
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/contacts",
        verbatim_text: contactHeading?.text || contacts.phones?.[0] || null,
      }),
    });
    order += 1;
    seq += 1;
  }

  const forms = snapshot.forms || [];
  const leadForms = forms.filter((f) => (f.fields || []).length >= 2);
  if (leadForms.length >= 1) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "lead_form",
      order,
      heading_text: leadForms[0].visible_purpose || null,
      content_summary: `${leadForms[0].fields.length} fields`,
      detection_method: "snapshot_field_map",
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/forms/0",
        verbatim_text: leadForms[0].visible_purpose || null,
      }),
    });
    order += 1;
    seq += 1;
  }

  const messengers = contacts.messengers || [];
  const messengerHref =
    (snapshot.cta_elements || []).some((c) =>
      /t\.me|wa\.me|viber:\/\//i.test(c.href || "")
    ) || messengers.length > 0;
  if (messengerHref) {
    blocks.push({
      block_id: blockIdFor(landingId, seq),
      block_type: "messenger_cta",
      order,
      heading_text: messengers[0] ? `${messengers[0].type}: ${messengers[0].handle}` : null,
      content_summary: null,
      detection_method: "snapshot_field_map",
      evidence: makeEvidence(snapshot, {
        snapshot_field: messengers.length ? "/contacts/messengers" : "/cta_elements",
        verbatim_text: messengers[0]?.handle || null,
      }),
    });
    order += 1;
    seq += 1;
  }

  return { visible_blocks: blocks, safe_unknown: safeUnknown };
}

module.exports = { detectBlocks };
