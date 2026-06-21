"use strict";

/**
 * Route-family cross-negative matrix v1.3 — Triumph Manipulator Search PPC.
 * Group-scoped discriminators; does not block own-route core terms.
 * NOT automated negative mining — deterministic export aid only.
 */

/** Route slug per group_id (12 groups). */
const GROUP_ID_TO_ROUTE = Object.freeze({
  grp_fc01_5ton: "5-tonn",
  grp_fc02_bytovka: "bytovki",
  grp_fc03_stroymaterialy: "stroymaterialy",
  grp_fc04_yurlica: "yurlic",
  grp_fc05_6x6: "vezdehod",
  grp_fc06_oborudovanie: "oborudovanie",
  grp_fc07_konteynery: "konteynery",
  grp_fc08_armatura: "armatura",
  grp_fc09_kirpich: "kirpich-bloki",
  grp_fc10_fbs: "fbs-zhbi",
  grp_fc11_kray: "kray",
  grp_fc12_zakaz: "zakaz",
});

/**
 * Route-specific negative tokens (applied to all groups EXCEPT that route).
 * No «манипулятор», no global «краснодар»/«край» — per calibration rules.
 */
const ROUTE_NEGATIVE_TOKENS = Object.freeze({
  "5-tonn": [],
  bytovki: ["бытовк*"],
  konteynery: ["контейнер*"],
  stroymaterialy: ["стройматериал*"],
  oborudovanie: ["оборудован*"],
  armatura: ["арматур*"],
  "kirpich-bloki": ["кирпич*", "блок*"],
  "fbs-zhbi": ["фбс", "жби"],
  vezdehod: ["вездеход", "6х6", "6x6"],
  yurlic: ["юрлиц*", "безнал", "документ*"],
  kray: ["межгород"],
  zakaz: [],
});

/** Extra cross-route tokens for capability / hot groups (5-tonn, zakaz). */
const HOT_GROUP_EXTRA_CROSS = Object.freeze([
  "бытовк*",
  "контейнер*",
  "арматур*",
  "кирпич*",
  "блок*",
  "фбс",
  "жби",
  "оборудован*",
  "вездеход",
  "6х6",
  "6x6",
  "юрлиц*",
  "безнал",
  "документ*",
  "межгород",
]);

const FORBIDDEN_GLOBAL_TOKENS = Object.freeze([
  "манипулятор",
  "манипулятор*",
  "краснодар",
  "краснодар*",
  "край",
  "край*",
  "грузотакси",
]);

const LEGACY_NEGATIVE_PATTERNS = [/грузотакси/i];

function normalizeToken(token) {
  return String(token ?? "")
    .trim()
    .toLowerCase()
    .replace(/\s+/g, " ");
}

function dedupeTokens(tokens) {
  const seen = new Set();
  const out = [];
  for (const raw of tokens) {
    const t = normalizeToken(raw);
    if (!t || seen.has(t)) continue;
    if (FORBIDDEN_GLOBAL_TOKENS.includes(t)) continue;
    seen.add(t);
    out.push(raw.trim());
  }
  return out;
}

function routeSlugFromGroupId(groupId) {
  return GROUP_ID_TO_ROUTE[groupId] || null;
}

/**
 * Cross-negatives for a group: sibling route tokens + JSON doctrine negatives.
 * @param {string} groupId
 * @param {string[]} doctrineNegatives — from JSON group_negatives.keywords
 */
function buildCrossNegativesForGroup(groupId, doctrineNegatives = []) {
  const route = routeSlugFromGroupId(groupId);
  const cross = [];

  if (route === "5-tonn" || route === "zakaz") {
    cross.push(...HOT_GROUP_EXTRA_CROSS);
  }

  for (const [slug, tokens] of Object.entries(ROUTE_NEGATIVE_TOKENS)) {
    if (slug === route) continue;
    cross.push(...tokens);
  }

  const merged = dedupeTokens([...doctrineNegatives, ...cross]);
  return merged.filter((t) => !LEGACY_NEGATIVE_PATTERNS.some((re) => re.test(t)));
}

function formatNegativesForCommander(keywords) {
  if (!Array.isArray(keywords) || !keywords.length) return "";
  return keywords
    .map((k) => {
      const word = String(typeof k === "string" ? k : k.phrase || k.keyword || "").trim();
      if (!word) return "";
      return word.startsWith("-") ? word : `-${word}`;
    })
    .filter(Boolean)
    .join(" ");
}

module.exports = {
  GROUP_ID_TO_ROUTE,
  ROUTE_NEGATIVE_TOKENS,
  HOT_GROUP_EXTRA_CROSS,
  FORBIDDEN_GLOBAL_TOKENS,
  LEGACY_NEGATIVE_PATTERNS,
  routeSlugFromGroupId,
  buildCrossNegativesForGroup,
  formatNegativesForCommander,
  dedupeTokens,
};
