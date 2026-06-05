"use strict";

/**
 * Evidence-backed phone presence and contact model (no raw competitor numbers in intelligence layer).
 */

function countByType(items, type) {
  return (items || []).filter((i) => i === type || i?.contact_type === type || i?.cta_type === type).length;
}

function hasPattern(pagePatterns, patternId) {
  return (pagePatterns || []).some(
    (p) => p.pattern_id === patternId || p.sub_type === patternId
  );
}

/**
 * Derive contact model enum from captured page structure.
 * @returns {{ phone_present: boolean, phone_prominent: boolean, contact_model: string, evidence: object[] }}
 */
function derivePhonePresenceModel(snapshot, detail = {}) {
  const phones = snapshot.contacts?.phones || [];
  const messengers = snapshot.contacts?.messengers || [];
  const emails = snapshot.contacts?.emails || [];
  const forms = snapshot.forms || [];
  const ctaPatterns = detail.cta_patterns || [];
  const pagePatterns = detail.page_patterns || [];
  const offers = snapshot.offers || [];

  const phone_present = phones.length > 0;
  const phone_prominent =
    phone_present &&
    (hasPattern(pagePatterns, "phone_prominent") ||
      ctaPatterns.some((c) => c.cta_type === "phone" && c.position_band === "header"));

  const phoneCtaCount = countByType(ctaPatterns, "phone");
  const messengerCtaCount = countByType(ctaPatterns, "messenger");
  const formCount = forms.filter((f) => (f.fields || []).length >= 2).length;
  const appSignals = offers.some((o) =>
    /(?:app\s*store|google\s*play|скачать\s+прилож|мобильн(?:ое|ого)\s+прилож)/i.test(o.text || "")
  );
  const hasAppPattern = hasPattern(pagePatterns, "app_first_order");

  const signals = [];
  if (phoneCtaCount > 0 || phone_prominent) {
    signals.push("phone");
  }
  if (formCount > 0) {
    signals.push("form");
  }
  if (appSignals || hasAppPattern) {
    signals.push("app");
  }
  if (messengers.length > 0 || messengerCtaCount > 0) {
    signals.push("messenger");
  }
  if (emails.length > 0) {
    signals.push("email");
  }

  let contact_model = "mixed";
  if (signals.length === 1) {
    const map = { phone: "phone_first", form: "form_first", app: "app_first", messenger: "messenger_first" };
    contact_model = map[signals[0]] || "mixed";
  } else if (signals.length === 0) {
    contact_model = "SAFE UNKNOWN";
  } else if (signals[0] === "phone" && signals.length === 2 && signals[1] === "form") {
    contact_model = "phone_first";
  }

  const evidence = [];
  if (phone_present) {
    evidence.push({
      signal: "phone_present",
      snapshot_field: "/contacts/phones",
      count: phones.length,
    });
  }
  if (phone_prominent) {
    evidence.push({
      signal: "phone_prominent",
      snapshot_field: hasPattern(pagePatterns, "phone_prominent")
        ? "/page_patterns/phone_prominent"
        : "/contacts/phones",
    });
  }

  return {
    phone_present,
    phone_prominent,
    contact_model,
    evidence,
  };
}

function formatPhonePresenceSummary(model) {
  if (!model) {
    return "SAFE UNKNOWN";
  }
  const parts = [
    `phone_present: ${model.phone_present}`,
    `phone_prominent: ${model.phone_prominent}`,
    `contact_model: ${model.contact_model}`,
  ];
  return parts.join("; ");
}

module.exports = {
  derivePhonePresenceModel,
  formatPhonePresenceSummary,
};
