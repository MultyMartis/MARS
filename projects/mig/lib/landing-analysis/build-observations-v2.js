"use strict";

const { filterOfferCandidates } = require("./nav-noise-filter");
const {
  classifyOfferCategory,
  hasDeliveryTimeTokens,
  hasPriceTokens,
  hasServiceCoverageTokens,
} = require("./offer-category");
const {
  classifyTrustSubtypeV2,
  splitTrustLines,
  detectPlatform,
  parseRatingNumbers,
  MAX_TRUST_LINE_CHARS,
} = require("./trust-subtype-v2");

function observationIdFor(landingId, seq) {
  return `${landingId}-obs${String(seq).padStart(3, "0")}`;
}

function evidenceGradeFromEvidence(evidence) {
  if (!evidence || !evidence.verbatim_text) {
    return "X";
  }
  if (evidence.source === "manual_annotation") {
    return "A";
  }
  if (evidence.source === "website_snapshot" && evidence.snapshot_field) {
    return "B";
  }
  if (evidence.source === "page_html") {
    return "C";
  }
  return "C";
}

function enrichEvidence(snapshot, evidence) {
  return {
    ...evidence,
    snapshot_id: evidence.snapshot_id || snapshot.snapshot_id,
  };
}

function dedupeKey(family, text) {
  return `${family}:${(text || "").toLowerCase().trim()}`;
}

/**
 * Build family-tagged observations[] from v1 extractor outputs (rules-only).
 */
function buildObservationsV2(detail, snapshot, options = {}) {
  const landingId = detail.landing_id;
  const observations = [];
  const excludedOffers = [];
  const seen = new Set();
  let seq = 1;

  function pushObservation(row) {
    const key = dedupeKey(row.family, row.text);
    if (!row.text || seen.has(key)) {
      return;
    }
    seen.add(key);
    const id = row.observation_id || observationIdFor(landingId, seq);
    seq += 1;
    const evidence = enrichEvidence(snapshot, row.evidence);
    observations.push({
      observation_id: id,
      family: row.family,
      text: row.text.length > 500 ? row.text.slice(0, 500) : row.text,
      sub_type: row.sub_type || undefined,
      category: row.category || undefined,
      offer_surface: row.offer_surface || undefined,
      block_id: row.block_id || undefined,
      platform: row.platform || undefined,
      numeric_value: row.numeric_value ?? undefined,
      numeric_secondary: row.numeric_secondary ?? undefined,
      numeric_unit: row.numeric_unit || undefined,
      confidence: row.confidence || evidenceGradeFromEvidence(evidence),
      ambiguity: row.ambiguity || "none",
      evidence,
      excluded_reason: row.excluded_reason || undefined,
      status: row.status || undefined,
      reason: row.reason || undefined,
    });
  }

  const offerCandidates = (detail.offers || []).map((o) => ({
    text: o.text,
    snapshot_field: o.evidence?.snapshot_field,
    offer_surface: o.offer_surface,
    block_id: o.block_id,
    evidence: o.evidence,
    pricing_ref: o.pricing_ref,
  }));

  const { kept: filteredOffers, excluded } = filterOfferCandidates(offerCandidates, {
    configPath: options.navNoiseConfigPath,
  });
  excludedOffers.push(...excluded);

  for (const offer of filteredOffers) {
    const text = offer.text;
    if (hasPriceTokens(text)) {
      pushObservation({
        family: "PRICING",
        text,
        sub_type: "visible_price_line",
        block_id: offer.block_id,
        evidence: offer.evidence,
      });
      continue;
    }
    if (hasDeliveryTimeTokens(text)) {
      pushObservation({
        family: "DELIVERY_PROMISE",
        text,
        sub_type: "time_promise",
        block_id: offer.block_id,
        evidence: offer.evidence,
      });
      continue;
    }
    if (hasServiceCoverageTokens(text) && classifyOfferCategory(text) === "scope") {
      pushObservation({
        family: "SERVICE_COVERAGE",
        text,
        sub_type: "scope_line",
        block_id: offer.block_id,
        evidence: offer.evidence,
      });
      continue;
    }
    pushObservation({
      family: "OFFERS",
      text,
      category: classifyOfferCategory(text),
      offer_surface: offer.offer_surface,
      block_id: offer.block_id,
      evidence: offer.evidence,
    });
  }

  for (const pricing of detail.pricing_patterns || []) {
    pushObservation({
      family: "PRICING",
      text: pricing.text,
      sub_type: pricing.currency_hint ? "priced_line" : "price_blob",
      block_id: pricing.block_id,
      evidence: pricing.evidence,
    });
  }

  for (const cta of detail.cta_patterns || []) {
    const label = cta.label_text || "CTA";
    pushObservation({
      family: "CTA",
      text: cta.target_href ? `${label} → ${cta.target_href}` : label,
      sub_type: cta.cta_type,
      block_id: cta.block_id,
      evidence: cta.evidence,
    });
  }

  for (const form of detail.form_patterns || []) {
    const fields = (form.fields || []).map((f) => f.name || f.type).filter(Boolean);
    const text =
      form.visible_purpose ||
      (fields.length ? `Form: ${fields.slice(0, 6).join(", ")}` : "Lead form visible");
    pushObservation({
      family: "LEAD_CAPTURE",
      text,
      sub_type: "lead_form",
      block_id: form.block_id,
      evidence: form.evidence,
    });
  }

  for (const contact of detail.contact_patterns || []) {
    pushObservation({
      family: "CONTACT_MODEL",
      text: `${contact.contact_type}: ${contact.value}`,
      sub_type: contact.contact_type,
      block_id: contact.block_id,
      evidence: contact.evidence,
    });
  }

  const registry = options.registry || {};
  for (const trust of detail.trust_patterns || []) {
    const lines =
      trust.text && trust.text.length > MAX_TRUST_LINE_CHARS
        ? splitTrustLines(trust.text)
        : [trust.text];

    for (const line of lines) {
      if (!line) {
        continue;
      }
      const subType = classifyTrustSubtypeV2(line, registry) || trust.trust_type;
      if (!subType || subType === "statistics") {
        continue;
      }
      const platform = detectPlatform(line);
      const nums = parseRatingNumbers(line);
      const family =
        (subType === "rating_display" || subType === "review_snippet") && platform
          ? "SOCIAL_PROOF"
          : "TRUST";

      pushObservation({
        family,
        text: line,
        sub_type: subType,
        platform: platform || undefined,
        numeric_value: nums.numeric_value ?? trust.numeric_value ?? undefined,
        numeric_secondary: nums.numeric_secondary ?? undefined,
        numeric_unit: nums.numeric_unit || undefined,
        block_id: trust.block_id,
        evidence: trust.evidence,
      });
    }
  }

  for (const pattern of detail.page_patterns || []) {
    const tag = pattern.pattern_id;
    if (!tag) {
      continue;
    }
    pushObservation({
      family: "MARKETING_PATTERNS",
      text: pattern.evidence?.verbatim_text || tag,
      sub_type: tag,
      evidence: pattern.evidence,
      confidence: "C",
    });
  }

  const familiesPresent = [...new Set(observations.map((o) => o.family))];
  const allFamilies = [
    "OFFERS",
    "PRICING",
    "CTA",
    "TRUST",
    "LEAD_CAPTURE",
    "SOCIAL_PROOF",
    "CONTACT_MODEL",
    "DELIVERY_PROMISE",
    "SERVICE_COVERAGE",
    "MARKETING_PATTERNS",
  ];
  const familiesUnknown = allFamilies.filter((f) => !familiesPresent.includes(f));

  if (!observations.some((o) => o.family === "OFFERS") && filteredOffers.length === 0) {
    if (excluded.length > 0 && !(detail.offers || []).some((o) => !hasPriceTokens(o.text))) {
      pushObservation({
        family: "OFFERS",
        status: "safe_unknown",
        reason: "no_marketing_offer_strings_after_nav_filter",
        text: "SAFE UNKNOWN — no classified offers after nav filter",
        confidence: "X",
        evidence: enrichEvidence(snapshot, {
          source: "website_snapshot",
          snapshot_field: null,
          verbatim_text: null,
        }),
      });
    } else if ((detail.offers || []).length === 0) {
      pushObservation({
        family: "OFFERS",
        status: "safe_unknown",
        reason: "no_marketing_offer_strings_after_nav_filter",
        text: "SAFE UNKNOWN — no offer strings in snapshot",
        confidence: "X",
        evidence: enrichEvidence(snapshot, {
          source: "website_snapshot",
          snapshot_field: null,
          verbatim_text: null,
        }),
      });
    }
  }

  const topSignals = observations
    .filter((o) => o.status !== "safe_unknown" && o.text && !o.text.startsWith("SAFE UNKNOWN"))
    .slice(0, 5)
    .map((o) => ({
      family: o.family,
      text: o.text.length > 120 ? `${o.text.slice(0, 117)}…` : o.text,
      observation_id: o.observation_id,
      confidence: o.confidence,
    }));

  return {
    observations,
    observation_summary: {
      families_present: familiesPresent,
      families_unknown: familiesUnknown,
      top_signals: topSignals,
    },
    _processing: {
      excluded_offers: excludedOffers,
    },
  };
}

module.exports = {
  observationIdFor,
  evidenceGradeFromEvidence,
  buildObservationsV2,
};
