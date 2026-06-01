"use strict";

const { offerIdFor, makeEvidence, uniqueByKey } = require("./utils");

function findBlockByType(blocks, blockType) {
  return blocks.find((b) => b.block_type === blockType) || null;
}

function offerSurfaceFromContext(context) {
  if (!context) {
    return "unknown";
  }
  if (/^h[1-3]$/i.test(context)) {
    return "heading";
  }
  if (context === "list_item") {
    return "list_item";
  }
  if (context === "button" || context === "button_label") {
    return "button_label";
  }
  return "unknown";
}

/**
 * Extract visible offer observations (no ranking).
 */
function extractOffers(snapshot, options = {}) {
  const landingId = options.landing_id;
  const blocks = options.visible_blocks || [];
  const offerBlock = findBlockByType(blocks, "offer_block");
  const pricingBlock = findBlockByType(blocks, "pricing_block");
  const offers = [];
  let seq = 1;
  const seen = new Set();

  function pushOffer(text, surface, snapshotField, pricingRef) {
    const key = text.toLowerCase().trim();
    if (!text || seen.has(key)) {
      return;
    }
    seen.add(key);
    offers.push({
      offer_id: offerIdFor(landingId, seq),
      text,
      offer_surface: surface,
      block_id: offerBlock?.block_id || null,
      pricing_ref: pricingRef || null,
      ambiguity: "none",
      evidence: makeEvidence(snapshot, {
        snapshot_field: snapshotField,
        verbatim_text: text,
      }),
    });
    seq += 1;
  }

  (snapshot.offers || []).forEach((o, idx) => {
    pushOffer(o.text, offerSurfaceFromContext(o.context), `/offers/${idx}`, null);
  });

  const h2h3 = (snapshot.headings || []).filter((h) => h.level >= 2 && h.level <= 3);
  for (const h of h2h3) {
    if (offerBlock || h.level === 3) {
      pushOffer(h.text, "heading", `/headings/${h.order}`, null);
    }
  }

  if (!offers.length && (snapshot.pricing_signals || []).length) {
    const pr = snapshot.pricing_signals[0];
    pushOffer(
      pr.text,
      "unknown",
      "/pricing_signals/0",
      pricingBlock ? `${landingId}-pr001` : null
    );
  }

  return uniqueByKey(offers, (o) => o.text.toLowerCase());
}

module.exports = { extractOffers };
