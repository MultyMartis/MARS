"use strict";

const { ctaIdFor, makeEvidence, uniqueByKey } = require("./utils");

function classifyCtaElement(cta, registry) {
  const href = (cta.href || "").toLowerCase();
  const text = (cta.text || "").toLowerCase();
  const ctaClass = registry.cta_classification || {};

  if (href.startsWith("tel:")) {
    return "phone";
  }
  if (
    (ctaClass.messenger_href || []).some((p) => href.includes(p.replace(/\\/g, ""))) ||
    /t\.me|wa\.me|viber:\/\//i.test(href)
  ) {
    return "messenger";
  }
  if (href.startsWith("#")) {
    return "anchor_scroll";
  }
  if ((ctaClass.callback_request || []).some((p) => text.includes(p.toLowerCase()))) {
    return "callback_request";
  }
  if (href && /^https?:\/\//i.test(href)) {
    return "external_link";
  }
  return "generic_action";
}

function findBlockForType(blocks, types) {
  const set = new Set(types);
  return blocks.find((b) => set.has(b.block_type)) || null;
}

/**
 * Extract typed CTA patterns (no ranking).
 */
function extractCtaPatterns(snapshot, options = {}) {
  const landingId = options.landing_id;
  const blocks = options.visible_blocks || [];
  const formPatterns = options.form_patterns || [];
  const registry = options.registry || {};
  const ctas = [];
  let seq = 1;

  for (const form of formPatterns) {
    ctas.push({
      cta_id: ctaIdFor(landingId, seq),
      cta_type: "lead_form",
      label_text: form.visible_purpose || "Lead form",
      target_href: form.action || null,
      element_type: "input",
      position_band: "body",
      form_id: form.form_id,
      block_id: findBlockForType(blocks, ["lead_form"])?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: `/forms`,
        verbatim_text: form.visible_purpose || "form",
      }),
    });
    seq += 1;
  }

  for (const phone of snapshot.contacts?.phones || []) {
    ctas.push({
      cta_id: ctaIdFor(landingId, seq),
      cta_type: "phone",
      label_text: phone,
      target_href: `tel:${phone.replace(/\s/g, "")}`,
      element_type: "link",
      position_band: "header",
      form_id: null,
      block_id: findBlockForType(blocks, ["contacts", "hero"])?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/contacts/phones",
        verbatim_text: phone,
      }),
    });
    seq += 1;
  }

  for (const msg of snapshot.contacts?.messengers || []) {
    ctas.push({
      cta_id: ctaIdFor(landingId, seq),
      cta_type: "messenger",
      label_text: `${msg.type}: ${msg.handle}`,
      target_href: null,
      element_type: "link",
      position_band: "footer",
      form_id: null,
      block_id: findBlockForType(blocks, ["messenger_cta"])?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: "/contacts/messengers",
        verbatim_text: msg.handle,
      }),
    });
    seq += 1;
  }

  for (let i = 0; i < (snapshot.cta_elements || []).length; i += 1) {
    const cta = snapshot.cta_elements[i];
    const ctaType = classifyCtaElement(cta, registry);
    ctas.push({
      cta_id: ctaIdFor(landingId, seq),
      cta_type: ctaType,
      label_text: cta.text,
      target_href: cta.href || null,
      element_type: cta.element_type || "link",
      position_band: cta.position_hint || "unknown",
      form_id: null,
      block_id: findBlockForType(blocks, ["hero", "offer_block"])?.block_id || null,
      evidence: makeEvidence(snapshot, {
        snapshot_field: `/cta_elements/${i}`,
        verbatim_text: cta.text,
      }),
    });
    seq += 1;
  }

  return uniqueByKey(ctas, (c) => `${c.cta_type}:${c.label_text}:${c.target_href || ""}`);
}

module.exports = { extractCtaPatterns, classifyCtaElement };
