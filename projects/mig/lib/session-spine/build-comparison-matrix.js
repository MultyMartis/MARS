"use strict";

const { obsByFamilies } = require("./format-landing-intelligence-v2");

const MATRIX_CAPS = {
  primary_offer: 3,
  pricing_signals: 4,
  delivery_promise: 2,
  trust_signals: 4,
  lead_capture_model: 3,
};

function joinOrUnknown(items) {
  if (!Array.isArray(items) || items.length === 0) {
    return "SAFE UNKNOWN";
  }
  return items.join("; ");
}

function pickTexts(observations, families, cap) {
  return obsByFamilies(observations, families)
    .slice(0, cap)
    .map((o) => o.text)
    .filter(Boolean);
}

function pickPricingTexts(observations, cap) {
  const pricing = obsByFamilies(observations, ["PRICING"]);
  const pricedLines = pricing.filter((o) => o.sub_type === "priced_line" || o.sub_type === "visible_price_line");
  const chosen = (pricedLines.length ? pricedLines : pricing).slice(0, cap);
  return chosen.map((o) => o.text).filter(Boolean);
}

function formatMessenger(m) {
  if (typeof m === "string") {
    return m;
  }
  if (m && typeof m === "object") {
    const type = m.type || "msg";
    const handle = m.handle || m.url || "";
    return handle ? `${type}:${handle}` : type;
  }
  return String(m);
}

function formatContactModel(snap, observations) {
  const contacts = snap?.contacts || {};
  const parts = [];

  if (contacts.phones?.length) {
    parts.push(`phones: ${contacts.phones.slice(0, 2).join(", ")}`);
  }
  if (contacts.emails?.length) {
    parts.push(`emails: ${contacts.emails.slice(0, 1).join(", ")}`);
  }
  if (contacts.messengers?.length) {
    parts.push(`messengers: ${contacts.messengers.map(formatMessenger).slice(0, 2).join(", ")}`);
  }

  if (parts.length) {
    return parts.join("; ");
  }

  const contactObs = pickTexts(observations, ["CONTACT_MODEL"], 3);
  return contactObs.length ? contactObs.join("; ") : "SAFE UNKNOWN";
}

function formatLeadCapture(observations, snap) {
  const leadCapture = obsByFamilies(observations, ["LEAD_CAPTURE"]).filter(
    (o) => o.text && !o.text.startsWith("Form: _")
  );
  const ctaLead = obsByFamilies(observations, ["CTA"]).filter((o) =>
    ["lead_form", "callback_request", "external_link"].includes(o.sub_type)
  );
  const combined = [...leadCapture, ...ctaLead]
    .map((o) => o.text)
    .filter(Boolean);
  const unique = [...new Set(combined)].slice(0, MATRIX_CAPS.lead_capture_model);

  if (unique.length) {
    return unique.join("; ");
  }

  if (snap?.forms?.length) {
    return `form present (${snap.forms.length})`;
  }

  return "SAFE UNKNOWN";
}

function findDetailForLanding(landingIndex, landing) {
  const detail = landingIndex._detail || [];
  return detail.find((d) => d.landing_id === landing.landing_id) || null;
}

function fallbackFromTopSignals(obs, family, cap) {
  return (obs.top_signals || [])
    .filter((s) => s.family === family)
    .map((s) => s.text)
    .slice(0, cap);
}

function collectEvidenceRefs(detail, snap) {
  return [
    detail?.artifact_refs?.landing_observation ||
      (detail?.landing_id ? `landings/${detail.landing_id}/landing_observation.json` : null),
    snap?.artifact_refs?.website_snapshot,
    snap?.artifact_refs?.page_html,
  ]
    .filter(Boolean)
    .join(", ");
}

/**
 * Project landing observations into comparison-matrix rows.
 * Requires landingIndex enriched with _detail (see load-landing-detail.js).
 */
function buildComparisonMatrix(landingIndex, websiteIndex) {
  const rows = [];

  for (const landing of landingIndex.landings || []) {
    const snap = (websiteIndex.snapshots || []).find((s) => s.snapshot_id === landing.snapshot_id);
    const detail = findDetailForLanding(landingIndex, landing);
    const observations = detail?.observations || [];
    const obs = landing.observation_summary || {};

    let topOffers = pickTexts(observations, ["OFFERS"], MATRIX_CAPS.primary_offer);
    let pricing = pickPricingTexts(observations, MATRIX_CAPS.pricing_signals);
    let delivery = pickTexts(
      observations,
      ["DELIVERY_PROMISE", "SERVICE_COVERAGE"],
      MATRIX_CAPS.delivery_promise
    );
    let trust = pickTexts(observations, ["TRUST", "SOCIAL_PROOF"], MATRIX_CAPS.trust_signals);

    if (!observations.length) {
      topOffers = fallbackFromTopSignals(obs, "OFFERS", MATRIX_CAPS.primary_offer);
      pricing = fallbackFromTopSignals(obs, "PRICING", MATRIX_CAPS.pricing_signals);
      delivery = [
        ...fallbackFromTopSignals(obs, "DELIVERY_PROMISE", MATRIX_CAPS.delivery_promise),
        ...fallbackFromTopSignals(obs, "SERVICE_COVERAGE", MATRIX_CAPS.delivery_promise),
      ].slice(0, MATRIX_CAPS.delivery_promise);
      trust = [
        ...fallbackFromTopSignals(obs, "TRUST", MATRIX_CAPS.trust_signals),
        ...fallbackFromTopSignals(obs, "SOCIAL_PROOF", MATRIX_CAPS.trust_signals),
      ].slice(0, MATRIX_CAPS.trust_signals);
    }

    const pageStructure = (snap?.headings || [])
      .slice(0, 6)
      .map((h) => h.text || h)
      .join(" → ");

    rows.push({
      domain: landing.domain,
      primary_offer: joinOrUnknown(topOffers),
      pricing_signals: joinOrUnknown(pricing),
      delivery_promise: joinOrUnknown(delivery),
      trust_signals: joinOrUnknown(trust),
      lead_capture_model: formatLeadCapture(observations, snap),
      contact_model: formatContactModel(snap, observations),
      page_structure: pageStructure || "SAFE UNKNOWN",
      evidence_refs: collectEvidenceRefs(detail || landing, snap),
      families_present: (obs.families_present || []).join(", "),
      acquisition_status: snap?.status || "SAFE UNKNOWN",
    });
  }

  return rows;
}

function comparisonMatrixMarkdown(rows) {
  const headers = [
    "Domain",
    "Primary Offer",
    "Pricing Signals",
    "Delivery Promise",
    "Trust Signals",
    "Lead Capture Model",
    "Contact Model",
    "Page Structure",
    "Evidence References",
  ];
  const lines = [
    "# Market leader comparison matrix",
    "",
    "Facts only — no strategic conclusions.",
    "",
    "| " + headers.join(" | ") + " |",
    "| " + headers.map(() => "---").join(" | ") + " |",
    ...rows.map((r) =>
      "| " +
        [
          r.domain,
          r.primary_offer.replace(/\|/g, "\\|").slice(0, 120),
          r.pricing_signals.replace(/\|/g, "\\|").slice(0, 100),
          r.delivery_promise.replace(/\|/g, "\\|").slice(0, 80),
          r.trust_signals.replace(/\|/g, "\\|").slice(0, 80),
          r.lead_capture_model.replace(/\|/g, "\\|").slice(0, 80),
          r.contact_model.replace(/\|/g, "\\|").slice(0, 80),
          r.page_structure.replace(/\|/g, "\\|").slice(0, 100),
          r.evidence_refs,
        ].join(" | ") +
        " |"
    ),
    "",
  ];
  return lines.join("\n");
}

module.exports = {
  MATRIX_CAPS,
  buildComparisonMatrix,
  comparisonMatrixMarkdown,
};
