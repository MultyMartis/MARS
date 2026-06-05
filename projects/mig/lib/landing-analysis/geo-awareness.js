"use strict";

/**
 * Detect visible geo mismatch signals (rules-only, evidence-backed).
 */

const CITY_LEXICON = [
  { key: "краснодар", forms: ["краснодар", "краснодаре", "краснодара", "краснодарский", "краснодарском"] },
  { key: "пенза", forms: ["пенза", "пензе", "пензы", "пенzen", "пензенск"] },
  { key: "москва", forms: ["москва", "москве", "москвы", "московск"] },
  { key: "санкт-петербург", forms: ["санкт-петербург", "петербург", "спб", "ленинград"] },
];

function normalizeTarget(scope = {}) {
  const raw = (scope.city || scope.region || "").toLowerCase().trim();
  if (!raw) {
    return null;
  }
  for (const entry of CITY_LEXICON) {
    if (entry.key === raw || entry.forms.some((f) => raw.includes(f))) {
      return entry.key;
    }
  }
  return raw;
}

function findCityMentions(text) {
  if (!text) {
    return [];
  }
  const lower = text.toLowerCase();
  const found = [];
  for (const entry of CITY_LEXICON) {
    for (const form of entry.forms) {
      if (lower.includes(form)) {
        found.push({ city_key: entry.key, matched_form: form });
        break;
      }
    }
  }
  return found;
}

function collectVisibleTexts(snapshot) {
  const rows = [];
  const push = (text, snapshot_field) => {
    if (text && String(text).trim()) {
      rows.push({ text: String(text).trim(), snapshot_field });
    }
  };

  push(snapshot.title, "/title");
  push(snapshot.meta_description, "/meta_description");
  for (let i = 0; i < (snapshot.headings || []).length; i += 1) {
    const h = snapshot.headings[i];
    push(h.text || h, `/headings/${i}`);
  }
  for (let i = 0; i < (snapshot.offers || []).length; i += 1) {
    push(snapshot.offers[i].text, `/offers/${i}`);
  }

  return rows;
}

/**
 * @returns {Array<{ family, sub_type, text, observed_city, research_target, evidence }>}
 */
function detectGeoMismatchSignals(snapshot, scope = {}) {
  const targetKey = normalizeTarget(scope);
  if (!targetKey) {
    return [];
  }

  const observations = [];
  const seen = new Set();

  for (const row of collectVisibleTexts(snapshot)) {
    const mentions = findCityMentions(row.text);
    for (const mention of mentions) {
      if (mention.city_key === targetKey) {
        continue;
      }
      const dedupeKey = `${mention.city_key}:${row.snapshot_field}`;
      if (seen.has(dedupeKey)) {
        continue;
      }
      seen.add(dedupeKey);

      const targetLabel = scope.city || scope.region || targetKey;
      observations.push({
        family: "GEO_AWARENESS",
        sub_type: "geo_mismatch",
        text: `research_target: ${targetLabel}; observed: ${mention.matched_form}`,
        observed_city: mention.city_key,
        research_target: targetLabel,
        evidence: {
          source: "website_snapshot",
          snapshot_field: row.snapshot_field,
          verbatim_text: row.text,
        },
      });
    }
  }

  return observations;
}

module.exports = {
  normalizeTarget,
  findCityMentions,
  detectGeoMismatchSignals,
};
