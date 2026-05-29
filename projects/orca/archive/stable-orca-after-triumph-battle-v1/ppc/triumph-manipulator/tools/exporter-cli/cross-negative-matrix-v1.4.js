"use strict";

/**
 * Route-family cross-negative matrix v1.4 — Commander-compatible syntax.
 * Wildcard stems expanded to explicit word forms; no * in export.
 * NOT automated negative mining — deterministic export aid only.
 */

const {
  GROUP_ID_TO_ROUTE,
  FORBIDDEN_GLOBAL_TOKENS,
  LEGACY_NEGATIVE_PATTERNS,
  routeSlugFromGroupId,
  dedupeTokens,
} = require("./cross-negative-matrix-v1.3");

/** Commander minus-phrase allowed charset (letters, digits, space, + - ( ) " [] Cyrillic). */
const COMMANDER_NEGATIVE_FORBIDDEN_RE = /[*?[\]{}|\\^$@#%&=<>~`]/;

/**
 * Template SoT phrase-level route discriminators (triumph-manipulator-commander-template-v1.xlsx).
 * Full phrases — no wildcards.
 */
const ROUTE_NEGATIVE_PHRASES = Object.freeze({
  bytovki: ["перевозка бытовок", "доставка бытовок"],
  konteynery: ["перевозка контейнеров", "доставка контейнеров"],
  stroymaterialy: ["доставка стройматериалов", "стройматериалы"],
  oborudovanie: ["перевозка оборудования", "доставка оборудования"],
  armatura: ["перевозка арматуры", "доставка арматуры"],
  "kirpich-bloki": ["доставка кирпича", "доставка блоков"],
  "fbs-zhbi": ["фбс", "жби"],
  vezdehod: ["вездеход", "6х6", "6x6"],
  yurlic: ["юрлица", "безнал", "документы"],
  kray: ["межгород"],
  "5-tonn": [],
  zakaz: [],
});

/** Stem expansions for legacy v1.3 wildcard tokens — explicit Commander-safe forms. */
const WILDCARD_STEM_EXPANSIONS = Object.freeze({
  бытовк: ["бытовка", "бытовки", "бытовку", "бытовок"],
  контейнер: ["контейнер", "контейнера", "контейнеров", "контейнеры"],
  стройматериал: ["стройматериал", "стройматериалы", "стройматериалов"],
  оборудован: ["оборудование", "оборудования"],
  арматур: ["арматура", "арматуры", "арматуру"],
  кирпич: ["кирпич", "кирпича", "кирпичи"],
  блок: ["блок", "блока", "блоки", "блоков"],
  юрлиц: ["юрлиц", "юрлица"],
  документ: ["документы", "документов"],
});

/** Cross-route stem tokens (v1.3 matrix) — expanded at export, never exported with *. */
const ROUTE_NEGATIVE_STEMS = Object.freeze({
  "5-tonn": [],
  bytovki: ["бытовк"],
  konteynery: ["контейнер"],
  stroymaterialy: ["стройматериал"],
  oborudovanie: ["оборудован"],
  armatura: ["арматур"],
  "kirpich-bloki": ["кирпич", "блок"],
  "fbs-zhbi": ["фбс", "жби"],
  vezdehod: ["вездеход", "6х6", "6x6"],
  yurlic: ["юрлиц", "безнал", "документ"],
  kray: ["межгород"],
  zakaz: [],
});

const HOT_GROUP_EXTRA_STEMS = Object.freeze([
  "бытовк",
  "контейнер",
  "арматур",
  "кирпич",
  "блок",
  "фбс",
  "жби",
  "оборудован",
  "вездеход",
  "6х6",
  "6x6",
  "юрлиц",
  "безнал",
  "документ",
  "межгород",
]);

function normalizeToken(token) {
  return String(token ?? "")
    .trim()
    .toLowerCase()
    .replace(/\s+/g, " ");
}

function isCommanderNegativeSyntaxValid(token) {
  const t = String(token ?? "").trim();
  if (!t) return false;
  const body = t.startsWith("-") ? t.slice(1) : t;
  if (!body) return false;
  return !COMMANDER_NEGATIVE_FORBIDDEN_RE.test(body);
}

/**
 * Expand v1.3 wildcard token (e.g. бытовк*) to explicit word forms.
 * Plain tokens pass through unchanged.
 */
function expandNegativeToken(raw) {
  const word = String(raw ?? "").trim();
  if (!word) return [];

  if (word.endsWith("*")) {
    const stem = normalizeToken(word.slice(0, -1));
    if (WILDCARD_STEM_EXPANSIONS[stem]) {
      return WILDCARD_STEM_EXPANSIONS[stem];
    }
    if (stem) return [stem];
    return [];
  }

  const normalized = normalizeToken(word);
  if (WILDCARD_STEM_EXPANSIONS[normalized]) {
    return WILDCARD_STEM_EXPANSIONS[normalized];
  }
  return [word.trim()];
}

function expandStemList(stems) {
  const out = [];
  for (const stem of stems) {
    const key = normalizeToken(stem);
    if (WILDCARD_STEM_EXPANSIONS[key]) {
      out.push(...WILDCARD_STEM_EXPANSIONS[key]);
    } else if (key) {
      out.push(stem.trim());
    }
  }
  return out;
}

function mergeNegativeCandidates(...lists) {
  const flat = lists.flat();
  const expanded = [];
  for (const item of flat) {
    expanded.push(...expandNegativeToken(item));
  }
  return dedupeTokens(expanded);
}

/**
 * Cross-negatives for a group: doctrine JSON + route phrases + expanded stems.
 */
function buildCrossNegativesForGroup(groupId, doctrineNegatives = []) {
  const route = routeSlugFromGroupId(groupId);
  const cross = [];

  if (route === "5-tonn" || route === "zakaz") {
    cross.push(...expandStemList(HOT_GROUP_EXTRA_STEMS));
  }

  for (const [slug, phrases] of Object.entries(ROUTE_NEGATIVE_PHRASES)) {
    if (slug === route) continue;
    cross.push(...phrases);
  }

  for (const [slug, stems] of Object.entries(ROUTE_NEGATIVE_STEMS)) {
    if (slug === route) continue;
    cross.push(...expandStemList(stems));
  }

  const merged = mergeNegativeCandidates(doctrineNegatives, cross);
  return merged.filter(
    (t) =>
      !LEGACY_NEGATIVE_PATTERNS.some((re) => re.test(t)) &&
      isCommanderNegativeSyntaxValid(t.startsWith("-") ? t : `-${t}`)
  );
}

function formatNegativesForCommander(keywords) {
  if (!Array.isArray(keywords) || !keywords.length) return "";
  const parts = [];
  for (const k of keywords) {
    const raw = String(typeof k === "string" ? k : k.phrase || k.keyword || "").trim();
    if (!raw) continue;
    for (const expanded of expandNegativeToken(raw)) {
      const word = expanded.trim();
      if (!word) continue;
      const formatted = word.startsWith("-") ? word : `-${word}`;
      if (!isCommanderNegativeSyntaxValid(formatted)) continue;
      if (FORBIDDEN_GLOBAL_TOKENS.includes(normalizeToken(word.replace(/^-/, "")))) continue;
      parts.push(formatted);
    }
  }
  const seen = new Set();
  const out = [];
  for (const p of parts) {
    const key = normalizeToken(p.replace(/^-/, ""));
    if (seen.has(key)) continue;
    seen.add(key);
    out.push(p);
  }
  return out.join(" ");
}

function validateNegativesCell(cellValue) {
  const text = String(cellValue ?? "").trim();
  if (!text) return { ok: true, invalid: [] };
  const tokens = text.split(/\s+/).filter(Boolean);
  const invalid = tokens.filter((t) => !isCommanderNegativeSyntaxValid(t));
  return { ok: invalid.length === 0, invalid };
}

module.exports = {
  GROUP_ID_TO_ROUTE,
  ROUTE_NEGATIVE_PHRASES,
  ROUTE_NEGATIVE_STEMS,
  WILDCARD_STEM_EXPANSIONS,
  HOT_GROUP_EXTRA_STEMS,
  COMMANDER_NEGATIVE_FORBIDDEN_RE,
  FORBIDDEN_GLOBAL_TOKENS,
  LEGACY_NEGATIVE_PATTERNS,
  routeSlugFromGroupId,
  buildCrossNegativesForGroup,
  formatNegativesForCommander,
  expandNegativeToken,
  expandStemList,
  isCommanderNegativeSyntaxValid,
  validateNegativesCell,
  dedupeTokens,
};
